> `man openssl-req`

* openssl-req - PKCS#10 certificate request and certificate generating command
* Synopsis
	* `openssl req [-help] [-inform DER|PEM] [-outform DER|PEM] [-in filename] [-passin arg] [-out filename] [-passout arg] [-text] [-pubkey] [-noout] [-verify] [-modulus] [-new] [-newkey arg] [-pkeyopt opt:value] [-noenc] [-nodes] [-key filename|uri] [-keyform DER|PEM|P12|ENGINE] [-keyout filename] [-keygen_engine id] [-digest] [-config filename] [-section name] [-x509] [-CA filename|uri] [-CAkey filename|uri] [-days n] [-set_serial n] [-newhdr] [-copy_extensions arg] [-addext ext] [-extensions section] [-reqexts section] [-precert] [-utf8] [-reqopt] [-subject] [-subj arg] [-multivalue-rdn] [-sigopt nm:v] [-vfyopt nm:v] [-batch] [-verbose] [-nameopt option] [-rand files] [-writerand file] [-engine id] [-provider name] [-provider-path path] [-propquery propq]`
* Description: This command primarily creates and processes certificate requests (CSRs) in PKCS#10 format. It can additionally create self-signed certificates for use as root CAs for example.

### Options
* `-help`
* `-inform DER|PEM, -outform DER|PEM`
	* see `openssl-format-options(1)`
	* The data is a PKCS#10 object.
* `-in filename`
	* This specifies the input filename to read a request from.
	* This defaults to standard input unless `-x509` or `-CA` is specified.
	* A request is only read if the creation options (`-new` or `-newkey` or `-precert`) are not specified.
* `-sigopt nm:v`
	* Pass options to the signature algorithm during sign operations.
	* Names and values of these options are algorithm-specific.
* `-vfyopt nm:v`
	* Pass options to the signature algorithm during verify operations.
	* Names and values of these options are algorithm-specific.
* `-out filename`
* `-text` : prints out the certificate request in text form
* `-subject` : Prints out the certificate request subject (or certificate subject if -x509 is in use).
* `-pubkey` : prints out the public key
* `-noout` : this option prevents output of the encoded version of the certificate request.
* `-modulus` : Prints out the value of the modulus of the public key contained in the request.
* `-verify` : verifies the self-signature on the request
* `-new`
	* This option generates a new certificate request.
	* It will prompt the user for the relevant field values. The actual fields prompted for and their maximum and minimum sizes are specified in the configuration file and any requested extensions.
	* If the `-key` option is not given it will generate a new private key using information specified in the configuration file or given with the `-newkey` and `-pkeyopt` options, else by default an RSA key with 2048 bits length.
* `-newkey arg`
	* This option is used to generate a new private key unless `-key` is given. It is subsequently used as if it was given using the `-key` option.
	* This option implies the `-new` flag to create a new certificate request or a new certificate in case `-x509` is given.
	* `[rsa:]nbits` generates an RSA key nbits in size.  If nbits is omitted, i.e., `-newkey rsa` is specified, the default key size specified in the configuration file with the `default_bits` option is used if present, else 2048.
* `-pkeyopt opt:value`
	* Set the public key algorithm option opt to value.
	* The precise set of options supported depends on the public key algorithm used and its implementation.
	* See "KEY GENERATION OPTIONS" in `openssl-genpkey(1)` for more details.
* `-key filename|uri`
	* This option provides the private key for signing a new certificate or certificate request.
	* Unless `-in` is given, the corresponding public key is placed in the new certificate or certificate request, resulting in a self-signature.
	* For certificate signing this option is overridden by the `-CA` option.
	* This option also accepts PKCS#8 format private keys for PEM format files.
* `-keyform DER|PEM|P12|ENGINE` : The format of the private key; unspecified by default.  See openssl-format-options(1) for details.
* `-keyout filename`
	* This gives the filename to write any private key to that has been newly created or read from `-key`.
	* If neither the `-keyout` option nor the `-key` option are given then the filename specified in the configuration file with the `default_keyfile` option is used, if present. Thus, if you want to write the private key and the `-key` option is provided, you should provide the `-keyout` option explicitly.
	* If a new key is generated and no filename is specified the key is written to standard output.
* `-noenc` : If this option is specified then if a private key is created it will not be encrypted.
* `-digest`
	* This specifies the message digest to sign the request.
	* Any digest supported by the OpenSSL `dgst` command can be used.
	* This overrides the digest algorithm specified in the configuration file.
	* Some public key algorithms may override this choice. For instance, DSA signatures always use SHA1.
* `-config filename`
	* This allows an alternative configuration file to be specified.
	* Optional; for a description of the default value, see "COMMAND SUMMARY" in `openssl(1)`.
