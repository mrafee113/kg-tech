#### Commands
- `renice` - (1) alter priority of running processes
- `service` - (8) run a System V init script
- `systemctl` - (1) Control the systemd system and service manager
- `jobs`
- `bg`
- `fg`
- `kill`
  - (1) send a signal to a process
  - (2) send signal to a process
- `kilall` - (1) kill processes by name
- `top` - (1) display Linux processes
- `setpriv` - (1) run a program with different Linux privilege settings
- `runuser` - (1) run a command with substitute user and group ID
- `sudo` - (8) execute a command as another user
- `su` - (1) run a command with substitute user and group ID
- `htop` - (1) interactive process viewer
- `nohup` - (1) run a command immune to hangups, with output to a non-tty
- `xargs` - (1) build and execute command lines from standard input

### Daemons/Services
A common feature in unix-like operating systems is the employment of seperate processes to control distinct functions of the system. They are also responsible for extended features underlying the os, like HTTP, FTP, databases, on-demand configuration.
 * Which daemons should be active depends on the purpose of the system.
* The program responsible for managing runlevels and associated daemons/resources is `/sbin/init`.

An implementation of some sort of **service management utility** exists in every major linux distro, to tackle the issue of controling daemons/services without the need to reboot the whole system.
* SysVinit aka System V aka SysV
	services are controlled by shell scripts
* systemd, upstart
	services controlled by a program and its configs
* First program run after the kernel -> `always` PID = 1

#### Systemd/Systemctl
* unit
	A unit consists of a `name`, a `type` and a `corresponding configuration file`.
	Main command to control systemd manager is `systemctl`.
	* *types of unit*
		- service
		- socket
			The socket unit type can be a filesystem socket or a network socket. All socket units have a corresponding service unit, loaded when the socket receives a request.
		- device
			   A device unit is associated with a hardware device identified by the kernel. A device will only be taken as a systemd unit if a udev rule for this purpose exists.
		- mount
			   A mount unit is a mount point definition in the filesystem, similar to an entry in /etc/fstab.
		- automount
			   Every automount unit has a corresponding mount unit, which is initiated when the automount mount point is accessed.
		- target
				grouping of other units managed as one
		- snapshot
				saved state of systemd manager
* systemctl commands
	for a hypothetical `unit.service`
	- start
	- stop
	- restart
	- is-active
	- enable
		will load during system init
	- disable
	- is-enabled
	- systemctl isolate `[target].target` -> very dangerous
	- systemctl set-default `[target].target` -> very dangerous
	- systemctl get-default
	- systemctl list-unit-files \[--type=\[service/target\]\]
	- systemctl list-units \[--type=\[service/target\]\]

			- *in the absence of `acpid`*
			- systemctl suspend -> low power mode
			- systemctl hibernate

#### Checking Services for unnecessary Daemons
* `sudo service --status-all` on SysVinit based systems
* `sudo update-rc.d [service] remove` disables a service
* `sudo chkconfig [service] off` disables a service on redhat-based distros
* `systemctl list-units --status active --type service` on systemd based systems
* `sudo systemctl disable [unit/service] --now` disables a service on systemd based systems
* `netstat -ltu` to get a survey of listening network services (on older systems)
* `ss -ltu` (socket services) to get a survey of listening network services (on modern systems)


### Runlevels
* 0
	system shutdown
* 1, s, or single
	Single user mode, without network and other non-essential capabilities (maintenance mode).
* 2, 3, or 4
	Multi-user mode. Users can log in by console or network. Runlevels 2 and 4 are not often used.
* 5
	Multi-user mode. It is equivalent to 3, plus the graphical mode login.
* 6
	System restart.

