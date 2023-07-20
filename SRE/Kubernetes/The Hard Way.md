v> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/)

## Prerequisites
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/01-prerequisites.md)

* VM Hardware Requirements
	* 8 GB of RAM (Preferebly 16 GB)
	* 50 GB Disk space
* Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://vagrantup.com/)
	* Versions used as writing this repo:
		* VirtualBox 7.0.6
		* Vagrant 2.3.7
* Take into consideration the info below is about the host system used for this repo:
	* Date: July 2023
	* VirtualBox 7.0.6
	* Vagrant 2.3.7
	* Ubuntu 22.10 x64 Kinetic host OS
	* Ubuntu 22.04 x64 Jammy guest OS
	* Host HW
		* 12 GB RAM
		* Intel® Core™ i7-7700HQ × 8

## Provisioning Compute Resources
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/02-compute-resources.md)
* At this point VirtualBox and Vagrant must have been installed.
* Download This repo and cd into the vagrant folder:
	* `git clone https://github.com/mrafee113/...`
	* `cd .../vagrant`
* Modify the VagrantFile to your needs:
	* `NUM_MASTER_NODE=2` : Number of master nodes to create
	* `NUM_WORKER_NODE=2` : Number of worker nodes to create
	* `IP_NW="192.168.56."` : The network ip on which the vagrant private network will be built on and static ips will be configured.
	* `MASTER_IP_START=10` : The static ips that master nodes will start at e.g. `192.168.56.10`
	* `NODE_IP_START=20` : The static ips that worker nodes will start at e.g. `192.168.56.20`
	* `PROVISION_DOCKER=false` : The boolean that determines whether the docker setup script `setup-docker.sh` should be provisioned or not.
		* This is set to false as default, because automatic installation of docker failed at the time of writing this, due to internet filtering.
	* `SYNC_FOLDER=true` : The boolean that determines whether a folder should be synced or not.
	* `SYNC_SRC="shared/"` : The host folder to sync with the guest system.
		* The target folder on the guest system is at `/media/vboxshared`, but you can change that too.
		* The Vagrant docs state that if a path is not absolute for sync source, it will be considered relative to the Vagrantfile base directory.
* Start the machines: `vagrant up`

### Default settings
* The dns nameserver added to `/etc/hosts` on each VM is `8.8.8.8`.
* Runs the below command on all nodes to allow for network forwarding in IP Tables. This is required for kubernetes networking to function correctly.
	* `sysctl net.bridge.bridge-nf-call-iptables=1

| VM | VM Name | Purpose | IP | Forwarded Port |
| :- | :- | :-: | :-: | :-: |
|master-1|kubernetes-ha-master-1|Master|192.168.5.11|2711|
|master-2|kubernetes-ha-master-2|Master|192.168.5.12|2712|
|worker-1|kubernetes-ha-worker-1|Worker|192.168.5.21|2730|
|worker-2|kubernetes-ha-worker-2|Worker|192.168.5.22|2721|
|lb|kubernetes-ha-lb|LoadBalancer|192.168.5.30|2722|

### Verify your environment
- Ensure all VMs are up
- Ensure VMs are assigned the above IP addresses
- Ensure you can SSH into these VMs using the IP and private keys
- Ensure the VMs can ping each other
- Ensure the worker nodes have Docker installed on them. Version: 18.06
	* `sudo docker version`
	* *Warning:* You may need to install docker manually.
		* Instruction to do so can be found at `vagrant/ubuntu/setup-docker.sh`
		* To escape the filtering you can set the "https_proxy" variable to point to a proxy server (nekoray in my case).

## Installing Client Tools
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/03-client-tools.md)
* The filtering on `dl.k8s.io` and `storage.googleapis.com` is very strict. At the time of writing this (Jul 1 2023), I had to connect using Windscribe, download on my local pc and transfer the binaries to the VM manually. Nothing else worked against the filtering.
* Install KubeCTL
	* The `kubectl` command line utility is used to interact with the Kubernetes API Server. Download and install `kubectl` from the official release binaries.
	* `KUBECTL_VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)`
	* `curl -L --output "kubectl_v$KUBECTL_VERSION_amd64" "https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl"`
	* `sudo chmod +x kubectl`
	* rename the file to plain `kubectl`
	* `sudo mv kubectl /usr/local/bin/`
		* or alternatively: `sudo install -o root -g root -m 0755 ./kubectl /usr/local/bin/kubectl`
	* verify: `kubectl version --short` or something like that. There's been a lot of deprecation going on... it's not clear which one is the right one.

## Provisioning a CA and Generating TLS Certificates
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/04-certificate-authority.md)

* In this lab you will provision a [PKI Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) using the popular openssl tool, then use it to bootstrap a Certificate Authority, and generate TLS certificates for the following components: etcd, kube-apiserver, kube-controller-manager, kube-scheduler, kubelet, and kube-proxy.

### Certificate Authority
* In this section you will provision a Certificate Authority that can be used to generate additional TLS certificates.
* Create a CA certificate, then generate a Certificate Signing Request and use it to create a private key:
```bash
# Create private key for CA
openssl genrsa -out ca.key 2048

