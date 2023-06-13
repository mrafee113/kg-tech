### Introduction
* Configuration information is used to assign local names to systems, and identifiers (such as IP addresses) to interfaces. It is also used to either provide or make use of various network services, such as DNS and Mobile IP home agents.
* Recall from chapter 2 that every interface to be used with TCP/IP networking requires an IP address, subnet maks, and broadcast address. The broadcast address can ordinarily be determined using the address and mask.
* Reasons for using a dynamic autoconfiguration mechanism
	1. client hosts are moved around more often than servers and routers, meaning they should have mechanisms for flexibly reassigning their configuration information.
	2. server hosts and routers are expected to be “always available” and relatively autonomous. As such, having their configuration information not depend on other network services can lead to greater confidence in their reliability.
	3. there are often far more clients in an organization than servers or routers, so it is simpler and less error-prone to use a centralized service to dynamically assign configuration information to client hosts.
	4. the operators of clients often have less system administration experience than server and router administrators, so it is once again less error-prone to have most clients configured by a centralized service administered by an experienced staff.

## DHCP
### BOOTP -> DHCP
* The design of DHCP is based on an earlier protocol called the Internet Bootstrap Protocol (BOOTP), which is now effectively obsolete.
* BOOTP provides limited configuration information to clients and does not have a mechanism to support changing that information after it has been provided. DHCP extends the BOOTP model with the concept of leases and can provide all information required for a host to operate.
* Leases allow clients to use the configuration information for an agreed-upon amount of time. A client may request to renew the lease and continue operations, subject to agreement from the DHCP server. BOOTP and DHCP are backward-compatible in the sense that BOOTP-only clients can make use of DHCP servers and DHCP clients can make use of BOOTP-only servers. BOOTP, and therefore DHCP as well, is carried using UDP/IP (see Chapter 10). Clients use port 68 and servers use port 67.

### Address Pools and Leases
* in dynamic ip allocation -> client requests an ip -> server responds with an ip from an ip pool
* Typically the IP pool is a contiguous range of IP addresses allocated specifically for DHCP.
* Lease duration is the specific amount of time that the client can allocate an IP.
	* client has ability to request an extension of the lease required.
	* they can range from a few minutes to a few days or more. ("infinite" is possible.)
	* determining best value for leases is a trade-off between
		* these things
			* number of expected clients
			* size of the address pool
			* the desire for stability of addresses
		* Longer lease durations tend to deplete the available address pool faster but provide greater stability in addresses and somewhat reduced network overhead (because there are fewer requests to renew leases).
		* Shorter leases tend to keep the pool available for other clients, with a consequent potential decrease in stability and increase in network traffic load. Common defaults include 12 to 24 hours, depending on the particular DHCP server being used.
		* Microsoft, for example, recommends 8 days for small networks and 16 to 24 days for larger networks. Clients begin trying to renew leases after half of the lease duration has passed.

### DHCP/BOOTP Message Fields
* Op (operation): identify as 1 request or 2 reply
* htype (HW Type): related to arp -> value 1 is ethernet
* hlen (HW Len): gives the number of bytes to hold the mac-address and is commonly 6 (ethernet)
* Hops: stores the number of relays through which the message has traveled, the sender of the message sets this value to 0, and it is incremented at each relay.
* Transaction ID: a random number chosen by the client and copied into responses by the server. It is used to match replies with requests.
* Secs: set by the client with the number of seconds that have elapsed since the first attempt to establish or renew an address.
* Flags: contains one bit, called the broadcast flag. Clients may set this bit in requests if they are unable or unwilling to process incoming unicast IP datagrams but can process incoming broadcast datagrams (e.g. because they do not yet have an IP address). Setting this bit informs the server and relays that broadcast addressing should be used for replies.
* ciaddr (Client IP Address): current IP of the requester, if known, otherwise 0.
* yiaddr (Your IP Address): Filled by server when providing an address to a requesting client.
* siaddr (Next Server IP Address): gives the IP address of the next server to use for the client’s bootstrap process (e.g., if the client needs to download an operating system image that may be accomplished from a server other than the DHCP server).
* giaddr (Gateway (or Relay) IP Address): filled in by a DHCP or BOOTP relay with its address when forwarding DHCP (BOOTP) messages.
* chaddr (Client Hardware Address): holds a unique identifier of the client and can be used in various ways by the server, including arranging for the same IP address to be given each time a particular client makes an address request. This field has traditionally held the client’s MAC address, which has been used as an identifier. Nowadays, the Client Identifier, an option described in Sections 6.2.3 and 6.2.4, is preferred for this use.
* Options (Vendor Extensions)
* sname (Server Name)
* file (Boot file name)
* **!** the last two are rarely used