### Jobs
Jobs are processes that have been started interactively through a terminal, sent to the background and have not yet finished execution.
* `jobs` command will show active jobs and their status
	* `sleep 60` and then `^Z` will produce a job and running `jobs` will produce
		*  `[1]+ Stopped      sleep 60` -> execution has been suspended
			* `[1]` is the job ID (**JID**)
			* `+` indicates the current, default job (that is, the last one being suspended or sent to the background). The previous job is flagged with a minus sign `-`. Any other prior jobs are not flagged.
			* `Stopped` is a description of the job status
			* `sleep 60` the command or job itself
	* options
		* `-l` will produce a process ID (**PID**) right before job description
		* `-n` lists processes that have changed status since the last notification
			* possible status: `Running, Stopped, Terminated, Done`
		* `-p` lists only process IDs
		* `-r` lists only running jobs
		* `-s` lists only suspended jobs
* `jobspec`
	The `job` command as well as `fg`, `bg` and `kill` need a job specification.
	* `%n` filter on JID
	* `%str` filter on command starting with `str`
	* `%?str` filter on command containing `str`
	* `%%` or `%+` return current job
	* `%-` return previous job
* if job is in background or suspended
	* note that when you `^z` (ctrl+z) on a running process it will be suspended.
	* `fg %[]` will bring it to foreground
	* `bg %[]` will put a suspended job in background
		* after that the command in `jobs` will have an `&` added to the end of it, indicating it's been sent to background.
		* also the status will be changed to `Running` and, well, it runs.
	* adding `&` to the end of a command will start it in the background
	* `kill %[]` will terminate a job by sending `SIGTERM` signal
* detach job from current session
	* `nohup [command] &`
		* this will redirect `stdout` and `stderr` to `./nohup.out`
		* `nohup [command] > /other/file &` will customize it
	* `kill [PID]`

### Process Monitoring
* A process or task is an instance of a running program. Thus, you create new processes every time you type in commands into the terminal.
* `watch [command]` will execute a program periodically (default=2s) and allows us to watch the output over time.
	* `watch uptime`
		* you can check system's uptime and **load average** with this
	* it also outputs `[period]: [command] [hostname] [datetime]` on the first line
	* it will run until interrupted by `^C`
	* `watch free` will show memory usage as processes are created and killed
	* `[-n/--interval] [seconds]` will set the watch period
* `pgrep [process name]` locates PID
* `pkill [process name]` kills processes
* `killall [process name]` kills all instances of a process
	* although it does have other functionalities too
	* signal specification (also works for `kill`)
		* `-[signal name in uppercase]`
		* `-[signal number]`
		* `-s [signal name in uppercase]`
	* `kill -l` will give an exhaustive list of signals along with their codes
* `top` #todo htop
* `ps` #todo
	* `ps a` shows processes witha a terminal
	* `ps -p [PID]` shows detail on a process
	* `ps -u [username]` shows processes of a user
	* `ps aux`
		* `a` shows process that are attached to a tty or terminal
		* `u` display user-oriented format
		* `x` show processes that are not attached to a tty or terminal

### Process Priority
* systems-calls are in charge of all inter-device communication
* Linux, as a preemptive multi-processing operating system, implements a scheduler that organizes the process queue. The scheduler also decides which queued `thread` will be executed. `thread` and `process` are interchangeable terms here.
* every process has two things that intervene in it having control of cpu
	* the scheduling priority
	* the scheduling policy
		* real-time policies
			* processes are scheduled by priority value directly
			* any real-time process has a higher priority than a normal process
		* normal policies
			* processes usually have the same scheduling priority
			* they have another process predicate called `nice value`
		* static priorities
			* 0-99 for real-time and 100-139 for normal processes
			* lower means higher priority 
		* priority can be found by `grep ^prio /proc/[PID]/sched`
			* or by `ps -Al` or `ps -el`
				* `ps` priority values (`PRI`) range from 40-99 so you should sum it with another 40
			* or by `top`
				* normal priorities range from 0 to 39
				* because it subtracts real priorities by 100
		* process niceness
			* every process starts with a niceness of `0` or priority of `120`
			* the name `nice` comes from the idea that "nicer" processes allow other processes to run before them in a particular execution queue
			* value ranges from `-20` (less nice, high priority), to `19` (more nice, low priority)
			* only `root` can decrease niceness below zero
			* `nice -n [niceness=10] [command]` starts a process with a non-standard nice value
			* `renice -[niceness] -p [PID]` changes the niceness of a running process
				* `-g` and `-u` are used to modify all the processes of a group or user respectively

