### Users and Groups
* `/etc/login.defs`
	* this file specifies the configuration parameters that control the creation of users and groups. In addition, the commands shown in the previous sections take default values from this file.
	* `UID_MAX, UID_MIN` the range of user ids
	* `GID_MAX, GID_MIN`
	* `CREATE_HOME` boolean: create home or not by default
	* `USERGROUPS_ENAB` specify whether the system should by default create a new group for each new user account with the same name as the user, and whether deleting the user account should also remove the user’s primary group if it no longer contains members.
	* `MAIL_DIR`
	* `PASS_MAX_DAYS` the maximum number of days a password may be used.
	* `PASS_MIN_DAYS` the minimum number of days allowed between password changes.
	* `PASS_MIN_LEN`
	* `PASS_WARN_AGE` the number of warning days before a password expires.
* group passwords
	Groups can also have a password, which can be set using the `gpasswd` command. Users, who are not members of a group but know its password, can join it temporarily using the `newgrp` command. Remember that `gpasswd` is also used to add and remove users from a group and to set the list of administrators and ordinary members of the group.
* `/etc/passwd` basic info on user in 7 fields
	* `username`
	* `password`: if shadow passwds are used -> `x`
	* `UID`
	* `GID`
	* `GECOS` an optional comment field, which is used to add extra information about the user (such as the full name). The field can contain multiple comma-separated entries.
	* `Home Directory`
	* `Shell`
* `/etc/group` basic info on group in 4 fields
	* `groupname`
	* `password`: if shadow passwds are used -> `x`
	* `GID`
	* `Member List` excluding the users that this is their primary group
* `/etc/shadow` encrypted user passwds in 9 fields
	* `username`
	* `encrypted password`
	* `date of last password change`
	* `minimum password age`
	* `maximum password age`
	* `password warning period`
	* `password inactivity period`
	* `account expiration date`
	* `a reserved field` a field reserved for future use
* `/etc/gshadow` encrypted group passwds in 4 fields
	* `groupname`
	* `encrypted password`
	* `group administrators` who can change passwords and add/remove members
	* `group members`
* shadow passwords ^shadow-passwords
	* To prevent all users except the root user from logging into the system temporarily, the superuser may create a file named `/etc/nologin`. `man 5 nologin`
	* Note there is also a command nologin which can be used to prevent a login when set as the default shell for a user. For example
		* `sudo usermod -s /sbin/nologin emma`
		* `man 8 nologin`

> [!Question] ChatGPT
> Explain the difference between a user's primary group and supplementary groups in linux
> 
> In Linux, both primary groups and supplementary groups are mechanisms used to manage permissions and access control for users. They determine which resources a user can access and what actions they can perform on those resources. However, they serve slightly different purposes within the context of user management:
> 
> 1. **Primary Group:**
>    
>    - Every user in Linux is associated with a primary group. This primary group is set when the user account is created and is stored in the system's user database (such as `/etc/passwd`).
>    - The primary group is typically used for managing file ownership. When a user creates a new file or directory, it is assigned the user's primary group as the group owner by default.
>    - The primary group also determines the group ownership of files and directories shared within the user's home directory or other locations where the user has write access.
>    - When a user logs in, the user's primary group becomes their effective group for permission checks, unless they explicitly switch their effective group using the `newgrp` command.
> 2. **Supplementary Groups:**
>    
>    - In addition to the primary group, users can be assigned to multiple supplementary groups. These are groups that a user belongs to apart from their primary group.
>    - Supplementary groups are used to extend a user's permissions beyond their primary group. By being a member of one or more supplementary groups, a user gains the ability to access files and directories owned by those groups, provided that the relevant permissions are granted.
>    - Supplementary groups are useful for scenarios where users need access to shared resources that are not directly related to their primary group.
>    - When a user logs in, their supplementary groups are set based on the user's group memberships as specified in the system's group database (such as `/etc/group`).
### Keeping Users Informed
* A linux system offers the following additional utilities and files to help with communication:
	* `/etc/issue`
	* `/etc/issue.net`
	* `/etc/motd`
	* `/sbin/shutdown`
	* `/bin/usr/notify-send` `(/usr/bin/notify-send)`
	* `/bin/wall` `(/usr/bin/wall)`
