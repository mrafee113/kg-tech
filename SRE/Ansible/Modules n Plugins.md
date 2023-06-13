### Plugins
#### Action Plugins
* Action plugins act in conjunction with [modules](https://docs.ansible.com/ansible/6/user_guide/modules.html#working-with-modules "(in Ansible v6)") to execute the actions required by playbook tasks. They usually execute automatically in the background doing prerequisite work before modules execute.
* The ‘normal’ action plugin is used for modules that do not already have an action plugin. If necessary, you can [create custom action plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-actions).
* You cannot list action plugins directly, they show up as their counterpart modules. Use `ansible-doc <name>` to see specific documentation and examples, this should note if the module has a corresponding action plugin.

#### Become Plugins
* Become plugins work to ensure that Ansible can use certain privilege escalation systems when running the basic commands to work with the target machine as well as the modules required to execute the tasks specified in the play.
* These utilities (`sudo`, `su`, `doas`, and so on) generally let you ‘become’ another user to execute a command with the permissions of that user.
* plugins
	* `ansible.builtin`
		* `runas` - run as user
		* `su` - substitude user
		* `sudo` - substitude user do
	* `ansible.netcommon`
		* `enable` - switch to elevated permissions on a network device
	* `community.general`
		* `doas`
		* `machinectl` - systemd's machinectl privilege escalation
		* `sudosu` - run tasks using sudo su -

#### Cache Plugins
* Cache plugins allow Ansible to store gathered facts or inventory source data without the performance hit of retrieving them from source.
* The default cache plugin is the [memory](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/memory_cache.html#memory-cache) plugin, which only caches the data for the current execution of Ansible. Other plugins with persistent storage are available to allow caching the data across runs. Some of these cache plugins write to files, others write to databases.
* You can use different cache plugins for inventory and facts. If you enable inventory caching without setting an inventory-specific cache plugin, Ansible uses the fact cache plugin for both facts and inventory. If necessary, you can [create custom cache plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-cache-plugins).
* plugins
	* `ansible.builtin`
		* `jsonfile`
		* `memory` - RAM backed, non persistent
	* `ansible.netcommon`
		* `memory` - RAM backed, non persistent cache
	* `community.general`
		* `memcached`
		* `pickle` - pickle formatted files
		* `redis`
		* `yaml`
	* `community.mongodb.mongodb`

#### Callback Plugins
* Callback plugins enable adding new behaviors to Ansible when responding to events. By default, callback plugins control most of the output you see when running the command line programs, but can also be used to add additional output, integrate with other tools and marshal the events to a storage backend.
* If necessary, you can [create custom callback plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-callbacks).
* plugins
	* `ansible.builtin`
		* `default` - default ansible screen output
		* `minimal` - minimal ansible screen output
		* `oneline` - one line ansible screen output
		* `tree` - save host events to files
	* `ansible.posix`
		* `cgroup_perf_recap` - profiles system activity of tasks and full execution using cgroups
		* `debug` - formatted stdout/stderr display
		* `json` - ansible screen output as JSON
		* `jsonl`
		* `profile_roles` - adds timing information to roles
		* `profile_tasks` - adds time information to tasks
		* `skippy` - ansible screen output that ignores skipped status
		* `timer` - adds time to play stats
	* `community.general`
		* `cgroup_memory_recap` - Profiles maximum memory usage of tasks and full execution using cgroups
		* `dense` - minimal stdout output
		* `diy` - customize the output
		* `log_plays` - write playbook output to log file
		* `mail` - sends failure events via mail
		* `null` - don't display stuff to screen
		* `say` - notify using software speech synthesizer
		* `selective` - only print certain tasks
		* `syslog_json` - sends JSON events to syslog
		* `unixy` - condensed ansible output
		* `yaml` - YAML-ized ansible screen output

#### Cliconf Plugins
* Cliconf plugins are abstractions over the CLI interface to network devices. They provide a standard interface for Ansible to execute tasks on those network devices.
* These plugins generally correspond one-to-one to network device platforms. Ansible loads the appropriate cliconf plugin automatically based on the `ansible_network_os` variable.

#### Connection Plugins
* Connection plugins allow Ansible to connect to the target hosts so it can execute tasks on them. Ansible ships with many connection plugins, but only one can be used per host at a time.
* If necessary, you can [create custom connection plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-connection-plugins).
* plugins
	* `ansible.builtin`
		* `local` - execute on controller
		* `paramiko_ssh` - run tasks via python ssh (paramiko)
		* `ssh`
	* `ansible.netcommon`
		* `grpc` - provides a persistent connection using the gRPC protocol
		* `httpapi` - use httpapi to run command on network appliances
		* `libssh`
		* `netconf` provides a persistent connection using the netconf protocol
		* `network_cli` - use network_cli to run command on network appliances
		* `persistent` - use a persistent unix socket for connection
	* `community.docker`
		* `docker` - run tasks in docker containers
		* `docker_api` - run tasks in docker containers
	* `community.general`
		* `chroot` - interact with local chroot
		* `lxc` - run tasks in lxc containers via lxc python library
		* `lxd` - run tasks in lxc containers via lxc CLI
	* `community.libvirt`
		* `libvirt` - run tasks in lxc containers via libvirt
		* `libvirt_qemu` - run tasks on libvirt/qemu virtual machines
	* `community.vmware.vmware_tools` - execute tasks inside a VM
	* `kubernetes.core.kubectl` - executes tasks in pods running on kubernetes

#### Filter Plugins
* Filter plugins manipulate data. With the right filter you can extract a particular value, transform data types and formats, perform mathematical calculations, split and concatenate strings, insert dates and times, and do much more.
* Ansible uses the [standard filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters "(in Jinja v3.1.x)") shipped with Jinja2 and adds some specialized filter plugins. You can [create custom Ansible filters as plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-filter-plugins).
* plugins
	* `ansible.builtin`
		* `b64decode`
		* `b64encode`
		* `basename` - get a path's basename
		* `bool` - cast
		* `checksum`
		* `combinations`
		* `combine` - combine two dictionaries
		* `comment` - comment out a string
		* `commonpath` - gets the common path
		* `dict2items`
		* `difference` - the difference of one list from another
		* `dirname`
		* `expanduser` - returns a path with `~` translation
		* `expandvars` - expand environment variables
		* `extract` - extract a value based on an index or key
		* `fileglob` - explode a path glob to matching files
		* `flatten`
		* `from_json`
		* `from_yaml`
		* `from_yaml_all`
		* `hash`
		* `human_readable`
		* `human_to_bytes`
		* `intersect`
		* `items2dict`
		* `log` - math
		* `mandatory` - make a variables existence mandatory
		* `md5`
		* `normpath`
		* `password_hash`
		* `path_join`
		* `permutations`
		* `pow`
		* `product` - cartesian product of lists
		* `quote` - shell quoting
		* `random`
		* `realpath`
		* `regex_escape`
		* `regex_findall`
		* `regex_replace`
		* `regex_search`
		* `rekey_on_member` - rekey a list of dicts into a dict using a member
		* `relpath` - make a path relative
		* `root` - math
		* `sha1`
		* `shuffle`
		* `split`
		* `splittext` - split a path into root and file extension
		* `strftime`
		* `subelements` - returns a product of a list and its elements
		* `symmetric_difference`
		* `ternary`
		* `to_datetime` - from string
		* `to_json` - from var
		* `to_nice_json`
		* `to_nice_yaml`
		* `to_uuid`
		* `to_yaml`
		* ***`type_debug` - show input data type***
		* `union`
		* `unique`
		* `unvault` - open an ansible vault
		* `urlsplit`
		* `vault` - vault your secrets
		* `zip` - combine list elements
		* `zip_longest`
	* `ansible.utils`
		* `cidr_merge` - this filter can be used to merge subnets or individual addresses
		* `consolidate` - consolidate facts together on common attributes
		* `from_xml` - to python dict
		* `get_path` - retrieve the value in a variable using a path
		* `index_of` - find the indices of items in a list matching criteria
		* `ip4_hex`
		* `ipaddr`
		* `ipmath`
		* `ipsubnet`
		* `ipv4`
		* `ipv6`
		* `ipwrap`
		* `keep_keys` - keep specific keys from a data recursively
		* `macaddr`
		* `hwaddr`
		* `network_in_network` - this filter returns whether an address or a network passed as argument is in a network.
		* `network_in_usable` - this filter returns whether an address passed as an argument is usable in a network.
		* `next_nth_usable` - this filter returns the next nth usable ip within a network described by value.
		* `nthhost`
		* `param_list_compare` - generate the final param list combining/comparing base and provided parameters.
		* `previous_nth_usable`
		* `reduce_on_network` this filter reduces a list of addresses to only the addresses that match a given network.
		* `remove_keys` - remove specific keys from a data recursively
		* `replace_keys` - replaces specific keys with their after value from a data recursively
		* `to_paths` - flatten a complex object into a dictionary of paths and values
		* `to_xml` - from json string
		* `usable_range` - expand the usable IP addresses
		* `validate` - validate data with provided data
	* `community.crypto`
		* `openssl_csr_info`
		* `openssl_privatekey_info`
		* `openssl_publickey_info`
		* `split_pem`
	* `community.dns`
		* `get_public_suffix` - returns the public suffix of a DNS name
		* `get_registrable_domain` - returns the registrable domain name of a DNS name
		* `remove_public_suffix`
		* `remove_registrable_domain`
	* `community.general`
		* `counter` - counts hashable elemets in a sequence
		* `dict` - convert list of tuples to dict
		* `dict_kv` - convert a value to a dictionary with a single key-value pair
		* `from_csv` - convert csv text input into a list of dicts
		* `groupby_as_dict` - transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute
		* `jc` - convert output of many shell commands and file-types to JSON
		* `json_query` - select a single element or a data subset from a complex data structure
		* `lists_mergeby` - merge two or more lists of dictionaries by a given attribute
		* `random_mac`
		* `to_days` - from duration string
		* `to_hours`
		* `to_milliseconds`
		* `to_minutes`
		* `to_months`
		* `to_seconds`
		* `to_time_unit`
		* `to_weeks`
		* `to_years`
		* `unicode_normalize` - normalizes unicode strings to facilitate comparison of characters with normalized forms
		* `version_sort` - sort a list according to version order instead of pure alphabetical one
	* `kubernetes.core.k8s_config_resource_name` - generate resource name for the given resource of type ConfigMap, Secret

#### Httpapi Plugins
* Httpapi plugins tell Ansible how to interact with a remote device’s HTTP-based API and execute tasks on the device.
* Each plugin represents a particular dialect of API. Some are platform-specific (Arista eAPI, Cisco NXAPI), while others might be usable on a variety of platforms (RESTCONF). Ansible loads the appropriate httpapi plugin automatically based on the `ansible_network_os` variable.
* plugins
	* `ansible.netcommon.restconf` - HttpApi Plugin for devices supporting Restconf API
	* `community.vmware.vmware` - HttpApi Plugin for VMware REST API

#### Inventory Plugins
* Inventory plugins allow users to point at data sources to compile the inventory of hosts that Ansible uses to target tasks, either using the `-i /path/to/file` and/or `-i 'host1, host2'` command line parameters or from other configuration sources. If necessary, you can [create custom inventory plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-inventory-plugins).
* Most inventory plugins shipped with Ansible are enabled by default or can be used by with the `auto` plugin.
* plugins
	* `ansible.builtin`
		* `advanced_host_list` - parses a ‘host list’ with ranges
		* `auto` - loads and executes an inventory plugin specified in a YAML config
		* `constructed` - uses Jinja2 to construct vars and groups based on existing inventory
		* `generator` - uses Jinja2 to construct hosts and groups from patterns
		* `host_list` - parses a ‘host list’ string
		* `ini` - uses an Ansible INI file as inventory source
		* `script` - executes an inventory script that returns JSON
		* `toml` - uses a specific TOML file as an inventory source
		* `yaml` - uses a specific YAML file as an inventory source
	* `community.docker`
		* `docker_containers` - ansible dynamic inventory plugin for Docker containers
		* `docker_machine` - docker machine inventory source
		* `docker_swarm` - ansible dynamic inventory plugin for Docker swarm nodes
	* `community.general`
		* `gitlab_runners`
		* `lxd` - returns Ansible inventory from lxd host
		* `nmap`
		* `virtualbox`
	* `community.libvirt.libvirt` - libvirt inventory source
	* `kubernetes.core.k8s` - Kubernetes (K8s) inventory source

#### Lookup Plugins
* Lookup plugins are an Ansible-specific extension to the Jinja2 templating language. You can use lookup plugins to access data from outside sources (files, databases, key/value stores, APIs, and other services) within your playbooks.
* Like all [templating](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html#playbooks-templating), lookups execute and are evaluated on the Ansible control machine. Ansible makes the data returned by a lookup plugin available using the standard templating system. You can use lookup plugins to load variables or templates with information from external sources. You can [create custom lookup plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-lookup-plugins).
* plugins
	* `ansible.builtin`
		* `config` - lookup current Ansible configuration values
		* `csvfile`
		* `dict`
		* `env`
		* `file`
		* `fileglob` - list files matching a pattern
		* `first_found` - return first file found from list
		* `indexed_items` - rewrites lists to return 'indexed items'
		* `ini`
		* `inventory_hostnames` - list of inventory hosts matching a host pattern
		* `items` - list of items
		* `lines` - read lines from command
		* `list` - simply returns what it is given
		* `nested` - composes a list with nested elements of other lists
		* `password` - retrieve or regenerate a random password, stored in a file
		* `pipe` - read output from a command
		* `random_choice`
		* `sequence` - generate a list based on a number of sequence
		* `subelements` - traverse nested key from a list of dictionaries
		* `template` - retrieve contents of file after templating with jinja2
		* `together` - merges lists into synchronized list
		* `unvault` - read vaulted file(s) content
		* `url` - return contents from URL
		* `varnames` - lookup matching variable names
		* `vars` - lookup templated value of variables
	* `ansible.utils`
		* `get_path` - retrieve the value in a variable using a path
		* `index_of` - find the indices of items in a list matching some criteria
		* `to_paths` - flatten a complex object into a dictionary of paths and values
		* `validate` - validate data with provided criteria
	* `community.general`
		* `bitwarden` - retrieve secrets from bitwarden
		* `cartesian` - returns the cartesian product of lists
		* `collection_version` - retrieves the version of an installed collection
		* `dependent` - composes a list with nested elements of other lists or dicts which can depend on previous loop variables
		* `dig` - query DNS using dnspython library
		* `dnstxt` - query a domain's DNS txt fields
		* `etcd`
		* `filetree` - recursively match all files in a dictionary tree
		* `flattened` - return single list completely flattened
		* `keyring` - grab secrets from the OS keyring
		* `merge_variables` - merge variables with a certain suffix
		* `random_string`
		* `random_words` - generates a number of random words
		* `redis`
		* `shelvefile` - read keys from python shelve file
	* `community.mongodb.mongodb` - lookup info from MongoDB
	* `kubernetes.core`
		* `k8s` - query the K8s API
		* `kustomize` - build a set of kubernetes resources using a 'kustomization.yaml' file

#### Netconf Plugins
* Netconf plugins are abstractions over the Netconf interface to network devices. They provide a standard interface for Ansible to execute tasks on those network devices.
* These plugins generally correspond one-to-one to network device platforms. Ansible loads the appropriate netconf plugin automatically based on the `ansible_network_os` variable. If the platform supports standard Netconf implementation as defined in the Netconf RFC specification, Ansible loads the `default` netconf plugin. If the platform supports propriety Netconf RPCs, Ansible loads the platform-specific netconf plugin.
* plugins
	* `ansible.netcommon.default` - use default netconf plugin to run standard netconf commands as per RFC

#### Shell Plugins
* Shell plugins work to ensure that the basic commands Ansible runs are properly formatted to work with the target machine and allow the user to configure certain behaviors related to how Ansible executes tasks.
* plugins
	* `ansible.builtin.sh` - POSIX shell (/bin/sh)
	* `ansible.posix`
		* `csh` - C shell (/bin/csh)
		* `fish` - fish shell (/bin/fish)

#### Strategy Plugins
* Strategy plugins control the flow of play execution by handling task and host scheduling. For more information on using strategy plugins and other ways to control execution order, see [Controlling playbook execution: strategies and more](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#playbooks-strategies).
* plugins
	* `ansible.builtin`
		* ***`debug` - executes tasks in interactive debug session***
		* `free` - executes tasks without waiting for all hosts
		* `host_pinned` - executes tasks on each host without interruption
		* `linear` - executes tasks in a linear fashion

#### Terminal Plugins
* Terminal plugins contain information on how to prepare a particular network device’s SSH shell is properly initialized to be used with Ansible. This typically includes disabling automatic paging, detecting errors in output, and enabling privileged mode if supported and required on the device.
* These plugins correspond one-to-one to network device platforms. Ansible loads the appropriate terminal plugin automatically based on the `ansible_network_os` variable.

#### Test Plugins
* Test plugins evaluate template expressions and return True or False. With test plugins you can create [conditionals](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html#playbooks-conditionals) to implement the logic of your tasks, blocks, plays, playbooks, and roles. Ansible uses the standard tests `_ shipped as part of Jinja, and adds some specialized test plugins. You can :ref:`create custom Ansible test plugins <developing_test_plugins>.
* plugins
	* `ansible.builtin`
		* `abs` - is path absolute
		* `all`
		* `any`
		* `changed` - did the task require changes
		* `contains`
		* `directory` - does the path resolve to an existing directory
		* `exists` - path
		* `failed` - task
		* `falsy` - pythonic false
		* `file` - does the path resolve to an existing file
		* `finished` - async task
		* `link` - does the path reference existing symbolic link
		* `link_exists` - does the path exist, no follow
		* `match` - does string match regular expression from the start
		* `mount` - does the path resolve to mount point
		* `nan` - is this not a number
		* `reachable` - task did not end due to unreachable host
		* `regex` - does string match regular expression from the start
		* `same_file` - compares two paths to see if they resolve to the same filesystem object
		* `search` - does string match a regular expression
		* `skipped` - task
		* `started` - async task
		* `subset` - is the list a subset of this other list
		* `success` - task
		* `superset` - lists
		* `truthy` - pythonic true
		* `unreachable` - did task end due to the host unreachable
		* `uri` - is valid URI
		* `url` - is valid URL
		* `urn` - is valid URN
		* `vault_encrypted` - is this an encrypted vault
		* `version`
	* `ansible.utils`
		* `in_any_network` - if an IP or network falls in a network
		* `in_network`
		* `in_one_network` - if IP address belongs in any of the networks in the list
		* `ip` - test if something in an IP address or network
		* `ip_address` - test if something in an IP address
		* `ipv4`
		* `ipv4_address`
		* `ipv6`
		* `ipv6_address`
		* `ipv4_hostmask` - test if an address is a valid hostmask
		* `ipv4_netmask` - test if an address is a valid netmask
		* `ipv6_ipv4_mapped` - test if something appears to be a mapped IPv6 to IPv4 mapped address
		* `ipv6_sixtofour` - test if something appears to be a 6to4 address
		* `loopback`
		* `mac` - validity
		* `multicast` - test for a multicast IP address
		* `private` - ip
		* `public` - ip
		* `reserved` - ip
		* `resolvable` - test if an IP or name can be resolved via /etc/hosts or DNS
		* `subnet_of` - networks
		* `supernet_of` - networks
		* `validate` - validate data with provided data

#### Vars Plugin
* Vars plugins inject additional variable data into Ansible runs that did not come from an inventory source, playbook, or command line. Playbook constructs like ‘host_vars’ and ‘group_vars’ work using vars plugins. For more details about variables in Ansible, see [Using Variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#playbooks-variables).
* plugins
	* `ansible.builtin.host_group_vars` - in charge of loading group_vars and host_vars

### Plugins vs Modules
If you are looking to add functionality to Ansible, you might wonder whether you need a module or a plugin. Here is a quick overview to help you understand what you need:
- [Plugins](https://docs.ansible.com/ansible/latest/plugins/plugins.html#working-with-plugins) extend Ansible’s core functionality. Most plugin types execute on the control node within the `/usr/bin/ansible` process. Plugins offer options and extensions for the core features of Ansible: transforming data, logging output, connecting to inventory, and more.
- Modules are a type of plugin that execute automation tasks on a ‘target’ (usually a remote system). Modules work as standalone scripts that Ansible executes in their own process outside of the controller. Modules interface with Ansible mostly via JSON, accepting arguments and returning information by printing a JSON string to stdout before exiting. Unlike the other plugins (which must be written in Python), modules can be written in any language; although Ansible provides modules in Python and Powershell only.

### Introduction to Modules
* Modules (also referred to as “task plugins” or “library plugins”) are discrete units of code that can be used from the command line or in a playbook task. Ansible executes each module, usually on the remote managed node, and collects return values.
* All modules return JSON format data.
	* This means modules can be written in any programming language.
	* Modules should be idempotent, and should avoid making any changes if they detect that the current state matches the desired final state.
	* When used in an Ansible playbook, modules can trigger ‘change events’ in the form of notifying [handlers](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html#handlers) to run additional tasks.

### Modules
* Modules are the main building blocks of Ansible playbooks.
* **Although we do not generally speak of “module plugins”, a module is a type of plugin.**
* For a developer-focused description of the differences between modules and other plugins, see [Modules and plugins: what is the difference?](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html#modules-vs-plugins).

#### `ansible.builtin`
* `add_host` - add a host (and alternatively a group) to the ansible-playbook in-memory inventory
* `apt`
* `apt_key`
* `apt_repository`
* `assemble` - assemble configuration files from fragments
* `assert`
* `async_status`
* `blockinfile` - insert/update/remove a text block surrounded by marker lines
* `command` - execute commands on targets
* `copy` - copy files to remote locations
* `cron` - manage cron.d and crontab entries
* `debconf` - configure a .deb package
* ***`debug` - print statements during execution***
* `dnf`
* `dpkg_selections` - dpkg package selection selections
* `expect` - executes a command and responds to prompts
* `fail` - fail with custom message
* `fetch` - fetch files from remote nodes
* `file` - manage files and file properties
* `find` - return a list of files based on specific criteria
* [`gather_facts`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/gather_facts_module.html#ansible-collections-ansible-builtin-gather-facts-module) - gathers facts about remote hosts
* [`get_url`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/get_url_module.html#ansible-collections-ansible-builtin-get-url-module) - downloads files from HTTP, HTTPS, or FTP to node
* [`getent`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/getent_module.html#ansible-collections-ansible-builtin-getent-module) - A wrapper to the unix getent utility
* [`git`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html#ansible-collections-ansible-builtin-git-module) - deploy software (or files) from git checkouts
* [`group`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/group_module.html#ansible-collections-ansible-builtin-group-module) - add or remove groups
* [`group_by`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/group_by_module.html#ansible-collections-ansible-builtin-group-by-module) - Create Ansible groups based on facts
- [`hostname`](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/hostname_module.html#ansible-collections-ansible-builtin-hostname-module) - manage hostname
- [import_playbook](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_playbook_module.html#ansible-collections-ansible-builtin-import-playbook-module) - import a playbook
- [import_role](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_role_module.html#ansible-collections-ansible-builtin-import-role-module) - import a role into a play
- [import_tasks](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_tasks_module.html#ansible-collections-ansible-builtin-import-tasks-module) - import a task list
- [include](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_module.html#ansible-collections-ansible-builtin-include-module) - include a task list
- [include_role](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_role_module.html#ansible-collections-ansible-builtin-include-role-module) - load and execute a role
- [include_tasks](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_tasks_module.html#ansible-collections-ansible-builtin-include-tasks-module) - dynamically include a task list
- [include_vars](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_vars_module.html#ansible-collections-ansible-builtin-include-vars-module) - load variables from files, dynamically within a task
- [iptables](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/iptables_module.html#ansible-collections-ansible-builtin-iptables-module) - modify iptables rules
- [known_hosts](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/known_hosts_module.html#ansible-collections-ansible-builtin-known-hosts-module) - add or remove a host from the `known_hosts` file
- [lineinfile](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html#ansible-collections-ansible-builtin-lineinfile-module) - manage lines in text files
- [meta](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/meta_module.html#ansible-collections-ansible-builtin-meta-module) - execute Ansible ‘actions’
- [package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html#ansible-collections-ansible-builtin-package-module) - generic OS package manager
- [package_facts](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_facts_module.html#ansible-collections-ansible-builtin-package-facts-module) - package information as facts
- [pause](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pause_module.html#ansible-collections-ansible-builtin-pause-module) - pause playbook execution
- [ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html#ansible-collections-ansible-builtin-ping-module) - try to connect to host, verify a usable python and return `pong` on success
- [pip](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html#ansible-collections-ansible-builtin-pip-module) - manages Python library dependencies
- [raw](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/raw_module.html#ansible-collections-ansible-builtin-raw-module) - executes a low-down and dirty command
- [reboot](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/reboot_module.html#ansible-collections-ansible-builtin-reboot-module) - reboot a machine
- [replace](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/replace_module.html#ansible-collections-ansible-builtin-replace-module) - replace all instances of a particular string in a file using a back-referenced regular expression
- [rpm_key](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/rpm_key_module.html#ansible-collections-ansible-builtin-rpm-key-module) - adds or removes a gpg key from the rpm db
- [script](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/script_module.html#ansible-collections-ansible-builtin-script-module) - runs a local script on a remote node after transferring it
- [service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html#ansible-collections-ansible-builtin-service-module) - manage services
- [service_facts](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_facts_module.html#ansible-collections-ansible-builtin-service-facts-module) - return service state information as fact data
- [set_fact](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/set_fact_module.html#ansible-collections-ansible-builtin-set-fact-module) - set host variable(s) and fact(s).
- [set_stats](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/set_stats_module.html#ansible-collections-ansible-builtin-set-stats-module) - define and display stats for the current ansible run
- [setup](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module) - gathers facts about remote hosts
- [shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html#ansible-collections-ansible-builtin-shell-module) - execute shell commands on targets
- [slurp](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/slurp_module.html#ansible-collections-ansible-builtin-slurp-module) - slurps a file from remote nodes
- [stat](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/stat_module.html#ansible-collections-ansible-builtin-stat-module) - retrieve file or file system status
- [systemd](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/systemd_module.html#ansible-collections-ansible-builtin-systemd-module) - manage systemd units
- [systemd_service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/systemd_service_module.html#ansible-collections-ansible-builtin-systemd-service-module) - manage systemd units
- [sysvinit](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/sysvinit_module.html#ansible-collections-ansible-builtin-sysvinit-module) - manage SysV services.
- [tempfile](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/tempfile_module.html#ansible-collections-ansible-builtin-tempfile-module) - creates temporary files and directories
- [template](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#ansible-collections-ansible-builtin-template-module) - template a file out to a target host
- [unarchive](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/unarchive_module.html#ansible-collections-ansible-builtin-unarchive-module) - unpacks an archive after (optionally) copying it from the local machine
- [uri](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html#ansible-collections-ansible-builtin-uri-module) - interacts with webservices
- [user](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html#ansible-collections-ansible-builtin-user-module) - manage user accounts
- [validate_argument_spec](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/validate_argument_spec_module.html#ansible-collections-ansible-builtin-validate-argument-spec-module) - validate role argument specs.
- [wait_for](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/wait_for_module.html#ansible-collections-ansible-builtin-wait-for-module) - waits for a condition before continuing
- [wait_for_connection](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/wait_for_connection_module.html#ansible-collections-ansible-builtin-wait-for-connection-module) - waits until remote system is reachable/usable
- [yum](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html#ansible-collections-ansible-builtin-yum-module) - manages packages with the _yum_ package manager
- [yum_repository](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_repository_module.html#ansible-collections-ansible-builtin-yum-repository-module) - add or remove YUM repositories

#### `ansible.netcommon`
- [cli_command](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/cli_command_module.html#ansible-collections-ansible-netcommon-cli-command-module) - run a cli command on cli-based network devices
- [cli_config](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/cli_config_module.html#ansible-collections-ansible-netcommon-cli-config-module) - push text based configuration to network devices over network_cli
- [grpc_config](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/grpc_config_module.html#ansible-collections-ansible-netcommon-grpc-config-module) - fetch configuration/state data from gRPC enabled target hosts.
- [grpc_get](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/grpc_get_module.html#ansible-collections-ansible-netcommon-grpc-get-module) - fetch configuration/state data from gRPC enabled target hosts.
- [net_get](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_get_module.html#ansible-collections-ansible-netcommon-net-get-module) - copy a file from a network device to Ansible Controller
- [net_ping](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html#ansible-collections-ansible-netcommon-net-ping-module) - tests reachability using ping from a network device
- [net_put](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_put_module.html#ansible-collections-ansible-netcommon-net-put-module) - copy a file from Ansible Controller to a network device
- [netconf_config](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/netconf_config_module.html#ansible-collections-ansible-netcommon-netconf-config-module) - netconf device configuration
- [netconf_get](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/netconf_get_module.html#ansible-collections-ansible-netcommon-netconf-get-module) - fetch configuration/state data from NETCONF enabled network devices.
- [netconf_rpc](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/netconf_rpc_module.html#ansible-collections-ansible-netcommon-netconf-rpc-module) - execute operations on NETCONF enabled network devices.
- [network_resource](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/network_resource_module.html#ansible-collections-ansible-netcommon-network-resource-module) - manage resource modules
- [restconf_config](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/restconf_config_module.html#ansible-collections-ansible-netcommon-restconf-config-module) - handles create, update, read and delete of configuration data on RESTCONF enabled devices.
- [restconf_get](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/restconf_get_module.html#ansible-collections-ansible-netcommon-restconf-get-module) - fetch configuration/state data from RESTCONF enabled devices.
- [telnet](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/telnet_module.html#ansible-collections-ansible-netcommon-telnet-module) - executes a low-down and dirty telnet command

#### `ansible.posix`
- [acl](https://docs.ansible.com/ansible/latest/collections/ansible/posix/acl_module.html#ansible-collections-ansible-posix-acl-module) - set and retrieve file ACL information.
- [at](https://docs.ansible.com/ansible/latest/collections/ansible/posix/at_module.html#ansible-collections-ansible-posix-at-module) - schedule the execution of a command or script file via the at command
- [authorized_key](https://docs.ansible.com/ansible/latest/collections/ansible/posix/authorized_key_module.html#ansible-collections-ansible-posix-authorized-key-module) - adds or removes an SSH authorized key
- [firewalld](https://docs.ansible.com/ansible/latest/collections/ansible/posix/firewalld_module.html#ansible-collections-ansible-posix-firewalld-module) - manage arbitrary ports/services with firewalld
- [firewalld_info](https://docs.ansible.com/ansible/latest/collections/ansible/posix/firewalld_info_module.html#ansible-collections-ansible-posix-firewalld-info-module) - gather information about firewalld
- [mount](https://docs.ansible.com/ansible/latest/collections/ansible/posix/mount_module.html#ansible-collections-ansible-posix-mount-module) - control active and configured mount points
- [patch](https://docs.ansible.com/ansible/latest/collections/ansible/posix/patch_module.html#ansible-collections-ansible-posix-patch-module) - apply patch files using the GNU patch tool
- [rhel_facts](https://docs.ansible.com/ansible/latest/collections/ansible/posix/rhel_facts_module.html#ansible-collections-ansible-posix-rhel-facts-module) - facts module to set or override RHEL specific facts.
- [rhel_rpm_ostree](https://docs.ansible.com/ansible/latest/collections/ansible/posix/rhel_rpm_ostree_module.html#ansible-collections-ansible-posix-rhel-rpm-ostree-module) - ensure packages exist in a RHEL for Edge rpm-ostree based system
- [rpm_ostree_upgrade](https://docs.ansible.com/ansible/latest/collections/ansible/posix/rpm_ostree_upgrade_module.html#ansible-collections-ansible-posix-rpm-ostree-upgrade-module) - manage rpm-ostree upgrade transactions
- [seboolean](https://docs.ansible.com/ansible/latest/collections/ansible/posix/seboolean_module.html#ansible-collections-ansible-posix-seboolean-module) - toggles SELinux booleans
- [selinux](https://docs.ansible.com/ansible/latest/collections/ansible/posix/selinux_module.html#ansible-collections-ansible-posix-selinux-module) - change policy and state of SELinux
- [synchronize](https://docs.ansible.com/ansible/latest/collections/ansible/posix/synchronize_module.html#ansible-collections-ansible-posix-synchronize-module) - a wrapper around rsync to make common tasks in your playbooks quick and easy
- [sysctl](https://docs.ansible.com/ansible/latest/collections/ansible/posix/sysctl_module.html#ansible-collections-ansible-posix-sysctl-module) - manage entries in sysctl.conf.

#### `ansible.utils`
- [cli_parse](https://docs.ansible.com/ansible/latest/collections/ansible/utils/cli_parse_module.html#ansible-collections-ansible-utils-cli-parse-module) - parse cli output or text using a variety of parsers
- [fact_diff](https://docs.ansible.com/ansible/latest/collections/ansible/utils/fact_diff_module.html#ansible-collections-ansible-utils-fact-diff-module) - find the difference between currently set facts
- [update_fact](https://docs.ansible.com/ansible/latest/collections/ansible/utils/update_fact_module.html#ansible-collections-ansible-utils-update-fact-module) - update currently set facts
- [validate](https://docs.ansible.com/ansible/latest/collections/ansible/utils/validate_module.html#ansible-collections-ansible-utils-validate-module) - validate data with provided criteria

#### `community.crypto`
- [acme_account](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_account_module.html#ansible-collections-community-crypto-acme-account-module) - create, modify or delete ACME accounts
- [acme_account_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_account_info_module.html#ansible-collections-community-crypto-acme-account-info-module) - retrieves information on ACME accounts
- [acme_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_certificate_module.html#ansible-collections-community-crypto-acme-certificate-module) - create SSL/TLS certificates with the ACME protocol
- [acme_certificate_revoke](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_certificate_revoke_module.html#ansible-collections-community-crypto-acme-certificate-revoke-module) - revoke certificates with the ACME protocol
- [acme_challenge_cert_helper](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_challenge_cert_helper_module.html#ansible-collections-community-crypto-acme-challenge-cert-helper-module) - prepare certificates required for ACME challenges such as `tls-alpn-01`
- [acme_inspect](https://docs.ansible.com/ansible/latest/collections/community/crypto/acme_inspect_module.html#ansible-collections-community-crypto-acme-inspect-module) - send direct requests to an ACME server
- [certificate_complete_chain](https://docs.ansible.com/ansible/latest/collections/community/crypto/certificate_complete_chain_module.html#ansible-collections-community-crypto-certificate-complete-chain-module) - complete certificate chain given a set of untrusted and root certificates
- [crypto_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/crypto_info_module.html#ansible-collections-community-crypto-crypto-info-module) - retrieve cryptographic capabilities
- [ecs_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/ecs_certificate_module.html#ansible-collections-community-crypto-ecs-certificate-module) - request SSL/TLS certificates with the Entrust Certificate Services (ECS) API
- [ecs_domain](https://docs.ansible.com/ansible/latest/collections/community/crypto/ecs_domain_module.html#ansible-collections-community-crypto-ecs-domain-module) - request validation of a domain with the Entrust Certificate Services (ECS) API
- [get_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/get_certificate_module.html#ansible-collections-community-crypto-get-certificate-module) - get a certificate from a host:port
- [luks_device](https://docs.ansible.com/ansible/latest/collections/community/crypto/luks_device_module.html#ansible-collections-community-crypto-luks-device-module) - manage encrypted (LUKS) devices
- [openssh_cert](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_cert_module.html#ansible-collections-community-crypto-openssh-cert-module) - generate OpenSSH host or user certificates.
- [openssh_keypair](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_keypair_module.html#ansible-collections-community-crypto-openssh-keypair-module) - generate OpenSSH private and public keys
- [openssl_csr](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_csr_module.html#ansible-collections-community-crypto-openssl-csr-module) - generate OpenSSL Certificate Signing Request (CSR)
- [openssl_csr_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_csr_info_module.html#ansible-collections-community-crypto-openssl-csr-info-module) - provide information of OpenSSL Certificate Signing Requests (CSR)
- [openssl_csr_pipe](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_csr_pipe_module.html#ansible-collections-community-crypto-openssl-csr-pipe-module) - generate OpenSSL Certificate Signing Request (CSR)
- [openssl_dhparam](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_dhparam_module.html#ansible-collections-community-crypto-openssl-dhparam-module) - generate OpenSSL Diffie-Hellman Parameters
- [openssl_pkcs12](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_pkcs12_module.html#ansible-collections-community-crypto-openssl-pkcs12-module) - generate OpenSSL PKCS#12 archive
- [openssl_privatekey](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_privatekey_module.html#ansible-collections-community-crypto-openssl-privatekey-module) - generate OpenSSL private keys
- [openssl_privatekey_convert](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_privatekey_convert_module.html#ansible-collections-community-crypto-openssl-privatekey-convert-module) - convert OpenSSL private keys
- [openssl_privatekey_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_privatekey_info_module.html#ansible-collections-community-crypto-openssl-privatekey-info-module) - provide information for OpenSSL private keys
- [openssl_privatekey_pipe](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_privatekey_pipe_module.html#ansible-collections-community-crypto-openssl-privatekey-pipe-module) - generate OpenSSL private keys without disk access
- [openssl_publickey](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_publickey_module.html#ansible-collections-community-crypto-openssl-publickey-module) - generate an OpenSSL public key from its private key.
- [openssl_publickey_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_publickey_info_module.html#ansible-collections-community-crypto-openssl-publickey-info-module) - provide information for OpenSSL public keys
- [openssl_signature](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_signature_module.html#ansible-collections-community-crypto-openssl-signature-module) - sign data with openssl
- [openssl_signature_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssl_signature_info_module.html#ansible-collections-community-crypto-openssl-signature-info-module) - verify signatures with openssl
- [x509_certificate](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_certificate_module.html#ansible-collections-community-crypto-x509-certificate-module) - generate and/or check OpenSSL certificates
- [x509_certificate_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_certificate_info_module.html#ansible-collections-community-crypto-x509-certificate-info-module) - provide information of OpenSSL X.509 certificates
- [x509_certificate_pipe](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_certificate_pipe_module.html#ansible-collections-community-crypto-x509-certificate-pipe-module) - generate and/or check OpenSSL certificates
- [x509_crl](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_crl_module.html#ansible-collections-community-crypto-x509-crl-module) - generate Certificate Revocation Lists (CRLs)
- [x509_crl_info](https://docs.ansible.com/ansible/latest/collections/community/crypto/x509_crl_info_module.html#ansible-collections-community-crypto-x509-crl-info-module) - retrieve information on Certificate Revocation Lists (CRLs)

#### `community.dns`
- [hetzner_dns_record](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_record_module.html#ansible-collections-community-dns-hetzner-dns-record-module) - add or delete a single record in Hetzner DNS service
- [hetzner_dns_record_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_record_info_module.html#ansible-collections-community-dns-hetzner-dns-record-info-module) - retrieve records in Hetzner DNS service
- [hetzner_dns_record_set](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_record_set_module.html#ansible-collections-community-dns-hetzner-dns-record-set-module) - add or delete record sets in Hetzner DNS service
- [hetzner_dns_record_set_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_record_set_info_module.html#ansible-collections-community-dns-hetzner-dns-record-set-info-module) - retrieve record sets in Hetzner DNS service
- [hetzner_dns_record_sets](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_record_sets_module.html#ansible-collections-community-dns-hetzner-dns-record-sets-module) - bulk synchronize DNS record sets in Hetzner DNS service
- [hetzner_dns_zone_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hetzner_dns_zone_info_module.html#ansible-collections-community-dns-hetzner-dns-zone-info-module) - retrieve zone information in Hetzner DNS service
- [hosttech_dns_record](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_record_module.html#ansible-collections-community-dns-hosttech-dns-record-module) - add or delete a single record in Hosttech DNS service
- [hosttech_dns_record_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_record_info_module.html#ansible-collections-community-dns-hosttech-dns-record-info-module) - retrieve records in Hosttech DNS service
- [hosttech_dns_record_set](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_record_set_module.html#ansible-collections-community-dns-hosttech-dns-record-set-module) - add or delete record sets in Hosttech DNS service
- [hosttech_dns_record_set_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_record_set_info_module.html#ansible-collections-community-dns-hosttech-dns-record-set-info-module) - retrieve record sets in Hosttech DNS service
- [hosttech_dns_record_sets](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_record_sets_module.html#ansible-collections-community-dns-hosttech-dns-record-sets-module) - bulk synchronize DNS record sets in Hosttech DNS service
- [hosttech_dns_zone_info](https://docs.ansible.com/ansible/latest/collections/community/dns/hosttech_dns_zone_info_module.html#ansible-collections-community-dns-hosttech-dns-zone-info-module) - retrieve zone information in Hosttech DNS service
- [wait_for_txt](https://docs.ansible.com/ansible/latest/collections/community/dns/wait_for_txt_module.html#ansible-collections-community-dns-wait-for-txt-module) - wait for TXT entries to be available on all authoritative nameservers

#### `community.docker`
- [current_container_facts](https://docs.ansible.com/ansible/latest/collections/community/docker/current_container_facts_module.html#ansible-collections-community-docker-current-container-facts-module) - return facts about whether the module runs in a container
- [docker_compose](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_compose_module.html#ansible-collections-community-docker-docker-compose-module) - manage multi-container Docker applications with Docker Compose.
- [docker_config](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_config_module.html#ansible-collections-community-docker-docker-config-module) - manage docker configs.
- [docker_container](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html#ansible-collections-community-docker-docker-container-module) - manage Docker containers
- [docker_container_copy_into](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_copy_into_module.html#ansible-collections-community-docker-docker-container-copy-into-module) - copy a file into a Docker container
- [docker_container_exec](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_exec_module.html#ansible-collections-community-docker-docker-container-exec-module) - execute command in a docker container
- [docker_container_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_info_module.html#ansible-collections-community-docker-docker-container-info-module) - retrieves facts about docker container
- [docker_host_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_host_info_module.html#ansible-collections-community-docker-docker-host-info-module) - retrieves facts about docker host and lists of objects of the services.
- [docker_image](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_module.html#ansible-collections-community-docker-docker-image-module) - manage docker images
- [docker_image_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_info_module.html#ansible-collections-community-docker-docker-image-info-module) - inspect docker images
- [docker_image_load](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_load_module.html#ansible-collections-community-docker-docker-image-load-module) - load docker image(s) from archives
- [docker_login](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_login_module.html#ansible-collections-community-docker-docker-login-module) - log into a Docker registry.
- [docker_network](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_network_module.html#ansible-collections-community-docker-docker-network-module) - manage Docker networks
- [docker_network_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_network_info_module.html#ansible-collections-community-docker-docker-network-info-module) - retrieves facts about docker network
- [docker_node](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_node_module.html#ansible-collections-community-docker-docker-node-module) - manage Docker Swarm node
- [docker_node_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_node_info_module.html#ansible-collections-community-docker-docker-node-info-module) - retrieves facts about docker swarm node from Swarm Manager
- [docker_plugin](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_plugin_module.html#ansible-collections-community-docker-docker-plugin-module) - manage Docker plugins
- [docker_prune](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_prune_module.html#ansible-collections-community-docker-docker-prune-module) - allows to prune various docker objects
- [docker_secret](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_secret_module.html#ansible-collections-community-docker-docker-secret-module) - manage docker secrets.
- [docker_stack](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_stack_module.html#ansible-collections-community-docker-docker-stack-module) - docker stack module
- [docker_stack_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_stack_info_module.html#ansible-collections-community-docker-docker-stack-info-module) - return information on a docker stack
- [docker_stack_task_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_stack_task_info_module.html#ansible-collections-community-docker-docker-stack-task-info-module) - return information of the tasks on a docker stack
- [docker_swarm](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_swarm_module.html#ansible-collections-community-docker-docker-swarm-module) - manage Swarm cluster
- [docker_swarm_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_swarm_info_module.html#ansible-collections-community-docker-docker-swarm-info-module) - retrieves facts about Docker Swarm cluster.
- [docker_swarm_service](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_swarm_service_module.html#ansible-collections-community-docker-docker-swarm-service-module) - docker swarm service
- [docker_swarm_service_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_swarm_service_info_module.html#ansible-collections-community-docker-docker-swarm-service-info-module) - retrieves information about docker services from a Swarm Manager
- [docker_volume](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_volume_module.html#ansible-collections-community-docker-docker-volume-module) - manage Docker volumes
- [docker_volume_info](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_volume_info_module.html#ansible-collections-community-docker-docker-volume-info-module) - retrieve facts about Docker volumes

#### `community.general`
- [aerospike_migrations](https://docs.ansible.com/ansible/latest/collections/community/general/aerospike_migrations_module.html#ansible-collections-community-general-aerospike-migrations-module) - check or wait for migrations between nodes
- [alternatives](https://docs.ansible.com/ansible/latest/collections/community/general/alternatives_module.html#ansible-collections-community-general-alternatives-module) - manages alternative programs for common commands
- [ansible_galaxy_install](https://docs.ansible.com/ansible/latest/collections/community/general/ansible_galaxy_install_module.html#ansible-collections-community-general-ansible-galaxy-install-module) - install Ansible roles or collections using ansible-galaxy
- [apache2_mod_proxy](https://docs.ansible.com/ansible/latest/collections/community/general/apache2_mod_proxy_module.html#ansible-collections-community-general-apache2-mod-proxy-module) - set and/or get members’ attributes of an Apache httpd 2.4 mod_proxy balancer pool
- [apache2_module](https://docs.ansible.com/ansible/latest/collections/community/general/apache2_module_module.html#ansible-collections-community-general-apache2-module-module) - enables/disables a module of the Apache2 webserver
- [apt_repo](https://docs.ansible.com/ansible/latest/collections/community/general/apt_repo_module.html#ansible-collections-community-general-apt-repo-module) - manage APT repositories via apt-repo
- [apt_rpm](https://docs.ansible.com/ansible/latest/collections/community/general/apt_rpm_module.html#ansible-collections-community-general-apt-rpm-module) - aPT-RPM package manager
- [archive](https://docs.ansible.com/ansible/latest/collections/community/general/archive_module.html#ansible-collections-community-general-archive-module) - creates a compressed archive of one or more files or trees
- [btrfs_info](https://docs.ansible.com/ansible/latest/collections/community/general/btrfs_info_module.html#ansible-collections-community-general-btrfs-info-module) - query btrfs filesystem info
- [btrfs_subvolume](https://docs.ansible.com/ansible/latest/collections/community/general/btrfs_subvolume_module.html#ansible-collections-community-general-btrfs-subvolume-module) - manage btrfs subvolumes
- [capabilities](https://docs.ansible.com/ansible/latest/collections/community/general/capabilities_module.html#ansible-collections-community-general-capabilities-module) - manage Linux capabilities
- [cloud_init_data_facts](https://docs.ansible.com/ansible/latest/collections/community/general/cloud_init_data_facts_module.html#ansible-collections-community-general-cloud-init-data-facts-module) - retrieve facts of cloud-init
- [cronvar](https://docs.ansible.com/ansible/latest/collections/community/general/cronvar_module.html#ansible-collections-community-general-cronvar-module) - manage variables in crontabs
- [crypttab](https://docs.ansible.com/ansible/latest/collections/community/general/crypttab_module.html#ansible-collections-community-general-crypttab-module) - encrypted Linux block devices
- [dconf](https://docs.ansible.com/ansible/latest/collections/community/general/dconf_module.html#ansible-collections-community-general-dconf-module) - modify and read dconf database
- [deploy_helper](https://docs.ansible.com/ansible/latest/collections/community/general/deploy_helper_module.html#ansible-collections-community-general-deploy-helper-module) - manages some of the steps common in deploying projects
- [django_manage](https://docs.ansible.com/ansible/latest/collections/community/general/django_manage_module.html#ansible-collections-community-general-django-manage-module) - manages a Django application
- [dnf_versionlock](https://docs.ansible.com/ansible/latest/collections/community/general/dnf_versionlock_module.html#ansible-collections-community-general-dnf-versionlock-module) - locks package versions in `dnf` based systems
- [dnsimple](https://docs.ansible.com/ansible/latest/collections/community/general/dnsimple_module.html#ansible-collections-community-general-dnsimple-module) - interface with dnsimple.com (a DNS hosting service)
- [dnsimple_info](https://docs.ansible.com/ansible/latest/collections/community/general/dnsimple_info_module.html#ansible-collections-community-general-dnsimple-info-module) - pull basic info from DNSimple API
- [dnsmadeeasy](https://docs.ansible.com/ansible/latest/collections/community/general/dnsmadeeasy_module.html#ansible-collections-community-general-dnsmadeeasy-module) - interface with dnsmadeeasy.com (a DNS hosting service)
- [dpkg_divert](https://docs.ansible.com/ansible/latest/collections/community/general/dpkg_divert_module.html#ansible-collections-community-general-dpkg-divert-module) - override a debian package’s version of a file
- [easy_install](https://docs.ansible.com/ansible/latest/collections/community/general/easy_install_module.html#ansible-collections-community-general-easy-install-module) - installs Python libraries
- [elasticsearch_plugin](https://docs.ansible.com/ansible/latest/collections/community/general/elasticsearch_plugin_module.html#ansible-collections-community-general-elasticsearch-plugin-module) - manage Elasticsearch plugins
- [etcd3](https://docs.ansible.com/ansible/latest/collections/community/general/etcd3_module.html#ansible-collections-community-general-etcd3-module) - set or delete key value pairs from an etcd3 cluster
- [filesize](https://docs.ansible.com/ansible/latest/collections/community/general/filesize_module.html#ansible-collections-community-general-filesize-module) - create a file with a given size, or resize it if it exists
- [filesystem](https://docs.ansible.com/ansible/latest/collections/community/general/filesystem_module.html#ansible-collections-community-general-filesystem-module) - makes a filesystem
- [gconftool2](https://docs.ansible.com/ansible/latest/collections/community/general/gconftool2_module.html#ansible-collections-community-general-gconftool2-module) - edit GNOME Configurations
- [gconftool2_info](https://docs.ansible.com/ansible/latest/collections/community/general/gconftool2_info_module.html#ansible-collections-community-general-gconftool2-info-module) - retrieve GConf configurations
- [git_config](https://docs.ansible.com/ansible/latest/collections/community/general/git_config_module.html#ansible-collections-community-general-git-config-module) - read and write git configuration
- [github_deploy_key](https://docs.ansible.com/ansible/latest/collections/community/general/github_deploy_key_module.html#ansible-collections-community-general-github-deploy-key-module) - manages deploy keys for GitHub repositories
- [github_issue](https://docs.ansible.com/ansible/latest/collections/community/general/github_issue_module.html#ansible-collections-community-general-github-issue-module) - view GitHub issue
- [github_key](https://docs.ansible.com/ansible/latest/collections/community/general/github_key_module.html#ansible-collections-community-general-github-key-module) - manage GitHub access keys
- [github_release](https://docs.ansible.com/ansible/latest/collections/community/general/github_release_module.html#ansible-collections-community-general-github-release-module) - interact with GitHub Releases
- [github_repo](https://docs.ansible.com/ansible/latest/collections/community/general/github_repo_module.html#ansible-collections-community-general-github-repo-module) - manage your repositories on Github
- [github_webhook](https://docs.ansible.com/ansible/latest/collections/community/general/github_webhook_module.html#ansible-collections-community-general-github-webhook-module) - manage GitHub webhooks
- [github_webhook_info](https://docs.ansible.com/ansible/latest/collections/community/general/github_webhook_info_module.html#ansible-collections-community-general-github-webhook-info-module) - query information about GitHub webhooks
- [gitlab_branch](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_branch_module.html#ansible-collections-community-general-gitlab-branch-module) - create or delete a branch
- [gitlab_deploy_key](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_deploy_key_module.html#ansible-collections-community-general-gitlab-deploy-key-module) - manages GitLab project deploy keys
- [gitlab_group](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_group_module.html#ansible-collections-community-general-gitlab-group-module) - creates/updates/deletes GitLab Groups
- [gitlab_group_members](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_group_members_module.html#ansible-collections-community-general-gitlab-group-members-module) - manage group members on GitLab Server
- [gitlab_group_variable](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_group_variable_module.html#ansible-collections-community-general-gitlab-group-variable-module) - creates, updates, or deletes GitLab groups variables
- [gitlab_hook](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_hook_module.html#ansible-collections-community-general-gitlab-hook-module) - manages GitLab project hooks
- [gitlab_project](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_project_module.html#ansible-collections-community-general-gitlab-project-module) - creates/updates/deletes GitLab Projects
- [gitlab_project_badge](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_project_badge_module.html#ansible-collections-community-general-gitlab-project-badge-module) - manage project badges on GitLab Server
- [gitlab_project_members](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_project_members_module.html#ansible-collections-community-general-gitlab-project-members-module) - manage project members on GitLab Server
- [gitlab_project_variable](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_project_variable_module.html#ansible-collections-community-general-gitlab-project-variable-module) - creates/updates/deletes GitLab Projects Variables
- [gitlab_protected_branch](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_protected_branch_module.html#ansible-collections-community-general-gitlab-protected-branch-module) - manage protection of existing branches
- [gitlab_runner](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_runner_module.html#ansible-collections-community-general-gitlab-runner-module) - create, modify and delete GitLab Runners
- [gitlab_user](https://docs.ansible.com/ansible/latest/collections/community/general/gitlab_user_module.html#ansible-collections-community-general-gitlab-user-module) - creates/updates/deletes/blocks/unblocks GitLab Users
- [haproxy](https://docs.ansible.com/ansible/latest/collections/community/general/haproxy_module.html#ansible-collections-community-general-haproxy-module) - enable, disable, and set weights for HAProxy backend servers using socket commands
- [heroku_collaborator](https://docs.ansible.com/ansible/latest/collections/community/general/heroku_collaborator_module.html#ansible-collections-community-general-heroku-collaborator-module) - add or delete app collaborators on Heroku
- [homectl](https://docs.ansible.com/ansible/latest/collections/community/general/homectl_module.html#ansible-collections-community-general-homectl-module) - manage user accounts with systemd-homed
- [htpasswd](https://docs.ansible.com/ansible/latest/collections/community/general/htpasswd_module.html#ansible-collections-community-general-htpasswd-module) - manage user files for basic authentication
- [ini_file](https://docs.ansible.com/ansible/latest/collections/community/general/ini_file_module.html#ansible-collections-community-general-ini-file-module) - tweak settings in INI files
- [interfaces_file](https://docs.ansible.com/ansible/latest/collections/community/general/interfaces_file_module.html#ansible-collections-community-general-interfaces-file-module) - tweak settings in /etc/network/interfaces files
- [ip_netns](https://docs.ansible.com/ansible/latest/collections/community/general/ip_netns_module.html#ansible-collections-community-general-ip-netns-module) - manage network namespaces
- [ipbase_info](https://docs.ansible.com/ansible/latest/collections/community/general/ipbase_info_module.html#ansible-collections-community-general-ipbase-info-module) - retrieve IP geolocation and other facts of a host’s IP address using the ipbase.com API
- [ipify_facts](https://docs.ansible.com/ansible/latest/collections/community/general/ipify_facts_module.html#ansible-collections-community-general-ipify-facts-module) - retrieve the public IP of your internet gateway
- [ipinfoio_facts](https://docs.ansible.com/ansible/latest/collections/community/general/ipinfoio_facts_module.html#ansible-collections-community-general-ipinfoio-facts-module) - retrieve IP geolocation facts of a host’s IP address
- [ipmi_boot](https://docs.ansible.com/ansible/latest/collections/community/general/ipmi_boot_module.html#ansible-collections-community-general-ipmi-boot-module) - management of order of boot devices
- [ipmi_power](https://docs.ansible.com/ansible/latest/collections/community/general/ipmi_power_module.html#ansible-collections-community-general-ipmi-power-module) - power management for machine
- [iptables_state](https://docs.ansible.com/ansible/latest/collections/community/general/iptables_state_module.html#ansible-collections-community-general-iptables-state-module) - save iptables state into a file or restore it from a file
- [irc](https://docs.ansible.com/ansible/latest/collections/community/general/irc_module.html#ansible-collections-community-general-irc-module) - send a message to an IRC channel or a nick
- [iso_create](https://docs.ansible.com/ansible/latest/collections/community/general/iso_create_module.html#ansible-collections-community-general-iso-create-module) - generate ISO file with specified files or folders
- [iso_customize](https://docs.ansible.com/ansible/latest/collections/community/general/iso_customize_module.html#ansible-collections-community-general-iso-customize-module) - add/remove/change files in ISO file
- [iso_extract](https://docs.ansible.com/ansible/latest/collections/community/general/iso_extract_module.html#ansible-collections-community-general-iso-extract-module) - extract files from an ISO image
- [jenkins_build](https://docs.ansible.com/ansible/latest/collections/community/general/jenkins_build_module.html#ansible-collections-community-general-jenkins-build-module) - manage jenkins builds
- [jenkins_job](https://docs.ansible.com/ansible/latest/collections/community/general/jenkins_job_module.html#ansible-collections-community-general-jenkins-job-module) - manage jenkins jobs
- [jenkins_job_info](https://docs.ansible.com/ansible/latest/collections/community/general/jenkins_job_info_module.html#ansible-collections-community-general-jenkins-job-info-module) - get information about Jenkins jobs
- [jenkins_plugin](https://docs.ansible.com/ansible/latest/collections/community/general/jenkins_plugin_module.html#ansible-collections-community-general-jenkins-plugin-module) - add or remove Jenkins plugin
- [jenkins_script](https://docs.ansible.com/ansible/latest/collections/community/general/jenkins_script_module.html#ansible-collections-community-general-jenkins-script-module) - executes a groovy script in the jenkins instance
- [kdeconfig](https://docs.ansible.com/ansible/latest/collections/community/general/kdeconfig_module.html#ansible-collections-community-general-kdeconfig-module) - manage KDE configuration files
- [kernel_blacklist](https://docs.ansible.com/ansible/latest/collections/community/general/kernel_blacklist_module.html#ansible-collections-community-general-kernel-blacklist-module) - blacklist kernel modules
- [keyring](https://docs.ansible.com/ansible/latest/collections/community/general/keyring_module.html#ansible-collections-community-general-keyring-module) - set or delete a passphrase using the Operating System’s native keyring
- [keyring_info](https://docs.ansible.com/ansible/latest/collections/community/general/keyring_info_module.html#ansible-collections-community-general-keyring-info-module) - get a passphrase using the Operating System’s native keyring
- [kibana_plugin](https://docs.ansible.com/ansible/latest/collections/community/general/kibana_plugin_module.html#ansible-collections-community-general-kibana-plugin-module) - manage Kibana plugins
- [ldap_attrs](https://docs.ansible.com/ansible/latest/collections/community/general/ldap_attrs_module.html#ansible-collections-community-general-ldap-attrs-module) - add or remove multiple LDAP attribute values
- [ldap_entry](https://docs.ansible.com/ansible/latest/collections/community/general/ldap_entry_module.html#ansible-collections-community-general-ldap-entry-module) - add or remove LDAP entries
- [ldap_passwd](https://docs.ansible.com/ansible/latest/collections/community/general/ldap_passwd_module.html#ansible-collections-community-general-ldap-passwd-module) - set passwords in LDAP
- [ldap_search](https://docs.ansible.com/ansible/latest/collections/community/general/ldap_search_module.html#ansible-collections-community-general-ldap-search-module) - search for entries in a LDAP server
- [listen_ports_facts](https://docs.ansible.com/ansible/latest/collections/community/general/listen_ports_facts_module.html#ansible-collections-community-general-listen-ports-facts-module) - gather facts on processes listening on TCP and UDP ports
- [locale_gen](https://docs.ansible.com/ansible/latest/collections/community/general/locale_gen_module.html#ansible-collections-community-general-locale-gen-module) - creates or removes locales
- [lvg](https://docs.ansible.com/ansible/latest/collections/community/general/lvg_module.html#ansible-collections-community-general-lvg-module) - configure LVM volume groups
- [lvol](https://docs.ansible.com/ansible/latest/collections/community/general/lvol_module.html#ansible-collections-community-general-lvol-module) - configure LVM logical volumes
- [lxc_container](https://docs.ansible.com/ansible/latest/collections/community/general/lxc_container_module.html#ansible-collections-community-general-lxc-container-module) - manage LXC Containers
- [lxca_cmms](https://docs.ansible.com/ansible/latest/collections/community/general/lxca_cmms_module.html#ansible-collections-community-general-lxca-cmms-module) - custom module for lxca cmms inventory utility
- [lxca_nodes](https://docs.ansible.com/ansible/latest/collections/community/general/lxca_nodes_module.html#ansible-collections-community-general-lxca-nodes-module) - custom module for lxca nodes inventory utility
- [lxd_container](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html#ansible-collections-community-general-lxd-container-module) - manage LXD instances
- [lxd_profile](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_profile_module.html#ansible-collections-community-general-lxd-profile-module) - manage LXD profiles
- [lxd_project](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_project_module.html#ansible-collections-community-general-lxd-project-module) - manage LXD projects
- [mail](https://docs.ansible.com/ansible/latest/collections/community/general/mail_module.html#ansible-collections-community-general-mail-module) - send an email
- [make](https://docs.ansible.com/ansible/latest/collections/community/general/make_module.html#ansible-collections-community-general-make-module) - run targets in a Makefile
- [modprobe](https://docs.ansible.com/ansible/latest/collections/community/general/modprobe_module.html#ansible-collections-community-general-modprobe-module) - load or unload kernel modules
- [nginx_status_info](https://docs.ansible.com/ansible/latest/collections/community/general/nginx_status_info_module.html#ansible-collections-community-general-nginx-status-info-module) - retrieve information on nginx status
- [nmcli](https://docs.ansible.com/ansible/latest/collections/community/general/nmcli_module.html#ansible-collections-community-general-nmcli-module) - manage Networking
- [npm](https://docs.ansible.com/ansible/latest/collections/community/general/npm_module.html#ansible-collections-community-general-npm-module) - manage node.js packages with npm
- [nsupdate](https://docs.ansible.com/ansible/latest/collections/community/general/nsupdate_module.html#ansible-collections-community-general-nsupdate-module) - manage DNS records
- [odbc](https://docs.ansible.com/ansible/latest/collections/community/general/odbc_module.html#ansible-collections-community-general-odbc-module) - execute SQL via ODBC
- [pam_limits](https://docs.ansible.com/ansible/latest/collections/community/general/pam_limits_module.html#ansible-collections-community-general-pam-limits-module) - modify Linux PAM limits
- [pamd](https://docs.ansible.com/ansible/latest/collections/community/general/pamd_module.html#ansible-collections-community-general-pamd-module) - manage PAM Modules
- [parted](https://docs.ansible.com/ansible/latest/collections/community/general/parted_module.html#ansible-collections-community-general-parted-module) - configure block device partitions
- [pear](https://docs.ansible.com/ansible/latest/collections/community/general/pear_module.html#ansible-collections-community-general-pear-module) - manage pear/pecl packages
- [pids](https://docs.ansible.com/ansible/latest/collections/community/general/pids_module.html#ansible-collections-community-general-pids-module) - retrieves process IDs list if the process is running otherwise return empty list
- [pip_package_info](https://docs.ansible.com/ansible/latest/collections/community/general/pip_package_info_module.html#ansible-collections-community-general-pip-package-info-module) - pip package information
- [proxmox](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_module.html#ansible-collections-community-general-proxmox-module) - management of instances in Proxmox VE cluster
- [proxmox_disk](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_disk_module.html#ansible-collections-community-general-proxmox-disk-module) - management of a disk of a Qemu(KVM) VM in a Proxmox VE cluster
- [proxmox_domain_info](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_domain_info_module.html#ansible-collections-community-general-proxmox-domain-info-module) - retrieve information about one or more Proxmox VE domains
- [proxmox_group_info](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_group_info_module.html#ansible-collections-community-general-proxmox-group-info-module) - retrieve information about one or more Proxmox VE groups
- [proxmox_kvm](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_kvm_module.html#ansible-collections-community-general-proxmox-kvm-module) - management of Qemu(KVM) Virtual Machines in Proxmox VE cluster
- [proxmox_nic](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_nic_module.html#ansible-collections-community-general-proxmox-nic-module) - management of a NIC of a Qemu(KVM) VM in a Proxmox VE cluster
- [proxmox_snap](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_snap_module.html#ansible-collections-community-general-proxmox-snap-module) - snapshot management of instances in Proxmox VE cluster
- [proxmox_storage_info](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_storage_info_module.html#ansible-collections-community-general-proxmox-storage-info-module) - retrieve information about one or more Proxmox VE storages
- [proxmox_tasks_info](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_tasks_info_module.html#ansible-collections-community-general-proxmox-tasks-info-module) - retrieve information about one or more Proxmox VE tasks
- [proxmox_template](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_template_module.html#ansible-collections-community-general-proxmox-template-module) - management of OS templates in Proxmox VE cluster
- [proxmox_user_info](https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_user_info_module.html#ansible-collections-community-general-proxmox-user-info-module) - retrieve information about one or more Proxmox VE users
- [puppet](https://docs.ansible.com/ansible/latest/collections/community/general/puppet_module.html#ansible-collections-community-general-puppet-module) - runs puppet
- [python_requirements_info](https://docs.ansible.com/ansible/latest/collections/community/general/python_requirements_info_module.html#ansible-collections-community-general-python-requirements-info-module) - show python path and assert dependency versions
- [read_csv](https://docs.ansible.com/ansible/latest/collections/community/general/read_csv_module.html#ansible-collections-community-general-read-csv-module) - read a CSV file
- [redis](https://docs.ansible.com/ansible/latest/collections/community/general/redis_module.html#ansible-collections-community-general-redis-module) - various redis commands, replica and flush
- [redis_data](https://docs.ansible.com/ansible/latest/collections/community/general/redis_data_module.html#ansible-collections-community-general-redis-data-module) - set key value pairs in Redis
- [redis_data_incr](https://docs.ansible.com/ansible/latest/collections/community/general/redis_data_incr_module.html#ansible-collections-community-general-redis-data-incr-module) - increment keys in Redis
- [redis_data_info](https://docs.ansible.com/ansible/latest/collections/community/general/redis_data_info_module.html#ansible-collections-community-general-redis-data-info-module) - get value of key in Redis database
- [redis_info](https://docs.ansible.com/ansible/latest/collections/community/general/redis_info_module.html#ansible-collections-community-general-redis-info-module) - gather information about Redis servers
- [rhevm](https://docs.ansible.com/ansible/latest/collections/community/general/rhevm_module.html#ansible-collections-community-general-rhevm-module) - rHEV/oVirt automation
- [say](https://docs.ansible.com/ansible/latest/collections/community/general/say_module.html#ansible-collections-community-general-say-module) - makes a computer to speak
- [shutdown](https://docs.ansible.com/ansible/latest/collections/community/general/shutdown_module.html#ansible-collections-community-general-shutdown-module) - shut down a machine
- [snmp_facts](https://docs.ansible.com/ansible/latest/collections/community/general/snmp_facts_module.html#ansible-collections-community-general-snmp-facts-module) - retrieve facts for a device using SNMP
- [ssh_config](https://docs.ansible.com/ansible/latest/collections/community/general/ssh_config_module.html#ansible-collections-community-general-ssh-config-module) - manage SSH config for user
- [stackdriver](https://docs.ansible.com/ansible/latest/collections/community/general/stackdriver_module.html#ansible-collections-community-general-stackdriver-module) - send code deploy and annotation events to stackdriver
- [stacki_host](https://docs.ansible.com/ansible/latest/collections/community/general/stacki_host_module.html#ansible-collections-community-general-stacki-host-module) - add or remove host to stacki front-end
- [sudoers](https://docs.ansible.com/ansible/latest/collections/community/general/sudoers_module.html#ansible-collections-community-general-sudoers-module) - manage sudoers files
- [syslogger](https://docs.ansible.com/ansible/latest/collections/community/general/syslogger_module.html#ansible-collections-community-general-syslogger-module) - log messages in the syslog
- [telegram](https://docs.ansible.com/ansible/latest/collections/community/general/telegram_module.html#ansible-collections-community-general-telegram-module) - send notifications via telegram
- [terraform](https://docs.ansible.com/ansible/latest/collections/community/general/terraform_module.html#ansible-collections-community-general-terraform-module) - manages a Terraform deployment (and plans)
- [timezone](https://docs.ansible.com/ansible/latest/collections/community/general/timezone_module.html#ansible-collections-community-general-timezone-module) - configure timezone setting
- [ufw](https://docs.ansible.com/ansible/latest/collections/community/general/ufw_module.html#ansible-collections-community-general-ufw-module) - manage firewall with UFW
- [uptimerobot](https://docs.ansible.com/ansible/latest/collections/community/general/uptimerobot_module.html#ansible-collections-community-general-uptimerobot-module) - pause and start Uptime Robot monitoring
- [xattr](https://docs.ansible.com/ansible/latest/collections/community/general/xattr_module.html#ansible-collections-community-general-xattr-module) - manage user defined extended attributes
- [xml](https://docs.ansible.com/ansible/latest/collections/community/general/xml_module.html#ansible-collections-community-general-xml-module) - manage bits and pieces of XML files or strings
- [yarn](https://docs.ansible.com/ansible/latest/collections/community/general/yarn_module.html#ansible-collections-community-general-yarn-module) - manage node.js packages with Yarn
- [yum_versionlock](https://docs.ansible.com/ansible/latest/collections/community/general/yum_versionlock_module.html#ansible-collections-community-general-yum-versionlock-module) - locks / unlocks a installed package(s) from being updated by yum package manager
- [zfs](https://docs.ansible.com/ansible/latest/collections/community/general/zfs_module.html#ansible-collections-community-general-zfs-module) - manage zfs
- [zfs_delegate_admin](https://docs.ansible.com/ansible/latest/collections/community/general/zfs_delegate_admin_module.html#ansible-collections-community-general-zfs-delegate-admin-module) - manage ZFS delegated administration (user admin privileges)
- [zfs_facts](https://docs.ansible.com/ansible/latest/collections/community/general/zfs_facts_module.html#ansible-collections-community-general-zfs-facts-module) - gather facts about ZFS datasets
- [zpool_facts](https://docs.ansible.com/ansible/latest/collections/community/general/zpool_facts_module.html#ansible-collections-community-general-zpool-facts-module) - gather facts about ZFS pools

#### `community.mongodb`
- [mongodb_balancer](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_balancer_module.html#ansible-collections-community-mongodb-mongodb-balancer-module) - manages the MongoDB Sharded Cluster Balancer.
- [mongodb_index](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_index_module.html#ansible-collections-community-mongodb-mongodb-index-module) - creates or drops indexes on MongoDB collections.
- [mongodb_info](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_info_module.html#ansible-collections-community-mongodb-mongodb-info-module) - gather information about MongoDB instance.
- [mongodb_maintenance](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_maintenance_module.html#ansible-collections-community-mongodb-mongodb-maintenance-module) - enables or disables maintenance mode for a secondary member.
- [mongodb_monitoring](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_monitoring_module.html#ansible-collections-community-mongodb-mongodb-monitoring-module) - manages the free monitoring feature.
- [mongodb_oplog](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_oplog_module.html#ansible-collections-community-mongodb-mongodb-oplog-module) - resizes the MongoDB oplog.
- [mongodb_parameter](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_parameter_module.html#ansible-collections-community-mongodb-mongodb-parameter-module) - change an administrative parameter on a MongoDB server
- [mongodb_replicaset](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_replicaset_module.html#ansible-collections-community-mongodb-mongodb-replicaset-module) - initialises a MongoDB replicaset.
- [mongodb_role](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_role_module.html#ansible-collections-community-mongodb-mongodb-role-module) - adds or removes a role from a MongoDB database
- [mongodb_schema](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_schema_module.html#ansible-collections-community-mongodb-mongodb-schema-module) - manages MongoDB Document Schema Validators.
- [mongodb_shard](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_shard_module.html#ansible-collections-community-mongodb-mongodb-shard-module) - add or remove shards from a MongoDB Cluster
- [mongodb_shard_tag](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_shard_tag_module.html#ansible-collections-community-mongodb-mongodb-shard-tag-module) - manage Shard Tags.
- [mongodb_shard_zone](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_shard_zone_module.html#ansible-collections-community-mongodb-mongodb-shard-zone-module) - manage Shard Zones.
- [mongodb_shell](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_shell_module.html#ansible-collections-community-mongodb-mongodb-shell-module) - run commands via the MongoDB shell.
- [mongodb_shutdown](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_shutdown_module.html#ansible-collections-community-mongodb-mongodb-shutdown-module) - cleans up all database resources and then terminates the mongod/mongos process.
- [mongodb_status](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_status_module.html#ansible-collections-community-mongodb-mongodb-status-module) - validates the status of the replicaset.
- [mongodb_stepdown](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_stepdown_module.html#ansible-collections-community-mongodb-mongodb-stepdown-module) - step down the MongoDB node from a PRIMARY state.
- [mongodb_user](https://docs.ansible.com/ansible/latest/collections/community/mongodb/mongodb_user_module.html#ansible-collections-community-mongodb-mongodb-user-module) - adds or removes a user from a MongoDB database

#### `community.mysql`
- [mysql_db](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_db_module.html#ansible-collections-community-mysql-mysql-db-module) - add or remove MySQL databases from a remote host
- [mysql_info](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_info_module.html#ansible-collections-community-mysql-mysql-info-module) - gather information about MySQL servers
- [mysql_query](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_query_module.html#ansible-collections-community-mysql-mysql-query-module) - run MySQL queries
- [mysql_replication](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_replication_module.html#ansible-collections-community-mysql-mysql-replication-module) - manage MySQL replication
- [mysql_role](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_role_module.html#ansible-collections-community-mysql-mysql-role-module) - adds, removes, or updates a MySQL role
- [mysql_user](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_user_module.html#ansible-collections-community-mysql-mysql-user-module) - adds or removes a user from a MySQL database
- [mysql_variables](https://docs.ansible.com/ansible/latest/collections/community/mysql/mysql_variables_module.html#ansible-collections-community-mysql-mysql-variables-module) - manage MySQL global variables

#### `community.postgresql`
- [postgresql_copy](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_copy_module.html#ansible-collections-community-postgresql-postgresql-copy-module) - copy data between a file/program and a PostgreSQL table
- [postgresql_db](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_db_module.html#ansible-collections-community-postgresql-postgresql-db-module) - add or remove PostgreSQL databases from a remote host
- [postgresql_ext](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_ext_module.html#ansible-collections-community-postgresql-postgresql-ext-module) - add or remove PostgreSQL extensions from a database
- [postgresql_idx](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_idx_module.html#ansible-collections-community-postgresql-postgresql-idx-module) - create or drop indexes from a PostgreSQL database
- [postgresql_info](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_info_module.html#ansible-collections-community-postgresql-postgresql-info-module) - gather information about PostgreSQL servers
- [postgresql_lang](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_lang_module.html#ansible-collections-community-postgresql-postgresql-lang-module) - adds, removes or changes procedural languages with a PostgreSQL database
- [postgresql_membership](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_membership_module.html#ansible-collections-community-postgresql-postgresql-membership-module) - add or remove PostgreSQL roles from groups
- [postgresql_owner](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_owner_module.html#ansible-collections-community-postgresql-postgresql-owner-module) - change an owner of PostgreSQL database object
- [postgresql_pg_hba](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_pg_hba_module.html#ansible-collections-community-postgresql-postgresql-pg-hba-module) - add, remove or modify a rule in a pg_hba file
- [postgresql_ping](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_ping_module.html#ansible-collections-community-postgresql-postgresql-ping-module) - check remote PostgreSQL server availability
- [postgresql_privs](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_privs_module.html#ansible-collections-community-postgresql-postgresql-privs-module) - grant or revoke privileges on PostgreSQL database objects
- [postgresql_publication](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_publication_module.html#ansible-collections-community-postgresql-postgresql-publication-module) - add, update, or remove PostgreSQL publication
- [postgresql_query](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_query_module.html#ansible-collections-community-postgresql-postgresql-query-module) - run PostgreSQL queries
- [postgresql_schema](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_schema_module.html#ansible-collections-community-postgresql-postgresql-schema-module) - add or remove PostgreSQL schema
- [postgresql_script](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_script_module.html#ansible-collections-community-postgresql-postgresql-script-module) - run PostgreSQL statements from a file
- [postgresql_sequence](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_sequence_module.html#ansible-collections-community-postgresql-postgresql-sequence-module) - create, drop, or alter a PostgreSQL sequence
- [postgresql_set](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_set_module.html#ansible-collections-community-postgresql-postgresql-set-module) - change a PostgreSQL server configuration parameter
- [postgresql_slot](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_slot_module.html#ansible-collections-community-postgresql-postgresql-slot-module) - add or remove replication slots from a PostgreSQL database
- [postgresql_subscription](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_subscription_module.html#ansible-collections-community-postgresql-postgresql-subscription-module) - add, update, or remove PostgreSQL subscription
- [postgresql_table](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_table_module.html#ansible-collections-community-postgresql-postgresql-table-module) - create, drop, or modify a PostgreSQL table
- [postgresql_tablespace](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_tablespace_module.html#ansible-collections-community-postgresql-postgresql-tablespace-module) - add or remove PostgreSQL tablespaces from remote hosts
- [postgresql_user](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_user_module.html#ansible-collections-community-postgresql-postgresql-user-module) - create, alter, or remove a user (role) from a PostgreSQL server instance
- [postgresql_user_obj_stat_info](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_user_obj_stat_info_module.html#ansible-collections-community-postgresql-postgresql-user-obj-stat-info-module) - gather statistics about PostgreSQL user objects

#### `kubernetes.core`
- [helm](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_module.html#ansible-collections-kubernetes-core-helm-module) - manages Kubernetes packages with the Helm package manager
- [helm_info](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_info_module.html#ansible-collections-kubernetes-core-helm-info-module) - get information from Helm package deployed inside the cluster
- [helm_plugin](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_plugin_module.html#ansible-collections-kubernetes-core-helm-plugin-module) - manage Helm plugins
- [helm_plugin_info](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_plugin_info_module.html#ansible-collections-kubernetes-core-helm-plugin-info-module) - gather information about Helm plugins
- [helm_pull](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_pull_module.html#ansible-collections-kubernetes-core-helm-pull-module) - download a chart from a repository and (optionally) unpack it in local directory.
- [helm_repository](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_repository_module.html#ansible-collections-kubernetes-core-helm-repository-module) - manage Helm repositories.
- [helm_template](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_template_module.html#ansible-collections-kubernetes-core-helm-template-module) - render chart templates
- [k8s](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_module.html#ansible-collections-kubernetes-core-k8s-module) - manage Kubernetes (K8s) objects
- [k8s_cluster_info](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_cluster_info_module.html#ansible-collections-kubernetes-core-k8s-cluster-info-module) - describe Kubernetes (K8s) cluster, APIs available and their respective versions
- [k8s_cp](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_cp_module.html#ansible-collections-kubernetes-core-k8s-cp-module) - copy files and directories to and from pod.
- [k8s_drain](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_drain_module.html#ansible-collections-kubernetes-core-k8s-drain-module) - drain, Cordon, or Uncordon node in k8s cluster
- [k8s_exec](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_exec_module.html#ansible-collections-kubernetes-core-k8s-exec-module) - execute command in Pod
- [k8s_info](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_info_module.html#ansible-collections-kubernetes-core-k8s-info-module) - describe Kubernetes (K8s) objects
- [k8s_json_patch](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_json_patch_module.html#ansible-collections-kubernetes-core-k8s-json-patch-module) - apply JSON patch operations to existing objects
- [k8s_log](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_log_module.html#ansible-collections-kubernetes-core-k8s-log-module) - fetch logs from Kubernetes resources
- [k8s_rollback](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_rollback_module.html#ansible-collections-kubernetes-core-k8s-rollback-module) - rollback Kubernetes (K8S) Deployments and DaemonSets
- [k8s_scale](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_scale_module.html#ansible-collections-kubernetes-core-k8s-scale-module) - set a new size for a Deployment, ReplicaSet, Replication Controller, or Job.
- [k8s_service](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_service_module.html#ansible-collections-kubernetes-core-k8s-service-module) - manage Services on Kubernetes
- [k8s_taint](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/k8s_taint_module.html#ansible-collections-kubernetes-core-k8s-taint-module) - taint a node in a Kubernetes/OpenShift cluster