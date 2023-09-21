* `ls --color=auto` for more info `man dir_colors`

[[Linux/Bash Scripting]]

### Shell Types
* interactive / login
	* `interactive/non-interactive` refers to to the interaction of the user with the shell. user gives command, shell gives output.
	* `login/non-login` refers to the provision of username password by the user
	* *interactive login shell*: provide user/pass at startup
	* *interactive non-login shell*: normal desktop use (shell opened after login)
	* *non-interactive login shell*: rare and impractical like `[command] | ssh`
	* *non-interactive non-login shell*: automated scripts
* pts / tty
	* *pts shell*: when opened from gui `ctrl+alt+F7`
		* pts: pseudo terminal slave `man pts`
	* *tty shell*: when run from system console `ctrl+alt+F[1-6]`
		* tty: teletypewriter `man tty`

#### Launching Shells
* `bash`
	* if you type `bash` in a shell, another shell will open which is a child of the prev one.
	* `[-l/--login]`
	* `-i` will invoke an interactive shell
	* `--noprofile` with login shells, will ignore startup files `/etc/profile`, `~/.bash_profile`, `~/.bash_login`, `~/.profile`
	* `--norc` with interactive shells, will ignore startup files `/etc/bash.bashrc`, `~/.bashrc`
	* `--rcfile [file]` is like `--norc` but takes `[file]` as rc
* su / sudo
	* su: change uid or become root
		* `su [-/-l/--login] [user]` will start an interactive shell as `[user]`
		* `su [user]` will start in interactive non-login shell as `user`
		* `su -` or `su - root` will start an interactive non-login shell as root
	* sudo: execute commands as another user
		* to add user to sudoers `usermod -aG sudo [user]`
		* `sudo su [-/-l/--login] [user]` is same as `su`
		* `sudo su [user]` is same as `su`
		* `sudo -u [user] -s` is the same as `sudo su [user]`
		* `sudo su -` or `sudo su - root` opens an interactive login shell as root
		* `sudo su root` or `sudo su` will start an interactive *non-login* shell as root
		* `sudo -s` or `sudo -u root -s` will start a non-login shell as root
		* `sudo -i` is the same as `sudo su -`
		* `sudo -i [command]` will start an interactive login shell as root, run command and return to original shell/user.
	* When using either su or sudo, it is important to consider our particular case scenario for starting a new shell: Do we need the target user’s environment or not? If so, we would use the options which invoke login shells; if not, those which invoke non-login shells.
* what's my shell: `echo $0`
	* interactive non-login: `-bash or -su`
	* interactive login: `bash or /bin/bash`
	* non-interactive non-login: `[name of script]`
* how many shells do we have
	* `ps aux | egrep "(bash|zsh)"`

### Config
* when there is more than one file to be searched, once one is found and run the others are ignored.
* templates for local startup configs are stored in `/etc/skel` according to `grep SKEL /etc/adduser.conf`
	* this dir can contain dirs too. in fact anything in it will be used for a new user in their home dir.
* interactive login shell
	* global
		* `/etc/prfile` this is the system-wide .profile file for the Bourne shell and Bourne compatible shells (bash included). Through a series of if statements this file sets a number of variables such as PATH and PS1 accordingly as well as sourcing — if they exist — both the file /etc/bash.bashrc and those in the directory /etc/profile.d.
		* `/etc/profile.d/*` contains scripts that get executed by profile
	* local
		* `~/.bash_profile` this Bash specific file is used for configuring the user environment. It can also be used to source both ~/.bash_login and ~/.profile.
		* `~/.bash_login` also Bash specific, this file will only be executed if there is no ~/.bash_profile file. Its name suggests that it should be used to run commands needed on login.
		* `~/.profile` this file is not Bash specific and gets sourced only if neither ~/.bash_profile nor ~/.bash_login exist — which is normally the case. Thus, the main purpose of ~/.profile is that of checking if a Bash shell is being run and — if so — sourcing ~/.bashrc if it exists. It usually sets the variable PATH so that it includes the user’s private ~/bin directory if it exists.
		* `~/.bash_logout` if it exists, this Bash specific file does some clean-up operations when exiting the shell. This can be convenient in such cases as those in remote sessions.
* interactive non-login shell
	* global
		* `/etc/bash.bashrc` this is the system-wide .bashrc file for interactive bash shells. Through its execution bash makes sure it is being run interactively, checks the window size after each command (updating the values of LINES and COLUMNS if necessary) and sets some variables.
	* local
		* `~/.bashrc` in addition to carrying out similar tasks to those described for /etc/bash.bashrc at a user level (such as checking the window size or if being run interactively), this Bash specific file usually sets some history variables and sources ~/.bash_aliases if it exists. Apart from that, this file is normally used to store users' specific aliases and functions. Likewise, it is also worthwhile noting that ~/.bashrc is read if bash detects its `<stdin>` is a network connection (as it was the case with the Secure Shell (SSH) connection in the example above).
