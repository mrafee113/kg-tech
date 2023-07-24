> - [vagrant-libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt)
> 	- [ubuntu installation guide](https://vagrant-libvirt.github.io/vagrant-libvirt/installation.html#ubuntu--debian)

* `sudo apt install vagrant`
* install `libvirt` and `qemu`
* `sudo apt-mark hold vagrant-libvirt`
* `sudo apt install ebtables libguestfs-tools`
* `sudo apt install ruby-fog-libvirt`
* export `http_proxy` and `https_proxy` (v2ray worked)
* `vagrant plugin install vagrant-libvirt`