### Basic IP Address Structure
* IPv4 has `4,294,967,296 (~= 4b 300m)` addresses
* IPv6 has `340,282,366,920,938,463,463,374,607,431,768,211,456 (~= 3e38)`
* When the Internet's address structure was originally defined, every unicast IP address had a `network` portion, to identify the network on which the interface using the IP address was to be found, and a `host` portion, used to identify the particular host on the network given the network portion.
* With the realization that different networks might have different numbers of hosts, and that each host requires a unique IP address, a partitioning was devised wherein different-size allocation units of IP address space could be given out to different sites, based on their current and projected number of hosts.
* classful IP addressing
	* class types
		* refer to page 35 (TCP-IP Ill) for pictures
		* also locate `classful-IPv4-address-space-partitioning-table`
	* The classful approach to Internet addressing lasted mostly intact for the first decade of the Internet’s growth (to about the early 1980s). After that, it began to show its first signs of scaling problems—it was becoming too inconvenient to centrally coordinate the allocation of a new class A, B, or C network number every time a new network segment was added to the Internet. In addition, assigning class A and B network numbers tended to waste too many host numbers, whereas class C network numbers could not provide enough host numbers to many new sites.
	* subnet addressing
		* #todo summarize this: page 36 (TCP-IP Ill)
	* subnet masks
		* #todo summarize this: page 39 (TCP-IP Ill)

> classful-IPv4-address-space-partitioning-table

| class | address range | high-order bits | use | fraction of total | number of nets | number of hosts |
| :-: | :-: | :- | :-: | :- | :- | :- |
| A | 0.0.0.0 - 127.255.255.255 | 0 | unicast/special | 1/2 | 128 | 16,777,216 |
| B | 128.0.0.0 - 191.255.255.255 | 10 | unicast/special | 1/4 | 16,384 | 65,536 |
| C | 192.0.0.0 - 223.255.255.255 | 110 | unicast/special | 1/8 | 2,097,152 | 256 |
| D | 224.0.0.0 - 239.255.255.255 | 1110 | multicast | 1/16 | N/A | N/A |
| E | 240.0.0.0 - 255.255.255.255 | 1111 | reserved | 1/16 | N/A | N/A |

### CIDR as a Solution
* 3 particular internet issues in early 1990s
	* By 1994, over half of all class B addresses had already been allocated. It was expected that the class B address space would be exhausted by about 1995.
	* The 32-bit IPv4 address was thought to be inadequate to handle the size of the Internet anticipated by the early 2000s.
	* The number of entries in the global routing table (one per network num- ber), about 65,000 in 1995, was growing. As more and more class A, B, and C routing entries appeared, routing performance would suffer.
* CIDR: classless inter-domain routing

### Special-use Addresses
* multicast addressing group scopes
	* node-local: same computer
	* link-local: same subnet
	* site-local: same site
	* global: entire internet
* anycast addressing
	An anycast address is a unicast IPv4 or IPv6 address that identifies a different host depending on where in the network it is used. This is accomplished by configuring Internet routers to advertise the same unicast routes from multiple locations in the Internet. Thus, an anycast address refers not to a single host in the Internet, but to the “most appropriate” or “closest” single host that is responding to the anycast address. Anycast addressing is used most frequently for finding a computer that provides a common service. For example, a datagram sent to an anycast address could be used to find a DNS server, a 6to4 gateway that encapsulates IPv6 traffic in IPv4 tunnels, or RPs for multicast routing.

> IPv4-special-use-address-table

| prefix | special use |
| :- | :- |
| 0.0.0.0/8 | Hosts on the local network. May be used only as a source IP address. |
| 10.0.0.0/8 | Address for private networks (intranets). Such addresses never appear on the public Internet. |
| 127.0.0.0/8 | Internet host loopback addresses (same computer). Typically only 127.0.0.1 is used. |
| 169.254.0.0/16 | “Link-local” addresses—used only on a single link and generally assigned automatically. |
| 172.16.0.0/12 | Address for private networks (intranets). Such addresses never appear on the public Internet. |
| 192.0.0.0/24 | IETF protocol assignments (IANA reserved). |
| 192.0.2.0/24 | TEST-NET-1 addresses approved for use in documentation. Such addresses never appear on the public Internet. |
| 192.88.99.0/24 | Used for 6to4 relays (anycast addresses). |
| 192.168.0.0/16 | Address for private networks (intranets). Such addresses never appear on the public Internet. |
| 198.18.0.0/15 | Used for benchmarks and performance testing. |
| 198.51.100.0/24 | TEST-NET-2. Approved for use in documentation. |
| 203.0.113.0/24 | TEST-NET-3. Approved for use in documentation. |
| 224.0.0.0/4 | IPv4 multicast addresses (formerly class D); used only as destination addresses. |
| 240.0.0.0/4 | Reserved space (formerly class E), except 255.255.255.255. |
| 255.255.255.255/32 | Local network (limited) broadcast address. |

