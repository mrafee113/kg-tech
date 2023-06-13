### Variables
* in bash, giving a `value` to a `name` is called `variable assignment`.
* assign: `[name]=[value]`
* accessing a name is called `variable referencing`.
	* `echo $[name]`
* variable names syntax `[a-zA-Z]+[a-zA-Z0-9_]*`
* variable values syntax `[a-zA-Z0-9?!*./etc]`
	* enclosing the value by double quotes `""` or `''`:
		* you can now use these too: ` <>|&`
			* or alternatively you can escape them with `\`
* in var assignment, single quotes `''` will take value literally, whereas double quotes `""` allow for `variable substitution`.
	* `$[name]` is variable substitution
	* but `![name]` is referencing history events
		* which I have no clue about #todo 
* local / shell variables
	* immutable
		* `readonly [name]=[value]`
		* or after creation `readonly [name]`
		* bash refuses change `-bash: [name]: readonly variable`
		* list all readonly variables by `readonly` or `readonly -p`
	* `set` useful when dealing with local vars
		* outputs all of the currently assigned shell `vars` and `functions`
	* `unset [name]` for global/local
	* global variable is aka `environment variable`
		* conventionally written in uppercase
	* `export`
		* `export [name]` makes a local var, a global var
		* `export [name]=[value]` declares a global var
			* `declare -x [name]=[value]` too
		* `export -n [name]` turns a var *back* into a local var
			* didn't work on zsh
		* `export -p` lists all env vars
* `env` and `printenv`
	* used to list environment variables
* `env -i bash` to enter an empty as possible environment
* common vars
	* `DISPLAY` is related to the X Server
	* `HISTCONTROL` controls what commands get saved into the `HISTFILE`
		* `ignorespace` commands starting with a space will not be saved
		* `ignoredups` commands which is the same as the previous one will not be saved
		* `ignoreboth`
	* `HISTSIZE` sets the number commands to be stored in **memory** while the session lasts
	* `HISTFILESIZE` sets the number of commands to be saved in `HISTFILE` both at the start and the end of the session :??
	* `HISTFILE` 
	* `HOME`
	* `HOSTNAME` stores the TCP/IP name of the host computer
	* `HOSTTYPE` stores the architecture of processor
	* `LANG`
	* `LD_LIBRARY_PATH` consists of colon seperated list of dirs for shared libraries
	* `MAIL` stores location for bash to search for mail
	* `MAILCHECK` stores bash check mail frequency in seconds
	* `PATH` 
	* `PS1, PS2, PS3, PS4` refer to page 43
	* `SHELL` stores the absolute path of the current shell `/usr/bin/bash`
	* `USER`

### Aliases and Functions
#### Aliases
* `alias [alias name]=[command(s)]`
* `alias` will list all current aliases
	* especially good for inspecting zsh plugins
* `unalias [alias name]`
* you can escape aliases with `\`
* dynamic / static
	* single quotes: dynamic
		```sh
		$ alias where?='echo $PWD'
		$ where?
		/home/user
		$ cd Music
		$ where?
		/home/user/Music
		```
	* double quotes: static
		```sh
		$ alias where?="echo $PWD"
		$ where?
		/home/user
		$ cd Music
		$ where?
		/home/user
		```
#### Functions
* def syntaxes
	* `function [f name] {\n command(s) \n}`
	* `[f name]() {\n command(s) \n}`
* bash special variables
	* `$?` stores the result of the last command run
		* `0` means success
	* `$$` expands to the shell PID
	* `$!` expands to the PID of the last background job
	* `$[0-9]` positional parameters
	* `$#` expands to the number of arguments passed
	* `$@ $*` these expand to the arguments (themselves) passed
	* `$_` expands to the last parameter or the name of the script
	* for more use `man bash`
* the scope of vars set in functions is local! meaning you can reference it during the shell session
* `shebang`
	* the first optional line in scripts which defines what program is going to run that script. 
		* `#/usr/bin/bash`
		* `#/usr/bin/sh`
		* `#/usr/bin/python3`
		* `#/usr/bin/zsh`
* `unset -f [function name]`

### Script Arguments
* `$*` all the arguments
* `$@` all the arguments
	* if it's wrapper in double quotes like `"$@"`, every arg will be enclosed by double quotes.
* `$#` the number of args
* `$0` the name of the script file
* `$!` PID of the last executed program
* `$$` PID of the current shell
* `$?` numerical exit code status of the last finished command
	* `0` means success
* `$[1-n]` positional args
	* if `n` is larger than 9, it should be in brackets like `${10}`

### Arrays
* they are 0 based indexed
* `declare -a [name]` 
* `[name]=( [space seperated values] )`
	* notice the spaces at the beginning and the end
* referenced like `${[name][[position]]}`
	* correct: `echo ${var[12]}`
	* incorrect
		* `echo $var` -> first value
		* `echo ${var}` -> first value
		* if max assigned is 10 values, `echo ${var[11]}` -> empty line
* change/assign
	* `[name][[position]]=[value]`
		* `var[12]=abcd`
* size
	* ***like ordinary variables*** `${#[name][[position]]}`
	* `echo ${#var[0]}` == `echo ${var}`
	* `echo ${#var[*]}` returns size of array
		* interestingly, if you modify the array out of place, the array length will only increase by your actual modification.
			* e.g. if array is size 5, and you assign something to position `10`, the size will increase by one.
