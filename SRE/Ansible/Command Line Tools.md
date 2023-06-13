### Introduction to ad hoc commands
> [source](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html)
* An Ansible ad hoc command uses the /usr/bin/ansible command-line tool to automate a single task on one or more managed nodes.
* ad hoc commands are quick and easy, but they are not reusable. So why learn about ad hoc commands? ad hoc commands demonstrate the simplicity and power of Ansible. The concepts you learn here will port over directly to the playbook language.

#### Why use ad hoc commands?
* ad hoc commands are great for tasks you repeat rarely. For example, if you want to power off all the machines in your lab for Christmas vacation, you could execute a quick one-liner in Ansible without writing a playbook. An ad hoc command looks like this:
	* `ansible [pattern] -m [module] -a "[module options]"`
* The `-a` option accepts options either through the `key=value` syntax or a JSON string starting with `{` and ending with `}` for more complex option structure. You can learn more about [[SRE/Ansible/Building Inventories#Patterns: targeting hosts and groups|patterns]] and [modules](https://docs.ansible.com/ansible/6/user_guide/modules.html#working-with-modules "(in Ansible v6)") on other pages.

#### Use cases for ad hoc tasks
* ad hoc tasks can be used to reboot servers, copy files, manage packages and users, and much more.
* You can use any Ansible module in an ad hoc task. ad hoc tasks, like playbooks, use a declarative model, calculating and executing the actions required to reach a specified final state.
	* They achieve a form of idempotence by checking the current state before they begin and doing nothing unless the current state is different from the specified final state.

##### Rebooting servers
* The default module for the `ansible` command-line utility is the [ansible.builtin.command module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#command-module).
* You can use an ad hoc task to call the command module and reboot all web servers in Atlanta, 10 at a time. To reboot all the servers in the `[atlanta]` group:
	* `ansible atlanta -a "/sbin/reboot"`
* By default Ansible uses only 5 simultaneous processes. If you have more hosts than the value set for the fork count, Ansible will talk to them, but it will take a little longer. To reboot the `[atlanta]` servers with 10 parallel forks:
	* `ansible atlanta -a "/sbin/reboot" -f 10`
* /usr/bin/ansible will default to running from your user account. To connect as a different user:
	* `ansible atlanta -a "/sbin/reboot" -f 10 -u username`
* Rebooting probably requires privilege escalation. You can connect to the server as `username` and run the command as the `root` user by using the [become](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html#become) keyword:
	* `ansible atlanta -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]`
	* If you add `--ask-become-pass` or `-K`, Ansible prompts you for the password to use for privilege escalation `(sudo/su/pfexec/doas/etc)`.
* The [command module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#command-module) does not support extended shell syntax like piping and redirects (although shell variables will always work). If your command requires shell-specific syntax, use the shell module instead. Read more about the differences on the [Working With Modules](https://docs.ansible.com/ansible/6/user_guide/modules.html#working-with-modules "(in Ansible v6)") page.
* So far all our examples have used the default ‘command’ module. To use a different module, pass `-m` for module name. For example, to use the [ansible.builtin.shell module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html#shell-module):
	* `ansible raleigh -m ansible.builtin.shell -a 'echo $TERM'`
* When running any command with the Ansible _ad hoc_ CLI (as opposed to [Playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks.html#working-with-playbooks)), pay particular attention to shell quoting rules, so the local shell retains the variable and passes it to Ansible. For example, using double rather than single quotes in the above example would evaluate the variable on the box you were on.

##### Managing files
* An ad hoc task can harness the power of Ansible and SCP to transfer many files to multiple machines in parallel. To transfer a file directly to all servers in the `[atlanta]` group:
	* `ansible atlanta -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"`
	* If you plan to repeat a task like this, use the [ansible.builtin.template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#template-module) module in a playbook.
* The [ansible.builtin.file](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html#file-module) module allows changing ownership and permissions on files. These same options can be passed directly to the `copy` module as well:
	* `ansible webservers -m ansible.builtin.file -a "dest=/srv/foo/a.txt mode=600"`
	* `ansible webservers -m ansible.builtin.file -a "dest=/srv/foo/b.txt mode=600 owner=mdehaan group=mdehaan"`
* The `file` module can also create directories, similar to `mkdir -p`:
	* `ansible webservers -m ansible.builtin.file -a "dest=/path/to/c mode=755 owner=mdehaan group=mdehaan state=directory"`
* As well as delete directories (recursively) and delete files:
	* `ansible webservers -m ansible.builtin.file -a "dest=/path/to/c state=absent"`

##### Managing packages
* You might also use an ad hoc task to install, update, or remove packages on managed nodes using a package management module such as `yum`. Package management modules support common functions to install, remove, and generally manage packages. **Some specific functions for a package manager might not be present in the Ansible module since they are not part of general package management.**
* To ensure a package is installed without updating it:
	* `ansible webservers -m ansible.builtin.yum -a "name=acme state=present"`
* To ensure a specific version of a package is installed:
	* `ansible webservers -m ansible.builtin.yum -a "name=acme-1.5 state=present"`
* To ensure a package is at the latest version:
	* `ansible webservers -m ansible.builtin.yum -a "name=acme state=latest"`
* To ensure a package is not installed:
	* `ansible webservers -m ansible.builtin.yum -a "name=acme state=absent"`
* Ansible has modules for managing packages under many platforms. If there is no module for your package manager, you can install packages using the command module or create a module for your package manager.

##### Managing users and groups
* You can create, manage, and remove user accounts on your managed nodes with ad hoc tasks:
	* `ansible all -m ansible.builtin.user -a "name=foo password=<crypted password here>"`
	* `ansible all -m ansible.builtin.user -a "name=foo state=absent"`
* See the [ansible.builtin.user](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html#user-module) module documentation for details on all of the available options, including how to manipulate groups and group membership.

##### Managing services
* Ensure a service is started on all webservers:
	* `ansible webservers -m ansible.builtin.service -a "name=httpd state=started"`
* Alternatively, restart a service on all webservers:
	* `ansible webservers -m ansible.builtin.service -a "name=httpd state=restarted"`
* Ensure a service is stopped:
	* `ansible webservers -m ansible.builtin.service -a "name=httpd state=stopped"`

##### Gathering facts
* Facts represent discovered variables about a system. You can use facts to implement conditional execution of tasks but also just to get ad hoc information about your systems. To see all facts:
	* `ansible all -m ansible.builtin.setup`
* You can also filter this output to display only certain facts, see the [ansible.builtin.setup](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html#setup-module) module documentation for details.
* See the [[Building Inventories#Patterns: targeting hosts and groups|patterns]] documentation for details on all of the available options, including how to limit using patterns in ad-hoc commands.

### Working with command-line tools
* [ansible](https://docs.ansible.com/ansible/latest/cli/ansible.html) ^cli-ansible
	* Define and run a single task ‘playbook’ against a set of hosts.
	* This is an extra-simple tool/framework/API for doing ‘remote things’.
	* `--list-hosts` outputs a list of matching hosts; does not execute anything else
	* `--syntax-check` perform a syntax check on the playbook, but do not execute it
	* `-C/--check` don’t make any changes; instead, try to predict some of the changes that may occur
	* `-D/--diff` when changing (small) files and templates, show the differences in those files; works great with –check
	* `-o/--one-line` condense output
	* `-t/--tree <dir>` log output to this directory
	* `ANSIBLE_CONFIG` override the default ansible config file
	* `/etc/ansible/ansible.cfg`
	* `~/.ansible.cfg` user config file, overrides the default config if present
* [ansible-config](https://docs.ansible.com/ansible/latest/cli/ansible-config.html) ^cli-ansible-config
	* View ansible configuration.
	* Desc: config command-line class
	* Synopsys: `ansible-config [-h] [--version] [-v] {list,dump,view,init} ...`
	* `list` list and output available configs
	* `dump` shows the current settings, merges `ansible.cfg` if specified
	* `view` displays the current config file
	* `init`
* [ansible-console](https://docs.ansible.com/ansible/latest/cli/ansible-console.html) ^cli-ansible-console
	* REPL console for executing ansible tasks
	* A REPL that allows for running ad-hoc tasks against a chosen inventory from a nice shell with built-in tab completion (based on dominis’ ansible-shell). 
	* It supports [several commands](https://docs.ansible.com/ansible/latest/cli/ansible-console.html#description), and you can modify its configuration at runtime.
	* `--step` one-step-at-a-time: confirm each task before running
* [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html) ^cli-ansible-doc
	* plugin documentation tool; displays information on modules installed in Ansible libraries. It displays a terse listing of plugins and their short descriptions, provides a printout of their DOCUMENTATION strings, and it can create a short “snippet” which can be pasted into a playbook.
	* simplified synopsys: `ansible-doc [plugin...]`
	* `-l/--list` lists available plugins. A supplied argument will be used for filtering, can be a namespace or full collection name.
	* `-F/--list_files` show plugin names and their source files without summaries (implies `--list`).
	* `-s/--snippet` show playbook snippet for these plugin types: inventory, lookup, module
* [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html) ^cli-ansible-galaxy
	* Perform various Role and Collection related operations. Command to manage Ansible roles and collections.
		* None of the CLI tools are designed to run concurrently with themselves. Use an external scheduler and/or locking to ensure there are no clashing operations.
	* Synopsys: `usage: ansible-galaxy [-h] [--version] [-v] TYPE ...`
	* Actions
		* Collection: Perform the action on an Ansible Galaxy collection. Must be combined with a further action like init/install as listed below.
			* `collection download`
				* `-r/--requirement-file <file>` is a file containing a list of collections to be downloaded.
			* `collection init`
				* Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy. By default, this command builds from the current working directory. You can optionally pass in the collection input path (where the `galaxy.yml` file is).
			* `collection publish`
				* Publish a collection into Ansible Galaxy. Requires the path to the collection tarball to publish.
			* `collection install`
			* `collection list` lists installed collections or roles
			* `collection verify`
		* Role: Perform the action on an Ansible Galaxy role. Must be combined with a further action like delete/install/init as listed below.
			* `role init`
				* Creates the skeleton framework of a role or collection that complies with the Galaxy metadata format. Requires a role or collection name. The collection name must be in the format `<namespace>.<collection>`.
			* `role remove` removes the list of roles passed as arguments from the local system.
			* `role delete` deletes a role from Ansible Galaxy.
			* `role list` lists installed collections or roles
			* `role search` searches for roles on the Ansible Galaxy server
				* `--author <github-username>`
				* `--galaxy-tags <tags>`
				* `--platforms <os-platforms>`
			* `role import` is used to import a role into Ansible Galaxy
			* `role setup` sets up an integration from Github or Travis for Ansible Galaxy roles
			* `role info` prints out detailed information about an installed role as well as info available from the galaxy API.
			* `role install`
* [ansible-inventory](https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html) ^cli-ansible-inventory
	* Used to display or dump the configured inventory as Ansible sees it
	* `--list` outputs all hosts info, works as inventory script
	* `--export` when doing a `--list`, represent in a way that is optimized for export,not as an accurate representation of how Ansible has processed it
	* `--graph` create inventory graph, if supplying pattern it must be a valid group name
	* `--toml` use TOML format instead of default JSON, ignored for `--graph`
	* `--vars` adds vars to graph display, ignored unless used with `--graph`
	* `-y/--yaml` uses YAML format instead of default JSON, ignored for `--graph`
* [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) ^cli-ansible-playbook
	* Runs ansible playbook, executing the defined tasks on the targeted hosts. This is the tool to run _Ansible playbooks_, which are a configuration and multinode deployment system.
	* `--list-hosts` outputs a list of matching hosts; does not execute anything else
	* `--list-tags` lists all available tags
	* `--list-tasks` lists all tasks that would be executed
	* `--start-at-task <name>` start the playbook at the task matching this name
	* `--step` one-step-at-a-time: confirm each task before running
	* `--syntax-check`
	* `-C/--check`
	* `-D/--diff`
* [ansible-pull](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html) ^cli-ansible-pull
	* Pulls playbooks from a VCS repo and executes them for the local host. This is used to pull a remote copy of ansible on each managed node, each set to run via cron and update playbook source via a source repository. This inverts the default _push_ architecture of ansible into a _pull_ architecture, which has near-limitless scaling potential.
	* The setup playbook can be tuned to change the cron frequency, logging locations, and parameters to ansible-pull. This is useful both for extreme scale-out as well as periodic remediation. Usage of the ‘fetch’ module to retrieve logs from ansible-pull runs would be an excellent way to gather and analyze remote logs from ansible-pull.
* [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html) ^cli-ansible-vault
	* Encryption and decryption utility for ansible data files. This can encrypt any structured data file used by Ansible. This can include _group_vars/_ or _host_vars/_ inventory variables, variables loaded by _include_vars_ or _vars_files_, or variable files passed on the ansible-playbook command line with _-e @file.yml_ or _-e @file.json_. Role variables and defaults are also included!
	* Because Ansible tasks, handlers, and other objects are data, these can also be encrypted with vault. If you’d like to not expose what variables you are using, you can keep an individual task file entirely encrypted.
	* Synopsys: `ansible-vault {create,decrypt,edit,view,encrypt,encrypt_string,rekey}`
	* create: create and open a file in an editor that will be encrypted with the provided vault secret when closed
	* decrypt: decrypt the supplied file using the provided vault secret
	* edit: open and decrypt an existing vaulted file in an editor, that will be encrypted again when closed
	* view: open, decrypt and view an existing vaulted file using a pager using the supplied vault secret
	* encrypt: encrypt the supplied file using the provided vault secret
	* encrypt_string: encrypt the supplied string using the provided vault secret
	* rekey: re-encrypt a vaulted file with a new secret, the previous secret is required
* [ansible-lint](https://ansible-lint.readthedocs.io/) ^cli-ansible-lint