# Create CSR using the private key
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr

# Self sign the csr using its own private key
openssl x509 -req -in ca.csr -signkey ca.key -CAcreateserial  -out ca.crt -days 1000
```
* results: `ca.crt`, `ca.key`
* The ca.crt is the Kubernetes Certificate Authority certificate and ca.key is the Kubernetes Certificate Authority private key. You will use the ca.crt file in many places, so it will be copied to many places. The ca.key is used by the CA for signing certificates. And it should be securely stored. In this case our master node(s) is our CA server as well, so we will store it on master node(s). There is not need to copy this file to elsewhere.

### Client and Server Certificates
* In this section you will generate client and server certificates for each Kubernetes component and a client certificate for the Kubernetes `admin` user.

#### The Admin Client Certificate
* Generate the `admin` client certificate and private key:
```bash
# Geenrate private key for admin user
openssl genrsa -out admin.key 2048

# Generate CSR for admin user. Note the OU.
openssl req -new -key admin.key -subj "/CN=admin/O=system:masters" -out admin.csr

# Sign certificate for admin user using CA servers private key
openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out admin.crt -days 1000
```
* Note that the admin user is part of the **system:masters** group. This is how we are able to perform any administrative operations on Kubernetes cluster using kubectl utility.
* results: `admin.key`, `admin.crt`
* The admin.crt and admin.key file gives you administrative access. We will configure these to be used with the kubectl tool to perform administrative functions on kubernetes.

#### The kubelet client certificates
##### The Controller Manager Client Certificate
* Generate the `kube-controller-manager` client certificate and private key:
```bash
openssl genrsa -out kube-controller-manager.key 2048
openssl req -new -key kube-controller-manager.key -subj "/CN=system:kube-controller-manager" -out kube-controller-manager.csr
openssl x509 -req -in kube-controller-manager.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out kube-controller-manager.crt -days 1000
```
* results: `kube-controller-manager.key`, `kube-controller-manager.crt`

##### The Kube Proxy Client Certificate
* Generate the `kube-proxy` client certificate and private key:
```bash
openssl genrsa -out kube-proxy.key 2048
openssl req -new -key kube-proxy.key -subj "/CN=system:kube-proxy" -out kube-proxy.csr
openssl x509 -req -in kube-proxy.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-proxy.crt -days 1000
```
* results: `kube-proxy.key`, `kube-proxy.crt`

##### The Scheduler Client Certificate
* Generate the `kube-scheduler` client certificate and private key:
```bash
openssl genrsa -out kube-scheduler.key 2048
openssl req -new -key kube-scheduler.key -subj "/CN=system:kube-scheduler" -out kube-scheduler.csr
openssl x509 -req -in kube-scheduler.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-scheduler.crt -days 1000
```
* results: `kube-scheduler.key`, `kube-scheduler.crt`

##### The Kubernetes API Server Certificate
* The kube-apiserver certificate requires all names that various components may reach it to be part of the alternate names. These include the different DNS names, and IP addresses such as the master servers IP address, the load balancers IP address, the kube-api service IP address etc.
* The `openssl` command cannot take alternate names as command line parameter. So we must create a `conf` file for it:
```bash
cat > openssl.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster.local
IP.1 = 10.96.0.1
IP.2 = 192.168.5.11
IP.3 = 192.168.5.12
IP.4 = 192.168.5.30
IP.5 = 127.0.0.1
EOF
```
* Generates certs for kube-apiserver:
```bash
openssl genrsa -out kube-apiserver.key 2048
openssl req -new -key kube-apiserver.key -subj "/CN=kube-apiserver" -out kube-apiserver.csr -config openssl.cnf
openssl x509 -req -in kube-apiserver.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out kube-apiserver.crt -extensions v3_req -extfile openssl.cnf -days 1000
```
* results: `kube-apiserver.key`, `kube-apiserver.crt`

##### The ETCD Server Certificate
* Similarly ETCD server certificate must have addresses of all the servers part of the ETCD cluster.
* The `openssl` command cannot take alternate names as command line parameter. So we must create a `conf` file for it:
```bash
cat > openssl-etcd.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
IP.1 = 192.168.5.11
IP.2 = 192.168.5.12
IP.3 = 127.0.0.1
EOF
```
* Generates certs for ETCD:
```bash
openssl genrsa -out etcd-server.key 2048
openssl req -new -key etcd-server.key -subj "/CN=etcd-server" -out etcd-server.csr -config openssl-etcd.cnf
openssl x509 -req -in etcd-server.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out etcd-server.crt -extensions v3_req -extfile openssl-etcd.cnf -days 1000
```
* results: `etcd-server.key`, `etcd-server.crt`

##### The Service Account Key Pair
* The Kubernetes Controller Manager leverages a key pair to generate and sign service account tokens as describe in the [managing service accounts](https://kubernetes.io/docs/admin/service-accounts-admin/) documentation.
* Generate the `service-account` certificate and private key:
```bash
openssl genrsa -out service-account.key 2048
openssl req -new -key service-account.key -subj "/CN=service-accounts" -out service-account.csr
openssl x509 -req -in service-account.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out service-account.crt -days 1000
```
* results: `server-account.key`, `server-account.crt`

### Distribute the Certificates
* Put these files into directory `ca/distribute`:
	* `ca.key`, `ca.crt`
	* `kube-apiserver.key`, `kube-apiserver.crt`
	* `etcd-server.key`, `etcd-server.crt`
	* `service-account.key`, `service-account.crt`
* Copy the appropriate certificates and private keys to each controller instance:
```bash
for instance in master-1 master-2; do
	vagrant upload ca/distribute/ /home/vagrant ${instance}
