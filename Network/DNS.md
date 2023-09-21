### Introduction
* The protocols we have studied so far operate using IP addresses to identify the hosts that participate in a distributed application. These addresses (especially IPv6 addresses) are cumbersome for humans to use and remember, so the Internet supports the use of host names to identify hosts, both clients and servers. In order to be used by protocols such as TCP and IP, host names are converted into IP addresses using a process known as name resolution.
* There are different forms of name resolution in the Internet, but the most prevalent and important one uses a distributed database system known as the Domain Name System (DNS). DNS runs as an application on the Internet, using IPv4 or IPv6 (or both). For scalability, DNS names are hierarchical, as are the servers that support name resolution.
* DNS is a distributed client/server networked database that is used by TCP/IP applications to map between host names and IP addresses (and vice versa), to provide electronic mail routing information, service naming, and other capabilities.
* The DNS provides the protocol that allows clients and servers to communicate with each other and also a protocol for allowing servers to exchange information.
* From an application’s point of view, access to the DNS is through an application library called a **resolver**. In general, an application must convert a host name to an IP address before it can ask TCP to open a connection or send a unicast datagram using UDP. The TCP and IP protocol implementations know nothing about the DNS; they operate only with the addresses.

> [!Info] Terminology
> 1. **Name Spaces:** DNS Name Spaces are hierarchical structures used to organize domain names in the Domain Name System (DNS). They consist of different levels and categories of domain names that allow for the identification and location of resources on the internet. The name space starts with the root domain and branches into top-level domains (TLDs), subdomains, and individual hostnames. Each level in the hierarchy adds specificity to the domain name, enabling efficient and accurate translation between human-readable names and numerical IP addresses.
> 2. **DNS (Domain Name System):** A distributed hierarchical naming system used to translate human-readable domain names into numerical IP addresses.
> 3. **Domain:** A logical grouping of computers or devices on a network, represented by a unique name.  
> 4. **Hostname:** The label assigned to a specific computer or device within a domain.
> 5. **Fully Qualified Domain Name (FQDN):** A complete domain name that specifies the exact location of a resource within the DNS hierarchy, including all labels and the root domain.
> 6. **Top-Level Domain (TLD):** The highest level of the DNS hierarchy, representing the last part of a domain name (e.g., .com, .org, .net).
> 7. **Subdomain:** A domain that is part of a larger domain, indicated by a prefix to the left of the root domain.
> 8. **Root Domain:** The highest level in the DNS hierarchy, represented by a single dot (.) and serving as the base for all other domains.
> 9. **Zone:** A portion of the DNS namespace managed by a specific DNS server or set of servers.
> 10. **Name Server (NS):** A DNS server responsible for storing and providing authoritative information about a specific domain or subdomain.
> 11. **Authoritative Name Server:** An authoritative nameserver is a DNS server responsible for storing and providing official, accurate information about a specific domain or subdomain. It has the authoritative data for that domain, including IP addresses and other DNS records, and responds to DNS queries with authoritative answers.
> 12. **Resolver:** A component that performs DNS queries on behalf of client devices to translate domain names into IP addresses.
> 13. **Caching:** The process of storing DNS query responses locally to improve lookup speed and reduce network traffic.
> 14. **DNS Cache:** A temporary storage location on a device or DNS server where recent DNS query results are stored.
> 15. **Reverse DNS (rDNS):** A process that maps IP addresses to domain names, used for tasks such as identifying the source of network traffic.
> 16. **MX Record (Mail Exchange Record):** A DNS record used to specify the mail server responsible for receiving email messages for a domain.
> 17. **TTL (Time-to-Live):** A value associated with DNS records that indicates how long a cached record can be considered valid before it needs to be refreshed.
> 18. **Recursive Query:** A type of DNS query in which the resolver requests another DNS server to fully resolve the query on its behalf.
> 19. **Iterative Query:** A type of DNS query in which the resolver interacts with multiple DNS servers to resolve the query step by step.
> 20. **Domain Registrar:** An organization or company responsible for registering and managing domain names on behalf of customers.
> 21. **DNSSEC (DNS Security Extensions):** A suite of extensions to DNS that provides cryptographic authentication of DNS data, enhancing security and integrity.
> 22. **Dynamic DNS (DDNS):** A system that automatically updates DNS records when IP addresses change, enabling devices with dynamic IP addresses to be accessible using a domain name.
> 23. **Anycast:** A routing and addressing method in which multiple servers share the same IP address, with network traffic directed to the nearest server based on routing protocols.
### Namespace
* The set of all names used with DNS constitutes the DNS name space. This space is partitioned hierarchically and is case insensitive. 
* The current DNS name space is a tree of domains with an unnamed root at the top. The top echelons of the tree are the so-called *top-level domains* (TLDs), which include *generic TLDs* (gTLDs), *country-code TLDs* (ccTLDs), and *internationalized country-code TLDs* (IDN ccTLDs), plus a special infrastructure TLD called, for historical reasons, ARPA.
	* Figure 11-1: NULL ROOT:
		* **Infrastructure gTLD**: ARPA
		* **ccTLDs**: AC, AD, AE, ..., ZW
		* **Generic TLDs**: COM, ORG, NET, INFO
		* **Generic-Restricted gTLDs**: BIZ, NAME, PRO
		* **Sponsored gTLDs**: AERO, ASIA, CAT, COOP, EDU, GOV, INT, JOBS, MIL, MOBI, MUSEUM, TEL, TRAVEL, XXX
		* **IDN ccTLDs**: \[in other langs\]
		* **IDN Test Domains**: \[in other langs\]
	* The gTLDs are grouped into categories: generic, generic-restricted, and sponsored. The generic gTLDs (generic appears twice) are open for unrestricted use. The others (generic-restricted and sponsored) are limited to various sorts of uses or are constrained as to what entity may assign names from the domain.
	* Table 11-1 gives more info on gTLDs
	* The ccTLDs include the two-letter country codes specified by the ISO 3166 standard.
