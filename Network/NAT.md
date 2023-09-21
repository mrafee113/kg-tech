* NAT is essentially a mechanism for allowing the same sets of IP addresses to be reused in different parts of the Internet.
* NAT was introduced to solve two problems: address depletion and concerns regarding the scalability of routing.
* Routing scalability was being tackled with the development of Classless Inter-Domain Routing (CIDR; see Chapter 2).
* NAT is popular because it reduces the need for globally routable Internet addresses but also because it offers some degree of natural firewall capability and requires little configuration.
* Despite its popularity, NAT has several drawbacks.
	* The most obvious is that offering Internet-accessible services from the private side of a NAT requires special configuration because privately addressed systems are not directly reachable from the Internet.
	* In addition, for a NAT to work properly, every packet in both directions of a connection or association must pass through the same NAT. This is because the NAT must actively rewrite the addressing information in each packet in order for communication between a privately addressed system and a conventionally addressed Internet host to work.
* NAT poses problems for some application protocols, especially those that send IP addressing information inside the application-layer payload. FTP and SIP are among the best-known protocols of this type. They require a special application-layer gateway function that rewrites the application content in order to work unmodified with NAT or other NAT traversal methods that allow the applications to determine how to work with the specific NAT they are using. A more complete list of considerations regarding NAT appears in. Despite their numerous problems, NATs are very widely used, and most network routers (including essentially all low-end home routers) support it. Today, NATs are so prevalent that application designers are encouraged to make their applications “NAT-friendly”. It is worth mentioning that despite its shortcomings, NAT supports the basic protocols (e.g., e-mail, Web browsing) that are needed by millions of client systems accessing the Internet every day.
* A NAT works by rewriting the identifying information in packets transiting through a router. Most commonly this happens for two directions of a data transfer. In its most basic form, NAT involves rewriting the source IP address of packets as they are forwarded in one direction and the destination IP addresses of packets traveling in the reverse direction. This allows the source IP address in outgoing packets to become one of the NAT router’s Internet-facing interfaces instead of the originating host’s. Thus, to a host on the Internet, packets coming from any of the hosts on the privately addressed side of the NAT appear to be coming from a globally routable IP address of the NAT router.
* The so-called traditional NAT includes both basic NAT and Network Address Port Translation (NAPT).
	* Basic NAT performs rewriting of IP addresses only. In essence, a private address is rewritten to be a public address, often from a pool or range of public addresses supplied by an ISP. This type of NAT is not the most popular because it does not help to dramatically reduce the need for IP addresses—the number of globally routable addresses must equal or exceed the number of internal hosts that wish to access the Internet simultaneously.
	* A much more popular approach, NAPT involves using the transport-layer identifiers (i.e., ports for TCP and UDP, query identifiers for ICMP) to differentiate which host on the private side of the NAT is associated with a particular packet. This allows a large number of internal hosts (i.e., multiple thousands) to access the Internet simultaneously using a limited number of public addresses, often only a single one. We shall ordinarily use the term NAT to include both traditional NAT and NAPT unless the distinction is important in a particular context.
* The addresses used in a private addressing realm “behind” or “inside” a NAT are not enforced by anyone other than the local network administrator. Thus, it is possible for a private realm to make use of global address space. In principle, this is acceptable. However, when such global addresses are owned and being used by another entity on the Internet, local systems in the private realm would most likely be unable to reach the public systems using the same addresses because the close proximity of the local systems would effectively “mask” the visibility of the farther-away systems using the same addresses. To avoid this undesirable situation, there are three IPv4 address ranges reserved for use with private addressing realms: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. These address ranges are often used as default values for address pools in embedded DHCP servers.
* NAT and TCP (page 306): in addition to forwarding the packet, the NAT creates a internal state to remember the fact that a new connection is being handled by the NAT (called a NAT session). At a minimum, this state includes an entry (called a NAT mapping) containing the source IP address and source port of the client.
* in general, fragments cannot be handled properly by simple NATs or NAPTs.
* 7.3.2 Address and Port Translation Behavior: (page 311) Figure 7-5 and table 7-1 are very important.
* 7.3.3 Filtering Behavior (page 313)

