> [geekflare](https://geekflare.com/tls-101/)

* While Netscape originally invented SSL in the mid-90s, it didn’t become compulsory for every website to install an SSL/TLS certificate until the Summer of 2018 when Google began marking unencrypted sites “**Not Secure**."
	* While Google – with its search engine, Chrome browser, and Android OS – can redefine the internet unilaterally, it was not alone on this mandate. Apple, Microsoft, Mozilla and the other major stakeholders in the tech industry have all made a concerted decision to mandate SSL/TLS certificates and HTTPS.
	* The reason for that is simple: without SSL/TLS and the ability to connect securely via HTTPS, all communication between websites and their visitors would be exchanged in plaintext and easily readable by a third party.

### An issue of exchanging keys
* What we discussed earlier, and what has traditionally been the standard for encryption, is private key encryption. This is also called symmetric encryption, or two-way encryption—with private keys handling both the encryption and decryption functions needed to communicate.
* For private key encryption to work the private key must be transferred between parties, or both parties need to possess their own copy. Either way, private key security was critical to the integrity of the cryptosystem and, as you can no doubt surmise, key exchange is a problem as old as encryption itself.
* Then, in the 1970s – technically two different times, an entire ocean apart – a new form of encryption was conceptualized and brought to life: public key encryption.
* Whereas private key encryption is a two-way function, symmetric, with the private key capable of both encrypting and decrypting data, public key encryption is asymmetric; one way. Rather than a single private key, there is a public-private key pair. The public key handles encryption and is, as the name implies, publicly available while the private key, which handles decryption, is kept secret by its owner. Using the public key, one can encrypt a piece of data and send it to the key’s owner, where only they will be able to decrypt it.
* Great, but how is that useful? Well, one-way encryption isn’t ideal for encrypting internet connections, it’s kind of difficult to communicate when one party can only encrypt, and the other can only decrypt. No, to encrypt an internet connection, you would need to use symmetric, private key encryption.
* But how do you exchange keys? Especially online? Public key encryption. And that, distilled down to its very essence, is what SSL/TLS is all about: secure key exchange.
* This is where we’ll tie all these concepts together. If you want your communication with a website to be private, then you need to connect to it securely. If you want to connect securely with that website, then you need to exchange symmetric private keys so you can use them to communicate. SSL/TLS (and PKI in general) is just a fancy mechanism for creating and exchanging that session key.
* Using SSL/TLS, you can authenticate the server or organization you’re about to connect with and ensure that you securely exchange the private keys you’ll use to encrypt your communication with the intended party.

### Building a Public Key Infrastructure (PKI)
* Now that we’ve laid the foundation let’s zoom out and look at the architecture employed by the trust model at the heart of SSL/TLS.
* When you arrive at a website, the first thing your browser does is verifies the authenticity of the SSL/TLS certificate that the site presents it with. We’re going to start by discussing the trust model that makes all this possible.
* So, we’ll begin by posing the question: how does my computer know whether to trust a given SSL/TLS certificate?
* To answer that, we’ll need to discuss and the various elements that make it work. We’ll start with Certificate Authorities and Root programs.

#### Certificate Authorities
* A Certificate Authority is an organization that complies with a set of predetermined standards in return for the ability to issue trusted digital certificates.
* There are dozens of CAs, both free and commercial, that can issue trusted certificates.
* They all must abide by a set of standards that has been debated and legislated through the CA/Browser Forum, which acts as the regulatory body for the TLS industry. These standards outline things like:
	* Technical safeguards that must be in place
	* Best practices for performing validation
	* Issuance best practices
	* Revocation procedures and timelines
	* Certificate Logging requirements
* These guidelines have been set forth by the browsers, in conjunction with the CAs. The browsers play a unique role in the TLS ecosystem.
* Nobody can get anywhere on the internet without their web browser. As such, it’s the browser that will be receiving and validating the digital TLS certificate and then exchanging keys with the server. So, given their paramount role, they bear considerable influence.
* And it’s important to keep in mind that browsers have been designed to be as skeptical as possible. To trust nothing. This is the best way to keep their users safe. So, if a browser is going to trust a digital certificate – which can potentially be misused to the detriment of the user – it needs certain assurances that whoever issued this certificate did their due diligence.
* This is the role and responsibility of the Certificate Authorities. And the browsers don’t abide mistakes, either. There is a literal graveyard of former CAs that have run afoul of the browsers and been put out to pasture.
* When a Certificate Authority has demonstrated its compliance with the CAB Forum baseline requirements and has passed all the requisite audits and reviews, it can petition the various root programs to have its Root certificates added.

#### Root Programs
* A root program – the major ones are run by Apple, Microsoft, Google, and Mozilla – is the apparatus that oversees and facilitates root stores (sometimes called trust stores), which are collections of Root CA certificates that reside on a user’s system. Once again, these roots are incredibly valuable and incredibly dangerous – they can issue trusted digital certificates, after all – so security is of the utmost concern.
* That’s why CAs almost never issue directly from the Root CA certificates themselves. Instead, they spin up intermediate root certificates and use those to issue end user or leaf certificates. They can also hand those roots off to Sub-CAs, which are Certificate Authorities that don’t have their dedicated roots but can still issue cross-signed certificates off their intermediates.
* So, let’s put this all together. When a website wants to have a TLS certificate issued, it generates something called a Certificate Signing Request (CSR) on the server it’s hosted on. Contained in this request are all the details the website wants to be included on the certificate. As you’ll see in a bit, the amount of information can vary from complete business details to a simple server identity, but once the CSR is completed, it’s sent along to the Certificate Authority for issuance.
* Before issuing the certificate, the CA will have to do its CA/Browser Forum-mandated due diligence and validate that the information contained in the CSR is accurate. Once that’s been verified, it signs the certificate with its private key and sends it back to the website owner for installation.

#### Certificate Chaining
* After the TLS certificate has been installed, anytime someone visits the site the server hosting it will present the user’s browser with the certificate. The browser is going to look at the digital signature on the certificate, the one that was made by the trusted certificate authority, which vouches for the fact that all information contained in the certificate is accurate.
* This is where the term certificate chaining comes into play.
* The browser is going to read the digital signature and move up a link on the chain—next, it will check the digital signature on the intermediate certificate whose private key was used to sign the leaf certificate. It’s going to continue following signatures until either the certificate chain ends at one of the trusted roots in its root store, or until the chain terminates without reaching a root, in which case a browser error will appear, and the connection will fail.

![img](https://geekflare.com/wp-content/uploads/2019/01/chain-cert.png)

* This is why you can’t issue and self-sign your certificates.
* The browsers will only trust SSL/TLS certificates that they can chain back to their root store (meaning that they were issued by a trusted entity). Certificate Authorities are required to abide by specific standards to maintain their trustworthiness, and even then the browsers are loath to trust them.
* Browsers have no such assurances about self-signed certificates, which is why they should only be deployed on internal networks, behind firewalls, and in test environments.

### SSL/TLS Certificate Types and Functionality
* Let’s talk about certificates and the various iterations that are available. TLS certificates are what facilitate the TLS protocol and help dictate the terms of the encrypted HTTPS connections that a website makes.
* Earlier we mentioned that installing a TLS certificate allows you to configure your website to make HTTPS connections via port 443. It also acts as a sort of name badge for the site or server you’re interacting with. Going back to the idea that at its heart, SSL/TLS and PKI are all exquisite forms of secure key exchange, the SSL/TLS certificate helps notify the browser of who it’s sending the session key to—who the party at the other end of the connection is.
* And when you break down the various iterations of SSL/TLS certificates, that’s a pertinent thing to keep in mind. Certificates vary regarding functionality and validation level. Or to put it another way, they vary based on:
	* How many identities to assert
	* What endpoints to assert identity on
* Answering those two questions will give you a pretty clear indication of what type of certificate you need.

### SSL/TLS in motion
#### Validation and Issuance
* Let’s start all the way at the beginning with a website purchasing an SSL/TLS certificate from a CA or reseller. Following the purchase, the organizational contact that is handling the certificate acquisition creates a Certificate Signing Request on the server where the certificate will be installed (the server that hosts the website).
* Along with the CSR, the server will also generate a public/private key pair and save the private key locally. When the CA receives the CSR and the Public Key, it performs the requisite validation steps to ensure that any information contained in the certificate is accurate. Generally, for business authentication certificates (not DV) this involves looking up an organization’s registration information and public records in government databases.
* Once validation has been completed, the CA uses one of the private keys from one of its issuing certificates, typically an intermediate root, and signs the certificate before returning it to the site owner.
* Now the website owner can take the newly issued SSL/TLS certificate, install it on their server and configure the website to make HTTPS connections on port 443 (using 301 redirects to send traffic from the pre-existing HTTP pages to their new HTTPS counterparts).

#### Authentication and the SSL Handshake
* Upon arriving at the website, the server will present the SSL/TLS certificate to the user’s browser. The user’s browser then performs a series of checks.
* First, it’s going to authenticate the certificate by viewing its digital signature and following the certificate chain. It will also make sure the certificate hasn’t expired and check Certificate Transparency (CT) logs and Certificate Revocation Lists (CRLs). Provided the chain leads back to one of the roots in the system’s trust store, and that it’s valid, the browser will trust the certificate.
* Now it’s handshake time. The SSL/TLS handshake is the series of steps where the client (user) and the server (website) negotiate the parameters of their secure connection, generate and then exchange symmetric session keys.
* First, they’re going to decide on a cipher suite. A cipher suite is the group of algorithms and ciphers that will be used for the connection. The SSL/TLS certificate provides a list of cipher suites that the server supports. Generally, a cipher suite includes a public key encryption algorithm, a key generation algorithm, a message authentication algorithm and a symmetric or bulk encryption algorithm—though that has been refined in TLS 1.3.
* Upon being presented with the list of supported ciphers, the client will pick an agreeable one and communicate it to the server. From there, the client will generate a symmetric session key, encrypt it using the public key and then send it along to the server, who possesses the private key needed to decrypt the session key.
* Once both parties have a copy of the session key, communication can commence.