### DHCP/BOOTP Options
* Given that DHCP extends BOOTP, any fields needed by DHCP that were not present when BOOTP was designed are carried as options.
* common options
	* pad (0)
	* subnet mask (1)
	* router address (3)
	* domain name server (6)
	* domain name (15)
	* requested ip address (50)
	* address lease time (51)
	* DHCP message type (53)
		* 1 byte long option, and is always used with DHCP messages
		* values
			* (1) DHCPDISCOVER
			* (2) DHCPOFFER
			* (3) DHCPREQUEST
			* (4) DHCPDECLINE
			* (5) DHCPACK
			* (6) DHCPNAK
			* (7) DHCPRELEASE
			* (8) DHCPINFORM
			* (9) DHCPFORCERENEW
			* (10) DHCPLEASEQUERY
			* (11) DHCPLEASEUNASSIGNED
			* (12) DHCPLEASEUNKNOWN
			* (13) DHCPLEASEACTIVE
	* server identifier (54)
	* parameter request list (55)
	* DHCP error message (56)
	* lease renewal time (58)
	* lease rebinding time (59)
	* client identifier (61)
	* domain search list (119)
	* End (255)

### DHCP Relays
* A DHCP relay agent extends the operation of DHCP beyond a single network segment. Information carried only between relays and DHCPv4 servers can be carried in the Relay Agent Information option.
* Note that in ordinary circumstances, a relay does not participate in all DHCP traffic exchanged between a client and a server. Rather, it relays only those messages that are broadcast. Such messages are usually exchanged when a client is obtaining its address for the first time. Once a client has acquired an IP address and the server’s IP address using the Server Identification option, it can carry out a unicast conversation with the server that does not involve the relay. Note that relay agents have traditionally been layer 3 devices and tend to incorporate routing capabilities.

### SLAAC: Stateless Address Autoconfiguration
* There are mechanisms in both IPv4 and IPv6 for link-local address autoconfiguration, whereby a host determines its address(es) largely without help. This is called stateless address autoconfiguration (SLAAC).
* a host can automatically generate its own IPv4 address from the link-local range 169.254.1.1 through 169.254.254.254 using the 16-bit subnet mask 255.255.0.0. This method is known as dynamic link-local address configuration or Automatic Private IP Addressing (APIPA).
* The utility of address autoconfiguration for IP is typically limited because routers that may be on the same network as the client are configured with particular IP address ranges in use that differ from the addresses a client is likely to autoconfigure. This is especially true for the IPv4 (APIPA) case, as the private link-local prefix 169.254/16 is very unlikely to be used by a router. Therefore, the consequence of self-assigning an IP address is that local subnet access may work, but Internet routing and name services (DNS) are likely to fail. When DNS fails, much of the common Internet “experience” fails with it. Thus, it is often more useful to have a client fail to get an IP address (which is relatively easily detected) than to allow it to obtain one that cannot really be used effectively.
* Disabling APIPA
	* `/etc/sysconfig/network`
		* `NOZEROCONF=yes`

### DHCP and DNS
* One of the important parts of the configuration information a DHCP client typically receives when obtaining an IP address is the IP address of a DNS server.
* `dnsmasq` linux package, is a DNS/DHCP combined server program that can be configured to give out IP address leases and other information but that also reads the Client Identifier or Domain Name present in a DHCPREQUEST and updates an internal DNS database with the name-to-address binding before responding with the DHCPACK.