> [!Question] ChatGPT
> **Thoroughly explain Linux process priority, niceness, and priority-policy in the context of process scheduling.**
> 
> In the context of process scheduling in Linux, process priority, niceness, and priority policy are concepts that determine how the operating system allocates CPU time to different processes. These concepts play a significant role in determining the order in which processes are executed and how system resources are distributed among them. Let's explore each of these concepts in detail:
>
> 1. **Process Priority:** Process priority is a numerical value assigned to a process that reflects its importance in terms of CPU scheduling. Priorities are typically represented as integers, where lower values indicate higher priority. The process scheduler uses these priorities to determine the order in which processes are allocated CPU time. Processes with higher priority values are given preference in CPU scheduling over processes with lower priority values.
> 
> 2. **Niceness:** Niceness is a concept that provides a more user-friendly way to adjust process priorities. It's represented as a value between -20 and +19, where lower values indicate higher priority (more "nice") and higher values indicate lower priority (less "nice"). The niceness value is essentially an offset from the default priority, which is usually 0.
>
 >    - Positive Niceness (Higher Values): Processes with higher niceness values are considered to be less urgent or less important. They are "nicer" to other processes, allowing them to have more CPU time. These processes are assigned lower priorities.
>    
 >   - Negative Niceness (Lower Values): Processes with negative niceness values are more urgent or important. They are given higher priority and compete for CPU time more aggressively.
>     
> 3. **Priority Policy:** Priority policy refers to the strategy used by the Linux scheduler to allocate CPU time to processes. The most common priority policies are:
> 
>    - **Round Robin (SCHED_RR):** In this policy, each process is given a fixed time slice to execute. Processes with the same priority are scheduled in a round-robin fashion. Real-time processes often use this policy.
>     
>    - **First-Come, First-Served (SCHED_FIFO):** Processes with the same priority are scheduled based on their arrival time. Once a process starts executing, it continues until it voluntarily yields or is preempted by a higher-priority process.
>      
>    - **Completely Fair Scheduler (CFS):** This is the default scheduler in modern Linux systems. It aims to provide "fair" allocation of CPU time to processes based on their priorities and resource needs. It uses virtual runtimes to estimate how long each process has been running.
>      
>    - **Batch (SCHED_BATCH):** This policy is designed for batch processing tasks that can tolerate slightly lower priority and longer response times.
>      
>    - **Idle (SCHED_IDLE):** This policy is used for processes that run only when the CPU has no other tasks to perform.
>      
>
> In summary, process priority, niceness, and priority policy are integral components of process scheduling in Linux. They allow administrators and users to influence the order in which processes receive CPU time, based on the urgency and importance of each process. These concepts help strike a balance between fairness, responsiveness, and resource utilization in a multi-tasking environment.