* The names below a TLD in the DNS name tree are further partitioned into groups known as **subdomains**. This is very common practice, especially for the ccTLDs. For example, most educational sites in England use the suffix .ac.uk, whereas names for most for-profit companies there end in the suffix .co.uk. In the United States, city government Web sites tend to use the subdomain ci.city.state.us where state is the two-letter abbreviation for the name of the state and city is the name of the city.
* The example names we have seen so far are known as **fully qualified domain names** (FQDNs). They are sometimes written more formally with a trailing period (e.g., mit.edu.). This trailing period indicates that the name is complete; no additional information should be added to the name when performing a name resolution. In contrast to the FQDN, an **unqualified domain name**, which is used in combination with a default domain or domain search list set during system configuration, has one or more strings appended to the end. When a system is configured, it is typically assigned a default domain extension and search list using DHCP. For example, the default domain cs.berkeley.edu might be configured in systems at the computer science department at UC Berkeley. If a user on one of these machines types in the name vangogh, the local resolver software converts this name to the FQDN vangogh.cs.berkeley.edu. before invoking a resolver to determine vangogh’s IP address.
* A domain name consists of a sequence of labels separated by periods. The name represents a location in the name hierarchy, where the period is the hierarchy delimiter and descending down the tree takes place from right to left in the name. For example, the FQDN `www.net.in.tum.de`, contains a host name label (`www`) in a four-level-deep domain (`net.in.tum.de`). Starting from the root, and working from right to left in the name, the TLD is `de` (the ccTLD for Germany), tum is shorthand for Technische Universität München, `in` is shorthand for informatik (German for “computer science”), and finally `net` is shorthand for the networks group within the computer science department. Each label can be up to 63 characters long, and an entire FQDN is limited to at most 255 (1-byte) characters.
* The hierarchical structure of the DNS name space allows different administrative authorities to manage different parts of the name space.
	* For example, creating a new DNS name of the form `elevator.cs.berkeley.edu` would likely require dealing with the owner of the `cs.berkeley.edu` subdomain only. The `berkeley.edu` and `edu` portions of the name space would not require alteration, so the owners of those would not need to be bothered.
	* This feature of DNS is one key aspect of its *scalability*. That is, no single entity is required to administer all the changes for the entire DNS name space.

