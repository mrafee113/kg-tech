##### Distros
[[Linux/Ubuntu/Package Management|Ubuntu]]

#### Commands
- `pip` - (1) A tool for installing and managing Python packages
- `whereis` - (1) locate the binary, source, and manual page files for a command
- `which` - (1) locate a command
- `update-alternatives` - (1) maintain symbolic links determining default commands

#### Shared Libraries
* shared libraries -> aka shared objects
	Pieces of code like functions or classes that are recurrently used by various programs. In windows they are DLLs.
	* common locations ^shared-libraries-common-locations
		* `/lib`
		* `/lib32`
		* `/lib64`
		* `/usr/lib`
		* `/usr/local/lib`
	* `ldd` command
		- list program libraries: `ldd [absolute executable path]`
		- list library dependencies: `ldd [absolute library path]`
* object files
	Compiler turns code into machine code that is stored as something called object files.
* linker
	combines object files and libraries to finally produce executables.
	* static libs
		- heavier program
		- program has a copy of the library
		- independent of the library in runtime
	* shared (dynamic) libs
		* economical as only one copy of the library is in memory even if used by multiple programs
		* no copying into the program
		* must be available at runtime
	* dynamic linker (`ld.so` or `ld-linux.so`)
		* resolves references in dynamically linked programs
		* searches for libraries in specific dirs specified in `/etc/ld.so.conf` and `/etc/ld.so.conf.d/`
			* `ldconfig` command reads these config files
		* defining extra shared library paths
			`LD_LIBRARY_PATH` environment variable. Whether it's in current shell, or exported to other shells of the session, or even made permenant in `~/.bashrc` or `/etc/bash.bashrc`

### Installation From Source
* basic steps required to build a program from source
	1. download the installation file
	2. unpack the installation file
	3. read the installation's documentation
	4. prepare for compiling
	5. compile the program
	6. move the binaries to appropriate locations
* Programs you run, sometimes called binaries or machine code, were originally source code programs, written in a programming language “easy” for humans to understand. A source code program is compiled and/or interpreted into machine code, and it becomes an executable program. To modify an executable program, you need its source code version.
* The proper final location for original source code is in a /usr/src/ subdirectory. However, during the installation process, the source code should temporarily reside in a home or temporary directory.
* reading installation documentation
	* commonly located at:
		* `README/README.txt` : general documentation and installation instructions
		* `INSTALL` : installation instructions
		* `COPYING` : software license
		* `RELEASE-NOTES` : features and bug fixes included in the program version
		* `NEWS` : features and bug fixes included in the program version
		* `AUTHORS` : program creator(s) and contact information
	* Another reason to read these files is that a program author will often document any needed dependencies. Unlike installing with utilities like yum or apt-get, software dependencies are not automatically obtained and installed as part of this process. You have to do it manually.
* You’ll need the correct compilers (software that compiles programs) installed on your system for the source code installation to work properly. It’s typically helpful to go ahead and install these potentially needed development tools ahead of time. On a Red Hat–based system, type `yum groupinstall "Development Tools"`, and on a Debian-based system, type `sudo apt-get install build-essential` at the command line.
* compiling preparation
	* In this next basic step, you run a standard script that checks the system’s configuration and sets up preparations for the compiling step. The script that you run is `configure`, and it should be one of the files within the program’s installation file directory.
	* Typically, when you run the configure script, it will look for both optional and mandatory dependencies and settings. The script will check to see if you have the proper compiler(s) installed, check for any necessary program dependencies, check for any optional dependencies, and create a file called Makefile. It can do some other checking and setup as well.
	* The Makefile is created (or updated) by the configure script using what it finds on your system as well as the contents of the Makefile.in file stored within the program’s installation file directory.
	* Many configure scripts have a help utility that provides a list of options that you can use with the script. Type `./configure --help` at the command line to view these options.
* compiling the program
	* At this point, you are ready to compile the source code into binary. The command to do so is `make`.
	* The `make` command uses the Makefile file, which was either created or modified in the previous step, as a **guide**.
	* Now that the program’s source code is compiled, all that is left to do is to finish the installation process.
* completing installation
	* To complete the installation, you just need to run the `make install` command.
	* It typically creates any needed program directories, moves the program binaries and any supporting files, such as documentation and program libraries, to their proper locations, and sets proper permissions settings for the files.
	* Once the program is installed, you can remove the installation files’ directory and its contents. But you may want to hang onto the program’s tarball, because an `uninstall` program that may prove useful is often included if you need to uninstall this program. Also, consider storing the unpacked source code in a `/usr/src` subdirectory.
