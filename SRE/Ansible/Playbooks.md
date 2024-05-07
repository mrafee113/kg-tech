* Playbooks are automation blueprints, in `YAML` format, that Ansible uses to deploy and configure nodes in an inventory.

### Playbooks intro
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html#ansible-playbooks)
* Ansible Playbooks offer a repeatable, re-usable, simple configuration management and multi-machine deployment system, one that is well suited to deploying complex applications.
* If you need to execute a task with Ansible more than once, write a playbook and put it under source control. Then you can use the playbook to push out new configuration or confirm the configuration of remote systems.
* The playbooks in the [ansible-examples repository](https://github.com/ansible/ansible-examples) illustrate many useful techniques. You may want to look at these in another tab as you read the documentation.

#### Playbook syntax
* Playbooks are expressed in YAML format with a minimum of syntax.
* A playbook is composed of one or more ‘plays’ in an ordered list. The terms ‘playbook’ and ‘play’ are sports analogies. Each play executes part of the overall goal of the playbook, running one or more tasks. Each task calls an Ansible module.

#### Playbook execution
* A playbook runs in order from top to bottom.
* Within each play, tasks also run in order from top to bottom.
* Playbooks with multiple ‘plays’ can orchestrate multi-machine deployments, running one play on your webservers, then another play on your database servers, then a third play on your network infrastructure, and so on.
* At a minimum, each play defines two things:
	* the managed nodes to target, using a [[SRE/Ansible/Building Inventories#Patterns: targeting hosts and groups]]
	* at least one task to execute
* Your playbook can include more than just a hosts line and tasks. For example a `remote_user`.
* You can add other [Playbook Keywords](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#playbook-keywords) at the playbook, play, or task level to influence how Ansible behaves. Playbook keywords can control the [connection plugin](https://docs.ansible.com/ansible/latest/plugins/connection.html#connection-plugins), whether to use [privilege escalation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html#become), how to handle errors, and more.
* To support a variety of environments, Ansible lets you set many of these parameters as command-line flags, in your Ansible configuration, or in your inventory. Learning the [precedence rules](https://docs.ansible.com/ansible/latest/reference_appendices/general_precedence.html#general-precedence-rules) for these sources of data will help you as you expand your Ansible ecosystem.
* Task execution
	* By default, Ansible executes each task in order, one at a time, against all machines matched by the host pattern. Each task executes a module with specific arguments. When a task has executed on all target machines, Ansible moves on to the next task.
	* You can use [strategies](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#playbooks-strategies) to change this default behavior. Within each play, Ansible applies the same task directives to all hosts. If a task fails on a host, Ansible takes that host out of the rotation for the rest of the playbook.
	* When you run a playbook, Ansible returns information about connections, the `name` lines of all your plays and tasks, whether each task has succeeded or failed on each machine, and whether each task has made a change on each machine. At the bottom of the playbook execution, Ansible provides a summary of the nodes that were targeted and how they performed. General failures and fatal “unreachable” communication attempts are kept separate in the counts.
* Desired state and 'idempotency'
	* Most Ansible modules check whether the desired final state has already been achieved, and exit without performing any actions if that state has been achieved, so that repeating the task does not change the final state. Modules that behave this way are often called **idempotent**.
	* Whether you run a playbook once, or multiple times, the outcome should be the same. However, not all playbooks and not all modules behave this way. If you are unsure, test your playbooks in a sandbox environment before running them multiple times in production.
* Running playbooks
	* To run your playbook, use the [[SRE/Ansible/Command Line Tools#^cli-ansible-playbook|ansible-playbook]] command.
	* `ansible-playbook playbook.yml -f 10`

### Working with playbooks
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks.html)

#### Templating (jinja2)
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html)
* Ansible uses Jinja2 templating to enable dynamic expressions and access to [variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#playbooks-variables) and [facts](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html#vars-and-facts).
* You can use templating with the [template module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#template-module). For example, you can create a template for a configuration file, then deploy that configuration file to multiple environments and supply the correct data (IP address, hostname, version) for each environment.
* You can also use templating in playbooks directly, by templating task names and more.
* You can use all the [standard filters and tests](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters "(in Jinja v3.1.x)") included in Jinja2. Ansible includes additional specialized filters for selecting and transforming data, tests for evaluating template expressions, and [Lookup plugins](https://docs.ansible.com/ansible/latest/plugins/lookup.html#lookup-plugins) for retrieving data from external sources such as files, APIs, and databases for use in templating.
* All templating happens on the Ansible controller **before** the task is sent and executed on the target machine. This approach minimizes the package requirements on the target (jinja2 is only required on the controller). It also limits the amount of data Ansible passes to the target machine. Ansible parses templates on the controller and passes only the information needed for each task to the target machine, instead of passing all the data on the controller and parsing it on the target.

#### Using filters to manipulate data
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html)
* Filters let you transform JSON data into YAML data, split a URL to extract the hostname, get the SHA1 hash of a string, add or multiply integers, and much more.
* You can use the Ansible-specific filters to manipulate your data, or use any of the standard filters shipped with Jinja2 - see the list of [built-in filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters "(in Jinja v3.1.x)") in the official Jinja2 template documentation. You can also use [Python methods](https://jinja.palletsprojects.com/en/3.1.x/templates/#python-methods "(in Jinja v3.1.x)") to transform data. You can [create custom Ansible filters as plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-filter-plugins), though we generally welcome new filters into the ansible-core repo so everyone can use them.
* Because templating happens on the Ansible controller, **not** on the target host, filters execute on the controller and transform data locally.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This a list of topics as a heads up:
	* Handling undefined variables
	* Defining different values for true/false/null (ternary)
	* Managing data types
	* Formatting data: YAML and JSON
	* Combining and selecting data
	* Randomizing data
	* Managing list variables
	* Selecting from sets or lists (set theory)
	* Calculating numbers (math)
	* Managing network interactions
	* Hashing and encrypting strings and passwords
	* Manipulating text
	* Manipulating strings
	* Managing UUIDs
	* Handling dates and times
	* Getting Kubernetes resource names

#### Tests
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tests.html)
* [Tests](https://jinja.palletsprojects.com/en/latest/templates/#tests) in Jinja are a way of evaluating template expressions and returning True or False. Jinja ships with many of these. See [builtin tests](https://jinja.palletsprojects.com/en/latest/templates/#builtin-tests) in the official Jinja template documentation.
* The main difference between tests and filters are that **Jinja tests are used for comparisons**, whereas **filters are used for data manipulation**, and have different applications in jinja. Tests can also be used in list processing filters, like `map()` and `select()` to choose items in the list.
* Like all templating, tests always execute on the Ansible controller, **not** on the target of a task, as they test local data.
* In addition to those Jinja2 tests, Ansible supplies a few more and users can easily create their own.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Test syntax
	* Testing strings
	* Vault
	* Testing truthiness
	* Comparing versions
	* Set theory tests
	* Testing if a list contains a value
	* Testing if a list value is True
	* Testing paths
	* Testing size formats
	* Testing task results
	* Type Tests

#### Lookups
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_lookups.html)
* Lookup plugins retrieve data from outside sources such as files, databases, key/value stores, APIs, and other services.
* Like all templating, lookups execute and are evaluated on the Ansible control machine. Ansible makes the data returned by a lookup plugin available using the standard templating system.
* Before Ansible 2.5, lookups were mostly used indirectly in `with_<lookup>` constructs for looping. Starting with Ansible 2.5, lookups are used more explicitly as part of Jinja2 expressions fed into the `loop` keyword.
* For more details and a list of lookup plugins in ansible-core, see [Working with plugins](https://docs.ansible.com/ansible/latest/plugins/plugins.html#plugins-lookup). You may also find lookup plugins in collections. You can review a list of lookup plugins installed on your control machine with the command `ansible-doc -l -t lookup`.

#### Python3 in templates
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_python_version.html)
* Ansible uses Jinja2 to take advantage of Python data types and standard functions in templates and variables. You can use these data types and standard functions to perform a rich set of operations on your data.

#### The now function
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating_now.html)
* The `now()` Jinja2 function retrieves a Python datetime object or a string representation for the current time.
	* `utc` specifies `True` to get the current time in UTC. Defaults to `False`.
	* `fmt` accepts a [strftime](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) string that returns a formatted date time string.

#### Loops
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_loops.html)
* Ansible offers the `loop`, `with_<lookup>`, and `until` keywords to execute a task multiple times.
* Examples of commonly-used loops include changing ownership on several files and/or directories with the [file module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html#file-module), creating multiple users with the [user module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/user_module.html#user-module), and repeating a polling step until a certain result is reached.
* **Note**:
	* We added `loop` in Ansible 2.5. It is not yet a full replacement for `with_<lookup>`, but we recommend it for most use cases.
	* We have not deprecated the use of `with_<lookup>` - that syntax will still be valid for the foreseeable future.
	* We are looking to improve `loop` syntax.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Comparing `loop` and `with_*`
	* Standard loops
	* Registering variables with a loop
	* Complex loops
	* Ensuring list input for `loop:` using `query` rather than `lookup`
	* Adding controls to loops
	* Migrating from with_X to loop

#### Controlling where tasks run: delegation and local actions
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_delegation.html)
* By default Ansible gathers facts and executes all tasks on the machines that match the `hosts` line of your playbook. This page shows you how to delegate tasks to a different machine or group, delegate facts to specific machines or groups, or run an entire playbook locally.
* Using these approaches, you can manage inter-related environments precisely and efficiently.
	* For example, when updating your webservers, you might need to remove them from a load-balanced pool temporarily. You cannot perform this task on the webservers themselves.
	* By delegating the task to localhost, you keep all the tasks within the same play.
* Tasks that cannot be delegated: Some tasks always execute on the controller. These tasks, including `include`, `add_host`, and `debug`, cannot be delegated.

##### Delegating tasks
* If you want to perform a task on one host with reference to other hosts, use the `delegate_to` keyword on a task. This is ideal for managing nodes in a load balanced pool or for controlling outage windows.
* You can use delegation with the [serial](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#rolling-update-batch-size) keyword to control the number of hosts executing at one time:
	```yaml
	---
	- hosts: webservers
	  serial: 5
	
	  tasks:
	    - name: Take out of load balancer pool
	      ansible.builtin.command: /usr/bin/take_out_of_pool {{ inventory_hostname }}
	      delegate_to: 127.0.0.1
	
	    - name: Actual steps would go here
	      ansible.builtin.yum:
	        name: acme-web-stack
	        state: latest
	
	    - name: Add back to load balancer pool
	      ansible.builtin.command: /usr/bin/add_back_to_pool {{ inventory_hostname }}
	      delegate_to: 127.0.0.1
	```
* The first and third tasks in this play run on 127.0.0.1, which is the machine running Ansible. There is also a shorthand syntax that you can use on a per-task basis: `local_action`. Here is the same playbook as above, but using the shorthand syntax for delegating to 127.0.0.1:
	```yaml
	---
	# ...
	
	  tasks:
	    - name: Take out of load balancer pool
	      local_action: ansible.builtin.command /usr/bin/take_out_of_pool {{ inventory_hostname }}
	
	# ...
	
	    - name: Add back to load balancer pool
	      local_action: ansible.builtin.command /usr/bin/add_back_to_pool {{ inventory_hostname }}
	```
* You can use a local action to call ‘rsync’ to recursively copy files to the managed servers:
	```yaml
	---
	# ...
	
	  tasks:
	    - name: Recursively copy files from management server to target
	      local_action: ansible.builtin.command rsync -a /path/to/files {{ inventory_hostname }}:/path/to/target/
	```
* To specify more arguments, use the following syntax:
	```yaml
	---
	# ...
	
	  tasks:
	    - name: Send summary mail
	      local_action:
	        module: community.general.mail
	        subject: "Summary Mail"
	        to: "{{ mail_recipient }}"
	        body: "{{ mail_body }}"
	      run_once: True
	```
* ***NOTE***: The ansible_host variable and other connection variables, if present, reflects information about the host a task is delegated to, not the inventory_hostname.
> [!Warning]
> Although you can `delegate_to` a host that does not exist in inventory (by adding IP address, DNS name or whatever requirement the connection plugin has), doing so does not add the host to your inventory and might cause issues. Hosts delegated to in this way do not inherit variables from the “all” group’, so variables like connection user and key are missing. If you must `delegate_to` a non-inventory host, use the [add host module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/add_host_module.html#add-host-module).

##### Delegation and parallel execution
* By default Ansible tasks are executed in parallel. Delegating a task does not change this and does not handle concurrency issues (multiple forks writing to the same file). Most commonly, users are affected by this when updating a single file on a single delegated to host for all hosts (using the `copy`, `template`, or `lineinfile` modules, for example). They will still operate in parallel forks (default 5) and overwrite each other.
* This can be handled in several ways:
	```yaml
	- name: "handle concurrency with a loop on the hosts with `run_once: true`"
	  lineinfile: "<options here>"
	  run_once: true
	  loop: '{{ ansible_play_hosts_all }}'
	```
* By using an intermediate play with serial: 1 or using throttle: 1 at task level, for more detail see [Controlling playbook execution: strategies and more](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#playbooks-strategies)

##### Delegating facts
* Delegating Ansible tasks is like delegating tasks in the real world - your groceries belong to you, even if someone else delivers them to your home. Similarly, any facts gathered by a delegated task are assigned by default to the inventory_hostname (the current host), not to the host which produced the facts (the delegated to host).
* To assign gathered facts to the delegated host instead of the current host, set `delegate_facts` to `true`:
	```yaml
	---
	- hosts: app_servers
	
	  tasks:
	    - name: Gather facts from db servers
	      ansible.builtin.setup:
	      delegate_to: "{{ item }}"
	      delegate_facts: true
	      loop: "{{ groups['dbservers'] }}"
	```
* This task gathers facts for the machines in the dbservers group and assigns the facts to those machines, even though the play targets the app_servers group.
* This task gathers facts for the machines in the dbservers group and assigns the facts to those machines, even though the play targets the app_servers group. This way you can lookup hostvars[‘dbhost1’][‘ansible_default_ipv4’][‘address’] even though dbservers were not part of the play, or left out by using –limit.

##### Local playbooks
* It may be useful to use a playbook locally on a remote host, rather than by connecting over SSH. This can be useful for assuring the configuration of a system by putting a playbook in a crontab. This may also be used to run a playbook inside an OS installer, such as an Anaconda kickstart.
* To run an entire playbook locally, just set the `hosts:` line to `hosts: 127.0.0.1` and then run the playbook like so:
	* `ansible-playbook playbook.yml --connection=local`
* Alternatively, a local connection can be used in a single playbook play, even if other plays in the playbook use the default remote connection type:
	```yaml
	---
	- hosts: 127.0.0.1
	  connection: local
	```
* **Note**: If you set the connection to local and there is no ansible_python_interpreter set, modules will run under /usr/bin/python and not under {{ ansible_playbook_python }}. Be sure to set ansible_python_interpreter: “{{ ansible_playbook_python }}” in host_vars/localhost.yml, for example. You can avoid this issue by using `local_action` or `delegate_to: localhost` instead.

#### Conditionals
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html)
* In a playbook, you may want to execute different tasks, or have different goals, depending on the value of a fact (data about the remote system), a variable, or the result of a previous task. You may want the value of some variables to depend on the value of other variables. Or you may want to create additional groups of hosts based on whether the hosts match other criteria. You can do all of these things with conditionals.
* Ansible uses Jinja2 [tests](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tests.html#playbooks-tests) and [filters](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#playbooks-filters) in conditionals. Ansible supports all the standard tests and filters, and adds some unique ones as well.
* **Note**: There are many options to control execution flow in Ansible. You can find more examples of supported conditionals at [here](https://jinja.palletsprojects.com/en/latest/templates/#comparisons).

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Basic conditionals with `when`
	* Debugging conditionals
	* Commonly-used facts

#### Blocks
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_blocks.html)
* Blocks create logical groups of tasks. Blocks also offer ways to handle task errors, similar to exception handling in many programming languages.

##### Grouping tasks with blocks
* All tasks in a block inherit directives applied at the block level. Most of what you can apply to a single task (with the exception of loops) can be applied at the block level, so blocks make it much easier to set data or directives common to the tasks.
* The directive does not affect the block itself, it is only inherited by the tasks enclosed by a block. For example, a when statement is applied to the tasks within a block, not to the block itself.
	```yaml
	 tasks:
	   - name: Install, configure, and start Apache
	     block:
	       - name: Install httpd and memcached
	         ansible.builtin.yum:
	           name:
	           - httpd
	           - memcached
	           state: present
	
	       - name: Apply the foo config template
	         ansible.builtin.template:
	           src: templates/src.j2
	           dest: /etc/foo.conf
	
	       - name: Start service bar and enable it
	         ansible.builtin.service:
	           name: bar
	           state: started
	           enabled: True
	     when: ansible_facts['distribution'] == 'CentOS'
	     become: true
	     become_user: root
	     ignore_errors: true
	```
* In the example above, the ‘when’ condition will be evaluated before Ansible runs each of the three tasks in the block.
* All three tasks also inherit the privilege escalation directives, running as the root user.
* Finally, `ignore_errors: true` ensures that Ansible continues to execute the playbook even if some of the tasks fail.
* Names for blocks have been available since Ansible 2.3. We recommend using names in all tasks, within blocks or elsewhere, for better visibility into the tasks being executed when you run the playbook.

##### Handling errors with blocks
* You can control how Ansible responds to task errors using blocks with `rescue` and `always` sections.
* Rescue blocks specify tasks to run when an earlier task in a block fails. This approach is similar to exception handling in many programming languages. Ansible only runs rescue blocks after a task returns a ‘failed’ state. Bad task definitions and unreachable hosts will not trigger the rescue block.
	```yaml
	 tasks:
	 - name: Handle the error
	   block:
	     - name: Print a message
	       ansible.builtin.debug:
	         msg: 'I execute normally'
	
	     - name: Force a failure
	       ansible.builtin.command: /bin/false
	
	     - name: Never print this
	       ansible.builtin.debug:
	         msg: 'I never execute, due to the above task failing, :-('
	   rescue:
	     - name: Print when errors
	       ansible.builtin.debug:
	         msg: 'I caught an error, can do stuff here to fix it, :-)'
	```
* You can also add an `always` section to a block. Tasks in the `always` section run no matter what the task status of the previous block is.
	```yaml
	 - name: Always do X
	   block:
	     - name: Print a message
	       ansible.builtin.debug:
	         msg: 'I execute normally'
	
	     - name: Force a failure
	       ansible.builtin.command: /bin/false
	
	     - name: Never print this
	       ansible.builtin.debug:
	         msg: 'I never execute :-('
	   always:
	     - name: Always do this
	       ansible.builtin.debug:
	         msg: "This always executes, :-)"
	```
* Together, these elements offer complex error handling.
	```yaml
	- name: Attempt and graceful roll back demo
	  block:
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: 'I execute normally'
	
	    - name: Force a failure
	      ansible.builtin.command: /bin/false
	
	    - name: Never print this
	      ansible.builtin.debug:
	        msg: 'I never execute, due to the above task failing, :-('
	  rescue:
	    - name: Print when errors
	      ansible.builtin.debug:
	        msg: 'I caught an error'
	
	    - name: Force a failure in middle of recovery! >:-)
	      ansible.builtin.command: /bin/false
	
	    - name: Never print this
	      ansible.builtin.debug:
	        msg: 'I also never execute :-('
	  always:
	    - name: Always do this
	      ansible.builtin.debug:
	        msg: "This always executes"
	```
* The tasks in the `block` execute normally. If any tasks in the block return `failed`, the `rescue` section executes tasks to recover from the error. The `always` section runs regardless of the results of the `block` and `rescue` sections.
* If an error occurs in the block and the rescue task succeeds, Ansible reverts the failed status of the original task for the run and continues to run the play as if the original task had succeeded. The rescued task is considered successful, and does not trigger `max_fail_percentage` or `any_errors_fatal` configurations. However, Ansible still reports a failure in the playbook statistics.
* You can use blocks with `flush_handlers` in a rescue task to ensure that all handlers run even if an error occurs:
```yaml
 tasks:
   - name: Attempt and graceful roll back demo
     block:
       - name: Print a message
         ansible.builtin.debug:
           msg: 'I execute normally'
         changed_when: true
         notify: run me even after an error

       - name: Force a failure
         ansible.builtin.command: /bin/false
     rescue:
       - name: Make sure all handlers run
         meta: flush_handlers
 handlers:
    - name: Run me even after an error
      ansible.builtin.debug:
        msg: 'This handler runs even on error'
```
* Ansible provides a couple of variables for tasks in the `rescue` portion of a block:
	* `ansible_failed_task` is the task that returned ‘failed’ and triggered the rescue. For example, to get the name use `ansible_failed_task.name`.
	* `ansible_failed_result` is the captured return result of the failed task that triggered the rescue. This would equate to having used this var in the `register` keyword.
	* **Note**: In `ansible-core` 2.14 or later, both variables are propagated from an inner block to an outer `rescue` portion of a block.

#### Handlers: running operations on change
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html)
* Sometimes you want a task to run only when a change is made on a machine.
* For example, you may want to restart a service if a task updates the configuration of that service, but not if the configuration is unchanged. Ansible uses handlers to address this use case. Handlers are tasks that only run when notified.

##### Handler example
* This playbook, `verify-apache.yml`, contains a single play with a handler.
	```yaml
	---
	- name: Verify apache installation
	  hosts: webservers
	  vars:
	    http_port: 80
	    max_clients: 200
	  remote_user: root
	  tasks:
	    - name: Ensure apache is at the latest version
	      ansible.builtin.yum:
	        name: httpd
	        state: latest
	
	    - name: Write the apache config file
	      ansible.builtin.template:
	        src: /srv/httpd.j2
	        dest: /etc/httpd.conf
	      notify:
	      - Restart apache
	
	    - name: Ensure apache is running
	      ansible.builtin.service:
	        name: httpd
	        state: started
	
	  handlers:
	    - name: Restart apache
	      ansible.builtin.service:
	        name: httpd
	        state: restarted
	```
* In this example playbook, the Apache server is restarted by the handler after all tasks complete in the play.

##### Notifying handlers
* Tasks can instruct one or more handlers to execute using the `notify` keyword. The `notify` keyword can be applied to a task and accepts a list of handler names that are notified on a task change.
* Alternately, a string containing a single handler name can be supplied as well.
* The following example demonstrates how multiple handlers can be notified by a single task:
	```yaml
	tasks:
	- name: Template configuration file
	  ansible.builtin.template:
	    src: template.j2
	    dest: /etc/foo.conf
	  notify:
	    - Restart apache
	    - Restart memcached
	
	handlers:
	  - name: Restart memcached
	    ansible.builtin.service:
	      name: memcached
	      state: restarted
	
	  - name: Restart apache
	    ansible.builtin.service:
	      name: apache
	      state: restarted
	```
* In the above example the handlers are executed on task change in the following order: `Restart memcached`, `Restart apache`. Handlers are executed in the order they are defined in the `handlers` section, not in the order listed in the `notify` statement.
* Notifying the same handler multiple times will result in executing the handler only once regardless of how many tasks notify it. For example, if multiple tasks update a configuration file and notify a handler to restart Apache, Ansible only bounces Apache once to avoid unnecessary restarts.

##### Naming handlers
* Handlers must be named in order for tasks to be able to notify them using the `notify` keyword.
* Alternately, handlers can utilize the `listen` keyword. Using this handler keyword, handlers can listen on topics that can group multiple handlers as follows:
	```yaml
	tasks:
	  - name: Restart everything
	    command: echo "this task will restart the web services"
	    notify: "restart web services"
	
	handlers:
	  - name: Restart memcached
	    service:
	      name: memcached
	      state: restarted
	    listen: "restart web services"
	
	  - name: Restart apache
	    service:
	      name: apache
	      state: restarted
	    listen: "restart web services"
	```
* Notifying the `restart web services` topic results in executing all handlers listening to that topic regardless of how those handlers are named.
* This use makes it much easier to trigger multiple handlers. It also decouples handlers from their names, making it easier to share handlers among playbooks and roles (especially when using third-party roles from a shared source such as Ansible Galaxy).
* Each handler should have a globally unique name. If multiple handlers are defined with the same name, only the last one defined is notified with `notify`, effectively shadowing all of the previous handlers with the same name. Alternately handlers sharing the same name can all be notified and executed if they listen on the same topic by notifying that topic.
* There is only one global scope for handlers (handler names and listen topics) regardless of where the handlers are defined. This also includes handlers defined in roles.

##### Controlling when handlers run
* By default, handlers run after all the tasks in a particular play have been completed. Notified handlers are executed automatically after each of the following sections, in the following order: `pre_tasks`, `roles`/`tasks` and `post_tasks`. This approach is efficient, because the handler only runs once, regardless of how many tasks notify it. For example, if multiple tasks update a configuration file and notify a handler to restart Apache, Ansible only bounces Apache once to avoid unnecessary restarts.
* If you need handlers to run before the end of the play, add a task to flush them using the [meta module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/meta_module.html#meta-module), which executes Ansible actions:
	```yaml
	tasks:
	  - name: Some tasks go here
	    ansible.builtin.shell: ...
	
	  - name: Flush handlers
	    meta: flush_handlers
	
	  - name: Some other tasks
	    ansible.builtin.shell: ...
	```
* The `meta: flush_handlers` task triggers any handlers that have been notified at that point in the play.
* Once handlers are executed, either automatically after each mentioned section or manually by the `flush_handlers` meta task, they can be notified and run again in later sections of the play.

##### Using variables with handlers
* You may want your Ansible handlers to use variables. For example, if the name of a service varies slightly by distribution, you want your output to show the exact name of the restarted service for each target machine. Avoid placing variables in the name of the handler. Since handler names are templated early on, Ansible may not have a value available for a handler name like this:
	```yaml
	handlers:
	# This handler name may cause your play to fail!
	- name: Restart "{{ web_service_name }}"
	```
* If the variable used in the handler name is not available, the entire play fails. Changing that variable mid-play **will not** result in newly created handler.
* Instead, place variables in the task parameters of your handler. You can load the values using `include_vars` like this:
	```yaml
	tasks:
	  - name: Set host variables based on distribution
	    include_vars: "{{ ansible_facts.distribution }}.yml"
	
	handlers:
	  - name: Restart web service
	    ansible.builtin.service:
	      name: "{{ web_service_name | default('httpd') }}"
	      state: restarted
	```
* While handler names can contain a template, `listen` topics cannot.

##### Handlers in roles
* Handlers from roles are not just contained in their roles but rather inserted into global scope with all other handlers from a play. As such they can be used outside of the role they are defined in. It also means that their name can conflict with handlers from outside the role. To ensure that a handler from a role is notified as opposed to one from outside the role with the same name, notify the handler by using its name in the following form: `role_name : handler_name`.
* Handlers notified within the `roles` section are automatically flushed at the end of the `tasks` section, but before any `tasks` handlers.

##### Includes and imports in handlers
* Notifying a dynamic include such as `include_task` as a handler results in executing all tasks from within the include. **It is not possible to notify a handler defined inside a dynamic include.**
* Having a static include such as `import_task` as a handler results in that handler being effectively rewritten by handlers from within that import before the play execution. **A static include itself cannot be notified;** the tasks from within that include, on the other hand, can be notified individually.

##### Meta tasks as handlers
* Since Ansible 2.14 [meta tasks](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/meta_module.html#ansible-collections-ansible-builtin-meta-module) are allowed to be used and notified as handlers. Note that however `flush_handlers` cannot be used as a handler to prevent unexpected behavior.

##### Limitations
* A handler cannot run `import_role` or `include_role`.

#### Error handling in playbooks
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_error_handling.html)
* When Ansible receives a non-zero return code from a command or a failure from a module, by default it stops executing on that host and continues on other hosts.
* However, in some circumstances you may want different behavior. Sometimes a non-zero return code indicates success. Sometimes you want a failure on one host to stop execution on all hosts. Ansible provides tools and settings to handle these situations and help you get the behavior, output, and reporting you want.

##### Ignoring failed commands
* By default Ansible stops executing tasks on a host when a task fails on that host. You can use `ignore_errors` to continue on in spite of the failure.
	```yaml
	- name: Do not count this as a failure
	  ansible.builtin.command: /bin/false
	  ignore_errors: true
	```
* The `ignore_errors` directive only works when the task is able to run and returns a value of ‘failed’. It does not make Ansible ignore undefined variable errors, connection failures, execution issues (for example, missing packages), or syntax errors.

##### Ignoring unreachable host errors
* You can ignore a task failure due to the host instance being ‘UNREACHABLE’ with the `ignore_unreachable` keyword. Ansible ignores the task errors, but continues to execute future tasks against the unreachable host. For example, at the task level:
	```yaml
	- name: This executes, fails, and the failure is ignored
	  ansible.builtin.command: /bin/true
	  ignore_unreachable: true
	
	- name: This executes, fails, and ends the play for this host
	  ansible.builtin.command: /bin/true
	```
* And at the playbook level:
	```yaml
	- hosts: all
	  ignore_unreachable: true
	  tasks:
	  - name: This executes, fails, and the failure is ignored
	    ansible.builtin.command: /bin/true
	
	  - name: This executes, fails, and ends the play for this host
	    ansible.builtin.command: /bin/true
	    ignore_unreachable: false
	```

##### Resetting unreachable hosts
* If Ansible cannot connect to a host, it marks that host as `UNREACHABLE` and removes it from the list of active hosts for the run. You can use `meta: clear_host_errors` to reactivate all hosts, so subsequent tasks can try to reach them again.

##### Handlers and failure
* Ansible runs [[SRE/Ansible/Playbooks#Handlers: running operations on change|handlers]] at the end of each play. If a task notifies a handler but another task fails later in the play, by default the handler does _not_ run on that host, which may leave the host in an unexpected state. For example, a task could update a configuration file and notify a handler to restart some service. If a task later in the same play fails, the configuration file might be changed but the service will not be restarted.
* You can change this behavior with the `--force-handlers` command-line option, by including `force_handlers: True` in a play, or by adding `force_handlers = True` to ansible.cfg.
* When handlers are forced, Ansible will run all notified handlers on all hosts, even hosts with failed tasks. (Note that certain errors could still prevent the handler from running, such as a host becoming unreachable.)

##### Defining failure
* Ansible lets you define what “failure” means in each task using the `failed_when` conditional. As with all conditionals in Ansible, lists of multiple `failed_when` conditions are joined with an implicit `and`, meaning the task only fails when _all_ conditions are met. If you want to trigger a failure when any of the conditions is met, you must define the conditions in a string with an explicit `or` operator.
* You may check for failure by searching for a word or phrase in the output of a command
	```yaml
	- name: Fail task when the command error output prints FAILED
	  ansible.builtin.command: /usr/bin/example-command -x -y -z
	  register: command_result
	  failed_when: "'FAILED' in command_result.stderr"
	```
* or based on the return code
	```yaml
	- name: Fail task when both files are identical
	  ansible.builtin.raw: diff foo/file1 bar/file2
	  register: diff_cmd
	  failed_when: diff_cmd.rc == 0 or diff_cmd.rc >= 2
	```
* You can also combine multiple conditions for failure. This task will fail if both conditions are true:
	```yaml
	- name: Check if a file exists in temp and fail task if it does
	  ansible.builtin.command: ls /tmp/this_should_not_be_here
	  register: result
	  failed_when:
	    - result.rc == 0
	    - '"No such" not in result.stdout'
	```
* If you want the task to fail when only one condition is satisfied, change the `failed_when` definition to
	```yaml
	failed_when: result.rc == 0 or "No such" not in result.stdout
	```
* If you have too many conditions to fit neatly into one line, you can split it into a multi-line YAML value with `>`.
	```yaml
	- name: example of many failed_when conditions with OR
	  ansible.builtin.shell: "./myBinary"
	  register: ret
	  failed_when: >
	    ("No such file or directory" in ret.stdout) or
	    (ret.stderr != '') or
	    (ret.rc == 10)
	```

##### Defininf "changed"
* Ansible lets you define when a particular task has “changed” a remote node using the `changed_when` conditional.
* This lets you determine, based on return codes or output, whether a change should be reported in Ansible statistics and whether a handler should be triggered or not.
* For example:
	```yaml
	tasks:
	
	  - name: Report 'changed' when the return code is not equal to 2
	    ansible.builtin.shell: /usr/bin/billybass --mode="take me to the river"
	    register: bass_result
	    changed_when: "bass_result.rc != 2"
	
	  - name: This will never report 'changed' status
	    ansible.builtin.shell: wall 'beep'
	    changed_when: False
	```
* You can also combine multiple conditions to override “changed” result.
	```yaml
	- name: Combine multiple conditions to override 'changed' result
	  ansible.builtin.command: /bin/fake_command
	  register: result
	  ignore_errors: True
	  changed_when:
	    - '"ERROR" in result.stderr'
	    - result.rc == 2
	```
* **Note**: Just like `when` these two conditionals do not require templating delimiters (`{{ }}`) as they are implied.
* See [[SRE/Ansible/Playbooks#Defining failure|Defining failure]] for more conditional syntax examples.

##### Ensuring success for command and shell
* The [command](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html#command-module) and [shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html#shell-module) modules care about return codes, so if you have a command whose successful exit code is not zero, you can do this:
	```yaml
	tasks:
	  - name: Run this command and ignore the result
	    ansible.builtin.shell: /usr/bin/somecommand || /bin/true
	```

##### Aborting a play on all hosts
* Sometimes you want a failure on a single host, or failures on a certain percentage of hosts, to abort the entire play on all hosts. You can stop play execution after the first failure happens with `any_errors_fatal`. For finer-grained control, you can use `max_fail_percentage` to abort the run after a given percentage of hosts has failed.

###### Aborting on the first error: `any_errors_fatal`
* If you set `any_errors_fatal` and a task returns an error, Ansible finishes the fatal task on all hosts in the current batch, then stops executing the play on all hosts. Subsequent tasks and plays are not executed. You can recover from fatal errors by adding a [[SRE/Ansible/Playbooks#Handling errors with blocks|rescue section]] to the block. You can set `any_errors_fatal` at the play or block level.
	```yaml
	- hosts: somehosts
	  any_errors_fatal: true
	  roles:
	    - myrole
	
	- hosts: somehosts
	  tasks:
	    - block:
	        - include_tasks: mytasks.yml
	      any_errors_fatal: true
	```
* You can use this feature when all tasks must be 100% successful to continue playbook execution. For example, if you run a service on machines in multiple data centers with load balancers to pass traffic from users to the service, you want all load balancers to be disabled before you stop the service for maintenance. To ensure that any failure in the task that disables the load balancers will stop all other tasks:
	```yaml
	---
	- hosts: load_balancers_dc_a
	  any_errors_fatal: true
	
	  tasks:
	    - name: Shut down datacenter 'A'
	      ansible.builtin.command: /usr/bin/disable-dc
	
	- hosts: frontends_dc_a
	
	  tasks:
	    - name: Stop service
	      ansible.builtin.command: /usr/bin/stop-software
	
	    - name: Update software
	      ansible.builtin.command: /usr/bin/upgrade-software
	
	- hosts: load_balancers_dc_a
	
	  tasks:
	    - name: Start datacenter 'A'
	      ansible.builtin.command: /usr/bin/enable-dc
	```
* In this example Ansible starts the software upgrade on the front ends only if all of the load balancers are successfully disabled.

###### Setting a maximum failure percentage
* By default, Ansible continues to execute tasks as long as there are hosts that have not yet failed. In some situations, such as when executing a rolling update, you may want to abort the play when a certain threshold of failures has been reached. To achieve this, you can set a maximum failure percentage on a play:
	```yaml
	---
	- hosts: webservers
	  max_fail_percentage: 30
	  serial: 10
	```
* The `max_fail_percentage` setting applies to each batch when you use it with [serial](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#rolling-update-batch-size). In the example above, if more than 3 of the 10 servers in the first (or any) batch of servers failed, the rest of the play would be aborted.

> [!Note]
> The percentage set must be exceeded, not equaled. For example, if serial were set to 4 and you wanted the task to abort the play when 2 of the systems failed, set the max_fail_percentage at 49 rather than 50.

##### Controlling errors in blocks
* You can also use blocks to define responses to task errors. This approach is similar to exception handling in many programming languages. See [[SRE/Ansible/Playbooks#Handling errors with blocks|Handling errors with blocks]] for details and examples.

#### Setting the remote environment
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_environment.html)
* You can use the `environment` keyword at the play, block, or task level to set an environment variable for an action on a remote host.
* With this keyword, you can enable using a proxy for a task that does http requests, set the required environment variables for language-specific version managers, and more.
* When you set a value with `environment:` at the play or block level, it is available only to tasks within the play or block that are executed by the same user.
* The `environment:` keyword does not affect Ansible itself, Ansible configuration settings, the environment for other users, or the execution of other plugins like lookups and filters.
* Variables set with `environment:` do not automatically become Ansible facts, even when you set them at the play level. You must include an explicit `gather_facts` task in your playbook and set the `environment` keyword on that task to turn these values into Ansible facts.

##### Setting the remote environment in a task
* You can set the environment directly at the task level.
	```yaml
	- hosts: all
	  remote_user: root
	
	  tasks:
	
	    - name: Install cobbler
	      ansible.builtin.package:
	        name: cobbler
	        state: present
	      environment:
	        http_proxy: http://proxy.example.com:8080
	```
* You can re-use environment settings by defining them as variables in your play and accessing them in a task as you would access any stored Ansible variable.
	```yaml
	- hosts: all
	  remote_user: root
	
	  # create a variable named "proxy_env" that is a dictionary
	  vars:
	    proxy_env:
	      http_proxy: http://proxy.example.com:8080
	
	  tasks:
	
	    - name: Install cobbler
	      ansible.builtin.package:
	        name: cobbler
	        state: present
	      environment: "{{ proxy_env }}"
	```
* You can store environment settings for re-use in multiple playbooks by defining them in a group_vars file.
	```yaml
	---
	# file: group_vars/boston
	
	ntp_server: ntp.bos.example.com
	backup: bak.bos.example.com
	proxy_env:
	  http_proxy: http://proxy.bos.example.com:8080
	  https_proxy: http://proxy.bos.example.com:8080
	```
* You can set the remote environment at the play level.
	```yaml
	- hosts: testing
	
	  roles:
	     - php
	     - nginx
	
	  environment:
	    http_proxy: http://proxy.example.com:8080
	```
* These examples show proxy settings, but you can provide any number of settings this way.

###### Working with language-specific version managers
* Some language-specific version managers (such as rbenv and nvm) require you to set environment variables while these tools are in use. When using these tools manually, you usually source some environment variables from a script or from lines added to your shell configuration file. In Ansible, you can do this with the environment keyword at the play level.
	```yaml
	---
	### A playbook demonstrating a common npm workflow:
	# - Check for package.json in the application directory
	# - If package.json exists:
	#   * Run npm prune
	#   * Run npm install
	
	- hosts: application
	  become: false
	
	  vars:
	    node_app_dir: /var/local/my_node_app
	
	  environment:
	    NVM_DIR: /var/local/nvm
	    PATH: /var/local/nvm/versions/node/v4.2.1/bin:{{ ansible_env.PATH }}
	
	  tasks:
	  - name: Check for package.json
	    ansible.builtin.stat:
	      path: '{{ node_app_dir }}/package.json'
	    register: packagejson
	
	  - name: Run npm prune
	    ansible.builtin.command: npm prune
	    args:
	      chdir: '{{ node_app_dir }}'
	    when: packagejson.stat.exists
	
	  - name: Run npm install
	    community.general.npm:
	      path: '{{ node_app_dir }}'
	    when: packagejson.stat.exists
	```

> [!Note]
> The example above uses `ansible_env` as part of the PATH. Basing variables on `ansible_env` is risky. Ansible populates `ansible_env` values by gathering facts, so the value of the variables depends on the remote_user or become_user Ansible used when gathering those facts. If you change remote_user/become_user the values in `ansible_env` may not be the ones you expect.

> [!Warning]
> Environment variables are normally passed in clear text (shell plugin dependent) so they are not a recommended way of passing secrets to the module being executed.

* You can also specify the environment at the task level.
	```yaml
	---
	- name: Install ruby 2.3.1
	  ansible.builtin.command: rbenv install {{ rbenv_ruby_version }}
	  args:
	    creates: '{{ rbenv_root }}/versions/{{ rbenv_ruby_version }}/bin/ruby'
	  vars:
	    rbenv_root: /usr/local/rbenv
	    rbenv_ruby_version: 2.3.1
	  environment:
	    CONFIGURE_OPTS: '--disable-install-doc'
	    RBENV_ROOT: '{{ rbenv_root }}'
	    PATH: '{{ rbenv_root }}/bin:{{ rbenv_root }}/shims:{{ rbenv_plugins }}/ruby-build/bin:{{ ansible_env.PATH }}'
	```

#### Re-using ansible artifacts
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse.html)
* You can write a simple playbook in one very large file, and most users learn the one-file approach first.
* However, breaking your automation work up into smaller files is an excellent way to organize complex sets of tasks and reuse them.
* Smaller, more distributed artifacts let you re-use the same variables, tasks, and plays in multiple playbooks to address different use cases. You can use distributed artifacts across multiple parent playbooks or even multiple times within one playbook.
	* For example, you might want to update your customer database as part of several different playbooks. If you put all the tasks related to updating your database in a tasks file or a role, you can re-use them in many playbooks while only maintaining them in one place.

##### Creating re-usable files and roles
* Ansible offers four distributed, re-usable artifacts: variables files, task files, playbooks, and roles.
	* A variables file contains only variables.
	* A task file contains only tasks.
	* A playbook contains at least one play, and may contain variables, tasks, and other content. You can re-use tightly focused playbooks, but you can only re-use them statically, not dynamically.
	* A role contains a set of related tasks, variables, defaults, handlers, and even modules or other plugins in a defined file-tree. Unlike variables files, task files, or playbooks, roles can be easily uploaded and shared through Ansible Galaxy. See [Roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#playbooks-reuse-roles) for details about creating and using roles.

##### Re-using playbooks
* You can incorporate multiple playbooks into a main playbook. However, you can only use imports to re-use playbooks. For example:
	```yaml
	- import_playbook: webservers.yml
	- import_playbook: databases.yml
	```
* Importing incorporates playbooks in other playbooks statically. Ansible runs the plays and tasks in each imported playbook in the order they are listed, just as if they had been defined directly in the main playbook.
* You can select which playbook you want to import at runtime by defining your imported playbook filename with a variable, then passing the variable with either `--extra-vars` or the `vars` keyword. For example:
	```yaml
	- import_playbook: "/path/to/{{ import_from_extra_var }}"
	- import_playbook: "{{ import_from_vars }}"
	  vars:
	    import_from_vars: /path/to/one_playbook.yml
	```
* If you run this playbook with `ansible-playbook my_playbook -e import_from_extra_var=other_playbook.yml`, Ansible imports both one_playbook.yml and other_playbook.yml.
* When to turn a playbook into a role
	* For some use cases, simple playbooks work well. However, starting at a certain level of complexity, roles work better than playbooks.
	* A role lets you store your defaults, handlers, variables, and tasks in separate directories, instead of in a single long document. Roles are easy to share on Ansible Galaxy. 
	* For complex use cases, most users find roles easier to read, understand, and maintain than all-in-one playbooks.

##### Re-using files and roles
* Ansible offers two ways to re-use files and roles in a playbook: dynamic and static.
	* For dynamic re-use, add an `include_*` task in the tasks section of a play:
		* [include_role](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_role_module.html#include-role-module)
		* [include_tasks](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_tasks_module.html#include-tasks-module)
		* [include_vars](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_vars_module.html#include-vars-module)
	* For static re-use, add an `import_*` task in the tasks section of a play:
		* [import_role](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_role_module.html#import-role-module)
		* [import_task](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/import_tasks_module.html#import-tasks-module)
* Task include and import statements can be used at arbitrary depth.
* You can still use the bare [roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#roles-keyword) keyword at the play level to incorporate a role in a playbook statically. However, the bare [include](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_module.html#include-module) keyword, once used for both task files and playbook-level includes, is now deprecated.

###### Includes: dynamic re-use
* Including roles, tasks, or variables adds them to a playbook dynamically. Ansible processes included files and roles as they come up in a playbook, so included tasks can be affected by the results of earlier tasks within the top-level playbook. Included roles and tasks are similar to handlers - they may or may not run, depending on the results of other tasks in the top-level playbook.
* The primary advantage of using `include_*` statements is looping. When a loop is used with an include, the included tasks or role will be executed once for each item in the loop.
* The filenames for included roles, tasks, and vars are templated before inclusion.
* You can pass variables into includes. See [Variable precedence: Where should I put a variable?](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#ansible-variable-precedence) for more details on variable inheritance and precedence.

###### Imports: static re-use
* Importing roles, tasks, or playbooks adds them to a playbook statically. Ansible pre-processes imported files and roles before it runs any tasks in a playbook, so imported content is never affected by other tasks within the top-level playbook.
* The filenames for imported roles and tasks support templating, but the variables must be available when Ansible is pre-processing the imports. This can be done with the `vars` keyword or by using `--extra-vars`.
* You can pass variables to imports. You must pass variables if you want to run an imported file more than once in a playbook. For example:
	```yaml
	tasks:
	- import_tasks: wordpress.yml
	  vars:
	    wp_user: timmy
	
	- import_tasks: wordpress.yml
	  vars:
	    wp_user: alice
	
	- import_tasks: wordpress.yml
	  vars:
	    wp_user: bob
	```
* See [Variable precedence: Where should I put a variable?](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#ansible-variable-precedence) for more details on variable inheritance and precedence.

###### Comparing includes and imports: dynamic and static re-use
* Each approach to re-using distributed Ansible artifacts has advantages and limitations. You may choose dynamic re-use for some playbooks and static re-use for others.
* Although you can use both dynamic and static re-use in a single playbook, **it is best to select one approach per playbook.**
* Mixing static and dynamic re-use can introduce difficult-to-diagnose bugs into your playbooks.
* This table summarizes the main differences so you can choose the best approach for each playbook you create.

| | Include_* | Import_* |
| :- | :- | :- |
| **Type of re-use** | **Dynamic** | **Static** |
| When processed | At runtime, when encountered | Pre-processed during playbook parsing |
| Task or play | All includes are tasks | `import_playbook` cannot be a task |
| Task options | Apply only to include task itself | Apply to all child tasks in import |
| Calling from loops | Executed once for each loop item | Cannot be used in a loop |
| Using `--list-tags` | Tags within includes not listed | All tags appear with `--list-tags` |
| Using `--list-tasks` | Tasks within includes not listed | All tasks appear with `--list-tasks` |
| Notifying handlers | Cannot trigger handlers within includes | Can trigger individual imported handlers |
| Using `--start-at-task` | Cannot start at tasks within includes | Can start at imported tasks |
| Using inventory variables | Can `include_*: {{ inventory_var }}` | Cannot `import_*: {{ inventory_var }}` |
| With playbooks | No `include_playbook` | Can import full playbooks |
| With variable files | Can include variable file | Use `var_files` to import variables | 

> [!Note]
> There are also big differences in resource consumption and performance, imports are quite lean and fast, while includes require a lot of management and accounting.

##### Re-using tasks as handlers
* You can also use includes and imports in the [Handlers: running operations on change](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html#handlers) section of a playbook. 
* For instance, if you want to define how to restart Apache, you only have to do that once for all of your playbooks. You might make a `restarts.yml` file that looks like:
	```yaml
	# restarts.yml
	- name: Restart apache
	  ansible.builtin.service:
	    name: apache
	    state: restarted
	
	- name: Restart mysql
	  ansible.builtin.service:
	    name: mysql
	    state: restarted
	```
* You can trigger handlers from either an import or an include, but the procedure is different for each method of re-use.
	* If you include the file, you must notify the include itself, which triggers all the tasks in `restarts.yml`.
	* If you import the file, you must notify the individual task(s) within `restarts.yml`.
	* You can mix direct tasks and handlers with included or imported tasks and handlers.

###### Triggering included (dynamic) handlers
* Includes are executed at run-time, so the name of the include exists during play execution, but the included tasks do not exist until the include itself is triggered. To use the `Restart apache` task with dynamic re-use, refer to the name of the include itself. This approach triggers all tasks in the included file as handlers. For example, with the task file shown above:
	```yaml
	- name: Trigger an included (dynamic) handler
	  hosts: localhost
	  handlers:
	    - name: Restart services
	      include_tasks: restarts.yml
	  tasks:
	    - command: "true"
	      notify: Restart services
	```

###### Triggering imported (static) handlers
* Imports are processed before the play begins, so the name of the import no longer exists during play execution, but the names of the individual imported tasks do exist. To use the `Restart apache` task with static re-use, refer to the name of each task or tasks within the imported file. For example, with the task file shown above:
	```yaml
	- name: Trigger an imported (static) handler
	  hosts: localhost
	  handlers:
	    - name: Restart services
	      import_tasks: restarts.yml
	  tasks:
	    - command: "true"
	      notify: Restart apache
	    - command: "true"
	      notify: Restart mysql
	```

#### Roles
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html)
* Roles let you automatically load related vars, files, tasks, handlers, and other Ansible artifacts based on a known file structure. After you group your content in roles, you can easily reuse them and share them with other users.

##### Role directory structure
* An Ansible role has a defined directory structure with eight main standard directories. You must include at least one of these directories in each role. You can omit any directories the role does not use. For example:
	```
	roles/
	    common/               # this hierarchy represents a "role"
	        tasks/            #
	            main.yml      #  <-- tasks file can include smaller files if warranted
	        handlers/         #
	            main.yml      #  <-- handlers file
	        templates/        #  <-- files for use with the template resource
	            ntp.conf.j2   #  <------- templates end in .j2
	        files/            #
	            bar.txt       #  <-- files for use with the copy resource
	            foo.sh        #  <-- script files for use with the script resource
	        vars/             #
	            main.yml      #  <-- variables associated with this role
	        defaults/         #
	            main.yml      #  <-- default lower priority variables for this role
	        meta/             #
	            main.yml      #  <-- role dependencies
	        library/          # roles can also include custom modules
	        module_utils/     # roles can also include custom module_utils
	        lookup_plugins/   # or other types of plugins, like lookup in this case
	
	    webtier/              # same kind of structure as "common" was above, done for the webtier role
	    monitoring/           # ""
	    fooapp/               # ""
	```
* By default Ansible will look in each directory within a role for a `main.yml` file for relevant content (also `main.yaml` and `main`):
	* `tasks/main.yml` - the main list of tasks that the role executes.
	* `handlers/main.yml` - handlers, which may be used within or outside this role.
	* `library/my_module.py` - modules, which may be used within this role (see [Embedding modules and plugins in roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#embedding-modules-and-plugins-in-roles) for more information).
	* `defaults/main.yml` - default variables for the role (see [Using Variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#playbooks-variables) for more information). These variables have the lowest priority of any variables available, and can be easily overridden by any other variable, including inventory variables.
	* `vars/main.yml` - other variables for the role (see [Using Variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#playbooks-variables) for more information).
	* `files/main.yml` - files that the role deploys.
	* `templates/main.yml` - templates that the role deploys.
	* `meta/main.yml` - metadata for the role, including role dependencies and optional Galaxy metadata such as platforms supported.
* You can add other YAML files in some directories. For example, you can place platform-specific tasks in separate files and refer to them in the `tasks/main.yml` file:
	```yaml
	# roles/example/tasks/main.yml
	- name: Install the correct web server for RHEL
	  import_tasks: redhat.yml
	  when: ansible_facts['os_family']|lower == 'redhat'
	
	- name: Install the correct web server for Debian
	  import_tasks: debian.yml
	  when: ansible_facts['os_family']|lower == 'debian'
	
	# roles/example/tasks/redhat.yml
	- name: Install web server
	  ansible.builtin.yum:
	    name: "httpd"
	    state: present
	
	# roles/example/tasks/debian.yml
	- name: Install web server
	  ansible.builtin.apt:
	    name: "apache2"
	    state: present
	```
* Roles may also include modules and other plugin types in a directory called `library`. For more information, please refer to [Embedding modules and plugins in roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#embedding-modules-and-plugins-in-roles) below.

##### Storing and finding roles
* By default, Ansible looks for roles in the following locations:
	* in collections, if you are using them
	* in a directory called `roles/`, relative to the playbook file
	* in the configured [roles_path](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-roles-path). The default search path is `~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles`.
	* in the directory where the playbook file is located
* If you store your roles in a different location, set the [roles_path](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-roles-path) configuration option so Ansible can find your roles. Checking shared roles into a single location makes them easier to use in multiple playbooks. See [Configuring Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html#intro-configuration) for details about managing settings in ansible.cfg.
* Alternatively, you can call a role with a fully qualified path:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - role: '/path/to/my/roles/common'
	```

##### Using roles
* You can use roles in three ways:
	* at the play level with the `roles` option: This is the classic way of using roles in a play.
	* at the tasks level with `include_role`: You can reuse roles dynamically anywhere in the `tasks` section of a play using `include_role`.
	* at the tasks level with `import_role`: You can reuse roles statically anywhere in the `tasks` section of a play using `import_role`.

###### Using roles at the play level
* The classic (original) way to use roles is with the `roles` option for a given play:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - common
	    - webservers
	```
* When you use the `roles` option at the play level, for each role ‘x’:
	* If `roles/x/tasks/main.yml` exists, Ansible adds the tasks in that file to the play.
	* If `roles/x/handlers/main.yml` exists, Ansible adds the handlers in that file to the play.
	* If `roles/x/vars/main.yml` exists, Ansible adds the variables in that file to the play.
	* If `roles/x/defaults/main.yml` exists, Ansible adds the variables in that file to the play.
	* If `roles/x/meta/main.yml` exists, Ansible adds any role dependencies in that file to the list of roles.
	* Any copy, script, template or include tasks (in the role) can reference files in `roles/x/{files,templates,tasks}/` (dir depends on task) without having to path them relatively or absolutely.
* When you use the `roles` option at the play level, Ansible treats the roles as static imports and processes them during playbook parsing. Ansible executes each play in this order:
	* Any `pre_tasks` defined in the play.
	* Any handlers triggered by `pre_tasks`.
	* Each role listed in `roles:`, in the order listed. Any role dependencies defined in the role’s `meta/main.yml` run first, subject to tag filtering and conditionals. See [Using role dependencies](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#role-dependencies) for more details.
	* Any `tasks` defined in the play.
	* Any handlers triggered by the `roles` or `tasks`.
	* Any `post_tasks` defined in the play.
	* Any handlers triggered by `post_tasks`.

> [!Note]
> If using tags with tasks in a role, be sure to also tag your pre_tasks, post_tasks, and role dependencies and pass those along as well, especially if the pre/post tasks and role dependencies are used for monitoring outage window control or load balancing. See [Tags](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#tags) for details on adding and using tags.

* You can pass other keywords to the `roles` option:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - common
	    - role: foo_app_instance
	      vars:
	        dir: '/opt/a'
	        app_port: 5000
	      tags: typeA
	    - role: foo_app_instance
	      vars:
	        dir: '/opt/b'
	        app_port: 5001
	      tags: typeB
	```
* When you add a tag to the `role` option, Ansible applies the tag to ALL tasks within the role.
* When using `vars:` within the `roles:` section of a playbook, the variables are added to the play variables, making them available to all tasks within the play before and after the role. This behavior can be changed by [DEFAULT_PRIVATE_ROLE_VARS](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-private-role-vars).

###### Including roles: dynamic reuse
* You can reuse roles dynamically anywhere in the `tasks` section of a play using `include_role`. While roles added in a `roles` section run before any other tasks in a play, included roles run in the order they are defined. If there are other tasks before an `include_role` task, the other tasks will run first.
* To include a role:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: "this task runs before the example role"
	
	    - name: Include the example role
	      include_role:
	        name: example
	
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: "this task runs after the example role"
	```
* You can pass other keywords, including variables and tags, when including roles:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Include the foo_app_instance role
	      include_role:
	        name: foo_app_instance
	      vars:
	        dir: '/opt/a'
	        app_port: 5000
	      tags: typeA
	  ...
	```
* When you add a [tag](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#tags) to an `include_role` task, Ansible applies the tag only to the include itself. This means you can pass `--tags` to run only selected tasks from the role, if those tasks themselves have the same tag as the include statement. See [Selectively running tagged tasks in re-usable files](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#selective-reuse) for details.
* You can conditionally include a role:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Include the some_role role
	      include_role:
	        name: some_role
	      when: "ansible_facts['os_family'] == 'RedHat'"
	```

###### Importing roles: static reuse
* You can reuse roles statically anywhere in the `tasks` section of a play using `import_role`. The behavior is the same as using the `roles` keyword. For example:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: "before we run our role"
	
	    - name: Import the example role
	      import_role:
	        name: example
	
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: "after we ran our role"
	```
* You can pass other keywords, including variables and tags, when importing roles:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Import the foo_app_instance role
	      import_role:
	        name: foo_app_instance
	      vars:
	        dir: '/opt/a'
	        app_port: 5000
	  ...
	```
* When you add a tag to an `import_role` statement, Ansible applies the tag to all tasks within the role. See [Tag inheritance: adding tags to multiple tasks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#tag-inheritance) for details.

##### Role argument validation
* Beginning with version 2.11, you may choose to enable role argument validation based on an argument specification. This specification is defined in the `meta/argument_specs.yml` file (or with the `.yaml` file extension). When this argument specification is defined, a new task is inserted at the beginning of role execution that will validate the parameters supplied for the role against the specification. If the parameters fail validation, the role will fail execution.

> [!Note]
> Ansible also supports role specifications defined in the role `meta/main.yml` file, as well. However, any role that defines the specs within this file will not work on versions below 2.11. For this reason, we recommend using the `meta/argument_specs.yml` file to maintain backward compatibility.

> [!Note]
> When role argument validation is used on a role that has defined [dependencies](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#role-dependencies), then validation on those dependencies will run before the dependent role, even if argument validation fails for the dependent role.

* [Specification format](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#specification-format)

##### Running a role multiple times in a play
* Ansible only executes each role once in a play, even if you define it multiple times, unless the parameters defined on the role are different for each definition. For example, Ansible only runs the role `foo` once in a play like this:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - foo
	    - bar
	    - foo
	```
* You have two options to force Ansible to run a role more than once.

###### Passing different parameters
* If you pass different parameters in each role definition, Ansible runs the role more than once. Providing different variable values is not the same as passing different role parameters. You must use the `roles` keyword for this behavior, since `import_role` and `include_role` do not accept role parameters.
* This play runs the `foo` role twice:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - { role: foo, message: "first" }
	    - { role: foo, message: "second" }
	```
* This syntax also runs the `foo` role twice;
	```yaml
	---
	- hosts: webservers
	  roles:
	    - role: foo
	      message: "first"
	    - role: foo
	      message: "second"
	```
* In these examples, Ansible runs `foo` twice because each role definition has different parameters.

###### Using `allow_duplicates: true`
* Add `allow_duplicates: true` to the `meta/main.yml` file for the role:
	```yaml
	# playbook.yml
	---
	- hosts: webservers
	  roles:
	    - foo
	    - foo
	
	# roles/foo/meta/main.yml
	---
	allow_duplicates: true
	```
* In this example, Ansible runs `foo` twice because we have explicitly enabled it to do so.

##### Using role dependencies
* Role dependencies let you automatically pull in other roles when using a role.
* Role dependencies are prerequisites, not true dependencies. The roles do not have a parent/child relationship. Ansible loads all listed roles, runs the roles listed under `dependencies` first, then runs the role that lists them. The play object is the parent of all roles, including roles called by a `dependencies` list.
* For further information, continue reading "[Using role dependencies](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#using-role-dependencies)."

##### Embedding modules and plugins in roles
> [!Note]
> This applies only to standalone roles. Roles in collections do not support plugin embedding; they must use the collection’s `plugins` structure to distribute plugins.

* If you write a custom module (see [Should you develop a module?](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules.html#developing-modules)) or a plugin (see [Developing plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#developing-plugins)), you might wish to distribute it as part of a role. For example, if you write a module that helps configure your company’s internal software, and you want other people in your organization to use this module, but you do not want to tell everyone how to configure their Ansible library path, you can include the module in your internal_config role.
* To add a module or a plugin to a role: Alongside the ‘tasks’ and ‘handlers’ structure of a role, add a directory named ‘library’ and then include the module directly inside the ‘library’ directory.
* Assuming you had this:
	```
	roles/
	    my_custom_modules/
	        library/
	            module1
	            module2
	```
* The module will be usable in the role itself, as well as any roles that are called _after_ this role, as follows:
	```yaml
	---
	- hosts: webservers
	  roles:
	    - my_custom_modules
	    - some_other_role_using_my_custom_modules
	    - yet_another_role_using_my_custom_modules
	```
* If necessary, you can also embed a module in a role to modify a module in Ansible’s core distribution. For example, you can use the development version of a particular module before it is released in production releases by copying the module and embedding the copy in a role. Use this approach with caution, as API signatures may change in core components, and this workaround is not guaranteed to work.

##### Sharing roles: Ansible Galaxy
* [Ansible Galaxy](https://galaxy.ansible.com/) is a free site for finding, downloading, rating, and reviewing all kinds of community-developed Ansible roles and can be a great way to get a jumpstart on your automation projects.
* The client `ansible-galaxy` is included in Ansible. The Galaxy client allows you to download roles from Ansible Galaxy and provides an excellent default framework for creating your own roles.
* Read the [Ansible Galaxy documentation](https://galaxy.ansible.com/docs/) page for more information. A page that refers back to this one frequently is the Galaxy Roles document which explains the required metadata your role needs for use in Galaxy <[https://galaxy.ansible.com/docs/contributing/creating_role.html](https://galaxy.ansible.com/docs/contributing/creating_role.html)>.

#### Module Defaults
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_module_defaults.html)
* If you frequently call the same module with the same arguments, it can be useful to define default arguments for that particular module using the `module_defaults` keyword.
* Here is a basic example:
	```yaml
	- hosts: localhost
	  module_defaults:
	    ansible.builtin.file:
	      owner: root
	      group: root
	      mode: 0755
	  tasks:
	    - name: Create file1
	      ansible.builtin.file:
	        state: touch
	        path: /tmp/file1
	
	    - name: Create file2
	      ansible.builtin.file:
	        state: touch
	        path: /tmp/file2
	
	    - name: Create file3
	      ansible.builtin.file:
	        state: touch
	        path: /tmp/file3
	```
* The `module_defaults` keyword can be used at the play, block, and task level. Any module arguments explicitly specified in a task will override any established default for that module argument.
	```yaml
	- block:
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: "Different message"
	  module_defaults:
	    ansible.builtin.debug:
	      msg: "Default message"
	```
* You can remove any previously established defaults for a module by specifying an empty dict.
	```yaml
	- name: Create file1
	  ansible.builtin.file:
	    state: touch
	    path: /tmp/file1
	  module_defaults:
	    file: {}
	```

> [!Note]
> Any module defaults set at the play level (and block/task level when using `include_role` or `import_role`) will apply to any roles used, which may cause unexpected behavior in the role.

* Here are some more realistic use cases for this feature.
* Interacting with an API that requires auth.
	```yaml
	- hosts: localhost
	  module_defaults:
	    ansible.builtin.uri:
	      force_basic_auth: true
	      user: some_user
	      password: some_password
	  tasks:
	    - name: Interact with a web service
	      ansible.builtin.uri:
	        url: http://some.api.host/v1/whatever1
	
	    - name: Interact with a web service
	      ansible.builtin.uri:
	        url: http://some.api.host/v1/whatever2
	
	    - name: Interact with a web service
	      ansible.builtin.uri:
	        url: http://some.api.host/v1/whatever3
	```
* Setting a default AWS region for specific EC2-related modules.
	```yaml
	- hosts: localhost
	  vars:
	    my_region: us-west-2
	  module_defaults:
	    amazon.aws.ec2:
	      region: '{{ my_region }}'
	    community.aws.ec2_instance_info:
	      region: '{{ my_region }}'
	    amazon.aws.ec2_vpc_net_info:
	      region: '{{ my_region }}'
	```

* Module defaults groups
	* Ansible 2.7 adds a preview-status feature to group together modules that share common sets of parameters. This makes it easier to author playbooks making heavy use of API-based modules such as cloud modules.
	* Read further at [here](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_module_defaults.html#module-defaults-groups).

#### Interactive input: prompts
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_prompts.html)
* If you want your playbook to prompt the user for certain input, add a ‘vars_prompt’ section. Prompting the user for variables lets you avoid recording sensitive data like passwords. In addition to security, prompts support flexibility. For example, if you use one playbook across multiple software releases, you could prompt for the particular release version.
* Here is a most basic example:
	```yaml
	---
	- hosts: all
	  vars_prompt:
	
	    - name: username
	      prompt: What is your username?
	      private: false
	
	    - name: password
	      prompt: What is your password?
	
	  tasks:
	
	    - name: Print a message
	      ansible.builtin.debug:
	        msg: 'Logging in as {{ username }}'
	```
* The user input is hidden by default but it can be made visible by setting `private: no`.

> [!Note]
> Prompts for individual `vars_prompt` variables will be skipped for any variable that is already defined through the command line `--extra-vars` option, or when running from a non-interactive session (such as cron or Ansible AWX). See [Defining variables at runtime](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#passing-variables-on-the-command-line).

* If you have a variable that changes infrequently, you can provide a default value that can be overridden.
	```yaml
	vars_prompt:
	
	  - name: release_version
	    prompt: Product release version
	    default: "1.0"
	```

##### Hashing values supplied by `vars_prompt`
* You can hash the entered value so you can use it, for instance, with the user module to define a password:
	```yaml
	vars_prompt:
	
	  - name: my_password2
	    prompt: Enter password2
	    private: true
	    encrypt: sha512_crypt
	    confirm: true
	    salt_size: 7
	```
* If you have [Passlib](https://passlib.readthedocs.io/en/stable/) installed, you can use any crypt scheme the library supports:
	- _`des_crypt`_ - DES Crypt
	- _`bsdi_crypt`_ - BSDi Crypt
	- _`bigcrypt`_ - BigCrypt
	- _`crypt16`_ - Crypt16
	- _`md5_crypt`_ - MD5 Crypt
	- _`bcrypt`_ - BCrypt
	- _`sha1_crypt`_ - SHA-1 Crypt
	- _`sun_md5_crypt`_ - Sun MD5 Crypt
	- _`sha256_crypt`_ - SHA-256 Crypt
	- _`sha512_crypt`_ - SHA-512 Crypt
	- _`apr_md5_crypt`_ - Apache’s MD5-Crypt variant
	- _`phpass`_ - PHPass’ Portable Hash
	- _`pbkdf2_digest`_ - Generic PBKDF2 Hashes
	- _`cta_pbkdf2_sha1`_ - Cryptacular’s PBKDF2 hash
	- _`dlitz_pbkdf2_sha1`_ - Dwayne Litzenberger’s PBKDF2 hash
	- _`scram`_ - SCRAM Hash
	- _`bsd_nthash`_ - FreeBSD’s MCF-compatible nthash encoding
- The only parameters accepted are ‘salt’ or ‘salt_size’. You can use your own salt by defining ‘salt’, or have one generated automatically using ‘salt_size’. By default Ansible generates a salt of size 8.
- If you do not have Passlib installed, Ansible uses the [crypt](https://docs.python.org/3/library/crypt.html) library as a fallback. Ansible supports at most four crypt schemes, depending on your platform at most the following crypt schemes are supported:
	-   _`bcrypt`_ - BCrypt
	-   _`md5_crypt`_ - MD5 Crypt
	-   _`sha256_crypt`_ - SHA-256 Crypt
	-   _`sha512_crypt`_ - SHA-512 Crypt

##### Allowing special characters in `vars_prompt` values
* Some special characters, such as `{` and `%` can create templating errors. If you need to accept special characters, use the `unsafe` option:
	```yaml
	vars_prompt:
	  - name: my_password_with_weird_chars
	    prompt: Enter password
	    unsafe: true
	    private: true
	```

#### Using variables
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html)
* Ansible uses variables to manage differences between systems. With Ansible, you can execute tasks and playbooks on multiple different systems with a single command. To represent the variations among those different systems, you can create variables with standard YAML syntax, including lists and dictionaries. You can define these variables in your playbooks, in your [inventory](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html#intro-inventory), in re-usable [files](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse.html#playbooks-reuse) or [roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#playbooks-reuse-roles), or at the command line. You can also create variables during a playbook run by registering the return value or values of a task as a new variable.
* Once you understand the concepts and examples on this page, read about [Ansible facts](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html#vars-and-facts), which are variables you retrieve from remote systems.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Creating valid variable names
	* Simple variables
	* When to quote variables (a YAML gotcha)
	* Boolean variables
	* List variables
	* Dictionary variables
	* Registering variables
	* Referencing nested variables
	* Transforming variables using Jinja2 filters
	* Where to set variables
	* Variable precedence: Where should I put a variable?
	* Using advanced variable syntax

#### Discovering variables: facts and magic variables
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html)
* With Ansible you can retrieve or discover certain variables containing information about your remote systems or about Ansible itself. Variables related to remote systems are called facts. With facts, you can use the behavior or state of one system as configuration on other systems. Variables related to Ansible are called magic variables.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Ansible facts
	* Information about ansible: magic variables
* #todo Create a list of best ansible facts to remember.

### Executing playbooks
* Running complex playbooks requires some trial and error so learn about some of the abilities that Ansible gives you to ensure successful execution. You can validate your tasks with “dry run” playbooks, use the start-at-task and step mode options to efficiently troubleshoot playbooks. You can also use Ansible debugger to correct tasks during execution. Ansible also offers flexibility with asynchronous playbook execution and tags that let you run specific parts of your playbook.

#### Validating tasks: check mode and diff mode
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html)
* Ansible provides two modes of execution that validate tasks: check mode and diff mode.
* These modes can be used separately or together. They are useful when you are creating or editing a playbook or role and you want to know what it will do.
* In check mode, Ansible runs without making any changes on remote systems. Modules that support check mode report the changes they would have made. Modules that do not support check mode report nothing and do nothing.
* In diff mode, Ansible provides before-and-after comparisons. Modules that support diff mode display detailed information.
* You can combine check mode and diff mode for detailed validation of your playbook or role.

##### Using check mode
* Check mode is just a simulation. It will not generate output for tasks that use [conditionals based on registered variables](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html#conditionals-registered-vars) (results of prior tasks). However, it is great for validating configuration management playbooks that run on one node at a time. To run a playbook in check mode:
	* `ansible-playbook foo.yml --check`

###### Enforcing or preventing check mode on tasks
* If you want certain tasks to run in check mode always, or never, regardless of whether you run the playbook with or without `--check`, you can add the `check_mode` option to those tasks:
	* To force a task to run in check mode, even when the playbook is called without `--check`, set `check_mode: true`.
	* To force a task to run in normal mode and make changes to the system, even when the playbook is called with `--check`, set `check_mode: false`.
* For example:
	```yaml
	tasks:
	  - name: This task will always make changes to the system
	    ansible.builtin.command: /something/to/run --even-in-check-mode
	    check_mode: false
	
	  - name: This task will never make changes to the system
	    ansible.builtin.lineinfile:
	      line: "important config"
	      dest: /path/to/myconfig.conf
	      state: present
	    check_mode: true
	    register: changes_to_important_config
	```
* Running single tasks with `check_mode: true` can be useful for testing Ansible modules, either to test the module itself or to test the conditions under which a module would make changes. You can register variables (see [Conditionals](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_conditionals.html#playbooks-conditionals)) on these tasks for even more detail on the potential changes.

###### Skipping tasks or ignorring erros in check mode
* If you want to skip a task or ignore errors on a task when you run Ansible in check mode, you can use a boolean magic variable `ansible_check_mode`, which is set to `True` when Ansible runs in check mode. For example:
	```yaml
	tasks:
	
	  - name: This task will be skipped in check mode
	    ansible.builtin.git:
	      repo: ssh://git@github.com/mylogin/hello.git
	      dest: /home/mylogin/hello
	    when: not ansible_check_mode
	
	  - name: This task will ignore errors in check mode
	    ansible.builtin.git:
	      repo: ssh://git@github.com/mylogin/hello.git
	      dest: /home/mylogin/hello
	    ignore_errors: "{{ ansible_check_mode }}"
	```

##### Using diff mode
* The `--diff` option for ansible-playbook can be used alone or with `--check`. When you run in diff mode, any module that supports diff mode reports the changes made or, if used with `--check`, the changes that would have been made. Diff mode is most common in modules that manipulate files (for example, the template module) but other modules might also show ‘before and after’ information (for example, the user module).
* Diff mode produces a large amount of output, so it is best used when checking a single host at a time. For example:
	* `ansible-playbook foo.yml --check --diff --limit foo.example.com`

###### Enforcing or preventing diff mode on tasks
* Because the `--diff` option can reveal sensitive information, you can disable it for a task by specifying `diff: no`. For example:
	```yaml
	tasks:
	  - name: This task will not report a diff when the file changes
	    ansible.builtin.template:
	      src: secret.conf.j2
	      dest: /etc/secret.conf
	      owner: root
	      group: root
	      mode: '0600'
	    diff: false
	```

#### Understanding privilege escalation: become
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html)
* Ansible uses existing privilege escalation systems to execute tasks with root privileges or with another user’s permissions. Because this feature allows you to ‘become’ another user, different from the user that logged into the machine (remote user), we call it `become`. The `become` keyword uses existing privilege escalation tools like `sudo`, `su`, `pfexec`, `doas`, `pbrun`, `dzdo`, `ksu`, `runas`, `machinectl` and others.

> [!Warning]
> Documentation for this header was really long, so it was dismissed for summarization. If you want read it, refer to the source.

* This is a list of topics as a heads up:
	* Using become
	* Risks and limitations of become
	* Become and network automation
	* Become and windows (obviously bullshit)

#### Tags
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html)
* If you have a large playbook, it may be useful to run only specific parts of it instead of running the entire playbook. You can do this with Ansible tags.
* Using tags to execute or skip selected tasks is a two-step process:
	1. Add tags to your tasks, either individually or with tag inheritance from a block, play, role, or import.
	2. Select or skip tags when you run your playbook.

##### Adding tags with the tag keyword
* You can add tags to a single task or include. You can also add tags to multiple tasks by defining them at the level of a block, play, role, or import.
* The keyword `tags` addresses all these use cases. The `tags` keyword always defines tags and adds them to tasks; it does not select or skip tasks for execution.
* You can only select or skip tasks based on tags at the command line when you run a playbook. See [Selecting or skipping tags when you run a playbook](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#using-tags) for more details.

###### Adding tags to individual tasks
* At the simplest level, you can apply one or more tags to an individual task. You can add tags to tasks in playbooks, in task files, or within a role. Here is an example that tags two tasks with different tags:
	```yaml
	tasks:
	- name: Install the servers
	  ansible.builtin.yum:
	    name:
	    - httpd
	    - memcached
	    state: present
	  tags:
	  - packages
	  - webservers
	
	- name: Configure the service
	  ansible.builtin.template:
	    src: templates/src.j2
	    dest: /etc/foo.conf
	  tags:
	  - configuration
	```
* You can apply the same tag to more than one individual task. This example tags several tasks with the same tag, “ntp”:
	```yaml
	---
	# file: roles/common/tasks/main.yml
	
	- name: Install ntp
	  ansible.builtin.yum:
	    name: ntp
	    state: present
	  tags: ntp
	
	- name: Configure ntp
	  ansible.builtin.template:
	    src: ntp.conf.j2
	    dest: /etc/ntp.conf
	  notify:
	  - restart ntpd
	  tags: ntp
	
	- name: Enable and run ntpd
	  ansible.builtin.service:
	    name: ntpd
	    state: started
	    enabled: true
	  tags: ntp
	
	- name: Install NFS utils
	  ansible.builtin.yum:
	    name:
	    - nfs-utils
	    - nfs-util-lib
	    state: present
	  tags: filesharing
	```
* If you ran these four tasks in a playbook with `--tags ntp`, Ansible would run the three tasks tagged `ntp` and skip the one task that does not have that tag.

###### Adding tags to includes
* You can apply tags to dynamic includes in a playbook. As with tags on an individual task, tags on an `include_*` task apply only to the include itself, not to any tasks within the included file or role. If you add `mytag` to a dynamic include, then run that playbook with `--tags mytag`, Ansible runs the include itself, runs any tasks within the included file or role tagged with `mytag`, and skips any tasks within the included file or role without that tag. See [Selectively running tagged tasks in re-usable files](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#selective-reuse) for more details.
* You add tags to includes the same way you add tags to any other task:
	```yaml
	---
	# file: roles/common/tasks/main.yml
	
	- name: Dynamic re-use of database tasks
	  include_tasks: db.yml
	  tags: db
	```
* You can add a tag only to the dynamic include of a role. In this example, the `foo` tag will not apply to tasks inside the `bar` role:
	```yaml
	---
	- hosts: webservers
	  tasks:
	    - name: Include the bar role
	      include_role:
	        name: bar
	      tags:
	        - foo
	```
* With plays, blocks, the `role` keyword, and static imports, Ansible applies tag inheritance, adding the tags you define to every task inside the play, block, role, or imported file. However, tag inheritance does _not_ apply to dynamic re-use with `include_role` and `include_tasks`. With dynamic re-use (includes), the tags you define apply only to the include itself. If you need tag inheritance, use a static import. If you cannot use an import because the rest of your playbook uses includes, see [Tag inheritance for includes: blocks and the apply keyword](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#apply-keyword) for ways to work around this behavior.

###### Tag inheritance: adding tags to multiple tasks
* Adding tags to blocks
* Adding tags to plays
* Adding tags to roles
* Adding tags to imports
* Tag inheritance for includes: blocks and the `apply` keyword

##### Special tags: always and never
* Ansible reserves two tag names for special behavior: always and never.
* If you assign the `always` tag to a task or play, Ansible will always run that task or play, unless you specifically skip it (`--skip-tags always`). For example:
	```yaml
	tasks:
	- name: Print a message
	  ansible.builtin.debug:
	    msg: "Always runs"
	  tags:
	  - always
	
	- name: Print a message
	  ansible.builtin.debug:
	    msg: "runs when you use tag1"
	  tags:
	  - tag1
	```

> [!Warning]
> Fact gathering is tagged with ‘always’ by default. It is only skipped if you apply a tag to the play and then use a different tag in `--tags` or the same tag in `--skip-tags`.

> [!Warning]
> The role argument specification validation task is tagged with ‘always’ by default. This validation will be skipped if you use `--skip-tags always`.

* If you assign the `never` tag to a task or play, Ansible will skip that task or play unless you specifically request it (`--tags never`). For example:
	```yaml
	tasks:
	  - name: Run the rarely-used debug task
	    ansible.builtin.debug:
	     msg: '{{ showmevar }}'
	    tags: [ never, debug ]
	```
* The rarely-used debug task in the example above only runs when you specifically request the `debug` or `never` tags.

##### Selecting or skipping a task when you run a playbook
* Once you have added tags to your tasks, includes, blocks, plays, roles, and imports, you can selectively execute or skip tasks based on their tags when you run [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#ansible-playbook). Ansible runs or skips all tasks with tags that match the tags you pass at the command line. If you have added a tag at the block or play level, with `roles`, or with an import, that tag applies to every task within the block, play, role, or imported role or file. If you have a role with lots of tags and you want to call subsets of the role at different times, either [use it with dynamic includes](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_tags.html#selective-reuse), or split the role into multiple roles.
* [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#ansible-playbook) offers five tag-related command-line options:
	* `--tags all` - run all tasks, ignore tags (default behavior)
	* `--tags [tag1, tag2]` - run only tasks with either the tag `tag1` or the tag `tag2`
	* `--skip-tags [tag3, tag4]` - run all tasks except those with either the tag `tag3` or the tag `tag4`
	* `--tags tagged` - run only tasks with at least one tag
	* `--tags untagged` - run only tasks with no tags
* For example, to run only tasks and blocks tagged either `configuration` or `packages` in a very long playbook:
	* `ansible-playbook example.yml --tags "configuration,packages"`
* To run all tasks except those tagged `packages`:
	* `ansible-playbook example.yml --skip-tags "packages"`

###### Previewing the results of using tags
* When you run a role or playbook, you might not know or remember which tasks have which tags, or which tags exist at all. Ansible offers two command-line flags for [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#ansible-playbook) that help you manage tagged playbooks:
	* `--list-tags` - generate a list of available tags
	* `--list-tasks` - when used with `--tags tagname` or `--skip-tags tagname`, generate a preview of tagged tasks
* For example, if you do not know whether the tag for configuration tasks is `config` or `conf` in a playbook, role, or tasks file, you can display all available tags without running any tasks:
	* `ansible-playbook example.yml --list-tags`
* If you do not know which tasks have the tags `configuration` and `packages`, you can pass those tags and add `--list-tasks`. Ansible lists the tasks but does not execute any of them.
	* `ansible-playbook example.yml --tags "configuration,packages" --list-tasks`
* These command-line flags have one limitation: they cannot show tags or tasks within dynamically included files or roles. See [Comparing includes and imports: dynamic and static re-use](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse.html#dynamic-vs-static) for more information on differences between static imports and dynamic includes.

###### Selectively running tagged tasks in re-usable files
* If you have a role or a tasks file with tags defined at the task or block level, you can selectively run or skip those tagged tasks in a playbook if you use a dynamic include instead of a static import. You must use the same tag on the included tasks and on the include statement itself. For example you might create a file with some tagged and some untagged tasks:
	```yaml
	# mixed.yml
	tasks:
	- name: Run the task with no tags
	  ansible.builtin.debug:
	    msg: this task has no tags
	
	- name: Run the tagged task
	  ansible.builtin.debug:
	    msg: this task is tagged with mytag
	  tags: mytag
	
	- block:
	  - name: Run the first block task with mytag
	    ...
	  - name: Run the second block task with mytag
	    ...
	  tags:
	  - mytag
	```
* And you might include the tasks file above in a playbook:
	```yaml
	# myplaybook.yml
	- hosts: all
	  tasks:
	  - name: Run tasks from mixed.yml
	    include_tasks:
	      name: mixed.yml
	    tags: mytag
	```
* When you run the playbook with `ansible-playbook -i hosts myplaybook.yml --tags "mytag"`, Ansible skips the task with no tags, runs the tagged individual task, and runs the two tasks in the block.

###### Configuring tags globally
* If you run or skip certain tags by default, you can use the [TAGS_RUN](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#tags-run) and [TAGS_SKIP](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#tags-skip) options in Ansible configuration to set those defaults.

#### Executing playbooks for troubleshooting
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_startnstep.html)
* When you are testing new plays or debugging playbooks, you may need to run the same play multiple times. To make this more efficient, Ansible offers two alternative ways to execute a playbook: start-at-task and step mode.

##### start-at-task
* To start executing your playbook at a particular task (usually the task that failed on the previous run), use the `--start-at-task` option.
* `ansible-playbook playbook.yml --start-at-task="install packages"`
* In this example, Ansible starts executing your playbook at a task named “install packages”. This feature does not work with tasks inside dynamically re-used roles or tasks (`include_*`), see [Comparing includes and imports: dynamic and static re-use](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse.html#dynamic-vs-static).

##### Step mode
* To execute a playbook interactively, use `--step`.
	* `ansible-playbook playbook.yml --step`
* With this option, Ansible stops on each task, and asks if it should execute that task. For example, if you have a task called “configure ssh”, the playbook run will stop and ask: `Perform task: configure ssh (y/n/c):` Answer “y” to execute the task, answer “n” to skip the task, and answer “c” to exit step mode, executing all remaining tasks without asking.

#### Debugging tasks
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_debugger.html)
* Ansible offers a task debugger so you can fix errors during execution instead of editing your playbook and running it again to see if your change worked. You have access to all of the features of the debugger in the context of the task. You can check or set the value of variables, update module arguments, and re-run the task with the new variables and arguments. The debugger lets you resolve the cause of the failure and continue with playbook execution.

##### Enabling the debugger
* The debugger is not enabled by default. If you want to invoke the debugger during playbook execution, you must enable it first.
* Use one of these three methods to enable the debugger:
	* with the debugger keyword
	* in configuration or an environment variable, or
	* as a strategy

###### Enabling the debugger with the `debugger` keyword
* You can use the `debugger` keyword to enable (or disable) the debugger for a specific play, role, block, or task. This option is especially useful when developing or extending playbooks, plays, and roles. You can enable the debugger on new or updated tasks. If they fail, you can fix the errors efficiently. The `debugger` keyword accepts five values:
	* `always` : Always invoke the debugger, regardless of the outcome
	* `never` : Never invoke the debugger, regardless of the outcome
	* `on_failed` : Only invoke the debugger if a task fails
	* `on_unreachable` : Only invoke the debugger if a host is unreachable
	* `on_skipped` : Only invoke the debugger if the task is skipped
* When you use the `debugger` keyword, the value you specify overrides any global configuration to enable or disable the debugger. If you define `debugger` at multiple levels, such as in a role and in a task, Ansible honors the most granular definition. The definition at the play or role level applies to all blocks and tasks within that play or role, unless they specify a different value. The definition at the block level overrides the definition at the play or role level, and applies to all tasks within that block, unless they specify a different value. The definition at the task level always applies to the task; it overrides the definitions at the block, play, or role level.
* Examples
	* Example of setting the `debugger` keyword on a task:
		```yaml
		- name: Execute a command
		  ansible.builtin.command: "false"
		  debugger: on_failed
		```
	* Example of setting the `debugger` keyword on a play:
		```yaml
		- name: My play
		  hosts: all
		  debugger: on_skipped
		  tasks:
		    - name: Execute a command
		      ansible.builtin.command: "true"
		      when: False
		```
	* Example of setting the `debugger` keyword at multiple levels:
		```yaml
		- name: Play
		  hosts: all
		  debugger: never
		  tasks:
		    - name: Execute a command
		      ansible.builtin.command: "false"
		      debugger: on_failed
		```

###### Enabling the debugger in configuration or an environment variable
* You can enable the task debugger globally with a setting in ansible.cfg or with an environment variable. The only options are `True` or `False`. If you set the configuration option or environment variable to `True`, Ansible runs the debugger on failed tasks by default.
* To enable the task debugger from ansible.cfg, add this setting to the defaults section:
```ini
[defaults]
enable_task_debugger = True
```
* To enable the task debugger with an environment variable, pass the variable when you run your playbook:
	* `ANSIBLE_ENABLE_TASK_DEBUGGER=True ansible-playbook -i hosts site.yml`
* When you enable the debugger globally, every failed task invokes the debugger, unless the role, play, block, or task explicitly disables the debugger. If you need more granular control over what conditions trigger the debugger, use the `debugger` keyword.

###### Enabling the debugger as a strategy
* If you are running legacy playbooks or roles, you may see the debugger enabled as a [strategy](https://docs.ansible.com/ansible/latest/plugins/strategy.html#strategy-plugins). You can do this at the play level, in ansible.cfg, or with the environment variable `ANSIBLE_STRATEGY=debug`. For example:
	```yaml
	- hosts: test
	  strategy: debug
	  tasks:
	  ...
	```
* Or in ansible.cfg:
```ini
[defaults]
strategy = debug
```

> [!Note]
> This backwards-compatible method, which matches Ansible versions before 2.5, may be removed in a future release.

##### Resolving errors in the debugger
* After Ansible invokes the debugger, you can use the seven [debugger commands](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_debugger.html#available-commands) to resolve the error that Ansible encountered. Consider this example playbook, which defines the `var1` variable but uses the undefined `wrong_var` variable in a task by mistake.
```yaml
- hosts: test
  debugger: on_failed
  gather_facts: false
  vars:
    var1: value1
  tasks:
    - name: Use a wrong variable
      ansible.builtin.ping: data={{ wrong_var }}
```
* If you run this playbook, Ansible invokes the debugger when the task fails. From the debug prompt, you can change the module arguments or the variables and run the task again.
* **Please refer to the source for the example in this section.**
* Changing the task arguments in the debugger to use `var1` instead of `wrong_var` makes the task run successfully.

##### Available debug commands
* You can use these seven commands at the debug prompt:

| Command | Shortcut | Action |
| :- | :-: | :- |
| print | p | print information about the task |
| task.args\[key\] = value | no shortcut | update module arguments |
| task_vars\[key\] = value | no shortcut | update task variables (you must `update_task` next) |
| update_task | u | recreate a task with updated task variables |
| redo | r | run the task again |
| continue | c | continue executing, starting with the next task |
| quit | q | quit the debugger |

* For more details, see the individual descriptions and examples ~~below~~ in the source.

##### How the debugger interacts with the free strategy
* With the default `linear` strategy enabled, Ansible halts execution while the debugger is active, and runs the debugged task immediately after you enter the `redo` command. With the `free` strategy enabled, however, Ansible does not wait for all hosts, and may queue later tasks on one host before a task fails on another host. With the `free` strategy, Ansible does not queue or execute any tasks while the debugger is active. However, all queued tasks remain in the queue and run as soon as you exit the debugger. If you use `redo` to reschedule a task from the debugger, other queued tasks may execute before your rescheduled task. For more information about strategies, see [Controlling playbook execution: strategies and more](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_strategies.html#playbooks-strategies).

#### Asynchronous actions and polling
> [source](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_async.html)
* By default Ansible runs tasks synchronously, holding the connection to the remote node open until the action is completed. This means within a playbook, each task blocks the next task by default, meaning subsequent tasks will not run until the current task completes. This behavior can create challenges. For example, a task may take longer to complete than the SSH session allows for, causing a timeout. Or you may want a long-running process to execute in the background while you perform other tasks concurrently. Asynchronous mode lets you control how long-running tasks execute.

##### Asynchronous ad hoc tasks
* You can execute long-running operations in the background with [ad hoc tasks](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html#intro-adhoc). 
* For example, to execute `long_running_operation` asynchronously in the background, with a timeout (`-B`) of 3600 seconds, and without polling (`-P`):
	* `$ ansible all -B 3600 -P 0 -a "/usr/bin/long_running_operation --do-stuff"`
* To check on the job status later, use the `async_status` module, passing it the job ID that was returned when you ran the original job in the background:
	* `$ ansible web1.example.com -m async_status -a "jid=488359678239.2844"`
* Ansible can also check on the status of your long-running job automatically with polling. In most cases, Ansible will keep the connection to your remote node open between polls. To run for 30 minutes and poll for status every 60 seconds:
	* `$ ansible all -B 1800 -P 60 -a "/usr/bin/long_running_operation --do-stuff"`
* Poll mode is smart so all jobs will be started before polling begins on any machine. Be sure to use a high enough `--forks` value if you want to get all of your jobs started very quickly. After the time limit (in seconds) runs out (`-B`), the process on the remote nodes will be terminated.
* Asynchronous mode is best suited to long-running shell commands or software upgrades. Running the copy module asynchronously, for example, does not do a background file transfer.