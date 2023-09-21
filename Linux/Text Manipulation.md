### Commands
- `cat` aka concatenate
	- (1) concatenate files and print on the standard output
	- view compressed files
		- `bzcat` for bzip
		- `xzcat` for xz
		- `zcat` for gzip
- `less`
- [[Linux/Shell#Pipes and Redirection]]
- `diff` - (1) compare files line by line
- `grep`
	- (1) print lines that match patterns
	* `-i` means *case insensitive*
	* another usage: `grep [filter] [command]`
		* doesn't include piping
	* `-v` inverts matching (selects non-matching lines)
- `head` first \[10\] lines
  - (1) output the first part of files
  - `-n` limits output
- `tail` last \[10\] lines
	- (1) output the last part of files
* `nl` will number the lines of a text stream
- `wc` is a word/line/char/byte counter
	- (1) print newline, word, and byte counts for each file
- `cut` - (1) remove sections from each line of files
- `sort` - (1) sort lines of text files
- `paste` - (1) merge lines of files
- `sed` is the stream editor for filtering and transforming text
	- (1) stream editor for filtering and transforming text
	* `-n` suppresses the original output of sed, or in other words filters the text streams instead of just changing some lines. **I GUESS!**
	* filter `/[pattern]/p` picks (I guess) the lines that match
	* filter `/[pattern]/=` prints line number of the lines that match
	* filter `/[pattern]/d` deletes the lines that match
	* filter `s/[pattern]/[pattern]/` swaps the lines that match
	* `-i` performs in-place operation on the file
		* if `-i` is written like `-i[filename with no spaces]`, sed will backup file to `./[original filename][appended filename after -i]`
- `uniq` remove repeated lines
	- (1) report or omit repeated lines
	- `-c` shows how many times it was repeated
- `tee` store on file and at the same time print to `stdout`
  - (1) read from standard input and write to standard output and files
  - `-a` appends
- `view` - (1) Vi Improved, a programmer's text editor
- `vim` - (1) Vi Improved, a programmer's text editor
- `vimtutor` - (1) the Vim tutor
- `awk` - (1) pattern scanning and text processing language
- `tac` - (1) concatenate and print files in reverse
- `read` - (2) read from a file descriptor
- `join` - (1) join lines of two files on a common field
- `diff3` - (1) compare three files line by line
- `patch` - (1) apply a diff file to an original
- `zipgrep` - (1) search files in a ZIP archive for lines matching a pattern
- `column` - (1) columnate lists
- `fzf` - (1) a command-line fuzzy finder
- `strings` - (1) print the sequences of printable characters in files
- `split` - (1) split a file into pieces
- `tr` - (1) translate or delete characters
* `groff` - (1) front-end for the groff document formatting system

### Text Filtering
#### Regular Expressions
* The simplest regular expressions contain an `atom`.
* An `atom`, so named because it’s the basic element of a regular expression, is just a character that may or may not have special meaning.
	* `.` (dot): match any character
	* `^` (caret): match the beginning of a line
	* `$` (dollar sign): match the end of the line
	* `^` and `$` are also called `anchors` because they're used when the beginning or the end of a line are of interest.
	* `[]` (bracket expression)
		* use `[^]` to *not* the expression
		* ranges `[0-9], [a-z] [A-Z]`
			* Ranges must be used with caution, as they might not be consistent across distinct locales.
		* classes
			* `[:alphanum:]`
			* `[:alpha:]` alphabetic
			* `[:ascii:]`
			* `[:blank:]` space or tab
			* `[:cntrl:]` a control character #todo 
			* `[:digit:]`
			* `[:xdigit:]` hexadecimal digits (0-F)
			* `[:lower:]`
			* `[:upper:]`
			* `[:graph:]` any printable character except space
			* `[:print:]` any printable character including space
			* `[:punct:]` any printable character except space or an alphanumeric
			* `[:space:]` white-space characters: form-feed `\f`, newline `\n`, carriage return `\r`, horizontal tab `\t`, vertical tab `\v`
* The reach of an atom, either a single character atom or a bracket atom, can be adjusted using an atom `quantifier`.
	* Atom quantifiers define atom `sequences`, that is, matches occur when a contiguous repetition for the atom is found in the string. The substring corresponding to the match is called a `piece`.
	* `*` (star): atom occurs zero or more times
		* It's a regular character if it's at the beginning or preceded by a backslash `\`.
	* `+` (plus sign): atom occurs one or more times
	* `?` (question mark): atom occurs once or not at all
	* `+` and `?` quantifiers need to be preceded by a backslash `\` in **basic REs**
		* without that `\`, unlike extended REs, these are literal characters
	* A `bound` is an atom quantifier that, as the name implies, allows a user to specify precise quantity boundaries for an atom.
		* extended REs
			* `{i[int]}`: the atom must appear **exactly** `i` times
			* `{i,}`: the atom must appear **at least** `i` times
			* `{i,j}`: the atom must appear **at least** `i` times and **at most** `j` times
		* basic REs
			* the delimiters must be preceded by `\:` and `\{` and `\}`
			* if not they would be considered literal chars
			* A `\{` followed by a character other than a digit is a literal character, not the beginning of a bound.
* Branches: only in extended REs
	* they're seperated by `|`
	* each one is an independent RE
	* the matching will be based on either of them that has matches
	* in basic REs `|` is a literal characters, however in most programs `\|` will be interpreted as a branching character (in a basic RE)
* Back References #todo 
	* `([[:digit:]])\1` ?? page368
	* `find /usr/share/fonts -regextype posix-extended -iregex '.*(dejavu|liberation).*sans.*(italic|oblique).*'`

#### Chain Filtering
* `grep`
	* `[-c/--count]` only displays the total count of match occurence
	* `[-i/--ignore-case]` 
	* `[-f/--file]=`
	* `[-n/--line-number]` also display file line numbers
	* `[-v/--invert-match]`
	* `[-H/--with-filename]` print also the file name containing the line
	* `[-r/--recursive]` scans all files in a given directory
	* `[-R/--dereference-recursive]` recursive, but unlike `-r` it follows symlinks
* `egrep` = `grep -E`
	* has extra features like extended REs
* `fgrep` = `grep -F`
	* no parsing for REs
	* only matches literal strings
* `sed`
	* `sed [options] -f [file]`
	* `sed [options] [file]`
	* `sed [options] -e [command]`
	* "factor \`seq 12\`" returns prime factors for numbers 1 to 12
	* `sed [number]d` deletes the `number`th line of output
	* `sed [n],[m]d` deletes lines from the `nth` to the `mth`
	* more than one insctruction can be given using `;`
		* but to prevent shell misinterpretations the instructions must either be in double quotes `""` or the semi-colon `;` must be preceded by a backslash `\`.
	* in sed anything between two slashes `/` is considered a regular expression. and by default all basic REs are supported.
		* `factor `\`seq 12\`` | sed "1d;/:.*2.*/d"`
		* `sed -e "/^#/d" /etc/services`
	* `c [text]` replaces matches with `text`
		* `factor `\`seq 12\`` | sed "1d;/:.*2.*/c REMOVED"`
	* `sed s/[find]/[replace]` replaces the first occurance matched
	* `sed s/[find]/[replace]/g` replaces all occurances matched

### Vim
* `vi +[line] [file]` opens file at `line`
* in vi `:vim-modes-intro`
* insert mode
* normal mode `default`
	* `/ and ?` search forward and backward
	* `v, V` start selection with current char or entire line
	* go to
		* `0`, `$` go to the beginning and the end of the line
		* `1G`, `G` go to the beginning and the end of the document
		* `(`, `)` go to the beginning and the end of the sentence
		* `{`, `}` go to the beginning and the end of the paragraph
		* `w`, `W` jump word, and jump word including punctuation
		* `h` left, `j` down, `k` up, `l` right
		* `e or E` go to the end of the current word
	* enter insert mode
		* `i` at current position
		* `I` at beginning of line
		* `a` after the current position 
		* `A` at the end of the line
		* `o` add a new line in the next line
		* `O` add a new line in the prev line
	* operation
		* `u` undo the last action
		* `Ctrl-R` redo the last action
		* `ZZ` close and save
		* `ZQ` close and don't save
		* regarding position
			* `s, S` erase char under cursor, or erase the entire line
			* `c` change the char under cursor
			* `r` replace char under cursor
			* `x` delete selected chars or the char under cursor
			* `y, yy` copy current/selected char or entire line
			* `p, P` paste copied content, after or before the position
* If preceded by a `number`, the command will be executed `number` of times.
	* `3yy` copies current line and the next two
	* `d5w` deletes current word and 4 next words
	* `vey` copies selection from current position until the end of the next word
	* `v3ey` copies selection from current position until the end of the next 3 words
* `vi` can organize text in **registers**. A register is specified by a character `"` and once created, it's kept until the end of the session.
	* `"ly` copies selection into register `l` and can be pasted through `"lp`
* `vi` can also store **bookmarked** positions per session. pressing `m` followed by a key will store the current position. returning back to that position can be done by `'[key]`.
* `vi` can also **record operations** per session and do them later.
	* to surround a selected text in double quotes, after the selection, press `q` followed by a key to start recording and associate that recording with that key, like `d`. The line `recording` will appear in the fotter line. First command is `x` to remove selection and copy it at the same time. The key `i` is pressed to insert two double quotes at the qurrent position, then `ESC` returns to normal mode. The last command is `P` to reinsert the deleted selection just before the last double quote. Pressing `q` again to end the recording.
	* Now a macro consisting of key sequence `x i "" ESC P` will execute every time keys `@d` are pressed in normal mode.
	* To make macros persistent they should be stored in the configuration file. 
		* in `.vimrc`: `let @d = 'xi""P'`
* colon commands `:`
	* `:s/REGEX/TEXT/g` like sed finds and replaces all occurances
	* `:!` run a following shell command
	* `:quit or :q` exit program
	* `:quit! or :q!` exit without saving
	* `:wq` save and exit
	* `:exit or :x or :e` save and exit, if needed
	* `:visual` go back to navigation mode
* `vimtutor` teaches vim
