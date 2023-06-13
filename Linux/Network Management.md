### Commands
- `nmcli` - (1) command-line tool for controlling NetworkManager
- `hostname`
  - (5) Local hostname configuration file
  - (1) show or set the system's host name
  - (7) hostname resolution description
- `host` - (1) DNS lookup utility
- `mtr` - (8) a network diagnostic tool
- `wget` - (1) The non-interactive network downloader.
- `curl` - (1) transfer a URL
- `ping` - (8) send ICMP ECHO_REQUEST to network hosts
- `gping` - ping but with a graph
- `tmate` - (1) terminal multiplexer with instant terminal sharing
- `ssh` - (1) OpenSSH remote login client
- `scp` - (1) OpenSSH secure file copy
- `youtube-dl` - download videos from youtube and other platforms
- `ip`
  - (8) show / manipulate routing, network devices, interfaces and tunnels
  - (7) Linux IPv4 protocol implementation
- `sftp` - (1) OpenSSH secure file transfer
- `systemd-resolve` - (1) Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver
- `resolvectl` - (1) Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver
- `tcpdump` - (8) dump traffic on a network
- `windscribe` - vpn client
- `openvpn` - (8) Secure IP tunnel daemon
- `ethtool` - (8) query or control network driver and hardware settings
- `yafc` - (1) Yet another FTP client
- `netstat` - (8) Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
- `nslookup` - (1) query Internet name servers interactively
- `traceroute`
  - (1) print the route packets trace to network host
  - (8) print the route packets trace to network host
- `route` - (8) show / manipulate the IP routing table
- `aria2c` - (1) The ultra fast download utility
- `nmap` - (1) Network exploration tool and security / port scanner
- `syncthing` - (1) Syncthing
- `ftp` - (1) Internet file transfer program
- `nmtui` - (1) Text User Interface for controlling NetworkManager
- `ncftp` - (1) Browser program for the File Transfer Protocol
- `ifconfig` - (8) configure a network interface
- `dig` - (1) DNS lookup utility

### Linux Networking Basics
* You’ll need to configure five main pieces of information in your Linux system to interact on a network:
	* the host address
	* the network address
	* the default router (sometimes called the gateway)
	* the system hostname
	* a DNS server address for resolving hostnames
* There are three different ways to configure this information in Linux systems:
	* Manually editing network configuration files
	* Using a graphical tool
	* Using command-line tools
* network configuration files
	* Every Linux distribution uses network configuration files to define the network settings required to communicate on the network. Unfortunately, though, there’s no single standard configuration file that all distributions use. Instead, different distributions use different configuration files to define the network settings. Here's a list of the most common ones:
		* Debian-based distribution -> `/etc/network/interfaces` file
		* Red Hat-based distribution -> `/etc/sysconfig/network-scripts/` dir
		* OpenSUSE distribution -> `/etc/sysconfig/network` file
	* While each of the Linux distributions uses a different method of defining the network settings, they all have similar features. Most configuration files define each of the required network settings as separate values in the configuration file.
	* For other types of Linux systems besides RedHat, storing the hostname in the `/etc/hostname` file has become somewhat of a de facto standard. However, some Linux distributions use `/etc/HOSTNAME` instead.
	* You will also need to define a DNS server so that the system can use DNS hostnames. Fortunately, all Linux systems follow this standard, and it is handled in the `/etc/resolv.conf` configuration file.
		* The `domain` entry defines the domain name assigned to the network. By default, the system will append this domain name to any hostnames that you specify.
		* The `search` entry defines any additional domains used to search for hostnames.
		* The `nameserver` entry is where you specify the DNS server assigned to your network. Some networks can have more than one DNS server; just add multiple nameserver entries in the file.
	* To help speed up connections to commonly used hosts, you can manually enter their hostnames and IP addresses into the /etc/hosts file on your Linux system. Linux will check this file before using DNS to look up the hostname.
* command-line tools
	* If you’re not working with a graphical desktop client environment, you’ll need to use the Linux command-line tools to set the network configuration information. You’ll need to know three main commands to do that:
		* `ifconfig` sets the IP address and netmask values for a network interface.
			* #todo read other docs and manpage and write a cheatsheet. you can also refer to page 285 (LPIC-2 Study Guide)
		* `iwconfig` sets the SSID and encryption key for a wireless interface.
		* `route` sets the default router address.
			* `route add default gw [ip]`
		* `iwlist` displays all of the wireless signals that your wireless card detects.
			* `iwlist wlan0 scan`
	* While the `ifconfig` and `iwconfig` commands are by far the most popular methods for retrieving and setting IP and wireless information, a newer set of programs is starting to appear in the Linux world. Simply called `ip` and `iw`, these programs allow “one-stop shopping” for all of your IP and wireless configuration needs. With the `ip` command, you can list the IP address, network mask, and router information with just a couple of commands: `ip addr show` and `ip route show`. Similarly, with the `iw` command, you can display all of the wireless statistics (such as which frequencies your wireless card is listening on) and select which bands your wireless card uses. If you find that the `ifconfig` or `iwconfig` commands don’t work in your particular Linux distribution, try using the `ip` and `iw` commands instead.
	* Three common DHCP programs are available for Linux systems:
		* `dhcpd`
		* `dhclient`
		* `pump`
		* The dhcpcd program is becoming the most popular of the three, but you’ll still see the other two used in some Linux distributions.

* packet sniffers
	* `tcptump`
	* `hex viewers`
	* `protocol analyzers`
* ip command: how to investigate further
	* ip subcommand man pages
		```text
		$ man ip
		...
		SEE ALSO
		ip-address(8), ip-addrlabel(8), ip-l2tp(8), ip-link(8), ip-maddress(8),
		ip-monitor(8), ip-mroute(8), ip-neighbour(8), ip-netns(8), ip-
		ntable(8), ip-route(8), ip-rule(8), ip-tcp_metrics(8), ip-token(8), ip-
		tunnel(8), ip-xfrm(8)
		IP Command reference ip-cref.ps
		...
		```
	* ip subcommand command help
		```text
		$ ip address help
		Usage: ip address {add|change|replace} IFADDR dev IFNAME [ LIFETIME ]
		[ CONFFLAG-LIST ]
		ip address del IFADDR dev IFNAME [mngtmpaddr]
		ip address {save|flush} [ dev IFNAME ] [ scope SCOPE-ID ]
		[ to PREFIX ] [ FLAG-LIST ] [ label LABEL ] [up]
		ip address [ show [ dev IFNAME ] [ scope SCOPE-ID ] [ master DEVICE ]
		[ type TYPE ] [ to PREFIX ] [ FLAG-LIST ]
		[ label LABEL ] [up] [ vrf NAME ] ]
		ip address {showdump|restore}
		IFADDR := PREFIX | ADDR peer PREFIX
		...
		```
* IPv4 and IPv6 are what are known as routed or routable protocols. This means they are designed in a way that make it possible for network designers to control traffic flow. Ethernet is not a routable protocol. This means that if you were to connect a bunch of devices together using nothing but Ethernet, there is very little you can do to control the flow of network traffic. Any measures to control traffic would end up similar to current routable and routing protocols.
* configuring an interface
	* list current interfaces
		* `ifconfig -a`
		* `ip link`
		* `ls /sys/class/net`
	* configure
		* `ifconfig enp1s0 192.168.50.50/24`
		* `ifconfig eth2 192.168.50.50 netmask 255.255.255.0`
		* `ifconfig eth2 192.168.50.50 netmask 0xffffff00`
		* `ifconfig enps0s8 add 2001:db8::10/24`
		* `ip address add 192.168.5.5/24 dev enp0s8`
		* `ip address add 2001:db8::10/24 dev enp0s8`
	* configuring low level options
		* low level is: `VLANs`, `ARP`, `MTUs`
		* disable/enable an interface
			* `ip link set dev enp0s8 down`
			* `ifconfig enp0s8 up`
		* set *mtu*
			* `ip link set enp0s8 mtu 2000`
			* `ifconfig enp0s3 mtu 1500`
* The routing table
	* view routing table
		* `netstat -r`
			* `-6r` for ipv6
		* `route`
			* `-6` for ipv6
		* `ip route`
			* `-6 route` for ipv6
			* the output reads as follows
				1. destination
				2. optional address followed by interface
				3. the routing protocol used to add the route
				4. the scope of the route
				5. the route's metric. this is used by dynamic routing protocols to determine the cost of the route.
				6. if it is an ipv6 route, RFC4191 route preference.
	* managin routes
		* route
			* `route add [ip] gw [gateway]`
			* `route del [ip] gw [gateway]`
		* ip route
			* `ip route add [ip] via [gateway]`
			* `ip route del [ip] via [gateway]`		

#### Discovering Open Ports
* `lsof` (list open files)
	* `-i` prints the listing of all internet network files
		* `-i4` and `-i6` for ipv4 and ipv6
		* `-i@[ip]` specifies particular host
		* `-i :[comma seperated ports]`
		* `-i@[ip]:[comma seperated ports]`
