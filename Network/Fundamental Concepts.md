### Architectural Principles
#### Protocol Definition
The first definition of a *protocol* according to the *New Oxford American Dictionary* is, **The Official procedure or system of rules governing affairs of state or diplomatic occasions.**

#### Protocol Suite Definition
A collection of related protocols is called a ***Protocol Suite***. The design that specifies how various protocols of a protocol suite relate to each other and divide up tasks to be accomplished is called ***the architecture or reference model*** for the protocol suite.

#### Datagram
Connection-oriented networks, whether built on circuits or packets, were the most prevalent form of networking for many years. In the late 1960s, another option was developed known as the **datagram**. A datagram is a special type of packet in which all the identifying information of the source and final destination resides inside the packet itself (instead of in the packet switches). Although this tends to require *larger packets*, *per-connection state* at packet switches is no longer required and a *connectionless network* could be built, eliminating the need for a (complicated) signaling protocol. Datagrams were eagerly embraced by the designers of the early Internet, and this decision had profound implications for the rest of the protocol suite.

#### The End-to-End Argument
When large systems such as an operating system or protocol suite are being designed, a question often arises as to where a particular feature or function should be placed. One of the most important principles that influenced the design of the TCP/IP suite is called the ***end-to-end** argument*. The function in question can completely and correctly be implemented *only with the knowledge and help of the application standing at the end points of the communication system.* Therefore, providing that questioned function as a feature of the communication itself is not possible. (Sometimes an incomplete version of the function provided by the communication system may be useful as a performance enhancement.)

#### Fate Sharing
Fate sharing suggests placing all the necessary state to maintain an active communication association (e.g., virtual connection) at the same location with the communicating endpoints. With this reasoning, the only type of failure that destroys communication is one that also destroys one or more of the endpoints, which obviously destroys the overall communication anyhow. Fate sharing is one of the design philosophies that allows virtual connections (e.g., those implemented by TCP) to remain active even if connectivity within the network has failed for a (modest) period of time. Fate sharing also supports a “dumb network with smart end hosts” model, and one of the ongoing tensions in today’s Internet is what functions reside in the network and what functions do not.

### Design and Implementation
#### Protocol Architecture vs Implementation Architecture
Although a protocol architecture may suggest a certain approach to implementation, it usually does not include a mandate. Consequently, we make a distinction between the protocol architecture and the ***implementation architecture***, which defines how the concepts in a protocol architecture may be rendered into existence, usually in the form of software.

#### Layering
* With layering, each layer is responsible for a different facet of the communications. Layers are beneficial because a layered design allows developers to evolve different portions of the system separately, often by different people with somewhat different areas of expertise.
* The most frequently mentioned concept of protocol layering is based on a standard called the **Open Systems Interconnection** (OSI) model. (picture at page 9)
* `end-to-end` protcol means that implementing some protocols is only necessary for the end device (usually hosts). Whereas `hop-by-hop` protocol is used on two end systems and every intermediate system (physical and link layer to say the least).

### TCP-IP Suite
#### PDU Names
* (based on figure 1-5 page 14) (TCP-IP Illustrated)
* 4: Transport: TCP: `TCP segment`
* 3: Network: IP protocol: `IP datagram`
* 2.5: Link (adjunct): ARP protocol: `frames`

#### Forwarding
The destination address of each datagram is used to determine where each datagram should be sent, and the process of making this determination and sending the datagram to its next hop is called forwarding.
There are 3 types of IP addresses, and the type affects how forwarding is performed.
* `unicast` is destined for a single host
* `broadcast` is destined for all hosts on a given network
* `multicast` is destined for a set of hosts that belong to a multicast group

#### Port Numbers by publicity
* `well-known: 0-1023`
* `registered: 1024-49151`
* `dynamic/private: 49152-65535`

### Internet, Intranet, Extranet
* ***internet*** means multiple networks connected together using a common protocol suite
* ***Internet*** refers to the collection of hosts around the world that communicate with each other using TCP/IP
* The Internet is an internet and not the other way around.
* ***intranet*** refers to a private internetwork in a particular place like organization or enterprize
* ***extranet*** is a network containing servers accessible to certain partners or other associates using the Internet

### Networked Apps Design Patterns
* client/server
	* server types
		* `iterative`
			1. wait for client request to arrive
			2. process the client request
			3. send the response back to the client that send the request
			4. go back to step 1
			* problem is when step 2 takes a long time and other requests come and they have to wait
		* `concurrent`
			1. wait for a client request to arrive
			2. Start a new server instance to handle this client’s request. This may involve creating a new process, task, or thread, depending on what the underlying operating system supports. This new server handles one client’s entire request. When the requested task is complete, the new server terminates. Meanwhile, the original server instance continues to step 3.
			3. go back to step 1.
	* Note that we use the terms client and server to refer to applications and not to the particular computer systems on which they run. The very same terms are sometimes used to refer to the pieces of hardware that are most often used to execute either client or server applications. Although the terminology is thus somewhat imprecise, it works well enough in practice. As a result, it is common to find a server (in the hardware sense) running more than one server (in the application sense).