done
```

> [!Info]
> The `kube-proxy`, `kube-controller-manager`, `kube-scheduler`, and `kubelet` client certificates will be used to generate client authentication configuration files in the next lab. These certificates will be embedded into the client authentication configuration files. We will then copy those configuration files to the other master nodes.

## Generating Kubernetes Configuration Files for Authentication
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/05-kubernetes-configuration-files.md)

* In this lab you will generate [Kubernetes configuration files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/), also known as kubeconfigs, which enable Kubernetes clients to locate and authenticate to the Kubernetes API Servers.

### Client Authentication Configs
* In this section you will generate kubeconfig files for the `controller manager`, `kubelet`, `kube-proxy`, and `scheduler` clients and the `admin` user.

#### Kubernetes Public IP Address
* Each kubeconfig requires a Kubernetes API Server to connect to. To support high availability the IP address assigned to the load balancer will be used. In our case it is `192.168.5.30`
	* `LOADBALANCER_ADDRESS=192.168.5.30`

#### kube-proxy Config
* Generate a kubeconfig file for the `kube-proxy` service:
```bash
{
  kubectl config set-cluster kubernetes-the-hard-way \
    --certificate-authority=ca.crt \
    --embed-certs=true \
    --server=https://${LOADBALANCER_ADDRESS}:6443 \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config set-credentials system:kube-proxy \
    --client-certificate=kube-proxy.crt \
    --client-key=kube-proxy.key \
    --embed-certs=true \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config set-context default \
    --cluster=kubernetes-the-hard-way \
    --user=system:kube-proxy \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
}
```
* result: `kube-proxy.kubeconfig`

#### kube-controller-manager Config
* Generate a kubeconfig file for the `kube-controller-manager` service:
```bash
{
  kubectl config set-cluster kubernetes-the-hard-way \
    --certificate-authority=ca.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config set-credentials system:kube-controller-manager \
    --client-certificate=kube-controller-manager.crt \
    --client-key=kube-controller-manager.key \
    --embed-certs=true \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config set-context default \
    --cluster=kubernetes-the-hard-way \
    --user=system:kube-controller-manager \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config use-context default --kubeconfig=kube-controller-manager.kubeconfig
}
```
* result: `kube-controller-manager.kubeconfig`

#### kube-scheduler Config
* Generate a kubeconfig file for the `kube-scheduler` service:
```bash
{
  kubectl config set-cluster kubernetes-the-hard-way \
    --certificate-authority=ca.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config set-credentials system:kube-scheduler \
    --client-certificate=kube-scheduler.crt \
    --client-key=kube-scheduler.key \
    --embed-certs=true \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config set-context default \
    --cluster=kubernetes-the-hard-way \
    --user=system:kube-scheduler \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config use-context default --kubeconfig=kube-scheduler.kubeconfig
}
```
* result: `kube-scheduler.kubeconfig`

#### admin Config
* Generate a kubeconfig file for the `admin` user:
```bash
{
  kubectl config set-cluster kubernetes-the-hard-way \
    --certificate-authority=ca.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=admin.kubeconfig

  kubectl config set-credentials admin \
    --client-certificate=admin.crt \
    --client-key=admin.key \
    --embed-certs=true \
    --kubeconfig=admin.kubeconfig

  kubectl config set-context default \
    --cluster=kubernetes-the-hard-way \
    --user=admin \
    --kubeconfig=admin.kubeconfig

  kubectl config use-context default --kubeconfig=admin.kubeconfig
}
```
* result: `admin.kubeconfig`

## Generating the Data Encryption Config and Key
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/06-data-encryption-keys.md)

* Kubernetes stores a variety of data including cluster state, application configurations, and secrets. Kubernetes supports the ability to [encrypt](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data) cluster data at rest.
* In this lab you will generate an encryption key and an [encryption config](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#understanding-the-encryption-at-rest-configuration) suitable for encrypting Kubernetes Secrets.

### The Encryption Key
* Generate an encryption key:
* `ENCRYPTION_KEY=$(head -c 32 /dev/urandom | base64)`

### The Encryption Config File
* Create the `encryption-config.yaml` encryption config file:
```bash
cat > encryption-config.yaml <<EOF
kind: EncryptionConfig
apiVersion: v1
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: ${ENCRYPTION_KEY}
      - identity: {}
