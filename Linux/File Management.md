#### Commands
- `ls [options] [file="."]`
	- (1) list directory contents
	* `-l` = long listing: permissions, owner, size, modified date/time, and name
	* `-h` = file size in human readable format
	* `-a` = list all files including hidden files
	* `[-R/--recursive]` list subdirs recursively
- `exa`
	- (1) exa
* `touch [options] [file name(s)]` also changes timestamps
	* `-a` changes `access time` to current time
	* `-m` changes `modification time` to current time
	* `-d [string]` | `--date=[string]`
		* uses custom timestamp instead of current time
		* humand readable free format
		* examples in man page
			* `Sun, 29 Feb 2004 16:21:42 -0800`
			* `2004-02-29  16:21:42`
			* `next Thursday`
		* man page notes
			* `A date string may contain items indicating calendar date, time of day, time zone, day of week, relative  time,  relative date, and numbers.`
			* `An empty string indicates the beginning of the day.  The date string format is more complex than is easily  documented here but is fully described in the info documentation.`
	* `-t [time]`
		* uses custom timestamp instead of current time
		* `[[CC]YY]MMDDhhmm[.ss]`
* `cp [options] [src file(s)/dir(s)] [dest dir]`
	* `[-R/-r/--recursive]`
	* `[-v/--verbose]` explain what's being done
	* `[-s/--symbolic-link]` sym link instead of copy
	* `[-l/--link]` hard link instead of copy
	* `[-u/--update]` copy only when the `[src]` file is newer than the destination file or when the destination file is missing
	* `--attributes-only` no data, only attribs
	* `[-i/--interactive]` prompt before overwrite
	* `[-n/--no-clobber]` don't overwrite existing files
	* `--copy-contents` copy contents of *special files* when recursive
	* `-H` follow command-line symbolic links in `[src]`
	* `[-L/--dereference]` always follow symbolic links in `[src]`
	* `[-P/--no-dereference]` never follow symbolic links in `[src]`
* `mv [options] [src file(s)/dir(s)] [dest dir]`
	* `[-v/--verbose]` explain what's being done
	* `[-u/--update]` copy only when the `[src]` file is newer than the destination file or when the destination file is missing
* `mkdir`
	* `-p` makes parents if they don't exist
	* `-v` explain
* `rmdir` remove dirs if they're empty
	* `-p`
	* `-v`
* `rm`
	* `-v` explain
	* `[-r/-R/--recursive]`
	* `[-f/--force]` ignore nonexistent files and arguments, never prompt
	* `-i` prompt before **every** removal
	* `[-d/--dir]` remove only empty dirs
