### Operating The Linux Filesystem
* Data is kept as ones and zeros on storage media, such as disk drives and DVDs. A filesystem bridges the gap between the ones and zeros stored on the media and the files you work with in your applications. Managing a filesystem includes providing access to the stored data as well as tuning, monitoring, and repairing filesystems in order to improve access times and protect the data.
* filesystem structures
	* Typically, *partitioning* is logically dividing a storage media device into individual sections called partitions. Be aware, however, that a single partition can span a whole device, as well as multiple devices. Logical volume management, allows multiple partitions to be logically grouped together into one partition, called a *volume*. Partitioning is accomplished via either GUI or command-line utilities, such as `parted`, `fdisk`, and `gdisk`.
	* High-level formatting is often just called formatting or making the filesystem. This formatting is accomplished using utilities such as `mkfs`.
	* When a partition or volume is formatted, several structures are put into place, depending on the filesystem type selected. One partition area holds the actual *file data*. The other area(s) hold structures containing items such as *filesystem metadata*, *file metadata*, *journal files*, and so on.
	* File metadata is stored in an *inode table*. When a file is created on the partition or volume, a new entry in the inode table is created. The inode table is a table of index numbers, called inodes. Typically, an inode is a number uniquely assigned to a file when it is created. (There are exceptions to this, such as when a hard link is created to a file. The hard link file and the original file share an inode number.) The inode and its assigned file’s metadata, such as *permissions*, *ownership*, and *pointers to the various file data locations*, are stored in the inode table.
	* A file’s name is not stored in the inode table. A file’s name is stored in its directory. A directory is actually a file that contains a table. The table has metadata on each file stored in that directory. Each file’s name and its associated inode number are listed within the directory table.
* filesystem types
	* A filesystem determines how the files are handled on physical media. Each type has its own unique methods for *accessing*, *updating*, and *protecting data integrity*. Thus, your filesystem type choice is an important selection.
	* Filesystems can be categorized in many different ways, such as to *how they protect data integrity*, the *physical medium on which they can be used*, *their original target operating system*, and so on.
	* native linux filesystem
		* A native Linux filesystem is one that was originally designed to be used on Linux. Table 4.1 (LPIC-2 Study Guide) shows filesystems, in alphabetical order, that fall into this category.
		* There's a difference between `Journaling` and `COW (Copy-On-Write)`, both of which are implementations for data intergrity. Refer to page 143 (LPIC-2 Study Guide) for further explanation.
		* The ext filesystem types are sometimes written with “fs” added to their name to indicate that they are a filesystem type. For example, ext3 can be written as ext3fs.
	* non-native linux filesystems
		* Table 4.2 (LPIC-2 Study Guide) shows several filesystems, in alphabetical order, that fall into this category.
* making a filesystem
	* The primary tool to format a filesystem is `mkfs`, and you need super user privileges to use it. The `mkfs` utility is actually a front end to various other utilities used for each filesystem type.
	* You can also use the `blkid` utility to check the filesystem type.
* attaching a filesystem
	* Linux uses a method to store files within a single directory structure called a virtual directory. At the base of this virtual directory is the root directory (/), and directories and files beneath the root directory are listed based on the directory path. You can attach filesystems to the virtual directory structure either temporarily or persistently, depending on your present needs. After you’ve attached a filesystem to the virtual directory structure, you can store and access data on that filesystem.
	* Attaching a filesystem to the Linux virtual directory is called *mounting*, and temporary mounting is done via the `mount` command.
	* You can easily determine the filesystem types supported by your Linux distribution’s kernel by viewing the `/proc/filesystems` file.
	* The `lost+found` directory is used for recovering files on ext2, ext3, and ext4 filesystems. If a file residing on this filesystem is not closed properly, such as when a system crash occurs or a software bug is encountered, it is stored in this directory.
	* If any files exist in the *mount_point* prior to mounting the filesystem, they will no longer be accessible after the filesystem is mounted.
	* The mount command, when used with no options or parameters, pulls the data it displays directly from the `/etc/mtab` file. The `/etc/mtab` file contains a list of all of the currently mounted filesystems.
	* The data in the files `/etc/mtab` and `/proc/mounts` is nearly identical, with a few exceptions. First, if a filesystem was attached with mount using the `-n` option, the `/etc/mtab` file will not contain information on that filesystem. Also, the `/proc/mounts` file is typically more up to date than `/etc/mtab`.
	* mount `-o` option allows you to mount the filesystem with one or more comma-separated opts. A few of the more popular opts selections are listed here:
		* `check=none` mounts the filesystem without performing an integrity check.
		* `exec` permits binary file execution.
		* `group` allows a non–super user to mount the filesystem, if the user belongs to the specified group.
		* `owner` allows a specified non–super user to mount the filesystem.
		* `ro` mounts the filesystem as read-only.
		* `rw` mounts the filesystem as read-write.
		* `sync` forces filesystem buffers to write from memory to the media for every write to the filesystem. No effect on XFS.
		* `user` allows a specified non–super user to mount the filesystem.
		* `users` allows all users to mount the filesystem.