* peer-to-peer
	* Some applications are designed in a more distributed fashion where there is no single server. Instead, each application acts both as a client and as a server, sometimes as both at once, and is capable of forwarding requests. Some very popular applications (e.g., Skype, BitTorrent) are of this form. These applications are called peer-to-peer or **p2p** applications. A concurrent p2p application may receive an incoming request, determine if it is able to respond to the request, and if not forward the request on to some other peer. Thus, the set of p2p applications together form a network among applications, also called an **overlay network**. Such overlays are now commonplace and can be extremely powerful.
	* One of the primary problems in p2p networks is called the discovery problem. That is, how does one peer find which other peer(s) can provide the data or service it wants in a network where peers may come and go? This is usually handled by a bootstrapping procedure whereby each client is initially configured with the addresses and port numbers of some peers that are likely to be operating. Once connected, the new participant learns of other active peers and, depending on the protocol, what services or files they provide.

### Networking Standard Groups
* IETF: Internet Engineering Task Force
* IESG: Internet Engineering Steering Group
* IAB: Internet Architecture Board
* SDOs: Standard Defining Organizations
* IRTF: Internet Research Task Force
* ISOC: Internet Society
* RFC: Request for Comments
* IEEE: Institude of Electrical and Electronics Engineers
* W3C: World Wide Web Consortium
* ITU: International Telecommunication Union

### Firewalls
* A firewall is a type of router that restricts the traffic it forwards.
* the number of available IPv4 addresses was diminishing, with a threat of exhaustion. Something would have to be done with the way addresses were allocated and used. One of the most important mechanisms developed to deal with this, aside from IPv6, is called Network Address Translation (NAT).
* With NAT, Internet addresses need not be globally unique, and as a consequence they can be reused in different parts of the Internet, called address realms.

#### Firewall Types
* Given the enormous management problems associated with trying to keep end system software up-to-date and bug-free, the focus of resisting attacks expanded from securing end systems to restricting the Internet traffic allowed to flow to end systems by filtering out some traffic using firewalls. Today, firewalls are common, and several different types have evolved.
* Packet-filtering Firewalls
	* The packet-filtering firewall is an Internet router that drops datagrams that (fail to) meet specific criteria.
	* They can generally be configured to discard or forward packets whose headers meet (or fail to meet) certain criteria, called filters.
	* Simple filters include range comparisons on various parts of the network-layer or transport-layer headers. The most popular filters involve undesired IP addresses or options, types of ICMP messages, and various UDP or TCP services, based on the port numbers contained in each packet.
	* As we shall see, the simplest packet-filtering firewalls are stateless, whereas the more sophisticated ones are stateful. Stateless packet-filtering firewalls treat each datagram individually, whereas stateful firewalls are able associate packets with either previously observed packets or packets that arrive in the future to make inferences about datagrams or streams—either those belonging to a single transport association or those IP fragments that constitute an IP datagram. IP fragmentation can significantly complicate a firewall’s job, and stateless packet-filtering firewalls are easily confused by fragments.
* Proxy Firewalls
	* The proxy firewall operates as a multihomed server host from the viewpoint of an Internet client. That is, it is the endpoint of TCP and UDP transport associations; it does not typically route IP datagrams at the IP protocol layer.
	* They are not really Internet routers in the true sense. Instead, they are essentially hosts running one or more application-layer gateways (ALGs)—hosts with more than one network interface that relay traffic of certain types between one connection/association and another at the application layer.
	* They do not typically perform IP forwarding as routers do, although more sophisticated proxy firewalls are now available that combine various functions.
	* For this type of firewall, clients on the inside of the firewall are usually configured in a special way to associate (or connect) with the proxy instead of the actual end host providing the desired service.
	* common forms
		* HTTP proxy firewalls aka Web Proxies
			These proxies act as Web servers for internal clients and as Web clients when accessing external Web sites. Such proxies often also operate as Web caches. These caches save copies of Web pages so that subsequent accesses can be served directly from the cache instead of from the originating Internet Web server. Doing so can reduce latency to display Web pages and improve the experience of users accessing the Web. Some Web proxies are also used as content filters, which attempt to block access to certain Web sites based on a “blacklist” of prohibited sites. Conversely, a number of so-called tunneling proxy servers are available on the Internet. These servers (e.g., psiphon, CGIProxy) essentially perform the opposite function—to allow users to avoid being blocked by content filters.
		* SOCKS firewalls
			The SOCKS protocol is more generic than HTTP for proxy access and is applicable to more services than just the Web. Two versions of SOCKS are currently in use: version 4 and version 5. Version 4 provides the basic support for proxy traversal, and version 5 adds strong authentication, UDP traversal, and IPv6 addressing. To use a SOCKS proxy, an application must be written to use SOCKS (it must be “socksified”) and configured to know about the location of the proxy and which version of SOCKS to use. Once this is accomplished, the client uses the SOCKS protocol to request the proxy to perform network connections and, optionally, DNS lookups.