* you can declare using output of other commands (cmd substitution)
	* `FS=( $(cut -f 2 < /proc/filesystem) )`
	* or `a=$(cut -f 2 < /proc/filesystem); FS=( $(echo $a) )`
* something about `IFS (Input Field Seperator)`

### Conditions
* `command1 && command2 && command3`
	* each will be executed depending on the success of the previous one
* `command1 || command2 || command3`
	* each will be executed depending on the failure of the previous one
* `if` only runs its body if the return of its condition is `0` which means success
* `test` is usually accompanied by if
	* a replacement for `test` is square brackets: `[]`
		* `if [ -x /bin/bash ] ; then echo "confirmed" ; fi`
			* notice space around brackets
	* the output is stored in `$0` and not printed. doesn't print!
	* recommended to surround a test var by double quotes, because if empty -> syntax error
		* `test -x "$VAR"`
	* options for files/dir `[path]`
		* `-a` if it exists and is file
		* `-b` if it's a special block file
		* `-c` if it's a special character file
		* `-d` if it's a dir
		* `-e` if it exists
		* `-f` if it exists and is regular
		* `-g` if it has the SGID perm
		* `-h/-L` if it's a symlink
		* `-k` if it has the Sticky Bit perm
		* `-p` if it's a pipe file
		* `-r` if it's readable by user
		* `-s` if it exists and isn't empty
		* `-S` if it's a socket file
		* `-t` if it's open in a terminal
		* `-u` if it has the SUID perm
		* `-w` if it's writable by user
		* `-x` confirms existence and execution/search
			* `if test -x /bin/bash ; then echo "confirmed" ; fi`
		* `-O` if it's owned by the user
		* `-G` if it belongs to the effective group of the user
		* `-N` if it's been modified since the last time it was accessed
		* `[p1] -nt [p2]` if path1 is newer than path2 based on mod dates
		* `[p1] -ot [p2]` if path1 is older than path2
		* `[p1] -ef [p2]` if path1 is a hardlink of path2
	* options for text
		* `-z` if it's empty
		* `-n` or an ommision of options, tests if it's not empty
		* `"$TXT1" = "$TXT2"`  or `"$TXT1" == "$TXT2` if they're equal
		* `"$TXT1" != "$TXT2"` if not equal
		* `"$TXT1" < "$TXT2"` alphabetically lower
		* `"$TXT1" > "$TXT2"` alphabetically higher
	* options for numbers
		* for two numbers `test $NUM1 [op] $NUM2`
			* op=`-lt -gt -le -ge -eq -ne`
	* general options
		* `! EXPR` evals if expr is wrong
		* `EXPR1 -a EXPR2` evals if both are **true**
		* `EXPR1 -o EXPR2` evals if at least one is **true**
* `case`
	* example
		```bash
		#!/bin/bash
		
		DISTRO=$1
		
		echo -n "Distribution $DISTRO uses "
		case "$DISTRO" in
			debian | ubuntu | mint)
			echo -n "The DEB"
			;;
			centos | fedora | opensuse)
			echo -n "The RPM"
			;;
			*)
			echo -n "an unknown"
			;;
		esac
		echo " package format."
		```
	* items should be seperated by pipes `|` and terminated by `)`
	* each list of patterns and associated commands must be terminated with `;;`, `;;&`, `;&`
	* Bash has an option called nocasematch that enables case-insensitive pattern matching for the case construct and other conditional commands. The shopt builtin command toggles the values of settings controlling optional shell behaviour: shopt -s will enable (set) the given option and shopt -u will disable (unset) the given option. Therefore, placing shopt -s nocasematch before the case construct will enable case-insensitive pattern matching. Options modified by shopt will only affect the current session, so modified options inside scripts running in a sub-shell — which is the standard way to run a script — do not affect the options of the parent session.

### Loops
* `for`
	* default
		```bash
		for VARNAME in LIST
		do
			COMMANDS
		done
		```
	* C-like
		```bash
		for (( IDX = 0; IDX < 2; IDX++ ))
		do
			COMMANDS
		done
		```
* `until`
	```bash
	until [ $IDX -eq ${LIST[*]} ]
	do
		COMMANDS
	done
	```
* `while`
	* like until but `while [ $IDX -lt ${LIST[*]} ]`

### Etcetera
* `read [text]` can be used in a script to ask the user for `input`
	* `-p` will also `echo` it back at the same time
	* `read [text] [name(s)]` will assign space seperated input terms to `name(s)`
* capture the output of a command
	* backticks \`\`: `OS=`\``uname -o`\``
	* or `OS=$(uname -o)`
* arithmetic `expr`
	* `expr 1 + 2` -> `3`
	* `SUM=$(expr 1 + 2)`
	* `SUM=$((1+2))` = `SUM=$(( 1 + 2 ))`
		* though there should be no space between adjacent parentheses
* script output
	* `echo -e` recognizes special characters
		* e.g. `echo "a\tb"` -> `a\tb`, `echo -e "a\tb"` -> `a       b`
		* but it requires double quotes, not single quotes
	* `printf "[format]" [var(s)]`
		* `format` can contain placeholders
			* `%s` strings
			* `%d` integers
		* works exactly like in C lang
