### Introduction
* The IP protocol alone provides no direct way for an end system to learn the fate of IP packets that fail to make it to their destinations. In addition, IP provides no direct way of obtaining diagnostic information (e.g., which routers are used along a path or a method to estimate the round-trip time). To address these deficiencies, a special protocol called the Internet Control Message Protocol (ICMP) is used in conjunction with IP to provide diagnostics and control information related to the configuration of the IP protocol layer and the disposition of IP packets.
* ICMP is often considered part of the IP layer itself, and it is required to be present with any IP implementation. It uses the IP protocol for transport. So, precisely, it is neither a network nor a transport protocol but lies somewhere between the two.
* The most common cause of packet drops (buffer overrun at a router) does not elicit any ICMP information. Other protocols, such as TCP, handle such situations.
* Because of the ability of ICMP to affect the operation of important system functions and obtain configuration information, hackers have used ICMP messages in a large number of attacks. As a result of concerns about such attacks, network administrators often arrange to block ICMP messages with firewalls, especially at border routers. If ICMP is blocked, however, a number of common diagnostic utilities (e.g., ping, traceroute) do not work properly.
* an RFC provides a method to add extension objects to certain ICMP messages. This facility is used for holding Multiprotocol Label Switching (MPLS) information and for indicating which interface and next hop a router would use in forwarding a particular datagram. Another RFC gives standard behavioral characteristics of ICMP through NATs (also discussed in Chapter 7).

### ICMP Messages
* 2 Major ICMP Message Categories
	* error messages: those that relate to delivering IP datagrams
	* query messages aka informational messages: those related to information gathering and configuration
	* refer to `ICMPv4-message-types-table`

> ICMPv4-message-types-table
> - those with aterisks (*) are common
> - those with + may contain \[RFC4884\] extension objects

| type | official name | E/I | Use/Comment |
| :- | :- | :-: | :- |
| 0 (\*) | Echo Reply | Informational | Echo (ping) reply; returns data |
| 3 (\*)(+) | Destination Unreachable | Error | Unreachable host/protocol |
| 4 | Source Quench | Error | Indicates Congestion (deprecated) |
| 5 (\*) | Redirect | Error | Indicates alternate router should be used |
| 8 (\*) | Echo | Informational | Echo (ping) request (data optional) |
| 9 | Router Advertisement | Informational | Indicates router addresses/preferences |
| 10 | Router Solicitation | Informational | Requests router advertisement |
| 11 (\*)(+) | Time Exceeded | Error | Resource exhausted (e.g. IPv4 TTL) |
| 12 (\*)(+) | Parameter Problem | Error | Malformed Packet or Header |

#### ICMP Error Messages
* The distinction between the error and informational classes of ICMP messages mentioned in the previous section is important because certain restrictions are placed on the generation of ICMPv4 error messages that do not apply to queries. 
	* In particular, an ICMP error message is not to be sent in response to any of the following messages:
		* An ICMPv4 error message. (An ICMPv4 error message may, however, be generated in response to an ICMPv4 query message.)
		* A datagram destined for an IPv4 broadcast address or an IPv4 multicast address (formerly known as a class D address).
		* A datagram sent as a link-layer broadcast.
		* A fragment other than the first.
		* A datagram whose source address does not define a single host. This means that the source address cannot be a zero address, a loopback address, a broadcast address, or a multicast address.
	* The reason for imposing these restrictions on the generation of ICMP errors is to limit the creation of so-called broadcast storms, a scenario in which the generation of a small number of messages creates an unwanted traffic cascade (e.g., by generating error responses in response to error responses, indefinitely).
* In addition to the rules governing the conditions under which ICMP messages are generated, there is also a rule that limits the overall ICMP traffic level from a single sender. A recommendation for rate-limiting ICMP messages is to use a token bucket. With a token bucket, a “bucket” holds a maximum number (B) of “tokens,” each of which allows a certain number of messages to be sent. The bucket is periodically filled with new tokens (at rate N) and drained by 1 for each message sent. Thus, a token bucket (or token bucket filter, as it is often called) is characterized by the parameters (B, N). For small or midsize devices, an example token bucket is using the parameters (10, 10). Token buckets are a common mechanism used in protocol implementations to limit bandwidth utilization, and in many cases B and N are in byte units rather than message units.

