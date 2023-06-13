> [!Example]
> H = `total hours`
> hpd = `hours per day`
> mpd = `minutes per day`
> hps = `hours per score`
> mps = `minutes per score`
>
> LPIC-1 score (`l1s`): 3408
> LPIC-2 score: 561 * 2 (`l2s`) = 1122
> total score (`ts`) = l1s + l2s = 4530
> hps = H / ts = H / 4530
> mps = hps * 60
> > [!info] Formula
> > hps = H / ts = H / 4530
> > mps = hps * 60
> > > [!warning] section time calculation
> > > section time = [mh]ps * section score
>
> 13 → 19 Esfand 1401
> 8 hpd → H = 56 hours
> > [!Success] study proportion
> > hps = 56 / 4530 = 0.0123620309
> > mps = 56 * 60 / 4530 = 0.741721854
> > > [!Exmaple] Example
> > > `103: GNU and UNIX commands`
> > > 	section score = 1065
> > > 	section time = 13.16 hours
> > > `102.1 Design Hard Disk Layout`
> > > 	section score = 28
> > > 	section time = 20.76 minutes

#### LPIC-1
> [!info summary]
> `sum weight: 94`
> `sum number of pages: 970`
> `sum score: 3408`

##### 101: System Architecture
> [!summary]
> `sum weight: 3`
> `sum number of pages: 18`
> `sum score: 54`

###### ~~101.1 Determine and Configure Hardware settings~~
> ~~`weight: 2, pg: 18, score: 36`~~
###### ~~101.2 Boot the System~~
> ~~`weight: 3, pg: 17, score: 51`~~
###### 101.3 Change runlevels / boot targets and shutdown or reboot system
> `weight: 3, pg: 18, score: 54`
> `time req: 40"`
> `time done: 1' 20"`
> `performance: 50%`