* detaching a filesystem
	* You can detach a filesystem from the Linux virtual directory structure with the `umount` command.
	* You can use the `lsof` or `fuser` command to determine what is keeping the filesystem busy.
* A handy utility to use with removable media is the `sync` command. The `sync` command allows you to “flush” the filesystem buffers. In other words, any filesystem metadata updates residing in memory are written to the filesystem structures on the media. The `sync` utility forces the data commitment process to take place immediately. This allows you to detach removable media safely from the directory structure without worrying about corruption. The sync command is used to flush filesystem buffers. The `sync` utility provides an exit status, which you can view using the echo $? command. A zero (0) indicates all is well, whereas a one (1) indicates that a problem has occurred.
* attaching a filesystem persistently
	* Instead of manually attaching your filesystems after every system reboot, you can have them attached by the system when it boots. This is done via a record placed in the `/etc/fstab` file, which is appropriately named the *Filesystem Table*.
* viewing attached filesystems
	* A simple command to start with is the `mountpoint` command. It requires no super user privileges. Just type in `mountpoint [directory_reference]` at the command line, and if you receive the message `"is a mount point"`, then a filesystem has been mounted at that particular directory location.
	* With the `blkid` command, you can view the various block devices and their attributes. Super user privileges are not required to see some of the information; however, accounts without super user privileges receive unverified cached information or none at all.
	* The `lsblk` command can also be a helpful utility. It works in a similar manner to the `blkid` command in that it also displays block device information. Since some of its options pull information from the `blkid` command, it’s best to have super user privileges when employing it.
	* Another utility that you may find helpful is the `e2label` command. With this utility, you can view any filesystem label for an ext2, ext3, or ext4 filesystem.
	* The `findfs` utility can also be helpful in managing your filesystems. It allows you to view the block device associated with a particular UUID or label. The `findfs` command does not require super user privileges. However, unfortunately, when typing in a filesystem UUID for the `findfs` command, the shell’s tab command completion is not available.
	* `findmnt` displays mounted filesystems in a tree format.
	* `df` displays mounted filesystem disk space usage, and it includes the filesystem’s mount point.
	* `mount` displays mounted filesystems, and it includes the filesystem’s mount point.

#### Mounting/Unmounting Filesystems
* manually mount a filesystem
	* `mount -t [type] [device] [mountpoint]`
		* `-r or -ro` mounts as read-only
		* `-w or -rw` mounts as writable
	* `type`: type of filesystem being mounted
	* `device`: the name of the partition containing the filesystem `e.g. /dev/sdb1`
	* `mountpoint` this *directory* must exist
	* e.g. `mount -t exfat /dev/sdb1 ~/usb-flash`
* `mount` will print all the currently mounted filesystems
	* `mount -t [type]` will filter output
		* `mount -t ext4`
* manually unmount
	* `umount /dev/sdb1` and `umount ~/usb-flash` are interchangable
		* notice that its Umount!
		* `-a` will unmount all filesystems listed in `/etc/fstab`
		* `-f` force unmount: useful when a mounted remote filesystem is unreachable
		* `-r` if it can't be unmounted this will make it read only
* dealing with open files
	* common err when unmounting: `target is busy`
* `/etc/fstab` mounting on bootup
	* syntax: `[filesystem] [mountpoint] [type] [options] [dump] [pass]`
		* `filesystem`: the device; or instead you can use `UUID` or `label` of the partition.
		* `dump` #todo page: 470 (LPIC1)
		* `pass` page: 470 (LPIC1)
		* `options` will be passed to mount
			* `atime(default) & noatime`
				* to enable or disable the automatic editing of `access time` attribute of files. if disabled, I/O operations would be faster.
			* `auto & noauto` whether the filesystem can (or can not) be mounted automatically with mount -a.
			* `defaults` this will pass the options rw, suid, dev, exec, auto, nouser and async to mount
			* `dev & nodev` whether character or block devices in the mounted filesystem should be interpreted.
			* `exec & noexec` allow or deny permission to execute binaries on the filesystem.
			* `user & nouser` allows (or not) an ordinary user to mount the filesystem.
			* `group` allows a user to mount the filesystem if the user belongs to the same group which owns the device containing it.
			* `owner` allows a user to mount a filesystem if the user owns the device containing it.
			* `suid & nosuid` allow, or not, SETUID and SETGID bits to take effect.
			* `ro & rw` mount a filesystem as read-only or writable.
			* `remount` ?
			* `sync & async` ?