* non-interactive login shell
	A non-interactive shell with the -l or --login options is forced to behave like a login shell and so the startup files to be run will be the same as those for interactive login shells. refer to page 12
* non-interactive non-login shell
	Scripts do not read any of the files listed above but look for the environment variable BASH_ENV, expand its value if needed and use it as the name of a startup file to read and execute commands.

### Environment Variables
* `env` lists environment vars
* *`PATH`* env var contains a list of directories that the shell or any other program can look in for other programs without specifying a complete path.
* `echo $[var name]`
* `export [var name]` will pass the variable and its value to any ***child*** shells that you may open
* `unset [var name]` will kill the variable
* `set` lists all variables and functions
* Bash classifies variables as either shell/local (those which live only within the limits of the shell in which they were created) or environment/global (those that are inherited by children shells and/or processes).

### Pipes and Redirection
* `[command] > [file]` tells a command to direct its output to a file instead of stdout
* `[command] >> [file]` like `>` but appends to the end of a file
* `[command that takes input] < [file] | [command]`
	* this will read redirect file stream to the first command and then redirect the output to the second command

#### Communication Channels
Standard linux **processes** have 3 communication channels **opened by default**.
* `0: stdin` the standard input channel at `/dev/stdin`
* `1: stdout` the standard output channel at `/dev/stdout`
* `2: stderr` the standard error channel at `/dev/stderr`
* The method of `file descriptors` allows to dynamically associate integer numbers with data channels, so that a process can reference them as its input/output data streams.

#### Redirect
The reassignment of a channel's file descriptor *in the shell environment* is called a `redirect`.
* redirection of `stdout` to a `file`: `>` or `1>`
	* `cat /some/file 1>/some/other/file`
* redirection of `stderr` to a `file`: `2>`
	* `cat /some/non/existent/file 2>/other/file`
* redirection of both `stderr` and `stdout`: `&>` or `>&`
* redirection target: `[fd]>&[other-fd]`
	* `1>&2` redirects `stdout` to `stderr`
* It is **not** possible to redirect `stderr` to `stdin`, **directly**. Instead, if necessary, you can redirect `stderr` to `stdout` and then to `stdin`.
	* `cat file.txt >log.txt 2>&1` will redirect `stderr` to `stdout` and then to the `stdin` of `log.txt`.
* redirecting data to `/dev/null` will discard that data **completely**.
* the `<` operator is used to redirect the content of a file to the `stdin` of a process. Right to left data flow!
	* `uniq -c </file`
		* this quals `uniq -c 0</file`
* It is possible for a program to ask for data from file descriptors of a variety of numbers. `0, 1, 2, 3, 4, etc`
* ***Guess***: using redirections is like definitions of redirection for bash.
	* example: consider a C program that works with fd 3 and 4. This is how you give them to it: `./fd 3</some/file 4>&1`
		* This program reads from fd 3 which has `/some/file` redirected to it, and writes to fd 4 which is being redirected to `stdout`.
	* Quote from book: `"The same file descriptor can even be used as input and output. In this case, the file descriptor is defined in the command line with both less than and greater than symbols, like in 3<>/tmp/error.txt."`
* The `here` Document and the `here` string methods
	* the here `document` redirect method allows to **type** multi-line text that will be used as data.	
		```txt
		$ wc -c <<EOF
		> How many characters
		> in this here document?
		> EOF
		43
		```
		* uses `<<[ending-term]`
	* the here `string` redirect method is like the document one but only for one line and it uses `<<<`
		* `wc -c <<<"How many characters are in this string?"`

#### Pipes
* left to right data flow
* the target is another **process**, not a filesystem path, a file descriptor or here document
* the pipe char `|` tells the shell to open all processes at the same time and connect the output of each of to the input of the next (from left to right), except the last one which will be redirected to `stdout`
* trick: `make 2>&1 | tee log.txt`
	* will output `make: *** No targets specified and no makefile found.`
	* `cat log.txt` will output `make: *** No targets specified and no makefile found.`

#### Command Substitution
* By placing a command inside backquotes, Bash replaces it with its standard output.
	* mkdir \`date +%Y-%m-%d\`
* Also works with `$()`
	* `mkdir $(date +%Y-%m-%d)`
* save output of a command as a var
	* `OS=$(uname -o)`
	* OS=\`uname -o\`
* `xargs` is a sophisticated version for this practice #todo 

### Sourcing Scripts
* the mechanism of including or executing other scripts is called sourcing files.
* using `source [file]`
* using `.` (dot): `. [file]`
	* in zsh you must give full path
* `!!` expands to the last command
* `!&` expands to the last argument of the last command