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

### Path MTU

> [!Question] ChatGPT
> **Explain Path MTU**
>
> Path Maximum Transmission Unit (Path MTU) refers to the maximum size of an IP packet that can be transmitted without fragmentation along the entire path of a network route. It's an important concept in networking, particularly for ensuring efficient and reliable data transmission across networks with varying link and router capabilities.
>
> In Internet Protocol (IP) networks, data is transmitted in packets. These packets have a maximum size defined by the Maximum Transmission Unit (MTU), which is the largest size of data that a network link can carry in a single transmission. However, as data travels through different network links and routers, it's possible that some links have smaller MTUs than others. If a packet is too large to pass through a link with a smaller MTU, it will need to be fragmented into smaller pieces, transmitted, and then reassembled at the receiving end.
> 
> Path MTU plays a role in optimizing data transmission by avoiding fragmentation. Here's how it works:
>
> 1. **Path Discovery:** When a device wants to send data to a destination, it first attempts to discover the smallest MTU along the entire path between the sender and receiver. This is achieved using the "Path MTU Discovery" process.
>    
> 2. **ICMP Messages:** If a router along the path encounters a packet that is larger than its MTU, it can send an Internet Control Message Protocol (ICMP) "Fragmentation Needed" message back to the sender. This message indicates the MTU of the router.
>    
> 3. **Sender Behavior:** Upon receiving an ICMP "Fragmentation Needed" message, the sender adjusts the size of the packets it sends to match the smallest MTU in the path. This ensures that no fragmentation is required during transmission, reducing the chances of packet loss, reassembly overhead, and potential performance issues.
>    
> 4. **Optimized Transmission:** By using the smallest MTU along the path, data can be transmitted efficiently without fragmentation. This helps improve the reliability and performance of data transmission.
>    
> 5. **MTU Black Hole:** In some cases, a router may not send the required ICMP message when it encounters a large packet. This can lead to a "black hole" situation, where large packets get dropped, and the sender is unaware of the issue.
>    
>
> It's worth noting that while Path MTU Discovery can significantly improve data transmission efficiency, some networks or devices might block ICMP messages due to security concerns. In such cases, the sender may need to use a conservative MTU value to avoid fragmentation, even though a larger MTU could be supported on parts of the path.

### Network Layers
> [!Question] ChatGPT
> **Thouroughly explain TCP/IP Layers in comparison to OSI and in relation to the protocols.**
>
> The TCP/IP protocol suite and the OSI (Open Systems Interconnection) model are two different conceptual frameworks used to describe the functionality of networking protocols. Both models are used to help understand how networking protocols work together to enable communication between devices on a network. Let's break down the TCP/IP layers in comparison to OSI and how they relate to specific protocols:
>
> **TCP/IP Protocol Suite:**
> The TCP/IP protocol suite consists of four layers, often referred to as a "stack," each responsible for specific networking functions. These layers are:
>
> 1. **Application Layer:** This layer deals with the communication between end-user applications and network services. It includes protocols that define the structure and content of data exchanged between applications. Examples of protocols at this layer include HTTP, HTTPS, FTP, SMTP, and DNS.
>
> 2. **Transport Layer:** The transport layer handles end-to-end communication and data segmentation, ensuring data reliability and integrity. It manages flow control, error correction, and retransmission of lost or corrupted packets. Two key transport layer protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
>
> 3. **Internet Layer:** Also known as the network layer, this layer handles routing and forwarding of data packets between different networks. It encapsulates data into packets, adds source and destination IP addresses, and manages routing decisions. The main protocol at this layer is the IP (Internet Protocol), which defines IP addresses and packet routing.
>
> 4. **Link Layer:** The link layer deals with the physical transmission of data on the local network segment. It includes both the data link and physical layers of the OSI model. This layer is responsible for framing data into frames, managing access to the physical medium, and addressing devices on the local network. Ethernet, Wi-Fi, and PPP are examples of link layer protocols.
>
> **OSI Model:**
> The OSI model consists of seven layers, each representing a specific aspect of networking functionality:
>
> 1. **Application Layer:** Similar to the TCP/IP application layer, it deals with user application communication and network services.
>
> 2. **Presentation Layer:** Responsible for data translation, encryption, and compression, ensuring that data sent by one application is understood by another.
>
> 3. **Session Layer:** Manages communication sessions between applications and provides mechanisms for checkpointing, recovery, and synchronization.
>
> 4. **Transport Layer:** Similar to the TCP/IP transport layer, it ensures reliable end-to-end communication and manages flow control and error correction.
>
> 5. **Network Layer:** Corresponds to the TCP/IP internet layer, handling routing, addressing, and packet forwarding across different networks.
>
> 6. **Data Link Layer:** Similar to the TCP/IP link layer, it deals with framing, addressing, and error detection on the local network segment.
>
> 7. **Physical Layer:** Deals with the actual transmission of raw binary data over physical media, defining characteristics such as voltage levels, cable types, and physical connectors.
> 
> **Relation to Protocols:**
> Both models describe the functionality of networking protocols, but they don't have a one-to-one correspondence between layers and protocols. Protocols can span multiple layers, and different protocols can exist within the same layer. For example:
>
> - HTTP, a protocol at the TCP/IP application layer, deals with web page retrieval. In the OSI model, its functions spread across the application and presentation layers.
>
> - TCP and UDP are transport layer protocols in the TCP/IP model, while the OSI model exclusively has these functions in the transport layer.
>
> - Ethernet operates at the link layer in both models but also encompasses the data link and physical layers in the OSI model.
>
> In summary, while both the TCP/IP and OSI models provide a conceptual framework for understanding networking protocols, the specific protocols they encompass and the way they organize networking functions may differ.