* using `UUIDs` and labels is a good idea to prevent colisions by devices. both are specified when the filesystem is created and will not change, unless the filesystem is destroyed or manually assigned a new label or `UUID`.
* `lsblk` find info on filesystems
	* `lsblk -f /dev/sdb1`
* `systemd`
	* Among many other tasks, systemd can also be used to manage the mounting (and automounting) of filesystems.
	* to use it create config in `/etc/systemd/system`
		* the config file is called a *mount unit*, and it ends with `.mount`
			* config file must have the same name as the mount point. So for `/mnt/external` it would be `mnt-external.mount`
			* What= `/dev/disk/by-uuid/[volume uuid]`
			* Options, are the same as fstab.
			* WantedBy: used for dependency management. In this case, we will use multi-user.target, which means that whenever the system boots into a multi-user environment (a normal boot) the unit will be mounted.
			```cfg
			[Unit]
			Description=External data disk
			
			[Mount]
			What=/dev/disk/by-uuid/56C11DCC5D2E1334
			Where=/mnt/external
			Type=ntfs
			Options=defaults
			
			[Install]
			WantedBy=multi-user.target
			```
		* after that you need to restart the systemd with `systemctl daemon-reload` and then start the unit with `systemctl start mnt-external.mount`
		* for automount refer to page: 476 #todo 

> [!Question] ChatGPT
> **Explain bind mount and how is it different from a normal mount?**
>
> A bind mount in Linux is a mechanism that allows you to attach or "bind" an existing directory or file from one location in the file system to another location. This effectively creates an additional reference to the same data, allowing the content to be accessible at multiple locations simultaneously. Unlike other types of mounts, bind mounts do not involve different filesystems; they simply make the same filesystem available at two different paths within the directory tree.
>
> Here's how bind mounts work and how they differ from normal (or "regular") mounts:
> 
> **Bind Mount:**
> - A bind mount creates a link between an existing directory (or file) and a target directory. Changes made to files within the bind-mounted directory are reflected immediately at both the source and target locations.
> - Bind mounts are commonly used to:
>   - Share data between containers in containerization platforms like Docker.
>   - Provide access to the same data at multiple paths for applications or users.
>   - Remount a directory with different mount options while maintaining access to the original data.
>
> **Differences from Normal Mount:**
> 1. **Filesystems vs. Directories:**
>    - In a normal mount, a new filesystem is attached to a directory, and the content of that filesystem is accessible through the directory. The original content of the directory is hidden while the new filesystem is mounted.
>    - In a bind mount, an existing directory (or file) is attached to another directory. Both the original content and the bind-mounted content remain accessible.
>
> 2. **New Mount Point vs. Additional Link:**
>    - A normal mount creates a new mount point in the directory tree, effectively hiding the content of the directory where the filesystem is mounted.
>    - A bind mount doesn't create a new mount point; it attaches the source directory or file to an existing directory, allowing both locations to access the same data.
>
> 3. **Filesystem Type:**
>    - In a normal mount, you usually mount a different filesystem type, such as ext4, NTFS, or FAT, to a directory.
>    - In a bind mount, you're mounting the same filesystem (usually the same type) at a different location.
>
> 4. **Impact on Original Content:**
>    - In a normal mount, the original content of the mount point becomes hidden while the new filesystem is mounted.
>    - In a bind mount, the original content of the source directory remains accessible and visible through the bind-mounted path.
>
> In summary, bind mounts provide a way to create an additional reference to existing data within the filesystem without involving new filesystems. This allows for sharing data between different parts of the filesystem or between containers without duplicating the data. Normal mounts, on the other hand, involve attaching a new filesystem to a directory, effectively replacing the original content of that directory with the mounted filesystem.
#### Additional Filesystem Topics
* memory-based filesystems
	* A topic that deserves some special attention is virtual or memory-based Linux filesystems. These filesystems are unique in that their data resides within system memory, but you can view their data using their mount points.
	* You’ll often find these memory-based filesystems mounted at `/dev`, `/proc`, `/sys`, and `/run` or one of their subdirectories.
	* Though they show no size information in their file listings.
