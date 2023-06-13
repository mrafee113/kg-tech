### ARP Cache
* Essential to the efficient operation of ARP is the maintenance of an ARP cache (or table) on each host and router. This cache maintains the recent mappings from network-layer addresses to hardware addresses for each interface that uses address resolution.
* the normal expiration time of a arp cache entry is 20 minutes from the time of creation.
* [[Network/ARP#^arp-a|ARP]]

#### Cache Timeout
* most implementations have a timeout of 20 minutes for a completed entry and 3 minutes for an incomplete entry
* some RFC suggests that entries should be expired even if they're in use, but most implementations refresh the timeout when the entry is referenced. This is due to soft state.
* Soft state is information that is discarded if not refreshed before some timeout is reached. Many Internet protocols use soft state because it helps to initiate automatic reconfiguration if network conditions change. The cost of soft state is that some protocol must refresh the state to avoid expiration. “Soft state refreshes” are often incorporated in a protocol design to keep the soft state active.

### Gratauitious ARP
* It is sending arp that targets the sender's own IP address.
* **Goal 1**: find out if any other host is using this IP address.
* **Goal 2**: If sender's MAC address has been changed, this will help reconfigure the arp cache entries on other hosts.

### ARP Command
* `arp -s` is used to manually add entries
* `arp -a` examines arp cache on linux ^arp-a
	* flags
		* C: learned dynamically by arp
		* M: entered by hand
		* P: (publish) the host responds to incoming arp requests
* #todo `man arp`
