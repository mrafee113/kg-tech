* resources
	* [github](https://github.com/kubernetes-sigs/kubespray)
		* [requirements](https://github.com/kubernetes-sigs/kubespray#requirements)
		* [kubespray vs](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/comparisons.md)
		* [getting started](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/getting-started.md) (ansible)
		* [ansible](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible.md#installing-ansible)
		* [ansible inventory and tags](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/ansible.md)
		* [network plugins](https://github.com/kubernetes-sigs/kubespray#network-plugins)
		* [vagrant install](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/vagrant.md)
		* [downloaded artifacts](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/downloads.md)
		* [adding/replacing a node](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/nodes.md)
		* [upgrades basics](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/nodes.md) (upgrading kubernetes)
		* [hardening](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/hardening.md) (secure kubernetes)
		* [mirror](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/mirror.md) (public mirror for quicker download)
	* [kubespray.io](https://kubespray.io/#/)

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