- `find [path] [options] [expression]`
	- (1) search for files in a directory hierarchy
	* `-type [fdl]` search files with `f`, dirs with `d`, and symlinks with `l`
	* `-name` means the query must be applied to the name of the file
	* `-iname` case-insensitive name
	* `-not` returns results that don't match
	* `-maxdepth [depth]`
	* `-mtime [number]` filter results based on modification time being grater than `current datetime - number * 24h`
	* `-size [pattern]`
		* pattern = `[ +-][0-9]*[bkMG]`
		* `[ +-]`
			* if there's nothing, it means the exact number
			* if `+` -> grater than
			* if `-` -> less than
		* `[bkMG]`
			* `b` byte
			* `k` kilobyte
			* `M` megabyte
			* `G` gigabyte
	* `-exec [command & args]` act on files filtered
		* `find . -type f -exec grep "lpi" '{}' \; -print`
			* `-print` prints output of exec
				* `-delete` also works but is **dangerous**
			* `'{}'` is for `find` match results
				* `''` are to avoid passing grep files that match `{}`
			* the `-exec` is terminated by `;` which is provided with a `\` to avoid shell interpretation
- `tar [op and options] [archive name] [file name(s)]`
	- (1) an archiving utility
	* short for tape archive(r)
	* `[op]eration`
		* only one is allowed and it's required
		* `[-c/--create]` new tar archive
		* `[-x/--extract]` extract the entire archive / or one or more files from it
		* `[-t/--list]` list content
		* `[-A/--catenate/--concatenate]` append archive to the end of another archive
			* `tar -A [archive] [archive]`
		* `[-d/--diff/--compare]` compares archive files with `[file...]`
			* `tar -d [-f archive] [options] [file...]`
		* `--delete` removes members from archive
			* `tar --delete [-f archive] [options] [member...]`
		* `[-r/--append]` appends files to the end of an archive
			* `tar -r [-f archive] [options] [file...]`
		* `[-u/--update]` appends file which are newer than the corresponding
			* `tar -u [-f archive] [options] [file...]`
			* this doesn't replace the same files, rather appends the new file alongside the old file.
	* `options`
		* `-v`
		* `[-f/--file][= ][archive-name]` specifies the archive file name, *which is weird*
		* overwrite control: tar action when extracting a file over an existing one on disk
			* `[-k/--keep-old-files]` don't replace existing files at all
			* `--keep-newer-files` for when the file on disk is newer
			* `--overwrite` overwrite away
			* `--recursive-unlink` recursively remove **all** files in the directory prior to extracting
			* `--remove-files` remove from disk after adding  to archive
- `bzip`
- `gzip`
	- (1) compress or expand files
- `cpio` wtf is this #todo 
- `dd if=[] of=[]`
	* (1) convert and copy a file
	* it's used for copying files
	* I think it's useful for manipulating files on the fly whilst copying
- `file`
	- (1) determine file type
- `chmod`
  - (1) change file mode bits
  - (2) change permissions of a file
- `ln` - (1) make links between files
- `pdfinfo` - (1) Portable Document Format (PDF) document information extractor (version 3.03)
- `ghostscript` - (1) Ghostscript (PostScript and PDF language interpreter and previewer)
- `calibre` - (1) calibre
- `cd`
- `git`
  - (1) the stupid content tracker
  - (3pm) Perl interface to the Git version control system
- `pstree` - (1) display a tree of processes
- `du` - (1) estimate file space usage
- `duf` - du modern alternative
- `mktemp`
  - (1) create a temporary file or directory
  - (3) make a unique temporary filename
- `less` - (1) opposite of more
- `more` - (1) file perusal filter for crt viewing
- `pwd` - (1) print name of current/working directory
- `rsync` - (1) a fast, versatile, remote (and local) file-copying tool
- `updatedb` - (1) update a file name database
- `broot`
- `fdisk` - (8) manipulate disk partition table
- `parted` - (8) a partition manipulation program
- `df` - (1) report file system disk space usage
- `mount`
  - (8) mount a filesystem
  - (2) mount filesystem
- `xz` - (1) Compress or decompress .xz and .lzma files
- `unxz` - (1) Compress or decompress .xz and .lzma files
- `xzcat` - (1) Compress or decompress .xz and .lzma files
- `lzma` - (1) Compress or decompress .xz and .lzma files
- `unlzma` - (1) Compress or decompress .xz and .lzma files
- `lzcat` - (1) Compress or decompress .xz and .lzma files
- `zip` - (1) package and compress (archive) files
- `unzip` - (1) list, test and extract compressed files in a ZIP archive
- `zipcloak` - (1) encrypt entries in a zipfile
- `zipnote` - (1) write the comments in zipfile to stdout, edit comments and rename files in zipfile
- `zipsplit` - (1) split a zipfile into smaller zipfiles
- `zipinfo` - (1) list detailed information about a ZIP archive
- `zipdetails` - (1) display the internal structure of zip files
- `gunzip` - (1) compress or expand files
- `zcat` - (1) compress or expand files
- `zless` - (1) file perusal filter for crt viewing of compressed text

#### Hard Disk Layout Design
* linux disk hierarchy
	* disk (physical) -> partition table -> partitions -> filesystem
* mounting
	Attaching the filesystem to a specific point in your system’s directory tree, called a mount point.

#### FHS
* FHS: The Filesystem Hierarchy Standard
	* basic directory structure
		* `/` (root) This is the root directory, the topmost directory in the hierarchy. Every other directory is located inside it.
		* `/bin` essential binaries, available to all users.
		* `/boot` files needed by the boot process, including the Initial RAM Disk (initrd) and the Linux kernel itself.
			* `/boot/efi`
		* `/dev` device files. These can be either physical devices connected to the system (for example, /dev/sda would be the first SCSI or SATA disk) or virtual devices provided by the kernel.
		* `/etc` host-specific configuration files. Programs may create subdirectories under /etc to store multiple configuration files if needed.
		* `/home` the exceptions are the superuser (root), which has a separate directory (/root) and some system users.
		* `/lib` shared libraries needed to boot the operating system and to run the binaries under /bin and /sbin.
		* `/media` user-mountable removable media, like flash drives, CD and DVD-ROM readers, floppy disks, memory cards and external disks are mounted under here.
		* `/mnt` mount point for temporarily mounted filesystems.
			* now known as `/media`
		* `/opt` application software packages.
		* `/root`
		* `/run` run-time variable data.
		* `/sbin` system binaries.
		* `/srv` data served by the system. For example, the pages served by a web server could be stored under /srv/www.
		* `/tmp` temporary files.
		* `/usr` read-only user data, including data needed by some secondary utilities and applications.
		* `/proc` virtual filesystem containing data related to running processes.
		* `/var` variable data written during system operation, including print queue, log data, mailboxes, temporary files, browser cache, etc.
			* `/var/tmp`
			* `/var/cache`
			* `/var/log`
			* `/var/lib/mysql` wtf?
		* [[Linux/Package Management#^shared-libraries-common-locations]]
	* temporary files
		* examples include the data of running processes, crash logs, scratch files from an autosave, intermediary files during a file conversion, cache files, etc.
		* `/tmp` according to the FHS, programs should not assume that files written here will be preserved between invocations of a program. The recommendation is that this directory be cleared (all files erased) during system boot-up, although this is not mandatory.
		* `/var/tmp` another location for temporary files, but this one should not be cleared during the system boot- up. Files stored here will usually persist between reboots.
		* `/run` this directory contains run-time variable data used by running processes, such as process identifier files (.pid). Programs that need more than one run-time file may create subdirectories here. This location must be cleared during system boot-up. The purpose of this directory was once served by /var/run, and on some systems /var/run may be a symbolic link to /run.

##### Searching for Files
* `find`
	* searching by attributes
		* `-user [username]` matches owner
		* `-group [groupname]` matches group owner
		* `-readable` matches files that readable by the current user
		* `-writable` matches files that are writable by the current user
		* `-executable` matches files that are executable by the current user
		* `-perm NNNN` matches permissions in octal mode
	* searching by time
		* `a` accessesd, `c` changed, `m` modified
		* `-[acm]min [N]`  where N is in minutes
		* `-[acm]time [N]` where N is in 24hours (number of days before)
* `locate` and `updatedb`
	* `updatedb` creates a database of files
		* `/var/lib/mlocate.db`
		* `/etc/updatedb.com`
			* `PRUNEFS=` excludes filesystems
			* `PRUNENAMES=` exclude by dir name
			* `PRUNEPATHS=` exclude by full path
	* `locate [pattern(s)]`
		* `-i` case insensitive
	* `-e` will make it check if the file still exists before displaying it

#### Cryptography
* `sha256sum`
	* `sha256sum [file]` will produce sign
		* syntax of sign is `[hash number] [filenme]`
	* `sha256sum -c [file]` will check sign based off of `[filename]` stored in the sign. so the command looks for the file in the current directory and checks it.
* `od` octal
	* `od [file]`
		* first column is the offset for the rest of the columns in each line.
	* `od -x [file]` hexadecimal format
	* `od -c [file]` printable char format
	* `-An` removes offset column 

#### Files
* types
	* regular files
	* directories, which contain other files
	* special files, which are used for input and output
* `[-dc][r-][w-][x-][r-][w-][x-][r-][w-][x-]`
	* example: `-rw-r--r--`
	* the first char `[-dc]` is either a file `-`, a directory `d` or a special file `c`
	* a group of `[r-][w-][x-]` gives permissions toward an operator entity.
		* each one tells if the corresponding permission was give or not.
			* read perm `[r-]`, write perm `[w-]`, and execute perm `[x-]`
		* the first group is towards #todo 
		* the second group is towards #todo 
		* the third group is towards #todo 
* globbing and wildcards
	* `*` zero or multiple chars of any value
	* `?` one char of any value
	* `[a-z]` a char with value of lowercase letter
		* also works with `[A-Z]` and `[0-9]`
		* these can be combined in a single bracket
	* `[aef]` a char with value of `a`, `e`, or `f