### Name Servers and Zones
* Management responsibility for portions of the DNS name space is assigned to individuals or organizations. A person given responsibility for managing part of the active DNS name space (one or more domains) is supposed to arrange for at least two name servers or DNS servers to hold information about the name space so that users of the Internet can perform queries on the names. The collection of servers forms the DNS (service) itself, a distributed system whose primary job is to provide name-to-address mappings. However, it can also provide a wide array of additional information.
* The unit of administrative delegation, in the language of DNS servers, is called a **zone**.
	* A zone is a subtree of the DNS name space that can be administered separately from other zones. Every domain name exists within some zone, even the TLDs that exist in the *root zone*.
	* Whenever a new record is added to a zone, the DNS administrator for the zone allocates a name and additional information (usually an IP address) for the new entry and enters these into the name server’s database.
* A DNS server can contain information for more than one zone. At any hierarchical change point in a domain name (i.e., wherever a period appears), a different zone and containing server may be accessed to provide information for the name. This is called a **delegation**.
	* A common delegation approach uses a zone for implementing a second-level domain name, such as `berkeley.edu`. In this domain, there may be individual hosts (e.g., `www.berkeley.edu`) or other domains (e.g., `cs.berkeley.edu`). Each zone has a designated owner or responsible party who is given authority to manage the names, addresses, and subordinate zones within the zone. Often this person manages not only the contents of the zone but also the name servers that contain the zone’s database(s).
* Zone information is supposed to exist in at least two places, implying that there should be at least two servers containing information for each zone.
	* This is for redundancy; if one server is not functioning properly, at least one other server is available. All of these servers contain identical information about a zone. Typically, among the servers, a *primary* server contains the zone database in a disk file, and one or more *secondary* servers obtain copies of the database in its entirety from the primary using a process called a **zone transfer**. DNS has a special protocol for performing zone transfers, but copies of a zone’s contents can also be obtained using other means (e.g., the rsync utility).

### Caching
* Name servers contain information such as name-to-IP-address mappings that may be obtained from three sources. The name server obtains the information directly from the zone database, as the result of a zone transfer (e.g., for a slave server), or from another server in the course of processing a resolution. In the first case, the server is said to contain *authoritative* information about the zone and may be called an *authoritative server* for the zone. Such servers are identified by name within the zone information.
* Most name servers (except some of the root and TLD servers) also cache zone information they learn, up to a time limit called the time to live (TTL).
	* They use this cached information to answer queries.
	* Doing so can greatly decrease the amount of DNS message traffic that would otherwise be carried on the Internet. 
	* When answering a query, a server indicates whether the information it is returning has been derived from its cache or from its authoritative copy of the zone.
	* When cached information is returned, it is common for a server to also include the domain names of the name servers that can be contacted to retrieve authoritative information about the corresponding zone.
* It is worth mentioning that caching is applied both for successful resolutions and for unsuccessful resolutions (called **negative caching**). If a request for a particular domain name fails to return a record, this fact is also cached. Doing so can help to reduce Internet traffic when errant applications repeatedly make requests for names that do not exist. Negative caching was changed from optional to mandatory.
* In Linux and other systems that support it, the *Name Service Caching Daemon* (NSCD) provides a client-side caching capability. It is controlled by the `/etc/nscd.conf` file that can indicate which types of resolutions (for DNS and some other services) are cached, along with some cache parameters such as TTL settings. In addition, the file `/etc/nsswitch.conf` controls how name resolution for applications takes place. Among other things, it can control whether local files, the DNS protocol, and/or NSCD is employed for mappings.

