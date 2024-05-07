> [source](https://developer.hashicorp.com/vagrant/docs/boxes)

### Overview
* Boxes are the package format for Vagrant environments.
* You specify a box environment and operating configurations in your [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile).

> [!Note]
> Boxes require a provider, a virtualization product, to operate. Before you can use a box, ensure that you have properly installed a supported [provider](https://developer.hashicorp.com/vagrant/docs/providers).
> - VirtualBox, Docker, Hyper-V, VMWare, etc...

* To find boxes, explore the [public Vagrant box catalog](https://vagrantcloud.com/boxes/search) for a box that matches your use case. The catalog contains most major operating systems as bases, as well as specialized boxes to get you started with common configurations such as LAMP stacks, Ruby, and Python.
* A common misconception is that a namespace like "ubuntu" represents the official space for Ubuntu boxes. This is untrue. Namespaces on Vagrant Cloud behave very similarly to namespaces on GitHub. Just as GitHub's support team is unable to assist with issues in someone's repository, HashiCorp's support team is unable to assist with third-party published boxes.
* For other base operating system environments, we recommend the [Bento boxes](https://vagrantcloud.com/bento). The Bento boxes are [open source](https://github.com/chef/bento) and built for a number of providers including VMware, VirtualBox, and Parallels. There are a variety of operating systems and versions available.
* It is often a point of confusion but Canonical, the company that makes the Ubuntu operating system, publishes boxes under the "ubuntu" namespace on Vagrant Cloud. These boxes only support VirtualBox.
* If you are unable to find a box that meets your specific use case, you can create one. We recommend that you first create a [base box](https://developer.hashicorp.com/vagrant/docs/boxes/base) to have a clean slate to start from when you build future development environments.
* Learn more about [box formats](https://developer.hashicorp.com/vagrant/docs/boxes/format) to get started.
