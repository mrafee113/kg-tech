> `man openssl-rsa`

* openssl-rsa - RSA key processing command
* Synopsis
	* `openssl rsa [-help] [-inform DER|PEM|P12|ENGINE] [-outform DER|PEM] [-in filename|uri] [-passin arg] [-out filename] [-passout arg] [-aes128] [-aes192] [-aes256] [-aria128] [-aria192] [-aria256] [-camellia128] [-camellia192] [-camellia256] [-des] [-des3] [-idea] [-text] [-noout] [-modulus] [-traditional] [-check] [-pubin] [-pubout] [-RSAPublicKey_in] [-RSAPublicKey_out] [-pvk-strong] [-pvk-weak] [-pvk-none] [-engine id] [-provider name] [-provider-path path] [-propquery propq]`
* Description
	* This command processes RSA keys. They can be converted between various forms and their components printed out.
	* use `openssl-pkey` instead. Also, the example section was repetetive.

### Options
* `-help`
* `-inform DER|PEM|P12|ENGINE`
	* The key input format; unspecified by default.
	* see `openssl-format-options(1)`
* `-outform DER|PEM`
	* The key output format; the default is PEM.
	* see `openssl-format-options(1)`
* `-traditional` : use PKCS#1 format instead of PKCS#8
* `-in filename|uri`
* `-out filename`
* `-text` : prints out the various public or private key components in plain text in addition to the encoded version.
* `-noout` : prevents output of the encoded version of the key
* `-modulus` : prints out the value of the modulus of the key
* `-check` : checks the consistency of an RSA private key
* `-pubin` : By default a private key is read from the input file: with this option a public key is read instead.
* `-pubout` : By default a private key is output: with this option a public key will be output instead. This option is automatically set if the input is a public key.