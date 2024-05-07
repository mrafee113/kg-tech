> `man genrsa`

* openssl-genrsa - generate an RSA private key
* Synopsis
	* `openssl genrsa [-help] [-out filename] [-passout arg] [-aes128] [-aes192] [-aes256] [-aria128] [-aria192] [-aria256] [-camellia128] [-camellia192] [-camellia256] [-des] [-des3] [-idea] [-F4] [-f4] [-3] [-primes num] [-verbose] [-traditional] [-rand files] [-writerand file] [-engine id] [-provider name] [-provider-path path] [-propquery propq] [numbits]`
* Description
	* This command has been deprecated. The [[Security/OpenSSL/genpkey|openssl-genpkey]] command should be used instead.
	* This command generates an RSA private key.

### Options
* `-help`
* `-out filename`
* `-primes num` : Specify the number of primes to use while generating the RSA key. The num parameter must be a positive integer that is greater than 1 and less than 16.  If num is greater than 2, then the generated key is called a 'multi-prime' RSA key, which is defined in RFC 8017.
* `numbits` : The size of the private key to generate in bits. This must be the last option specified. The default is 2048 and values less than 512 are not allowed.
