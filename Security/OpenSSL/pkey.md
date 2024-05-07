> `man openssl-pkey`

* openssl-pkey - public or private key processing command
* Synopsis
	* `openssl pkey [-help] [-engine id] [-provider name] [-provider-path path] [-propquery propq] [-check] [-pubcheck] [-in filename|uri] [-inform DER|PEM|P12|ENGINE] [-passin arg] [-pubin] [-out filename] [-outform DER|PEM] [-cipher] [-passout arg] [-traditional] [-pubout] [-noout] [-text] [-text_pub] [-ec_conv_form arg] [-ec_param_enc arg]`
* Description
	* This command processes public or private keys. They can be converted between various forms and their components printed.

### Options
#### General Options
* `-help`
* `-check` : checks the consistency of a key pair for both public and private components
* `-pubcheck` : checks the correctness of either a public key or the public component of a key pair

#### Input Options
* `-in filename|uri`
* `-inform DER|PEM|P12|ENGINE`
	* The key input format; unspecified by default.
	* see `openssl-format-options(1)`
* `-pubin` : By default a private key is read from the input.  With this option only the public components are read.

#### Output Options
* `-out filename`
* `-outform DER|PEM`
	* The key output format; the default is PEM.
	* see `openssl-format-options(1)`
* `-cipher`
	* Encrypt the PEM encoded private key with the supplied cipher.
	* Any algorithm name accepted by `EVP_get_cipherbyname()` is acceptable such as `aes128`.
	* Encryption is not supported for DER output.
* `-traditional` : use PKCS#1 format instead of PKCS#8
* `-pubout`
	* By default the private and public key is output; this option restricts the output to the public components.
	* This option is automatically set if the input is a public key.
	* When combined with `-text`, this is equivalent to `-text_pub`.
* `-noout` : Do not output the key in encoded form.
* `-text`
	* Output the various key components in plain text (possibly in addition to the PEM encoded form).
	* This cannot be combined with encoded output in DER format.
* `-text_pub`
	* Output in text form only the public key components (also for private keys).
	* This cannot be combined with encoded output in DER format.

### Examples
* To remove the pass phrase on a private key:
	* `openssl pkey -in key.pem -out keyout.pem`
* To encrypt a private key using triple DES:
	* `openssl pkey -in key.pem -des3 -out keyout.pem`
* To convert a private key from PEM to DER format:
	* `openssl pkey -in key.pem -outform DER -out keyout.der`
* To print out the components of a private key to standard output:
	* `openssl pkey -in key.pem -text -noout`
* To print out the public components of a private key to standard output:
	* `openssl pkey -in key.pem -text_pub -noout`
* To just output the public part of a private key:
	* `openssl pkey -in key.pem -pubout -out pubkey.pem`