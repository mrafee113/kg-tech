* resources
	* [github](https://github.com/kubernetes-sigs/kubespray)
		* [requirements](https://github.com/kubernetes-sigs/kubespray#requirements)
		* [kubespray vs](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/comparisons.md)
		* [getting started](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/getting-started.md) (ansible)
		* [ansible](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible.md)
		* [network plugins](https://github.com/kubernetes-sigs/kubespray#network-plugins)
		* [vagrant install](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/vagrant.md)
		* [downloaded artifacts](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/downloads.md)
		* [adding/replacing a node](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/nodes.md)
		* [hardening](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/hardening.md) (secure kubernetes)
		* [mirror](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/mirror.md) (public mirror for quicker download)
		* [offline environment](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/offline-environment.md)
		* [offline tools](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/offline/README.md)
	* [kubespray.io](https://kubespray.io/#/)
		* [variables](https://kubespray.io/#/docs/vars)
		* operations
			* [upgrading kubernetes](https://kubespray.io/#/docs/upgrades)
			* [large deployments](https://kubespray.io/#/docs/large-deployments)
		* CNI
			* [calico](https://kubespray.io/#/docs/calico)
			* [weave](https://kubespray.io/#/docs/weave)
		* CRI
			* [containerd](https://kubespray.io/#/docs/containerd)
			* [docker](https://kubespray.io/#/docs/docker)
		* [proxy](https://kubespray.io/#/docs/proxy)
		* [cert manager](https://kubespray.io/#/docs/cert_manager)
		* [dns stack](https://kubespray.io/#/docs/dns-stack)
		* [NTP](https://kubespray.io/#/docs/ntp)

### Requirements
> [source](https://github.com/kubernetes-sigs/kubespray#requirements)
> as of Jul 23 2023

- **Minimum required version of Kubernetes is v1.25**
- **Ansible v2.11+, Jinja 2.11+ and python-netaddr is installed on the machine that will run Ansible commands**
- The target servers must have **access to the Internet** in order to pull docker images. Otherwise, additional configuration is required ***(See [Offline Environment](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/offline-environment.md))***
- The target servers are configured to allow **IPv4 forwarding**.
- If using IPv6 for pods and services, the target servers are configured to allow **IPv6 forwarding**.
- The **firewalls are not managed**, you'll need to implement your own rules the way you used to. in order to avoid any issue during deployment you should disable your firewall.
- If kubespray is run from non-root user account, correct privilege escalation method should be configured in the target servers. Then the `ansible_become` flag or command parameters `--become or -b` should be specified.

Hardware: These limits are safeguarded by Kubespray. Actual requirements for your workload can differ. For a sizing guide go to the [Building Large Clusters](https://kubernetes.io/docs/setup/cluster-large/#size-of-master-and-master-components) guide.

- Master
    - Memory: 1500 MB
- Node
    - Memory: 1024 MB

# Vagrant
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/vagrant.md)

* Assuming you have the requirements, you should be able to launch a 3 node Kubernetes cluster by simply running `vagrant up`.
* To give an estimate of the expected duration of a provisioning run: On a dual core `i5-6300u` laptop with an SSD, provisioning takes around 13 to 15 minutes, once the container images and other files are cached. Note that `libvirt/qemu` is recommended over `virtualbox` as it is quite a bit faster, especially during boot-up time.
* For proper performance a minimum of 12GB RAM is recommended. It is possible to run a 3 node cluster on a laptop with 8GB of RAM using the default Vagrantfile, provided you have 8GB zram swap configured and not much more than a browser and a mail client running. If you decide to run on such a machine, then also make sure that any `tmpfs` devices, that are mounted, are mostly empty and disable any `swapfiles` mounted on HDD/SSD or you will be in for some serious swap-madness. Things can get a bit sluggish during provisioning, but when that's done, the system will actually be able to perform quite well.

## Customize Vagrant
* You can override the default settings in the `Vagrantfile` either by directly modifying the `Vagrantfile` or through an override file. In the same directory as the `Vagrantfile`, create a folder called `vagrant` and create `config.rb` file in it. An example of how to configure this file is given below.

### Use alternative OS for Vagrant
* By default, Vagrant uses Ubuntu 18.04 box to provision a local cluster. You may use an alternative supported operating system for your local cluster.
* Customize $os variable in Vagrantfile or as override, e.g.,:
```bash
echo '$os = "flatcar-stable"' >> vagrant/config.rb
```
* The supported operating systems for vagrant are defined in the `SUPPORTED_OS` constant in the `Vagrantfile`.

### File and Image Caching
* Kubespray can take quite a while to start on a laptop.
* To improve provisioning speed, the variable `download_run_once` is set.
* This will make kubespray download all files and containers just once and then redistributes them to the other nodes and as a bonus, also cache all downloads locally and re-use them on the next provisioning run.
* For more information on download settings see [download documentation](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/downloads.md).

### Example Use of Vagrant
* The following is an example of setting up and running kubespray using `vagrant`.
* For repeated runs, you could save the script to a file in the root of the kubespray and run it by executing `source <name_of_the_file>`.
```bash
# use virtualenv to install all python requirements
VENVDIR=venv
virtualenv --python=/usr/bin/python3.7 $VENVDIR
source $VENVDIR/bin/activate
pip install -r requirements.txt

# prepare an inventory to test with
INV=inventory/my_lab
rm -rf ${INV}.bak &> /dev/null
mv ${INV} ${INV}.bak &> /dev/null
cp -a inventory/sample ${INV}
rm -f ${INV}/hosts.ini

# customize the vagrant environment
mkdir vagrant
cat << EOF > vagrant/config.rb
\$instance_name_prefix = "kub"
\$vm_cpus = 1
\$num_instances = 3
\$os = "centos-bento"
\$subnet = "10.0.20"
\$network_plugin = "flannel"
\$inventory = "$INV"
\$shared_folders = { 'temp/docker_rpms' => "/var/cache/yum/x86_64/7/docker-ce/packages" }
EOF

# make the rpm cache
mkdir -p temp/docker_rpms

vagrant up

# make a copy of the downloaded docker rpm, to speed up the next provisioning run
scp kub-1:/var/cache/yum/x86_64/7/docker-ce/packages/* temp/docker_rpms/

# copy kubectl access configuration in place
mkdir $HOME/.kube/ &> /dev/null
ln -s $PWD/$INV/artifacts/admin.conf $HOME/.kube/config
# make the kubectl binary available
sudo ln -s $PWD/$INV/artifacts/kubectl /usr/local/bin/kubectl
#or
export PATH=$PATH:$PWD/$INV/artifacts
```

* If a vagrant run failed and you've made some changes to fix the issue causing the fail, here is how you would re-run ansible:
```bash
ansible-playbook -vvv -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory cluster.yml
```
* If all went well, you check if it's all working as expected:
```bash
kubectl get nodes
```
```text
$ kubectl get nodes
NAME    STATUS   ROLES                  AGE     VERSION
kub-1   Ready    control-plane,master   4m37s   v1.22.5
kub-2   Ready    control-plane,master   4m7s    v1.22.5
kub-3   Ready    <none>                 3m7s    v1.22.5
```
* Another nice test is the following:
```bash
kubectl get pods --all-namespaces -o wide
```

# Ansible
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible.md#installing-ansible)

### Installing Ansible
> as of Jul 24 2023
* Kubespray supports multiple ansible versions and ships different `requirements.txt` files for them. Depending on your available python version you may be limited in choosing which ansible version to use.
* It is recommended to deploy the ansible version used by kubespray into a python virtual environment.
```bash
VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate
cd $KUBESPRAYDIR
pip install -U -r requirements.txt
```
* In case you have a similar message when installing the requirements:
```text
ERROR: Could not find a version that satisfies the requirement ansible==7.6.0 (from -r requirements.txt (line 1)) (from versions: [...], 6.7.0)
ERROR: No matching distribution found for ansible==7.6.0 (from -r requirements.txt (line 1))
```
* It means that the version of Python you are running is not compatible with the version of Ansible that Kubespray supports. If the latest version supported according to pip is 6.7.0 it means you are running Python 3.8 or lower while you need at least Python 3.9 (see the table below).

#### Ansible Python compatibility
* Based on the table below and the available python version for your ansible host you should choose the appropriate ansible version to use with kubespray.

| Ansible version | Python version |
| :-: | :-: |
| 2.14 | 3.9-3.11 |

### Inventory
* The inventory is composed of 3 groups:
	- **kube_node** : list of kubernetes nodes where the pods will run.
	- **kube_control_plane** : list of servers where kubernetes control plane components (apiserver, scheduler, controller) will run.
	- **etcd**: list of servers to compose the etcd server. You should have at least 3 servers for failover purpose.
- Below is a complete inventory example:
```ini
## Configure 'ip' variable to bind kubernetes services on a
## different ip than the default iface
node1 ansible_host=95.54.0.12 ip=10.3.0.1
node2 ansible_host=95.54.0.13 ip=10.3.0.2
node3 ansible_host=95.54.0.14 ip=10.3.0.3
node4 ansible_host=95.54.0.15 ip=10.3.0.4
node5 ansible_host=95.54.0.16 ip=10.3.0.5
node6 ansible_host=95.54.0.17 ip=10.3.0.6

[kube_control_plane]
node1
node2

[etcd]
node1
node2
node3

[kube_node]
node2
node3
node4
node5
node6

[k8s_cluster:children]
kube_node
kube_control_plane
```

#### Group vars and overriding variable precedence
* The group variables to control main deployment options are located in the directory `inventory/sample/group_vars`.
* Optional variables are located in the `inventory/sample/group_vars/all.yml`.
* Mandatory variables that are common for at least one role (or a node group) can be found in the `inventory/sample/group_vars/k8s_cluster.yml`.
	* There are also role vars for docker, kubernetes preinstall and control plane roles.
	* According to the [ansible docs](https://docs.ansible.com/ansible/latest/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable), those cannot be overridden from the group vars. In order to override, one should use the `-e` runtime flags (most simple way) or other layers described in the docs.

Kubespray uses only a few layers to override things (or expect them to be overridden for roles):

| Layer | Comment |
| :- | :- |
| **role defaults** | provides best UX to override things for Kubespray deployments |
| inventory vars | Unused |
| **inventory group_vars** | Expects users to use `all.yml`,`k8s_cluster.yml` etc. to override things |
| inventory host_vars | Unused |
| playbook group_vars | Unused |
| playbook host_vars | Unused |
| **host facts** | Kubespray overrides for internal roles' logic, like state flags |
| play vars | Unused |
| play vars_prompt | Unused |
| play vars_files | Unused |
| registered vars | Unused |
| **set_facts** | Kubespray overrides those, for some places |
| **role and include vars** | Provides bad UX to override things! Use extra vars to enforce |
| block vars (only for tasks in block) | Kubespray overrides for internal roles' logic |
| task vars (only for the task) | Unused for roles, but only for helper scripts |
| **extra vars (always win precedence)** | override with `ansible-playbook -e @foo.yml` |

#### Ansible Tags
The following tags are defined in playbooks.
Note: Use the `bash scripts/gen_tags.sh` command to generate a list of all tags found in the codebase. New tags will be listed with the empty "Used for" field.

|Tag name|Used for|
|---|---|
|annotate|Create kube-router annotation|
|apps|K8s apps definitions|
|asserts|Check tasks for download role|
|aws-ebs-csi-driver|Configuring csi driver: aws-ebs|
|azure-csi-driver|Configuring csi driver: azure|
|bastion|Setup ssh config for bastion|
|bootstrap-os|Anything related to host OS configuration|
|calico|Network plugin Calico|
|calico_rr|Configuring Calico route reflector|
|cephfs-provisioner|Configuring CephFS|
|cert-manager|Configuring certificate manager for K8s|
|cilium|Network plugin Cilium|
|cinder-csi-driver|Configuring csi driver: cinder|
|client|Kubernetes clients role|
|cloud-provider|Cloud-provider related tasks|
|cluster-roles|Configuring cluster wide application (psp ...)|
|cni|CNI plugins for Network Plugins|
|containerd|Configuring containerd engine runtime for hosts|
|container_engine_accelerator|Enable nvidia accelerator for runtimes|
|container-engine|Configuring container engines|
|container-runtimes|Configuring container runtimes|
|coredns|Configuring coredns deployment|
|crio|Configuring crio container engine for hosts|
|crun|Configuring crun runtime|
|csi-driver|Configuring csi driver|
|dashboard|Installing and configuring the Kubernetes Dashboard|
|dns|Remove dns entries when resetting|
|docker|Configuring docker engine runtime for hosts|
|download|Fetching container images to a delegate host|
|etcd|Configuring etcd cluster|
|etcd-secrets|Configuring etcd certs/keys|
|etchosts|Configuring /etc/hosts entries for hosts|
|external-cloud-controller|Configure cloud controllers|
|external-openstack|Cloud controller : openstack|
|external-provisioner|Configure external provisioners|
|external-vsphere|Cloud controller : vsphere|
|facts|Gathering facts and misc check results|
|files|Remove files when resetting|
|flannel|Network plugin flannel|
|gce|Cloud-provider GCP|
|gcp-pd-csi-driver|Configuring csi driver: gcp-pd|
|gvisor|Configuring gvisor runtime|
|helm|Installing and configuring Helm|
|ingress-controller|Configure ingress controllers|
|ingress_alb|AWS ALB Ingress Controller|
|init|Windows kubernetes init nodes|
|iptables|Flush and clear iptable when resetting|
|k8s-pre-upgrade|Upgrading K8s cluster|
|k8s-secrets|Configuring K8s certs/keys|
|k8s-gen-tokens|Configuring K8s tokens|
|kata-containers|Configuring kata-containers runtime|
|krew|Install and manage krew|
|kubeadm|Roles linked to kubeadm tasks|
|kube-apiserver|Configuring static pod kube-apiserver|
|kube-controller-manager|Configuring static pod kube-controller-manager|
|kube-vip|Installing and configuring kube-vip|
|kubectl|Installing kubectl and bash completion|
|kubelet|Configuring kubelet service|
|kube-ovn|Network plugin kube-ovn|
|kube-router|Network plugin kube-router|
|kube-proxy|Configuring static pod kube-proxy|
|localhost|Special steps for the localhost (ansible runner)|
|local-path-provisioner|Configure External provisioner: local-path|
|local-volume-provisioner|Configure External provisioner: local-volume|
|macvlan|Network plugin macvlan|
|master|Configuring K8s master node role|
|metallb|Installing and configuring metallb|
|metrics_server|Configuring metrics_server|
|netchecker|Installing netchecker K8s app|
|network|Configuring networking plugins for K8s|
|mounts|Umount kubelet dirs when reseting|
|multus|Network plugin multus|
|nginx|Configuring LB for kube-apiserver instances|
|node|Configuring K8s minion (compute) node role|
|nodelocaldns|Configuring nodelocaldns daemonset|
|node-label|Tasks linked to labeling of nodes|
|node-webhook|Tasks linked to webhook (grating access to resources)|
|nvidia_gpu|Enable nvidia accelerator for runtimes|
|oci|Cloud provider: oci|
|persistent_volumes|Configure csi volumes|
|persistent_volumes_aws_ebs_csi|Configuring csi driver: aws-ebs|
|persistent_volumes_cinder_csi|Configuring csi driver: cinder|
|persistent_volumes_gcp_pd_csi|Configuring csi driver: gcp-pd|
|persistent_volumes_openstack|Configuring csi driver: openstack|
|policy-controller|Configuring Calico policy controller|
|post-remove|Tasks running post-remove operation|
|post-upgrade|Tasks running post-upgrade operation|
|pre-remove|Tasks running pre-remove operation|
|pre-upgrade|Tasks running pre-upgrade operation|
|preinstall|Preliminary configuration steps|
|registry|Configuring local docker registry|
|reset|Tasks running doing the node reset|
|resolvconf|Configuring /etc/resolv.conf for hosts/apps|
|rbd-provisioner|Configure External provisioner: rdb|
|services|Remove services (etcd, kubelet etc...) when resetting|
|snapshot|Enabling csi snapshot|
|snapshot-controller|Configuring csi snapshot controller|
|upgrade|Upgrading, f.e. container images/binaries|
|upload|Distributing images/binaries across hosts|
|vsphere-csi-driver|Configuring csi driver: vsphere|
|weave|Network plugin Weave|
|win_nodes|Running windows specific tasks|
|youki|Configuring youki runtime|

### Example commands
* Example command to filter and apply only DNS configuration tasks and skip everything else related to host OS configuration and downloading images of containers:
```bash
ansible-playbook -i inventory/sample/hosts.ini cluster.yml --tags preinstall,facts --skip-tags=download,bootstrap-os
```
* And this play only removes the K8s cluster DNS resolver IP from hosts' `/etc/resolv.conf` files:
```bash
ansible-playbook -i inventory/sample/hosts.ini -e dns_mode='none' cluster.yml --tags resolvconf
```
* And this prepares all container images locally (at the ansible runner node) without installing or upgrading related stuff or trying to upload container to K8s cluster nodes:
```bash
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
    -e download_run_once=true -e download_localhost=true \
    --tags download --skip-tags upload,upgrade
```

> [!Note]
> use `--tags` and `--skip-tags` wise and only if you're 100% sure what you're doing.

# Getting started
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/getting-started.md)

### Building your own inventory
* Ansible inventory can be stored in 3 formats: YAML, JSON, or INI-like.
* You can use an [inventory generator](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/inventory_builder/inventory.py) to create or modify an Ansible inventory. Currently, it is limited in functionality and is only used for configuring a basic Kubespray cluster inventory, but it does support creating inventory file for large clusters as well. It now supports separated ETCD and Kubernetes control plane roles from node role if the size exceeds a certain threshold. Run `python3 contrib/inventory_builder/inventory.py` help for more information.
* Example inventory generator usage:
```bash
cp -r inventory/sample inventory/mycluster
declare -a IPS=(10.10.1.3 10.10.1.4 10.10.1.5)
CONFIG_FILE=inventory/mycluster/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
```
* Then use `inventory/mycluster/hosts.yml` as inventory file.

### Starting custom deployments
* Once you have an inventory, you may want to customize deployment data vars and start the deployment.

> [!Important]
> Edit `my_inventory/groups_vars/*.yaml` to override data vars.

#### Adding nodes
* You may want to add worker, control plane or etcd nodes to your existing cluster. This can be done by re-running the `cluster.yml` playbook, **or** you can target the bare minimum needed to get kubelet installed on the worker and talking to your control planes. This is especially helpful when doing something like autoscaling your clusters.
	* Add the new worker node to your inventory in the appropriate group (or utilize a [dynamic inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#intro-dynamic-inventory)).
	* Run the ansible-playbook command, substituting `cluster.yml` for `scale.yml`:
		```bash
		ansible-playbook -i inventory/mycluster/hosts.yml scale.yml -b -v --private-key=~/.ssh/private_key
		```

#### Removing nodes
* You may want to remove **control plane**, **worker**, or **etcd** nodes from your existing cluster. This can be done by re-running the `remove-node.yml` playbook.
* First, all specified nodes will be drained, then stop some kubernetes services and delete some certificates, and finally execute the kubectl command to delete these nodes.
* This can be combined with the add node function. This is generally helpful when doing something like autoscaling your clusters.
* Of course, if a node is not working, you can remove the node and install it again.
* Use `--extra-vars "node=<nodename>,<nodename2>"` to select the node(s) you want to delete.
	```bash
	ansible-playbook -i inventory/mycluster/hosts.yml remove-node.yml -b -v \
	--private-key=~/.ssh/private_key \
	--extra-vars "node=nodename,nodename2"
	```
* If a node is completely unreachable by ssh, add `--extra-vars reset_nodes=false` to skip the node reset step.
* If one node is unavailable, but others you wish to remove are able to connect via SSH, you could set `reset_nodes=false` as a host var in inventory.

### Connecting to kubernetes
* By default, Kubespray configures `kube_control_plane` hosts with insecure access to `kube-apiserver` via port `8080`.
* A kubeconfig file is not necessary in this case, because kubectl will use `http://localhost:8080` to connect.
* The kubeconfig files generated will point to localhost (on `kube_control_planes`) and `kube_node` hosts will connect either to a localhost nginx proxy or to a loadbalancer if configured. More details on this process are in the [HA guide](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ha-mode.md).
* Kubespray permits connecting to the cluster remotely on any IP of any `kube_control_plane` host on port `6443` by default. However, this requires authentication. One can get a kubeconfig from `kube_control_plane` hosts ([see below](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/getting-started.md#accessing-kubernetes-api)).
* For more information on kubeconfig and accessing a Kubernetes cluster, refer to the Kubernetes [documentation](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).

### Accessing kubernetes dashboard
* Supported version is kubernetes-dashboard v2.0.x:
	* Login option : token/kubeconfig by default
	* Deployed by default in "kube-system" namespace, can be overridden with `dashboard_namespace: kubernetes-dashboard` in inventory,
	* Only serves over https
* Access is described in [dashboard docs](https://github.com/kubernetes/dashboard/tree/master/docs/user/accessing-dashboard). With kubespray's default deployment in kube-system namespace, instead of kubernetes-dashboard:
	* Proxy URL is [http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#/login](http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#/login)
	* kubectl commands must be run with `-n kube-system`
* Accessing through Ingress is highly recommended. For proxy access, please note that proxy must listen to [localhost](https://github.com/kubernetes/dashboard/issues/692#issuecomment-220492484) (`proxy --address="x.x.x.x"` will not work)
* For token authentication, guide to create Service Account is provided in [dashboard sample user doc](https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md). Still take care of default namespace.
* Access can also by achieved via ssh tunnel on a control plane:
```bash
# localhost:8081 will be sent to control-plane-1's own localhost:8081
ssh -L8001:localhost:8001 user@control-plane-1
sudo -i
kubectl proxy
```

### Accessing kubernetes API
* The main client of Kubernetes is `kubectl`. It is installed on each `kube_control_plane` host and can optionally be configured on your ansible host by setting `kubectl_localhost: true` and `kubeconfig_localhost: true` in the configuration:
	* If `kubectl_localhost` enabled, `kubectl` will download onto `/usr/local/bin/` and setup with bash completion. A helper script `inventory/mycluster/artifacts/kubectl.sh` also created for setup with below `admin.conf`.
	* If `kubeconfig_localhost` enabled, `admin.conf` will appear in the `inventory/mycluster/artifacts/` directory after deployment.
	* The location where these files are downloaded to can be configured via the `artifacts_dir` variable.

> [!Note]
> The controller host name in the `admin.conf` file might be a private IP. If so, change it to use the controller's public IP or the cluster's load balancer.

* You can see a list of nodes by running the following commands:
```bash
cd inventory/mycluster/artifacts
./kubectl.sh get nodes
```

> [!Tip]
> If desired, copy `admin.conf` to `~/.kube/config`.

# HA endpoints for k8s
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ha-mode.md)

* The following components require a highly available endpoints:
	* etcd cluster,
	* kube-apiserver service instances.
* The latter relies on a 3rd side reverse proxy, like Nginx or HAProxy, to achieve the same goal.

### etcd
* The etcd clients (kube-api-masters) are configured with the list of all etcd peers. If the etcd-cluster has multiple instances, it's configured in HA **already**.

### kube-apiserver
* K8s components require a loadbalancer to access the apiservers via a reverse proxy.
* Kubespray includes support for an nginx-based proxy that resides on each non-master Kubernetes node. This is referred to as localhost loadbalancing. It is less efficient than a dedicated load balancer because it creates extra health checks on the Kubernetes apiserver, but is more practical for scenarios where an external LB or virtual IP management is inconvenient.
* This option is configured by the variable `loadbalancer_apiserver_localhost` (defaults to `True`. Or `False`, if there is an external `loadbalancer_apiserver` defined).
* You may also define the port the local internal loadbalancer uses by changing, `loadbalancer_apiserver_port`. This defaults to the value of `kube_apiserver_port`.
* It is also important to note that Kubespray will only configure kubelet and kube-proxy on non-master nodes to use the local internal loadbalancer.
* If you wish to control the name of the loadbalancer container, you can set the variable `loadbalancer_apiserver_pod_name`.

> [!Warning]
> Read the rest by opening the source.

* Access API endpoints are evaluated automatically, as the following:

|Endpoint type|kube_control_plane|non-master|external|
|---|---|---|---|
|Local LB (default)|`https://dbip:sp`|`https://lc:nsp`|`https://m[0].aip:sp`|
|Local LB (default) + cbip|`https://cbip:sp` and `https://lc:nsp`|`https://lc:nsp`|`https://m[0].aip:sp`|
|Local LB + Unmanaged here LB|`https://dbip:sp`|`https://lc:nsp`|`https://ext`|
|External LB, no internal|`https://dbip:sp`|`<https://lb:lp>`|`https://lb:lp`|
|No ext/int LB|`https://dbip:sp`|`<https://m[0].aip:sp>`|`https://m[0].aip:sp`|

* Where:
	- `m[0]` - the first node in the `kube_control_plane` group;
	- `lb` - LB FQDN, `apiserver_loadbalancer_domain_name`;
	- `ext` - Externally load balanced VIP:port and FQDN, not managed by Kubespray;
	- `lc` - localhost;
	- `cbip` - a custom bind IP, `kube_apiserver_bind_address`;
	- `dbip` - localhost for the default bind IP '0.0.0.0';
	- `nsp` - nginx secure port, `loadbalancer_apiserver_port`, defers to `sp`;
	- `sp` - secure port, `kube_apiserver_port`;
	- `lp` - LB port, `loadbalancer_apiserver.port`, defers to the secure port;
	- `ip` - the node IP, defers to the ansible IP;
	- `aip` - `access_ip`, defers to the ip.

# Downloads
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/downloads.md)

- Kubespray supports several download/upload modes. The default is:
	- Each node downloads binaries and container images on its own, which is `download_run_once: False`.
	- For K8s apps, pull policy is `k8s_image_pull_policy: IfNotPresent`.
	- For system managed containers, like kubelet or etcd, pull policy is `download_always_pull: False`, which is pull if only the wanted repo and tag/sha256 digest differs from that the host has.
- There is also a "pull once, push many" mode as well:
	- Setting `download_run_once: True` will make kubespray download container images and binaries only once and then push them to the cluster nodes. The default download delegate node is the first `kube_control_plane`.
	- Set `download_localhost: True` to make localhost the download delegate. This can be useful if cluster nodes cannot access external addresses. To use this requires that the container runtime is installed and running on the Ansible master and that the current user is either in the docker group or can do passwordless sudo, to be able to use the container runtime. **Note**: even if `download_localhost` is false, files will still be copied to the Ansible server (local host) from the delegated download node, and then distributed from the Ansible server to all cluster nodes.

> [!Note]
> When `download_run_once` is true and `download_localhost` is false, all downloads will be done on the delegate node, including downloads for container images that are not required on that node. As a consequence, the storage required on that node will probably be more than if download_run_once was false, because all images will be loaded into the storage of the container runtime on that node, instead of just the images required for that node.

- On caching:
	- When `download_run_once` is True, all downloaded files will be cached locally in `download_cache_dir`, which defaults to `/tmp/kubespray_cache`. On subsequent provisioning runs, this local cache will be used to provision the nodes, minimizing bandwidth usage and improving provisioning time. Expect about 800 MB of disk space to be used on the ansible node for the cache. Disk space required for the image cache on the kubernetes nodes is a much as is needed for the largest image, which is currently slightly less than 150 MB.
	- By default, if `download_run_once` is false, kubespray will not retrieve the downloaded images and files from the download delegate node to the local cache, or use that cache to pre-provision those nodes. If you have a full cache with container images and files and you don’t need to download anything, but want to use a cache - set `download_force_cache` to True.
	- By default, cached images that are used to pre-provision the remote nodes will be deleted from the remote nodes after use, to save disk space. Setting `download_keep_remote_cache` will prevent the files from being deleted. This can be useful while developing kubespray, as it can decrease provisioning times. As a consequence, the required storage for images on the remote nodes will increase from 150 MB to about 550 MB, which is currently the combined size of all required container images.
- Container images and binary files are described by the vars like `foo_version`, `foo_download_url`, `foo_checksum` for binaries and `foo_image_repo`, `foo_image_tag` or optional `foo_digest_checksum` for containers.
- Container images may be defined by its repo and tag, for example: `andyshinn/dnsmasq:2.72`. Or by repo and tag and sha256 digest: `andyshinn/dnsmasq@sha256:7c883354f6ea9876d176fe1d30132515478b2859d6fc0cbf9223ffdc09168193`.
- Note, the SHA256 digest and the image tag must be both specified and correspond to each other. The given example above is represented by the following vars:
```bash
dnsmasq_digest_checksum: 7c883354f6ea9876d176fe1d30132515478b2859d6fc0cbf9223ffdc09168193
dnsmasq_image_repo: andyshinn/dnsmasq
dnsmasq_image_tag: '2.72'
```
- The full list of available vars may be found in the download's ansible role defaults. Those also allow to specify custom urls and local repositories for binaries and container images as well. See also the DNS stack docs for the related intranet configuration, so the hosts can resolve those urls and repos.

# Adding/Replacing a Node
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/nodes.md)

### Limitation: Removal of first `kube_control_plane` and `etcd-master`
* Currently you can't remove the first node in your `kube_control_plane` and `etcd-master` list. If you still want to remove this node you have to:
	1. Change order of current control planes
		* Modify the order of your control plane list by pushing your first entry to any other position. E.g. if you want to remove `node-1` of the following example:
		```yaml
		  children:
		    kube_control_plane:
		      hosts:
		        node-1:
		        node-2:
		        node-3:
		    kube_node:
		      hosts:
		        node-1:
		        node-2:
		        node-3:
		    etcd:
		      hosts:
		        node-1:
		        node-2:
		        node-3:
		```
		* change your inventory to:
		```yaml
		  children:
		    kube_control_plane:
		      hosts:
		        node-2:
		        node-3:
		        node-1:
		    kube_node:
		      hosts:
		        node-2:
		        node-3:
		        node-1:
		    etcd:
		      hosts:
		        node-2:
		        node-3:
		        node-1:
		```
	2. Upgrade the cluster
		* run `upgrade-cluster.yml` or `cluster.yml`. Now you are good to go on with the removal.

### Adding/replacing a worker node
* This should be the easiest.
1. Add new node to the inventory.
2. Run `scale.yaml`
	* You can use `--limit=NODE_NAME` to limit Kubespray to avoid disturbing other nodes in the cluster.
	* Before using `--limit` run playbook `facts.yml` without the limit to refresh facts cache for all nodes.
3. Remove an old node with `remove-node.yaml`
	* With the old node still in the inventory, run `remove-node.yml`. You need to pass `-e node=NODE_NAME` to the playbook to limit the execution to the node being removed.
	* If the node you want to remove is not online, you should add `reset_nodes=false` and `allow_ungraceful_removal=true` to your `extra-vars: -e node=NODE_NAME -e reset_nodes=false -e allow_ungraceful_removal=true`. Use this flag *even when you remove other types of nodes like a control plane or etcd nodes*.
4. Remove the node from the inventory.
	* That's it.

### Adding/replacing a control plane node
1. Run `cluster.yml`
	* Append the new host to the inventory and run `cluster.yml`. You can NOT use `scale.yml` for that.
2. Restart the kube-system/nginx-proxy
	* In all hosts, restart nginx-proxy pod. This pod is a local proxy for the apiserver. Kubespray will update its static config, but it needs to be restarted in order to reload.
		```bash
		# run in every host
		docker ps | grep k8s_nginx-proxy_nginx-proxy | awk '{print $1}' | xargs docker restart
		```
3. Remove old control plane nodes
	* With the old node still in the inventory, run `remove-node.yml`.
	* You need to pass `-e node=NODE_NAME` to the playbook to limit the execution to the node being removed.
	* If the node you want to remove is not online, you should add `reset_nodes=false` and `allow_ungraceful_removal=true` to your extra-vars.

### Replacing a first control plane node
1. Change control plane nodes order in inventory
	* from
		```
		[kube_control_plane]
		 node-1
		 node-2
		 node-3
		```
	* to
		```
		[kube_control_plane]
		 node-2
		 node-3
		 node-1
		```
2. Remove old first control plane node from cluster
	* With the old node still in the inventory, run `remove-node.yml`. You need to pass `-e node=node-1` to the playbook to limit the execution to the node being removed.
	* If the node you want to remove is not online, you should add `reset_nodes=false` and `allow_ungraceful_removal=true` to your extra-vars.
3. Edit cluster-info configmap in kube-public namespace
	* `kubectl edit cm -n kube-public cluster-info`
	* Change ip of old `kube_control_plane` node with ip of live `kube_control_plane` node (server field). Also, update `certificate-authority-data` field if you changed certs.
4. Add new control plane node
	* update inventory (if needed)
	* Run `cluster.yml` with `--limit=kube_control_plane`

### Adding an etcd node
* You need to make sure there are always an odd number of etcd nodes in the cluster. In such a way, this is always a replacement or scale up operation. Either add two new nodes or remove an old one.
1. Add the new node running `cluster.yml`
	* Update the inventory and run `cluster.yml` passing `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes`. If the node you want to add as an etcd node is already a worker or control plane node in your cluster, you have to remove him first using `remove-node.yml`.
	* Run `upgrade-cluster.yml` also passing `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes`. This is necessary to update all etcd configuration in the cluster.
	* At this point, you will have an even number of nodes. Everything should still be working, and you should only have problems if the cluster decides to elect a new etcd leader before you remove a node. Even so, running applications should continue to be available.
	* If you add multiple etcd nodes with one run, you might want to append `-e etcd_retries=10` to increase the amount of retries between each etcd node join. Otherwise the etcd cluster might still be processing the first join and fail on subsequent nodes. `etcd_retries=10` might work to join 3 new nodes.
2. Add the new node to apiserver config
	* In every control plane node, edit `/etc/kubernetes/manifests/kube-apiserver.yaml`. Make sure the new etcd nodes are present in the apiserver command line parameter `--etcd-servers=...`.

### Removing an etcd node
1. Remove an old etcd node
	* With the node still in the inventory, run `remove-node.yml` passing `-e node=NODE_NAME` as the name of the node that should be removed. If the node you want to remove is not online, you should add `reset_nodes=false` and `allow_ungraceful_removal=true` to your extra-vars.
2. Make sure only remaining nodes are in your inventory
	* Remove `NODE_NAME` from your inventory file.
3. Update kubernetes and network configuration files with the valid list of etcd members
	* Run `cluster.yml` to regenerate the configuration files on all remaining nodes.
4. Remove the old etcd node from apiserver config
	* In every control plane node, edit `/etc/kubernetes/manifests/kube-apiserver.yaml`. Make sure only active etcd nodes are still present in the apiserver command line parameter `--etcd-servers=...`.
5. Shutdown the old instance
	* That's it.

# Public Download Mirror
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/mirror.md)

* The public mirror is useful to make the public resources download quickly in some areas of the world. (such as China).
### Configuring kubespray to use a mirror site
* You can follow the [offline](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/offline-environment.md) to config the image/file download configuration to the public mirror site. If you want to download quickly in China, the configuration can be like:
```yaml
gcr_image_repo: "gcr.m.daocloud.io"
kube_image_repo: "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo: "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"

files_repo: "https://files.m.daocloud.io"
```
* Use mirror sites only if you trust the provider. The Kubespray team cannot verify their reliability or security. You can replace the `m.daocloud.io` with any site you want.

### Example usage full steps
* You can follow the full steps to use the kubespray with mirror. for example:
* Install Ansible according to Ansible installation guide then run the following steps:
```bash
# Copy ``inventory/sample`` as ``inventory/mycluster``
cp -rfp inventory/sample inventory/mycluster

# Update Ansible inventory file with inventory builder
declare -a IPS=(10.10.1.3 10.10.1.4 10.10.1.5)
CONFIG_FILE=inventory/mycluster/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]}

# Use the download mirror
cp inventory/mycluster/group_vars/all/offline.yml inventory/mycluster/group_vars/all/mirror.yml
sed -i -E '/# .*\{\{ files_repo/s/^# //g' inventory/mycluster/group_vars/all/mirror.yml
tee -a inventory/mycluster/group_vars/all/mirror.yml <<EOF
gcr_image_repo: "gcr.m.daocloud.io"
kube_image_repo: "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo: "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"
files_repo: "https://files.m.daocloud.io"
EOF

# Review and change parameters under ``inventory/mycluster/group_vars``
cat inventory/mycluster/group_vars/all/all.yml
cat inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml

# Deploy Kubespray with Ansible Playbook - run the playbook as root
# The option `--become` is required, as for example writing SSL keys in /etc/,
# installing packages and interacting with various systemd daemons.
# Without --become the playbook will fail to run!
ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
```
* The above steps are by adding the "Use the download mirror" step to the `README.md` steps.

### Community-run mirror sites
* DaoCloud (China)
	- [image-mirror](https://github.com/DaoCloud/public-image-mirror)
	- [files-mirror](https://github.com/DaoCloud/public-binary-files-mirror)

# Offline Environment
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/offline-environment.md)

* In case your servers don't have access to the internet directly (for example when deploying on premises with security constraints), you need to get the following artifacts in advance from another environment where has access to the internet.
	* Some static files (zips and binaries)
	* OS packages (rpm/deb files)
	* Container images used by Kubespray. Exhaustive list depends on your setup
	* \[Optional\] Python packages used by Kubespray (only required if your OS doesn't provide all python packages/versions listed in `requirements.txt`)
	* \[Optional\] Helm chart files (only required if `helm_enabled=true`)
* Then you need to setup the following services on your offline environment:
	* an HTTP reverse proxy/cache/mirror to serve some static files (zips and binaries)
	* an internal Yum/Deb repository for OS packages
	* an internal container image registry that need to be populated with all container images used by Kubespray
	* \[Optional\] an internal PyPi server for python packages used by Kubespray
	* \[Optional\] an internal Helm registry for Helm chart files
* You can get artifact lists with [`generate_list.sh`](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/offline/generate_list.sh) script. In addition, you can find some tools for offline deployment under [contrib/offline](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/offline/README.md).

### Configure inventory
* Once all artifacts are accessible from your internal network, adjust the following variables in [your inventory](https://github.com/kubernetes-sigs/kubespray/blob/master/inventory/sample/group_vars/all/offline.yml) to match your environment:
```yaml
# Registry overrides
kube_image_repo: "{{ registry_host }}"
gcr_image_repo: "{{ registry_host }}"
docker_image_repo: "{{ registry_host }}"
quay_image_repo: "{{ registry_host }}"
github_image_repo: "{{ registry_host }}"

kubeadm_download_url: "{{ files_repo }}/kubernetes/{{ kube_version }}/kubeadm"
kubectl_download_url: "{{ files_repo }}/kubernetes/{{ kube_version }}/kubectl"
kubelet_download_url: "{{ files_repo }}/kubernetes/{{ kube_version }}/kubelet"
# etcd is optional if you **DON'T** use etcd_deployment=host
etcd_download_url: "{{ files_repo }}/kubernetes/etcd/etcd-{{ etcd_version }}-linux-{{ image_arch }}.tar.gz"
cni_download_url: "{{ files_repo }}/kubernetes/cni/cni-plugins-linux-{{ image_arch }}-{{ cni_version }}.tgz"
crictl_download_url: "{{ files_repo }}/kubernetes/cri-tools/crictl-{{ crictl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
# If using Calico
calicoctl_download_url: "{{ files_repo }}/kubernetes/calico/{{ calico_ctl_version }}/calicoctl-linux-{{ image_arch }}"
# If using Calico with kdd
calico_crds_download_url: "{{ files_repo }}/kubernetes/calico/{{ calico_version }}.tar.gz"
# Containerd
containerd_download_url: "{{ files_repo }}/containerd-{{ containerd_version }}-linux-{{ image_arch }}.tar.gz"
runc_download_url: "{{ files_repo }}/runc.{{ image_arch }}"
nerdctl_download_url: "{{ files_repo }}/nerdctl-{{ nerdctl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
# Insecure registries for containerd
containerd_insecure_registries:
    "{{ registry_addr }}"："{{ registry_host }}"

# CentOS/Redhat/AlmaLinux/Rocky Linux
## Docker / Containerd
docker_rh_repo_base_url: "{{ yum_repo }}/docker-ce/$releasever/$basearch"
docker_rh_repo_gpgkey: "{{ yum_repo }}/docker-ce/gpg"

# Fedora
## Docker
docker_fedora_repo_base_url: "{{ yum_repo }}/docker-ce/{{ ansible_distribution_major_version }}/{{ ansible_architecture }}"
docker_fedora_repo_gpgkey: "{{ yum_repo }}/docker-ce/gpg"
## Containerd
containerd_fedora_repo_base_url: "{{ yum_repo }}/containerd"
containerd_fedora_repo_gpgkey: "{{ yum_repo }}/docker-ce/gpg"

# Debian
## Docker
docker_debian_repo_base_url: "{{ debian_repo }}/docker-ce"
docker_debian_repo_gpgkey: "{{ debian_repo }}/docker-ce/gpg"
## Containerd
containerd_debian_repo_base_url: "{{ ubuntu_repo }}/containerd"
containerd_debian_repo_gpgkey: "{{ ubuntu_repo }}/containerd/gpg"
containerd_debian_repo_repokey: 'YOURREPOKEY'

# Ubuntu
## Docker
docker_ubuntu_repo_base_url: "{{ ubuntu_repo }}/docker-ce"
docker_ubuntu_repo_gpgkey: "{{ ubuntu_repo }}/docker-ce/gpg"
## Containerd
containerd_ubuntu_repo_base_url: "{{ ubuntu_repo }}/containerd"
containerd_ubuntu_repo_gpgkey: "{{ ubuntu_repo }}/containerd/gpg"
containerd_ubuntu_repo_repokey: 'YOURREPOKEY'
```
* For the OS specific settings, just define the one matching your OS. If you use the settings like the one above, you'll need to define in your inventory the following variables:
	* `registry_host`: Container image registry. If you don't use the same repository path for the container images that the ones defined in [Download's role defaults](https://github.com/kubernetes-sigs/kubespray/blob/master/roles/download/defaults/main/main.yml) , you need to override the `*_image_repo` for these container images. If you want to make your life easier, use the same repository path, you won't have to override anything else.
	* `registry_addr`: Container image registry, but only have `[domain or ip]:[port]`.
	* `files_repo`: HTTP webserver or reverse proxy that is able to serve the files listed above. Path is not important, you can store them anywhere as long as it's accessible by kubespray. It's recommended to use `*_version` in the path so that you don't need to modify this setting every time kubespray upgrades one of these components.
	* `yum_repo`/`debian_repo`/`ubuntu_repo`: OS package repository depending on your OS, should point to your internal repository. Adjust the path accordingly.

### Install kubespray python packages
#### Recommended way: kubespray container image
* The easiest way is to use [kubespray container image](https://quay.io/kubespray/kubespray) as all the required packages are baked in the image. Just copy the container image in your private container image registry and you are all set!

#### Manual installation
* Look at the `requirements.txt` file and check if your OS provides all packages out-of-the-box (Using the OS package manager). For those missing, you need to either use a proxy that has Internet access (typically from a DMZ) or setup a PyPi server in your network that will host these packages.
* If you're using an HTTP(S) proxy to download your python packages:
```bash
sudo pip install --proxy=https://[username:password@]proxyserver:port -r requirements.txt
```
* When using an internal PyPi server:
```bash
# If you host all required packages
pip install -i https://pypiserver/pypi -r requirements.txt

# If you only need the ones missing from the OS package manager
pip install -i https://pypiserver/pypi package_you_miss
```

### Run kubespray as usual
* Once all artifacts are in place and your inventory properly set up, you can run kubespray with the regular `cluster.yaml` command:
	```bash
	ansible-playbook -i inventory/my_airgap_cluster/hosts.yaml -b cluster.yml
	```
* If you use Kubespray Container Image, you can mount your inventory inside the container:
```bash
docker run --rm -it -v path_to_inventory/my_airgap_cluster:inventory/my_airgap_cluster myprivateregisry.com/kubespray/kubespray:v2.14.0 ansible-playbook -i inventory/my_airgap_cluster/hosts.yaml -b cluster.yml
```

# Offline Deployment
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/contrib/offline/README.md)
### manage-offline-container-images.sh
* Container image collecting script for offline deployment
* This script has two features:
	1. Get container images from an environment which is deployed online.
	2. Deploy local container registry and register the container images to the registry.
* Step(1) should be done online site as a preparation, then we bring the gotten images to the target offline environment. if images are from a private registry, you need to set `PRIVATE_REGISTRY` environment variable. Then we will run step(2) for registering the images to local registry.
* Step(1) can be operated with:
	* `manage-offline-container-images.sh   create`
* Step(2) can be operated with:
	* `manage-offline-container-images.sh   register`

### generate_list.sh
* This script generates the list of downloaded files and the list of container images by `roles/download/defaults/main/main.yml` file.
* Run this script will execute `generate_list.yml` playbook in kubespray root directory and generate four files, all downloaded files url in `files.list`, all container images in `images.list`, jinja2 templates in `*.template`.
```text
./generate_list.sh
tree temp
temp
├── files.list
├── files.list.template
├── images.list
└── images.list.template
0 directories, 5 files
```
* In some cases you may want to update some component version, you can declare version variables in ansible inventory file or group_vars, then run `./generate_list.sh -i [inventory_file]` to update `file.list` and `images.list`.

### manage-offline-files.sh
* This script will download all files according to `temp/files.list` and run nginx container to provide offline file download.
* Step(1) generate files.list
	* `./generate_list.sh`
* Step(2) download files and run nginx container
	* `./manage-offline-files.sh`
* when nginx container is running, it can be accessed through `http://127.0.0.1:8080/`.

# Network Checker Application
> [source](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/netcheck.md)

* With the `deploy_netchecker` var enabled (defaults to `false`), Kubespray deploys a Network Checker Application from the 3rd side `mirantis/k8s-netchecker` docker images. It consists of the server and agents trying to reach the server by usual for Kubernetes applications network connectivity meanings. Therefore, this automatically verifies a pod to pod connectivity via the cluster IP and checks if DNS resolve is functioning as well.
* The checks are run by agents on a periodic basis and cover standard and host network pods as well. The history of performed checks may be found in the agents' application logs.
* To get the most recent and cluster-wide network connectivity report, run from any of the cluster nodes:
```bash
curl http://localhost:31081/api/v1/connectivity_check
```
* Note that Kubespray does not invoke the check but only deploys the application, if requested.
* There are related application specific variables:
```yaml
netchecker_port: 31081
agent_report_interval: 15
netcheck_namespace: default
```
* Note that the application verifies DNS resolve for FQDNs comprising only the combination of the `netcheck_namespace.dns_domain` vars, for example the `netchecker-service.default.svc.cluster.local`. If you want to deploy the application to the non default namespace, make sure as well to adjust the `searchdomains` var so the resulting search domain records to contain that namespace, like:
```yaml
search: foospace.cluster.local default.cluster.local ...
nameserver: ...
```

