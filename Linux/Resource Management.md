* Managing your system’s resource usage involves troubleshooting resource problems as they occur. However, measuring via monitoring and predicting future resource usage can help minimize resource problems ahead of time. Unfortunately, too many system administrators spend more time on troubleshooting and less time on monitoring/predicting.
### Measuring Resource Usage
* There is an old saying that states, ***“You can’t manage what you can’t measure.”***
* You must measure resources often, accurately, and thoroughly to gather the necessary data to manage these resources properly. In addition, you must measure accurately before you can begin to troubleshoot or capacity plan resource usage.
* Here are a few key items for which you should be measuring and collecting data on each system/network you manage:
	* system uptime
	* CPU usage and load statistics
	* memory usage and swap statistics
	* disk I/O and load statistics
	* network I/O and load statistics
	* firewall throughput
	* router throughput
	* network bandwidth usage
* For some command-line tools refer to `command-line-monitoring-utilities-table`. Find your distro's tools with `man -k monitor` and `man -k performance`.
	* Several utilities in Table 2.7 have additional resources that they monitor other than the abbreviated types listed in the Monitors column. See the man pages for a full description of these various utilities.
	* You can turn the *static* utilities here into *dynamic* by using the `watch` command.

> command-line-monitoring-utilities-table (Table 2.7 LPIC-2 Study Guide)

| utility | description | display type | monitors |
| :- | :- | :- | :- |
| free | shows the amount of free/used physical and swap memory | static | memory |
| htop | enhancement of the top utility, which allows horizontal as well as vertical scrolling, and uses function keys for process control | dynamic | cpu, memory, process states, uptime |
| iftop | similar to the top utility, it shows current network traffic information, including DNS | dynamic | network |
| iostat | shows device I/O loading summary broken down per device | static or dynamic | cpi, device i/o |
| iotop | similar to the top utility, it shows current I/O usage by processes (or threads) | dynamic | device i/o |
| ip | the -s link option and route option will Static display network and routing statistics. (Replaces the netstat command.) | static | network, routing |
| iptraf | shows network information, and it is menu driven | dynamic | network |
| lsof | hows open files and network connections by process | static | network, process map |
| mpstat | shows multiple processor statistics | static or dynamic | cpu |
| mtr | shows routing information for the URL parameter | dynamic | routing |
| netstat | the netstat -i option and -r option will display network and routing statistics. This command is considered obsolete. Use ip instead. | static | network, routing |
| ntop | gathers network statistics that can be viewed via a web browser via port 3000 | dynamic | network |
| pmap | shows a processes map for the PID parameter | static | process map |
| ps | shows current process information, including CPU consumption | static | cpu, process states |
| pstree | shows current processes in a tree format | static | process map |
| sar | acronym for System Activity Reporter: a Static or Dynamic multiple resource monitoring utility that collects and displays a wide variety of resource usage information. | static or dynamic | cpu, memory, network, device i/o |
| ss | displays socket statistics directly from kernel space. Provides more information than the netstat utility. | static | network |
| tcpdump | a packet analyzer/sniffer that shows designated network interface captured packet content descriptions. | dynamic | network |
| top | multiple display panels that show various resource usage data such as processes consuming the most CPU. Display can easily be changed on the fly. The atop and htop utilities are enhancements of the top command. | dynamic | cpu, memory, process states, uptime |
| uptime | shows how long the system has gone without a reboot, load averages, and current number of users. | static | uptime |
| vmstat | shows swap (virtual memory) performance | static or dynamic | memory |
| w | shows current user information, including CPU consumption. | static | cpu, process states |

### Predicting Resource Usage
* formally called ***Capacity Planning***
* involves these steps
	1. understanding the current user's needs
	2. monitoring the current system’s usage of resources
	3. gathering future direction and anticipated needs of the system users and applications
	4. making predictions and decisions based on the information gathered