EOF
```
* Copy the `encryption-config.yaml` encryption config file to each controller instance:
```bash
for instance in master-1 master-2; do
  vagrant upload encryption-config.yaml /home/vagrant/ ${instance}
done
```

## Bootstrapping the etcd Cluster
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/07-bootstrapping-etcd.md)

* Kubernetes components are stateless and store cluster state in [etcd](https://github.com/coreos/etcd). In this lab you will bootstrap a three node etcd cluster and configure it for high availability and secure remote access.
* The commands in this lab must be run on each controller instance: `master-1`, and `master-2`. Login to each of these using an SSH terminal.

### Bootstrapping an etcd Cluster Member
* Download the official etcd release binaries from the [coreos/etcd](https://github.com/coreos/etcd) GitHub Project. Grab the link of the latest release from the releases page.
* On host os:
```bash
wget -q --show-progress --https-only --timestamping "[link]"
cp etcd*.tar.gz ~/Studio/VBox/VBoxFiles
mv etcd*.tar.gz ~/Studio/VBox/VBoxShared
```
* On master nodes:
```bash
cp /media/vboxshared/etcd*.tar.gz /tmp
{
  tar -xvf etcd*.tar.gz
  sudo mv etcd*/etcd* /usr/local/bin/
}
# /usr/local/bin ::
# - etcd
# - etcdctl
# - etcdutl
```

#### Configure the etcd Server
```bash
{
  sudo mkdir -p /etc/etcd /var/lib/etcd
  sudo cp ca.crt etcd-server.key etcd-server.crt /etc/etcd/
}
```
* The instance internal IP address will be used to serve client requests and communicate with etcd cluster peers. Retrieve the internal IP address of the master(etcd) nodes:
	* `INTERNAL_IP=$(ip addr show enp0s8 | grep "inet " | awk '{print $2}' | cut -d / -f 1)`
* Each etcd member must have a unique name within an etcd cluster. Set the etcd name to match the hostname of the current compute instance:
	* `ETCD_NAME=$(hostname -s)`
* Create the `etcd.service` systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/etcd.service
[Unit]
Description=etcd
Documentation=https://github.com/coreos

[Service]
ExecStart=/usr/local/bin/etcd \\
  --name ${ETCD_NAME} \\
  --cert-file=/etc/etcd/etcd-server.crt \\
  --key-file=/etc/etcd/etcd-server.key \\
  --peer-cert-file=/etc/etcd/etcd-server.crt \\
  --peer-key-file=/etc/etcd/etcd-server.key \\
  --trusted-ca-file=/etc/etcd/ca.crt \\
  --peer-trusted-ca-file=/etc/etcd/ca.crt \\
  --peer-client-cert-auth \\
  --client-cert-auth \\
  --initial-advertise-peer-urls https://${INTERNAL_IP}:2380 \\
  --listen-peer-urls https://${INTERNAL_IP}:2380 \\
  --listen-client-urls https://${INTERNAL_IP}:2379,https://127.0.0.1:2379 \\
  --advertise-client-urls https://${INTERNAL_IP}:2379 \\
  --initial-cluster-token etcd-cluster-0 \\
  --initial-cluster master-1=https://${INTERNAL_IP}:2380,master-2=https://${INTERNAL_IP}:2380 \\
  --initial-cluster-state new \\
  --data-dir=/var/lib/etcd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

#### Start the etcd Server
```bash
{
  sudo systemctl daemon-reload
  sudo systemctl enable etcd
  sudo systemctl start etcd
}
```

### Verification
* List the etcd cluster members:
```bash
sudo ETCDCTL_API=3 etcdctl member list \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/etcd/ca.crt \
  --cert=/etc/etcd/etcd-server.crt \
  --key=/etc/etcd/etcd-server.key
