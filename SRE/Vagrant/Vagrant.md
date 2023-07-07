> [source](https://developer.hashicorp.com/vagrant/docs)

* [[SRE/Vagrant/CLI|CLI]]
* [[SRE/Vagrant/Vagrantfile|Vagrantfile]]
* [[SRE/Vagrant/Boxes|Boxes]]
* [[SRE/Vagrant/Provisioning|Provisioning]]
* [[SRE/Vagrant/Networking|Networking]]
* [[SRE/Vagrant/Multi-Machine|Multi-Machine]]
* [[SRE/Vagrant/Synced Folders|Synced Folders]]

> [!Question]
> **ChatGPT prompt**: What's a multi-machine machine in vagrant?
> In the context of Vagrant, a "multi-machine" configuration refers to a setup where you can define and manage multiple virtual machines within a single Vagrantfile. Vagrant is a tool that simplifies the creation and management of virtual machines for development environments.
> 
> By using the multi-machine feature, you can define and configure multiple virtual machines within a single Vagrantfile. Each virtual machine is treated as a separate entity and can have its own specific configuration, such as the choice of base box, network settings, provisioning scripts, and more.
> 
> This feature is particularly useful when you need to set up a complex development environment that involves multiple interconnected machines. For example, you may have a setup where one virtual machine serves as a web server, another as a database server, and a third as a load balancer. With Vagrant's multi-machine support, you can define and manage all these virtual machines together in a single Vagrantfile, making it easier to provision, start, stop, and interact with the entire environment.
> 
> Here's an example of a multi-machine configuration in a Vagrantfile:
> ```ruby
> Vagrant.configure("2") do |config|
>   config.vm.define "web" do |web|
>     web.vm.box = "ubuntu/bionic64"
>     web.vm.network "private_network", ip: "192.168.33.10"
>   end
> 
>   config.vm.define "db" do |db|
>     db.vm.box = "ubuntu/bionic64"
>     db.vm.network "private_network", ip: "192.168.33.20"
>   end
> end
> ```
> 
> In this example, we define two virtual machines: "web" and "db." Each machine has its own configuration block where you can specify the desired box (base image) and network settings.
> 
> With a multi-machine setup like this, you can start and manage both virtual machines together using Vagrant commands. For example, you can run `vagrant up` to start both machines simultaneously or `vagrant ssh web` to SSH into the "web" machine specifically.
> 
> The multi-machine feature in Vagrant allows you to create and manage complex development environments, making it easier to work with interconnected virtual machines.