### The DNS Protocol
* DNS has two protocols
	* A query/response protocol used for performing queries against the DNS for particular names
	* A protocol for name servers to exchange database records (zone transfers)
		* It also has a way to notify secondary servers that the zone database has evolved and a zone transfer is necessary (DNS Notify).
		* And it also has a way to dynamically update the zone (dynamic updates).
			* DNS zone dynamic update is a process that allows authorized devices to modify DNS records within a specific DNS zone without manual intervention. It enables the automatic addition, removal, or modification of DNS records, such as hostnames and IP addresses, in real-time. This feature is particularly useful for managing dynamic IP addresses or adding new resources to a network, ensuring that DNS records stay up-to-date without requiring manual changes.
* If a dns server does not know the IP address for a name, and neither does it know the IP address for a related TLD, it forwards the request to another dns server. This is called **recursion**.
	* If the second dns server (in the example in figure 11-2 it was an ISP provided dns server) also does not know the IP address, it will send a dns request to a root server.
	* The root servers are not recursive, so they do not process the request further but instead return this information required to contact a name server for the related TLD. 

#### Message Format
* There is one basic DNS format used for all operations: queries, responses, zone transfers, notifications, and dynamic updates.
* The dns message begins with a 12 byte fixed header, followed by variable-length sections: questions (or queries), answers, authority records, and additional records.
	* All but the first section contain **resource records** (RRs).
* fixed-length header
	* Transaction ID field: is set by the client and returned by the server. It let's the client match responses with requests.
	* QR (query/response): 1 bit - 0 for query, and 1 for response
	* OpCode: 4 bits - 0 for standard query, 1-3 are deprecated, 4 for notify, and 5 for update.
	* AA (authoritative answer) (as opposed to a cached answer): 1 bit
	* TC (truncated): 1 bit - With UDP, this flag being set means that the total size of the reply exceeded 12 bytes, and only the first 512 bytes of the reply were returned.
	* RD (recursion desired): 1 bit - It can be set in a query and is then returned in the response. It tells the server to perform a recursive query. If the bit is not set, and the requested name server does not have an authoritative answer, the requested name server returns a list of other name servers to contact for the answer. At this point, the overall query may be continued by contacting the list of other name servers. This is called an **iterative query**.
	* RA (recursion available): 1 bit - This bit is set in the response if the server supports recursion. Root servers generally do not support recursion, thereby forcing clients to perform iterative queries to complete name resolution.
	* Z (zero): 1 bit set to zero - reserved for future use
	* AD (authentic data): 1 bit - is set to true if the contained information is *authenticated*
	* CD (checking disabled): 1 bit - is set to true if security checking is disabled (chapter 18)
	* RCODE (response code): 4 bits - for a list of values refer to Table 11-2 (page 522). Additional types are defined using an extension (section 11.5.2).
		* A name error is returned only from an authoritative name server and means that the domain name specified in the query does not exist.
	* The next four fields are 16 bits in size and specify the number of entries in the question, answer, authority, and additional information sections that complete the DNS message.
* 11.5.1.1 Names and Labels
	* The variable-length sections at the end of a DNS message contain a collection of questions, answers, authority information (names of name servers that contain authoritative information for certain data), and additional information that may be useful to reduce the number of necessary queries. Each question and each RR begins with a ***name*** (called the domain name or owning name) to which it refers. Each name consists of a sequence of labels. ***There*** are two categories of label  types: ***data labels*** and ***compression labels***. Data labels contain characters that constitute a label; compression labels act as pointers to other labels. Compression labels help to save space in a DNS message when multiple copies of the same string of characters are present across multiple labels.

