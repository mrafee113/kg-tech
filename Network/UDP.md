### Introduction
* UDP is a simple, datagram-oriented, transport-layer protocol that preserves message boundaries.
	* It does not provide:
		* error correction
		* sequencing
		* duplicate elimination
		* flow control
		* congestion control
	* It **can** provide error detection
	* It includes an end-to-end checksum at the transport layer.
	* This protocol provides minimal functionality itself, so applications using it have a great deal of control over how packets are sent and processed. Applications wishing to ensure that their data is reliably delivered or sequenced must implement these protections themselves.
	* Generally, each UDP output operation requested by an application produces exactly one UDP datagram, which causes one IP datagram to be sent.
* There is no protocol mechanism to prevent high-rate UDP traffic from negatively impacting other network users.
* Given this lack of reliability and protection, we might be tempted to conclude that there are no benefits to using UDP at all. This is not true, however.
	* Because of its connectionless character, it has less overhead than other transport protocols. In addition, broadcast and multicast operations are much more straightforward using a connectionless transport such as UDP. Finally, the ability of an application to choose its own unit of retransmission can be an important consideration.
* IPv4 protocol field has value 17 to indicate UDP. 

### UDP Header
* Port numbers act as mailboxes and help a protocol implementation identify the sending and receiving processes. They are purely abstract—they do not correspond to any physical entity on a host.
* In UDP, port numbers are positive 16-bit numbers, and the source port number is optional; it may be set to 0 if the sender of the datagram never requires a reply.
* Transport protocols such as TCP, UDP, and SCTP use the destination port number to help demultiplex incoming data from IP. Because IP demultiplexes the incoming IP datagram to a particular transport protocol based on the value of the Protocol field in the IPv4 header, this means that the port numbers can be made independent among the transport protocols. That is, TCP port numbers are used only by TCP, and the UDP port numbers only by UDP, and so on.
	* A straightforward consequence of this separation is that two completely distinct servers can use the same port number and IP address, as long as they use different transport protocols.
	* Despite this independence, if a well-known service is provided (or can conceivably be provided) by both TCP and UDP, the port number is normally allocated to be the same for both transport protocols. This is purely for convenience and is not required by the protocols.

### UDP Checksum
* It is computed at the initial sender and checked at the final destination.
* It is not modified in transit except when it passes through a NAT.
* IPv4 checksum covers only the IP header and not the data. And is also recalculated at every hop due to TTL being decremented.
* Transport protocol checksums cover their header and data. With UDP, the checksum is optional (although strongly suggested), while with the others it is mandatory.
* To provide error-free data to applications, a transport-layer protocol such as UDP must always compute a checksum or use some other error detection mechanism before delivering the data to a receiving application.

### UDP-Lite
* Some applications are tolerant of bit errors that may be introduced in the data they send and receive. Often, these types of applications wish to use UDP in order to avoid connection setup overhead or to use broadcast or multicast addressing, but UDP uses a checksum that covers either the entire payload or none of it (i.e., when no checksum is computed by the sender). A protocol called UDP-Lite or UDPLite addresses this issue by modifying the conventional UDP protocol to provide partial checksums. Such checksums cover only a portion of the payload in each UDP datagram. UDP-Lite has its own IPv4 Protocol, so it effectively counts as a separate transport protocol.

### UDP Path MTU Discovery
* Let us examine the interaction between an application using UDP and the path MTU discovery mechanism (PMTUD). For a protocol such as UDP, in which the calling application is generally in control of the outgoing datagram size, it is useful if there is some way to determine an appropriate datagram size if fragmentation is to be avoided. Conventional PMTUD uses ICMP PTB messages (see Chapter 8) in determining the largest packet size along a routing path that can be used without inducing fragmentation. These messages are typically processed below the UDP layer and are not directly visible to an application, so either an API call is used for the application to learn the best current estimate of the path MTU size for each destination with which it has communicated, or the IP layer can perform PMTUD independently without the application knowing. The IP layer often caches PMTUD information on a per-destination basis and times it out if it is not refreshed.

### UDP Server Design
* 10.11.1 IP Addresses and UDP Port Numbers
	* What arrives at a UDP server from a client is a UDP datagram. The IP header contains the source and destination IP addresses, and the UDP header contains the source and destination UDP port numbers. When an application receives a UDP message, the IP and UDP headers have been stripped off; the application must be told by the operating system in some other way who sent the message (the source IP address and port number), if it intends to furnish a reply. This feature allows a UDP server to handle multiple clients.
	* Some servers need to know to whom the datagram was sent, that is, the destination IP address. While it may seem obvious that such information would immediately be known by a server without looking into the received datagram, this is not always the case. For example, because of multihoming, IP address aliasing, and ordinary IPv6 usage with multiple scopes, a host may have multiple IP addresses, and a single server may receive incoming datagrams using any of them (this is in fact the common case). Any server wishing to perform its tasks differently depending on the destination IP address selected by the client would require access to the destination IP address information.
		* The lesson here is that even though an API may deliver all the data contained in a transport-layer datagram, additional information from the various layers (typically addressing information) may be required for a server to operate most effectively.
* 10.11.2 Restricting Local IP Addresses
	* Most UDP servers wildcard their local IP address when they bind a UDP endpoint. This means that an incoming UDP datagram destined for the server’s port is accepted on any local IP address (any IP address in use on the local machine, including the local loopback address).
