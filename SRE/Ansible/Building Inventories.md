* [source](https://docs.ansible.com/ansible/latest/inventory_guide/index.html)
### How to build your inventory
> [source](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
* Ansible automates tasks on managed nodes or “hosts” in your infrastructure, using a list or group of lists known as inventory.
* You can pass host names at the command line, but most Ansible users create inventory files.
* Your inventory defines the managed nodes you automate, with groups so you can run automation tasks on multiple hosts at the same time.
* Once your inventory is defined, you use [patterns](https://docs.ansible.com/ansible/latest/inventory_guide/intro_patterns.html#intro-patterns) to select the hosts or groups you want Ansible to run against.
* The simplest inventory is a single file with a list of hosts and groups. The default location for this file is `/etc/ansible/hosts`. You can specify a different inventory file at the command line using the `-i <path>` option or in configuration using `inventory`.
* Ansible [Inventory plugins](https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins) support a range of formats and sources to make your inventory flexible and customizable. As your inventory expands, you may need more than a single file to organize your hosts and groups. Here are three options beyond the `/etc/ansible/hosts` file:
	* You can create a directory with multiple inventory files. See [Organizing inventory in a directory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#inventory-directory). These can use different formats (YAML, ini, and so on).
	* You can pull inventory dynamically. For example, you can use a dynamic inventory plugin to list resources in one or more cloud providers. See [Working with dynamic inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#intro-dynamic-inventory).
	* You can use multiple sources for inventory, including both dynamic inventory and static files. See [Passing multiple inventory sources](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#using-multiple-inventory-sources).

#### Inventory basics: formats, hosts, and groups
* You can create your inventory file in one of many formats, depending on the inventory plugins you have. The most common formats are INI and YAML.
* A basic INI `/etc/ansible/hosts` might look like this:
	```yaml
	all:
	  hosts:
	    mail.example.com:
	  children:
	    webservers:
	      hosts:
	        foo.example.com:
	        bar.example.com:
	    dbservers:
	      hosts:
	        one.example.com:
	        two.example.com:
	        three.example.com:
	```
	* The headings in brackets are group names, which are used in classifying hosts and deciding what hosts you are controlling at what times and for what purpose. Group names should follow the same guidelines as [Creating valid variable names](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#valid-variable-names).

##### Default groups
* Even if you do not define any groups in your inventory file, Ansible creates two default groups: `all` and `ungrouped`.
* The `all` group contains every host.
* The `ungrouped` group contains all hosts that don’t have another group aside from `all`.
* Every host will always belong to at least 2 groups (`all` and `ungrouped` or `all` and some other group).
* Though `all` and `ungrouped` are always present, they can be implicit and not appear in group listings like `group_names`.

##### Hosts in multiple groups
* You can (and probably will) put each host in more than one group.
* For example a production webserver in a datacenter in Atlanta might be included in groups called `[prod]` and `[atlanta]` and `[webservers]`.
* You can create groups that track:
	* What - An application, stack or microservice (for example, database servers, web servers, and so on).
	* Where - A datacenter or region, to talk to local DNS, storage, and so on (for example, east, west).
	* When - The development stage, to avoid testing on production resources (for example, prod, test).
* Extending the previous YAML inventory to include what, when, and where would look like this:
	```yaml
	all:
	  hosts:
	    mail.example.com:
	  children:
	    webservers:
	      hosts:
	        foo.example.com:
	        bar.example.com:
	    dbservers:
	      hosts:
	        one.example.com:
	        two.example.com:
	        three.example.com:
	    east:
	      hosts:
	        foo.example.com:
	        one.example.com:
	        two.example.com:
	    west:
	      hosts:
	        bar.example.com:
	        three.example.com:
	    prod:
	      hosts:
	        foo.example.com:
	        one.example.com:
	        two.example.com:
	    test:
	      hosts:
	        bar.example.com:
	        three.example.com:
	```

##### Grouping groups: parent/child group relationship
* You can create parent/child relationships among groups. Parent groups are also known as nested groups or groups of groups.
* For example, if all your production hosts are already in groups such as `atlanta_prod` and `denver_prod`, you can create a `production` group that includes those smaller groups.
* This approach reduces maintenance because you can add or remove hosts from the parent group by editing the child groups.
* To create parent/child relationships for groups:
	-   in INI format, use the `:children` suffix
	-   in YAML format, use the `children:` entry
- Here is the same inventory as shown above, simplified with parent groups for the `prod` and `test` groups. The two inventory files give you the same results:
	```yaml
	all:
	  hosts:
	    mail.example.com:
	  children:
	    webservers:
	      hosts:
	        foo.example.com:
	        bar.example.com:
	    dbservers:
	      hosts:
	        one.example.com:
	        two.example.com:
	        three.example.com:
	    east:
	      hosts:
	        foo.example.com:
	        one.example.com:
	        two.example.com:
	    west:
	      hosts:
	        bar.example.com:
	        three.example.com:
	    prod:
	      children:
	        east:
	    test:
	      children:
	        west:
	```
- Child groups have a couple of properties to note:
	* Any host that is member of a child group is automatically a member of the parent group.
	* Groups can have multiple parents and children, **but not circular relationships**.
	* Hosts can also be in multiple groups, but there will only be **one** instance of a host at runtime. **Ansible merges the data from the multiple groups.**

##### Adding ranges of hosts
* If you have a lot of hosts with a similar pattern, you can add them as a range rather than listing each hostname separately:
	```yaml
	...
	  webservers:
	    hosts:
	      www[01:50].example.com:
	```
* You can specify a stride (increments between sequence numbers) when defining a numeric range of hosts:
	```yaml
	...
	  webservers:
	    hosts:
	      www[01:50:2].example.com:
	```
* For numeric patterns, leading zeros can be included or removed, as desired.
* Ranges are inclusive.
* You can also define alphabetic ranges:
	```
	[databases]
	db-[a:f].example.com
	```

##### Passing multiple inventory sources
You can target multiple inventory sources (directories, dynamic inventory scripts or files supported by inventory plugins) at the same time by giving multiple inventory parameters from the command line or by configuring [`ANSIBLE_INVENTORY`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#envvar-ANSIBLE_INVENTORY). This can be useful when you want to target normally separate environments, like staging and production, at the same time for a specific action.

#### Organizing inventory in a directory
* You can consolidate multiple inventory sources in a single directory. The simplest version of this is a directory with multiple files instead of a single inventory file.
* A single file gets difficult to maintain when it gets too long. If you have multiple teams and multiple automation projects, having one inventory file per team or project lets everyone easily find the hosts and groups that matter to them.
* You can also combine multiple inventory source types in an inventory directory. This can be useful for combining static and dynamic hosts and managing them as one inventory. You can target this inventory directory as follows: `ansible-playbook example.yml -i inventory`
	```
	inventory/
	  openstack.yml          # inventory plugin conf to get hosts from cloud
	  dynamic-inventory.py   # add additional hosts with dynamic inventory script
	  on-prem                # add static hosts and groups
	  parent-groups          # add static hosts and groups
	```
* You can also configure the inventory directory in your `ansible.cfg` file. See [Configuring Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html#intro-configuration) for more details.

##### Managing inventory load order
* Ansible loads inventory sources in ASCII order according to the filenames.
	* If you define parent groups in one file or directory and child groups in other files or directories, the files that define the child groups must be loaded first.
	* If the parent groups are loaded first, you will see the error `Unable to parse /path/to/source_of_parent_groups as an inventory source`
* For example, if you have a file called `groups-of-groups` that defines a `production` group with child groups defined in a file called `on-prem`, Ansible cannot parse the `production` group.
	* To avoid this problem, you can control the load order by adding prefixes to the files:
		```
		inventory/
		  01-openstack.yml          # configure inventory plugin to get hosts from OpenStack cloud
		  02-dynamic-inventory.py   # add additional hosts with dynamic inventory script
		  03-on-prem                # add static hosts and groups
		  04-groups-of-groups       # add parent groups
		```
* You can find examples of how to organize your inventories and group your hosts in [Inventory setup examples](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#inventory-setup-examples).

#### Adding variables to inventory
* You can store variable values that relate to a specific host or group in inventory. To start with, you may add variables directly to the hosts and groups in your main inventory file.
* See [Organizing host and group variables](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#splitting-out-vars) for guidelines on storing variable values in individual files in the ‘host_vars’ directory.
* See [Organizing host and group variables](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#splitting-out-vars) for details.

#### Assigning variables to one machine: host variables
* You can easily assign a variable to a single host, then use it later in playbooks. You can do this directly in your inventory file.
	```yaml
	atlanta:
	  hosts:
	    host1:
	      http_port: 80
	      maxRequestsPerChild: 808
	    host2:
	      http_port: 303
	      maxRequestsPerChild: 909
	```
* Unique values like non-standard SSH ports work well as host variables. You can add them to your Ansible inventory by adding the port number after the hostname with a colon: `badwolf.example.com:5309`
* Connection variables also work well as host variables:
```ini
[targets]

localhost            ansible_connection=local
other1.example.com   ansible_connection=ssh   ansible_user=myuser
other2.example.com   ansible_connection=ssh   ansible_user=myotheruser
```
* **Note**: If you list non-standard SSH ports in your SSH config file, the `openssh` connection will find and use them, but the `paramiko` connection will not.

##### Inventory Aliases
* You can also define aliases in your inventory using host variables. In this example, running Ansible against the host alias “jumper” will connect to `192.0.2.50` on port `5555`.
```yaml
...
  hosts:
    jumper:
      ansible_port: 5555
      ansible_host: 192.0.2.50
```
* See [behavioral inventory parameters](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#behavioral-parameters) to further customize the connection to hosts.

#### Assigning variables to many machines: group variables
* If all hosts in a group share a variable value, you can apply that variable to an entire group at once.
	```yaml
	atlanta:
	  hosts:
	    host1:
	    host2:
	  vars:
	    ntp_server: ntp.atlanta.example.com
	    proxy: proxy.atlanta.example.com
	```
* Group variables are a convenient way to apply variables to multiple hosts at once. Before executing, however, Ansible always flattens variables, including inventory variables, to the host level. If a host is a member of multiple groups, Ansible reads variable values from all of those groups. If you assign different values to the same variable in different groups, Ansible chooses which value to use based on internal [rules for merging](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#how-we-merge).

##### Inheriting variable values: group variables for groups of groups
* You can apply variables to parent groups (nested groups or groups of groups) as well as to child groups.
	```yaml
	all:
	  children:
	    usa:
	      children:
	        southeast:
	          children:
	            atlanta:
	              hosts:
	                host1:
	                host2:
	            raleigh:
	              hosts:
	                host2:
	                host3:
	          vars:
	            some_server: foo.southeast.example.com
	            halon_system_timeout: 30
	            self_destruct_countdown: 60
	            escape_pods: 2
	        northeast:
	        northwest:
	        southwest:
	```
* A child group’s variables will have higher precedence (override) a parent group’s variables.

#### Organizing host and group variables
* Although you can store variables in the main inventory file, storing separate host and group variables files may help you organize your variable values more easily.
* You can also use lists and hash data in host and group variables files, which you cannot do in your main inventory file.
* Host and group variable files must use YAML syntax. See [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#yaml-syntax) if you are new to YAML.
* Ansible loads host and group variable files by searching paths relative to the inventory file or the playbook file. If your inventory file at `/etc/ansible/hosts` contains a host named `foosball` that belongs to two groups, `raleigh` and `webservers`, that host will use variables in YAML files at the following locations:
	```sh
	/etc/ansible/group_vars/raleigh # can optionally end in '.yml', '.yaml', or '.json'
	/etc/ansible/group_vars/webservers
	/etc/ansible/host_vars/foosball
	```
* You can also create _directories_ named after your groups or hosts. Ansible will read all the files in these directories in lexicographical order. This can be very useful to keep your variables organized when a single file gets too big, or when you want to use [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/vault_using_encrypted_content.html#playbooks-vault) on some group variables.
* For `ansible-playbook` you can also add `group_vars/` and `host_vars/` directories to your playbook directory.
	* Other Ansible commands (for example, `ansible`, `ansible-console`, and so on) will only look for `group_vars/` and `host_vars/` in the inventory directory. If you want other commands to load group and host variables from a playbook directory, you must provide the `--playbook-dir` option on the command line. 
	* If you load inventory files from both the playbook directory and the inventory directory, variables in the playbook directory will override variables set in the inventory directory.
* Keeping your inventory file and variables in a git repo (or other version control) is an excellent way to track changes to your inventory and host variables.

#### How variables are merged
* By default variables are merged/flattened to the specific host before a play is run. This keeps Ansible focused on the Host and Task, so groups don’t really survive outside of inventory and host matching.
* By default, Ansible overwrites variables including the ones defined for a group and/or host (see [DEFAULT_HASH_BEHAVIOUR](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-hash-behaviour)). The order/precedence is (from lowest to highest):
	* all group (because it is the ‘parent’ of all other groups)
	* parent group
	* child group
	* host
* By default Ansible merges groups at the same parent/child level in ASCII order, and variables from the last group loaded overwrite variables from the previous groups. For example, an a_group will be merged with b_group and b_group vars that match will overwrite the ones in a_group. You can change this behavior by setting the group variable `ansible_group_priority` to change the merge order for groups of the same level (after the parent/child order is resolved). The larger the number, the later it will be merged, giving it higher priority. This variable defaults to `1` if not set. For example:
	```yaml
	a_group:
	  vars:
	    testvar: a
	    ansible_group_priority: 10
	b_group:
	  vars:
	    testvar: b
	```
* In this example, if both groups have the same priority, the result would normally have been `testvar == b`, but since we are giving the `a_group` a higher priority the result will be `testvar == a`.
* **Note**: `ansible_group_priority` can only be set in the inventory source and not in group_vars/, as the variable is used in the loading of group_vars.

##### Managing inventory variable load order
* When using multiple inventory sources, keep in mind that any variable conflicts are resolved according to the rules described in [[SRE/Ansible/Building Inventories|Building Inventories#How variables are merged]] and [Variable precedence: Where should I put a variable?](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#ansible-variable-precedence). You can control the merging order of variables in inventory sources to get the variable value you need.
* When you pass multiple inventory sources at the command line, Ansible merges variables in the order you pass those parameters. If `[all:vars]` in staging inventory defines `myvar = 1` and production inventory defines `myvar = 2`, then:
	* pass `-i staging -i production` to run the playbook with `myvar = 2`.
	* pass `-i production -i staging` to run the playbook with `myvar = 1`.
* For more details on inventory plugins and dynamic inventory scripts see [Inventory plugins](https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins) and [Working with dynamic inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#intro-dynamic-inventory).

#### Connecting to hosts: behavioral inventory parameters
* Host connections:
	* **Note**: Ansible does not expose a channel to allow communication between the user and the ssh process to accept a password manually to decrypt an ssh key when using the ssh connection plugin (which is the default). The use of `ssh-agent` is highly recommended.
	* `ansible_connection`: Connection type to the host. This can be the name of any of ansible’s connection plugins. SSH protocol types are `smart`, `ssh` or `paramiko`. The default is smart. Non-SSH based types are described in the next section.
* General for all connections:
	* `ansible_host`: The name of the host to connect to, if different from the alias you wish to give to it.
	* `ansible_port`: The connection port number, if not the default (22 for ssh)
	* `ansible_user`: The user name to use when connecting to the host
	* `ansible_password`: The password to use to authenticate to the host (never store this variable in plain text; always use a vault. See [Keep vaulted variables safely visible](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults))
* Specific to the ssh connection:
	* `ansible_ssh_private_key_file`: Private key file used by ssh. Useful if using multiple keys and you don’t want to use SSH agent.
	* `ansible_ssh_common_args`: This setting is always appended to the default command line for **sftp**, **scp**, and **ssh**. Useful to configure a `ProxyCommand` for a certain host (or group).
	* `ansible_sftp_extra_args`: This setting is always appended to the default **sftp** command line.
	* `ansible_scp_extra_args`: This setting is always appended to the default **scp** command line.
	* `ansible_ssh_extra_args`: This setting is always appended to the default **ssh** command line.
	* `ansible_ssh_pipelining`: Determines whether or not to use SSH pipelining. This can override the `pipelining` setting in `ansible.cfg`.
	* `ansible_ssh_executable`: This setting overrides the default behavior to use the system **ssh**. This can override the `ssh_executable` setting in `ansible.cfg`.
* Privilege escalation (see [Ansible Privilege Escalation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html#become) for further details):
	* `ansible_become`: Equivalent to `ansible_sudo` or `ansible_su`, allows to force privilege escalation
	* `ansible_become_method`: Allows to set privilege escalation method
	* `ansible_become_user`: Equivalent to `ansible_sudo_user` or `ansible_su_user`, allows to set the user you become through privilege escalation
	* `ansible_become_password`: Equivalent to `ansible_sudo_password` or `ansible_su_password`, allows you to set the privilege escalation password (never store this variable in plain text; always use a vault. See [Keep vaulted variables safely visible](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#tip-for-variables-and-vaults))
	* `ansible_become_flags`: Equivalent to `ansible_sudo_flags` or `ansible_su_flags`, allows you to set the flags passed to the selected escalation method. This can be also set globally in `ansible.cfg` in the `sudo_flags` option

##### Non-ssh connection types
* As stated in the previous section, Ansible executes playbooks over SSH but it is not limited to this connection type. With the host specific parameter `ansible_connection=<connector>`, the connection type can be changed. The following non-SSH based connectors are available:
	* `local`: This connector can be used to deploy the playbook to the control machine itself.
	* Docker: This connector deploys the playbook directly into Docker containers using the local Docker client. The following parameters are processed by this connector:
		* `ansible_host`: The name of the Docker container to connect to.
		* `ansible_user`: The user name to operate within the container. The user must exist inside the container.
		* `ansible_become`: If set to `true` the `become_user` will be used to operate within the container.
		* `ansible_docker_extra_args`: Could be a string with any additional arguments understood by Docker, which are not command specific. This parameter is mainly used to configure a remote Docker daemon to use.
* For a full list with available plugins and examples, see [Plugin list](https://docs.ansible.com/ansible/latest/plugins/connection.html#connection-plugin-list).

#### Inventory setup examples
> [source](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#inventory-setup-examples)
#### Working with dynamic Inventory
> [source](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html)
* If your Ansible inventory fluctuates over time, with hosts spinning up and shutting down in response to business demands, the static inventory solutions described in [[SRE/Ansible/Building Inventories|Building Inventories#How to build your inventory]] will not serve your needs. You may need to track hosts from multiple sources: cloud providers, LDAP, [Cobbler](https://cobbler.github.io/), and/or enterprise CMDB systems.
* Ansible integrates all of these options through a dynamic external inventory system. Ansible supports two ways to connect with external inventory: [Inventory plugins](https://docs.ansible.com/ansible/latest/plugins/inventory.html#inventory-plugins) and inventory scripts.
	* Inventory plugins take advantage of the most recent updates to the Ansible core code. We recommend plugins over scripts for dynamic inventory. You can [write your own plugin](https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory) to connect to additional dynamic inventory sources.
	* You can still use inventory scripts if you choose. When we implemented inventory plugins, we ensured backwards compatibility through the script inventory plugin.
* If you prefer a GUI for handling dynamic inventory, the inventory database on AWX or [Red Hat Ansible Automation Platform](https://docs.ansible.com/ansible/latest/reference_appendices/tower.html#ansible-platform) syncs with all your dynamic inventory sources, provides web and REST access to the results, and offers a graphical inventory editor. With a database record of all of your hosts, you can correlate past event history and see which hosts have had failures on their last playbook runs.

* Inventory script examples
	* [Cobbler](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#inventory-script-example-cobbler)
	* [OpenStack](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#inventory-script-example-openstack)
* [Other inventory scripts](https://docs.ansible.com/ansible/latest/inventory_guide/intro_dynamic_inventory.html#other-inventory-scripts)

### Patterns: targeting hosts and groups
* When you execute Ansible through an ad hoc command or by running a playbook, you must choose which managed nodes or groups you want to execute against. Patterns let you run commands and playbooks against specific hosts and/or groups in your inventory.
* An Ansible pattern can refer to a single host, an IP address, an inventory group, a set of groups, or all hosts in your inventory.
* Patterns are highly flexible - you can exclude or require subsets of hosts, use wildcards or regular expressions, and more. Ansible executes on all inventory hosts included in the pattern.

#### Using Patterns
* You use a pattern almost any time you execute an ad hoc command or a playbook. The pattern is the only element of an [ad hoc command](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#intro-adhoc) that has no flag. It is usually the second element:
	* `ansible <pattern> -m <module_name> -a "<module options>"`
	* e.g. `ansible webservers -m service -a "name=httpd state=restarted"`
* In a playbook the pattern is the content of the `hosts:` line for each play:
	```yaml
	- name: <play_name>
	  hosts: <pattern>
	```
	* e.g.
	```yaml
	- name: restart webservers
	  hosts: webservers
	```
	* Since you often want to run a command or playbook against multiple hosts at once, patterns often refer to inventory groups. Both the ad hoc command and the playbook above will execute against all machines in the `webservers` group.

#### Common Patterns
* This table lists common patterns for targeting inventory hosts and groups.
| Description | Pattern(s) | Targets |
| :- | :- | :- |
| All hosts | all (or \*) | |
| One host | host1 | |
| Multiple hosts | host1:host2 (or host1,host2) | |
| One group | webservers | |
| Multiple groups | webservers:dbservers | all hosts in webservers plus all hosts in dbservers |
| Excluding groups | webservers:!atlanta | all hosts in webservers except those in atlanta |
| Intersection of groups | webservers:&staging | any hosts in webservers that are also in staging |
* **Note**: You can use either a comma `(,)` or a colon `(:)` to separate a list of hosts. The comma is preferred when dealing with ranges and IPv6 addresses.
* Once you know the basic patterns, you can combine them.
	* `webservers:dbservers:&staging:!phoenix`
		* This example targets all machines in the groups `webservers` and `dbservers` that are also in the group `staging`, except any machines in the group `phoenix`.
* You can use wildcard patterns with FQDNs or IP addresses, as long as the hosts are named in your inventory by FQDN or IP address:
	```
	192.0.*
	*.example.com
	*.com
	```
* You can mix wildcard patterns and groups at the same time
	* `one*.com:dbservers`

#### Limitations of patterns
* Patterns depend on inventory. If a host or group is not listed in your inventory, you cannot use a pattern to target it. If your pattern includes an IP address or hostname that does not appear in your inventory, you will see an error like this:
	```
	[WARNING]: No inventory was parsed, only implicit localhost is available
	[WARNING]: Could not match supplied host pattern, ignoring: *.not_in_inventory.com
	```
* If you have an alias for a host in your inventory, and you use the IP address, you will once again get the error:
	* `[WARNING]: Could not match supplied host pattern, ignoring: 127.0.0.2`

#### Pattern processing order
* The processing is a bit special and happens in the following order:
	1. `:` and `,`
	2. `&`
	3. `!`
* This positioning only accounts for processing order inside each operation.
	* ``a:b:&c:!d:!e == &c:a:!d:b:!e == !d:a:!e:&c:b`` all of these result in the following:
		* Host in/is (a or b) AND host in/is all(c) AND host NOT in/is all(d, e).
	* Now `a:b:!e:!d:&c` is a slight change as the `!e` gets processed before the `!d`, though this doesn’t make much of a difference:
		* Host in/is (a or b) AND host in/is all(c) AND host NOT in/is all(e, d).

#### Advanced pattern options
* The common patterns described above will meet most of your needs, but Ansible offers several other ways to define the hosts and groups you want to target.
* Using variables in patterns.
	* You can use variables to enable passing group specifiers via the `-e` argument to ansible-playbook:
		* `webservers:!{{ excluded }}:&{{ required }}`
* Using group position in patterns
	* You can define a host or subset of hosts by its position in a group. For example, given the following group:
	```yaml
	[webservers]
	cobweb
	webbing
	weber
	```
	* you can use subscripts to select individual hosts or ranges within the webservers group:
	```
	webservers[0]       # == cobweb
	webservers[-1]      # == weber
	webservers[0:2]     # == webservers[0],webservers[1]
	                    # == cobweb,webbing
	webservers[1:]      # == webbing,weber
	webservers[:3]      # == cobweb,webbing,weber
	```
* Using regex in patterns
	* You can specify a pattern as a regular expression by starting the pattern with `~`.
		* `~(web|db).*\.example\.com`

#### Patterns and ad-hoc commands
* You can change the behavior of the patterns defined in ad-hoc commands using command-line options. You can also limit the hosts you target on a particular run with the `--limit` flag.
	* Limit to one host:
		* `ansible all -m [module] -a "[module options]" --limit "host1"`
	* Limit to multiple hosts:
		* `ansible all -m [module] -a "[module options]" --limit "host1,host2"`
	* Negated limit. Note that single quotes MUST be used to prevent bash interpolation.
		* `ansible all -m [module] -a "[module options]" --limit 'all:!host1'`
	* Limit to host group:
		* `ansible all -m [module] -a "[module options]" --limit 'group1'`

#### Patterns and ansible playbook flags
* You can change the behavior of the patterns defined in playbooks using command-line options.
* For example, you can run a playbook that defines `hosts: all` on a single host by specifying `-i 127.0.0.2,` (note the trailing comma). This works even if the host you target is not defined in your inventory, but this method will NOT read your inventory for variables tied to this host and any variables required by the playbook will need to be specified manually at the command line.
* You can also limit the hosts you target on a particular run with the `--limit` flag, which will reference your inventory:
	* `ansible-playbook site.yml --limit datacenter2`
* Finally, you can use `--limit` to read the list of hosts from a file by prefixing the file name with `@`:
	* `ansible-playbook site.yml --limit @retry_hosts.txt`
* If [RETRY_FILES_ENABLED](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#retry-files-enabled) is set to `True`, a `.retry` file will be created after the `ansible-playbook` run containing a list of failed hosts from all plays. This file is overwritten each time `ansible-playbook` finishes running.
	* `ansible-playbook site.yml --limit @site.retry`
* To apply your knowledge of patterns with Ansible commands and playbooks, read [Introduction to ad hoc commands](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#intro-adhoc) and [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#playbooks-intro).

### Connection methods and details
> [source](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html)
* This section shows you how to expand and refine the connection methods Ansible uses for your inventory.
* ControlPersist and paramiko
	* By default, Ansible uses native OpenSSH, because it supports ControlPersist (a performance feature), Kerberos, and options in `~/.ssh/config` such as Jump Host setup.
	* If your control machine uses an older version of OpenSSH that does not support ControlPersist, Ansible will fallback to a Python implementation of OpenSSH called `paramiko`.
* Setting a remote user
	* By default, Ansible connects to all remote devices with the user name you are using on the control node. If that user name does not exist on a remote device, you can set a different user name for the connection. [read further...](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#setting-a-remote-user)
* [Setting up SSH keys](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#setting-up-ssh-keys)
* [Running against localhost](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#running-against-localhost)
* [Managing host key checking](https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#managing-host-key-checking)
* Other connection methods: Ansible can use a variety of connection methods beyond SSH. You can select any connection plugin, including managing things locally and managing chroot, lxc, and jail containers. A mode called ‘ansible-pull’ can also invert the system and have systems ‘phone home’ via scheduled git checkouts to pull configuration directives from a central repository.