#### UDP vs TCP
* The well-known port number for DNS is 53, for both UDP and TCP.
* The most common format uses the UDP/IPv4 datagram structure.
* DNS messages are typically encapsulated in a UDP/IPv4 datagram and are limited to 512 bytes in size *unless* TCP and/or EDNS0 is used.
* When a resolver issues a query and the response comes back with the TC bit field set (“truncated”), the size of the true response exceeded 512 bytes, so only the first 512 bytes are returned by the server. The resolver may issue the request again, using TCP. This allows more than 512 bytes to be returned because TCP breaks up large messages into multiple segments.

#### Question (Query) and Zone Selection Format
* The question or query section of a DNS message lists the question(s) being referenced.
* The query (or question) section of a DNS message does not contain a TTL because it is not cached.
* Structure -> Figure 11-7 (TCP-IP Ill)
	* The Query Name is the domain name being looked up, using the encoding for labels we described before.
	* The class value (Query Class) is 1, 254, or 255, indicating the Internet class, no class, or all classes, respectively, for all cases in which we are interested (other values are not typically used for TCP/IP networks).
	* The Query Type field holds a value indicating the type of query being performed using the values from Table 11-2 (TCP-IP Ill).

#### Answer, Authority, and additional Section Formats
* RR structure -> Figure 11-8 (TCP-IP Ill)
	* The Name field (sometimes called the “owning name,” “owner,” or “record owner’s name”) is the domain name to which the following resource data corresponds.
	* The Type field specifies one of the RR type codes (see Section 11.5.6). These are the same as the query type values we described earlier.
	* The Class field is 1 for Internet data.
	* The TTL field is the number of seconds for which the RR can be cached.
	* The Resource Data Length (RDLENGTH) field specifies the number of bytes contained in the Resource Data (RDATA) field.
		* The format of this data depends on the type. For example, A records (type 1) have a 32-bit IPv4 address in the RDATA area.
* An RFC defines the term Resource Record Set (RRSet) to be a set of resource records that share the same name, class, and type but not the same data. This occurs, for example, when a host has more than one address record for its name (e.g., because it has more than one IP address). TTLs for RRs in the same RRSet must be equal.

#### Resource Record Types
##### CNAME Records
* The CNAME record stands for canonical name record and is used to introduce an alias for a single domain name into the DNS naming system.
	* For example, the name `www.berkeley.edu` may have a CNAME record that maps to some other machine (e.g., `www.w3.berkeley.edu`), so that if the Web server is located at a different computer, a relatively simple change to the DNS database may be all that is required for the rest of the world to find the new system. It is now common practice to use CNAME records to establish aliases for common services. As a result, names such as `www.berkeley.edu`, ftp.sun.com, mail.berkeley.edu, and `www.ucsd.edu` are all CNAME entries in the DNS that refer to other RRs.
* Within a CNAME RR, the RDATA section contains the “canonical name” associated with the domain name (alias).

##### Reverse DNS Queries: PTR Records
* The PTR RR type is used in response to reverse DNS queries, which are typically necessary when converting an IP address to a name. This uses the special `in-addr.arpa` domain, in a special way.

##### Authority (SOA) Records
* In DNS, each zone has an authority record, using an RR type called **start of authority** (SOA). These records provide authoritative links between portions of the DNS name space and the servers that provide the zone information allowing various queries to be performed for addresses and other information. The SOA RR is used to identify the name of the host providing the official permanent database, the responsible party’s e-mail address (where “.” is used instead of @), zone update parameters, and the default TTL. The default TTL is applied to RRs in the zone that are not otherwise assigned an explicit per-RR TTL.
* The zone update parameters include a serial number, refresh time, retry time, and expire time. The serial number is increased (by at least 1), usually by the network administrator, anytime there is a change to the zone contents. It is used by secondary servers to determine if they should initiate a zone transfer (when they do not have a copy of the zone contents with largest serial number). The refresh time tells secondary servers how long to wait before checking the SOA record from the primary and its version number to determine if a zone transfer is required. The retry and expire times are used in the case of zone transfer failure. The retry value gives the time (in seconds) a secondary will wait before retrying. The expire time is an upper bound (in seconds) that a secondary server will keep retrying zone transfers before giving up. If it gives up, such a server ceases to respond to queries for the zone. In general, a zone can contain a mix of IPv4 and IPv6 data and can be accessed using either version of IP.