> IPv4-multicast-class-D-address-space-major-sections-table
> refer to page: 55 (TCP-IP Ill)

### IP Headers Fields
* Version
	* 4 bits
	* value 4 for IPv4 and 6 for IPv6
* Internet Header Length (IHL)
	* 4 bits
	* it's the number of 32-bit words in IPv4 header
	* because 4 bits -> IPv4 is limited to a maximum of 15 32-bit words, or 60 bytes
* Type of Service (ToS)
	* 8 bits
	* practically deprecated into:
		* 6 bit Differentiated Services Field (DS Field)
		* 2 bit Explicit Congestion Notification (ECN) field
* Total Length
	* total length of the IPv4 datagram in bytes
	* 16 bit -> max IPv4 datagram size = 65,535 bytes
	* **required field**
	* A host is **NOT** required to be able to receive an IPv4 datagram larger than 576 bytes
	* if an IP datagram is fragmented, this field reflects the length of each fragment
* Identification
	* helps identify each datagram sent by an IPv4 host, to ensure the fragments of one datagram are not confused with that of another!
* Time To Live (TTL)
	* sets an upper limit on the number of routers through which it can pass
* Protocol
	* indicates the type of data found in the payload
	* common values
		* 17: UDP
		* 6: TCP
		* 4: IPv4-in-IPv4
* Header Checksum
	* this is not calculated by the IP protocol itself, rather other protocols such as ICMP, IGMP, UDP and TCP check its integrity.
* 32-bit Source IP Address
* 32-bit Destination IP Address

### IP Forwarding
* The IP layer has some information on memory, usually called a `routing table` or a `forwarting table`, which it searches each time it receives a datagram to send.
* Forwarding table fields
	* Destination: 32-bit, used for matching the result of a masking operation
	* Mask: 32-bit field, applied as a bitwise AND mask to the destination IP address **of** a datagram being looked up in the table. The result is then compared with the set of destinations in the table entries.
	* Next-hop: 32-bit IPv4 address, of the next IP entity (router or host) to which the datagram should be sent. Usually this address is on the same network as the host. ***AKA***, gateway.
	* Interface: This contains an identifier used by the IP layer to reference the network interface that should be used to send the datagram to its next hop.
* The job of ensuring correctness of the routing table is given to one or more routing protocols, like RIP, OSPF, BGP and IS-IS.
* For examining the destination IP address, the following `longest prefix match algorithm` is performed:
	1. Search the table for all entries for which the following property holds.
	   `(D ^ m[j] = d[j]`, where m\[j\] is mask at j'th entry, d\[j\] is destination IP address at j'th entry, and D is the incoming datagram's destination IP address.
	   If a match occurs, the algorithm notes the index (j) and looks as to how many bits were resulted to 1. The more bits set to 1, the "better".
	2. The best matching entry e\[k\] (the one with largest number of bits set to 1) is selected, and forwarded to the n\[k\] IP address. n\[k\] being the next-hop field of the k'th entry.
	* ***IF*** no matches are found in the forwarding table the datagram is undeliverable. If it was generated locally on the same host, "host unreachable" error is presented, otherwise an ICMP message is normally sent back to the host that sent the datagram.

### Host Processing of IP Datagrams
* Although routers do not ordinarily have to consider which IP addresses to place in the Source IP Address and Destination IP Address fields of the packets they forward, hosts must consider both. Applications such as Web browsers may attempt to make connections to a named host or server that can have multiple addresses. The client system making such connections may also have multiple addresses. Thus, there is some question as to which address (and version of IP) should be used when sending a datagram. A more subtle point we shall explore is whether to accept traffic destined for a local IP address if it arrives on the wrong interface (i.e., one that is not configured with the destination address present in a received datagram).
* Host Models
	* strong host model
		* a datagram is accepted for delivery to the local protocol stack only if the IP address contained in the Destination IP Address field matches one of those configured upon which the datagram arrived.
		* sends datagrams from a particular interface only if one of the interface’s configured addresses matches the Source IP Address field in the datagram being sent.
		* The attraction of using this is for security concerns.
	* weak host model
		* a datagram carrying a destination address matching any of the local addresses may arrive on any interface and is processed by the receiving protocol stack, irrespective of the network interface upon which it arrived.
* Procedures for selecting Source/Destination IP Addresses
	* source address selection: page 223
	* destination address selection: page 224
	* default rules in RFC3484 for address selection
		* prefer source/destination address pairs where the addresses are of the same scope
		* prefer smaller smaller over larger scopes
		* avoid the use of temporary addresses when other addresses are available
		* and to otherwise prefer pairs with the longest common prefix
		* global addresses are preferred over temporary addresses if available
	* The selection is controlled by a `policy table`