### Permissions
* every file on disk is owned by a user and a user group and has three sets of permissions:
	* one for its `owner`
	* one for the `group` who owns the file
	* one for everyone else
* `ls`
	* `ls -l`
		* first col: `[file type][u|owner perms][g|group perms][o|others perms]`
			* `file type`
				* `-` normal file
				* `d` directory
				* `l` symbolic link
				* `c` character device
				* `b` block device
					* This file stands for a virtual or physical device, usually disks or other kinds of storage devices.
				* `s` sockets
					* Sockets serve as “conduits” passing information between two programs.
			* each `perms` is a three character sequence
			* `o|others perm` is also known as `world permissions`
		* 3rd and 4th column are `user` and `group` that own the file
		* 2nd col shows the number of hard links 
	* `ls -l -d`  shows info about the directory itself
* permissions
	* char sequence
		* `r(4)` read
			* for directories, this does not imply the permission to access files within that directory.
		* `w(2)` write
			* for dirs it means permission to create, delete a file (I think not edit?). Keep in mind these don't work without a dir/file execute permission.
		* `x(1)` execute
			* for dirs, it means entering a directory, but not listing them. for that `r` is needed.
		* `-(0)` no permissions
	* checking
		* first, system checks if the user is the `owner` of the file. If not, it checks if the user belongs to the `group owner` of the file. Again, if not, it will consider the user as `others`.
		* based on which item the user is associated with by the system, it will pick the permissions accordingly.
	* `chmod [options] [which perms to change] [file/dir]`
		* for dirs, chmod only changes dir perms. add `-R` to do it recursively.
		* `[which perms to change]` has to modes
			* symbolic mode
				* the first char indicates whose perms you will alter.
					* `u` user
					* `g` group
					* `o` others
					* `a` everyone
				* then you need to tell it what to do
					* `+` grant perm
					* `-` revoke perm
					* `=` set it to specific value
				* lastly, you specify which permissions you wish to act on `rwx`
				* examples
					* `g+w` = for the `group`, `grant`, `write` permissions
					* `u-r` = for the `user`, `revoke`, `read` permissions
					* `a=rw-` = sets permission `rw-` for `everyone`
					* `u+rwx,g-x` = for the `user`, `grant`, `all` permissions **and** for the `group`, `revoke`, `execute` permissions
						* you can pass multiple statements by seperating them using a comma `,`
			* octal mode
				* this is a 3 digit string, each one representing (in order) `user`, `group`, and `others` permissions.
				* the value of each digit should be summed up by the octal value of each perm char
					* `rwx = 7`, `--- = 0`, `r-x = 5`
				* if a digit is `odd`, it definitely has `execute` permissions.
			* octal mode is more specific yet short, but symbolic mode helps if you just want to flip a switch.
		* `options` #todo 
	* `chown [username]:[groupname] [file]`
		* useful to modify the owner of the file or directory
		* if you only want to change one of `user` and `group`, the other one can be omitted.
		* `chgrp` can alternatively be used to change the group owner
		* **unless** you are root, you cannot change ownership of a file to another user or group  you don't belong to. if you try, you'll get `Operation not permitted.`
	* default permissions
		* default file permissions: `-rw-r--r-- = 644`
		* default dir permissions: `drwxr-xr-x = 755`
		* stored in `user mask`
			* `umask [-S]` shows default
			* for further info refer to page:496
	* special permissions: for further info refer to doc page: 497
		* Sticky bit: for dirs, if true, users can only operate on their own files
		* Set GID bit: something about group inheritance
		* Set UID: again, something about user inheritance
