> [source](https://developer.hashicorp.com/vagrant/docs/provisioning)

### Overview
* Provisioners in Vagrant allow you to automatically install software, alter configurations, and more on the machine as part of the `vagrant up` process.
* This is useful since [boxes](https://developer.hashicorp.com/vagrant/docs/boxes) typically are not built _perfectly_ for your use case. Of course, if you want to just use `vagrant ssh` and install the software by hand, that works. But by using the provisioning systems built-in to Vagrant, it automates the process so that it is repeatable. Most importantly, it requires no human interaction, so you can `vagrant destroy` and `vagrant up` and have a fully ready-to-go work environment with a single command. Powerful.
* Vagrant gives you multiple options for provisioning the machine, from simple shell scripts to more complex, industry-standard configuration management systems.
* Provisioning happens at certain points during the lifetime of your Vagrant environment:
	* On the first `vagrant up` that creates the environment, provisioning is run. If the environment was already created and the up is just resuming a machine or booting it up, they will not run unless the `--provision` flag is explicitly provided.
	* When `vagrant provision` is used on a running environment.
	* When `vagrant reload --provision` is called. The `--provision` flag must be present to force provisioning.
* You can also bring up your environment and explicitly _not_ run provisioners by specifying `--no-provision`.

### Basic Usage
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/basic_usage)

* While Vagrant offers multiple options for how you are able to provision your machine, there is a standard usage pattern as well as some important points common to all provisioners that are important to know.

#### Options
* Every Vagrant provisioner accepts a few base options. The only required option is what type a provisioner is.
* `name` (string) : The name of the provisioner. Note: if no `type` option is given, this option _must_ be the type of provisioner it is. If you wish to give it a different name you must also set the `type` option to define the kind of provisioner.
* `type` (string) : The class of provisioner to configure. (i.e. `"shell"` or `"file"`)

#### Configuration
* First, every provisioner is configured within your [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile) using the `config.vm.provision` method call.
	```ruby
	Vagrant.configure("2") do |config|
	  # ... other configuration
	
	  config.vm.provision "shell", inline: "echo hello"
	end
	```
* Every provisioner has a type, such as `"shell"`, used as the first parameter to the provisioning configuration. Following that is basic key/value for configuring that specific provisioner. Instead of basic key/value, you can also use a Ruby block for a syntax that is more like variable assignment.
* The following is the same as the previous one:
	```ruby
	Vagrant.configure("2") do |config|
	  # ... other configuration
	
	  config.vm.provision "shell" do |s|
	    s.inline = "echo hello"
	  end
	end
	```
* The benefit of the block-based syntax is that with more than a couple options it can greatly improve readability. Additionally, some provisioners, like the Chef provisioner, have special methods that can be called within that block to ease configuration that cannot be done with the key/value approach, or you can use this syntax to pass arguments to a shell script.

#### Running
* Provisioners are run in three cases: the initial `vagrant up`, `vagrant provision`, and `vagrant reload --provision`.
* A `--no-provision` flag can be passed to `up` and `reload` if you do not want to run provisioners. Likewise, you can pass `--provision` to force provisioning.
* The `--provision-with` flag can be used if you only want to run a specific provisioner if you have multiple provisioners specified. For example, if you have a shell and Puppet provisioner and only want to run the shell one, you can do `vagrant provision --provision-with shell`. The arguments to `--provision-with` can be the provisioner type (such as "shell") or the provisioner name (such as "bootstrap" from above).

### File Provisioner
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/file)

* The Vagrant file provisioner allows you to upload a file or directory from the host machine to the guest machine.
	```ruby
	Vagrant.configure("2") do |config|
	  # ... other configuration
	
	  config.vm.provision "file", source: "~/path/to/host/folder-or-file", destination: "$HOME/remote/newfolder-or-newfile"
	end
	```