```
* output:
```bash
45bf9ccad8d8900a, started, master-2, https://192.168.5.12:2380, https://192.168.5.12:2379
54a5796a6803f252, started, master-1, https://192.168.5.11:2380, https://192.168.5.11:2379
```

## Bootstrapping the Kubernetes Control Plane
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/08-bootstrapping-kubernetes-controllers.md)

* In this lab you will bootstrap the Kubernetes control plane across 2 compute instances and configure it for high availability. You will also create an external load balancer that exposes the Kubernetes API Servers to remote clients. The following components will be installed on each node: Kubernetes API Server, Scheduler, and Controller Manager.

### config kube control plane
* Create the Kubernetes configuration directory:
	* `mkdir -p /etc/kubernetes/config`
* Download kubernetes binaries from [downloadkubernetes](https://www.downloadkubernetes.com/). `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `kubectl`
* Install the binaries (first move them to vboxshared):
	* `cp -rvp /media/vboxshared/kube /tmp`
	* `chmod +x /tmp/kube/*`
	* `sudo mv /tmp/kube/* /usr/local/bin/`
* Configure the API Server
```bash
{
  sudo mkdir -p /var/lib/kubernetes/

  sudo cp ca.crt ca.key kube-apiserver.crt kube-apiserver.key \
    service-account.key service-account.crt \
    etcd-server.key etcd-server.crt \
    encryption-config.yaml /var/lib/kubernetes/
}
```
* Create the kube-apiserver.service systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/kube-apiserver.service
[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes

[Service]
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=${INTERNAL_IP} \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --audit-log-maxage=30 \\
  --audit-log-maxbackup=3 \\
  --audit-log-maxsize=100 \\
  --audit-log-path=/var/log/audit.log \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --client-ca-file=/var/lib/kubernetes/ca.crt \\
  --enable-admission-plugins=NodeRestriction,ServiceAccount \\
  --enable-swagger-ui=true \\
  --enable-bootstrap-token-auth=true \\
  --etcd-cafile=/var/lib/kubernetes/ca.crt \\
  --etcd-certfile=/var/lib/kubernetes/etcd-server.crt \\
  --etcd-keyfile=/var/lib/kubernetes/etcd-server.key \\
  --etcd-servers=https://192.168.5.11:2379,https://192.168.5.12:2379 \\
  --event-ttl=1h \\
  --encryption-provider-config=/var/lib/kubernetes/encryption-config.yaml \\
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.crt \\
  --kubelet-client-certificate=/var/lib/kubernetes/kube-apiserver.crt \\
  --kubelet-client-key=/var/lib/kubernetes/kube-apiserver.key \\
  --kubelet-https=true \\
  --runtime-config=api/all \\
  --service-account-key-file=/var/lib/kubernetes/service-account.crt \\
  --service-cluster-ip-range=10.96.0.0/24 \\
  --service-node-port-range=30000-32767 \\
  --tls-cert-file=/var/lib/kubernetes/kube-apiserver.crt \\
  --tls-private-key-file=/var/lib/kubernetes/kube-apiserver.key \\
  --v=2
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

### config kube controller manager
* Move the kube-controller-manager kubeconfig into place:
```bash
sudo mv kube-controller-manager.kubeconfig /var/lib/kubernetes/
```
* Create the `kube-controller-manager.service` systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/kube-controller-manager.service
[Unit]
Description=Kubernetes Controller Manager
Documentation=https://github.com/kubernetes/kubernetes

[Service]
ExecStart=/usr/local/bin/kube-controller-manager \\
  --address=0.0.0.0 \\
  --cluster-cidr=192.168.5.0/24 \\
  --cluster-name=kubernetes \\
  --cluster-signing-cert-file=/var/lib/kubernetes/ca.crt \\
  --cluster-signing-key-file=/var/lib/kubernetes/ca.key \\
  --kubeconfig=/var/lib/kubernetes/kube-controller-manager.kubeconfig \\
  --leader-elect=true \\
  --root-ca-file=/var/lib/kubernetes/ca.crt \\
  --service-account-private-key-file=/var/lib/kubernetes/service-account.key \\
  --service-cluster-ip-range=10.96.0.0/24 \\
  --use-service-account-credentials=true \\
  --v=2
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

### config kube scheduler
* Move the `kube-scheduler` kubeconfig into place:
```bash
sudo mv kube-scheduler.kubeconfig /var/lib/kubernetes/
```
* Create the `kube-scheduler.service` systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/kube-scheduler.service
[Unit]
Description=Kubernetes Scheduler
Documentation=https://github.com/kubernetes/kubernetes

[Service]
ExecStart=/usr/local/bin/kube-scheduler \\
  --kubeconfig=/var/lib/kubernetes/kube-scheduler.kubeconfig \\
  --address=127.0.0.1 \\
  --leader-elect=true \\
  --v=2
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

### start the services
```bash
{
  sudo systemctl daemon-reload
  sudo systemctl enable kube-apiserver kube-controller-manager kube-scheduler
  sudo systemctl start kube-apiserver kube-controller-manager kube-scheduler
}
```

> Allow up to 10 seconds for the Kubernetes API Server to fully initialize.

### verification
```bash
kubectl get componentstatuses --kubeconfig admin.kubeconfig
```
```text
NAME                 STATUS    MESSAGE              ERROR
controller-manager   Healthy   ok
scheduler            Healthy   ok
etcd-0               Healthy   {"health": "true"}
etcd-1               Healthy   {"health": "true"}
```

> Remember to run the above commands on each controller node: `master-1`, and `master-2`.

### The Kubernetes Frontend Load Balancer
* In this section you will provision an external load balancer to front the Kubernetes API Servers. The kubernetes-the-hard-way static IP address will be attached to the resulting load balancer.

#### Provision a Network Load Balancer
```bash
#Install HAProxy
#loadbalancer machine
sudo apt-get update && sudo apt-get install -y haproxy
```
```bash
cat <<EOF | sudo tee /etc/haproxy/haproxy.cfg 
frontend kubernetes
    bind 192.168.5.30:6443
    option tcplog
    mode tcp
    default_backend kubernetes-master-nodes

backend kubernetes-master-nodes
    mode tcp
    balance roundrobin
    option tcp-check
    server master-1 192.168.5.11:6443 check fall 3 rise 2
    server master-2 192.168.5.12:6443 check fall 3 rise 2
EOF
```
```bash
sudo service haproxy restart
```

#### verification
* Make a HTTP request for the Kubernetes version info:
```bash
curl  https://192.168.5.30:6443/version -
```
```text
output: {
  "major": "1",
  "minor": "13",
  "gitVersion": "v1.13.0",
  "gitCommit": "ddf47ac13c1a9483ea035a79cd7c10005ff21a6d",
  "gitTreeState": "clean",
  "buildDate": "2018-12-03T20:56:12Z",
  "goVersion": "go1.11.2",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

## Bootstrapping the Kubernetes Worker Nodes
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/09-bootstrapping-kubernetes-workers.md)

* In this lab you will bootstrap 2 Kubernetes worker nodes. We already have Docker installed on these nodes.
* **The commands in this lab must be run on first worker instance: `worker-1`. Login to first worker instance using SSH Terminal.**

### Provisioning kubelet client certificates
* Kubernetes uses a special-purpose authorization mode called Node Authorizer, that specifically authorizes API requests made by Kubelets. In order to be authorized by the Node Authorizer, Kubelets must use a credential that identifies them as being in the system:nodes group, with a username of `system:node:<nodeName>`. In this section you will create a certificate for each Kubernetes worker node that meets the Node Authorizer requirements.
* Generate a certificate and private key for one worker node:
```bash
cat > openssl-worker-1.cnf <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = worker-1
IP.1 = 192.168.5.21
EOF

openssl genrsa -out worker-1.key 2048
openssl req -new -key worker-1.key -subj "/CN=system:node:worker-1/O=system:nodes" -out worker-1.csr -config openssl-worker-1.cnf
openssl x509 -req -in worker-1.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out worker-1.crt -extensions v3_req -extfile openssl-worker-1.cnf -days 1000
```
* results: `worker-1.crt`, `worker-1.key`

### the kubernetes kubelet configuration file
* When generating kubeconfig files for Kubelets the client certificate matching the Kubelet's node name must be used. This will ensure Kubelets are properly authorized by the Kubernetes [Node Authorizer](https://kubernetes.io/docs/admin/authorization/node/).
* `LOADBALANCER_IP=192.168.56.30`
* Generate a kubeconfig file for the first worker node:
```bash
{
  kubectl config set-cluster kubernetes-the-hard-way \
    --certificate-authority=ca.crt \
    --embed-certs=true \
    --server=https://${LOADBALANCER_ADDRESS}:6443 \
    --kubeconfig=worker-1.kubeconfig

  kubectl config set-credentials system:node:worker-1 \
    --client-certificate=worker-1.crt \
    --client-key=worker-1.key \
    --embed-certs=true \
    --kubeconfig=worker-1.kubeconfig

  kubectl config set-context default \
    --cluster=kubernetes-the-hard-way \
    --user=system:node:worker-1 \
    --kubeconfig=worker-1.kubeconfig

  kubectl config use-context default --kubeconfig=worker-1.kubeconfig
}
```
* results: `worker-1.kubeconfig`

### download and install worker binaries
* download `kubectl`, `kubeproxy`, and `kubelet`
* Create the installation directories:
```bash
sudo mkdir -p \
  /etc/cni/net.d \
  /opt/cni/bin \
  /var/lib/kubelet \
  /var/lib/kube-proxy \
  /var/lib/kubernetes \
  /var/run/kubernetes
```
* Install the worker binaries:
```bash
{
  chmod +x kubectl kube-proxy kubelet
  sudo mv kubectl kube-proxy kubelet /usr/local/bin/
}
```

### configure the kubelet
```bash
{
  sudo mv ${HOSTNAME}.key ${HOSTNAME}.crt /var/lib/kubelet/
  sudo mv ${HOSTNAME}.kubeconfig /var/lib/kubelet/kubeconfig
  sudo mv ca.crt /var/lib/kubernetes/
}
```
* Create the kubelet-config.yaml configuration file:
```bash
cat <<EOF | sudo tee /var/lib/kubelet/kubelet-config.yaml
kind: KubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  anonymous:
    enabled: false
  webhook:
    enabled: true
  x509:
    clientCAFile: "/var/lib/kubernetes/ca.crt"
authorization:
  mode: Webhook
clusterDomain: "cluster.local"
clusterDNS:
  - "10.96.0.10"
resolvConf: "/run/systemd/resolve/resolv.conf"
runtimeRequestTimeout: "15m"
EOF
```

> The `resolvConf` configuration is used to avoid loops when using CoreDNS for service discovery on systems running `systemd-resolved`.

* Create the kubelet.service systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/kubelet.service
[Unit]
Description=Kubernetes Kubelet
Documentation=https://github.com/kubernetes/kubernetes
After=docker.service
Requires=docker.service

[Service]
ExecStart=/usr/local/bin/kubelet \\
  --config=/var/lib/kubelet/kubelet-config.yaml \\
  --image-pull-progress-deadline=2m \\
  --kubeconfig=/var/lib/kubelet/kubeconfig \\
  --tls-cert-file=/var/lib/kubelet/${HOSTNAME}.crt \\
  --tls-private-key-file=/var/lib/kubelet/${HOSTNAME}.key \\
  --network-plugin=cni \\
  --register-node=true \\
  --v=2
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

#### containerd.io
* kubelet requires containerd. [source](https://serverfault.com/questions/1118051/failed-to-run-kubelet-validate-service-connection-cri-v1-runtime-api-is-not-im)
* add docker to apt sources.
```bash
sudo apt install containerd.io
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml
sudo vim /etc/containerd/config.toml # set SystemdCgroup = true
sudo systemctl restart containerd
```

### configure kube-proxy
```bash
sudo mv kube-proxy.kubeconfig /var/lib/kube-proxy/kubeconfig
```
* Create the kube-proxy-config.yaml configuration file:
```bash
cat <<EOF | sudo tee /var/lib/kube-proxy/kube-proxy-config.yaml
kind: KubeProxyConfiguration
apiVersion: kubeproxy.config.k8s.io/v1alpha1
clientConnection:
  kubeconfig: "/var/lib/kube-proxy/kubeconfig"
mode: "iptables"
clusterCIDR: "192.168.5.0/24"
EOF
```
* Create the kube-proxy.service systemd unit file:
```bash
cat <<EOF | sudo tee /etc/systemd/system/kube-proxy.service
[Unit]
Description=Kubernetes Kube Proxy
Documentation=https://github.com/kubernetes/kubernetes

[Service]
ExecStart=/usr/local/bin/kube-proxy \\
  --config=/var/lib/kube-proxy/kube-proxy-config.yaml
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```

### start the services
```bash
{
  sudo systemctl daemon-reload
  sudo systemctl enable kubelet kube-proxy
  sudo systemctl start kubelet kube-proxy
}
```

> Remember to run the above commands on worker node: `worker-1`

### verification
* List the registered Kubernetes nodes from the master node:
```bash
kubectl get nodes --kubeconfig admin.kubeconfig
```

> output

```text
NAME       STATUS     ROLES    AGE   VERSION
worker-1   NotReady   <none>   93s   v1.13.0
```

> **Note**: It is OK for the worker node to be in a NotReady state. That is because we haven't configured Networking yet.

## Bootstrapping kubernetes workers
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/10-tls-bootstrapping-kubernetes-workers.md)

* In the previous step we configured a worker node by
	- Creating a set of key pairs for the worker node by ourself
	- Getting them signed by the CA by ourself
	- Creating a kube-config file using this certificate by ourself
	- Everytime the certificate expires we must follow the same process of updating the certificate by ourself
- This is not a practical approach when you have 1000s of nodes in the cluster, and nodes dynamically being added and removed from the cluster. With TLS boostrapping:
	* The Nodes can generate certificate key pairs by themselves
	* The Nodes can generate certificate signing request by themselves
	* The Nodes can submit the certificate signing request to the Kubernetes CA (Using the Certificates API)
	* The Nodes can retrieve the signed certificate from the Kubernetes CA
	* The Nodes can generate a kube-config file using this certificate by themselves
	* The Nodes can start and join the cluster by themselves
	* The Nodes can renew certificates when they expire by themselves

### What is required for TLS bootstrapping?
* **Certificates API**: The Certificate API (as discussed in the lecture) provides a set of APIs on Kubernetes that can help us manage certificates (Create CSR, Get them signed by CA, Retrieve signed certificate etc). The worker nodes (kubelets) have the ability to use this API to get certificates signed by the Kubernetes CA.

### 