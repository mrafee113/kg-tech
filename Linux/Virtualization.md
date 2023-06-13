### Hypervisor
* it's a software platform
* utilizises hardware for use by virtual machines which are `guests` of the hypervisor
* common linux hypervisors:
	* Xen
		* does not need an os to run
		* called `bare-metal`
		* `type-1` hypervisor
	* KVM
		* linux kernel module for virtualization
		* uses `libvirt` daemon
		* `type-1` (why?) and `type-2` hypervisor
		* need a linux os to run
	* VirtualBox
		* `type-2` hypervisor
* `migration`
	Moving a guest to another hypervisor.
	If the guest is running it's called `live migration`.

### Virtual Machines
* types
	* fully virtualized
		* the guest is completely unaware of it being a virtual machine
		* there's no additional software drivers that translate the instructions to a simulated or a real hardware
			* I have no idea what this means!!
	* paravirtualized (PVM)
		* aware that it's a vm
		* utilization of the resources of the hypervisor
			* use of a modified kernel
			* use of special drivers *`(guest drivers)`*
		* better performance because of special software drivers
	* hybrid
		* unmodified os
		* special drivers *`(guest drivers)`*
* types of `disk images`
	* COW `(copy-on-write)`
		* aka thin provisioning aka sparse images
		* it's defined as somewhat empty, although it has metadata.
		* increases size as new data arrives.
		* `qcow2` is a QEMU COW file format
	* RAW
		* aka full disk type
		* pre-allocated space
		* better performance because the hypervisor doens't constantly need to check disk space
* D-BUS machine ID
	* validate existence of a D-BUS machine ID exists: `dbus-uuidgen --ensure`
		* successful if nothing shows
	* get D-BUS machine ID: `dbus-uuidgen --get`
	* no two VM running on a hypervisor should have the same D-BUS machine ID.
	* located at `/var/lib/dbus/machine-id` -> `/etc/machine-id`

### Cloud
* `ssh-keygen` for creating public and private ssh key pair
	* private key is stored locally in `~/.ssh/`
		* permission `0600`
	* public key is stored in the cloud
		* `ssh-copy-id -i [public key] [user]@[cloud server]`
			* will be stored at `~/.ssh/authorized_keys`
		* permission `0644`
* cloud initialization
	* `cloud-init`
	* cloudconfig.yaml
	```yaml
	#cloud-config
	timezone: Africa/Dar_es_Salaam
	hostname: test-system
	
	# update the system when it first boots up
	apt_update: true
	apt_upgrade: true
	
	# install the nginx web server
	packages:
	- nginx
	```

### Containers
* uses the os kernel
	* makes it far better in performance than that of VMs on hypervisors
	* far less overhead
* great flexibility
	* live migration is always applicable
* container techonologies for linux
	* docker
	* kubernetes
	* LXD/LXC
	* system-nspawn
	* OpenShift
* control groups mechanism
	`cgroups` is a mechanism within the linux kernel that helps partition resouces like memory, processor time, disk storage and network bandwidth.
