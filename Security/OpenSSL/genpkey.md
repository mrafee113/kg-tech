> `man openssl-genpkey`

* openssl-genpkey - generate a private key
* Synopsis
	* `openssl genpkey [-help] [-out filename] [-outform DER|PEM] [-quiet] [-pass arg] [-cipher] [-paramfile file] [-algorithm alg] [-pkeyopt opt:value] [-genparam] [-text] [-engine id] [-provider name] [-provider-path path] [-propquery propq] [-config configfile]`
* Description: This command generates a private key.

### Options
* `-help`
* `-out filename` : output the key to file. If not provided, stdout is used.
* `-outform value`
	* The output format, except when `-genparam` is given; the default is `PEM`.
	* See `openssl-format-options(1)` for details.
	* value can be either `DER` or `PEM`
	* When `-genparam` is given, `-outform` is ignored.
* `-pass` : password related, `openssl-passphrase-options(1)`
* `-cipher`
	* This options encrypts the private key with the supplied cipher.
	* Any algorithm name accepted by `EVP_get_cipherbyname()` is acceptable such as `des3`.
* `-algorithm alg`
	* Public key algorithm to use such as RSA, DSA, DH or DHX.
	* If used this option must precede any `-pkeyopt` options.
	* The options `-paramfile` and `-algorithm` are mutually exclusive.
	* Engines may add algorithms in addition to the standard built-in ones.
* `-pkeyopt opt:value`
	* Set the public key algorithm option opt to value.
	* The precise set of options supported depends on the public key algorithm used and its implementation.
	* See the sections "KEY GENERATION OPTIONS" and "PARAMETER GENERATION OPTIONS".
* `-genparam`
	* Generate a set of parameters instead of a private key.
	* If used this option must precede any `-algorithm`, `-paramfile` or `-pkeyopt` options.
* `-paramfile filename`
	* Some public key algorithms generate a private key based on a set of parameters. They can be supplied using this option.
	* If this option is used the public key algorithm used is determined by the parameters.
	* If used this option must precede any `-pkeyopt` options.
	* The options `-paramfile` and `-algorithm` are mutually exclusive.
* `-text` : Print an (unencrypted) text representation of private and public keys and parameters along with the PEM or DER structure.
* `-config configfile` : `config(5)`

### Key Generation Options
* The options supported by each algorithm and indeed each implementation of an algorithm can vary.
* The options for the OpenSSL implementations of RSA are detailed below. Refer to the manual for more.
* RSA Key Generation Options
	* `rsa_keygen_bits:numbits` : The number of bits in the generated key. If not specified 2048 is used.
	* `rsa_keygen_primes:numprimes` : The number of primes in the generated key. If not specified 2 is used.
	* `rsa_keygen_pubexp:value` : The RSA public exponent value. This can be a large decimal or hexadecimal value if preceded by "0x". Default value is 65537.

### Examples
* Generate an RSA private key using default parameters:
	* `openssl genpkey -algorithm RSA -out key.pem`
* Encrypt output private key using 128 bit AES and the passphrase "hello":
	* `openssl genpkey -algorithm RSA -out key.pem -aes-128-cbc -pass pass:hello`
* Generate a 2048 bit RSA key using 3 as the public exponent:
	* `openssl genpkey -algorithm RSA -out key.pem -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:3`
* Generate DSA key from parameters:
	* `openssl genpkey -paramfile dsap.pem -out dsakey.pem`
* Output 2048 bit DH parameters:
	* `openssl genpkey -genparam -algorithm DH -out dhp.pem -pkeyopt dh_paramgen_prime_len:2048`