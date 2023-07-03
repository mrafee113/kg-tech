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