[[Linux/Process Management#Daemons/Services]]
[[Linux/Process Management#Runlevels]]
[[Linux/Process Management#Systemd/Systemctl]]
[[Linux/System Management#^shutdown]]

##### 102: Linux Installation and Package Management
> [!summary]
> `sum weight: 7`
> `sum number of pages: 101`
> `sum score: 163`

###### 102.1 Design Hard Disk Layout
> `weight: 2, pg: 14, score: 28`
> `time req: 21"`
> `time done: 36"`
> `performance: 58.3%`

[[Linux/File Management#Hard Disk Layout Design]]
[[Linux/File Management#FHS]]

###### ~~102.2 Install a boot manager~~
> ~~`weight: 2, pg: 22, score: 44`~~
###### 102.3 Manage shared libraries
> `weight: 1, pg: 15, score: 15`
> `time rec: 11"`
> `time done: 43"`
> `performance: 25.58%`

[[Linux/Package Management#Shared Libraries]]

###### 102.4 Debian package management
> `weight: 3, pg: 24, score: 72`
> `time rec: 54"`
> `time done: 1'`
> `performance: 90%`

[[Linux/Ubuntu/Package Management#DPKG: `The Debian Package Tool`]]
[[Linux/Ubuntu/Package Management#APT: `Advanced Package Tool`]]

###### ~~102.5: Use RPM and YUM package management~~
> ~~`weight: 3, pg: 27, score: 81`~~
###### 102.6 Linux as a virtualization guest
> `weight: 1, pg: 48, score: 48`
> `time rec: 35"`
> `time done: 55"`
> `performance: 63%`

[[Linux/Virtualization#Hypervisor]]
[[Linux/Virtualization#Virtual Machines]]
[[Linux/Virtualization#Cloud]]
[[Linux/Virtualization#Containers]]

##### 103: GNU and UNIX Commands
> [!summary]
> `sum weight: 26`
> `sum number of pages: 302`
> `sum score: 1065`

###### 103.1 Work on the command line
> `weight: 4, pg: 23, score: 92`
> `time rec: 1' 10"`
> `time done: 40"`
> `performance: 175%`

[[Linux/Commands#General]]
[[Linux/Shell#Environment Variables]]

###### 103.2 Process text streams using filters
> `weight: 2, pg: 35, score: 70`
> `time rec: 55"`
> `time done: 1' 10"`
> `performance: 78.5%`

[[Linux/Text Manipulation]]

###### 103.3 basic file management
> `weight: 4, pg: 41, score: 164`
> `time rec: 2'`
> `time done: 2' 10"`
> `performance: 85%`

`
* commands

[[Linux/File Management#Commands]]

###### 103.4 streams, pipes and redirects
> `weight: 4, pg: 23, score: 92`
> `time rec: 1' 10"`
> `time done: 1' 35"`
> `performance: 73%`

[[Linux/Shell#Communication Channels]]
[[Linux/Shell#Redirect]]
[[Linux/Shell#Pipes]]
[[Linux/Shell#Command Substitution]]

###### 103.5 create, monitor and kill processes
> `weight: 4, pg: 61, score: 244`
> `time rec: 3'`
> `time done: 1' 30"`
> `performance: 200%`

[[Linux/Process Management#Jobs]]
[[Linux/Process Management#Process Monitoring]]
* Terminal Multiplexers #todo 

###### 103.6 process priority
> `weight: 2, pg: 14, score: 28`
> `time rec: 20"`
> `time done: 35"`
> `performance: 60%`

[[Linux/Process Management#Process Priority]]

###### 103.7 Search text files using regular expressions
> `weight: 3, pg: 31, score: 93`
> `time rec: 1' 10"`
> `time done: 1' 50"`
> `performance: 63%`

[[Linux/Text Manipulation#Regular Expressions]]
[[Linux/Text Manipulation#Chain Filtering]]

###### 103.8 Basic file editing
> `weight: 3, pg: 14, score: 42`
> `time rec: 30"`
> `time done: 40"`
> `performance: 75%`

[[Linux/Text Manipulation#Vim]]

##### 104: Devices, Linux Filesystems, Filesystem Hierarchy standard
> [!summary]
> `sum weight: 10`
> `sum number of pages: 86`
> `sum score: 220`

###### ~~104.1 Create partitions and filesystem~~
> ~~`weight: 2, pg: 36, score: 72`~~
###### ~~104.2 Maintain the integrity of filesystem~~
> ~~`weight: 2, pg: 23, score: 46`~~
###### 104.3 Control mounting and unmounting of filesystems
> `weight: 3, pg: 20, score: 60`
> `time rec: 45"`
> `time done: 50`
> `performance: 90%`

[[Linux/Filesystem Management#Mounting/Unmounting Filesystems]]

###### 104.5 file permissions
> `weight: 3, pg: 28, score: 84`
> `time rec: 1'`
> `time done: 1' 10"`
> `performance: 85%`

[[Linux/File Management#Permissions]]

###### 104.6 hard/symbolic links
> `weight: 2, pg: 17, score: 34`
> `time rec: 25"`
> `time done: 19"`
> `performance: 131%`

[[Linux/File Management#Hard/Symbolic Links]]

###### 104.7 Filesystem Hierarchy Standard
> `weight: 2, pg: 21, score: 42`
> `time rec: 30"`
> `time done: 32"`
> `performance: 93%`

* Those interested in the details of filesystem organization can read the FHS 3.0 specification, available in multiple formats at [linuxfoundation](http://refspecs.linuxfoundation.org/fhs.shtml)
[[Linux/File Management#FHS]]
[[Linux/File Management#Searching for Files]]

##### 105: Shells and Shell Scripting
> [!summary]
> `sum weight: 8`
> `sum number of pages: 122`
> `sum score: 488`

###### 105.1 Customize and use the shell environment
> `weight: 4, pg: 84, score: 336`
> `time rec: 4' 10"`
> `time done: 3' 35"`
> `performance: 116%`

[[Linux/Shell#Shell Types]]
[[Linux/Shell#Launching Shells]]
[[Linux/Shell#Config]]
[[Linux/Shell#Sourcing Scripts]]
[[Linux/Bash Scripting#Variables]]
[[Linux/Bash Scripting#Aliases]]
[[Linux/Bash Scripting#Functions]]

###### 105.2 Customize or write simple scripts `weight: 4 pg: 38`
> `weight: 4, pg: 38, score: 152`
> `time rec: 1' 55"`
> `time done: 1' 54"`
> `performance: 100.8%`

[[Linux/Bash Scripting#Script Arguments]]
[[Linux/Bash Scripting#Arrays]]
[[Linux/Bash Scripting#Conditions]]
[[Linux/Bash Scripting#Loops]]
[[Linux/Bash Scripting#Etcetera]]

##### ~~106: User Interfaces and Desktops~~
> [!summary]
> `sum weight: 0`
> `sum number of pages: 0`
> `sum score: 0`

###### ~~106.1 Install and configure X11~~
> ~~`weight: 2, pg: 18, score: 36`~~
###### ~~106.2 Graphical Desktops~~
> ~~`weight: 1, pg: 15, score: 15`~~
###### ~~106.3 Accessibility~~
> ~~`weight: 1, pg: 12, score: 12`~~

##### 107: Administrative Tasks
> [!summary]
> `sum weight: 9`
> `sum number of pages: 63`
> `sum score: 285`

###### 107.1 Manage user and group accounts and related system files
> `weight: 5, pg: 33, score: 165`
> `time rec: 2'`
> `time done: 1' 20"`
> `performance: 150%`

[[Linux/User Management]]

###### 107.2 Automate system administration tasks by scheduling jobs
> `weight: 4, pg: 30, score: 120`
> `time rec: 1' 30"`
> `time done: 1' 25"`
> `performance: 105%`

[[Linux/Process Management#Cron/Systemd Timers]]
[[Linux/Process Management#The `at` Command]]

###### ~~107.3 Localisation and internationalization~~
> ~~`weight: 3, pg: 18, score: 54`~~

##### 108: Essential System services
> [!summary]
> `sum weight: 7`
> `sum number of pages: 95`
> `sum score: 343`

###### 108.1 Maintain system time
> `weight: 3, pg: 37, score: 111`
> `time rec: 1' 25"`
> `time done: 1' 5"`
> `performance: 130%`

[[Linux/System Management#System Time]]
[[Linux/System Management#Network Time Protocol (NTP)]]

###### 108.2 System logging
> `weight: 4, pg: 58, score: 232`
> `time rec: 2' 55"`
> `time done: 3' 23"`
> `performance: 86%`

[[Linux/System Management#Traditional Logging Services]]
[[Linux/System Management#Journald]]

###### ~~108.3 Mail Transfer Agent (MTA) basics~~
> ~~`weight: 3, pg: 17, score: 51`~~
###### ~~108.4 Manage printers and printing~~
> ~~`weight: 2, pg: 22, score: 44`~~

##### 109: Networking Fundamentals
> [!summary]
> `sum weight: 14`
> `sum number of pages: 105`
> `sum score: 388`

###### 109.1: Fundamentals of internet protocols
> `weight: 4, pg: 27, score: 108`
> `time rec: 1' 20"`
> `time done: 28"`
> `performance: 285%`

###### 109.2 Persistent network configuration
> `weight: 4, pg: 29, score: 116`
> `time rec: 1' 25"`
> `time done: 1' 45"`
> `performance: 80%`

[[Linux/Network Management#The Network Interface]]
[[Linux/Network Management#Systemd]]

###### 109.3 basic network troubleshooting
> `weight: 4, pg: 33, score: 132`
> `time rec: 1' 40"`
> `time done: 1'`
> `performance: 166%`

[[Linux/Network Management#Basic Network Troubleshooting]]
[[Linux/Network Management#Basic Network Troubleshooting]]

###### 109.4 Configure client side DNS
> `weight: 2, pg: 16, score: 32`
> `time rec: 23"`
> `time done: 34"`
> `performance: 67%`

[[Linux/Network Management#Configuring Client-side DNS]]

##### 110: Security
> [!summary]
> `sum weight: 10`
> `sum number of pages: 48`
> `sum score: 312`

###### 110.1 perform security administration tasks
> `weight: 3, pg: 37, score: 111`
> `time rec: 1' 22"`
> `time done: 1' 53"`
> `performance: 72%`

[[Linux/File Management#Checking For Files with the SUID and SGID set]]
* password management and aging
	* [[Linux/User Management#^passwd]]
	* [[Linux/User Management#^chage]]
[[Linux/Network Management#Discovering Open Ports]]
[[Linux/Network Management#^user-limits-ulimit]]
* Dealing with Logged in Users
	* [[Linux/User Management#^last]]
	* The who and w utilities focus on currently logged in users and are quite similar. The former displays who is logged on, while the latter also shows information on what they are doing.
	* [[Linux/User Management#^who]]
	* [[Linux/User Management#^w]]
[[Linux/User Management#sudo Configuration]]

###### 110.2 Setup host security
> `weight: 3, pg: 18, score: 45`
> `time rec: 33"`
> `time done: 29"`
> `performance: 113%`

[[Linux/User Management#^shadow-passwords]]
[[Linux/Network Management#inetd and xinetd]]
[[Linux/Process Management#Checking Services for unnecessary Daemons]]

###### 110.3 Securing data with encryption
> `weight: 4, pg: 39, score: 156`
> `time rec: 1' 55"`
> `time done: 54"`
> `performance: 212%`

[[Linux/System Management#OpenSSH]]]

#### LPIC-2
> [!Info summary]
> `sum weight: 58`

##### 200: Capacity Planning
> [!summary]
> `sum weight: 8`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 2: Maintaining The System]]

###### 200.1 Measure and troubleshoot resource usage
> `weight: 6`
###### 200.2 Predict future resource needs
> `weight: 2`

##### 201: Linux Kernel
> [!summary]
> `sum weight: 9`
###### 201.1 Kernel components
> `weight: 2`
###### 201.2 Compiling a linux kernel
> `weight: 3`
###### 201.3 Kernel runtime management and troubleshooting
> `weight: 4`

##### 202: System Startup
> [!summary]
> `sum weight: 9`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 1: Starting a System]]

###### 202.1 Customizing system startup
> `weight: 3`
###### 202.2 System recovery
> `weight: 4
###### 202.3 Alternate bootloaders
> `weight: 2

##### 203: Filesystem and Devices
> [!summary]
> `sum weight: 9`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 4: Managing The Filesystem]]

###### 203.1 Operating the linux filesystem
> `weight: 4`
###### 203.2 Maintaining a linux filesystem
> `weight: 3`
###### 203.3 Creating and configuring filesystem options
> `weight: 2`

##### 204: Advanced Storage Device Administration
> [!summary]
> `sum weight: 8`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 5: Administering Advanced Storage Devices]]

###### 204.1 Configuring RAID
> `weight: 3`
###### 204.2 Adjusting storage device access
> `weight: 2`
###### 204.3 Logical volume manager
> `weight: 3`

##### 205: Networking Configuration
> [!summary]
> `sum weight: 11`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 6: Navigating Network Services]]

###### 205.1 Basic networking configuration
> `weight: 3`
###### 205.2 Advanced network configuration
> `weight: 4`
###### 205.3 Troubleshooting network issues
> `weight: 4`

##### 206: System Maintenance
> [!summary]
> `sum weight: 6`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 2: Maintaining The System]]

###### 206.1 Make and install programs from source
> `weight: 2`
###### 206.2 Backup operations
> `weight: 3`
###### 206.3 Notify users on system-related issues
> `weight: 1`

##### 207: Domain Name Server
> [!summary]
> `sum weight: 8`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 8: Directing DNS]]

###### 207.1 Basic DNS server configuration
> `weight: 3`
###### 207.2 Create and maintain DNS zones
> `weight: 3`
###### 207.3 Securing a DNS server
> `weight: 2`

##### 208: HTTP Services
> [!summary]
> `sum weight: 11`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 9: Offering Web Services]]

###### 208.1 Basic apache configuration
> `weight: 4`
###### 208.2 Apache configuration for HTTPS
> `weight: 3`
###### 208.3 Implementing Squid as a caching proxy
> `weight: 2`
###### 208.4 Implementing Nginx as a web server and a reverse proxy
> `weight: 2`

##### 209: File Sharing
> [!summary]
> `sum weight: 8`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 10: Sharing Files]]

###### 209.1 Samba server configuration
> `weight: 5`
###### 209.2 NFS server configuration
> `weight: 3`

##### 210: Network Client Management
> [!summary]
> `sum weight: 11`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 11: Managing Network Clients]]

###### 210.1 DHCP configuration
> `weight: 2`
###### 210.2 PAM authentication
> `weight: 3`
###### 210.3 LDAP client usage
> `weight: 2`
###### 210.4 Configuring an OpenLDAP server
> `weight: 4`

##### 211: E-Mail Services
> [!summary]
> `sum weight: 8`

###### 211.1 Using e-mail servers
> `weight: 4`
###### 211.2 Managing e-mail delivery
> `weight: 2`
###### 211.3 Managin mailbox access
> `weight: 2`

##### 212: System Security
> [!summary]
> `sum weight: 14`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 12: Setting Up System Security]]

###### 212.1 Configuring a router
> `weight: 3`
###### 212.2 Managing FTP servers
> `weight: 2`
> sources: [[Linux/LPIC-2 Study Guide#Chapter 10: Sharing Files]]
###### 212.3 Secure Shell (SSH)
> `weight: 4`
###### 212.4 Security tasks
> `weight: 3`
###### 212.5 OpenVPN
> `weight: 2`