* Capacity planning predictions need to have documented proof of both `current resource usage` and the `current resource usage growth rate through time`. Without this data, the projected `resource usage growth` and `anticipated capacity break point of a configuration` will be grossly inaccurate.
* There are several full-resource-monitoring software solutions that you can use to collect data and produce the needed graphs. Generally, these solutions are divided into *presentation software*, which produces useful charts and/or graphs, and *collector software* (also called a *data logger*), which gathers resource usage data. You’ll find that many of these software products have the ability to work together. A few of these are covered here:
	* **Cacti**
		* It is a resource usage presentation software solution, which provides the ability to produce usage graphs from templates. It is a front end to RRDTool.
		* Cacti stores its data in a MySQL database, and its front end is handled via PHP.
		* It is often used for monitoring network traffic because it can handle rather complex networks.
		* Also, it allows this gathered data to be used in MRTG graphs.
	* **collectd**
		* It is a daemon that allows you to monitor IT infrastructure usage.
		* Written in C for portability, it collects local (and remote with a network plugin) system statistics.
		* The `collectd` daemon is fairly easy to configure. You configure the data gathered and how it is gathered via plugins and a few other settings within the `collectd.conf` configuration file located in `/etc/` or `/etc/collectd/`, depending on your distribution. The config uration file’s *LoadPlugin* options determine which plugins to use in collectd.
	* **MRTG**
		* This software solution’s name is an acronym for *Multi Router Traffic Grapher*, which nearly says it all.
		* It collects and graphs network traffic data.
		* Written in Perl for portability, it can graph just about any network device’s statistics.
		* MRTG produces HTML pages that deliver a dynamic network traffic graph.
		* It can be used in conjunction with RRDTool as well.
	* **Nagios**
		* This very popular software solution suite comes in two flavors: FOSS and proprietary.
		* You’ll have to pay for the Nagios XI software solution, but the Nagios Core product is free.
		* Nagios Core provides monitoring of systems, network devices, and various services.
		* It uses a plugin that allows you to create customized service checks if desired.
		* Nagios Core provides a centralized view for all monitored items throughout your company. There is a web interface for viewing current and collected data and logs of previous outages, events, alerts, and so on.
		* Nagios Core is primarily a data collector, and it doesn’t provide usage or performance graphing. However, the collected data can be used with third-party graphing tools, such as PNP4Nagios and nagiosgraph.
		* One of Nagios Core’s best features is that it can send out problem alerts via email or text messaging. You can even incorporate your own custom alert script.
		* There is also a Nagios community that provides an ISO-certified CD-ROM for CentOS, including the tools most often used in Nagios. This allows you to install and set up Nagios quickly for monitoring. The Nagios community website is http://www.fullyautomatednagios.org/.
	* **Icinga**: Icinga started as a Nagios (described earlier) fork. It is now split into two different products, Icinga1 (the original Nagios fork) and Icinga2 (a total rewrite). Icinga is compatible and similar to Nagios, but incorporates a different (some feel it is better) user interface, and a quicker development cycle.
	* **RDDTool**: An industry standard, RRDTool stands for Round-Robin Database Tool, because its collected resource usage data is stored in a round-robin database. This database’s size doesn’t change because the oldest data is deleted whenever newer data is stored in it. It does provide tools on how to use this data in order to produce resource usage graphs. However, it is often used in other utilities, such as Cacti, MRTG, and Nagios.

### Troubleshooting Resource Usage
* Once you have monitoring resource usage and capacity planning in place, you will minimize having to troubleshoot resource usage. However, when troubles do come, they will be much easier to solve.
* The following are a few items to consider as you troubleshoot resource usage.
#### Memory
* Memory (also called RAM) is divided into 4 Kb chunks called pages.
* When the system needs more memory, using a memory management scheme, it takes an idle process’s memory pages and copies them to disk.
* This disk location is a special partition called swap space or swap or virtual memory.
* If the idle process is no longer idle, its memory pages are copied back into memory.
* This process of copying memory pages to and from the disk swap space is called swapping.
* You can view memory statistics on a system using command-line tools such as `free`, `sar`, and `vmstat`.
* If your system does not have properly sized memory, you should see high RAM usage. In addition, due to these memory issues, the system will increase swapping and result in increased disk I/O. The vmstat tool is handy in this case, because it allows you to view disk I/O specific to swapping as well as total blocks in and blocks out to the device.
* Be aware that RAM bottlenecks keep processor(s) usage artificially low. If you increase the RAM on your system, your processor(s) loads will also increase.
#### Processes
* It is crucial to identify what processes are using what resources, especially if a particular resource is having problems. You may need to determine if resource problems are causing the process problems or vice versa.
* The `ps`, `psmap`, and `pstree` utilities can be useful in correlating particular processes with particular resource problems.
* For example, if a disk is experiencing unusually high I/O, it may be due to a particular process and it may be causing a group of processes performance troubles. This is called **I/O blocking**. In this particular example, you would find these processes in what is called an *uninterruptible sleep*. The `vmstat` utility’s b column displays how many processes are in this state. To determine the actual processes, use the `ps` utility and look for a `D` process state.
* Don’t forget that the /proc directory has lots of useful information concerning a running system and its processes.
#### CPU
* For troubleshooting and monitoring purposes, you need to understand your CPU’s hardware. First, determine how many CPUs are on your system. For each CPU, you need to know the *number of processor cores*, whether or not *hyper-threading* is used, *cache sizes*, and so on. The `/proc/cpuinfo` file and the `lscpu` commands can be helpful here.
* The various CPU items to watch include *idle time*, *average use loads*, *queue length*, *interrupt request loads*, and so on. The `uptime`, `top`, `sar`, and `mpstat` are a few of the utilities to help you here.
#### Device I/O
* For device I/O, which is usually focused on disks, you need to understand your hardware. Is it NAS, iSCSI, or SAN? Are you using LVM, and what is the filesystem type employed? Once you understand your system’s underlying disk hardware, then you will be better able to interpret monitoring software and utilities data.
* The command-line utilities useful here include `iostat`, `iotop`, `lsof`, and `sar`.
* If your disks are accessed through your network, don’t forget to include network monitors as part of your device I/O troubleshooting toolkit.
#### Network Throughput
* Network package throughput and bottlenecks can be a constant worry in a system administrator’s life. Understanding your network’s hardware and topology is the first step in troubleshooting. Without a clear picture, you’ll be chasing rabbits instead of solving problems.
* Your network’s *size*, *hardware*, and *topology* will also determine what tools will work best for your troubleshooting purposes.
* The command-line utilities `iftop`, `ip`, `iptraf`, and `ntop` can be helpful. If set up to capture network traffic, the `sar` utility can also be used.
* Also, `lsof` can display what network services, such as FTP, are in use on your system, and `tcpdump` can provide network packet analysis.
* And let’s not forget those humble little helpful utilities such as `ping`, `traceroute`, and `ifconfig`.
* Keep in mind that if you manage a large network, the various full-resource-monitoring software solutions, such as MRTG, may be more useful for troubleshooting. Their graphics capabilities might prove necessary for locating bottlenecks.