* query groups
	* `getent group` will list all groups available on the system
	* `groups [username]` will list the groups that `username` belongs to
	* `sudo groupmems -g [group] -l` will list the users that belong to `group`

> [!Question] ChatGPT
> **Explain sticky bit in linux file/dir permissions**
>
> The sticky bit is a special permission in Linux file and directory permissions that has a unique and specific purpose. It's represented by the letter "t" or "T" in the permission string of a directory, depending on whether the execute permission is set for others. For files, the sticky bit doesn't have any effect.
>
> When the sticky bit is set on a directory, it influences the behavior of file deletion within that directory, particularly in a shared environment where multiple users have write access to the directory.
>
> The primary use case for the sticky bit is in directories that are used for temporary file storage or public sharing. For example, the `/tmp` directory often has the sticky bit set, ensuring that users can only delete or modify their own temporary files while preventing them from affecting files owned by other users.

> [!Question] ChatGPT
> **explain the suid bit in linux file permissions**
> 
> The Set User ID (SUID) bit is a special permission in Linux file permissions that is represented by the letter "s" in the permission string of an executable file. When the SUID bit is set on an executable file, it allows the user who executes the file to temporarily assume the ownership privileges of the file's owner. In other words, it allows the executable to be executed with the permissions of the file owner, even if the user executing the file does not have those permissions.
> 
> When the SUID bit is set on a directory, any new files or directories created within that directory will inherit the owner of the parent directory, rather than the user who created them. This can be useful for enforcing a specific ownership structure in shared directories.
> 
> It's important to note that the SUID bit only works for executable files and programs, not for scripts or interpreted files (like shell scripts). Additionally, SUID does not affect group or other permissions, so the file's permissions still apply in those contexts.
> 
> Due to security considerations, the use of the SUID bit needs to be carefully controlled. Allowing users to execute files with elevated privileges can potentially lead to security vulnerabilities if not properly managed. Therefore, system administrators need to carefully assess the risks and benefits of using the SUID bit and only apply it to files and programs where it's truly necessary.
#### Checking For Files with the SUID and SGID set
* `find`
	* find files having the special permission exclusively
		* `-perm [numeric-value/symbolic-value]`
	* find files having the special permission and other permissions
		* `-perm -[numeric-value/symbolic-value]`
	* find files having either of the special permission (and other permissions)
		* `-perm /[numeric-value/symbolic-value]`