* `fuser` (find file's user)
	* Next on the list of network commands is fuser. Its main purpose is to find a “file’s user” — which involves knowing what processes are accessing what files; it also gives you some other information such as the type of access.
	* `fuser -v .` to check on the current working directory
		* `FILE` the file we are getting information about
		* `USER` the owner of the file
		* `PID`
		* `ACCESS` type of access
			* `c` current dir
			* `e` executable being run
			* `f` open file (omitted in default display mode)
			* `F` open file for writing (omitted in default display mode)
			* `r` root directory
			* `m` mmap'ed file or shared library
			* `.` placeholder (omitted in default display mode)
		* `COMMAND` the command affliated with the file
	* `-n/--namespace [protocol] [port]` find info on ports and sockets
		* `fuser -vn tcp 80`
	* `-k/--kill` can be used to kill the processes
* `netstat`
	* netstat is a very versatile network tool that is mostly used to print “network statistics”.
	* `[no option]` will display both active internet connections and unix sockets
	* `-l/--listening` only lists listening ports and sockets. if omitted, only established conns will be shown.
	* `-t/--tcp`
	* `-u/--udp`
	* `-e/--extend` will display additional information
	* `-n/--numeric` show only ports and ip addresses
* `nmap` network mapper
	* Another very powerful utility, this port scanner is executed by specifying an IP address or hostname.
	* `nmap localhost`
	* aside from a single host nmap will allow you to scan:
		* *multiple hosts*, by seperating them by spaces: `nmap localhost 192.168.1.7`
		* *host ranges*, by using a dash: `nmap 192.168.1.3-20`
		* *subnets*, by using a wildcard `nmap 192.168.1.*`. you can also exclude `nmap 192.168.1.0/24 --exclude 192.168.1.7`
	* `-p [port/program name]` to scan a particular port
		* program name like ssh
		* you can scan multiple ports by seperating them by dashes and commas
	* `-F` run a fast scan on the 100 most common ports
	* `-v` get verbose output
	* `-vv` get even more verbose output

### Persistent Network Configuration
* In any TCP/IP network, every node must configure its network adapter to match the network requirements, otherwise they will not be able to communicate with each other. Therefore, the system administrator must provide the basic configuration so the operating system will be able to setup the appropriate network interface, as well as to identify itself and the basic features of the network every time it boots.
* Linux supports virtually every network technology used to connect servers, containers, virtual machines, desktops and mobile devices. The connections between all these network nodes can be dynamic and heterogeneous, thus requiring appropriate management by the operating system running in them.

#### The Network Interface
* this is the term by which the operating system refers to the communication channel configured to work with the network hardware attached to the system, such as an ethernet or a wifi device. The exception to this is the *loopback interface*, which the operating system uses to establish a connection with itself. But the main purpose of a network interface is to provide a route through which local data can be sent and remote data can be received. Unless the network interface is properly configured, the operating system will not be able to communicate with other machines in the network.
* list which network interfaces are present on the system
	* `ip link show`
	* `nmcli device`
* Desktops and laptops running Linux usually have two or three predefined network interfaces, one for the loopback virtual interface and the others assigned to the network hardware found by the system. Servers and network appliances running Linux, on the other hand, may have tens of network interfaces, but the same principles apply to all of them. The abstraction provided by the operating system allows for the setup of network interfaces using the same methods, regardless of the underlying hardware.
* Interface Names
	* *interface type*: all interfaces start with this two-char prefix
		* `en` ethernet
		* `ib` InfiniBand
		* `sl` Serial Line IP (slip)
		* `wl` Wireless local area network (WLAN)
		* `ww` Wireless wide area network (WWAN)
	* from higher to lower *priority*, the following rules are used by the OS to name and number the network interface.
		1. Name the interface after the index provided by the BIOS or by the firmware of embedded devices e.g. `eno1`
		2. Name the interface after the PCI express slot index, as given by the BIOS or firmware e.g. `ens1`
		3. Name the interface after its address at the corresponding bus, e.g. `enp3s5`
		4. Name the interface after the interface's MAC address e.g. `enx78e7d1ea46da`
		5. Name the interface using the legacy convention e.g. `eth0`
* Interface Management
	* deprecated `ifconfig` -> replaced by `ip`
	* `ip` is capable of managing many other aspects of TCP/IP interfaces, like *routes* and *tunnels*.
	* But the many capabilities can be overkill for most ordinary tasks -> therefore there are auxiliary commands to facilitate the activation and configuration of the network interfaces.
	* `ifup` and `ifdown` can be used confg network interfaces based on interface **definitions** found in `/etc/network/interfaces`
		* All network interfaces managed by these two should be listed in said file.
		* **WARNING:** `/etc/network/interfaces` is not available on Ubuntu 18.04+ and has been replaced by **netplan**.
		* `/etc/network/interfaces` syntax
			* lines begininning with the word `auto` are used to identify the physical interfaces to be brought up when *ifup* is executed with the `-a` option. The interface name should follow the word auto on the same line. All interfaces maked auto are brought up at boot time, in the order they are listed.
			* The actual interface configuration is written in another line, starting with the word `iface`, followed by the *interface name*, *the name of the address family* that the interface uses, and *the name of the method* used to configure the interface.
				* example: `lo (loopback)`
					```text
					auto lo
					iface lo inet loopback
					```
					* 
				* example: `enp3s5`
					```text
					auto enp3s5
					iface enp3s5 inet dhcp
					```
			* The address family should be `inet` for TCP/IP networking, but there is also support for IPX networking `(ipx)`, and IPv6 networking `(inet6)`. Looback interfaces use the loopback configuration method. With the `dhcp` method, the interface will use the IP settings provided by the network's DHCP server. 
			* In networks without a DHCP server, the static method could be used instead and the IP settings provided manually in `/etc/network/interfaces`. Interfaces using the static method do not need a corresponding *auto* directive, as they are brought up  whenever the network hardware is detected.
				```text
				iface enp3s5 inet static
					address 192.168.1.2/24
					gateway 192.168.1.1
				```
			* If the same interface has more than one iface entry, then all of the configured addresses and options will be applied when bringing up that interface. This is useful to configure both IPv4 and IPv6 addresses on the same interface, as well as to configure multiple addresses of the same type on a single interface.
* Local and Remote names
	* The name by which the system identifies itself is customizable and it is good practice to define it, even if the machine is not intended to join a network. The local name often matches the network name of the machine, but this isn’t necessarily always true. If the file `/etc/hostname`exists, the operating system will use the contents of the first line as its local name, thereafter simply called the hostname.
	* `hostnamectl`
		* `hostnamectl set-hostname [name]` sets static hostname
			* `--pretty` can include all kinds of special characters
			* `--transient` defaulted to when static isn't set
	* The hostname defined in /etc/hostname is the static hostname, that is, the name which is used to initialize the system’s hostname at boot. The static hostname may be a free-form string up to 64 characters in length. However, it is recommended that it consists only of ASCII lower-case characters and no spaces or dots. It should also limit itself to the format allowed for DNS domain name labels, even though this is not a strict requirement.
	* Regarding the name of the remote network nodes, there are two basic ways the operating system can implement to match names and IP numbers: to use a local source or to use a remote server to translate names into IP numbers and vice versa.
	  The methods can be complementary to each other and their priority order is defined in the **Name Service Switch** configuration file: `/etc/nsswitch.conf`.
	* `/etc/nsswitch.conf`
		* This file is used by the system and applications to determine not only the sources for name-IP matches, but also the sources from which to obtain name-service information in a range of categories, called ***databases***.
		* The hosts database
			* The hosts database keeps track of the mapping between host names and host numbers. The line inside `nsswitch.conf` beginning with *hosts* defines the services accountable for providing the associations for it: `hosts: files dns`
			* In this example entry, files and dns are the service names that specify how the lookup process for host names will work. First, the system will look for matches in local files, then it will ask the DNS service for matches.
			* The local file for the hosts database is `/etc/hosts`, a simple text file that associates IP addresses with hostnames, one line per IP address.
				* `127.0.0.1 localhost`
					* The IP number 127.0.0.1 is the default address for the loopback interface, hence its association with the localhost name.
				* It is also possible to bind optional aliases to the same IP. Aliases can provide alternate spellings, shorter hostnames and should be added at the end of the line.
					* `192.168.1.10 foo.mydomain.org foo`
				* Formatting rules
					* Fields of the entry are separated by any number of blanks and/or tab characters.
					* Text from a # character until the end of the line is a comment and is ignored.
					* Host names may contain only alphanumeric characters, minus signs and periods.
					* Host names must begin with an alphabetic character and end with an alphanumeric character.
			* DNS service
				* Following the files service specification, the dns specification tells the system to ask a DNS service for the desired name/IP association. The set of routines responsible for this method is called the resolver and its configuration file is `/etc/resolv.conf`.
				* exmaple: `nameserve 8.8.4.4` 
				* Only one nameserver is required, but up to three nameservers can be given. The supplementary ones will be used as a fallback. If no nameserver entries are present, the default behaviour is to use the name server on the local machine.
				* The resolver can be configured to automatically add the domain to names before consulting them on the name server. For example:
					```text
					nameserver 8.8.4.4
					nameserver 8.8.8.8
					domain mydomain.org
					search mydomain.net mydomain.com
					```
					* The domain entry sets mydomain.org as the local domain name, so queries for names within this domain will be allowed to use short names relative to the local domain. The search entry has a similar purpose, but it accepts a list of domains to try when a short name is provided. By default, it contains only the local domain name.

#### NetworkManager
* Its purpose is to make network configuration as simple and automatic as possible. 
* By default NetworkManager daemon controls the network interfaces not mentioned in `/etc/network/interfaces`, it does so not to interfere with other configuration methods that may be present as well, thus modifying the unattended interfaces only.
* `nmcli` and `nmtui` are command line clients for NetworkManager. nmtui is a graphical command line tool.
* `nmcli`
	* nmcli seperates all network related properties controlled by NetworkManager in categoriez called `objects`. The object name is the main argument to nmcli.
		* `general` NetworkManager's general status and operation
		* `networking` Overall networking control
		* `radio` NetworkManager's radio switches
		* `connection` NetworkManager's connections
		* `device` Devices managed by NetworkManager
		* `agent` NetworkManager secret agent or polkit agent
		* `monitor` monitor NetworkManager changes
	* `nmcli general` shows overall connectivity status
		* `STATE` tells whether the system is connected to a network or not.
		* `CONNECTIVITY`: If the connection is limited due to external misconfiguration or access restrictions, then this column will not report the `full` connectivity status. If `portal` appears, means that extra authentication steps (usually through the web browser) are required to complete the connection process.
		* The remaining columns report the status of the wireless connections
	* In addition to *the object argument*, nmcli also needs a **command** to execute. *The status command* is used by default if no command argument is present. e.g. `nmcli general` = `nmcli general status`
	* `nmcli device wifi list` lists available wireless networks
	* `nmcli device connect [SSID] [password [password]]`
		* if the SSID is hidden you can still connect to it with appending `hidden yes`
		* if there is more than one wifi adapter, to choose which one to connect with, append: `ifname [device name]`
		* if connection is established, nmcli will store it for future use.
	* `nmcli connection show`
		* type of each conn can be `wifi`, `tun`, `gsm`, `bridhe`, etc
		* to interact with a connection, its name or UUID must be supplied.
	* `nmcli connection [up/down] [conn name/UUID]`
	* `nmcli device [connect/disconnect] [device name]` is used to activate/deactivate interfaces
	* `nmcli radio wifi [off/on]`
* NetworkManager also supports plugins to extend its functionalities. e.g. there's a plugin to support VPNs.

#### Systemd
* `systemd-resolved` to manage the local name resolution
* `systemd-networkd` to control network interfaces
	* config file directories
		* `/lib/systemd/network` the system network dir
		* `/run/systemd/network` the volatile runtime network dir
		* `/etc/systemd/network` the local administration network dir
	* configs
		* The files are processed in lexicographic order, so it is recommended to start their names with numbers to make the ordering easier to read and set.
		* Files in `/etc` have the highest priority, whilst files in `/run` take precedence over files with the same name in `/lib`. This means that if configuration files in different directories have the same name, then systemd-networkd will ignore the files with lesser priority. Separating files like that is a way to change the interface settings without having to modify the original files: modifications can be placed in `/etc/systemd/network` to override those in `/lib/systemd/network`.
		* The purpose of each configuration file depends on its suffix. File names ending in .netdev are used by systemd-networkd to create virtual network devices, such as bridge or tun devices. Files ending in .link set low-level configurations for the corresponding network interface. systemd- networkd detects and configures network devices automatically as they appear — as well as ignore devices already configured by other means — so there is little need to add these files in most situations.
		* The most important suffix is .network. Files using this suffix can be used to setup network addresses and routes. As with the other configuration file types, the name of the file defines the order in which the file will be processed.
		* config syntax
			* The network interface to which the configuration file refers to is defined in the \[Match\]\` section inside the file.
			* For example, the ethernet network interface enp3s5 can be selected within the file `/etc/systemd/network/30-lan.network` by using the Name=enp3s5 entry in the \[Match\]\ section.
			* A list of whitespace-separated names is also accepted to match many network interfaces with this same file at once. The names can contain shell-style globs, like en*. Other entries provide various matching rules, like selecting a network device by its MAC address: `MACAddress=00:16:3e:8d:2b:5b`.
			* The settings for the device are in the \[Network\] section of the file. A simple static network configuration only requires the Address and Gateway entries: `Address=192.168.0.100/24` and `Gateway=192.168.0.1`
			* To use the DHCP protocol instead of static IP addresses, the DHCP entry should be used instead: `DHCP=yes`
				* The systemd-networkd service will try to fetch both IPv4 and IPv6 addresses for the network interface. To use IPv4 only, DHCP=ipv4 should be used. Likewise, DHCP=ipv6 will ignore IPv4 settings and use the provided IPv6 address only.
	* WPA supplicant
		* Password-protected wireless networks can also be configured by systemd-networkd, but the network adapter must be already authenticated in the network before systemd-networkd can configure it. Authentication is performed by WPA supplicant, a program dedicated to configure network adapters for password protected networks.
		* The first step is to create the credentials file with command wpa_passphrase: `wpa_passphrase MyWifi > /etc/wpa_supplicant/wpa_supplicant-wlo1.conf`. This command will take the passphrase for the MyWifi wireless network from the standard input and store its hash in the `/etc/wpa_supplicant/wpa_supplicant-wlo1.conf`. Note that the filename should contain the appropriate name of the wireless interface, hence the wlo1 in the file name.
		* The systemd manager reads the WPA passphrase files in `/etc/wpa_supplicant/` and creates the corresponding service to run WPA supplicant and bring the interface up. The passphrase file created in the example will then have a corresponding service unit called `wpa_supplicant@wlo1.service`. Command `systemctl start wpa_supplicant@wlo1.service` will associate the wireless adapter with the remote access point. Command `systemctl enable wpa_supplicant@wlo1.service` makes the association automatic during boot time.
		* Finally, a .network file matching the wlo1 interface must be present in /etc/systemd/network/, as systemd-networkd will use it to configure the interface as soon as WPA supplicant finishes the association with the access point.

### Basic Network Troubleshooting
* The best way to test a network connection is to try to use your application. When that doesn’t work, there are plenty of tools available to help diagnose the problem.
* checking the log files
	* One primary reason for a lack of network connectivity is that something went wrong with the kernel loading the appropriate module for the network card hardware. The way to troubleshoot this is to look at the kernel boot messages.
	* One way to do that is with the `dmesg` command, which displays the contents of the kernel ring buffer. The kernel ring buffer contains kernel messages, but it cycles old messages out as new messages are received. If you recently booted the Linux system, the boot messages may still be in the buffer.
	* If it’s been awhile since you booted the Linux system, the kernel boot messages may have rolled out of the kernel ring buffer. In that case, you’ll need to check the log files in the `/var/log` directory. Depending on your Linux distribution, the kernel boot messages may be in the `dmesg`, `syslog`, or `messages` file.
* viewing the ARP cache
	* You can view the contents of the ARP table by using the `arp` command.
* sending test packets
	* One way to test network connectivity is to send test packets to known hosts. Linux provides the `ping` and `ping6` commands to do just that.
	* The `ping` and `ping6` commands can be used to send an ICMP echo request to an IPv4 or IPv6 address, respectively. An ICMP echo request sends a small amount of data to the destination address. If the destination address is reachable, it will send an ICMP echo reply message back to the sender with the same data that was sent to it.
	* Unfortunately, these days many hosts don’t support ICMP packets because they can be used to create a denial-of-service (DOS) attack against the host. Don’t be surprised if you try to `ping` a remote host and don’t get any responses.
* testing network routes
	* The `route` command provides information about the default router on your local network, but it doesn’t help you with determining just how your packets get to a remote destination outside your local network. The `traceroute` command can do that.
		* The `traceroute` and `traceroute6` programs can be used to show you the route a packet takes to get to its destination. They do this by sending multiple packets to the destination, incrementing the Time-To-Live (TTL) field of the IP header with each subsequent packet. Each router along the way will respond with a TTL exceeded ICMP message.
		* By default, `traceroute` sends 3 UDP packets with junk data to port 33434, incrementing it each time it sends a packet. Each line in the command’s output is a router interface the packet traverses through. The times shown in each line of the output is the round trip time for each packet. The IP address is the address of the router interface in question. If `traceroute` is able to, it uses the DNS name of the router interface. Sometimes you will see \* in place of a time. When this happens, it means that `traceroute` never received the TTL exceeded message for this packet. When you start seeing this, this often indicates that the last response is the last hop on the route.
		* If you have access to root, the `-I` option will set `traceroute` to use ICMP echo requests instead of UDP packets. This is often more effective than UDP because the destination host is more likely to respond to an ICMP echo request than the UDP packet.
		* Some organizations block ICMP echo requests and replies. To get around this, you can use TCP. By using a known open TCP port, you can guarantee the destination host will respond. To use TCP, use the `-T` option along with `-p` to specify the port. As with ICMP echo requests, you must have access to root to do this.
	* The `mtr` command (short for My Traceroute) is designed to provide real-time information about network performance. It combines the `traceroute` and `ping` commands into a single interface that continually updates in real-time.
* finding MTUs with `tracepath`
	The `tracepath` command is similar to `traceroute`. The difference is it tracks Maximum Transmission Unit (MTU) sizes along the path. The MTU is either a configured setting on a network interface or hardware limitation of the largest protocol data unit that it can transmit or receive. The `tracepath` program works the same way as `traceroute` in that it increments the TTL with each packet. It differs by sending a very large UDP datagram. It is almost inevitable for the datagram to be larger than the device with the smallest MTU along the route. When the packet reaches this device, the device will typically respond with a destination unreachable packet. The ICMP destination unreachable packet has a field for the MTU of the link it would send the packet on if it were able. `tracepath` then sends all subsequent packets with this size.
* testing client/server connectivity
	* Just being able to push `ping` or `traceroute` packets to a remote host may not necessarily prove much; sometimes you need to simulate real data across the network. A great tool for doing that is the `nc` command (short for netcat).
	* The `nc` command allows you to simulate both a server and a client from the command line. You can use the `nc` command to send data out on the network, as well as receive data from the network by specifying command-line options.
	* #todo read the man pages and/or refer to page 293 (LPIC-2 Study Guide) for options and other information about the `nc` command. make a cheatsheet.
* finding host information
	* Sometimes the problem isn’t with network connectivity but with the DNS hostname system. You can test a hostname using the `host` command.
		* `host www.linux.org`
		* `host 107.170.40.56`
	* The `host` command queries the DNS server to determine the IP addresses assigned to the specified hostname. By default, it returns all IP addresses associated with the hostname. Some hosts are supported by multiple servers in a load-balancing configuration. The `host` command will show all of the IP addresses associated with those servers.
	* Another great tool to use is the `dig` command. The `dig` command displays all of the DNS data records associated with a specific host or network.
* viewing current connections and listeners
	* The `netstat` and ss programs can be used to view the status of your current listeners and connections. As with `ifconfig`, `netstat` is a legacy tool. Both `netstat` and `ss` have similar output and options.
		* `-a` show all sockets
		* `-l` show listening sockets
		* `-p` show the process associated with the connection
		* `-n` prevent name lookups for both ports and addresses
		* `-t` show TCP connections
		* `-u` show UDP connections
* network security
	* If a client can’t connect to a network service, you may need to look into the security restriction settings for the service. Many network applications provide network security by allowing only specific hosts to connect (called a whitelist) or by blocking problematic hosts (called a blacklist).
	* The `tcp_wrappers` program is a common Linux utility that allows you to create whitelists and blacklists for network applications.
	* It does that by acting as a proxy for network applications defined in the `/etc/inetd.conf` configuration file.
	* It intercepts all packets destined to the transport ports specified in the configuration file, compares the source IP address to a database list, and then passes allowed addresses to the specified application.
	* The access lists are contained in two files:
		* `/etc/hosts.allow`
		* `/etc/hosts.deny`

#### Advanced Network Troubleshooting
* viewing open network connections
	* Sometimes it helps to be able to see just what network connections are active on a Linux system. There are two ways to troubleshoot that issue.
	* `lsof`
		* It provides a list of files that are currently open on the Linux system.
		* Since Linux treats network connections as files, any open network session will appear in the `lsof` output list.
		* The lsof command will produce lots of output. To limit the output to only network connections, use the `–i` command-line option.
	* `netstat`
		* It can provide a wealth of network information for you.
		* By default, it lists all of the open network connections on the system.
		* It produces considerable output, because normally many programs use network services on Linux systems. You can limit the output to just TCP or UDP connections by using the `–t` command-line option for TCP connections or `–u` for UDP connections.
		* You can also get a list of what applications are listening on which network ports by using the `–l` option.
* viewing network statistics
	* Yet another great feature of the `netstat` command is that the `–s` option displays statistics for the different types of packets that the system has used on the network. The `netstat` statistics output can give you a rough idea of how busy your Linux system is on the network or if there’s a specific issue with one of the protocols installed.
	* Another tool used to view network socket statistics is the `ss` command.
		* It works in a similar manner to the `netstat` command, but it can also display detailed socket information, such as the send and receive queues for the sockets.
		* By examining the send and receive queues in the sockets, you can tell if an application is having trouble keeping up with the data it sends or receives.
* scanning the network
	* The `nmap` command takes the idea (of determining what applications are listening to which network posts on your linux system), one step further and allows you to scan your local network to view what network ports other hosts have open.
	* It is somewhat powerful, so it’s not usually installed by default in Linux distributions. `sudo apt install nmap`
	* basic syntax: `nmap [scan type] [options] target`
	* The `nmap` command provides different types of network scanning, from brute-force connection attempts to stealthy connections that can slip through firewalls. The target parameter allows you to scan a specific host on the network or a range of hosts on the network based on IP addresses.
	* Be careful when running the nmap tool in a network environment. Ensure that you have permission from the administrator for each host that you scan. Because of its use by attackers, many organizations ban the use of nmap on their networks and prosecute anyone caught using it (even internal employees).
* capturing network traffic
	* When it comes to troubleshooting specific network applications, nothing can replace viewing the actual network packets that are sent between the systems on the network. Fortunately, Linux provides the `tcpdump` command just for doing that.
	* The `tcpdump` program places the network card in promiscuous mode, which enables it to capture all network traffic that it sees (not just traffic destined for the host). This allows you to sniff any type of network traffic and even use your Linux system as a crude network sniffer to troubleshoot other network issues.
	* By default, `tcpdump` captures all packets that it sees on the network interface and displays a rough description of each packet.
	* #todo read manpage for options and other info, and make a cheatsheet. Or refer to page 304 (LPIC-2 Study Guide).

### Configuring Client-side DNS
* name resolution process
	Programs that resolve names to numbers almost always use functions provided by the standard C library, which on Linux systems is the GNU project’s glibc. The first things these functions do is read the file /etc/nsswitch.conf for instructions on how to resolve that type of name. This lesson is focused on host name resolution, but the same process applies to other types of name resolution as well. Once the process reads /etc/nsswitch.conf, it looks up the name in the manner specified. Since /etc/nsswitch.conf supports plugins, what comes next could be anything. After the function is done looking up the name or number, it returns the result to the calling process.
* Understanding `/etc/nsswitch.conf`
	* Below is a simple example of /etc/nsswitch.conf from its man page:
		```text
		passwd:compat
		group:compat
		shadow:compat
		hosts:dns [!UNAVAIL=return] files
		networks:nis [NOTFOUND=return] files
		ethers:nis [NOTFOUND=return] files
		protocols:nis [NOTFOUND=return] files
		rpc:nis [NOTFOUND=return] files
		services:nis [NOTFOUND=return] files
		# This is a comment. It is ignored by the resolution functions.
		```
	* The file is organized into columns. The far left column is the type of name database. The rest of the columns are the methods the resolution functions should use to lookup a name. The methods are followed by the functions from left to right. Columns with [] are used to provide some limited conditional logic to the column immediately to the left of it.
	* Suppose a process is trying to resolve the host name learning.lpi.org. It would make an appropriate C library call (most likely gethostbyname). This function will then read /etc/nsswitch.conf. Since the process is looking up a host name, it will find the line starting with hosts. It would then attempt to use DNS to resolve the name. The next column, \[!UNAVAIL=return\] means that if the service is not unavailable, then do not try the next source, i.e., if DNS is available, stop trying to resolve the host name even if the name servers are unable to. If DNS is unavailable, then continue on to the next source. In this case, the next source is files.
	* When you see a column in the format \[result=action\], it means that when a resolver lookup of the column to the left of it is result, then action is performed. If result is preceded with a !, it means if the result is not result, then perform action. For descriptions of the possible results and actions, see the man page.
	* Now suppose a process is trying to resolve a port number to a service name. It would read the services line. The first source listed is NIS. NIS stands for Network Information Service (it is sometimes referred to as yellow pages). It is an old service that allowed central management of things such as users. It is rarely used anymore due to its weak security. The next column \[NOTFOUND=return\] means that if the lookup succeeded but the service was not found to stop looking. If the aforementioned condition does not apply, use local files.
* The `/etc/resolv.conf` file
	* The file /etc/resolv.conf is used to configure host resolution via DNS. Some distributions have startup scripts, daemons, and other tools that write to this file. Keep this in mind when manually editing this file. Check your distribution and any network configuration tools documentation if this is the case. Some tools, such as Network Manager will leave a comment in the file letting you know that manual changes will be overwritten. 
	* The file format is rather straight forward. In the far left column, you have the option name. The rest of the columns on the same line are the option’s value.
	* The most common option is the nameserver option. It is used to specify the IPv4 or IPv6 address of a DNS server. As of the date of this writing, you can specify up to three name servers. If your /etc/resolv.conf does not have a nameserver option, your system will by default use the name server on the local machine.
	* The search option is used to allow short form searches. In the example, a single search domain of lpi.org is configured. This means that any attempt to resolve a host name without a domain portion will have .lpi.org appended before the search. For example, if you were to try to search for a host named learning, the resolver would search for learning.lpi.org. You can have up to six search domains configured.
	* Another common option is the domain option. This is used to set your local domain name. If this option is missing, this defaults to everything after the first . in the machine’s host name. If the host name does not contain a ., it is assumed that the machine is part of the root domain. Like search, domain can be used for short name searches.
	* Keep in mind that domain and search are mutually exclusive. If both are present, the last instance in the file is used.
	* There are several options that can be set to affect the behavior of the resolver. To set these, use the options keyword, followed by the name of the option to set, and if applicable, a : followed by the value. Below is an example of setting the timeout option, which is the length of time in seconds the resolver will wait for a name server before giving up: `option timeout:3`
* The `/etc/hosts` file
	The file /etc/hosts is used to resolve names to IP addresses and vice versa. Both IPv4 and IPv6 are supported. The left column is the IP address, the rest are names associated with that address. The most common use for /etc/hosts is for hosts and addresses where DNS is not possible, such as loop back addresses. In the example below, IP addresses of critical infrastructure components are defined.
* systemd-resolved
	Systemd provides a service called systemd-resolved. It provides mDNS, DNS, and LLMNR. When it is running, it listens for DNS requests on 127.0.0.53. It does not provide a full fledged DNS server. Any DNS requests it receives are looked up by querying servers configured in `/etc/systemd/resolv.conf` or `/etc/resolv.conf`. If you wish to use this, use resolve for hosts in /etc/nsswitch.conf. Keep in mind that the OS package that has the systemd-resolved library may not be installed by default.
* Name Resolution Tools
	* `getent` is useful for seeing how real world requests will resolve.
		* The getent utility is used to display entries from name service databases. It can retrieve records from any source configurable by `/etc/nsswitch.conf`.
		* To use getent, follow the command with the type of name you wish to resolve and optionally a specific entry to lookup.
			* `getent hosts`
			* `getent hosts dns1.lpi.org`
		* `-s` force specify data source
			* `getent -s files hosts`
			* `getent -s dns hosts`
	* `host` is useful for simple DNS queries.
		* host is a simple program for looking up DNS entries. With no options, if host is given a name, it returns the A, AAAA, and MX record sets. If given an IPv4 or IPv6 address, it outputs the PTR record if one is available.
		* `host wikipedia.org`
		* `-t` specifies record type
			* `host -t NS lpi.org`
		* host can also be used to query a specific name server if you do not wish to use the ones in /etc/resolv.conf. Simply add the IP address or host name of the server you wish to use as the last argument: `host -t MX lpi.org dns1.easydns.com`
	* `dig` is useful for complex DNS operations that can aid with troubleshooting DNS server problems.
		* Another tool for querying DNS servers is dig. This command is much more verbose than host. By default, dig queries for A records. It is probably too verbose for simply looking up an IP address or host name. dig will work for simple lookups, but it is more suited for troubleshooting DNS server configuration.
		* `dig learning.lpi.org`
			* As you can see, dig provides a lot of information. The output is divided into sections. The first section displays information about the version of dig installed and the query sent, along with any options used for the command. Next it shows information about the query and the response.
			* The next section shows information about EDNS extensions used and the query. In the example, the cookie extension is used. dig is looking for an A record for learning.lpi.org.
			* The next section shows the result of the query. The number in the second column is the TTL of the resource in seconds.
			* The rest of the output provides information about the domain’s name servers, including the NS records for the server along with the A and AAAA records of the servers in the domain’s NS record.
		* `-t` specify record type
		* options for fine tuning output and query
			* `+short` suppress all output except the result
			* `+nocookie` turns off cookie EDNS extension

### inetd and xinetd
* superdaemon to listen for incoming network connections
	* Network services such as web servers, email servers and print servers usually run as a standalone service listening on a dedicated network port. All of these standalone services are running side-by-side.
	* In former times the availability of computer resources had been much smaller. To run many services in standalone mode in tandem was not a good option. Instead a so-called superdaemon had been used to listen for incoming network connections and start the appropriate service on demand. This method of building a network connection took a little more time. Well known superdaemons are `inetd` and `xinetd`. On current systems based on systemd the `systemd.socket` unit can be used in a similar way.
	* `/etc/xinetd.d/` and `/etc/xinetd.conf`
		* `service` lists the service xitend has to control. you may use either a port number or the name mapped to the port number in `/etc/services`
		* detailed settings begin with an opening curly bracket
		* `disable` to activate these settings, set this to no. if you want to disable the settings temporarily you may set it to yes.
		* `socket_type` you can choose `stream` for TCP sockets, or `dgram` for UDP sockets.
		* `protocol` choose either TCP or UDP
		* `wait` for TCP connections this is set to no usually
		* `user` the service started in this line will be owned by this user
		* `server` full path to the service which should be started by xinetd
		* `server_args` you can add options for the service here. if started by a super-server many services require a special option. for ssh this would be the -i option.
		* `flags` you may choose IPv4, IPv6 and others
		* `interface` the network interface which xinetd has to control. note: you may also choose the `bind` directive, which is just a synonym for `interface`.
		* finish with a closing bracket

### DNS Server
* For Linux systems, BIND is a popular package that provides DNS. Setting up DNS via BIND can be a complicated process, involving modifying configuration files and creating and maintaining zones, in addition to securing the DNS server and its various transactions.
* understanding DNS and BIND
	* DNS
		* FQDN: fully qualified domain name
		* name resolution: the process of translating between a system’s FQDN and its IP address
		* Historically a system’s local `/etc/hosts` file was used to provide name resolution. If desired, you can still use this file for that purpose on very small local networks that consist of a few systems.
		* Name Servers
			* **Primary (Master) Server**: This name server is required, and it is considered the authoritative server, because it has authority over the domain; the information it contains (such as the domain’s name and what subdomains exist in that domain) is called authoritative information.
			* **Secondary (Slave) Server**: This name server is optional; it is considered an authoritative server, but it receives its information from the primary server and is often used for performance reasons to offload the primary server’s burden.
			* **Caching Server**: Often used by ISPs, this name server receives its information from the primary (or secondary) server, and it stores the information locally in its own cache, which provides faster name resolution.
			* **Forwarding Server**: This specialized caching server also forwards queries to the other servers if it cannot find the needed query answer in its cache; it is often implemented for security reasons and can also be implemented on the DNS client side to improve name resolution performance.
		* for more info refer to page 372 (LPIC-2 Study Guide) or the DNS chapter of TCP-IP Illustrated.
	* **BIND**: *Berkeley Internet Name Domain* (BIND) provides DNS protocol implementation. BIND got its start more than 30 years ago at the University of California at Berkeley, and it is open source. It also is the most popular DNS software available.
	* BIND Alternatives
		* `djbdns` software is actually several DNS applications, including `tinydns`, which was very popular around the turn of the millennium. The `djbdns` software collection was released to the public domain in 2007 and resulted in several project forks, including the Debian project’s `dbndns` and `ndjbdns`.
		* `dnsmasq`
			* Often installed by default on various distributions (such as Ubuntu), the `dnsmasq` utility provides a lightweight combination of DNS and Dynamic Host Control Protocol (DHCP) services as well as a few others.
			* The software is designed for small networks.
			* For DNS services, it acts as a DNS forwarding server and can maintain a small cache so that not all queries need to be forwarded to other servers.
			* It is fairly easy to configure, and it includes the `/etc/hosts` file’s contents in its configuration.
			* Some turn off many of the `dnsmasq` utility features and configure it to act as only a local cache and forwarding server. This can greatly improve name resolution speeds.
		* `pdnsd`
			* PowerDNS is a full-service DNS server implementation.
			* It is free, is open source, and has the GPL license.
			* The PowerDNS software has a modular approach in that one application provides an authoritative server, while a separate software application provides recursive server features.
			* It also offers an application programming interface (API) for managing zone data, and the data can be stored either in plain-text files or in a third-party database, such as MySQL, PostgreSQL, or MariaDB.
* configuring DNS on linux
	* How you configure BIND on your Linux system(s) depends on your DNS goals.
		* If you are a domain owner, you’ll need at least two name servers.
			* On one name server, you will need to configure DNS via BIND as an authoritative primary server to handle DNS name resolution queries.
			* Your second required server can be any of the other three types—authoritative secondary, caching, or forwarding—depending on your domain’s performance needs.
		* If you’re primarily configuring your system to be a DNS client (resolver), you may want to consider configuring your system to be a caching-only server (if it’s not preconfigured this way). By caching name resolutions, resolver speeds can improve significantly.
	* installing BIND
		* The BIND 9 software is in the `bind9` or `bind` package, depending on your distribution.
		* Also, you’ll need various utilities to troubleshoot and manage it, which are in the `bindutils` package.
		* For ubuntu it's `bind9`, `bind9utils` and `bind9-doc`.
		* On ubuntu, once installed, the documentation is located in the `/usr/share/doc/bind9/` directory for review. The Ubuntu `/etc/bind/ named.conf` file strongly recommends that you do so prior to modifying it.
	* comparing BIND services and daemons
		* The BIND daemon provides DNS services, and it is typically located on a system in the `/usr/sbin/` directory.
		* To control the BIND DNS services on Ubuntu, the `bind9` service name (instead of `named`) is used: `service bind9 status`
		* Also, you can see that on an Ubuntu distribution, the `/usr/sbin/named` daemon is running, but it runs under the `bind` username (instead of `named`)
			* `ps -ef | grep ^bind`
			* output: `bind 1242 1 0 08:20 ? 00:00:00 /usr/sbin/named -u bind`
			* `grep bind /etc/passwd`
			* output: `bind:x:117:126::/var/cache/bind:/bin/false`
		* Other distribution BIND differences exist in the configuration files and their locations, which is typical.
	* exploring BIND's files on linux
		* The main configuration file for BIND is `/etc/named.conf` or `/etc/bind/named.conf`, depending on your distribution. The `named.conf` file provides many different configuration settings. To understand the various settings, it is useful to break them down into groupings (also called clauses) as follows (Example at page 382 LPIC-2 Study Guide):
			* **Comments**: Comment fields within the `named.conf` file often provide very helpful configuration information or warnings. Comment lines either begin with `//` or they are encased by `/* comment */`. You can also add a comment at a line’s end, as long as the comment is preceded by a hash mark `(#)`. Because the `named.conf` file default structure can vary so greatly among the different distributions, it is worthwhile to review this file’s comments as part of your BIND setup investigation process.
			* **Options**
				* Within the options section, global options are set.
				* Individual zone options are set within the zone section(s) or files, and they override global options.
				* The `listen-on` and `listen-on-v6` settings specify what port number to listen to for UDP and TCP traffic and which IP addresses (also called the *address match list*), including the local host address, will listen for any incoming queries.
				* The directory setting indicates the primary directory for the `named` daemon. This is the directory where the zone files are located, as well as other important files. The directory is typically set to `/var/named/`, and it is the default BIND configuration.
				* The `dump-file` directive defines where a cache and/or zone database is dumped. The database(s) is dumped only when the `rndc dumpdb` command is issued.
				* Records within the `named.conf` file are either inert or active. Comments are inert (inactive). Any record that ends with a semicolon (;) is an active statement, which causes a BIND configuration directive to take effect.
				* When the `rndc stats` command is issued, it will write any server statistics to the file indicated by the `statistics-file` setting.
					* If this global option is not set, the stats are written to the `/directory/named.stats` file, where `directory` is the defined directory option.
				* The `memstatistics-file` setting determines where DNS server memory usage statistics are recorded when the server exits.
				* The `allow-query` directive is an important setting concerning access and security. You can specify an IP address match list of systems allowed to make queries to this DNS server.
					* The IP addresses are listed within the curly brackets `({})` and separated by a semicolon `(;)`.
					* The designation of localhost within an address match list means that the server’s IP address and its loopback address, `127.0.0.1`, are included in the match list and allowed to make queries.
					* It’s important to include the `allow-query` directive in your `named.conf` file’s options section. If you do not include it, the default is set to `allow-query{any;}`, which effectively allows any system from anywhere to make queries to your DNS server. If your DNS server is a Recursive Name Server that has a public IP address, and you do not set the `allow-query` directive, your server could become involved in a DNS amplification attack.
					* Also, as of BIND v9.4, there is a new directive, `allow-query-cache`, which has syntax similar to the `allow-query` directive and should be set to allow only designated systems access to this server’s DNS cache.
				* The `recursion` setting, if set to yes, tells BIND that this DNS server is to act as a Recursive Name Server. You should set `recursion` to no if you are configuring an authoritative server, such as a primary or secondary DNS server.
				* The `dnssec-enable` directive is set to yes by default (for BIND v9.5 and up). This enabling can be for securing zone transfers, for DNS Security Extensions (DNSSEC), for safeguarding DNS query responses, for securing DDNS updates, and so on.
				* Hand in hand with the `dnssec-enable` directive, the `dnssec-validation` directive is part of the DNSSEC process and is set to yes by default (for BIND v9.5 and up). However, either the `managed-keys` or `trusted-anchors` option must be set as well for this setting to be effective.
					* The DNSSEC process uses keys. These keys are kept in the file designated by the `manage-keys` directive. If `dnssec-validation` is enabled (set to yes), this directive should be included for the global option.
				* The `bindkeys-file` directive sets the location of a trusted keys repository for use with zone keys.
				* The `pid-file` directive specifies a file to hold the BIND daemon’s `(named)` process ID (PID). If the directive is not set, the file used is `named.pid`, and it is typically located in one of the following directories, `/run/named/`, `/var/run/`, or `/etc/`, depending on your distribution.
				* BIND allows dynamic updates to zones. A key used to update a zone is placed in the file designated by the `session-keyfile` setting.
			* **Logging**
				* Within the logging section, directives configure the BIND logging system. Logs can assist in troubleshooting DNS problems as well as tracking security and performance issues.
				* The various `named` channel settings determine where and what information is logged.
				* The `file` directive names the log file and its location.
				* The `severity` directive determines what possible information is logged. It can be set to very little information, `critical` (only critical errors), or to a great deal of information, `dynamic` (debugging data, notices, warnings, and so on).
				* Some distributions have logging set in their configuration file by default while others do not.
			* **Zones**
				* Because a zone defines what a domain name server has authority over, **BIND’s focus is on zones instead of on domains**. Thus, the zone directives are very important.
				* If a zone is defined here, it is typically the *root* zone.
				* The zone `"."` (also called the root zone) directive sets the authoritative root server to query.
				* Various root server addresses are normally stored in the `named.ca` file.
				* The `type hint` setting denotes that the selected root server from this file can respond with the needed authoritative information.
				* The `root zone` directive is needed so that any zone not defined within the local system’s DNS configuration can have a query for it fulfilled. This `root zone` directive is often called a ***Hint for Root Level Servers***.
				* Additional zones can be defined in this file, but on most distributions they are not. Zone directives are often put into their own separate files and then included in the `named.conf` file via an *include statement*.
			* **Include Files**: Additional configuration settings can be stored in separate files and then included using an include statement. Some distributions, such as Ubuntu, have all of the `named.conf` configuration settings stored in include files.
			* `man named.conf`
		* The `/sbin/named-checkconf` utility will conduct a syntax check on your `named.conf` file, which is helpful if you modify it. The utility does not check any configuration files loaded via the include statements, but you can check these files by passing their names to the utility. `man named-checkconf`
		* Let's look at the default zone configuration file on a Linux DNS client where BIND has been installed.
			* On some distributions, this default zone configuration file is `/etc/named.rfc1912.zones`.
			* On other distributions, the zone file is `/etc/bind/named.default-zones`.
			* You can often find your distribution’s default zone file name by looking through its `named.conf` file or one of the `named.conf` file’s include files.
			* The default zone configuration contains only zone directives, and it is typically created when BIND is installed. Each zone directive points to zone files (also called databases) located in the `/var/named` or `/etc/bind` directory, depending on your distribution.
			* If your distribution does not include a `root zone` directive in its `named.conf` file, it’s most likely in the default zone configuration file.
			* The `type master` directive indicates that this zone file contains the primary (master) authoritative configuration for this particular zone.
			* Your distribution may not only have a different location for zone files (databases), but the files may have different naming conventions. On an Ubuntu distribution, these zone files are typically called `/etc/bind/db.[label]`. 
		*  Both the primary DNS configuration file, `named.conf`, and the default zone configuration file are loaded when BIND is started.
	* configuring BIND on linux
		* BIND provides DNS services via the `named` daemon. By default, the daemon listens for both UDP and TCP traffic on port 53.
		* ==*The certification objectives focus on configuring BIND to function as a caching-only DNS server. Thus, this section also focuses on only this DNS server type. A caching-only DNS server is worth exploring.*==
		* A caching-only server is sometimes called a `resolver`, and it is often set up locally to reduce query times for local systems.
		* When a caching-only DNS server has an answer for an FQDN to IP address translation query, it saves it to file or memory (BIND saves it to memory). Other local systems can then have their queries answered by the local caching-only server, until the answer’s TTL value is reached or BIND is restarted. Substantial improvements in query time can be achieved if the caching-only DNS server is physically close to the other systems it is serving.
		* Keep in mind that many DNS terms thrown around, such as `resolver`, can cause confusion. Though a caching-only DNS server may sometimes be called a `resolver`, recall that a `resolver` is also a system’s library routine or program that checks its own cache and/or files for an answer to the DNS query. If it can’t find the answer, it forwards the query to another `resolver` on another system.
		* On some distributions, the installed BIND configuration files come already configured to provide client-side caching-only DNS name services. Be aware that some distributions, such as Ubuntu, come with `dnsmasq` pre-installed and set to run on boot. If you are installing and configuring BIND on such a distribution, some caching oddities may occur.
		* Before making any configuration file changes, first decide what local servers will be allowed to query the caching-only DNS server. Once you have chosen those servers, using super user privileges, change the `allow-query` directive in either the `named.conf` or `named.conf.options` configuration file, depending on your distribution. Though you could just add the IP addresses of the chosen servers to the `allow-query` directive, it’s better first to create an access control list using the `acl` (Access Control List) directive (page 389 LPIC-2 Study Guide).
		* It is important to keep this DNS caching-only server private, behind a firewall, and allow only designated servers to use it. If you do not take these actions, your DNS caching-only server could be used in a DNS amplification attack, which allows malicious people to overwhelm other servers and thus deny access to them.
		* By default, the `recursion` directive is already set to yes. If for some reason it is set to no in your `named.conf` or `named.conf.options` file, you will need to change it. No matter what access to the cache you have granted, no access will be granted if `recursion` is set to no.
		* Once you have your caching-only DNS name server configured and tested, you will need to configure the other local systems to use this name server for their name resolution queries. Enter the caching-only DNS name server’s IP address into the local system’s `/etc/resolv.conf` file.
		* Current Ubuntu distributions typically use the `dnsmasq` utility for providing local caching and lightweight DHCP services. If you decide to use a local caching-only DNS server instead, you will need to disable the `dnsmasq` service. To do so, edit the `NetworkManager.conf` file located in the `/etc/NetworkManager/` directory. Place a hash mark (#) in front of the `dns=dnsmasq` line, save the file, and restart your network manager.
		* Your system may come with the `/sbin/lwresd` utility preinstalled. The `lwresd` is a simple caching-only DNS name server daemon. It listens for queries on the IPv4 loopback interface, `127.0.0.1`. The `lwresd` daemon is installed as part of the `bind9` package on Red Hat–based distributions. For an Ubuntu system, `sudo apt-get install lwresd`. `man lwresd`.
* starting, stopping, and reloading BIND
	* Several methods are available for starting and stopping BIND as well as for reloading modified BIND configuration files without stopping the BIND service.
	* traditional methods (wrote only systemd version)
		* start: `systemctl start [BINDname]`
		* stop
			* `systemctl stop [BINDname]`
			* `kill -s SIGTERM [BIND_PID]`
			* `kill -s SIGINT [BIND_PID]`
		* restarting: `systemctl restart [BINDname]`
		* reloading BIND conf files:
			* `systemctl reload [BINDname]`
			* `kill -s SIGHUP [BIND_PID]`
		* In the preceding commands, the `BINDname` variable is either named or `bind9`, depending on your distribution.
		* The BIND_PID is the BIND daemon’s process ID (PID). The BIND daemon’s PID is typically stored in the `/run/named/named.pid` or `/var/run/named.pid` file, depending on your distribution. Therefore, `kill -s SIGHUP $(cat /run/named/named.pid)`
		* Though the traditional methods work, they are not considered best practices. This is especially true with the `kill` command, because sending the wrong signal to the BIND daemon could have unintended consequences.
	* exploring `rndc`
		* The best way to control the BIND daemon is via the `rndc` utility.
		* The `/usr/sbin/rndc` tool is the primary utility for managing BIND.
		* It has many features, including the ability to use a TCP connection to communicate with a remote name server and send it commands authenticated with digital signatures.
		* To see all of the various features of your `rndc` utility, just type `rndc` and press Enter.
		* `rndc status`
		* `rndc reload`
		* `rndc stop`
		* However, be aware that while you can stop the BIND daemon using `rndc`, you cannot start or restart it using the `rndc` utility.
		* `systemctl start named`
* BIND logging
	* An important part of setting up your BIND configuration is determining how you want BIND messages to be logged as well as the desired message detail level.
	* Logs can assist in troubleshooting DNS problems as well as tracking security and performance issues. Therefore, you may want to configure BIND to provide more complex logging than its default configuration provides.
	* Typically, BIND logging is configured in the `named.conf` file.
	* The `logging` directives determine what is logged and where it is logged.
	* For example syntax refer to page 398 (LPIC-2 Study Guide).
	* The logging directives can be broken up into two primary groupings: `channel` and `category`. A channel is either a predefined channel directive or it is a custom channel. It controls where messages are logged and filters what is logged. A category directive defines DNS message types to be logged.
	* logging channels
		* There are four **predefined** channel directives, briefly described here:
			* **default_debug**: Write log messages to `named.run` in the specified directory, with the severity filter directive set to dynamic.
			* **default_stderr**: Write log messages to stderr (while running BIND in the foreground for debugging) with the severity filter directive set to info.
			* **default_syslog**: Write log messages to syslog or rsyslog, with the severity filter directive set to info.
			* **null**: Write all log messages to `/dev/null` (do not keep log messages).
		* You can modify the default settings of these predefined channel directives.
		* You are not stuck with the predefined channel directives. You can set up multiple custom channels to finely control your BIND logging. As long as each channel is uniquely named, you can set as many unique logging directives as desired for that channel.
		* Within a custom channel, you can set where the log messages are sent. These locations include a file, a syslog facility, standard error (stderr), or null, which essentially throws out log messages.
		* For the file directive, at a minimum, the file’s name must be specified. To control the file’s location, the path setting, you can do any one of the following:
			* Accept the default location of the `/var/named/` directory.
			* Accept the location set by the directory directive (typically located earlier in the `named.conf` file).
			* Set a path relative to the directory directive.
			* Set a custom path via declaring an absolute directory path.
		* You can even control the log file’s `size` through the size setting. The log file’s version numbers are managed via the `versions` directive.
		* The `severity` directive is a filter that has seven levels. A message whose classified severity is equal to or higher than the specified severity level is logged through the declared channel. Going from the lowest severity to the highest, the levels that you can set are these:
			* dynamic
				* The dynamic severity filter is similar to debug severity, but it uses any debugging level set when the `named` daemon is started.
			* debug level
				* For the debug severity filter, you can specify a debug level. The higher the debug level number, the more information is logged. If no level is specified, it defaults to debug level 1. Debugging can be turned off by specifying level 0.
			* info
			* notice
			* warning
			* error
			* critical
		* The `print-` directives allow you to control additional information that is logged. If not set, they default to no. If set to yes, `print-category` logs the category, `print-severity` logs the actual severity level (as opposed to the set severity filter level), and `print-time` will log the date and time.
		* Once you have set where information will be logged and how that logging data will be filtered via the channels, you then set the category.
	* logging categories
		* Categories determine what DNS information will be logged, and categories are pointed to channels so that the log messages are filtered and recorded to the desired location.
		* Each log message category can go into a single declared (or default) channel or into multiple channels.
		* You have a lot of flexibility as to how to filter and record these various log message categories.
		* If no category is defined, it defaults to:
			*  `category default { default_syslog; default_debug; };`
			* The category’s name is `default`, which essentially captures all of the various categories’ messages that are normally captured without being declared.
			* The `default` category does not capture a particular category if that category is also declared within the `named.conf` file.
			* The categories’ messages are sent to two different channels: `default_syslog` and `default_debug`.
		* Because of the rather confusing nature of DNS logging, it’s a good idea to start out with a simple logging directive. Configure your DNS logging to capture all of the various categories, set a low severity filter (debug 3), and send the log messages to a single file. Over time, you will get an idea of what particular messages you want to log, what to filter out, and how to divide the log messages among the various logging facilities. Slowly change and test your logging settings as you make these discoveries.
		* There are several log message categories. A few category names to use within a category directive are shown in Table 8.1 (page 402 LPIC-2 Study Guide). You will notice that potentially a lot of overlap can occur among the various log message categories. There are more categories than those listed in Table 8.1. Also, the BIND developers may add additional log message categories in the future. You can stay up to date on current BIND 9 logging category additions and other BIND enhancements by visiting the ISC’s website at `www.isc.org`.
		* Some DNS managers set each individual category into its own channel, with that channel having a high severity filter (so few messages are filtered out) and recording the log messages to a file. While this may prove useful as you start exploring DNS logging, be aware that you will have numerous log files, which may quickly become rather large.

### NFS
* While NFS lacks features for mixed environments, it does provide enhanced performance for sharing files. It’s a better alternative for non-mixed networks.
* understanding NFS
	* NFS stands for Network File System.
	* NFS is a protocol that allows client systems to access and use NFS server-offered filesystems over a network as local filesystems.
	* ==The LPIC-2 certification objectives focus on NFSv3. Therefore, most of this section’s information is based on NFSv3.==
	* NFSv3 software uses the Remote Procedure Call (RPC) protocol.
	* The RPC protocol allows a program to be ignorant of network details but still request services from another system within that network. For NFSv3, RPC handles mounting the NFS filesystem, lock management, and quota.
	* The filesystem an NFS server offers is called either an *export* or a *share*. However, the processing of making an NFS share available is only called *exporting*.
	* To implement NFS services, your distribution’s Linux kernel must support NFS. This is because NFS is a combination of kernel-level functions and daemons.
	* Depending on your NFS configuration and version, there are potentially several daemons or kernel services involved in providing NFS shares. The various NFS daemons and Linux kernel services are described in Table 10.9 (page 531 LPIC-2 Study Guide).
	* Choosing which NFS version to use can be difficult. Therefore, with NFS, it is vital to review NFS documentation prior to NFS implementation.
	* For NFS documentation, if you have NFS installed, typically the `/usr/share/doc/nfs*/` directories have current documentation as well as the locally installed man pages. You can also find Linux NFS documentation at the developer site’s wiki at `linux-nfs.org`. If you are seeking older NFS documentation, visit the old NFS developers’ site at `nfs.sourceforge.net`.
* configuring NFS
	* installing NFS server
		* Several NFS packages are available. Which package(s) you need to install depends on your distribution, its version, the NFS version you are trying to implement, as well as whether you are installing packages for an NFS server or a client.
		* Typically for a Debian-based distribution, such as Ubuntu, you’ll find the NFS packages listed in Table 10.11 (page 534 LPIC-2 Study Guide) are either preinstalled or available to install.
	* NFS dirs and files
		* The primary files and directories are listed in Table 10.12 (page 535 LPIC-2 Study Guide).
		* In addition to the items listed in Table 10.12 (page 535 LPIC-2 Study Guide), the `/proc/filesystems`, `/etc/fstab`, `/etc/mtab`, and `/proc/mounts` can also be involved with NFS.
		* **exploring the `/etc/exports` file** #todo 
		* **exploring NFS utilities** #todo 
		* **configuring a temporary NFS export** #todo 
		* **configuring a permenant NFS export** #todo 
* securing NFS #todo 
* troubleshooting NFS #todo 

### FTP
* Typically, FTP is used when mounting a share permanently or temporarily is not desired or workable and transfer speed is an issue. It is ideal for situations where files are shared for download purposes only, such as when an instructor on a local lab LAN is sharing binaries with newbie Linux students.
* understanding FTP
	* It is a simple network protocol for sharing files between systems.
	* It is primarily used to share public documents over a network.
	* When you connect to an FTP service, its authentication process may require you to give it a valid username and password. Once you are authenticated, depending on the FTP service’s configuration, you can essentially look around and download (or upload) files.
	* If you are using account and password information to log into an FTP service, be aware that they are typically not encrypted. This means anyone using a network sniffer application, such as Wireshark, will see your FTP server username and password in the clear. It is better to use Secure FTP (SFTP), which encrypts FTP via OpenSSH.
	* It’s more common for an FTP service to be set up for anonymous access and only allow file downloads. With anonymous FTP access, instead of an individually assigned username, a general username, such as anonymous or ftp, is used. There may be no password required or a request for your email address as the password (though the email address is not verified).
	* passive and active connections
		* It’s important to know that FTP l uses two operating modes: *passive* and *active*.
		* The mode used determines how a connection is established. Passive mode has fewer problems, so it is the more popular of the two.
		* FTP also uses two TCP ports: the *data port* and the *command port*.
			* The command port is used for sending commands and handling command responses.
			* The data port is used for transporting file data.
			* The FTP server uses port 20 as its data port and port 21 as its command port.
		* In active mode, both the FTP server and client are active in establishing the connections.
		* The basic active mode connection steps are as follows:
			1. The FTP client picks and opens a random unprivileged port C (where C is >1024) to serve as its command port in order to send and receive commands.
			2. The FTP client picks and opens another random unprivileged port D (where D is C+1) to serve as its data port and begins to listen for FTP server data.
			3. The FTP client uses its command port (port C) to inform the FTP server via the server’s command port (port 21) that it is listening for data on its data port (port D).
			4. The FTP server uses its command port (port 21) to acknowledge the request, which is sent to the FTP client’s command port (port C).
			5. The FTP server uses its data port (port 20) to connect to the FTP client’s data port (port D).
			* Thus, in active mode, the FTP client establishes the command connection, but the FTP server establishes the data connection.
			* The server’s active role can cause problems with certain network configurations because of firewalls. The FTP client’s firewall may see the FTP server data port connection attempt (step 5) as potentially malicious (an external system trying to connect with an internal system) and block the attempt.
				* For example, if you have a local FTP client trying to connect to a FTP server across the Internet using active mode, your LAN firewalls most likely will block this.
		* Because of this issue, the FTP passive mode was created.
		* In passive mode, the FTP server is passive, and only the FTP client is active in establishing the connections. Also, the FTP server uses port 20 as its data port but a random unprivileged port as its command port.
		* The basic passive mode connection steps are as follows:
			1. The FTP client picks and opens two random unprivileged ports: port C to serve as its command port and port D to serve as its data port.
			2. The FTP client uses its command port (port C) to inform the FTP server via the server’s command port (port 21) that it is establishing a passive connection.
			3. The FTP server picks and opens a random unprivileged port SD (where SD is > 1024) as its data port to send/receive the FTP client’s data.
			4. The FTP server uses its command port (port 21) to inform the FTP client via the client’s command port (port C) that it is listening for data on its data port (port SD).
			5. The FTP client uses its data port (port D) to connect to the FTP server’s data port (port SD).
		* There are pros and cons to both passive and active FTP modes. Generally, passive mode is used by FTP servers that are servicing many WAN FTP client systems. However, if you employ this mode on an FTP server, it is important to configure your server’s firewall properly and consider making it an FTP-only server to help prevent malicious attacks.
	* FTP servers and clients
		* FTP services are available through various packages. Linux FTP servers mentioned in the certification objectives are listed here:
			* **Very Secure FTP**: Very Secure FTP `(vsftpd)` is open-source Unix and Linux FTP server software whose primary focuses are on security, performance, and stability. It supports non-anonymous and anonymous FTP server access as well as PAM authentication. This popular FTP server software has been the default FTP daemon in many distributions for several years, though it typically must be manually installed.
			* **Pure-FTPd**: Pure-FTPd `(pure-ftpd)` is an open-source cross-platform FTP server software whose primary focuses are on security, efficiency, and ease of use. Its security features include built-in chroot emulation, virtual accounts, and optional support for SSL/TLS encryption.
			* **ProFTPD**: ProFTPD is open source and somewhat cross platform. This FTP server software is full of features, including several security attributes. For example, you can block scripted FTP clients, which are typically maliciously trying to find and exploit poorly configured anonymous FTP sites. Though feature rich, it is not overly difficult to configure. It has a single primary configuration file, `/etc/proftpd/proftpd.conf`, and has an Apache-like configuration. By default, there is a command-line interface, but several third-party GUI interfaces are available.
		* There are also many FTP client applications. The one you choose will depend on how you are using FTP and your security needs.
			* **Web Browsers**: You can use just about any web browser, such as Mozilla Firefox or Google Chrome, to connect to an FTP server. In the address bar, type in ftp:// followed by the FTP server’s FQDN or IP address. An anonymous connection is made if you do not include a username and password. By clicking the presented links, you can either download files or traverse the listed directories.
			* **GUI Applications**: Several free FTP client GUI applications are available, such as the popular open-source cross-platform FileZilla software. Once it’s installed, you enter the FTP server’s FQDN and your username and password information. Afterward, the connection is initiated via menu options or key sequences. A rich GUI interface offers the ability to drag and drop files to download/upload.
			* **Command-Line Utilities**: There are also command-line FTP client utilities available to install and use (depending on your distribution). The `ftp` utility is a standard basic FTP client, whereas the `lftp` utility is a refined FTP client that provides more features, such as the ability to transfer files in parallel. Most current distributions include these two utilities in their repositories.
		* The FTP server and FTP client packages you choose depend heavily on your particular file transfer needs. Keep in mind that if you are using FTP primarily for copying files back and forth over the network, it may make more sense to use something like the `ssh` or `scp` utilities.
* configuring `vsftpd` #todo 
* configuring Pure-FTPd #todo 

### Web Servers
#todo this should not be here

* The most popular use of Linux in the server environment is as a web server.
* Linux web servers dominate the Internet, and they are also very popular for hosting corporate intranet applications.
* Everything from serving static web pages to hosting dynamic web applications often runs faster and more efficiently on a Linux server platform.
* web server basics
	* HTTP was developed to help out with the easy transfer of data anonymously between systems.
	* For public data that doesn’t need to be protected, HTTP allows a client to connect to a server anonymously, retrieve data files, and then disconnect. This process has greatly helped speed up retrieving data from the remote systems connected to the Internet, and it is what has made the Internet a popular place for sharing data.
* linux web servers
	* apache
		* By far the most popular web server on the Internet today is the Apache web server application.
		* It is an open source project, maintained by the Apache Software Foundation.
		* Over the years, the Apache web server project has pioneered many new features that define just what web servers should support:
			* **Loadable Dynamic Modules**: The ability to activate and deactivate features on the fly as the web server is running.
			* **Scalable Multisession Support**: The ability to handle easily multiple client requests at the same time is crucial for modern web servers.
			* **Limiting Concurrent Connections**: While multiuser support is crucial, so is the ability to limit the number of clients that can connect at the same time to help prevent system overload.
			* **Bandwidth Throttling**: The ability to regulate the output from the web server to prevent overloading the network, even if the system can handle more connections.
			* **Web Caching** (aka web proxy): The ability to store web pages requested by multiple clients and read additional requests from the cache rather than from the original data source.
			* **Load Balancing** (aka reverse proxy): The ability to act as a single point of connection for clients and then redirect requests to multiple backend servers for processing.
			* **Common Gateway Interface**: The ability to forward web page content to internal server programs, commonly used for processing embedded scripting code.
			* **Virtual Hosting**: The ability to host multiple domains on a single web server.
			* **User-Based Web Page Hosting**: Allows individual users on the system to host their own web pages.
		* With Apache, all of these features, plus a lot more, are easily enabled or disabled using simple text-based configuration files.
	* squid
		* The Squid web server performs not as much as a stand-alone web server but as a web proxy server.
		* A web proxy server intercepts HTTP requests from multiple clients on a network before they leave the network. It then resends the requests directly to the remote destination, waits for the response, and then forwards the response back to the client.
		* While this may seem counterproductive, there are two benefits of this process:
			* The web proxy server can filter client requests to block those that the network administrators deem inappropriate.
			* The web proxy server can cache the remote server responses. If another client makes the same request, the web proxy server can return the cached data instead of having to re-download the data from the remote server. This can both speed up web page performance and save network bandwidth.
		* The Squid web proxy server has become the de facto web proxy server used in Linux environments.
	* nginx
		* While it too can operate as a standard web server, the nginx (pronounced “engine-X”) web server is better known as a reverse proxy server.
		* As you can probably guess, a reverse proxy server does the opposite of what a web proxy server does. Instead of processing requests from multiple clients to a single web server, a reverse proxy server processes requests from a single client to multiple web servers. This technique is also known as *load balancing*.
		* A load balancing server receives HTTP requests from clients and sends them to a specific server in a pool of common web servers for processing. Each web server in the pool contains the same data and can process the same HTTP requests. The load balancing process helps distribute the client load on multiple web servers in a high-traffic environment, helping prevent overloading and slow performance.