* swap filesystems
	* The term swap filesystem is really inaccurate. A swap partition doesn’t hold a filesystem, but instead it is a special location on the disk that acts as the system’s swap space (also called virtual memory).
	* Typically, a swap partition is created, formatted, and added to the /etc/fstab configuration file at system installation. However, you may need to create and manage additional swap partitions, for example, if you increase your system’s RAM.
	* You aren’t limited to swap disk partitions. You can set up your swap space on a logical volume and increase the size as needed using logical volume resizing tools. You can also create a file using the dd command to make it the proper size and then turn it into a swap file to be used as swap space.
	* A couple of useful utilities are available for checking your current swap space. Most likely, you’re already familiar with the `free` command. But you may not be familiar with using the `swapon` command for swap space statistics
		* On some distributions, you can get the same information from the `/proc/swaps` file.
		* If desired, the new swap partition’s use priority can be changed to a different priority using the `swapon` command. You must first use the `swapoff` command on the swap partition before changing its priority.
		* If you want to move your system to a new swap space, do not use the `swapoff` command on the current swap space until your new swap partition is set up and ready to go. Otherwise, you may end up with a hung system.
	* You can have more than one system swap space. In fact, in many cases, it is desirable to do so. The Web has some great discussions on this performance issue. Google `purpose of multiple Linux swap partitions`.
	* The `mkswap` command is used to “format” the partition into a swap partition.
	* If all is well with your new swap partition, you should add it to the `/etc/fstab` file so that it will be persistent. You can closely mimic the current swap partition’s record settings, but be sure to change the partition name to your new swap partition.
* network-based filesystems
	* Some filesystems are not locally attached, but instead they physically reside on network-attached storage media. These network-based filesystems are shared across the network.
	* Filesystems that can be included in this category are NFS and Common Internet File System (CIFS), which is implemented via Samba and is called SMBFS on older systems.
	* You can stretch the filesystem definition a bit to include Network Attached Storage (NAS), which has entire Linux distributions available to implement it, such as *OpenMediaVault*. NAS typically uses NFS or CIFS at its core. Whilewe’re stretching definitions, let’s include *Storage Attached Networks* (SANs). You can implement a SAN with the iSCSI protocol on Linux.