* The main difference between them is the layer in the protocol stack at which they operate, and consequently the way IP addresses and port numbers are used.

### Broadcasting and Local Multicasting
* there are 4 kinds of IP addresses: unicast, anycast, multicast and broadcast
* Broadcasting and Multicasting provide two services for an application:
	* delivery to multiple destinations
	* solicitation of servers by clients
* Although both broadcasting and multicasting can provide these important capabilities, multicasting is generally preferable to broadcasting because multicasting involves only those systems that support or use a particular service or protocol, and broadcasting does not.
* Broadcast request affects all hosts that are reachable within the scope of the broadcast, whereas multicast affects only those hosts that are likely to be interested in the request.
* There is a trade-off between the higher overhead and simplicity of broadcast and the improved efficiency but greater complexity associated with multicast.


#### Broadcasting
* A multicast MAC address has the low-order bit of the high order byte turned on. In hexadecimal it looks like 01:00:00:00:00:00.
* We may consider ethernet broadcast address as ff:ff:ff:ff:ff:ff as special cast of the ethernet multicast address.
* In IPv4, each subnet has a local subnet-directed broadcast address formed by placing all 1 bits in the host portion of the address.
* The special address 255.255.255.255 corresponds to a local network (also called "limited") broadcast.
* `ipcalc` package can calculate the local broadcast address e.g. by providing it with 10.0.0.0/25.
* Broadcast addressing and multicast addressing can be used to discover systems or services that are otherwise unknown.

#### Multicasting
* To reduce the amount of overhead involved in broadcasting, it is possible to send traffic only to those receivers that are interested in it. This is called multicasting. Fundamentally, this is accomplished by either having the sender indicate the receivers, or instead having the receivers independently indicate their interest. The network then becomes responsible for sending traffic only to intended/inter- ested recipients. Implementing multicast is considerably more challenging than broadcast because multicast state (information) must be maintained by hosts and routers as to what traffic is of interest to what receivers.
	* In the TCP/IP model of multicasting, receivers indicate their interest in what traffic they wish to receive by specifying a multicast address and optional list of sources. This information is maintained as soft state (see Chapter 4) within hosts and routers, meaning that it must be updated regularly or it will time out and be deleted. When this happens, delivery of multicast traffic either ceases or reverts to broadcast.
	* To make multicasting work, applications that wish to be involved in a communication require a mechanism to notify their protocol implementations of their desires. The host software can then arrange to receive packets matching the applications’ criteria.
* IP multicasting originated using a design based on the way group addressing works in link-layer networks such as Ethernet. In this approach, each station selects the group address for which it is willing to accept traffic, irrespective of the sender. This approach is also sometimes called any-source multicast (ASM) because of the insensitivity to the identity of the sender. As IP multicasting has evolved, an alternative form that is sensitive to the identity of the sender called source-specific multicast (SSM) has been developed that allows end stations to explicitly include or exclude traffic sent to a multicast group from a particular set of senders.
* Recall from chapter 2 that all IPv4 multicast addresses (class D) range from 224.0.0.0 through 239.255.255.255. (224.0.0.0/4)

### IP Fragmentation
* As we described in Chapter 3, link-layer framing normally imposes an upper limit on the maximum size of a frame that can be transmitted. To keep the IP datagram abstraction consistent and isolated from link-layer details, IP employs fragmentation and reassembly. Whenever the IP layer receives an IP datagram to send, it determines which local interface the datagram is to be sent over next (via a forwarding table lookup; see Chapter 5) and what MTU is required. IP compares the outgoing interface’s MTU with the datagram size and performs fragmentation if the datagram is too large. Fragmentation in IPv4 can take place at the original sending host and at any intermediate routers along the end-to-end path. Note that datagram fragments can themselves be fragmented.
* When an IP datagram is fragmented, it is not reassembled until it reaches its final destination. Two reasons have been given for this, the second more compelling than the first. First, not performing reassembly within the network alleviates the forwarding software (or hardware) in routers from implementing this feature. Second, it is possible for different fragments of the same datagram to follow different paths to their common destination. If this happens, no single router along the path would in general be capable of reassembling the original datagram because it would see only a subset of the fragments. The first argument is not terribly convincing at face value given the current performance levels of routers, but it is even less convincing when one considers that most routers must ultimately be capable of functioning as end hosts anyhow (e.g., when being managed or configured). The second argument remains compelling.