### Hard/Symbolic Links
* symlinks
	* aka soft links
	* points to `target`
	* if the target gets deleted, pointer will still exist but won't work because it now points to nothing.
	* `ln -s [target] [symlink]` creates a symlink
	* in appearance, symlinks show all permissions for everyone. but in practice they use the permissions of the target.
	* always specify target path because the string is directly stored as target without further processes.
* hard links
	* they're not duplicates
	* they're an additional entry in the filesystem pointing to the same place (inode) on the disk.
		* An inode is a data structure that stores attributes for an object (like a file or directory) on a filesystem. Among those attributes are permissions, ownership and on which blocks of the disk the data for the object is stored. Think of it as an entry on an index, hence the name, which comes from “index node”.
	* `ln [target] [link name]` creates a hl
	* if you change the file through one *name*, the file will be changed for all names.
	* if you delete one name, the rest will still work
	* you can't tell a hard link from an original file. practically at least.
	* every hard link to a file increases the `link count` of the file
		* link count is 1 by default
			* directories have a count of 2
	* `ls -li`
		* first col is inode
		* second col is link count

### Backup
* Introduction
	* Just having backups is useless if there are no plans in place for recovering the data.
	* Consider starting the data backup planning process with this question to company leaders, “Just how valuable is your data?”
	* Because they are often used interchangeably, confusion may exist between the terms ***backup*** and ***archive***.
		* A backup is a copy of the data that is used for safeguarding the original data.
		* An archive is either a copy of the data or the actual data itself, typically put on less-expensive media and moved into long-term storage, which is often environmentally controlled and in a different physical location.
	* When developing a data backup plan, you should consider several important items. These items will allow you to determine a budget and make decisions on what methods to include in your backup plan. Typically, these important items include the following:
		* Data categories
			* These involve cataloging your data into groups in order to determine value.
			* For example, you will have a system data category that covers data necessary for system operation. You may also have data categories such as customer payment information.
		* Value of each data category
		* Maximum acceptable data inaccessibility time
			* Typically, measurements such as recovery time objective (RTO) are used.
			* RTO states the maximum tolerable length of time that data (or a computer) can be unreachable.
	* Keep in mind that whole books have been written on creating backup and recovery strategies.
	* When the previous key items have been determined, research and decisions on the following backup and recovery topics can take place:
		* Backup media
		* Backup storage and rotation solutions
		* Backup types
		* Data recovery
		* Directories to backup
		* Software solutions (network and local)
		* When you are developing this plan, none of these topics can be viewed in isolation. For example, the backup media that you select will affect your software and storage solution decisions. And, of course, the best backup plan is one that is reviewed and tested.
