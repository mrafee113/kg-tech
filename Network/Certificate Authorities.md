### Introduction
* The tools provided by cryptography and related mathematics, including digital signatures and enciphering algorithms, provide a sound basis for constructing secure systems, but a great deal of additional work is required to create an entire system from these parts. Among the items of particular concern are the construction of secure protocols that use cryptographic methods in safe ways, and how keys are created, exchanged, and revoked (called key management). Key management remains one of the greatest challenges in deploying cryptographic systems on a widespread basis across multiple administrative domains.
* One of the challenges with public key cryptosystems is to determine the correct public key for a principal or identity. In our running example, if Alice were to send her public key to Bob, Mallory could modify it in transit to be her own public key, and Bob (called the relying party here) might unknowingly be using Mallory’s key, thinking it is Alice’s. This would allow Mallory to effectively masquerade as Alice. To address this problem, a public key certificate is used to bind an identity to a particular public key using a digital signature. At first glance, this presents a certain “chicken-egg” problem: How can a public key become signed if the digital signature itself requires a reliable public key? There are two ways this is accomplished today.
* One model, called a web of trust, involves having a certificate (identity/key binding) endorsed by a collection of existing users (called endorsers). An endorser signs a certificate and distributes the signed certificate. The more endorsers for= a certificate over time, the more reliable it is likely to be. An entity checking a certificate might require some number of endorsers or possibly some particular endorsers to trust the certificate. The web of trust model is decentralized and “grassroots” in nature, with no central authority. This has mixed consequences. Having no central authority suggests that the scheme will not collapse because of a single point of failure, but it also means that a new entrant may experience some delay in getting its key endorsed to a degree sufficient to be trusted by a significant number of users. Some groups hold “key signing parties” to hasten this process. The web of trust model was first described as part of the Pretty Good Privacy (PGP) encryption system for electronic mail, which has evolved to support a standard encoding format called OpenPGP, defined by some RFC.
* A more formal approach, which has the added benefit of being provably secure under certain theoretical assumptions in exchange for more dependence on a centralized authority, involves the use of a public key infrastructure (PKI). A PKI is a service responsible for creating, revoking, distributing, and updating key pairs and certificates. It operates with a collection of certificate authorities (CAs). A CA is an entity and service set up to manage and attest to the bindings between identities and their corresponding public keys. There are several hundred commercial CAs. A CA usually employs a hierarchical signing scheme. This means that a public key may be signed using a parent key which is in turn signed by a grandparent key, and so on. Ultimately a CA has one or more root certificates upon which many subordinate certificates depend for trust. An entity that is authoritative for certificates and keys (e.g., a CA) is called a trust anchor, although this term is also used to describe the certificates or other cryptographic material associated with such entities, which we discuss next.