> [!Question] ChatGPT
> **What are real-time and normal priority policies?**
>
> In the context of process scheduling in Linux, real-time and normal priority policies refer to two distinct approaches for managing the execution of processes based on their priority levels. These policies determine how the operating system allocates CPU time to processes with different priority values. Let's explore both real-time and normal priority policies:
>
> 1. **Real-Time Priority Policy:** The real-time priority policy is designed to cater to processes that have stringent timing requirements. Real-time processes need to meet specific deadlines and have predictable response times. Linux provides two types of real-time scheduling policies: SCHED_FIFO and SCHED_RR.
>    
>    - **SCHED_FIFO (First-Come, First-Served):** Processes scheduled with SCHED_FIFO operate in a strict priority-based manner. A process with a higher priority level preempts processes with lower priorities. The process continues to execute until it yields the CPU or is preempted by a higher-priority process. This policy is suitable for applications where maintaining precise timing is critical, such as industrial control systems.
>        
>    - **SCHED_RR (Round Robin):** Similar to SCHED_FIFO, SCHED_RR assigns strict priorities to processes. However, processes of the same priority are scheduled in a round-robin fashion, allowing each process to run for a fixed time slice before switching to the next process of the same priority.
>        
> 2. **Normal Priority Policy:** The normal priority policy, also known as the Completely Fair Scheduler (CFS), is the default scheduler in modern Linux systems. It aims to provide fairness and efficient resource allocation among processes while considering their priority levels. The CFS scheduler uses a concept called "virtual runtime" to approximate how long each process has been running relative to its priority.
>    
>    - Processes with higher priority values (lower niceness values) receive more CPU time compared to processes with lower priority values. However, even lower-priority processes receive some CPU time, ensuring that no process is starved of resources.
>        
>    - The CFS scheduler divides the available CPU time among active processes using a fair sharing algorithm. This approach provides more balanced resource allocation and responsiveness in typical multitasking scenarios.
>        
>
> In summary, real-time priority policies (SCHED_FIFO and SCHED_RR) are designed for time-critical applications where predictable response times are crucial. Normal priority policies, such as the Completely Fair Scheduler (CFS), aim to provide balanced resource allocation and responsiveness in a multitasking environment without favoring any specific process too heavily. The choice between these policies depends on the nature of the application and its timing requirements.

> [!Question] ChatGPT
> **Is the nice value a value that Linux subtracts from the priority value and then determines scheduling based on the result of the subtraction? If not, how else does Linux interact with these two values?**
>
> Yes, you're correct! The nice value in Linux is used as an offset that is subtracted from the default priority value of a process. This subtraction determines the actual priority that the process is assigned for scheduling purposes. The lower the nice value, the higher the resulting priority of the process. Conversely, higher nice values result in lower priorities.
>
> Here's how the interaction between the nice value and priority works:
>
> 1. **Calculating Priority:**
>    
>    - The default priority for a process is usually set at a mid-range value, often around 120.
>    - The nice value ranges from -20 (highest priority) to +19 (lowest priority). Negative nice values represent higher priority levels, while positive nice values represent lower priority levels.
> 2. **Calculating Final Priority:**
>    
>    - The actual priority that the scheduler uses to determine which process to run next is calculated by adding the nice value to the default priority. The resulting value is used for scheduling decisions.
>    - For processes with lower nice values (higher priority), the subtraction reduces the calculated priority.
>    - For processes with higher nice values (lower priority), the addition increases the calculated priority.
>
> In summary, the nice value acts as an offset that adjusts the priority of a process for scheduling purposes. The scheduler determines the execution order of processes based on their calculated priorities. This approach allows administrators and users to influence the scheduling behavior of processes without directly manipulating the underlying priority values, making it more intuitive and user-friendly to adjust process priorities.
### Job Scheduling
#### Cron/Systemd Timers
* `cron` is a **daemon** that runs continuously and wakes up every minute to check a set of tables to find tasks to execute. These tables are called `crontabs` and contain the so-called `cron jobs`. 
* alternative for desktops/laptops is `anacron`. When the machine is off at the scheduled time, it will run the next time the machine starts running.
* user crontabs are always named after the user that created them. location is distro-based but it's generally a *subdirectory* or `/var/spool/cron`
* crontab syntax per line
	space seperated fields
	1. the minute of the hour `0-59`
	2. the hour of the day `0-23`
	3. the day of the month `1-31`
	4. the month of the year `1-12` | or first 3 letters
	5. the day of the week `0-7` with `sunday=0=7` | or first 3 letters
	6. the command to run
	* values for first 5 fields
		* `*` asterisk -> any value
		* `,` comma -> list of possible values
		* `-` dash -> range of possible values
		* `/` slash -> stepped values
	* for example
		* `0 9 * * 5 RCLCRON_RCLINDEX= RECOLL_CONFDIR="/home/mehdi/.recoll" recollindex` runs recoll indexing everyday at 9am
	* `/etc/crontab` can be referred to for the layout of the crontab
