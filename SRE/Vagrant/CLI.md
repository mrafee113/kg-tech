> [source](https://developer.hashicorp.com/vagrant/docs/cli)

### Overview
* Autocompletion
	* `vagrant autocomplete install --bash --zsh`
* `VAGRANT_HOME` env
	* by default it is `~/.vagrant.d`
	* set it to `$STUDIO_DIR/Vagrant`

### `vagrant box`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/box)

#### `vagrant box add`
* usage: `vagrant box add ADDRESS`
* The address can be one of three things:
	* A shorthand name from the [public catalog of available Vagrant images](https://vagrantcloud.com/boxes/search), such as "hashicorp/bionic64".
	* File path or HTTP URL to a box in a [catalog](https://vagrantcloud.com/boxes/search). For HTTP, basic authentication is supported and `http_proxy` environmental variables are respected. HTTPS is also supported.
	* URL directly a box file. In this case, you must specify a `--name` flag (see below) and versioning/updates will not work.
* If an error occurs during the download or the download is interrupted with a Ctrl-C, then Vagrant will attempt to resume the download the next time it is requested. Vagrant will only attempt to resume a download for 24 hours after the initial download.
* options
	* [`--box-version VALUE`](https://developer.hashicorp.com/vagrant/docs/cli/box#box-version-value)
	* `--clean` : If given, Vagrant will remove any old temporary files from prior downloads of the same URL. This is useful if you do not want Vagrant to resume a download from a previous point, perhaps because the contents changed.
	* `--force` : When present, the box will be downloaded and overwrite any existing box with this name.
	* [`--name VALUE`](https://developer.hashicorp.com/vagrant/docs/cli/box#name-value) : Logical name for the box. This is the value that you would put into `config.vm.box` in your Vagrantfile. When adding a box from a catalog, the name is included in the catalog entry and does not have to be specified.

#### `vagrant box list`
* This command lists all the boxes that are installed into Vagrant.

#### `vagrant box outdated`
* This command tells you whether or not the box you are using in your current Vagrant environment is outdated.
* This will show the latest version available for the specific provider type, which may be different than the absolute latest version available.
* Checking for updates involves refreshing the metadata associated with a box. This generally requires an internet connection.
* If the `--global` flag is present, every installed box will be checked for updates.
* `--force` checks for updates for all installed boxes and ignore cache interval.

#### `vagrant box prune`
* This command removes old versions of installed boxes. If the box is currently in use vagrant will ask for confirmation.
* options
	* `--dry-run`
	* `--name NAME`
	* `--force`
	* `--keep-active-boxes`

#### `vagrant box remove`
* usage: `vagrant box remove NAME`
* This command removes a box from Vagrant that matches the given name.
* options
	* `--box-version VALUE`
	* `--all`
	* `--force`
	* `--provider VALUE`

#### `vagrant box update`
* This command updates the box for the current Vagrant environment if there are updates available.
* Note that updating the box will not update an already-running Vagrant machine. To reflect the changes in the box, you will have to destroy and bring back up the Vagrant machine.
* If you just want to check if there are updates available, use the `vagrant box outdated` command.
* options
	* `--box VALUE` : Name of a specific box to update.
	* `--provider VALUE`

### `vagrant cloud search`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/cloud#cloud-search)

* usage: `vagrant cloud search QUERY`
* The cloud search command will take a query and search Vagrant Cloud for any matching Vagrant boxes. Various filters can be applied to the results.
* options
	* `--json`
	* `--page PAGE` : Defaults to the first page of results.
	* `--short`
	* `--order ORDER` : Can either be `desc` or `asc`. Defaults to `desc`.
	* `--limit LIMIT` : Defaults to 25.
	* `--provider PROVIDER`
	* `--sort-by SORT` : Can be `created`, `downloads` , or `updated`. Defaults to `downloads`.

### `vagrant destroy`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/destroy)

* usage: `vagrant destroy [name|id]`
* This command stops the running machine Vagrant is managing and destroys all resources that were created during the machine creation process. After running this command, your computer should be left at a clean state, as if you never created the guest machine in the first place.
* For Linux-based guests, Vagrant uses the `shutdown` command to gracefully terminate the machine.
* options
	* `-f/--force` : do not ask for confirmation
	* `-g/--graceful` : shutdown the machine gracefully

> [!Warning]
> The `destroy` command does not remove a box that may have been installed on your computer during `vagrant up`. Thus, even if you run `vagrant destroy`, the box installed in the system will still be present on the hard drive. To return your computer to the state as it was before `vagrant up` command, you need to use `vagrant box remove`.

### `vagrant global-status`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/global-status)

* This command will tell you the state of all active Vagrant environments on the system for the currently logged in user.

> [!Warning]
> **This command does not actively verify the state of machines**, and is instead based on a cache. Because of this, it is possible to see stale results (machines say they're running but they're not). For example, if you restart your computer, Vagrant would not know. To prune the invalid entries, run global status with the `--prune` flag.

* options
	* `--prune` : Prunes invalid entries from the list. This is much more time consuming than simply listing the entries.
* Environment Not Showing Up
	* If your environment is not showing up, you may have to do a `vagrant destroy` followed by a `vagrant up`.
	* If you just upgraded from a previous version of Vagrant, existing environments will not show up in global-status until they are destroyed and recreated.

### `vagrant halt`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/halt)

* usage: `vagrant halt [name|id]`
* This command shuts down the running machine Vagrant is managing.
* Vagrant will first attempt to gracefully shut down the machine by running the guest OS shutdown mechanism. If this fails, or if the `--force` flag is specified, Vagrant will effectively just shut off power to the machine.
* For Linux-based guests, Vagrant will:
	1. Attempt to detect and use Systemd to execute `systemctl poweroff`; but otherwise,
	2. Fallback to using the `shutdown` command to gracefully terminate the machine.

### `vagrant init`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/init)

* usage: `vagrant init [name [url]]`
* This initializes the current directory to be a Vagrant environment by creating an initial [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile) if one does not already exist.
* If a first argument is given, it will prepopulate the `config.vm.box` setting in the created Vagrantfile.
* If a second argument is given, it will prepopulate the `config.vm.box_url` setting in the created Vagrantfile.
* options
	* `--box-version`
	* `-f/--force` : If specified, this command will overwrite any existing `Vagrantfile`.
	* `-m/--minimal` : If specified, a minimal Vagrantfile will be created. This Vagrantfile does not contain the instructional comments that the normal Vagrantfile contains.
	* `--output FILE` : This will output the Vagrantfile to the given file. If this is "-", the Vagrantfile will be sent to stdout.
	* `--template FILE` : Provide a custom ERB template for generating the Vagrantfile.
	
### `vagrant port`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/port)

* usage: `vagrant port [name|id]`
* The port command displays the full list of guest ports mapped to the host machine ports:
* In a multi-machine Vagrantfile, the name of the machine must be specified.
* `--machine-readable` : This tells Vagrant to display machine-readable output instead of the human-friendly output. More information is available in the [machine-readable output](https://developer.hashicorp.com/vagrant/docs/cli/machine-readable) documentation.

### `vagrant provision`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/provision)

* usage: `vagrant provision [vm-name]`
* Runs any configured [provisioners](https://developer.hashicorp.com/vagrant/docs/provisioning) against the running Vagrant managed machine.
* This command is a great way to quickly test any provisioners, and is especially useful for incremental development of shell scripts, Chef cookbooks, or Puppet modules. You can just make simple modifications to the provisioning scripts on your machine, run a `vagrant provision`, and check for the desired results. Rinse and repeat.
* `--provision-with x,y,z` : This will only run the given provisioners. For example, if you have a `:shell` and `:chef_solo` provisioner and run `vagrant provision --provision-with shell`, only the shell provisioner will be run.

### `vagrant reload`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/reload)

* usage: `vagrant reload [name|id]`
* The equivalent of running a [halt](https://developer.hashicorp.com/vagrant/docs/cli/halt) followed by an [up](https://developer.hashicorp.com/vagrant/docs/cli/up).
* This command is usually required for changes made in the Vagrantfile to take effect. After making any modifications to the Vagrantfile, a `reload` should be called.
* The configured provisioners will not run again, by default. You can force the provisioners to re-run by specifying the `--provision` flag.
* options
	* `--provision`
	* `--provision-with`

### `vagrant resume`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/resume)

* usage: `vagrant resume [name|id]`
* This resumes a Vagrant managed machine that was previously suspended, perhaps with the [suspend command](https://developer.hashicorp.com/vagrant/docs/cli/suspend).
* The configured provisioners will not run again, by default. You can force the provisioners to re-run by specifying the `--provision` flag.
* options
	* `--provision`
	* `--provision-with`

### `vagrant ssh`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/ssh)

* usage: `vagrant ssh [name|id] [-- extra_ssh_args]`
* This will SSH into a running Vagrant machine and give you access to a shell.
* On a simple vagrant project, the instance created will be named default.
* On multi-machine setups, you can login to each VM using the name as displayed on `vagrant status`.
* On a system with machines running from different projects, you could use the id as listed in `vagrant global-status`.
* If a `--` (two hyphens) are found on the command line, any arguments after this are passed directly into the `ssh` executable. This allows you to pass any arbitrary commands to do things such as reverse tunneling down into the `ssh` program.
* options
	* `-c/--command CMD` : This executes a single SSH command, prints out the stdout and stderr, and exits.
	* `-p/--plain` : This does an SSH without authentication, leaving authentication up to the user.

### `vagrant ssh-config`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/ssh_config)

* usage: `vagrant ssh-config [name|id]`
* This will output valid configuration for an SSH config file to SSH into the running Vagrant machine from `ssh` directly (instead of using `vagrant ssh`).
* `--host NAME` : Name of the host for the outputted configuration.

### `vagrant status`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/status)

* usage: `vagrant status [name|id]`
* This will tell you the state of the machines Vagrant is managing.
* It is quite easy, especially once you get comfortable with Vagrant, to forget whether your Vagrant machine is running, suspended, not created, etc. This command tells you the state of the underlying guest machine.

### `vagrant suspend`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/suspend)

* This suspends the guest machine Vagrant is managing, rather than fully [shutting it down](https://developer.hashicorp.com/vagrant/docs/cli/halt) or [destroying it](https://developer.hashicorp.com/vagrant/docs/cli/destroy).
* A suspend effectively saves the _exact point-in-time state_ of the machine, so that when you [resume](https://developer.hashicorp.com/vagrant/docs/cli/resume) it later, it begins running immediately from that point, rather than doing a full boot.
* This generally requires extra disk space to store all the contents of the RAM within your guest machine, but the machine no longer consumes the RAM of your host machine or CPU cycles while it is suspended.

### `vagrant up`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/up)

* usage: `vagrant up [name|id]`
* This command creates and configures guest machines according to your [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile).
* This is the single most important command in Vagrant, since it is how any Vagrant machine is created.
* options
	* `name` : Name of machine defined in [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile). Using `name` to specify the Vagrant machine to act on must be done from within a Vagrant project (directory where the Vagrantfile exists).
	* `id` : Machine id found with `vagrant global-status`. Using `id` allows you to call `vagrant up id` from any directory.
	* `--[no-]destroy-on-error` : Destroy the newly created machine if a fatal, unexpected error occurs. This will only happen on the first `vagrant up`. By default this is set.
	* `--[no-]install-provider` : If the requested provider is not installed, Vagrant will attempt to automatically install it if it can. **By default this is enabled.**
	* `--provider x` : Bring the machine up with the given [provider](https://developer.hashicorp.com/vagrant/docs/providers). By default this is "virtualbox".
	* `--[no-]provision` : Force, or prevent, the provisioners to run.
	* `--provision-with x,y,z`

### `vagrant upload`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/upload)

* usage: `vagrant upload source [destination] [name|id]`
* This command uploads files and directories from the host to the guest machine.
* options
	* `destination` : Path on the guest machine to upload file or directory.
	* `source` : Path to file or directory on host to upload to guest machine.
	* `--compress` : Compress the file or directory before uploading to guest machine.
	* `--compress-type type` : Type of compression to use when compressing file or directory for upload. Defaults to `tgz` for non-Windows guests. Valid values: `tgz`, `zip`.
	* `--temporary` : Create a temporary location on the guest machine and upload files to that location.

### `vagrant validate`
> [source](https://developer.hashicorp.com/vagrant/docs/cli/validate)

* This command validates your [Vagrantfile](https://developer.hashicorp.com/vagrant/docs/vagrantfile).
* `--ignore-provider` - Ignores provider config options.