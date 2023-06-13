> `sources`
> [Medium: IPTables Tutorial: Beginners to Advanced Guide To Linux Firewall](https://erravindrapawadia.medium.com/iptables-tutorial-beginners-to-advanced-guide-to-linux-firewall-839e10501759)
> [DigitalOcean: A Deep Dive into Iptables and Netfilter Architecture](https://www.digitalocean.com/community/tutorials/a-deep-dive-into-iptables-and-netfilter-architecture)

* For many years, the firewall software most commonly used in Linux was called `iptables`. In some distributions, it has been replaced by a new tool called `nftables`, but `iptables` syntax is still commonly used as a baseline.
* IPtables is a command-line firewall utility that uses policy chains to allow or block traffic that will be enforced by the linux kernel’s netfilter framework.
* The `iptables` firewall works by interacting with the packet filtering hooks in the Linux kernel’s networking stack. These kernel hooks are known as the `netfilter` framework.
* Iptables packet filtering mechanism is organized into three different kinds of structures: **tables**, **chains** and **targets**.
* Network traffic is made up of packets. Iptables identifies the packets received and then uses a set of rules to decide what to do with the packets that matches.

### Netfilter Hooks
- `NF_IP_PRE_ROUTING`: This hook will be triggered by any incoming traffic very soon after entering the network stack. This hook is processed before any routing decisions have been made regarding where to send the packet.
- `NF_IP_LOCAL_IN`: This hook is triggered after an incoming packet has been routed if the packet is destined for the local system.
- `NF_IP_FORWARD`: This hook is triggered after an incoming packet has been routed if the packet is to be forwarded to another host.
- `NF_IP_LOCAL_OUT`: This hook is triggered by any locally created outbound traffic as soon as it hits the network stack.
- `NF_IP_POST_ROUTING`: This hook is triggered by any outgoing or forwarded traffic after routing has taken place and just before being sent out on the wire.

* Kernel modules that need to register at these hooks must also provide a priority number to help determine the order in which they will be called when the hook is triggered. This provides the means for multiple modules (or multiple instances of the same module) to be connected to each of the hooks with deterministic ordering. Each module will be called in turn and will return a decision to the `netfilter` framework after processing that indicates what should be done with the packet.

### IPTables Tables and their Chains
* The `iptables` firewall uses tables to organize its rules. These tables classify rules according to the type of decisions they are used to make. For instance, if a rule deals with network address translation, it will be put into the `nat` table. If the rule is used to decide whether to allow the packet to continue to its destination, it would probably be added to the `filter` table.
* Within each `iptables` table, rules are further organized within separate “chains”. While tables are defined by the general aim of the rules they hold, the built-in chains represent the `netfilter` hooks which trigger them. Chains determine *when* rules will be evaluated.
* Chains and Netfilter Hooks associations:
	* each chain is triggered by a corresponding netfilter hook
	* PREROUTING -> NF_IP_PRE_ROUTING
	- INPUT -> NF_IP_LOCAL_IN
	- FORWARD -> NF_IP_FORWARD
	- OUTPUT -> NF_IP_LOCAL_OUT
	- POSTROUTING -> NF_IP_POST_ROUTING
* Chains allow the administrator to control where in a packet’s delivery path a rule will be evaluated. Since each table has multiple chains, a table’s influence can be exerted at multiple points in processing. Because certain types of decisions only make sense at certain points in the network stack, every table will not have a chain registered with each kernel hook.
* There are only five `netfilter` kernel hooks, so chains from multiple tables are registered at each of the hooks. For instance, three tables have `PREROUTING` chains. When these chains register at the associated `NF_IP_PRE_ROUTING` hook, they specify a ***priority*** that dictates what order each table’s `PREROUTING` chain is called. Each of the rules inside the highest priority `PREROUTING` chain is evaluated sequentially before moving onto the next `PREROUTING` chain.

#### Tables
##### 1. Filter
* The Filter table is used most frequently. This is default table.
* The `filter` table is used to make decisions about whether to let a packet continue to its intended destination or to deny its request.
* In firewall parlance, this is known as “filtering” packets.
* This table provides the bulk of functionality that people think of when discussing firewalls.
* Chains:
	* **INPUT**: This chain handles all packets that are destined to your server and also to control the behaviour for incoming connections.
		* For instance, if a user attempts to SSH into your PC/server, iptables will attempt to match the IP address and port to a rule in the input chain.
	* **FORWARD**: This chain is used for packets routed through the system. Think of a router, data is always being sent to it but rarely actually destined for the router itself, the data is just forwarded to its target.
	* **OUTPUT**: This chain contains rules for packets generated locally.
		* For instance, if you try to ping google.com, iptables will check its output chain to see what the rules are regarding pinging the google.com.

##### 2. NAT
* This table is consulted when a packet tries to create a new connection.
* This table is used to implement network address translation rules. As packets enter the network stack, rules in this table will determine whether and how to modify the packet’s source or destination addresses in order to impact the way that the packet and any response traffic are routed. This is often used to route packets to networks when direct access is not possible.
* Chains:
	* **PREROUTING**: This chain rule alters a packet as soon as it’s received.
	* **POSTROUTING**: This chain rule alters a packet as it is about to go out.
	* **OUTPUT**: This chain rule alerts locally generated traffic.

##### 3. RAW
* The Raw table is used to exempt packets from connection tracking.
* The `iptables` firewall is stateful, meaning that packets are evaluated in regards to their relation to previous packets. The connection tracking features built on top of the `netfilter` framework allow `iptables` to view packets as part of an ongoing connection or session instead of as a stream of discrete, unrelated packets. The connection tracking logic is usually applied very soon after the packet hits the network interface.
* The `raw` table has a very narrowly defined function. Its only purpose is to provide a mechanism for marking packets in order to opt-out of connection tracking.
* Chains:
	* **OUTPUT**: To alter locally generated packets.
	* **PREROUTING**: To alter incoming connections.

##### 4. Mangle
* The Mangle table adjusts the IP header properties of packets.
	* For instance, you can adjust the TTL (Time to Live) value of a packet, either lengthening or shortening the number of valid network hops the packet can sustain. Other IP headers can be altered in similar ways.
* This table can also place an internal kernel “mark” on the packet for further processing in other tables and by other networking tools. This mark does not touch the actual packet, but adds the mark to the kernel’s representation of the packet.
* Chains:
	- **INPUT**: for incoming packets.
	- **OUTPUT**: To alter locally generated packets.
	- **FORWARD**: for packets routed through the linux box.
	- **PREROUTING**: To alter incoming connections.
	- **POSTROUTING**: To alert outgoing connections.

##### 5. Security
* The `security` table is used to set internal SELinux security context marks on packets, which will affect how SELinux or other systems that can interpret SELinux security contexts handle the packets. These marks can be applied on a per-packet or per-connection basis.

#### Chains/Tables Relationship
* The following table indicates the chains that are available within each `iptables` table when read from left-to-right. For instance, we can tell that the `raw` table has both `PREROUTING` and `OUTPUT` chains. When read from top-to-bottom, it also displays the order in which each chain is called when the associated `netfilter` hook is triggered.
* A few things should be noted. In the representation below, the `nat` table has been split between `DNAT` operations (those that alter the destination address of a packet) and `SNAT` operations (those that alter the source address) in order to display their ordering more clearly. It also includes rows that represent points where routing decisions are made and where connection tracking is enabled in order to give a more holistic view of the processes taking place.

| Tables↓/Chains→ | PREROUTING | INPUT | FORWARD | OUTPUT | POSTROUTING |
| :- | :-: | :-: | :-: | :-: | :-: |
| (routing decision) | | | | ✓ | |
| raw | ✓ | | | ✓ | |
| (connection tracking enabled) | ✓ | | | ✓ | |
| mangle | ✓ | ✓ | ✓ | ✓ | ✓ |
| nat (DNAT) | ✓ | | | ✓ | |
| (routing decision) | ✓ | | | ✓ | |
| filter | | ✓ | ✓ | ✓ | |
| security | | ✓ | ✓ | ✓ | |
| nat (SNAT) | | ✓ | | | ✓ |

* As a packet triggers a `netfilter` hook, the associated chains will be processed as they are listed in the table above from top-to-bottom. The hooks (columns) that a packet will trigger depend on whether it is an incoming or outgoing packet, the routing decisions that are made, and whether the packet passes filtering criteria.
* Certain events will cause a table’s chain to be skipped during processing. For instance, only the first packet in a connection will be evaluated against the NAT rules. Any `nat` decisions made for the first packet will be applied to all subsequent packets in the connection without additional evaluation. Responses to NAT’ed connections will automatically have the reverse NAT rules applied to route correctly.

#### Chain Traversal Order
* Assuming that the server knows how to route a packet and that the firewall rules permit its transmission, the following flows represent the paths that will be traversed in different situations:
	-   **Incoming packets destined for the local system**: `PREROUTING` -> `INPUT`
	-   **Incoming packets destined to another host**: `PREROUTING` -> `FORWARD` -> `POSTROUTING`
	-   **Locally generated packets**: `OUTPUT` -> `POSTROUTING`
* If we combine the above information with the ordering laid out in the previous table, we can see that an incoming packet destined for the local system will first be evaluated against the `PREROUTING` chains of the `raw`, `mangle`, and `nat` tables. It will then traverse the `INPUT` chains of the `mangle`, `filter`, `security`, and `nat` tables before finally being delivered to the local socket.

### IPTables Rules
* Rules are placed within a specific chain of a specific table. As each chain is called, the packet in question will be checked against each rule within the chain in order. Each rule has a matching component and an action component.

#### Matching
* The matching portion of a rule specifies the criteria that a packet must meet in order for the associated action (or “target”) to be executed.
* The matching system is very flexible and can be expanded significantly with additional `iptables` extensions. Rules can be constructed to match by protocol type, destination or source address, destination or source port, destination or source network, input or output interface, headers, or connection state among other criteria. These can be combined to create complex rule sets to distinguish between different traffic.

#### IPTables Targets
* When a packet matches a rule and it is given a **target**, which can be another chain, or a special option.
* Special Options:
	- **REJECT**: Means server receives the packet and rejects that packet and also send the acknowledgement.
	- **DROP**: Means server receives the packet and drop the request without sending any acknowledgement.
	- **ACCEPT**: Means server receives the packet and server allows that request.
	- **RETURN**: this rule sends the packet back to the originating chain so you can match it against other rules.
- Targets are generally divided into two categories:
	- **Terminating targets**: Terminating targets perform an action which terminates evaluation within the chain and returns control to the `netfilter` hook. Depending on the return value provided, the hook might drop the packet or allow the packet to continue to the next stage of processing.
	- **Non-terminating targets**: Non-terminating targets perform an action and continue evaluation within the chain. Although each chain must eventually pass back a final terminating decision, any number of non-terminating targets can be executed beforehand.

##### User-Defined Chains
* There is also a special class of non-terminating target: the jump target. Jump targets are actions that result in evaluation moving to a different chain for additional processing. We’ve covered the built-in chains which are tied to the `netfilter` hooks that call them. However, `iptables` also allows administrators to create their own chains for organizational purposes.
* Rules can be placed in user-defined chains in the same way that they can be placed into built-in chains. The difference is that user-defined chains can only be reached by “jumping” to them from a rule (they are not registered with a `netfilter` hook themselves).
* User-defined chains act as extensions of the chain which called them. For instance, in a user-defined chain, evaluation will pass back to the calling chain if the end of the rule list is reached or if a `RETURN` target is activated by a matching rule. Evaluation can also jump to additional user-defined chains.
* This construct allows for greater organization and provides the framework necessary for more robust branching.

### IPTables and Connection Tracking
* We introduced the connection tracking system implemented on top of the `netfilter` framework when we discussed the `raw` table and connection state matching criteria. Connection tracking allows `iptables` to make decisions about packets viewed in the context of an ongoing connection. The connection tracking system provides `iptables` with the functionality it needs to perform “stateful” operations.
* Connection tracking is applied very soon after packets enter the networking stack. The `raw` table chains and some sanity checks are the only logic that is performed on packets prior to associating the packets with a connection.
* The system checks each packet against a set of existing connections. It will update the state of the connection in its store if needed and will add new connections to the system when necessary. Packets that have been marked with the `NOTRACK` target in one of the `raw` chains will bypass the connection tracking routines.
* ***Available States***:
	- **NEW**: When a packet arrives that is not associated with an existing connection, but is not invalid as a first packet, a new connection will be added to the system with this label. This happens for both connection-aware protocols like TCP and for connectionless protocols like UDP.
	- **ESTABLISHED**: A connection is changed from `NEW` to `ESTABLISHED` when it receives a valid response in the opposite direction. For TCP connections, this means a `SYN/ACK` and for UDP and ICMP traffic, this means a response where source and destination of the original packet are switched.
	- **RELATED**: Packets that are not part of an existing connection, but are associated with a connection already in the system are labeled `RELATED`. This could mean a helper connection, as is the case with FTP data transmission connections, or it could be ICMP responses to connection attempts by other protocols.
	- **INVALID**: Packets can be marked `INVALID` if they are not associated with an existing connection and aren’t appropriate for opening a new connection, if they cannot be identified, or if they aren’t routable among other reasons.
	- **UNTRACKED**: Packets can be marked as `UNTRACKED` if they’ve been targeted in a `raw` table chain to bypass tracking.
	- **SNAT**: This is a virtual state set when the source address has been altered by NAT operations. This is used by the connection tracking system so that it knows to change the source addresses back in reply packets.
	- **DNAT**: This is a virtual state set when the destination address has been altered by NAT operations. This is used by the connection tracking system so that it knows to change the destination address back when routing reply packets.
- The states tracked in the connection tracking system allow administrators to craft rules that target specific points in a connection’s lifetime. This provides the functionality needed for more thorough and secure rules.

### Install IPTables
* `sudo apt install iptables`
* `sudo apt install iptables-persistent`
	* For when you want to keep iptables firewall rules when you reboot the system.

### IPTables Basic Syntax
* `sudo iptables [option] CHAIN_rule [-j target]`
* common options:
	- `–A` - append: Add a rule to the chain (at the end).
	- `–C` - check: Look for a rule that matches the chain’s requirements.
	- `–D` - delete: Remove specified rules from the chain.
	- `–F` - flush: Remove all rules.
	- `–I` - insert: Add a rule to a chain at some given position.
	- `–L` - list: Show all rules in a chain.
	- `–N` - new–chain: Create a new chain.
	- `–v` - verbose: Show more information when using a list option.
	- `–X` - delete–chain: Delete the provided chain.

#### Configuring IPTables Rules
* check current iptables status
	* `sudo iptables -L`
* get the status of the packets transferred
	* `sudp iptables -L -n -v`
* you can allow loopback access (access from 127.0.0.1) from localhost. This configures the firewall to accept traffic for the localhost interface.
	* `sudo iptables -A INPUT -i lo -j ACCEPT`
	* `sudo iptables -A OUTPUT -o lo -j ACCEPT`
* block an specific IP address.
	* `iptables -A INPUT -s 192.168.72.128 -j DROP`
	* `iptables -A INPUT -p tcp -s 192.168.72.128 -j DROP`
		* This blocks only tcp connections.
	* `iptables -A INPUT -m iprange --src-range 192.168.72.1-192.168.72.255 -j REJECT`
		* This blocks a range of IPs.
* unblock an IP address.
	* `iptables -D INPUT -s 192.168.72.128 -j DROP`
* allow traffic on specific ports.
	* `iptables -A INPUT -p tcp --dport [port e.g. 80] -j ACCEPT`
* block specific port
	* `iptables -A OUTPUT -p tcp --dport 80 -j DROP`
* allow multiple ports on iptables using multiport
	* `iptables -A INPUT -p tcp -m multiport --dport 22,80,443 -j ACCEPT`
	* `iptables -A OUTPUT -p tcp -m multiport --sport 22,80,443 -j ACCEPT`
* allow specific network range on particular port
	* `iptables -A OUTPUT -p tcp -d 192.168.72.128/24 --dport 22 -j ACCEPT`
* block incoming ping request
	* `iptables -A INPUT -p icmp -i eth0 -j DROP`
* flush iptables firewall chains or rules
	* `iptables -F`
		* drops all chains
	* `iptables -t nat -F`
		* drop from specific table
* save rules to file
	* `iptables-save > /path/to/file.rules`
* restore rules from file
	* `iptables-restore < /path/to/file.rules`
* drop unwanted traffic. If you already define dport firewall rules, you need to prevent unauthorized access by dropping any traffic that comes through other ports.
	* `iptables -A INPUT -j DROP`
* delete a rule
	* `iptables -L --line-numbers`
		* add line numbering when listing rules
	* `iptables -D INPUT <line-number>`