### Public Key Certificates, CAs
* While several types of certificates have been used in the past, the one of most interest to us is based on an Internet profile of the ITU-T X.509 standard. In addition, any particular certificate may be stored and exchanged in a number of file or encoding formats. The most common ones include DER, PEM (a Base64 encoded version of DER), PKCS#7 (P7B), and PKCS#12 (PFX). We also saw the use of PKCS#1 in Chapter 8. Today, Internet PKI-related standards tend to use the cryptographic message syntax, which is based on PKCS#7 version 1.5.
* Certificates are primarily used in identifying four types of entities on the Internet: individuals, servers, software publishers, and CAs.
* One popular commercial CA, Verisign, assigns a “class” to each certificate, in the range 1 through 5. Class 1 certificates are intended for individuals, class 2 for organizations, class 3 for servers and software signing, class 4 for online transactions between companies, and class 5 for private organizations and governments.
* Certificate classes are primarily a convenience for grouping and naming types of certificates and for defining different security policies associated with them. Generally speaking, a higher class number is supposed to indicate more rigorous controls on the process required to validate an identity (called identity proofing) prior to issuing the associated certificate.
* This still does not totally solve the chicken-egg PKI bootstrapping problem mentioned before. In practice, systems requiring public key operations have root certificates for popular CAs installed at configuration time (e.g., Microsoft Internet Explorer, Mozilla’s Firefox, and Google’s Chrome are all capable of accessing a preconfigured database of root certificates). To see how this works, we can use a command that gives information about certificates.
	* `CDIR=`\`openssl version -d | awk '{print $2}'\`
	* `openssl s_client _CApath $CDIR -connect www.digicert.com:443 > digicert.out 2>1`
	* `C^` (to interrupt)
	* The first command determines where the local system stores its preconfigured CA certificates. This is usually a directory that varies by system. In this case, the name of the directory is stored in the shell variable CDIR.
	* We next make a connection to the HTTPS port (443) on the `www.digicert.com` server and redirect the output to the digicert.out file. The openssl command2 takes care to print the entity identified by each of the certificates, and at what depth they are in the certificate hierarchy relative to the root (depth 0 is the server’s certificate, so the depth numbers are counted bottom to top). It also checks the certificates against the stored CA certificates to see if they verify properly. In this case, they do, as indicated by “verify return” having value 0 (ok).
	* `grep "return code" digicert.out`
* The file digicert.out contains not only a trace of the connection to the server but also a copy of the server’s certificate. To get the certificate into a more usable form, we can extract the certificate data, convert it, and place the result into a PEM-encoded certificate file:
	* `openssl x509 -in digicert.out -out digicert.pem`
* Given the certificate in PEM format, we can now use a variety of openssl functions to manipulate and inspect it. At the highest level, the certificate includes some data to be signed (called the “TBSCertificate”) followed by a signature algorithm identifier and signature value.
	* To see the server certificate
		* `openssl x509 -in digicert.pem -text`
		* Looking at the command’s output, we see a decoded version of the certificate followed by an ASCII (PEM) representation of the certificate (between the BEGIN CERTIFICATE and END CERTIFICATE indicators). The decoded certificate shows a data portion and a signature portion. Within the data portion is some metadata including a Version field, indicating the particular X.509 certificate type (3, the most recent, is encoded using hex value 0x02), a Serial Number of the particular certificate, a number assigned by the CA unique to each certificate, and a Validity field that gives the time during which the certificate should be treated as legitimate, starting with the Not Before subfield and ending with the Not After subfield. The certificate metadata also indicates which signature algorithm is used to sign the data portion. In this case, it is signed by computing a hash using SHA-1 and signing the result using RSA. The signature itself appears at the end of the certificate.
		* The Issuer field indicates the distinguished name (jargon from the ITU-T X.500 standard) of the entity that issued the certificate and may have these special subfields (based on X.501): C (country), L (locale or city), O (organization), OU (organizational unit), ST (state or province), CN (common name). Other subfields have also been defined. In this case, we can see that an extended validation (EV) CA certificate has been used to sign the server’s certificate.
			* EV certificates represent an industry response to certain phishing attacks involving malicious Web sites that were issued certificates without rigorous identity proofing. Issuing of an EV certificate takes place only under an agreed-upon set of stringent criteria, and a user visiting a Web site using EV certificates and a modern browser typically sees a green title bar and CA information to indicate the enhanced level of rigor. One of the requirements for EV certificates placed upon each CA is to provide a certification practice statement (CPS), which outlines the practices used in issuing certificates. Considerations for authors of CPSs (and certificate policies or CPs that apply on a per-certificate basis) are given in. Note that although EV certificates may provide higher assurance (e.g., for some Web sites), most users do not pay careful attention to the cues provided by Web browsers that reveal this fact.
		* The Subject field identifies the entity this certificate is about, and the owner of the public key contained in the subsequent Subject Public Key Info field. In this example, the Subject field is a somewhat complex structure like the Issuer field and contains multiple object IDs (OIDs). Most are decoded with names (e.g., O, C, ST, L, CN), but some are not because the particular version of openssl that printed the output did not understand them. The OID 1.3.6.1.4.1.311.60.2.1.3 is also called jurisdictionOfIncorporationCountryName, and 1.3.6.1.4.1.311.60.2.1.2 is called jurisdictionOfIncorporationStateOrProvinceName, both with obvious meanings. The OID 2.5.4.15 is businessCategory. Note that the CN subfield tends to be an important one when identifying subjects and issuers for certificates used on the Internet. For this certificate, it gives the correct matching name for the server (along with any names included in the Subject Alternative Name (SAN) extension). Nonmatching names or URLs (e.g., `https:// digicert.com` instead of `https://www.digicert.com`) referring to the same server, when accessed, result in an error. Note that CN is not really the field for holding a DNS name; SANs are intended for this purpose.
		* When a certificate needs to be validated, a recursive process works up the certificate hierarchy to a root CA certificate by matching the issuer distinguished name in one certificate with the subject name in another. In this case, the certificate was issued by DigiCert High Assurance EV CA-1 (the issuer’s CN subfield). Assuming all certificates are current in their validity periods and are being used in appropriate ways, some parent certificate (immediate parent, grandparent, etc., but usually a root CA certificate) to the Subject field of the certificate we are evaluating must be trusted for validation to be successful.
		* The Subject Public Key Info field gives the algorithm and public key belonging to the entity specified in the Subject field. In this case, the public key is an RSA public key with a 2048-bit modulus and public exponent of 65537. The subject is in possession of the matching RSA private key (modulus plus private exponent) that is paired to the public key. If the private key is compromised, or if the public key needs to be changed for other reasons, the public and private keys must be regenerated and a new certificate issued. The old certificate is then revoked.
		* Version 3 X.509 certificates may include zero or more extensions. Extensions are either critical or noncritical, and some are required by the Internet profile in some RFC. If critical, an extension must be processed and found acceptable by the relying party’s (CPS jargon) policy. Noncritical extensions are processed if supported but do not otherwise cause errors. In the present example, there are ten X.509v3 extensions. Although many extensions have been defined, those we shall discuss tend to fall into two informal categories. The first category includes information about the subject and how the certificate in question can be used. The second category relates to items describing the issuer and may include key identification and URIs indicating locations of additional information related to the issuing CA that is not included elsewhere. The certificate in our example is an end entity (not CA) certificate. CA certificates often have somewhat different extensions or values for their extensions.
			* The Basic Constraints extension, a critical extension, indicates whether the certificate is a CA certificate. In this case it is not, so it cannot be used for signing other certificates. A certificate indicating that it is a CA certificate may be used in a certificate validation chain at a location other than a leaf. This is common for root CA certificates or for other certificate-signing certificates (“intermediate” certificates, such as the DigiCert High Assurance EV CA-1 certificate referenced in this example).
			* The Subject Key Identifier extension identifies the public key in the certificate. It allows different keys owned by the same subject to be differentiated. The Key Usage extension, a critical extension, determines the valid usage for the key. Possible usages include digital signature, nonrepudiation (content commitment), key encipherment, data encipherment, key agreement, certificate signing, CRL signing (see Section 18.5.2), encipher only, and decipher only. Because server certificates of this kind are primarily used for identifying the two endpoints of a connection and encrypting a session key (see Section 18.9), the possible usages may be somewhat limited, as in this case.
			* The Extended Key Usage extension, which may be critical or noncritical, may provide further restrictions on the key use. Possible values of this extension when used in the Internet profile include the following: TLS client and server authentication, signing of downloadable code, e-mail protection (nonrepudiation and key agreement or encipherment), various IPsec operating modes (see Section 18.8), and timestamping.
			* The SAN extension allows a single certificate to be used for multiple purposes (e.g., for multiple Web sites with distinct DNS names). This alleviates the need to have a separate certificate for each Web site, which can significantly reduce cost and administrative burden.
			* The Netscape Cert Type extension is now deprecated but was used to indicate key usage to Netscape software.
			* **The remaining extensions in our example certificate relate to the management and status of the certificate and its issuing CA.**
			* The CRL Distribution Points (CDP) extension gives a list of URLs for finding the CA’s certificate revocation list (CRL), a list of revoked certificates used to determine if a certificate in a validation chain has been revoked (see Section 18.5.2).
			* The Certificate Policies (CP) extension includes certificate policies applicable to the certificate.
			* The Authority Information Access (AIA) extension indicates where information may be retrieved from the CA.