#### DNS UPDATE
* It is possible to dynamically update a zone, called DNS UPDATE. It supports the ability to specify prerequisites in conjunction with an update request. Prerequisites are evaluated at the server; if they are not true, the update is not performed and an error message is returned.
* DNS UPDATE is accomplished by sending dynamic update DNS messages to an authoritative DNS server for a zone. The structure of such messages is the same as for a conventional DNS message, except the header fields and sections have different names (see Figure 11-3). The sections indicate the zone being updated, prerequisites that require various RRs to be present (or not) for the update to take effect, and the *update information*. In an update, the header mirrors the format for a query, but the Opcode field is set to Update (5). The header fields ZOCOUNT, PRCOUNT, UPCOUNT, and ADCOUNT contain counts of the following: zones to be updated (this will have the value 1), prerequisites to consider, updates to be made, and additional information records, respectively.
* The zone section of an update message (see Figure 11-7) indicates the zone’s name, a type, and a class. The type value will be 6 to indicate the presence of an SOA record, which identifies the zone. The class value will be 1 (Internet) for any update message with which we are concerned. All records being updated must be in the same zone.
* The prerequisite section of an update message contains one or more prerequisites, expressed using the format for RRs we discussed previously in Section 11.5.5. There are five types of prerequisites: *RRSet exists* (value-dependent and value-independent varieties), *RRSet does not exist*, *name is in use*, and *name is not in use*. Recall that an RRSet is a group of RRs from the same zone sharing a common name, class, and type. To express the semantics of a prerequisite, a combination of an RR’s class, type, and RDATA values are set according to Table 11-5 (lookup `rr-class-and-type-fields-in-prerequisite-section-table`).
* The *RRSet exists* type means that at least one RRSet exists in the zone specified in the zone section that matches the name and type of the corresponding RR in the prerequisite section. In the value-dependent case, the prerequisite is true only if the matching RRs also contain matching RDATA values. *The RRSet does not exist* type means that no RRSet in the zone specified in the zone section matches the name and type of the RR in the Prerequisites section. The last two cases (*Name is in use* and *Name is not in use*) refer only to the domain name; the type value is not used. The values for NONE and ANY as DNS classes are 254 and 255, respectively.
* Following the Prerequisite section, the Update section contains RRs to be added or deleted from the zone specified in the zone section. There are four types of updates, encoded as an RR with various combinations of values in the Class, Type, and RDATA fields, as indicated in Table 11-6 (lookup `rr-class-and-type-fields-in-update-section-table`).
* you can use `nsupdate` on linux

> rr-class-and-type-fields-in-prerequisite-section-table

| prerequisite type (semantics) | class setting | type setting | RData setting |
| :- | :- | :- | :- |
| RRSet exists (value-independent) | ANY | same as zone's type | Empty |
| RRSet exists (value-dependent) | same as zone's class | type being checked | RRSet being checked |
| RRSet does not exist | NONE | type being checked | Empty |
| name is in use | ANY | ANY | Empty |
| name is not in use | NONE | ANY | Empty |

> rr-class-and-type-fields-in-update-section-table

| use | class setting | type setting | RData |
| :- | :- | :- | :- |
| add RR to RRSet | same as zone's class | type of RR being added | RData of RR being added |
| delete RRSet | ANY | type of RRSet to delete | Empty (TTL and RDLENGTH also zero) |
| delete all RRSets from a name | ANY | ANY | Empty (TTL and RDLENGTH also zero) |
| delete RR from RRSet | NONE | type of RR being deleted | matching RData to delete |