* Backup Strategy Development
	* Backup Media
		* There are many factors to consider when you are looking at the media available for your backup strategy, such as *portability*, *longevity*, and *cost*.
		* **Magnetic Tape**
		* **Optical Disks**
		* **HDDs**
		* **SSDs**
	* Backup Types
		* *Backup Types* refer to the different methods for backing up data that has been modified.
			* Full
				* A copy of all data, ignoring its modification date, to another set of media.
				* This backup type’s primary advantage is that it takes a lot less time than other types to **restore** a system’s data.
				* However, not only does it take longer to create a full backup compared to the other types, but it also requires more storage.
			* Incremental
				* It makes a copy of only data that has been modified since the last backup operation (any backup operation type). Typically, a file’s modified time stamp is compared to the last backup type’s time stamp.
				* This backup type takes a lot less time to create than the other types, and it requires a lot less storage space.
				* However, the data restoration time for this backup type can be significant, because you first have to restore the full backup and then restore each incremental backup.
				* For optimization purposes, you must complete a full backup periodically.
			* Differential
				* It makes a copy of all data that has changed since the last full backup. It could be considered the happy medium between full and incremental backups.
				* This backup type takes less time than a full backup but potentially more time than an incremental backup.
				* It requires less storage space than a full backup but more space than a plain incremental backup.
				* Also, restoration takes a lot less time using differential backups than incremental backups, because only the full backup and the latest differential backup are needed.
				* For optimization purposes, you must complete a full backup periodically.
			* Incremental vs Differential (as per ChatGPT)
				* In summary, incremental backups only back up changes since the last backup (whether it was full or incremental), while differential backups back up changes since the last full backup.
				* Incremental backups only back up the data that has changed since the last backup, regardless of whether it was a full backup or an incremental backup. For example, if you perform a full backup on Monday and an incremental backup on Tuesday, the incremental backup will only include the data that has changed since Monday's backup. On Wednesday, if you perform another incremental backup, it will only include the data that has changed since Tuesday's backup.
				* Differential backups, on the other hand, back up all the data that has changed since the last full backup. So, using the same example as before, if you perform a full backup on Monday and a differential backup on Tuesday, the differential backup will include all the data that has changed since Monday's full backup, regardless of whether it was previously included in an incremental backup.
			* Snapshot
				* It is considered a hybrid approach, and it is a slightly different flavor of backup.
				* First, the backup software makes a full data copy to backup media, such as a SAN (Storage Area Network), and then the software uses pointers, such as hard links, to create a reference table linking the backup data with the original data.
				* The next timeyou make a backup, instead of a full backup the backup software performs an incremental backup (only modified or new files are copied to the backup media), and the software copies and updates the pointer reference table.
				* This saves space, because only modified files and the updated pointer reference table need to be stored for each additional backup.
				* The snapshot backup type described here is a copy-on-write snapshot. There is another snapshot flavor called a split-mirror snapshot, where the data is kept on a mirrored storage device. When a backup is run, a copy of all the data is created, not just new or modified data.
				* With a snapshot backup, you end up with the ability to go back to any point in time and do a full system restore from that point.
				* It also uses a lot less space than the other backup types.
				* In essence, snapshots simulate multiple full backups per day without taking up the same space or requiring the same processing power as a full backup type would.
	* Data Recovery
		* The time comes when data needs to be restored. No one really likes to think about it, but it does happen. Files are accidently deleted, disk drives fail, and grand disasters happen. Like death and taxes, data recovery is inevitable.
		* Data restoration needs to be an integral part of your backup plan. The specific details are heavily dependent on the other plan choices you make. However, you need to plan for each one of the following data-restoration scenarios:
			* **Single or Multiple Data File Recovery**: This is the most common data-recovery scenario that occurs on a system. Users accidently delete their files. Other users ruin data within their files. It’s convenient if you can provide a solution that allows users to recover these files themselves and provide up-front education on how to avoid these types of scenarios.
			* **Full Partition or Disk Recovery**: Hopefully, you have proper structures in place, such as RAID disks, to avoid these kinds of problems, but they still can happen. Your RTO measurements will play a big factor in the recovery plan for this scenario.
			* **System Recovery**
				* This is typically your worst-case situation. The entire system and all its data must be restored.
				* There are two flavors of this restore:
					* You can do a full system restore, which involves booting the OS from a live distribution and then restoring all of the files needed for the Linux OS to work (all of the system configuration files and all the data files).
					* Another flavor is the configuration/data restore. This entails first reinstalling Linux and then restoring the system configuration files and all of the data files.
	* Directories to Backup Up
		* It’s a good idea to periodically document all of the packages installed on the system. You can create this documentation using package utilities, such as rpm or dpkg. This documentation is primarily for your own reference, just in case you need to know what packages were installed due to a data recovery failure or some other terrible data disaster. It’s always better to have too much documentation instead of too little.
		* Refer to `directories-to-consider-for-backup-plans-table`
	* Backup Software Solutions
		* Amanda
			* Amanda (also called Amanda Network Backup) is an open-source software backup solution that runs on a Linux host machine.
			* At its core are command-line utilities, such as `dump` and `tar`.
			* It provides the ability to back up data from multiple-OS platforms to a variety of media that include disk and tape, as well as to the cloud.
		* Bacula
			* Bacula is also an open-source software backup solution that is released under the AGPL v3 license.
			* It has five primary components (Director, Console, File, Storage, and Monitor services), which allow flexibility in how you manage your network backups, including web, GUI, and text-based interfaces.
			* It provides the ability to back up data from multiple-OS platforms to a variety of media that include disk and tape, as well as to the cloud.
			* However, the Bacula project doesn’t recommend that you use its product if you are not experienced at using command-line options, such as `tar` and `dump`, due to its **difficulty in setup**. Nevertheless, there are many tutorials on the Web.
		* Bareos
			* Bareos is a fork of the Bacula backup software. It is open-source and also released under the AGPL v3 license.
			* The Bareos backup solution is nearly a clone of Bacula. It has the same primary components as well as the various interfaces.
			* Bareos does have a few additional features, including the ability to install the Director component on a Windows system. In addition, the Bareos developers have created their backup solution to protect your backup data following user-specified rules. This feature may make it difficult to reuse backup tapes with Bareos, and therefore the project developers recommend using another solution for this particular situation.
		* [Duplicity](http: //duplicity.nongnu.org/)
			* It can be used from the command line or via a GUI front end called `deja-dup`.
			* It typically comes preinstalled on Ubuntu, and it is the core behind the Unity Backups icon.
			* It provides the ability to back up data to a variety of media, as well as to the cloud. It allows you to encrypt your backups using GNU Privacy Guard (GPG).
		* [BackupPC](http://backuppc.sourceforge.net)
			* BackupPC is another open-source software backup solution, which is released under the GNU GPL.
			* It can back up Linux, Unix, Mac OS X, and Windows machines, and it supports disk backup media.
			* BackupPC has a web-based front end and uses `rsync` and `tar` at its core.
		* `cpio`
		* `dd`
		* `dump/restore`
		* `rsync`
		* `star (tar with SELinux)`
		* `tar`
* Performing Backups
	* If you have planned properly, backing up your data will occur on a regular and potentially automated basis. But occasionally you will need to conduct unscheduled data backups.
	* [`tar`](https://www.gnu.org/software/tar/manual/)
		* tar: Tape Archiver
		* Using the `tar` command, you start out with several files that need to be backed up. You end up with a copy of those files, stored in a single file, called an *archive file*. If the archive file is compressed using a data compression utility, the compressed archive file is called a *tarball*.
		* refer to `man tar` and `info tar`
		* also refer to page 61 (LPIC-2 Study Guide)
		* The tar command views full and incremental backups in levels. A full backup is a one that includes all of the files indicated, and it is considered a level 0 backup. The first tar incremental backup after a full backup is considered a level 1 backup. The second tar incremental backup is considered a level 2 backup, and so on. You can force the tar command to do a full backup with a level n snapshot file via the --level=0 option.
	* `rsync`
		* The rsync is a nice utility that allows you to perform backups to disk drives locally or to those connected over a network.
		* Not only it is lightning fast, but you can easily encrypt your file transfers tunneling through OpenSSH.
		* `man rsync`
		* You can do much more with rsync than just partial file backups. You can also set up full backups. In addition, employing hard links lets you use rsync for incremental backups as well. (Use your favorite search engine to find articles on using rsync and hard links to create incremental backups for your data.)
	* `dd`
		* It’s primarily used to create a low-level copy of a hard drive, and it is often used in digital forensics.
		* The output-device is either an entire drive or a partition. The input-device is the same.
		* `man dd`
	* Shell Script Automation
		* Once you have your backup scripts working and tested, consider running them with cron (or anacron) to ensure that backups are never forgotten. Since backups are a popular shell script, use your favorite search engine to find various examples located on the Internet. You may be able to find something that will meet your needs with only a few modifications.

> directories-to-consider-for-backup-plans-table (table 2.1 LPIC-2 Study Guide)

| Directory | Contents | Backup Consideration |
| :- | :- | :- |
| `/bin` | user utility programs. alternatively `/usr/bin` | full system restore: yes, configuration/data restore: no |
| `/boot` | holds config files used during boot process | full system restore: only for documentation purposes (e.g. comparing boot files to restored boot files), configuration/data restore: no |
| `/dev` | contains device files | full system restore: only if distro is configured to use static dev files, configuration/data restore: no |
| `/etc` | system config files | yes |
| `/home` | user's home dir | yes |
| `/lib` | stores kernel modules and shared libraries | full system restore: yes, configuration/data restore: no |
| `/lost+found` | files saved during unplanned system shutdowns | no |
| `/media` | temporary mount dir for removable media devices | no |
| `/mnt` | same as `/media` | no |
| `/opt` | third-party apps | yes |
| `/proc` | virtual filesystem for running processes and kernel info | no |
| `/root` | the root user's home dir | yes |
| `/run` | a tmpfs mounted early during the boot process and used by various tools | no |
| `/sbin` | system administrator utility programs | full system restore: yes, configuration/data restore: no |
| `/srv` | system-specific files for various services | yes |
| `/sys` | virtual filesystem stores information concerning and allows modification of connected hardware devices | no |
| `/tmp` | temporary files | no |
| `/usr` | stores binaries, documentation, source code, libraries, etc | yes |
| `/var` | contains log, lock, spool, mail, and temp files | yes (some subdirs e.g. `/var/run` can be excluded) |