* Note that, unlike with synced folders, files or directories that are uploaded will not be kept in sync.
* The file uploads by the file provisioner are done as the _SSH_ user. This is important since these users generally do not have elevated privileges on their own. If you want to upload files to locations that require elevated privileges, we recommend uploading them to temporary locations and then using the [shell provisioner](https://developer.hashicorp.com/vagrant/docs/provisioning/shell) to move them into place.
* options
	* `source` (string) : Is the local path of the file or directory to be uploaded.
	* `destination` (string) : Is the remote path on the guest machine where the source will be uploaded to. The file/folder is uploaded as the SSH user over SCP, so this location must be writable to that user. The SSH user can be determined by running `vagrant ssh-config`, and defaults to "vagrant". Variables like `$HOME` are expanded by Vagrant, not by guest.

### Shell Provisioner
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/shell)

* The Vagrant Shell provisioner allows you to upload and execute a script within the guest machine.
* Shell provisioning is ideal for users new to Vagrant who want to get up and running quickly and provides a strong alternative for users who are not comfortable with a full configuration management system such as Chef or Puppet.
* For POSIX-like machines, the shell provisioner executes scripts with SSH.
* options
	* One of `inline` or `path` is required:
		* `inline` (string) : Specifies a shell command inline to execute on the remote machine. See the [inline scripts](https://developer.hashicorp.com/vagrant/docs/provisioning/shell#inline-scripts) section below for more information.
		* `path` (string) : Path to a shell script to upload and execute. It can be a script relative to the project Vagrantfile or a remote script (like a [gist](https://gist.github.com/)).
	* optional args:
		* `args` (string or array) : Arguments to pass to the shell script when executing it as a single string. These arguments must be written as if they were typed directly on the command line, so be sure to escape characters, quote, etc. as needed. You may also pass the arguments in using an array. In this case, Vagrant will handle quoting for you.
		* `env` (hash) : List of key-value pairs to pass in as environment variables to the script. Vagrant will handle quoting for environment variable values, but the keys remain untouched.
		* `name` (string) : This value will be displayed in the output so that identification by the user is easier when many shell provisioners are present.
		* `privileged` (boolean) : Specifies whether to execute the shell script as a privileged user or not (`sudo`). By default this is "true".
		* `reboot` (boolean) : Reboot the guest. This requires the guest to have a reboot capability implemented.
		* `reset` (boolean) : Reset the communicator to the machine after completion. This is useful when a shell may need to be reloaded.
		* `sensitive` (boolean) : Marks the Hash values used in the `env` option as sensitive and hides them from output. By default this is "false".
		* `upload_path` (string) : Is the remote path where the shell script will be uploaded to. The script is uploaded as the SSH user over SCP, so this location must be writable to that user. By default this is "/tmp/vagrant-shell".

```ruby
Vagrant.configure("2") do |config|
  config.vm.provision "shell",
    inline: "echo Hello, World"
end
```
```ruby
$script = <<-SCRIPT
echo I am provisioning...
date > /etc/vagrant_provisioned_at
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $script
end
```
```ruby
$script = <<-'SCRIPT'
echo "These are my \"quotes\"! I am provisioning my guest."
date > /etc/vagrant_provisioned_at
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $script
end
```
```ruby
Vagrant.configure("2") do |config|
  config.vm.provision "shell" do |s|
    s.inline = "echo $1"
    s.args   = "'hello, world!'"
  end
end
```
```ruby
Vagrant.configure("2") do |config|
  config.vm.provision "shell" do |s|
    s.inline = "echo $1"
    s.args   = ["hello, world!"]
  end
end
```
* To run a script already available on the guest you can use an inline script to invoke the remote script on the guest.
```ruby
Vagrant.configure("2") do |config|
  config.vm.provision "shell",
    inline: "/bin/sh /path/to/the/script/already/on/the/guest.sh"
end
```

### Ansible Intro
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_intro)

* The information below is applicable to both Vagrant Ansible provisioners:
	- [`ansible`](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible), where Ansible is executed on the **Vagrant host**
	- [`ansible_local`](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_local), where Ansible is executed on the **Vagrant guest**
- The list of common options for these two provisioners is documented in a [separate documentation page](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common) (or [[SRE/Vagrant/Provisioning#Common Ansible Options|down below]]).
- This documentation page will not go into how to use Ansible or how to write Ansible playbooks, since Ansible is a complete deployment and configuration management system that is beyond the scope of Vagrant documentation.
- To learn more about Ansible, please consult the [Ansible Documentation Site](https://docs.ansible.com/).

#### The Inventory File
* When using Ansible, it needs to know on which machines a given playbook should run. It does this by way of an [inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory) file which lists those machines. In the context of Vagrant, there are two ways to approach working with inventory files.

##### Auto-Generated Inventory
* The first and simplest option is to not provide one to Vagrant at all. Vagrant will generate an inventory file encompassing all of the virtual machines it manages, and use it for provisioning machines.
* example with `ansible` provisioner:
```ini
# Generated by Vagrant

default ansible_host=127.0.0.1 ansible_port=2200 ansible_user='vagrant' ansible_ssh_private_key_file='/home/.../.vagrant/machines/default/virtualbox/private_key'
```
* Note that the generated inventory file is stored as part of your local Vagrant environment in `.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory`.
* example with `ansible_local` provisioner:
```ini
# Generated by Vagrant

default ansible_connection=local
```
* Note that the generated inventory file is uploaded to the guest VM in a subdirectory of `tmp_path`, e.g. `/tmp/vagrant-ansible/inventory/vagrant_ansible_local_inventory`.

###### Host Variables
* With this configuration example:
```ruby
Vagrant.configure("2") do |config|
  config.vm.define "host1"
  config.vm.define "host2"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.host_vars = {
      "host1" => {"http_port" => 80,
                  "maxRequestsPerChild" => 808},
      "host2" => {"http_port" => 303,
                  "maxRequestsPerChild" => 909}
    }
  end
end
```
* Vagrant would generate the following inventory file:
```ini
# Generated by Vagrant

host1 ansible_host=... http_port=80 maxRequestsPerChild=808
host2 ansible_host=... http_port=303 maxRequestsPerChild=909
```

###### Groups and Group Variables
* With this configuration example:
```ruby
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.define "machine1"
  config.vm.define "machine2"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.groups = {
      "group1" => ["machine1"],
      "group2" => ["machine2"],
      "group3" => ["machine[1:2]"],
      "group4" => ["other_node-[a:d]"], # silly group definition
      "all_groups:children" => ["group1", "group2"],
      "group1:vars" => {"variable1" => 9,
                        "variable2" => "example"}
    }
  end
end
```
* Vagrant would generate the following inventory file:
```ini
# Generated by Vagrant

machine1 ansible_host=127.0.0.1 ansible_port=2200 ansible_user='vagrant' ansible_ssh_private_key_file='/home/.../.vagrant/machines/machine1/virtualbox/private_key'
machine2 ansible_host=127.0.0.1 ansible_port=2222 ansible_user='vagrant' ansible_ssh_private_key_file='/home/.../.vagrant/machines/machine2/virtualbox/private_key'

[group1]
machine1

[group2]
machine2

[group3]
machine[1:2]

[group4]
other_node-[a:d]

[all_groups:children]
group1
group2

[group1:vars]
variable1=9
variable2=example
```

* Notes
	* Unmanaged machines and undefined groups are not added to the inventory, to avoid useless Ansible errors (e.g. unreachable host or undefined child group)
		* For example, machine3 and group3 in the example below would not be added to the generated inventory file:
			```ruby
			ansible.groups = {
			  "group1" => ["machine1"],
			  "group2" => ["machine2", "machine3"],
			  "all_groups:children" => ["group1", "group2", "group3"]
			}
			```

##### Static Inventory
* The second option is for situations where you would like to have more control over the inventory management.
* With the [`inventory_path`](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common#inventory_path) option, you can reference a specific inventory resource (e.g. a static inventory file, a [`dynamic inventory script`](https://docs.ansible.com/intro_dynamic_inventory.html) or even [`multiple inventories stored in the same directory`](https://docs.ansible.com/intro_dynamic_inventory.html#using-multiple-inventory-sources)). Vagrant will then use this inventory information instead of generating it.
* Notes
	* The machine names in `Vagrantfile` and `ansible.inventory_path` files should correspond, unless you use `ansible.limit` option to reference the correct machines.
	* The `ansible.inventory_path` option by default is only scoped to apply to a single guest in the inventory file, and does not apply to all defined guests. To allow access to all available machines in the inventory, it is necessary to set `ansible.limit = "all"`.
	* The SSH host addresses (and ports) must obviously be specified twice, in `Vagrantfile` and `ansible.inventory_path` files.
	* Sharing hostnames across Vagrant host and guests might be a good idea (e.g. with some Ansible configuration task, or with a plugin like [`vagrant-hostmanager`](https://github.com/smdahlen/vagrant-hostmanager)).

##### The Ansible Configuration File
* Certain settings in Ansible are (only) adjustable via a [configuration file](https://docs.ansible.com/intro_configuration.html), and you might want to ship such a file in your Vagrant project.
* When shipping an Ansible configuration file it is good to know that:
	* as of Ansible 1.5, the lookup order is the following:
		* any path set as `ANSIBLE_CONFIG` environment variable
		* `ansible.cfg` in the runtime working directory
		* `.ansible.cfg` in the user home directory
		* `/etc/ansible/ansible.cfg`
	* Ansible commands don't look for a configuration file relative to the playbook file location (e.g. in the same directory)
	* an `ansible.cfg` file located in the same directory as your `Vagrantfile` will be used by default.
	* it is also possible to reference any other location with the [`config_file`](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common#config_file) provisioner option. In this case, Vagrant will set the `ANSIBLE_CONFIG` environment variable accordingly.

### Ansible Provisioner
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible)

* The Vagrant Ansible provisioner allows you to provision the guest using Ansible playbooks by executing `ansible-playbook` from the Vagrant host.

#### Setup Requirements
- **[Install Ansible](https://docs.ansible.com/intro_installation.html#installing-the-control-machine) on your Vagrant host**.
- Your Vagrant host should ideally provide a recent version of OpenSSH that [supports ControlPersist](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#controlpersist-and-paramiko).
- If installing Ansible directly on the Vagrant host is not an option in your development environment, you might be looking for the [Ansible Local provisioner](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_local) ([[SRE/Vagrant/Provisioning#Ansible Local Provisioner|below]]) alternative.

#### Usage
* Simplest configuration: To run Ansible against your Vagrant guest, the basic `Vagrantfile` configuration looks like:
```ruby
Vagrant.configure("2") do |config|

  #
  # Run Ansible from the Vagrant Host
  #
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end

end
```

#### Options
* In addition to the options listed below, this provisioner supports the [common options for both Ansible provisioners](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common) ([[SRE/Vagrant/Provisioning#Common Ansible Options|below]]).
* `ask_become_pass` (boolean) : require Ansible to [prompt for a password](https://docs.ansible.com/intro_getting_started.html#remote-connection-information) when switching to another user with the [become/sudo mechanism](http://docs.ansible.com/ansible/become.html). Default=`false`
* `force_remote_user` (boolean)
	* require Vagrant to set the `ansible_ssh_user` setting in the generated inventory, or as an extra variable when a static inventory is used. All the Ansible `remote_user` parameters will then be overridden by the value of `config.ssh.username` of the [Vagrant SSH Settings](https://developer.hashicorp.com/vagrant/docs/vagrantfile/ssh_settings).
	* If this option is set to `false` Vagrant will set the Vagrant SSH username as a default Ansible remote user, but `remote_user` parameters of your Ansible plays or tasks will still be taken into account and thus override the Vagrant configuration.
	* Default=`true`
* `host_key_checking` (boolean) : require Ansible to [enable SSH host key checking](https://docs.ansible.com/intro_getting_started.html#host-key-checking). Default=`false`
* `raw_ssh_args` (array of strings) : require Ansible to apply a list of OpenSSH client options.
	* Example: `['-o ControlMaster=no']`.
	* It is an unsafe wildcard that can be used to pass additional SSH settings to Ansible via `ANSIBLE_SSH_ARGS` environment variable, overriding any other SSH arguments (e.g. defined in an [`ansible.cfg` configuration file](https://docs.ansible.com/intro_configuration.html#ssh-args)).

#### Tips and Tricks
##### Ansible Parallel Execution
* Vagrant is designed to provision [multi-machine environments](https://developer.hashicorp.com/vagrant/docs/multi-machine) in sequence, but the following configuration pattern can be used to take advantage of Ansible parallelism:
```ruby
# Vagrant 1.7+ automatically inserts a different
# insecure keypair for each new VM created. The easiest way
# to use the same keypair for all the machines is to disable
# this feature and rely on the legacy insecure key.
# config.ssh.insert_key = false
#
# Note:
# As of Vagrant 1.7.3, it is no longer necessary to disable
# the keypair creation when using the auto-generated inventory.

N = 3
(1..N).each do |machine_id|
  config.vm.define "machine#{machine_id}" do |machine|
    machine.vm.hostname = "machine#{machine_id}"
    machine.vm.network "private_network", ip: "192.168.77.#{20+machine_id}"

    # Only execute once the Ansible provisioner,
    # when all the machines are up and ready.
    if machine_id == N
      machine.vm.provision :ansible do |ansible|
        # Disable default limit to connect to all the machines
        ansible.limit = "all"
        ansible.playbook = "playbook.yml"
      end
    end
  end
end
```

> [!Tip]
> If you apply this parallel provisioning pattern with a static Ansible inventory, you will have to organize the things so that [all the relevant private keys are provided to the `ansible-playbook` command](https://github.com/hashicorp/vagrant/pull/5765#issuecomment-120247738). The same kind of considerations applies if you are using multiple private keys for a same machine (see [`config.ssh.private_key_path` SSH setting](https://developer.hashicorp.com/vagrant/docs/vagrantfile/ssh_settings)).

### Ansible Local Provisioner
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_local)

* The Vagrant Ansible Local provisioner allows you to provision the guest using [Ansible](http://ansible.com/) playbooks by executing `ansible-playbook` directly on the guest machine.

#### Setup Requirements
* The main advantage of the Ansible Local provisioner in comparison to the Ansible (remote) provisioner is that it does not require any additional software on your Vagrant host.
* On the other hand, [Ansible must obviously be installed](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) on your guest machine(s).

> [!Note]
> By default, Vagrant will try to automatically install Ansible if it is not yet present on the guest machine (see the `install` option below for more details).

#### Usage
* The Ansible Local provisioner requires that all the Ansible Playbook files are available on the guest machine, at the location referred by the `provisioning_path` option. Usually these files are initially present on the host machine (as part of your Vagrant project), and it is quite easy to share them with a Vagrant [[SRE/Vagrant/Synced Folders|Synced Folders]].
* Simplest configuration: To run Ansible from your Vagrant guest, the basic `Vagrantfile` configuration looks like:
	```ruby
	Vagrant.configure("2") do |config|
	  # Run Ansible from the Vagrant VM
	  config.vm.provision "ansible_local" do |ansible|
	    ansible.playbook = "playbook.yml"
	  end
	end
	```
	* requirements:
		* The `playbook.yml` file is stored in your Vagrant's project home directory.
		* The [default shared directory](https://developer.hashicorp.com/vagrant/docs/synced-folders/basic_usage) is enabled (`.` → `/vagrant`).

#### Options
* This section lists the specific options for the Ansible Local provisioner. In addition to the options listed below, this provisioner supports the [[SRE/Vagrant/Provisioning#Common Ansible Options|common options for both Ansible provisioners]].
* `install` (boolean)
	* Try to automatically install Ansible on the guest system.
	* Default=`true`
	* Vagrant will try to install (or upgrade) Ansible when one of these conditions are met:
		* Ansible is not installed (or cannot be found).
		* The `version` option is set to "latest".
> [!Attention]
> There is no guarantee that this automated installation will replace a custom Ansible setup, that might be already present on the Vagrant box.
* `install_mode` (`:default`, `:pip`, or `:pip_args_only`)
	* Select the way to automatically install Ansible on the guest system.
	* The default value of `install_mode` is `:default`, and any invalid value for this option will silently fall back to the default value.
	* `:default` : Ansible is installed from the operating system package manager. This mode doesn't support `version` selection. For many platforms (e.g Debian, FreeBSD, OpenSUSE) the official package repository is used, except for the following Linux distributions:
		* On Ubuntu-like systems, the latest Ansible release is installed from the `ppa:ansible/ansible` repository. The compatibility is maintained only for active long-term support (LTS) versions.
		* On RedHat-like systems, the latest Ansible release is installed from the [EPEL](http://fedoraproject.org/wiki/EPEL) repository.
	* `:pip` : Ansible is installed from [PyPI](https://pypi.python.org/pypi) with [pip](https://pip.pypa.io/) package installer. With this mode, Vagrant will systematically try to [install the latest pip version](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py). With the `:pip` mode you can optionally install a specific Ansible release by setting the [`version`](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common#version) option.
		* example:
			```ruby
			config.vm.provision "ansible_local" do |ansible|
			  ansible.playbook = "playbook.yml"
			  ansible.install_mode = "pip"
			  ansible.version = "2.2.1.0"
			end
			```
		* With this configuration, Vagrant will install `pip` and then execute the command
		* `sudo pip install --upgrade ansible==2.2.1.0`
		* As-is `pip` is installed if needed via a default command which looks like
		* `curl https://bootstrap.pypa.io/get-pip.py | sudo python`
		* This can be problematic in certain scenarios, for example, when behind a proxy. It is possible to override this default command by providing an explicit command to run as part of the config using `pip_install_cmd`. For example:
			```ruby
			config.vm.provision "ansible_local" do |ansible|
			  ansible.playbook = "playbook.yml"
			  ansible.install_mode = "pip"
			  ansible.pip_install_cmd = "https_proxy=http://your.proxy.server:port curl -s https://bootstrap.pypa.io/get-pip.py | sudo https_proxy=http/your.proxy.server:port python"
			  ansible.version = "2.2.1.0"
			end
			```
		* If `pip_install_cmd` is not provided in the config, then `pip` is installed via the default command.
	* `:pip_args_only` : This mode is very similar to the `:pip` mode, with the difference that in this case no pip arguments will be automatically set by Vagrant.
		* Example:
			```ruby
			config.vm.provision "ansible_local" do |ansible|
			  ansible.playbook = "playbook.yml"
			  ansible.install_mode = "pip_args_only"
			  ansible.pip_args = "-r /vagrant/requirements.txt"
			end
			```
		* With this configuration, Vagrant will install `pip` and then execute the command
		* `sudo pip install -r /vagrant/requirements.txt`
* `pip_args` (string) : When Ansible is installed via pip, this option allows the definition of additional pip arguments to be passed along on the command line. By default, this option is not set.
* `provisioning_path` (string) : An absolute path on the guest machine where the Ansible files are stored. The `ansible-galaxy` and `ansible-playbook` commands are executed from this directory. This is the location to place an [`ansible.cfg`](http://docs.ansible.com/ansible/intro_configuration.html) file, in case you need it. Default=`/vagrant`
* `tmp_path` (string) : An absolute path on the guest machine where temporary files are stored by the Ansible Local provisioner. Default=`/tmp/vagrant-ansible`

### Common Ansible Options
> [source](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_common)

* These options get passed to the `ansible-playbook` command that ships with Ansible, either via command line arguments or environment variables, depending on Ansible own capabilities.
* `become` (boolean) : Perform all the Ansible playbook tasks [as another user](https://docs.ansible.com/ansible/latest/become.html), different from the user used to log into the guest system. Default=`false`
* `become_user` (string) :  Set the default username to be used by the Ansible `become` [privilege escalation](https://docs.ansible.com/ansible/latest/become.html) mechanism. By default this option is not set, and therefore the Ansible default `root` will be used.
* `config_file` (string) : The path to an [Ansible Configuration file](https://docs.ansible.com/ansible/latest/intro_configuration.html). By default, this option is not set, and Ansible will [search for a possible configuration file in some default locations](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_intro#the-ansible-configuration-file).
* `extra_vars` (string or hash) : Pass additional variables (with highest priority) to the playbook. This parameter can be a path to a JSON or YAML file, or a hash.
	* example:
		```ruby
		ansible.extra_vars = {
		  ntp_server: "pool.ntp.org",
		  nginx: {
		    port: 8008,
		    workers: 4
		  }
		}
		```
	* These variables take the highest precedence over any other variables.
* `groups` (hash) : Set of inventory groups to be included in the [auto-generated inventory file](https://developer.hashicorp.com/vagrant/docs/provisioning/ansible_intro).
	* example:
		```ruby
		ansible.groups = {
		  "web" => ["vm1", "vm2"],
		  "db"  => ["vm3"]
		}
		```
	* example with [group variables](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#assigning-a-variable-to-many-machines-group-variables):
		```ruby
		ansible.groups = {
		  "atlanta" => ["host1", "host2"],
		  "atlanta:vars" => {"ntp_server" => "ntp.atlanta.example.com",
		                     "proxy" => "proxy.atlanta.example.com"}
		}
		```
	* Notes
		* Alphanumeric patterns are not supported (e.g. `db-[a:f]`, `vm[01:10]`).
		* This option has no effect when the `inventory_path` option is defined.
* `host_vars` (hash) :  Set of inventory host variables to be included in the [auto-generated inventory file](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#assigning-a-variable-to-one-machine-host-variables).
	* example:
		```ruby
		ansible.host_vars = {
		  "host1" => {"http_port" => 80,
		              "maxRequestsPerChild" => 808,
		              "comments" => "text with spaces"},
		  "host2" => {"http_port" => 303,
		              "maxRequestsPerChild" => 909}
		}
		```
	* Note: This option has no effect when the `inventory_path` option is defined.
* `inventory_path` (string) : The path to an Ansible inventory resource (e.g. a [static inventory file](https://docs.ansible.com/ansible/latest/intro_inventory.html), a [dynamic inventory script](https://docs.ansible.com/ansible/latest/intro_dynamic_inventory.html) or even [multiple inventories stored in the same directory](https://docs.ansible.com/ansible/latest/intro_dynamic_inventory.html#using-multiple-inventory-sources)). By default, this option is disabled and Vagrant generates an inventory based on the `Vagrantfile` information.
* `limit` (string or array of strings) : Set of machines or groups from the inventory file to further control which hosts [are affected](https://docs.ansible.com/ansible/latest/glossary.html#limit-groups).
	* The default value is set to the machine name (taken from `Vagrantfile`) to ensure that `vagrant provision` command only affect the expected machine.
	* Setting `limit = "all"` can be used to make Ansible connect to all machines from the inventory file.
* `playbook_command` (string) : The command used to run playbooks. Default=`ansible-playbook`
* `raw_arguments` (array of strings) : a list of additional `ansible-playbook` arguments.
	* It is an unsafe wildcard that can be used to apply Ansible options that are not (yet) supported by this Vagrant provisioner. As of Vagrant 1.7, `raw_arguments` has the highest priority and its values can potentially override or break other Vagrant settings.
	* e.g. `['--check', '-M', '/my/modules']`
	* e.g. `["--connection=paramiko", "--forks=10"]`
> [!Attention]
> The `ansible` provisioner does not support whitespace characters in `raw_arguments` elements. Therefore don't write something like `["-c paramiko"]`, which will result with an invalid `" paramiko"` parameter value.
* `skip_tags` (string or array of strings) : Only plays, roles and tasks that [*do not match* these values will be executed](https://docs.ansible.com/ansible/latest/playbooks_tags.html).
* `start_at_task` (string) : The task name where the [playbook execution will start](https://docs.ansible.com/ansible/latest/playbooks_startnstep.html#start-at-task).
* `tags` (string or array of strings) : Only plays, roles and tasks [tagged with these values will be executed](https://docs.ansible.com/ansible/latest/playbooks_tags.html).
* `verbose` (boolean or string) : Set Ansible's verbosity to obtain detailed logging
	* Default=`false` (minimal verbosity)
	* `true` -> `v`
	* `-vvv` -> `vvv`
	* `vvvv`
	* Note that when the `verbose` option is enabled, the `ansible-playbook` command used by Vagrant will be displayed.