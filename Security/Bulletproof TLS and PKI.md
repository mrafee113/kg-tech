> [source](https://www.feistyduck.com/books/bulletproof-tls-and-pki/)

## Chapter 1: SSL, TLS, and Cryptography
> `pg: 23`

* All the devices connected to the Internet have one thing in common—they rely on the protocols called SSL (Secure Socket Layer) and TLS (Transport Layer Security) to protect the information in transit.
* SSL and TLS are cryptographic protocols designed to provide secure communication over insecure infrastructure. What this means is that, if these protocols are properly deployed, you can open a communication channel to an arbitrary service on the Internet, be reasonably sure that you’re talking to the correct server, and exchange information safe in knowing that your data won’t fall into someone else’s hands and that it will be received intact. These protocols protect the communication link or transport layer, which is where the name TLS comes from.
* TLS has four main goals, listed here in the order of priority:
	* **Cryptographic security**: Enable secure communication between any two parties who wish to exchange information.
	* **Interoperability**: Independent programmers should be able to develop programs and libraries that are able to communicate with one another using common cryptographic parameters.
	* **Extensibility**: TLS is effectively a framework for the development and deployment of cryptographic protocols. Its important goal is to be independent of the actual cryptographic primitives (e.g., ciphers and hashing functions) used, allowing migration from one primitive to another without needing to create new protocols.
	* **Efficiency**: The final goal is to achieve all of the previous goals at an acceptable performance cost, reducing costly cryptographic operations down to the minimum and providing a session caching scheme to avoid them on subsequent connections.
* Arranging communication in the OSI way provides clean separation of concerns; protocols don’t need to worry about the functionality implemented by lower layers. Further, protocols at different layers can be added and removed; a protocol at a lower layer can be used for many protocols from higher levels. SSL and TLS (Presentation Layer) are a great example of how this principle works in practice. They sit above TCP but below higher-level protocols such as HTTP. When encryption is not necessary, we can remove TLS from our model, but that doesn’t affect the higher-level protocols, which continue to work directly with TCP. When you do want encryption, you can use it to encrypt HTTP, but also any other TCP protocol, for example SMTP, IMAP and so on.

### Cryptography
* Cryptography is the science and art of secure communication.
* When cryptography is correctly deployed, it addresses the three core requirements of security: keeping secrets (**confidentiality**), verifying identities (**authenticity**), and ensuring safe transport (**integrity**).

> [!Note]
> If you want to spend more time learning about cryptography, there’s plenty of good literature available. My favorite book on this topic is ***Understanding Cryptography***, written by Christof Paar and Jan Pelzl and published by Springer in 2010.

#### Building Blocks
* At the lowest level, cryptography relies on various cryptographic primitives. Each primitive is designed with a particular useful functionality in mind.
* For example, we might use one primitive for encryption and another for integrity checking.
* The primitives alone are not very useful, but we can combine them into schemes and protocols to provide robust security.

##### Symmetric Encryption
* Symmetric encryption (or *private-key cryptography*) is a method for obfuscation (the action of making something obscure and unintelligible) that enables secure transport of data over insecure communication channels.
* To communicate securely,
	* Alice and Bob first agree on the encryption algorithm and a secret key.
	* Later on, when Alice wants to send some data to Bob, she uses the secret key to encrypt the data.
	* Bob uses the same key to decrypt it.
	* Eve, who has access to the communication channel and can see the encrypted data, doesn’t have the key and thus can’t access the original data.
	* Alice and Bob can continue to communicate securely for as long as they keep the secret key safe.

> [!Note]
> Three terms are commonly used when discussing encryption: **plaintext** is the data in its original form, **cipher** is the algorithm used for encryption, and **ciphertext** is the data after encryption.

* **Auguste Kerckhoffs**: A cryptosystem should be secure even if the attacker knows everything about the system, except the secret key. Although it might seem strange at first, Kerckhoffs’s principle—as it has come to be known—makes sense if you consider the following:
	* For an encryption algorithm to be useful, it must be shared with others. As the number of people with access to the algorithm increases, the likelihood that the algorithm will fall into the enemy’s hands increases too.
	* A single algorithm without a key is very inconvenient to use in large groups; everyone can decrypt everyone’s communication.
	* It’s very difficult to design good encryption algorithms. The more exposure and scrutiny an algorithm gets, the more secure it can be. Cryptographers recommend a conser- vative approach when adopting new algorithms; it usually takes years of breaking at- tempts until a cipher is considered secure.
* Ciphers can be divided into two groups: stream and block ciphers.

###### Stream Ciphers
* Conceptually, stream ciphers operate in a way that matches how we tend to imagine encryption. You feed one byte of plaintext to the encryption algorithm, and out comes one byte of ciphertext. The reverse happens at the other end. The process is repeated for as long as there is data to process.
* An encryption process is considered secure if the attacker can’t predict which keystream bytes are at which positions.
	* For this reason, it is vital that stream ciphers are never used with the same key more than once.
	* This is because, in practice, attackers know or can predict plaintext at certain locations (think of HTTP requests being encrypted; things such as request method, protocol version, and header names are the same across many requests).
	* When you know the plaintext and can observe the corresponding ciphertext, you uncover parts of the keystream. You can use that information to uncover the same parts of future ciphertexts if the same key is used.
	* To work around this problem, stream algorithms are used with one-time keys derived from long-term keys.

###### Block Ciphers
* Block ciphers encrypt entire blocks of data at a time; modern block ciphers tend to use a block size of 128 bits (16 bytes).
	* A block cipher is a transformation function: it takes some input and produces seemingly random output from it.
	* For every possible input combination, there is exactly one output, as long as the key stays the same.
	* A key property of block ciphers is that a small variation in input (e.g., a change of one bit anywhere) produces a large variation in output.
* On their own, block ciphers are not very useful because of several limitations.
	* First, you can only use them to encrypt data lengths equal to the size of the encryption block. To use a block cipher in practice, you need a scheme to handle data of arbitrary length.
	* Another problem is that block ciphers are *deterministic*; they always produce the same output for the same input. This property opens up a number of attacks and needs to be dealt with.
* In practice, block ciphers are used via encryption schemes called block cipher modes, which smooth over the limitations and sometimes add authentication to the mix. Block ciphers can also be used as the basis for other cryptographic primitives, such as hash functions, message authentication codes, pseudorandom generators, and even stream ciphers.
* The world’s most popular block cipher is **AES** (short for Advanced Encryption Standard), which is available in strengths of 128, 192, and 256 bits.

##### Hash Functions
* A hash function is an algorithm that converts input of arbitrary length into fixed-size output. The result of a hash function is often called simply a hash.
* Hash functions are commonly used in programming, but not all hash functions are suitable for use in cryptography.
* Cryptographic hash functions are hash functions that have several additional properties:
	* **Preimage resistance**: Given a hash, it’s computationally unfeasible to find or construct a message that produces it.
	* **Second preimage resistance**: Given a message and its hash, it’s computationally unfeasible to find a different message with the same hash.
	* **Collision resistance**: It’s computationally unfeasible to find two messages that have the same hash.
* Unlike with ciphers, the strength of a hash function doesn’t equal the hash length. Because of the birthday paradox (a well-known problem in probability theory), the strength of a hash function is at most one half of the hash length.
* A hash function could be used to verify data integrity, but only if the hash of the data is transported separately from the data itself. Otherwise, an attacker could modify both the message and the hash, easily avoiding detection.

##### Message Authentication Codes
* A message authentication code (MAC) or a keyed-hash is a cryptographic function that extends hashing with authentication. Only those in possession of the hashing key can produce a valid MAC.
* MACs are commonly used in combination with encryption.
	* Even though Mallory can’t decrypt ciphertext, she can modify it in transit if there is no MAC; encryption provides confidentiality but not integrity.
	* If Mallory is smart about how she’s modifying ciphertext, she could trick Bob into accepting a forged message as authentic.
	* When a MAC is sent along with ciphertext, Bob (who shares the hashing key with Alice) can be sure that the message has not been tampered with.
* Any hash function can be used as the basis for a MAC using a construction known as HMAC (short for hash-based message authentication code).
	* In essence, HMAC works by interleaving the hashing key with the message in a secure way.

##### Block Cipher Modes
* Block cipher modes are cryptographic schemes designed to extend block ciphers to encrypt data of arbitrary length.
* All block cipher modes support confidentiality, but some combine it with authentication.
* Some modes transform block ciphers to produce stream ciphers.

##### Asymmetric Encryption
* Symmetric encryption does a great job at handling large amounts of data at great speeds, but it leaves a lot to be desired as soon as the number of parties involved increases:
	* Members of the same group must share the same key. The more people join a group, the more exposed the group becomes to the key compromise.
	* For better security, you could use a different key for every two people, but this approach doesn’t scale. Although three people need only three keys, ten people would need 45 (9 + 8 + . . . + 1) keys. A thousand people would need 499,500 keys!
	* Symmetric encryption can’t be used on unattended systems to secure data. Because the process can be reversed by using the same key, a compromise of such a system leads to the compromise of all data stored in the system.
* Asymmetric encryption (also known as public-key cryptography) is a different approach to encryption that uses two keys instead of one.
	* One of the keys is private; the other is public.
	* There’s a special mathematical relationship between these keys that enables some useful features.
	* If you encrypt data using someone’s public key, only their corresponding private key can decrypt it.
	* On the other hand, if data is encrypted with the private key anyone can use the public key to unlock the message.
	* The latter operation doesn’t provide confidentiality, but it does function as a digital signature.
	* Asymmetric encryption makes secure communication in large groups much easier. Assuming that you can securely share your public key widely (a job for PKI), anyone can send you a message that only you can read. If they also sign that message using their private key, you know exactly whom it is from.
* Despite its interesting properties, public-key cryptography is rather slow and unsuitable for use with large quantities of data. For this reason, it’s usually deployed for authentication and negotiation of shared secrets, which are then used for fast symmetric encryption.
* RSA is by far the most popular asymmetric encryption method deployed today. The recommended strength for RSA today is 2,048 bits, which is equivalent to about 112 symmetric bits.

##### Digital Signatures
* A digital signature is a cryptographic scheme that makes it possible to verify the authenticity of a digital message or document.
* The MAC is a type of digital signature; it can be used to verify authenticity provided that the secret hashing key is securely exchanged ahead of time.
	* Although this type of verification is very useful, it’s limited because it still relies on a private secret key.
* Digital signatures similar to the real-life handwritten ones are possible with the help of public-key cryptography; we can exploit its asymmetric nature to devise an algorithm that allows a message signed by a private key to be verified with the corresponding public key.
	* The exact approach depends on the selected public-key cryptosystem.
	* For example, RSA can be used for encryption and decryption. If something is encrypted with a private RSA key, only the corresponding public key can decrypt it.
	* We can use this property for digital signing if we combine it with hash functions:
		1. Calculate a hash of the document you wish to sign; no matter the size of the input document, the output will always be fixed, for example, 256 bits for SHA256.
		2. Encode the resulting hash and some additional metadata. For example, the receiver will need to know the hashing algorithm you used before she can process the signature.
		3. Encrypt the encoded hash using the private key; the result will be the signature, which you can append to the document as proof of authenticity.
	* To verify the signature, the receiver takes the document and calculates the hash independently using the same algorithm.
		* Then, she uses your public key to decrypt the message and recover the hash, confirm that the correct algorithms were used, and compare with the decrypted hash with the one she calculated.
		* The strength of this signature scheme depends on the individual strengths of the encryption, hashing, and encoding components.

> [!Note]
> Not all digital signature algorithms function in the same way as RSA. In fact, RSA is an exception, because it can be used for both encryption and digital signing. Other popular public key algorithms, such as DSA and ECDSA, can’t be used for encryption and rely on different approaches for signing.

##### Random Number Generation
* In cryptography, all security depends on the quality of random number generation.
* The problem with random numbers is that computers tend to be very predictable.
	* They follow instructions to the letter.
	* If you tell them to generate a random number, they probably won’t do a very good job.
	* This is because truly random numbers can be obtained only by observing certain physical processes. In absence of that, computers focus on collecting small amounts of entropy. This usually means monitoring keystrokes and mouse movement and the interaction with various peripheral devices, such as hard disks.
	* Entropy collected in this way is a type of true random number generator (TRNG), but the approach is not reliable enough to use directly.
		* For example, you might need to generate a 4,096-bit key, but the system might have only a couple of hundreds of bits of entropy available. If there are no reliable external events to collect enough entropy, the system might stall.
* For this reason, in practice we rely on pseudorandom number generators (PRNGs), which use small amounts of true random data to get them going.
	* This process is known as seeding.
	* From the seed, PRNGs produce unlimited amounts of pseudorandom data on demand.
	* General-purpose PRNGs are often used in programming, but they are not appropriate for cryptography, even if their output is statistically seemingly random.
* Cryptographic pseudo-random number generators (CPRNGs) are PRNGs that are also unpredictable.
	* This attribute is crucial for security; an adversary mustn’t be able to reverse-engineer the internal state of a CPRNG by observing its output.

#### Protocols
* Cryptographic primitives such as encryption and hashing algorithms are seldom useful by themselves.
* We combine them into schemes and protocols so that we can satisfy complex security requirements.
* To illustrate how we might do that, let’s consider a simplistic cryptographic protocol that allows Alice and Bob to communicate securely. We’ll aim for all three main requirements: **confidentiality**, **integrity**, and **authentication**.
	* Let’s assume that our protocol allows exchange of an arbitrary number of messages. Because symmetric encryption is very good at encrypting bulk data, we might select our favorite algorithm to use for this purpose, say, AES.
		* With AES, Alice and Bob can exchange secure messages, and Mallory won’t be able to recover the contents. But that’s not quite enough, because Mallory can do other things, for example, modify the messages without being detected.
		* To fix this problem, we can calculate a MAC of each message using a hashing key known only to Alice and Bob. When we send a message, we send along the MAC as well.
		* Now, Mallory can’t modify the messages any longer. However, she could still drop or replay arbitrary messages.
		* To deal with this, we extend our protocol to assign a sequence number to each message; crucially, we make the sequences part of the MAC calculation.
			* If we see a gap in the sequence numbers, then we know that there’s a message missing.
			* If we see a sequence number duplicate, we detect a replay attack.
		* For best results, we should also use a special message to mark the end of the conversation. Without such a message, Mallory would be able to end (truncate) the conversation undetected.
		* With all of these measures in place, the best Mallory can do is prevent Alice and Bob from talking to one another. There’s nothing we can do about that.
		* So far, so good, but we’re still missing a big piece: how are Alice and Bob going to negotiate the two needed keys (one for encryption and the other for integrity validation) in the presence of Mallory? We can solve this problem by adding two additional steps to the protocol.
		* First, we use public-key cryptography to authenticate each party at the beginning of the conversation. For example, Alice could generate a random number and ask Bob to sign it to prove that it’s really him. Bob could ask Alice to do the same.
		* With authentication out of the way, we can use a key-exchange scheme to negotiate encryption keys securely. For example, Alice could generate all the keys and send them to Bob by encrypting them with his public key; this is how the RSA key exchange works. Alternatively, we could have also used a protocol known as Diffie-Hellman (DH) key exchange for this purpose. The latter is slower, but it has better security properties.
	* In the end, we ended up with a protocol that (1) starts with a handshake phase that includes authentication and key exchange, (2) follows with the data exchange phase with confidentiality and integrity, and (3) ends with a shutdown sequence. At a high level, our protocol is similar to the work done by SSL and TLS.

## Chapter 11: OpenSSL
> `pg: 46`

* RSA
	* `openssl genrsa -aes128 -out fd.key 2048`
	* print info: `openssl rsa -text -in fd.key`
	* extract pubkey: `openssl rsa -in fd.key -pubout -out fd-public.key`
* CSR (Certificate Signing Request)
	* interactive: `openssl req -new -key fd.key -out fd.csr`
	* double-check: `openssl req -text -in fd.csr -noout`
	* extract from existing certificate: `openssl x509 -x509toreq -in fd.crt -out fd.csr -signkey fd.key`
	* non-interactive: `openssl req -new -config fd.cnf -key fd.key -out fd.csr`
* Self-Signed Certificate
	* `openssl x509 -req -days 365 -in fd.csr -signkey fd.key -out fd.crt`
	* without seperate csr: `openssl x509 -req -new -x509 -days 365 -key fd.key -out fd.crt`
	* print info: `openssl x509 -text -in fd.crt -noout`
* Creating Certificates Valid for Multiple Hostnames
	* By default, certificates produced by OpenSSL have only one common name and are valid for only one hostname. Because of this, even if you have related web sites, you are forced to use a separate certificate for each site. In this situation, using a single multidomain certificate makes much more sense. Further, even when you’re running a single web site, you need to ensure that the certificate is valid for all possible paths that end users can take to reach it. In practice, this means using at least two names, one with the www prefix and one without (e.g., www.feistyduck.com and feistyduck.com).
	* There are two mechanisms for supporting multiple hostnames in a certificate. The first is to list all desired hostnames using an X.509 extension called Subject Alternative Name (SAN). The second is to use wildcards. You can also use a combination of the two approaches when it’s more convenient. In practice, for most sites, you can specify a bare domain name and a wildcard to cover all the subdomains (e.g., feistyduck.com and *.feistyduck.com).
	* First, place the extension information in a separate text file. I’m going to call it fd.ext. In the file, specify the name of the extension (subjectAltName) and list the desired hostnames, as in the following example:
		* `subjectAltName = DNS:*.feistyduck.com, DNS:feistyduck.com`
	* Then, when using the x509 command to issue a certificate, refer to the file using the `-extfile` switch:
		* `openssl x509 -req -days 365 -in fd.csr -signkey fd.key -out fd.crt -extfile fd.ext`
* Key and Certificate Conversion
	* Private keys and certificates can be stored in a variety of formats, which means that you’ll often need to convert them from one format to another. The most common formats are:
		* **Binary (DER) certificate**: Contains an X.509 certificate in its raw form, using DER ASN.1 encoding.
		* **ASCII (PEM) certificate(s)**: Contains a base64-encoded DER certificate, with -----BEGIN CERTIFICATE----- used as the header and -----END CERTIFICATE----- as the footer. Usually seen with only one certificate per file, although some programs allow more than one certificate de- pending on the context. For example, the Apache web server requires the server cer- tificate to be alone in one file, with all intermediate certificates together in another.
		* **Binary (DER) key**: Contains a private key in its raw form, using DER ASN.1 encoding. OpenSSL creates keys in its own traditional (SSLeay) format. There’s also an alternative format called PKCS#8 (defined in RFC 5208), but it’s not widely used. OpenSSL can convert to and from PKCS#8 format using the pkcs8 command.
		* **ASCII (PEM) key**: Contains a base64-encoded DER certificate with additional metadata (e.g., the algorithm used for password protection).
		* **PKCS#7 certificate(s)**: A complex format designed for the transport of signed or encrypted data, defined in RFC 2315. It’s usually seen with .p7b and .p7c extensions and can include the entire certificate chain as needed. This format is supported by Java’s keytool utility.
		* **PKCS#12 (PFX) key and certificate(s)**: A complex format that can store and protect a server key along with an entire certificate chain. It’s commonly seen with .p12 and .pfx extensions. This format is commonly used in Microsoft products, but is also used for client certificates. These days, the PFX name is used as a synonym for PKCS#12, even though PFX referred to a different format a long time ago (an early version of PKCS#12). It’s unlikely that you’ll encounter the old version anywhere.
	* PEM and DER conversion
		* Certificate conversion between PEM and DER formats is performed with the x509 tool. To convert a certificate from PEM to DER format:
			* `openssl x509 -inform PEM -in fd.pem -outform DER -out fd.der`
		* To convert a certificate from DER to PEM format:
			* `openssl x509 -inform DER -in fd.der -outform PEM -out fd.pem`