* Fluid Messaging
	* Fluid messaging involves informing active system users of current events, such as a system shutdown, as they are happening. These methods are intended to be used either for emergency purposes or as supplemental communication for a planned situation.
	* The `wall` command
		* The `/usr/bin/wall` command sends simple messages to certain system users.
		* Only users who meet the following conditions will receive these messages:
			* Users who are currently logged into a terminal (tty#) or a terminal emulator (pts/#)
			* Users who have their message status set to “yes”
		* The `/bin/mesg`  command allows you to view and set your message status.
			* `mesg` -> shows status on/off (y/n)
			* `mesg y` -> turn on messaging
			* `mesg n` -> turn off messaging
			* What’s happening behind the scenes with mesg is that you are granting (y) or revoking (n) write access to your terminal device. If write access is granted, other users can use programs such as /bin/write or /usr/bin/ write to send messages to the terminal.
		* The general `write` command syntax: `write [username] [terminal_id]`
		* `who -T` -> shows terminal ids
			* This command shows the current write access status of each logged-in user. A plus sign (+) between the username and terminal id indicates that write access is granted, while a minus sign (-) indicates that no write access has been granted. A question mark (?) indicates a user who is logged into the GUI. For a GUI user to receive a write command message, a GUI terminal emulator must be opened, designated by a pts/# terminal type, and write access must be granted. The pts/0 terminal id in Figure 2.1 indicates that the user, rich, has a terminal emulator application running in his GUI. However, the terminal must still have write access granted (+) in order to receive write command messages, which it does.
		* You can use the `/bin/wall` utility to broadcast a message to all terminals with write access granted. Thus, it can be a handy utility to use for standard communication. -> `wall message`
		* By default, the `systemctl` utility will send a wall message when any of its following commands are issued: `emergency`, `halt`, `kexec`, `power-off`, `reboot`, or `rescue`. To prevent a wall message from being sent while using systemctl, include the `--no-wall` option in its command line.
		* The wall message is disruptive in that it will display in the middle of whatever the user is currently doing in the terminal. However, the user receiving the message can simply press Enter to receive the $ prompt back.
	* Using the `notify-send` command
		* The wall command is useful, but if a user is not logged into a console terminal or does not have a GUI terminal emulator open, you cannot send messages to that user.
		* The notify-send command may not be installed by default. If it is not and you wish to install it, you can find the notify-send utility in the `libnotify-bin` package.
		* `notify-send "[title]" "[message]"`
		* Be aware that users can turn off these notification messages via simple desktop environment settings. That can be problematic if you are solely dependent on the notify-send command for GUI user communication purposes.
		* To send notify-send messages to GUI users besides yourself, you need super user privileges. Additionally, you need certain environment variables, depending upon how you are implementing the notify-send utility and which distribution you are using.
		* The `DISPLAY` environment variable in Figure 2.6 (LPIC2 Study Guide) is set to the `w` command’s tty column value for the user kevin. This is necessary for the `notify-send` utility to know where to send its output. Notice that the `sudo` command is also used. It is needed so that the `su -c` command can be employed to issue the `notify-send` command as the user logged into the GUI; in this case, that’s kevin. The backslashes (\\) in front of the quotation marks (") surrounding both the `notify-send` command’s message title and message are also necessary. Because the command, sent as an option with `su -c`, must be surrounded by its own quotation marks, the backslashes allow the `notify-send` options to have their necessary double quotation marks (") and not interfere with the `su -c` command’s operation. The very last parameter in Figure 2.6’s long command is the username kevin. This is an option to the `su -c` command, so that the user kevin will execute the `notify-send` command.
		* On other distributions, such as *CentOS*, when sending messages to other GUI users, even more environment variables are needed. In Figure 2.8 (LPIC2 Study Guide), notice that prior to using the `notify-send` command, the `DBUS_SESSION_BUS_ADDRESS` environment variable must be set to the GUI user’s current setting for that variable and then exported. This environment variable is often needed when you create a cron job to automate such communication.
	* Using the `/sbin/shutdown` command
		* This command allows you to halt, reboot, or power down your system as well as to communicate with your system users while doing so.
		* `sudo shutdown [options] [time] [wall message]`
		* Common options include `-H` to halt, `-P` to poweroff, and `-r` to reboot the system, as well as several other useful selections. Once you’ve started a shutdown process, you can typically cancel it by using the `shutdown -c` command.
		* For time formatting see the manpage.
		* The `[wall message]` parameter lets you modify the shutdown command message sent to any logged-in users. This parameter operates in a similar manner as the wall command, with one major difference: it ignores the mesg setting on a terminal. Therefore, the message can be written on any terminal whether write access is granted or not.
* Static Messaging
	* Static messaging involves communicating with system users using files that are changed only when the message needs to change.
	* The system users see these messages when they log into the system. Thus this static messaging form is specifically called *logon messaging*.
	* These techniques are intended to be used as primary communication methods for planned situations.
	* There are several Linux files that can help employ this automated communication style:
		* `/etc/issue`
			* This file allows text to be displayed on the tty terminal login screens.
			* It typically holds a company’s system access policy, and it rarely changes. It may also contain planned upcoming system outages.
			* When unmodified, this file usually simply holds system information, such as what Linux kernel version is running.
		* `/etc/issue.net`
			* This file is very similar to the `/etc/issue` file.
			* Its primary purpose is to display logon messages for remote logins.
			* By default, it is typically enabled only for Telnet connections.
		* `/etc/motd`
			* The `/etc/motd` file *(Message of the Day file)* provides an additional logon communication method only for tty terminal users.
			* The file contents are displayed after the user has logged into the system but before a command-line prompt is displayed.
			* Traditionally, the file contained more light-hearted messages, such as upcoming company events or sayings. It now typically contains upcoming system event information, often because the `/etc/issue` and `/etc/issue.net` files are needed for displaying legal logon messages.
			* `man motd`

### Commands
- `sudo useradd [name]`
	- (8) create a new user or update default new user information
	* group file changed
	* password should be set with `passwd`
	* user home can be added with extra options
	* a group with `[name]` is created too
	* options
		* `-c` it's comment used as user's full name
		* `-d` custom home dir
		* `-e` set specific date on which account will be disabled
		* `-f` number of days after which the password expires and account will be disabled, and during which the user should update the password
		* `-u` specific UID
		* `-g` specific GID
		* `-G` adding it to multiple secondary groups
		* `-m` create home dir
		* `-M` create user without home dir
		* `-k` copy skeleton files to home (if `-m`) from custom dir
		* `-s` specific login shell which defaults to `/etc/default/useradd:SHELL` which defaults to `/bin/sh`
- `id [username]` -> UID, GID, list of groups
	- (1) print real and effective user and group IDs
- `sudo usermod [options] [username]`
	- (8) modify a user account
	* options are like that of `useradd`
	* `-d` migrates home dir
	* `-G` alone deletes previous secondary groups and adds new ones
		* but with `-a` it only adds them
	* `-l` change login name
	* `-L` lock the specified user. funnily, this puts an exclamation mark in front of the encrypted password within the `/etc/shadow` file, thus disabling access with a password for that user.
	* `-U` unlock user account 
	* Remember that when you change the login name of a user account, you should probably rename the home directory of that user and other user-related items such as mail spool files. Also remember that when you change the UID of a user account, you should probably fix the ownership of files and directories outside the user’s home directory (the user ID is changed automatically for the user’s mailbox and for all files owned by the user and located in the user’s home directory).
- `sudo userdel [username]`
	* `-r` also removes home dir
- `sudo groupadd [groupname]`
	- (8) create a new group
	- `-g` specific GID
* `sudo groupmod [options] [groupname]`
* `sudo groupdel [groupname]`
- `sudo passwd [username]` ^passwd
	- (1) change user password
	- (5) the password file
	* only root can change everyone's passwords. anyone can change their own passwords. because passwd has the SUID bit set.
	* `-d` delete password -> thus disabling it
	* `-e` force user to change password
	* `-i` set the number of days of inactivity after a password expires during which the user should update the password (otherwise the account will be disabled).
	* `-l` **GENIUS**: Lock the user account (the encrypted password is prefixed with an exclamation mark in the /etc/shadow file).
	* `-u` unlock account
	* `-n` set the minimum password lifetime.
	* `-S` output password status
		1. user's login name
		2. `[P/L/NP]` P indicates user has a password, L is for a locked password, NP is for no password
		3. `[date]` date of the last password change
		4. `[integer]` minimum age in days (the minimum number of days between password changes). a value of 0 means the password may be changed at any time.
		5. `[integer]` maximum age in days (for expiration). a value of 99999 will disable password expiration.
		6. `[integer]` warning period in days.
		7. `[integer]` password inactivity period in days (the number of inactive days after password expiration before the account is locked). a value of -1 will remove an account's inactivity.
	* `-x` set maximum password lifetim
	* `-w` set the number of days of warning before the password expires during which the user is warned that the password must be changed.
- `chage [options] [user]` ^chage
	- (1) change user password expiry information
	- This command, which stands for “change age”, is used to change the password aging information of a user.
	* without root access, users can only use `-l` to query their info
	* `[no option]` behaves interactively
	* `-l` show status
	* `-d/--lastday [days]` specify number of days since the password was last changed. 0 will force user to change on next login.
	* `-E/--expiredate [date]` set expiration date for user
	* `-I/--inactive [days]` set the number of days of inactivity after a password expires during which the user should update the password (otherwise the account will be disabled).
	* `-m/--mindays [days]` set the minimum password lifetime for a user account.
	* `-M/--maxdays [days]` set the maximum password lifetime for a user account.
	* `-W/--warndays [days]` set the number of days of warning before the password expires during which the user is warned that the password must be changed.
* `getent`
	* (1) get entries from NSS libraries
	* Another way to access these databases is to use the `getent` command. In general, this command displays entries from databases supported by the *Name Service Switch (NSS)* libraries and requires the name of the database and a lookup key. If no key argument is provided, all entries in the specified database are displayed (unless the database does not support enumeration). Otherwise, if one or more key arguments are provided, the database is filtered accordingly.
	* Remember that `getent` can only access databases configured in `/etc/nsswitch.conf`.
	* `getent passwd emma`
	* `getent group db-admin`
* `ulimit` ^user-limits-ulimit
	* Limits on User Logins, Processes, and Memory Usage
	* `-S` for soft and `-H` for hard limits
	* `-a/-Sa` shows all soft limits
	* `-Ha` shows all hard limits
	* `-b` maximum socket buffer size
	* `-f` maximum size of file written by the shell and its children
	* `-l` maximum size that may be locked into memory
	* `-m` maximum resident set size (RSS) - the current portion of memory held by a process in main memory (RAM)
	* `-v` maximum amount of virtual memory
	* `-u` maximum number of processes available to a single user
	* you can set a new limit by providing a value after designating an attribute.
	* to make limits persistent across reboots, use `/etc/security/limits.conf`
	* for further infomation **use *`man bash`***. there's no manpage for this!
- `last` ^last
	- (1) show a listing of last logged in users
	- `last` prints a listing of the last logged in users with the most recent information on top.
	* for examples refer to page 497
	* you can also pass a username
	* to check for bad login attempts use `lastb`
* `who` ^who
	* (1) show who is logged on
	* `[no option]` display logged in users: terminal, date, time, hostname
	* `-b/--boot` display time of last reboot
	* `-r/--runlevel` display current runlevel
	* `-H/--heading` print column headings
- `w` ^w
	- (1) Show who is logged on and what they are doing.
	* compared to `who`, it's a bit more verbose
	* columns
		* `USER`
		* `TTY`
		* `FROM` remote host from which the user is logged on
		* `LOGIN@` login time
		* `IDLE` idle time
		* `JCPU` time used by all processes attached to the tty (including currently running background jobs).
		* `PCPU` time used by current process (the one showing under WHAT).
		* `WHAT` command line of current process.
		* just like who, you can pass w usernames.
- `chown`
  - (1) change file owner and group
  - (2) change ownership of a file
- `logout` - (3) write utmp and wtmp entries
- `login`
  - (1) begin session on the system
  - (3) write utmp and wtmp entries
- `groups` - (1) print the groups a user is in
- `whoami` - (1) print effective userid

### sudo Configuration
* On the other hand, there is the sudo command. With it you can execute a command as the root user — or any other user for that matter. From a security perspective, sudo is a far better option than su as it presents two main advantages:
	* to run a command as root, you do not need the root user’s password, but only that of the invoking user in compliance with a security policy. The default security policy is sudoers as specified in `/etc/sudoers` and `/etc/sudoers.d/*`.
	* sudo lets you run single commands with elevated privileges instead of launching a whole new subshell for root as su does.
* sudoers will use a per-user (and per-terminal) timestamp for credential caching, so that you can use sudo without a password for a default period of fifteen minutes. This default value can be modified by adding the `timestamp_timeout` option as a Defaults setting in `/etc/sudoers` (e.g.: `Defaults timestamp_timeout=1` will set credential caching timeout to one minute).
* sudoers
	* sudo's main configuration file is `/etc/sudoers`(there is also the `/etc/sudoers.d` directory). That is the place where users' sudo privileges are determined. In other words, here you will specify who can run what commands as what users on what machines — as well as other settings.
		```text
		carol@debian:~$ sudo less /etc/sudoers
		(...)
		# User privilege specification
		root
		ALL=(ALL:ALL) ALL
		# Allow members of group sudo to execute any command
		%sudo ALL=(ALL:ALL) ALL
		```
	* The privilege specification for the root user is ALL=(ALL:ALL) ALL. This translates as: user root (root) can log in from all hosts (ALL), as all users and all groups ((ALL:ALL)), and run all commands (ALL). The same is true for members of the sudo group — note how group names are identified by a preceding percent sign (%).
	* Thus, to have user carol be able to check apache2 status from any host as any user or group, you will add the following line in the sudoers file:
		* `carol ALL=(ALL:ALL) /usr/bin/systemctl status apache2`
	* You may want to save carol the inconvenience of having to provide her password to run the systemctl status apache2 command. For that, you will modify the line to look like this:
		* `carol ALL=(ALL:ALL) NOPASSWD: /usr/bin/systemctl status apache2`
	* Say that now you want to restrict your hosts to 192.168.1.7 and enable carol to run systemctl status apache2 as user mimi. You would modify the line as follows:
		* `carol 192.168.1.7=(mimi) /usr/bin/systemctl status apache2`
	* If carol was to be promoted to sysadmin and you wanted to give her all privileges, the easiest approach would be that of including her in the special sudo group with usermod and the -G option (you may also want to use the -a option, which ensures that the user is not removed from any other groups they might belong to):
		* `sudo useradd -aG sudo carol`
	* Aside from users and groups, you can also make use of aliases in /etc/sudoers. There are three main categories of aliases that you can define: host aliases (*Host_Alias*), user aliases (*User_Alias*) and command aliases (*Cmnd_Alias*). Here is an example:
		```text
		# Host alias specification
		Host_Alias SERVERS = 192.168.1.7, server1, server2
		# User alias specification
		User_Alias REGULAR_USERS = john, mary, alex
		User_Alias PRIVILEGED_USERS = mimi, alex
		User_Alias ADMINS = carol, %sudo, PRIVILEGED_USERS, !REGULAR_USERS
		# Cmnd alias specification
		Cmnd_Alias SERVICES = /usr/bin/systemctl *
		# User privilege specification
		rootALL=(ALL:ALL) ALL
		ADMINSSERVERS=SERVICES
		# Allow members of group sudo to execute any command
		%sudo
		ALL=(ALL:ALL) ALL
		```
		* Host Aliases
			They include a comma-separated list of hostnames, IP addresses, as well as networks and netgroups (preceded by +). Netmasks can be also specified. The SERVERS host alias includes an IP address and two hostnames: `Host_Alias SERVERS = 192.168.1.7, server1, server2`
		* User Aliases
			They include a comma-separated list of users specified as usernames, groups (preceded by %) and netgroups (preceded by +). You can exclude particular users with !. The ADMINS user alias — for example — includes user carol, the members of the sudo group and those members of the PRIVILEGE_USERS user alias that do not belong in the REGULAR_USERS user alias: `User_Alias ADMINS = carol, %sudo, PRIVILEGED_USERS, !REGULAR_USERS`
		* Command Aliases
			They include a comma-separated list of commands and directories. If a directory is specified, any file in that directory will be included — subdirectories will be ignored, though. The SERVICES command alias includes a single command with all its subcommands — as specified by the asterisk (\*): `Cmnd_Alias SERVICES = /usr/bin/systemctl *`
		* As a result of the alias specifications, the line ADMINS SERVERS=SERVICES under the User privilege specification section translates as: all users belonging in ADMINS can use sudo to run any command in SERVICES on any server in SERVERS.
		* There is a fourth type of alias that you can include in /etc/sudoers: runas aliases (Runas_Alias). They are very similar to user aliases, but allow you to specify users by their user ID (UID). This feature might be convenient in some scenarios.