> [!Question] ChatGPT
> **What's the benefit of Port Address Translation (or Nat overloading)?**
>
> Port Address Translation (PAT), also known as Network Address Translation (NAT) Overloading, is a technique used in networking to map multiple private IP addresses to a single public IP address by using different ports. PAT is a more advanced form of NAT and provides several benefits:
>
> 1. **Conservation of Public IP Addresses:**
   PAT allows multiple devices within a private network to share a single public IP address. This is especially valuable as the number of available public IPv4 addresses is limited, and many organizations have more internal devices than available public addresses.
>
> 2. **Security and Privacy:**
   By using PAT, internal devices are hidden behind a single public IP address. This provides a level of security by obscuring the individual addresses of devices within the network, making them less vulnerable to external attacks.
>
> 3. **Load Balancing:**
   PAT can be used to distribute incoming traffic across multiple internal servers. When external clients connect to the public IP address, the NAT router can forward the traffic to different internal servers based on the destination port number.
>
> 4. **Simpler Configuration:**
   PAT allows multiple devices to share the same public IP address without requiring extensive manual configuration. This simplifies network management and reduces the need for large ranges of public IP addresses.
>
> 5. **Connection Tracking:**
   PAT routers keep track of the translation between internal private IP addresses and the single public IP address, along with the port numbers. This connection tracking helps ensure that responses from external servers are correctly routed back to the appropriate internal devices.
>
> 6. **Protocol Support:**
   PAT works with various protocols, including TCP, UDP, and ICMP. This allows for a wide range of applications to be used within the private network.
>
> 7. **Multiple Services on a Single IP:**
   With PAT, a single public IP address can be used to provide multiple services, each mapped to a different port number on the public IP address. This is useful for hosting different services (such as web, email, FTP) on the same external IP.
>
> 8. **IP Address Space Separation:**
   PAT allows organizations to use private IP address ranges within their internal networks, which don't need to be globally unique. This separation between internal and external IP address spaces aids in network design and reduces the risk of IP address conflicts.

> [!Question] ChatGPT
> **What devices do organizations use to provide NAT and NAT overloading for their internal private IP addresses?**
>
> Organizations typically use network devices like routers, firewalls, and dedicated Network Address Translation (NAT) devices to provide NAT and NAT Overloading (also known as Port Address Translation or PAT) for their internal private IP addresses. These devices play a key role in managing the translation of private IP addresses to a single public IP address, allowing internal devices to communicate with the external Internet. Here are some common devices used for NAT and NAT Overloading:
>
> 1. **Residential and Small Business Routers:** Consumer-grade routers often include NAT capabilities by default. They are commonly used in homes and small offices to allow multiple devices to share a single public IP address. These routers usually offer basic NAT and PAT functionalities.
>    
> 2. **Enterprise Routers:** Larger organizations use enterprise-grade routers that provide advanced NAT and PAT capabilities. These routers are capable of handling higher traffic volumes, more complex rule configurations, and advanced security features.
>    
> 3. **Firewalls:** Firewalls are security devices that often include NAT and PAT functionality as part of their features. Firewalls provide a layer of protection by controlling the flow of traffic between internal and external networks, making them an ideal location for implementing NAT and PAT.
>    
> 4. **Load Balancers:** Load balancers can use NAT and PAT to distribute incoming  traffic to multiple internal servers based on the destination port number. This is useful for ensuring efficient distribution of client requests to backend servers.
>    
> 5. **Proxy Servers:** Proxy servers can perform NAT and PAT as part of their functionality. They act as intermediaries between clients and servers, helping to improve security, performance, and caching for web requests.
>    
> 6. **NAT Gateways:** Some organizations deploy dedicated NAT gateways that are specifically designed to handle NAT and PAT tasks. These devices offer specialized features for translating and routing traffic between internal and external networks.
>    
> 7. **Network Appliances:** Organizations might deploy network appliances that are purpose-built for NAT and PAT. These appliances can provide enhanced performance, scalability, and management features tailored to address NAT-related challenges.
>    
> 8. **Virtual Appliances:** Virtual machines or virtual appliances can also be used to provide NAT and PAT services in virtualized environments. These can be integrated into virtual network configurations to manage traffic between virtual machines and external networks.
>    
> 9. **Software Solutions:** Some organizations use software-based NAT and PAT solutions that run on standard server hardware. These solutions can be cost-effective and offer flexibility for custom configurations.