### Zone Transfers and DNS NOTIFY
* A zone transfer is used to copy a set of RRs for a zone from one server to another (generally from the master server to slave servers). 
	* The purpose of doing so is to keep multiple servers in sync with respect to a zone’s contents.
	* Multiple servers provide resiliency to failure, in case a server should go down.
	* Performance can also be improved as multiple servers can be used to share the processing load for incoming queries.
	* Finally, the latency of a DNS query/response can potentially be reduced if servers are placed in locations close to clients (i.e., where the network latency between resolver and server is small).
* As originally specified, zone transfers are initiated after polling, where slaves periodically contact masters to see if a zone transfer is necessary by comparing the zones’ version numbers. A later method says if a zone transfer needs to be initiated using an asynchronous update mechanism when the zone contents change. This is called *DNS NOTIFY*. Once a zone transfer is initiated, either the entire zone is transferred (using DNS AXFR messages), or an *incremental zone transfer* option may be used (using DNS IXFR messages). The general scheme operates according to the illustration in Figure 11-18 (TCP-IP Ill).
* 11.5.8.1 Full Zone Transfers (AXFR Messages)
	* Full zone transfers are controlled by the zone transfer parameters carried in a zone’s SOA record: *primary name server*, *serial number*, and the *refresh*, *retry*, and *expire* intervals.
	* When configured, a slave server attempts to contact the primary server to see if a zone transfer is necessary.
	* Contacts are attempted periodically, according to the refresh interval.
		* They are also attempted when a server first starts.
		* If a contact is not successful (no response from the server), retries are attempted periodically according to the retry interval (generally shorter than the refresh interval).
		* The entire zone contents are flushed if not refreshed within the expire interval, effectively incapacitating the server for the zone.
	* An All Zone Transfer (AXFR) DNS message (a standard query containing type AXFR in the Question section) is used to request a complete zone transfer using TCP.
		* refer to page 560 (TCP-IP Ill) for examples
		* Although it used to be possible to perform such zone transfers with virtually any DNS server, they are now typically restricted to the authoritative servers in a zone (e.g., those listed in NS records for the zone). The reason for this restriction is privacy and security—knowledge of the hosts within the zone might help an attacker target particular services or hosts.
* 11.5.8.2 Incremental Zone Transfers (IXFR Messages)
	* To improve the efficiency of zone transfers, an RFC defines the use of incremental zone transfers. Using incremental zone transfers and the IXFR message type, only the changes in a zone are provided. To execute an incremental zone transfer, the client (e.g., slave server) must provide its current serial number for the zone.
	* refer to page 562 (TCP-IP Ill) for examples
* 11.5.8.3 DNS NOTIFY
	* As mentioned previously, polling has traditionally been used to determine the need for zone transfers, meaning that the slave servers would check with a master periodically (the “refresh” interval) to see if the zone had been updated (indicated by a different serial number), in which case a zone transfer would be initiated. This is a somewhat wasteful process because many useless polls may occur before the zone is updated. To improve the situation, an RFC developed the DNS NOTIFY mechanism. DNS NOTIFY allows a server with modified zone contents to notify slave servers that an update has been made and a zone transfer should be initiated. More specifically, if enabled, a notification message is sent to a set of interested servers if the SOA RR for a zone changes (e.g., if the serial number increases). This allows zone transfers to be initiated easily when required.
	* refer to page 564 (TCP-IP Ill) for examples

