> [source](https://developer.hashicorp.com/vagrant/docs/networking)

### Overview
* In order to access the Vagrant environment created, Vagrant exposes some high-level networking options for things such as forwarded ports, connecting to a public network, or creating a private network.
* The high-level networking options are meant to define an abstraction that works across multiple [providers](https://developer.hashicorp.com/vagrant/docs/providers). This means that you can take your Vagrantfile you used to spin up a VirtualBox machine and you can reasonably expect that Vagrantfile to behave the same with something like VMware.

### Basic Usage
> [source](https://developer.hashicorp.com/vagrant/docs/networking/basic_usage)

* Vagrant offers multiple options for how you are able to connect your guest machines to the network, but there is a standard usage pattern as well as some points common to all network configurations that are important to know.
* All networks are configured within your [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile) using the `config.vm.network` method call. For example, the Vagrantfile below defines some port forwarding:
* Multiple networks can be defined by having multiple `config.vm.network` calls within the Vagrantfile. The exact meaning of this can differ for each [provider](https://developer.hashicorp.com/vagrant/docs/providers), but in general the order specifies the order in which the networks are enabled.
* Networks are automatically configured and enabled after they've been defined in the Vagrantfile as part of the `vagrant up` or `vagrant reload` process.

#### Setting a Hostname
* A hostname may be defined for a Vagrant VM using the `config.vm.hostname` setting. By default, this will modify `/etc/hosts`, adding the hostname on a loopback interface that is not in use. For example:
```ruby
Vagrant.configure("2") do |config|
  # ...
  config.vm.hostname = "myhost.local"
end
```
* will add the entry `127.0.X.1 myhost myhost.local` to `/etc/hosts`.
* A public or private network with an assigned IP may be flagged for hostname. In this case, the hostname will be added to the flagged network. Note, that if there are multiple networks only one may be flagged for hostname. For example:
```ruby
Vagrant.configure("2") do |config|
  # ...
  config.vm.hostname = "myhost.local"
  config.vm.network "public_network", ip: "192.168.0.1", hostname: true
  config.vm.network "public_network", ip: "192.168.0.2"
end
```
* will add the entry `192.168.0.1 myhost myhost.local` to `/etc/hosts`.

### Forwarded Ports
> [source](https://developer.hashicorp.com/vagrant/docs/networking/forwarded_ports)

* Vagrant forwarded ports allow you to access a port on your host machine and have all data forwarded to a port on the guest machine, over either TCP or UDP.
* For example: If the guest machine is running a web server listening on port 80, you can make a forwarded port mapping to port 8080 (or anything) on your host machine. You can then open your browser to `localhost:8080` and browse the website, while all actual network data is being sent to the guest.

#### Definition
* The forwarded port configuration expects two parameters, the port on the guest and the port on the host. Example:
```ruby
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080
end
```
* This will allow accessing port 80 on the guest via port 8080 on the host.
* For most providers, forwarded ports by default bind to all interfaces. This means that other devices on your network can access the forwarded ports. If you want to restrict access, see the `guest_ip` and `host_ip` settings below.

#### Options
* This is a complete list of the options that are available for forwarded ports. Only the `guest` and `host` options are required. Below this section, there are more detailed examples of using these options.
* `auto_correct` (boolean) : If true, the host port will be changed automatically in case it collides with a port already in use. By default, this is false.
* `guest_ip` (string) : The guest IP to bind the forwarded port to. If this is not set, the port will go to every IP interface. By default, this is empty.
* `host` (int) : The port on the host that you want to use to access the port on the guest. This must be greater than port 1024 unless Vagrant is running as root (which is not recommended).
* `host_ip` (string) : The IP on the host you want to bind the forwarded port to. If not specified, it will be bound to every IP. By default, this is empty.
* `protocol` (string) : Either "udp" or "tcp". This specifies the protocol that will be allowed through the forwarded port. By default this is "tcp".
* `id` (string) : Name of the rule (can be visible in VirtualBox). By default this is "protocol""guest" (example : "tcp123").

#### Port Collisions and Correction
* It is common when running multiple Vagrant machines to unknowingly create forwarded port definitions that collide with each other (two separate Vagrant projects forwarded to port 8080, for example). Vagrant includes built-in mechanism to detect this and correct it, automatically.
* Port collision detection is always done. Vagrant will not allow you to define a forwarded port where the port on the host appears to be accepting traffic or connections.
* Port collision auto-correction must be manually enabled for each forwarded port, since it is often surprising when it occurs and can lead the Vagrant user to think that the port was not properly forwarded.
* The final `:auto_correct` parameter set to true tells Vagrant to auto correct any collisions. During a `vagrant up` or `vagrant reload`, Vagrant will output information about any collisions detections and auto corrections made, so you can take notice and act accordingly.
* You can define allowed port range assignable by Vagrant when port collision is detected via [config.vm.usable_port_range](https://developer.hashicorp.com/vagrant/docs/vagrantfile/machine_settings) property.
```ruby
Vagrant.configure("2") do |config|
  config.vm.usable_port_range = 8000..8999
end
```

### Private Networks
> [source](https://developer.hashicorp.com/vagrant/docs/networking/private_network)

* Vagrant private networks allow you to access your guest machine by some address that is not publicly accessible from the global internet. In general, this means your machine gets an address in the [private address space](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces).
* Multiple machines within the same private network (also usually with the restriction that they're backed by the same [provider](https://developer.hashicorp.com/vagrant/docs/providers)) can communicate with each other on private networks.

#### DHCP
* The easiest way to use a private network is to allow the IP to be assigned via DHCP.
```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", type: "dhcp"
end
```
* This will automatically assign an IP address from the reserved address space. The IP address can be determined by using `vagrant ssh` to SSH into the machine and using the appropriate command line tool to find the IP, such as `ifconfig` or `ip addr show`.

#### Static IP
* You can also specify a static IP address for the machine. This lets you access the Vagrant managed machine using a static, known IP. The Vagrantfile for a static IP looks like this:
```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.50.4"
end
```
* It is up to the users to make sure that the static IP does not collide with any other machines on the same network.
* While you can choose any IP you would like, you _should_ use an IP from the [reserved private address space](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces). These IPs are guaranteed to never be publicly routable, and most routers actually block traffic from going to them from the outside world.
* For some operating systems, additional configuration options for the static IP address are available such as setting the default gateway or MTU.

### Public Networks
> [source](https://developer.hashicorp.com/vagrant/docs/networking/public_network)

* Vagrant public networks are less private than private networks, and the exact meaning actually varies from [provider to provider](https://developer.hashicorp.com/vagrant/docs/providers), hence the ambiguous definition. The idea is that while [private networks](https://developer.hashicorp.com/vagrant/docs/networking/private_network) should never allow the general public access to your machine, public networks can.

> [!Info] Confused?
> We kind of are, too. It is likely that public networks will be replaced by `:bridged` in a future release, since that is in general what should be done with public networks, and providers that do not support bridging generally do not have any other features that map to public networks either.

> [!Warning]
> Vagrant boxes are insecure by default and by design, featuring public passwords, insecure keypairs for SSH access, and potentially allow root access over SSH. With these known credentials, your box is easily accessible by anyone on your network. Before configuring Vagrant to use a public network, consider _all_ potential security implications and review the [default box configuration](https://developer.hashicorp.com/vagrant/docs/boxes/base) to identify potential security risks.

#### DHCP
* The easiest way to use a public network is to allow the IP to be assigned via DHCP. In this case, defining a public network is trivially easy:
```ruby
Vagrant.configure("2") do |config|
  config.vm.network "public_network"
end
```
* When DHCP is used, the IP can be determined by using `vagrant ssh` to SSH into the machine and using the appropriate command line tool to find the IP, such as `ifconfig`.

#### Static IP
* Depending on your setup, you may wish to manually set the IP of your bridged interface. To do so, add a `:ip` clause to the network definition.
```ruby
config.vm.network "public_network", ip: "192.168.0.17"
```

#### Default Network Interface
* If more than one network interface is available on the host machine, Vagrant will ask you to choose which interface the virtual machine should bridge to. A default interface can be specified by adding a `:bridge` clause to the network definition.
```ruby
config.vm.network "public_network", bridge: "en1: Wi-Fi (AirPort)"
```
* The string identifying the desired interface must exactly match the name of an available interface. If it cannot be found, Vagrant will ask you to pick from a list of available network interfaces.
* With some providers, it is possible to specify a list of adapters to bridge against:
```ruby
config.vm.network "public_network", bridge: [
  "en1: Wi-Fi (AirPort)",
  "en6: Broadcom NetXtreme Gigabit Ethernet Controller",
]
```