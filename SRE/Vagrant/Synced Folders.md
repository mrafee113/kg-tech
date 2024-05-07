> [source](https://developer.hashicorp.com/vagrant/docs/synced-folders)

* Synced folders enable Vagrant to sync a folder on the host machine to the guest machine, allowing you to continue working on your project's files on your host machine, but use the resources in the guest machine to compile or run your project.

### Basic Usage
> [source](https://developer.hashicorp.com/vagrant/docs/synced-folders/basic_usage)

#### Configuration
* Synced folders are configured within your Vagrantfile using the `config.vm.synced_folder` method. Usage of the configuration directive is very simple:
```ruby
Vagrant.configure("2") do |config|
  # other config here
  config.vm.synced_folder "src/", "/srv/website"
end
```
* The first parameter is a path to a directory on the host machine. If the path is relative, it is relative to the project root. The second parameter must be an absolute path of where to share the folder within the guest machine. This folder will be created (recursively, if it must) if it does not exist. By default, Vagrant mounts the synced folders with the owner/group set to the SSH user and any parent folders set to root.

#### options
* `create` (boolean) : If true, the host path will be created if it does not exist. Defaults to false.
* `disabled` (boolean) : If true, this synced folder will be disabled and will not be setup. This can be used to disable a previously defined synced folder or to conditionally disable a definition based on some external factor.
* `mount_options` (array) : A list of additional mount options to pass to the `mount` command.
* `type` (string) : The type of synced folder. If this is not specified, Vagrant will automatically choose the best synced folder option for your environment. Otherwise, you can specify a specific type such as "nfs".
* `id` (string) : The name for the mount point of this synced folder in the guest machine. This shows up when you run `mount` in the guest machine.

#### Enabling and Disabling
* Synced folders are automatically setup during `vagrant up` and `vagrant reload`.
* Synced folders can be disabled by adding the `disabled` option to any definition:
```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder "src/", "/srv/website", disabled: true
end
```
* Disabling the default `/vagrant` share can be done as follows:
```ruby
config.vm.synced_folder ".", "/vagrant", disabled: true
```

### VirtualBox
> [source](https://developer.hashicorp.com/vagrant/docs/synced-folders/virtualbox)

* If you are using the Vagrant VirtualBox [provider](https://developer.hashicorp.com/vagrant/docs/providers), then VirtualBox shared folders are the default synced folder type. These synced folders use the VirtualBox shared folder system to sync file changes from the guest to the host and vice versa.
* options
	* `automount` (boolean) : If true, the `--automount` flag will be used when using the VirtualBox tools to share the folder with the guest VM. Defaults to false if not present.
	* `SharedFoldersEnableSymlinksCreate` (boolean) : If false, will disable the ability to create symlinks with the given VirtualBox shared folder. Defaults to true if the option is not present.