* auto-mounting
	* Many distributions automatically mount removable media, such as USB flash drives and DVDs, to a Linux virtual directory. *Dynamic device management* aka `udev` (related to kernel), is responsible for handling these devices’ auto-mounting functions.
	* AutoFS
		* Another type of auto-mounting is geared to network-based filesystems. The automounter service, AutoFS, can manage NFS filesystems’ auto-mounting functions, as well as those of other network-based filesystems.
		* You can put NFS filesystems in the `/etc/fstab` configuration file so that they are automatically mounted upon system boot. However, in some cases, the system can experience performance problems using this arrangement. By allowing AutoFS to manage mounting NFS filesystems, you avoid these problems.
			* For example, one way that AutoFS helps with system performance is that NFS filesystems are mounted when they are accessed instead of at system boot time. This makes the boot process much faster.
		* If not currently installed on your system, the AutoFS service and various required files are in the autofs package. `sudo apt install autofs`
		* AutoFS uses the `/etc/auto.master` file, also called the *master map*, as its primary configuration file for managing automatically attached network storage.
		* Master Map
			* The master map file gives the AutoFS service information concerning network-based filesystems, including where they are currently located, where they are to be mounted, and options to use.
			* You can define a different master map in the AutoFS configuration file, `/etc/sysconfig/autofs` or `/etc/default/autofs` (depending on your distribution). The configuration file also contains other settings, such as how long a mounted filesystem can be inactive before it is detached (timeout value). However, the currently defined master map file works in most cases, so there is rarely a need to change it.
			* Except for comment lines that are preceded with a hash mark (#), each master map entry has this basic format:
				* `mount-point map-name [mount-options]`
			* Entries in the master map are one of three different map types. Each map type determines the exact syntax of the master map entry.
				* **Built-in Map**
					* The built-in map file is triggered by having `-hosts` in a master map’s `map-name` field.
					* It has AutoFS mount all of the NFS filesystems available from any NFS server listed within a special directory, `/net`. (This is sometimes called lazy mounting, but built-in mapping sounds better.)
					* For example, if you wanted the NFS filesystem from the NFS server, Server01, to be mounted, you would need the directory, `/net/Server01`, along with the built-in map entry in the master map file. The NFS filesystem from Server01 would be automatically mounted at `/net/Server01`.
					* Thus, the directories not only serve as a trigger for the built-in map, but they also serve as a mount point. You can have multiple directories under `/net`, one for each NFS server.
					* For example, if you also have NFS filesystems on Server02 and Server03, the `/net/Server02` and `/net/Server03` directories would act as triggers for the built-in map and mount points too.
					* A typical built-in map entry in the master map file looks like this:
						* `/net -hosts`
				* **Direct Map**
					* A direct map entry is simply a pointer to another file. The other file is `/etc/auto.direct`.
					* This entry is typically not in the master map by default, so if you desire it, you will have to add it.
					* A typical direct map entry in the master map file looks like this:
						* `/- /etc/auto.direct`
					* Within the `/etc/auto.direct` file, absolute directory path names are listed for the mount points as well as options and their associated servers.
					* Two typical entries in the direct map file may look like this:
						* `/home/bucket server01.acme.com:/home/bucket`
						* `/mnt/nfs/var/nfsshare 192.168.56.101:/var/nfsshare`
				* **Indirect Maps**
					* An indirect map entry is also a pointer to another file. The other file is `/etc/auto.directory` (listed in the certification objectives as `/etc/auto.[dir]`), where directory matches the mount point.
					* For example, the typical default indirect map entry in the master map file looks like this:
						* `/misc /etc/auto.misc`
					* The /etc/auto.misc file is typically used for mounting removable media, such as optical filesystems or USB flash drives. It also has several entries available for you to use if they include no preceding hash mark, such as this one:
						* `cd -fstype=iso9660,ro,nosuid,nodev :/dev/cdrom`
						* Because this file is an indirect map, this entry will cause any CDs to mount under the /misc directory, specifically using the mount point /misc/cd. Thus, the term *indirect map* is applied here.
						* Whereas a direct map file indicates an absolute directory reference, such as `/home/bucket`, an indirect map file only lists a relative map point, such as `cd`, which will be mounted under the directory listed in its master map entry, such as `/misc`.
					* You can have additional indirect map files as needed. For example, if your company had special projects called ProjectX and ProjectY, which required temporary (but not backed up) work space under the `/tmp` directory for several systems, you could set up two NFS filesystems and then add an entry as such in your master map:
						* `/tmp /etc/auto.tmp`
						* Continuing this example, you would then create the file `/etc/auto.tmp`. This indirect map file could contain the following two entries:
							* `projectx -fstype=nfs4,rw :/tmp/projectx`
							* `projecty -fstype=nfs4,rw :/tmp/projecty`
				* Additional sub-master maps can also be included, which are handy if you have a large-scale network-based filesystem deployment. This entry in the master map includes any maps (whose entries must follow the same formatting as those in the master map file) located in the `/etc/auto.master.d/` directory:
					* `+dir:/etc/auto.master.d`
		* When you modify the AutoFS configuration and map files, you will need to restart your AutoFS service. Also, remember that you will need to access the directory to be automatically mounted via AutoFS (an `ls` command will suffice) to trigger the auto-mount of that directory. You can check that the directory is mounted using the `df` command. If the directory is not mounting, check the `/var/log/messages` file for any pertinent error messages.
		* If you are using AutoFS for NFS filesystems and get an error similar to "unable to read `auto.master`", then you may need to comment out the `+auto.master` line, by putting a hash mark (#) in front of it.
		* AutoFS and its maps allow a great deal of flexibility for auto-mounting network-based filesystems. If you decide to set up AutoFS and add any network-based filesystems to it that currently are mounted via the `/etc/fstab` file, be sure to remove them from `/etc/fstab` or you’ll have some interesting situations during your next system reboot!
	* automount units
		* you can use systemd `.automount` units.

#### Maintaining Filesystems
* Filesystem maintenance comprises manipulating standard filesystems via utilities such as `tune2fs`, monitoring a filesystem’s health, and repairing filesystems when problems are encountered.
* adjusting a filesystem
	* For the extended filesystems ext2, ext3, and ext4, you can use these utilities:
		* `debugfs` is an interactive utility that can be used to modify metadata
		* `e2label` modifies a filesystem label
		* `resize2fs` enlarges or shrinks an unmounted filesystem
		* `tune2fs` tunes filesystem attributes, including UUIDs and labels. It is a very versatile utility.
		* `uuidgen` is used to generate a new UUID.
	* for filesystems like xfs and btrfs refer to page 186 (LPIC-2 Study Guide)
* checking and repairing a filesystem
	* For extended filesystems, these utilities can be used:
		* `fsck.*` checks and optionally repairs linux filesystems. Replace the \* with the filesystem type that you wish to check, such as `fsck.ext4`.
			* These utils use the `lost+found` dir. If `fsck` is used to repair a filesystem and it finds files that are not complete (such as a data-filled file that has an inode number but has no name in any directory table), it will attempt to restore these files and place them in the `lost+found` directory for that filesystem.
			* You can check all of the filesystems listed within the `/etc/fstab` file by issuing the `fsck` command using super user privileges at the command line.
		* `debugfs` is an interactive utility that can be used to extract data in order to move it to a new location. 
		* `dump2efs` displays filesystem information.
		* `tune2fs` displays filesystem attributes with the `-l` option.

> [!Warning] Real World Scenario
> When Filesystems Go Bad
> `source: page 189 :: LPIC-2 Study Guide`
> 
> It’s not a case of if it will happen. It’s a case of when it will happen. Filesystems will have problems and, more than likely, it will be up to you to fix things.
> 
> It’s a mistake to handle filesystem repairs on the fly or look up utility information as a problem is occurring. Properly maintaining a filesystem includes implementing plans for these minor calamities, so that they don’t turn into major disasters. In addition, these recorded plans should be reviewed and tested on a regular basis, just like any other disaster plans.
> 
> Of course, data backups and disaster plans are vitally important, but you need planned preventive practices as well. These should include regularly scheduled maintenance for all of your filesystems, along with continual filesystem health monitoring. The filesystem utilities covered in this section (***checking and repairing a filesystem***) can be of assistance to you as you implement these practices.

### LVM
* Data has a habit of increasing.
* While you may be able to predict accurately your data’s growth within a short timeframe, it is much more difficult to predict data growth accurately over longer periods. Fortunately, logical volumes are handy for those times when your predictions are less than accurate.
* understanding LVM
	* *Logical volume management* or *logical volume manager* (LVM) allows multiple partitions to be grouped together and used as a single partition for formatting, mounting on the Linux virtual directory structure, storing data, and so on.
	* This grouping is accomplished through an abstraction layer so that the multiple partitions are referred to as a single volume.
	* LVM has three primary parts:
		* **Pyhsical Volume**
			* A *physical volume* (PV) is created using the LVM’s `/sbin/pvcreate` command.
			* This utility designates an unused disk partition (or whole drive) to be used by LVM.
			* The LVM structures, a volume label, and metadata are added to the partition during this process.
		* **Volume Group**
			* A *volume group* (VG) is created using the LVM’s `/sbin/vgcreate` command, which adds PVs to a storage pool. This storage pool is used in turn to build various logical volumes.
			* You can have multiple volume groups. When using the command to add a PV(s) to a VG, volume group metadata is added to the PV during this process. This metadata includes name, unique VG name, physical extent size, and so on.
			* A disk’s partition, designated as a PV, can belong to only a single VG. However, a disk’s other partitions, also designated as PVs, can belong to other VGs.
		* **Logical Volumes**
			* A *logical volume* (LV) is created using the LVM’s `/sbin/lvcreate` command.
			* A LV consists of storage space chunks (logical extents) from a VG pool. It can be formatted with a filesystem, mounted, and used just like a typical disk partition.
			* While you can have multiple VGs, each LV is created from only one designated VG. However, you can have multiple LVs sharing a single VG.
			* You can resize (grow or reduce) an LV using the appropriate LVM commands. This feature adds a great deal of flexibility to your data storage management.
	* You can see that there are many ways to divide and manage your data storage media using LVM.
	* Additional LVM terms:
		* **Physical Extent (PE)**
			* It is the smallest block size that can be allocated on a PV.
			* This size is set during the process of adding a PV to a VG.
			* By default, the `vgcreate` command chooses 4 MiB. However, you can choose a different setting using the `-s` or `--physicalextentsize` option.
			* The typical size range is 8 KiB to 16 GiB.
				* For example, if you have a 2 TiB PV and use the default 4 MiB PE size, approximately 500,000 PEs will be added to the volume group.
			* After the initial PV, any PV added to the VB will have the same PE size set.
		* **Logical Extent (LE)**
			* LVs are made up of LEs. Logical extents are mapped to VG physical extents.
			* The mapping provides a way to access the data without concern about where a physical extent is located.
* creating logical volumes
	* The lvm utility is an interactive utility for creating and managing LVs.
	* `sudo apt install lvm2`
	* In lvm console you can use `help`.
	* You can use `quit` to exit lvm console.
	* #todo create an lvm console cheatsheet later.
	* five steps to create the first LV:
		1. create PV
		2. create VG
		3. create LV
		4. format LV
		5. mount LV
	* creating physical volumes
		* Before designating drives as PVs, they should be partitioned. Afterward, you can designate the partitions as a PV using the `pvcreate` command.
		* The `pvcreate` command designates the specified disk partition to be used by LVM and adds LVM structures, a volume label, and metadata to the partition. The specified disk partition must be unused.
		* To see the information on your PVs, you can use the `pvdisplay` command. You can specify a PV to see information only on that particular PV, or you can simply enter the `pvdisplay` command to see all of your PVs’ information.
		* Notice that a unique PV UUID is created for each PV. This UUID is generated by the `pvcreate` command, and it can be overwritten using the `--uuid` option when using `pvcreate`.
	* creating volume groups
		* Any PV can be added to a VG.
		* The command to use is `vgcreate`, and its basic syntax is as follows:
			* `vgcreate [VG_name] [PV(s)]`
		* If you need to add PVs at a later time to a VG, you should use the `vgextend` command.
		* It’s important to choose your PE size prior to creating your VG pool. Once set, it can be difficult to change, if current VG members need to have the new PE size. The `-s` option sets the PE size when you use the `vgcreate` command.
		* Common practice names the first VG vg00, the next one vg01, and so on. However, it’s your choice what to name your volume group.
		* Because many distributions on installation set up LVM for the virtual directory structure’s root (/) and other directories, it’s a good idea to check for any current VGs on your system using the `vgdisplay` command.
		* Once you have successfully created a VG, it makes sense to check it. You can do so with the `vgdisplay` command, which operates similarly to the `pvdisplay` command.
		* Once your VG storage pool contains at least one PV, you can move on to creating a LV.
	* creating logical volumes
		* To create an LV from a VG storage pool, the `lvcreate` command is employed. Its basic syntax is as follows:
			* `lvcreate -L [size] [VG_name]`
		* With the `lvcreate` command, the volume’s size is designated using the `-L` option and the VG from which to pull logical extents (LE)s is designated by VG_name.
		* If for some reason a VG does not have enough LEs to give to the LV for the designated size, then it will not be able to create the LV.
		* The minimum size that you can specify for an LV is the VG’s PE size. Thus, if you use the default PE size when creating your VG, the smallest size LV is 4 MiB.
		* The first LV from a VG's default name is lvol0. And you must use its full path name for displaying an LV's information.
			* `lvdisplay /dev/[VG_name]/[LV_name]`
		* Besides the `lvdisplay` command, you can use the `lvs` and the `lvscan` commands to display information on all of your system’s LVs.
		* Once you have your LV created, you can treat it as if it is a regular partition. Of course, it is different in that you can grow or shrink this partition on the fly as needed.
	* formatting and mounting a logical volume
		* You don’t have to do anything special with your LV in order to make a filesystem on it and then mount it to the virtual directory structure.
		* The system views it as a normal partition.
		* For example:
			* `mkfs -t ext4 /dev/vg00/lvol0`
			* `mount -t ext4 /dev/vg00/lvol0 Temp`
			* `ls Temp`
* supporting logical volumes
	* growing your VGs and LVs
		* Before increasing an LV’s size, it’s worthwhile to look at increasing a VG’s size with more PVs. You can’t increase an LV beyond what its VG has to offer.
		* Once you’ve added or located additional storage, be sure that it is designated as a PV prior to attempting to add it to a VG pool.
		* If you have two oversized VGs, you can merge them with the `vgmerge` command. This can be useful if you have no additional partitions to use and need to increase an LV’s size immediately.
		* Besides the `pvdisplay` command, you can use the `pvscan` utility to check the system for all available PVs.
		* With the additional needed PV(s) designated, the VG can be extended. To increase the size of a VG pool, use the `vgextend` command.
		* To grow an LV, use the `lvextend` command. The `-L` option is used to set the new desired size of the LV.
		* After using `vgextend`, notice that a volume group backup is created. These backups are VG metadata only, and they do not contain any user or system LV data. They are often automatically created when using utilities like `lvextend`. However, it may be useful to create a VG metadata backup manually using the `vgcfgbackup` utility. You can restore the metadata using the `vgcfgrestore` command.
		* A helpful way to check your extended LV is using `lvdisplay` with the `--maps` option. This option allows you to see the LV’s logical extents mapped to PV physical extents.
		* If you need to **shrink** an LV’s size, you can do so with the `lvreduce` command. However, this command can destroy data, so **use it with caution**, and be sure to ***review its man pages*** prior to using the command.
	* creating and maintaining an LV snapshot -> refer to page 257 (LPIC-2 Study Guide)
	* renaming LV
		* Renaming an LV is simple using the `lvrename` utility.
		* `lvrename /dev/[VG_name]/[old_LV_name] /dev/[VG_name]/[new_LV_name]`
		* or: `lvrename [VG_name] [old_LV_name] [new_LV_name]`
	* employ the LVM config file
		* When using the various LVM utilities, each utility uses a central configuration file to govern its behavior. This configuration file is the `/etc/lvm/lvm.conf` file.
		* `man lvm.conf`
		* The lvm.conf file’s existence is not required, because the LVM utilities will use default settings. However, if the file does exist and has not been modified, it most likely will contain these default settings.
		* The `lvm.conf` configuration file is considered a global file, and it may load additional local configuration files to refine its settings.
		* LVM uses timestamps in association with this global file and any local configuration files. If the global (or local) configuration file has been modified, LVM reloads them.
		* Though you may never need to modify the lvm.conf file, there are some cases where it may be useful for your particular environment. For example, you can modify the `lvm.conf` configuration file to use filters, which are regular expressions. These filters in turn will limit what the various LVM \*scan utilities can view. This is useful for speeding up scans should you have a large mixed storage environment.
		* You can employ the `lvm dumpconfig` utility to display `lvm.conf` settings.
			* `lvm dumpconfig --type default`
			* `man lvm-dumpconfig`
* understading the device mapper
	* LVs are assisted by the Device Mapper.
	* The *Device Mapper* is a kernel driver, and it provides the ability to create mapped devices.
	* It maps physical storage blocks to virtual storage blocks, creating a framework for LVM and RAID.
	* You can interact with the Device Mapper directory via the `dmsetup` utility.
	* To see the various LVs on your system, type `dmsetup info`.
	* You can get help on the utility by entering `dmsetup help`.
	* It’s unlikely that you will need to modify any Device Mapper settings. However, you do need to be aware of the mapper. When you create an LV using the `lvcreate` command, not only can you reference it via its `/dev` name, such as `/dev/vg00/lvol0`, but you can also reference it via `/dev/mapper/LV_name`.
	* As you can see, there are `/dev/mapper` names in the `/etc/fstab` file. On some distributions, `/dev/mapper` names must be used instead of `/dev` names for LVs so that the system will invoke LVM at system boot. Therefore, best practice recommends using `/dev/mapper` names within the `/etc/fstab` file for mounting LVs at system boot.

> [!Question] ChatGPT
> **What are the common usages of LVM in linux servers? I can't imagine why a company would need to use this.**
>
> Logical Volume Management (LVM) offers several benefits for managing storage on Linux servers, particularly in enterprise environments where scalability, flexibility, and efficient resource utilization are critical. Here are some common usages of LVM in Linux servers that companies might find beneficial:
>
> 1. **Dynamic Volume Management:** LVM allows administrators to create logical volumes (LVs) that span multiple physical disks or partitions. This enables dynamic resizing and movement of filesystems without requiring downtime. Servers can grow or shrink storage volumes as needed without disrupting services.
>    
> 2. **Storage Pooling:** LVM enables the creation of storage pools by combining multiple physical disks into a single logical volume group (VG). This aggregated storage can be easily allocated to different logical volumes, providing efficient resource utilization and avoiding potential disk space silos.
>    
> 3. **Snapshot Management:** LVM provides the ability to create snapshots, which are point-in-time copies of logical volumes. These snapshots are particularly useful for creating backups or performing system updates without affecting the live data.
>    
> 4. **Volume Migration:** LVM supports non-disruptive data migration between physical disks or storage systems. This feature is helpful for maintaining storage systems without causing downtime.
>    
> 5. **Online Volume Expansion:** With LVM, administrators can expand filesystems online by adding new physical volumes or extending existing ones. This is particularly valuable for rapidly growing data stores without the need to take services offline.
>    
> 6. **Storage Tiering:** LVM allows organizations to implement storage tiering by combining SSDs and traditional hard drives in a single logical volume group. Frequently accessed data can be placed on SSDs for faster access, while less frequently used data can reside on slower, larger-capacity drives.
>    
> 7. **Reducing Downtime:** LVM's flexibility in resizing, relocating, and redistributing data means that administrators can perform maintenance or upgrades with minimal downtime, reducing the impact on users and services.
>    
> 8. **Complex Partitioning:** LVM simplifies partition management by abstracting physical storage from logical volumes. This reduces the need for complex partitioning schemes and allows for more flexible resource allocation.
>    
> 9. **Consolidation and Centralized Management:** For organizations with multiple servers, LVM can provide a centralized approach to storage management, allowing administrators to allocate and manage storage resources from a single management console.
>    
> 10. **Virtualization and Cloud Deployments:** LVM's features are particularly beneficial in virtualized environments, allowing easy resizing and management of virtual machine storage without requiring changes to the underlying storage infrastructure.
