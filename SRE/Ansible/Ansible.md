* [Ansible Documentation](https://docs.ansible.com/ansible/latest/)

#### About Ansible
* Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.
* Ansible’s main goals are **simplicity** and **ease-of-use**. It also has a strong focus on **security** and **reliability**, featuring a minimum of moving parts, usage of OpenSSH for transport (with other transports and pull modes as alternatives), and a language that is designed around *auditability by humans*–even those not familiar with the program.
* Ansible is appropriate for managing all environments, from small setups with a handful of instances to enterprise environments with many thousands of instances.
* Ansible manages machines in an *agent-less* manner. There is never a question of how to upgrade remote daemons or the problem of not being able to manage systems because daemons are uninstalled.
* Ansible is *decentralized*–it relies on your existing OS credentials to control access to remote machines. And if needed, Ansible can easily connect with *Kerberos*, *LDAP*, and other centralized authentication management systems.

## Getting started with ansible
* Ansible automates the management of remote systems and controls their desired state. A basic Ansible environment has three main components:
	* **Control Node**: A system on which Ansible is installed. You run Ansible commands such as `ansible` or `ansible-inventory` on a control node.
	* **Managed Node**: A remote system, or host, that Ansible controls.
	* **Inventory**: A list of managed nodes that are logically organized. You create an inventory on the control node to describe host deployments to Ansible.
* [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installation-guide): `python3 -m pip intsall --user ansible`

### Ansible Ping Pong
* Define hosts in `/etc/ansible/hosts`:
```
[myvirtualmachines]
192.168.1.100
192.168.1.110

[all:vars]
ansible_ssh_port=2200
```
* Add the control node's public key to the hosts and setup ssh.
* Check ansible to host connectivity by `ansible all -m ping`.
	* If the ssh ports are different, there's 3 ways:
		* `ansible --ssh-extra-args='-p 2200' ...`
			* or alternatively, `--ssh-common-args`
			* This method is advised by chatgpt to be avoided, as it apparently should be used by advanced user because it decreases security.
		* `ansible all -m ping -e 'ansible_ssh_port=2200'`
		* Or add `ansible_ssh_port=2200` to `/etc/ansible/hosts` under `[all:vars]`.

### Building an Inventory
* Inventories organize managed nodes in centralized files that provide Ansible with system information and network locations.
* Using an inventory file, Ansible can manage a large number of hosts with a single command.
* Inventories also help you use Ansible more efficiently by reducing the number of command-line options you need to specify.
* Build an Inventory:
	* Create a yaml file anywhere:
		```yaml
		virtualmachines:
		  hosts:
		    vm01:
		      ansible_host: 192.168.1.100
		    vm02:
		      ansible_host: 192.168.1.110
		```
	* Verify the inventory with `ansible-inventory -i /path/to/inv.yaml --list`
	* Check connectivity: `ansible virtualmachines -m ping -e 'ansible_ssh_port=2200'`
* [**Tips for Building Inventories**](https://docs.ansible.com/ansible/latest/getting_started/get_started_inventory.html#tips-for-building-inventories)
	* [**Use metagroups**](https://docs.ansible.com/ansible/latest/getting_started/get_started_inventory.html#use-metagroups)
	* [**Create variables**](https://docs.ansible.com/ansible/latest/getting_started/get_started_inventory.html#create-variables)

### Creating a Playbook
* Playbooks are automation blueprints, in `YAML` format, that Ansible uses to deploy and configure managed nodes.
	* **Playbook**: A list of plays that define the order in which Ansible performs operations, from top to bottom, to achieve an overall goal.
	* **Play**: An ordered list of tasks that maps to managed nodes in an inventory.
	* **Task**: A list of one or more modules that defines the operations that Ansible performs.
	* **Module**: A unit of code or binary that Ansible runs on managed nodes. Ansible modules are grouped in collections with a [Fully Qualified Collection Name (FQCN)](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-Fully-Qualified-Collection-Name-FQCN) for each module. (It's something like that of python module paths.)
* Create a playbook:
	* Create a playbook yaml file anywhere:
		```yaml
		- name: My first play
		  hosts: virtualmachines
		  tasks:
		   - name: Ping my hosts
		     ansible.builtin.ping:
		   - name: Print message
		     ansible.builtin.debug:
		       msg: Hello world
		```
	* Run the playbook: `ansible-playbook -e 'ansible_ssh_port=2200' -i inventory.yaml playbook.yaml`

## Ansible Documentation
### Using Ansible
* [[SRE/Ansible/Ansible#Getting started with ansible]]
* [[SRE/Ansible/Building Inventories|Building Inventories]]
* [[SRE/Ansible/Command Line Tools|Command Line Tools]]
* [[SRE/Ansible/Playbooks|Playbooks]]
* [[SRE/Ansible/Vault|Vault]]
* [[SRE/Ansible/Modules n Plugins|Modules n Plugins]]
* [[SRE/Ansible/Collections|Collections]]
* [[SRE/Ansible/Tips n Tricks|Tips n Tricks]]

### Table of Contents
* Ansible tips and tricks: 1500 words
* Sample Ansible setup: 2400 words
#todo tips and tricks left for when reading kubernetes