### OpenDNS
* Many home users are assigned a single IPv4 address by their ISP, and this address may change over time as the user’s computer or home gateway connects, disconnects, and reconnects to the Internet. Consequently, it is often difficult for the user to establish a DNS entry that allows for running services that are visible from the Internet.
* A number of so-called open Dynamic DNS (DDNS) servers are available that support a special update protocol called the DNS Update API \[DYNDNS\], whereby a user may update an entry in a provider’s DNS server given a preregistration or account. This scheme does not use the DNS UPDATE protocol described earlier but is instead a separate application-layer protocol.
* To use the service, a DDNS client program (e.g., inadyn or ddclient on Linux) runs on the client system, which could also be a user’s home router. Most often, these programs are configured with login information used to access a remote DDNS service. When the service is invoked, the client program contacts the server, provides the current global IP address of its host (the one assigned by an ISP, often a NAT mapped address), and goes quiescent. After that, it periodically renews the information with the server. Doing so allows the server to clear the information if an update is not received within a certain time interval.

### DNSSEC
* The extensions provide origin authentication and integrity assurance for DNS data, along with a (limited) key distribution facility. **That is, the extensions provide a cryptographically secure way to determine what entity has authored a block of DNS information and that the information has been received unaltered.** DNSSEC also provides *authenticated nonexistence*. DNS responses indicating the nonexistence of a particular domain name include protection similar to that of responses for existing domain names. DNSSEC does not provide privacy (confidentiality) of DNS information, DoS protection, or access control. Transaction security, used with DNSSEC, is defined separately.
* DNSSEC accommodates resolvers with varying levels of security “awareness.” A *validating security-aware resolver* (also called *validating resolver*) checks cryptographic signatures to ensure that the DNS data it handles is secure. Other resolvers, including stub resolvers on hosts and the “resolver side” of recursive name servers, may be security-aware but may not perform cryptographic validation. Instead, such resolvers should establish secure associations with validating resolvers. We shall focus on the validating resolvers, as they are the most sophisticated and interesting. When operating, they are able to ascertain whether DNS information is secure (valid with all signatures checked), insecure (valid signatures indicate that something should not be present but is), bogus (proper data appears to be present but cannot be validated for some reason), or indeterminate (veracity cannot be determined, usually because of lack of signatures). The indeterminate case is the default case when no other information is available.
* DNSSEC works securely only when a zone is signed by a domain administrator, there is some basis for trust, and both server and resolver software participate. Validating resolvers check signatures to ensure that DNS information is secure, and they must be configured with one or more initial trust anchors that are similar to root certificates in a PKI. Note, however, that DNSSEC is not a PKI; in particular, it provides only limited signing and key revocation. It does not implement an analog to certificate revocation lists.
* When performing a DNS query with DNSSEC, a security-aware resolver uses EDNS0 and enables the DO (DNSSEC OK) bit in an OPT meta-RR present in the request. This bit indicates the client’s interest in and ability to process DNSSEC-related information along with its support for EDNS0. The DO bit is896 Security: EAP, IPsec, TLS, DNSSEC, and DKIM the first (high-order) bit of the second 16-bit field in the “extended RCODE and flags” portion of the EDNS0 meta-RR. Servers that receive requests in which the DO bit is not set (or present) are prohibited from returning most of the RRs discussed in Section 18.10.1 unless such records are explicitly asked for in the request. This helps to improve DNS performance because it avoids having to carry security-related RRs that are never processed by security-unaware resolvers. This can be especially beneficial because DNS typically uses relatively small UDP packets and falls back to using TCP, which increases latency due to its three-way handshake, for large responses.
* When a server processes a request from a DNSSEC-enabled resolver, it checks the CD (checking disabled) bit in the DNS request (see Chapter 11). If set, this indicates that the client is willing to accept nonvalidated data in a response. When preparing a response, a server ordinarily validates the data it is returning cryptographically. Successful validation results in the AD (authentic data) bit being set in the response. A security-aware but nonvalidating resolver can in principle trust this information if it has a secure path to the server. However, the arguably best case is to use validating stub resolvers that perform cryptographic validation and consequently set the CD bit on queries. This provides end-to-end security of the DNS (i.e., an intermediate resolver need not be trusted), and it reduces the computational load on the intermediate servers that would otherwise have to perform cryptographic validation.
