> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/)

## Prerequisites
> [source](https://github.com/ddometita/mmumshad-kubernetes-the-hard-way/blob/master/docs/01-prerequisites.md)

* VM Hardware Requirements
	* 8 GB of RAM (Preferebly 16 GB)
	* 50 GB Disk space
* Install VirtualBox and [Vagrant](https://vagrantup.com/)

## Installing Client Tools
> [source](https://github.com/kelseyhightower/kubernetes-the-hard-way/blob/master/docs/02-client-tools.md)
* The filtering on `dl.k8s.io` and `storage.googleapis.com` is very strict. At the time of writing this (Jul 1 2023), I had to connect using Windscribe, download on my local pc and transfer the binaries to the VM manually. Nothing else worked against the filtering.
* Install CFSSL
	* The `cfssl` and `cfssljson` command line utilities will be used to provision a [PKI Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) and generate TLS certificates.
	* Alternative source for binaries: [github releases](https://github.com/cloudflare/cfssl/releases)
	* `wget -q --show-progress --https-only --timestamping https://storage.googleapis.com/kubernetes-the-hard-way/cfssl/[replace with stable/latest version]/linux/cfssl https://storage.googleapis.com/kubernetes-the-hard-way/cfssl/[replace with stable/latest version]/linux/cfssljson`
	* `chmod +x cfsl*`
	* `mv cfssl_... cfssl`
	* `mv cfssljson... cfssljson`
	* `mv cfssl cfssljson /usr/local/bin/`
	* `cfssl version`
	* `cfssljson --version`
* Install KubeCTL
	* The `kubectl` command line utility is used to interact with the Kubernetes API Server. Download and install `kubectl` from the official release binaries.
	* `KUBECTL_VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)`
	* `curl -L --output "kubectl_v$KUBECTL_VERSION_amd64" "https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl"`
	* `chmod +x kubectl`
	* `mv kubectl_... kubectl`
	* `mv kubectl /usr/local/bin/`
		* or alternatively: `sudo install -o root -g root -m 0755 ./kubectl /usr/local/bin/kubectl`
	* `kubectl version --short` or something like that. There's been a lot of deprecation going on... it's not clear which one is the right one.
