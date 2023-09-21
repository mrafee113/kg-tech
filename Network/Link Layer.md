### Loopback
Although it may seem surprising, in many cases clients may wish to communicate with servers on the same computer using Internet protocols such as TCP/IP. To enable this, most implementations support a network-layer loopback capability that typically takes the form of a virtual loopback network interface. It acts like a real network interface but is really a special piece of software provided by the operating system to enable TCP/IP and other communications on the same host computer.

### Common Tunneling Methods
* Generic Routing Encapsulation (GRE)
	* was developed to replace IP-in-IP tunneling
	* not necessarily encrypted
	* usually used between ISPs or in an intranet
* microsoft proprietary Point-to-Point Tunneling Protocol (PPTP)
	* essentially is (=) PPP+GRE
	* most often used between users and their ISPs
	* is often encrypted (e.g. using MPPE)
* Layer 2 Tunneling Protocol (L2TP)
	* was developed to replace PPTP