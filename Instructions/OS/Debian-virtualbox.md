> [!Warning]
> This is only for setting up debian-11 (DVD) on virtualbox.

* `netselect`
* Usually the username is `debianu` and password is `jeez`.
* sudo is not installed at first. Therefore the command cannot be found error will be shown.
	* first enter root mode: `su -`
	* then `nano /etc/apt/sources.list`
		* comment out `deb cdrom:...`
		* then add `deb http://debian.snt.utwente.nl/debian bullseye main contrib`
	* `apt update`
	* `apt install sudo`
	* add the user `debianu` to sudoers file: `usermod -aG sudo debianu`
	* then logout for user group change to take effect.
* apt-source mirrors
	* `http://debian.snt.utwente.nl/debian`
	* `http://mirror.arvancloud.ir/debian`
	* `http://mirror.arvancloud.ir/debian-security`
* virtualbox guest additions:
	* `apt install dkms linux-headers-$(uname -r) buils-essentials module-assistant make gcc libxt6 libxmu6`
	* `m-a prepare`
	* VBox -> Devices -> Insert Guest Additions CD Image
	* `mkdir /media/cdrom1`
	* `mount -t auto /dev/cdrom /media/cdrom1`
	* `/media/cdrom1/VBoxLinuxAdditions.run`
* Connec to v2ray on local machine.
	* There should be a v2ray installed on the laptop.
	* Change configs of v2ray:
		* The address of the inbound should be IPv4, but not `"0.0.0.0"`, because that way v2ray switches to IPv6. The IP should be that of the IP of the v2ray host, on the shared network. For example, if you connect to the internet through the `192.168.1.0` network, because that's what the router created, and you have configured the VMs to bridge and therefore connected to this, the IP should be `192.168.1.105` which (as of now) belongs to the laptop.
		* So the configuration of v2ray must have double the number of its default inbounds. There are 2 default inbounds, one for socks and another for http. And these 2 default ones listen on `127.0.0.1`. Now there should be 2 more just like them, except these new ones should listen on `192.168.1.105`.
	* Install `tsocks`, and configure it:
		* In tsocks configuration you should add the network that you want to operate on as local:
			* `local = 192.168.1.0/255.255.255.0`
		* The server should be the IP address of the host of v2ray, which is the laptop:
			* `server = 192.168.1.105`
		* And the port should be that of v2ray socks:
			* `server_port = 10808`
		* Do not forget that the `server_type` should be set to 5 to use **socks5**.
	* Also you can use the v2ray http proxy as well, for example:
		* `pip install --user --proxy=http://192.168.1.105:10809 ansible`
	* Do not forget to add the firewall rules if you have activated the firewall:
		* `ufw add 10808/tcp`
		* `ufw add 10808/udp`
		* `ufw add 10809/tcp`
		* `ufw add 10809/udp`