##### ICMP Destination Unreachable (type 3)
* Messages of this type are used to indicate that a datagram could not be delivered all the way to its destination because of either a problem in transit or the lack of a receiver interested in receiving it.
* Although 16 different codes are defined for this message in ICMPv4, only 4 are commonly used.
	* Host Unreachable (code 1)
		* This message is generated when a router or a host is required to send an IP datagram to a host using direct delivery but for some reason cannot reach the destination.
	* Port Unreachable (code 3)
		* This message is generated when an incoming datagram is destined for an application that is not ready to receive it. This occurs most commonly in conjunction with UDP (see Chapter 10), when a message is sent to a port number that is not in use by any server process. If UDP receives a datagram and the destination port does not correspond to a port that some process has in use, UDP responds with an ICMP Port Unreachable message.
	* (PTB) Fragmentation Required/Don’t-Fragment Specified (code 4)
		* If an IPv4 router receives a datagram that it intends to forward, and if the datagram does not fit into the MTU in use on the selected outgoing network interface, the datagram must be fragmented (see Chapter 10). If the arriving datagram has the Don’t Fragment bit field set in its IP header, however, it is not forwarded but instead is dropped, and this ICMPv4 Destination Unreachable (PTB) message is generated. Because the router sending this message knows the MTU of the next hop, it is able to include the MTU value in the error message it generates.
		* This message was originally intended to be used for network diagnostics but has since been used for path MTU discovery. PMTUD is used to determine an appropriate packet size to use when communicating with a particular host, on the assumption that avoiding packet fragmentation is desirable. It is used most commonly with TCP.
	* and Communication Administratively Prohibited (code 13)
		* This message provides the ability to indicate that an *administrative prohibition* is preventing successful communication with the destination. This is typically the result of a firewall that intentionally drops traffic that fails to comply with some operational policy enforced by the router that sent the ICMP error. In many cases, the fact that there is a special policy to drop traffic should not be advertised, so it is generally possible to disable the generation of these messages by either silently discarding incoming packets or generating some other ICMP error message instead.

##### ICMP Redirect (type 5)
* If a router receives a datagram from a host and can determine that it is not the correct next hop for the host to have used to deliver the datagram to its destination, the router sends a Redirect message to the host and sends the datagram on to the correct router (or host). That is, if it can determine that there is a better next hop than itself for the given datagram, it redirects the host to update its forwarding table so that future traffic for the same destination will be directed toward the new node. This facility provides a crude form of routing protocol by indicating to the IP forwarding function where to send its packets.
* When the router sends the ICMP Redirect message to the host, it also forwards the datagram to where it should, as mentioned in page 372, which has said to be another router... Weird...
* The ICMP Redirect message contains the IP address of the better hop advised to the host.

##### ICMP Time Exceeded (type 11)
When a router discards (drops) an IP datagram because it has TTL value 0, it sends an ICMP Time Exceeded datagram back. Which is also the foundation that `traceroute` works upon.

##### ICMP Parameter Problem (type 12)
* ICMP Parameter Problem messages are generated by a host or router receiving an IP datagram containing some problem in its IP header that cannot be repaired. When a datagram cannot be handled and no other ICMP message adequately describes the problem, this message acts as a sort of “catchall” error condition indicator.
* It has a pointer field which indicates the byte offset where the problem was found in the IP header.
* It also has a code field indicating the type of Parameter problem
	* Code 0 is most common
	* Code 1 was formerly used to indicate that a required option was missing but is now historic
		* was once used to indicate missing options such as security labels on packets but is now historic
	* Code 2 indicates that the offending IPv4 datagram has a bad IHL or Total Length Field

#### ICMP Query/Infomational Messages
* ICMP query messages Address Mask Request/Reply (types 17/18), Timestamp Request/Reply (types 13/14), Information Request/Reply (types 15/16) have been replaced by other, more purpose-specific protocols (including DHCP).
* The remaining popular ICMP query messages are Echo Request/Response messages, more commonly called `ping`, and the Router Discovery messages.