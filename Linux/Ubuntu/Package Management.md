#### Commands
* *depr*: debtree
	* `sudo apt install apt-rdepends`
	* `sudo apt install rdepends`
* `ppa-purge` removes a ppa and reverts packages to normal
* `add-apt-repository [--remove] [repo]`

#### DPKG: `The Debian Package Tool`
* upgrade or install `dpkg -i [deb file]`
* remove `dpkg -r [pkg name]`
	* dependency check: if you try to remove a package, dpkg won't do it unless all other packages that rely on this are also removed.
	* `--force` will bypass the dependency check and leave your device in a broken state
* remove with associations `dpkg -P [pkg name]`
	* to remove everything that the package associated with alongside the package itself
	* purge
* deb info `dpkg -I [deb file]`
* list of every package installed `dpkg --get-selections`
* list of every **file** installed by a *package* `dpkg -L [pkg name]`
* find packages that own **file** `dpkg-query -S [path to file]`
* `dpkg-reconfigure` reconfigures packages after they have been already installed.
* `dpkg-deb` packs, unpacks and provides info about Debian archives.
* configure unpacked but unconfigured packages
	* `dpkg --configure`
	* append `-a` to config all unconfigured ones
* `dpkg-builpackage` automates the process of making packages.

#### APT: `Advanced Package Tool`
* apt-get: download, install, upgrade, remove
	* `apt-get update`
	* `apt-get install [pkg name]`
	* `apt-get install [pkg name] --no-upgrade`
	* `apt-get install [pkg name] --only-upgrade`
	* download bin to cwd `apt-get download [pkg name]`
	* `apt-get remove [pkg name]`
	* `apt-get purge [pkg name]` | `apt-get remove --purge [pkg name]`
	* fix broken dependency `apt-get install [-f/--fix-broken]` 
	* `apt-get upgrade`
	* update package cache and check broken dependencies `apt-get check`
	* local cache `/var/cache/apt/archives`
	* local cache of partially downloaded: `/var/cache/apt/archives/partial`
	* clean local cache `apt-get clean`
 * apt-cache: search
	 * `apt-cache search [pkg name]`
	 * `apt-cache show [pkg name]`
	 * `apt-cache policy [pkg name]`
	 * print reverse/forward dependencies `apt-cache showpkg [pkg name(s)]`
	 * `apt-cache depends [pkg name]`
	 * `apt-cache rdepends [pkg name]`
	 * list all packages (even not installed) `apt-cache pkgnames [prefix]`
* apt-file: search for files inside packages
	* update package cache: `apt-file update`
	* contents of a package: `apt-file list [pkg name]` | `apt list [pkg name]`
	* search all packages for a file: `apt-file search [file *name*]`
		* compared to dpkg-query, apt-file also searches uninstalled packages, whereas dpkg-query only searches installed packages.
* apt: combination of these
	* update location -> `/var/lib/apt/lists`
	* apt-key -> `/etc/apt/trusted.gpg.d`
	* sources
		* `/etc/apt/sources.list`
		* `/etc/apt/sources.list.d/`
		* syntax: `deb http://us.archive.ubuntu.com/ubuntu/ disco main restricted universe multiverse`
			1. archive type: binary package `deb`, source code `deb-src`
			2. url
			3. distribution: codename for \[your\] distribution, in case the repo provides for multiple distros
			4. components: each component represents a set of packages
				* ubuntu components
					* main: officially supported, open-source packages
					* restricted: officially supported, closed-source software
					* universe: community maintained open-source software
					* multiverse: unsupported, closed-source or patent-encumbered software
				* debian components
					* main: packages compliant with the [Debian Free Software Guideline](https://www.debian.org/social_contract#guidelines) `(DFSG)` that do not rely on external packages.
					* contrib: packages compliant with DFSG but might rely on external packages and aren't in main.
					* non-free: non-compliant with DFSG
					* security
					* backports: up to date packages outside of main which is restricted to the debian dev lifecycle (2 years)