* `-section name` : specifies the name of the section to use; the default is `req`.
* `-subj arg`
	* Sets subject name for new request **or** supersedes the subject name when processing a certificate request.
	* The arg must be formatted as "/type0=value0/type1=value1/type2=...".
		* Special characters may be escaped by "\\" (backslash), whitespace is retained.
		* Empty values are permitted, but the corresponding type will not be included in the request.
	* [stackoverflow: subject fields and meanings](https://stackoverflow.com/questions/6464129/certificate-subject-x-509)
* `-x509`
	* This option outputs a certificate instead of a certificate request.
	* This is typically used to generate test certificates.
	* It is **implied** by the `-CA` option.
	* This option implies the `-new` flag ***if*** `-in` is not given.
	* If an existing request is specified with the `-in` option, it is converted to the a certificate; otherwise a request is created from scratch.
	* Unless specified using the `-set_serial` option, a large random number will be used for the serial number.
	* Unless the `-copy_extensions` option is used, X.509 extensions are not copied from any provided request input file.
	* X.509 extensions to be added can be specified in the configuration file or using the `-addext` option.
* `-CA filename|uri`
	* Specifies the "CA" certificate to be used for signing a new certificate and **implies** use of `-x509`.
	* When present, this behaves like a "micro CA" as follows: The subject name of the "CA" certificate is placed as issuer name in the new certificate, which is then signed using the "CA" key given.
* `-CAkey filename|uri`
	* Sets the "CA" private key to sign a certificate with.
	* The private key must match the public key of the certificate given with `-CA`.
	* If this option is not provided then the key **must** be present in the `-CA` input.
* `-days n` : When `-x509` is in use this specifies the number of days to certify the certificate for, otherwise it is ignored. n should be a positive integer. The default is 30 days.
* `-set_serial n`
	* Serial number to use when outputting a self-signed certificate.
	* This may be specified as a decimal value or a hex value if preceded by "0x".
	* If not given, a large random number will be used.
* `-copy_extensions arg`
* `-addext ext`
* `-extensions section`
* `-reqexts section`
* `-utf8` : This option causes field values to be interpreted as UTF8 strings, by default they are interpreted as ASCII. This means that the field values, whether prompted from a terminal or obtained from a configuration file, must be valid UTF8 strings.
* `-reqopt option`
	* Customise the printing format used with `-text`.
	* The option argument can be a single option or multiple options separated by commas.
	* See discussion of the  `-certopt` parameter in the `openssl-x509(1)` command.
* `-batch` : non-interactive mode
* `-verbose`
* `-nameopt option`
	* This specifies how the subject or issuer names are displayed.
	* See `openssl-namedisplay-options(1)` for details.
* `-rand files` `-writerand file`

### Configuration File Format
* The configuration options are specified in the `req` section of the configuration file.
* An alternate name be specified by using the `-section` option.
* As with all configuration files, if no value is specified in the specific section then the initial unnamed or default section is searched too.
* `default_bits` : the default key size in bits. used with `-new`
* `default_keyfile` : default filename to write a private key to. overridden by `-keyout`
* `req_extensions` : overridden by `-reqexts`. see `x509v3_config(5)`
* `x509_extensions` : overridden by `-x509`
* `prompt`
* `utf8`

### Examples
* Examine and verify certificate request:
	* `openssl req -in req.pem -text -verify -noout`
* Create a private key and then generate a certificate request from it:
	* `openssl genrsa -out key.pem 2048`
	* `openssl req -new -key key.pem -out req.pem`
* The same but just using req:
	* `openssl req -newkey rsa:2048 -keyout key.pem -out req.pem`
* Generate a self-signed root certificate:
	* `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out req.pem`

* Sample configuration file prompting for field values:
	```
	[ req ]
	default_bits           = 2048
	default_keyfile        = privkey.pem
	distinguished_name     = req_distinguished_name
	attributes             = req_attributes
	req_extensions         = v3_ca
	
	dirstring_type = nobmp
	
	[ req_distinguished_name ]
	countryName                    = Country Name (2 letter code)
	countryName_default            = AU
	countryName_min                = 2
	countryName_max                = 2
	
	localityName                   = Locality Name (eg, city)
	
	organizationalUnitName         = Organizational Unit Name (eg, section)
	
	commonName                     = Common Name (eg, YOUR name)
	commonName_max                 = 64
	
	emailAddress                   = Email Address
	emailAddress_max               = 40
	
	[ req_attributes ]
	challengePassword              = A challenge password
	challengePassword_min          = 4
	challengePassword_max          = 20
	
	[ v3_ca ]
	
	subjectKeyIdentifier=hash
	authorityKeyIdentifier=keyid:always,issuer:always
	basicConstraints = critical, CA:true
	```

* Sample configuration containing all field values:
	```
	[ req ]
	default_bits           = 2048
	default_keyfile        = keyfile.pem
	distinguished_name     = req_distinguished_name
	attributes             = req_attributes
	prompt                 = no
	output_password        = mypass
	
	[ req_distinguished_name ]
	C                      = GB
	ST                     = Test State or Province
	L                      = Test Locality
	O                      = Organization Name
	OU                     = Organizational Unit Name
	CN                     = Common Name
	emailAddress           = test@email.address
	
	[ req_attributes ]
	challengePassword              = A challenge password
	
	Example of giving the most common attributes (subject and extensions) on the command line:
	
	openssl req -new -subj "/C=GB/CN=foo" \
					 -addext "subjectAltName = DNS:foo.co.uk" \
					 -addext "certificatePolicies = 1.2.3.4" \
					 -newkey rsa:2048 -keyout key.pem -out req.pem
	```