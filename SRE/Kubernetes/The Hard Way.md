> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/)

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