* system crontabs can only be edited by root. `/etc/crontab` and `/etc/cron.d/*` are all sys crontabs.
* #todo learn how to create custom `/etc/cron.d/hourly`-based crontabs
* system crontab syntax
	* like that of the user except:
	* 5. day of the week
	* 6. the name of the user account to be used when executing the command
	* 7. the command to run
* **particular**(*alternative*) time specifications
	* instead of the first five fields you can use:
	* `@reboot` run once after reboot
	* `@hourly` run once an hour at the beginning of the hour
	* `@daily or @midnight` run once a day at midnight
	* `@weekly` run once a week at midnight on sunday
	* `@monthly` run once a month at midnight on the first day of the month
	* `@yearly or @annually` run once a year at midnight on the 1st of jan
* crontab **variables**
	Within a crontab file, there are sometimes variable assignments defined before the scheduled tasks are declared. Common ones:
	* `HOME` the dir where cron invokes the command
	* `MAILTO` the name of the user or the address to which the standard output and error is mailed (by default the crontab owner). Multiple comma-separated values are also allowed and an empty value indicates that no mail should be sent.
	* `PATH` the path where commands can be found
	* `SHELL` the shell to use (default `/bin/sh`)
* Creating user crontabs
	* using command `crontab`
	* `crontab -e` to edit your own or create and edit if it doesn't exist
	* `select-editor` selects default editor : not just for crontab
	* the permissions on the crontab **file** only allow users to edit them the crontab command, or with root priviledges.
	* `-l` display the current crontab on standard output
	* `-r` remove the current crontab
	* `-u` specify the user to edit crontab, only for root
* Output
	* redirect to file
		* `30 01 * * * root /root/barfoo.sh >>/root/output.log 2>>/root/error.log`
		* output is appended to `barfoo.sh`, and errors are appended to `error.log`
	* *Unless output is redirected to a file as the example above*, *or the `MAILTO` variable is set to a blank value*, **all output from the cronjob will be sent to the user via e-mail.**
* access configs to job scheduling
	* if `/etc/cron.allow` exists, only non-root users within it can edit crontabs.
	* reverse of allow, if `/etc/cron.deny` exists, only non-root users can not be allowed to edit crontabs.

* alternative to cron: **systemd timers**
	* they are systemd unit
	* should have the same name as service + `.timer`
	* each should correspond to a systemd unit
	* for further info refer to page 206: LPIC101: 107.2: Lesson 1: An alternative to cron #todo 

#### The `at` Command
* run a job in the future only once
* after `at [time specification]`, you will enter the at prompt. there, you can define the commands to be executed. you can exit it using `Ctrl+d`
* the output will be sent via email
* in order to use it, it requires the `atd` daemon to be running.
* an alternative is `batch`. but for batch jobs to be run the system load should be low enough to allow it.
* options
	* `-c` print the commands of a specific job ID
	* `-d` delete jobs based on JID. alias for `atrm`
	* `-f` read the job from file instead of stdin
	* `-l` list pending jobs of user. if root, list all pending jobs. alias for `atq`
		* JID, execution date, execution time, queue, username
	* `-m` send mail to user at the end of the job even if there was no output
	* `-q` specify a queue in the form of a single letter from a to z and from A to Z (by default a for at and b for batch). Jobs in the queues with the highest letters are executed with increased niceness. Jobs submitted to a queue with a capital letter are treated as batch jobs.
	* `-v` show the time at which the job will run before reading the job
* config access with `/etc/at.allow` and `/etc/at.deny`
* datetime specification
	* time: `HH:MM [AM/PM]?`
	* date
		* `[month name] [day of month]`
		* `[month name] [day of month] [year]`
		* `MMDDYY`
		* `MM/DD/YY`
		* `DD.MM.YY`
		* `YYYY-MM-DD`
	* keywords
		* `midnight`
		* `noon`
		* `teatime` (4pm)
		* `now +[n] [minutes/hours/days/weeks]`
	* `/usr/share/doc/at/timespec`
* another alternative: `systemd-run`