### Protocols
* ***Application Layer (Layer 7):**
   1. **HTTP (Hypertext Transfer Protocol)**
      - Often uses TCP for reliable transport.
      - port 80
   2. **HTTPS (Hypertext Transfer Protocol Secure)**
      - Relies on SSL/TLS for encryption and TCP for transport.
      - port 443
   3. **SSH (Secure Shell)**
      * Used for secure remote access and data communication between devices.
      * For security it often uses Public Key Cryptography.
      * Relies on TCP
      * port 22
   4. **FTP (File Transfer Protocol)**
      - Often uses TCP for reliable data transfer.
      - port 21
   5. **SFTP (SSH File Transfer Protocol)**
      - Secure version of FTP that uses SSH for encrypted file transfer.
      - Requires SSH for security.
      - port 22
   6. **SMTP (Simple Mail Transfer Protocol)**
      - Used for sending emails between mail servers.
      - Often uses TCP for reliable communication.
      - port 25
   7. **POP3 (Post Office Protocol version 3)**
      - Used by email clients to retrieve emails from mail servers.
      - Typically used with TCP.
      - port 110
   8. **IMAP (Internet Message Access Protocol)**
      - Used by email clients to manage and retrieve emails from mail servers.
      - Also relies on TCP for communication.
      - port 143
   9. **DNS (Domain Name System)**
      - Uses UDP for query/response and sometimes TCP for larger queries.
      - port 53
   10. **SNMP (Simple Network Management Protocol)**
      - Used for monitoring and managing network devices.
      - Typically relies on UDP.
      - port 161
   11. **Telnet**
      - Provides terminal emulation for remote access to devices.
      - Often uses TCP.
      - port 23
   12. **LDAP (Lightweight Directory Access Protocol)**
      - Used to access and manage directory information.
      - Relies on TCP.
      - port 389
   13. **HTTP/2 and HTTP/3:** Updates to HTTP with improved performance and security.
      - HTTP/2 uses multiplexing and compression, HTTP/3 uses QUIC protocol for transport.
   14. **SSL (Secure Sockets Layer) / TLS (Transport Layer Security):** Used to secure data transmission over the internet.
     - Often used with HTTPS, SMTPS, IMAPS, and other secure protocols.
     - port 443
   15. **VPN Protocols (e.g., PPTP, L2TP, IPsec):** Used for creating secure virtual private networks.
      - Work with various transport and network layer protocols.
   16. **S/MIME (Secure/Multipurpose Internet Mail Extensions):** Adds security to email by encrypting and digitally signing messages.
      - Works with email protocols like SMTP, POP3, and IMAP.

* ***Presentation Layer (Layer 6):**
	- This layer is often associated with data translation, encryption, and compression, but it's less focused on distinct protocols.

* ***Session Layer (Layer 5):**
	- This layer is responsible for managing communication sessions, but it's less associated with distinct protocols.

* ***Transport Layer (Layer 4):**
   1. **TCP (Transmission Control Protocol)**
      - Provides reliable, connection-oriented data transfer.
      - Often used with application protocols that require reliable communication.
      - Relies on the Internet Protocol (IP)
   2. **UDP (User Datagram Protocol)** 
      - Provides lightweight, connectionless data transfer.
      - Used for applications that prioritize speed over reliability.
      - Relies on the Internet Protocol (IP)
   3. **QUIC (Quick UDP Internet Connections)**
      * It's a modern connection-less transport protocol developed by Google to improve the performance of web applications over the internet.
      * It's designed to address some of the limitations and inefficiencies of traditional transport protocols like TCP (Transmission Control Protocol) and TLS (Transport Layer Security) when used in combination.
      * Relies on UDP
      * Has built-in encryption similar to TLS

* ***Network Layer (Layer 3):**
   1. **IP (Internet Protocol)**
      - Provides logical addressing and routing of data packets.
      - Relies on ARP for ip discovery
   2. **ICMP (Internet Control Message Protocol)**
      - Used for sending error and control messages.
      - Works alongside IP for error reporting and diagnostics.
   3. **ARP (Address Resolution Protocol)**
      - Maps IP addresses to MAC addresses on a local network.
      - Relies on Ethernet frames on Ethernet networks.
   4. **RIP (Routing Information Protocol)**
      - Used for dynamic routing within small networks.
      - Works with IP for routing updates.
   5. **OSPF (Open Shortest Path First)**
      - Interior gateway protocol for larger networks.
      - Operates with IP for routing and link-state updates.
   6. **BGP (Border Gateway Protocol)**
      - Used for routing between autonomous systems.
      - Works with IP for inter-domain routing.

* ***Data Link Layer (Layer 2):**
   1. **Ethernet**
      - Provides the physical and data link layer functionality for LANs.
      - Uses MAC addresses for addressing.
   2. **802.11 (WiFi)**
      - Wireless LAN standard for wireless data transmission.
      - Includes various security protocols like WPA, WPA2, WPA3.
   3. **PPP (Point-to-Point Protocol)**
      - Used for dial-up and serial connections.
      - Often used for establishing point-to-point connections.

* ***Physical Layer (Layer 1):**
	- This layer defines the physical medium and signaling for data transmission, so it's not typically associated with distinct protocols.