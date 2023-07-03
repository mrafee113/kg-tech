> [source](https://developer.hashicorp.com/vagrant/docs/vagrantfile)

### Overview
* The primary function of the Vagrantfile is to describe the type of machine required for a project, and how to configure and provision these machines.
* The syntax of Vagrantfiles is [Ruby](http://www.ruby-lang.org/), but knowledge of the Ruby programming language is not necessary to make modifications to the Vagrantfile, since it is mostly simple variable assignment.
* Lookup Path
	* When you run any `vagrant` command, Vagrant climbs up the directory tree looking for the first Vagrantfile it can find, starting first in the current directory.
	* This feature lets you run `vagrant` from any directory in your project.
	* You can change the starting directory where Vagrant looks for a Vagrantfile by setting the `VAGRANT_CWD` environmental variable to some other path.
* Load Order and Merging
	* An important concept to understand is how Vagrant loads Vagrantfiles. Vagrant actually loads a series of Vagrantfiles, merging the settings as it goes. This allows Vagrantfiles of varying level of specificity to override prior settings. Vagrantfiles are loaded in the order shown below. Note that if a Vagrantfile is not found at any step, Vagrant continues with the next step.
		1. Vagrantfile packaged with the [box](https://developer.hashicorp.com/vagrant/docs/boxes) that is to be used for a given machine.
		2. Vagrantfile in your Vagrant home directory (defaults to `~/.vagrant.d`). This lets you specify some defaults for your system user.
		3. Vagrantfile from the project directory. This is the Vagrantfile that you will be modifying most of the time.
		4. [Multi-machine overrides](https://developer.hashicorp.com/vagrant/docs/multi-machine) if any.
		5. [Provider-specific overrides](https://developer.hashicorp.com/vagrant/docs/providers/configuration), if any.
	* At each level, settings set will be merged with previous values. What this exactly means depends on the setting. For most settings, this means that the newer setting overrides the older one. However, for things such as defining networks, the networks are actually appended to each other. By default, you should assume that settings will override each other. If the behavior is different, it will be noted in the relevant documentation section.
	* Within each Vagrantfile, you may specify multiple `Vagrant.configure` blocks. All configurations will be merged within a single Vagrantfile in the order they're defined.

### Tips & Tricks
> [source](https://developer.hashicorp.com/vagrant/docs/vagrantfile/tips)

#### Loop Over VM Definitions
* If you want to apply a slightly different configuration to many multi-machine machines, you can use a loop to do this. For example, if you wanted to create three machines:
```ruby
(1..3).each do |i|
  config.vm.define "node-#{i}" do |node|
	node.vm.provision "shell",
	  inline: "echo hello from node #{i}"
  end
end
```

> [!Warning]
> The inner portion of multi-machine definitions and provider overrides are lazy-loaded. This can cause issues if you change the value of a variable used within the configs. For example, the loop below _does not work_:

```ruby
# THIS DOES NOT WORK!
for i in 1..3 do
  config.vm.define "node-#{i}" do |node|
    node.vm.provision "shell",
      inline: "echo hello from node #{i}"
  end
end
```
* The `for i in ...` construct in Ruby actually modifies the value of `i` for each iteration, rather than making a copy. Therefore, when you run this, every node will actually provision with the same text.
* This is an easy mistake to make, and Vagrant cannot really protect against it, so the best we can do is mention it here.

#### Overwrite host locale in SSH session
* Usually, host locale environment variables are passed to guest. It may cause failures if the guest software do not support host locale. One possible solution is override locale in the `Vagrantfile`:
```ruby
ENV["LC_ALL"] = "en_US.UTF-8"

Vagrant.configure("2") do |config|
  # ...
end
```
* The change is only visible within the `Vagrantfile`.

### `config.vm`
> [source](https://developer.hashicorp.com/vagrant/docs/vagrantfile/machine_settings)

* The settings within `config.vm` modify the configuration of the machine that Vagrant manages.
* `config.vm.allow_fstab_modification` (boolean) : If true, will add fstab entries for synced folders. If false, no modifications to fstab will be made by Vagrant. Note, this may mean that folders will not be automatically mounted on machine reboot. Defaults to true.
* `config.vm.allow_hosts_modification` (boolean) : If false, will prevent Vagrant from writing to `/etc/hosts`. Defaults to true.
* `config.vm.base_address` (string) : The IP address to be assigned to the default NAT interface on the guest. _Support for this option is provider dependent._
* `config.vm.boot_timeout` (integer) : The time in seconds that Vagrant will wait for the machine to boot and be accessible. By default this is 300 seconds.
* `config.vm.box` (string) : This configures what [box](https://developer.hashicorp.com/vagrant/docs/boxes) the machine will be brought up against. The value here should be the name of an installed box or a shorthand name of a box in [HashiCorp's Vagrant Cloud](https://developer.hashicorp.com/vagrant/vagrant-cloud).
* `config.vm.box_check_update` (boolean) : If true, Vagrant will check for updates to the configured box on every `vagrant up`. If an update is found, Vagrant will tell the user. By default this is true. Updates will only be checked for boxes that properly support updates (boxes from [HashiCorp's Vagrant Cloud](https://developer.hashicorp.com/vagrant/vagrant-cloud) or some other versioned box).
* `config.vm.box_download_options` (map) : A map of extra download options to pass to the downloader. For example, a path to a key that the downloader should use could be specified as `{key: "<path/to/key>"}`. The keys should be options supported by `curl` using the unshortened form of the flag. For example, use `append` instead of `a`. To pass a curl option that does not accept a value, include the option in the map with the value `true`. For example specify the `--fail` flag as `{fail: true}`.
* `config.vm.box_download_insecure` (boolean) : If true, then SSL certificates from the server will not be verified. By default, if the URL is an HTTPS URL, then SSL certs will be verified.
* `config.vm.box_version` (string) : The version of the box to use. This defaults to ">= 0" (the latest version available). This can contain an arbitrary list of constraints, separated by commas, such as: `>= 1.0, < 1.5`. When constraints are given, Vagrant will use the latest available box satisfying these constraints.
* `config.vm.hostname` (string) : The hostname the machine should have. Defaults to nil. If nil, Vagrant will not manage the hostname. If set to a string, the hostname will be set on boot. If set, Vagrant will update `/etc/hosts` on the guest with the configured hostname.
* `config.vm.network` : Configures [networks](https://developer.hashicorp.com/vagrant/docs/networking) on the machine. Please see the networking page for more information.
* `config.vm.provider` : Configures [provider-specific configuration](https://developer.hashicorp.com/vagrant/docs/providers/configuration), which is used to modify settings which are specific to a certain [provider](https://developer.hashicorp.com/vagrant/docs/providers). If the provider you are configuring does not exist or is not setup on the system of the person who runs `vagrant up`, Vagrant will ignore this configuration block. This allows a Vagrantfile that is configured for many providers to be shared among a group of people who may not have all the same providers installed.
* `config.vm.provision` : Configures [provisioners](https://developer.hashicorp.com/vagrant/docs/provisioning) on the machine, so that software can be automatically installed and configured when the machine is created. Please see the page on provisioners for more information on how this setting works.
* `config.vm.usable_port_range` (range) : A range of ports Vagrant can use for handling port collisions and such. Defaults to `2200..2250`.

### `config.ssh`
> [source](https://developer.hashicorp.com/vagrant/docs/vagrantfile/ssh_settings)

* The settings within `config.ssh` relate to configuring how Vagrant will access your machine over SSH. As with most Vagrant settings, the defaults are typically fine, but you can fine tune whatever you would like.
* `config.ssh.config` (string) : Path to a custom ssh_config file to use for configuring the SSH connections.
* `config.ssh.extra_args` (array_of_string) : This settings value is passed directly into the ssh executable. This allows you to pass any arbitrary commands to do things such as reverse tunneling down into the SSH program. These options can either be single flags set as strings such as `"-6"` for IPV6 or an array of arguments such as `["-L", "8008:localhost:80"]` for enabling a tunnel from host port 8008 to port 80 on guest. **Note:** This option only affects the `ssh` command or instances where the SSH executable is invoked (non-interactive SSH connections use the internal SSH communicator which is unaffected by this setting).
* `config.ssh.forward_env` (array_of_strings) : An array of host environment variables to forward to the guest. If you are familiar with OpenSSH, this corresponds to the `SendEnv` parameter.
	* `config.ssh.forward_env = ["CUSTOM_VAR"]`
* `config.ssh.guest_port` (integer) : The port on the guest that SSH is running on. This is used by some providers to detect forwarded ports for SSH. For example, if this is set to 22 (the default), and Vagrant detects a forwarded port to port 22 on the guest from port 4567 on the host, Vagrant will attempt to use port 4567 to talk to the guest if there is no other option.
* `config.ssh.host` (string) : The hostname or IP to SSH into. By default this is empty, because the provider usually figures this out for you.
* `config.ssh.insert_key` (boolean) : By default or if set to `true`, Vagrant will automatically insert a keypair to use for SSH, replacing Vagrant's default insecure key inside the machine if detected. If you already use private keys for authentication to your guest, or are relying on the default insecure key, this option will not be used. If set to `false`, Vagrant will not automatically add a keypair to the guest.
* `config.ssh.keep_alive` (boolean) : If `true`, this setting SSH will send keep-alive packets every 5 seconds by default to keep connections alive.
* `config.ssh.keys_only` (boolean) : Only use Vagrant-provided SSH private keys (do not use any keys stored in ssh-agent). The default value is `true`.
* `config.ssh.password` (string) : This sets a password that Vagrant will use to authenticate the SSH user. Note that Vagrant recommends you use key-based authentication rather than a password (see `private_key_path`) below. If you use a password, Vagrant will automatically insert a keypair if `insert_key` is true.
* `config.ssh.port` (integer) : The port to SSH into. By default this is port 22.
* `config.ssh.private_key_path` (string, array_of_strings) : The path to the private key to use to SSH into the guest machine. By default this is the insecure private key that ships with Vagrant, since that is what public boxes use. If you make your own custom box with a custom SSH key, this should point to that private key. You can also specify multiple private keys by setting this to be an array. This is useful, for example, if you use the default private key to bootstrap the machine, but replace it with perhaps a more secure key later.
* `config.ssh.shell` (string) : The shell to use when executing SSH commands from Vagrant. By default this is `bash -l`.
* `config.ssh.sudo_command` (string) : The command to use when executing a command with `sudo`. This defaults to `sudo -E -H %c`. The `%c` will be replaced by the command that is being executed.
* `config.ssh.username` (string) : This sets the username that Vagrant will SSH as by default. Providers are free to override this if they detect a more appropriate user. By default this is "vagrant", since that is what most public boxes are made as.

### `config.vagrant`
> [source](https://developer.hashicorp.com/vagrant/docs/vagrantfile/vagrant_settings)

* The settings within `config.vagrant` modify the behavior of Vagrant itself.
* `config.vagrant.plugins` (string, array, hash) : Define plugin, list of plugins, or definition of plugins to install for the local project. Vagrant will require these plugins be installed and available for the project. If the plugins are not available, it will attempt to automatically install them into the local project.
	* When requiring a single plugin, a string can be provided:
		* `config.vagrant.plugins = "vagrant-plugin"`
	* If multiple plugins are required, they can be provided as an array:
		* `config.vagrant.plugins = ["vagrant-plugin", "vagrant-other-plugin"]`
	* Plugins can also be defined as a Hash, which supports setting extra options for the plugins. When a Hash is used, the key is the name of the plugin, and the value is a Hash of options for the plugin. For example, to set an explicit version of a plugin to install:
		* `config.vagrant.plugins = {"vagrant-scp" => {"version" => "1.0.0"}}`
	* options
		* `entry_point` : Path for Vagrant to load plugin
		* `sources` : Custom sources for downloading plugin
		* `version` : Version constraint for plugin