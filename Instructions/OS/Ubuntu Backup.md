* **/home/mehdi**
	* `.zshrc`
	* `.mehdirc`
	* `.zshrc.zni`
	* `.vimrc`
	* `.python_history`
	* `.pypirc`
	* `.zsh_history (.histfile)`
	* `.gitconfig`
	* `.aria2c`
	* `.wdm`
	* `.vim`
	* `.venvs`

* steam data for csgo
* **virtualenv names and freeze**
	* backup
		```zsh
		destination="/tmp/venvs"
		file_extension=".pip.txt"
	
		mkdir $destination
		for d in */ ; do           
	        source ./$d/bin/activate
	        len=${#d}
	        filename=$(cut -c 1-$(($len-1)) <<< "$d")
	        filename="$filename""$file_extension"
	        pip freeze > $destination/$filename
		done
		```
	* restore
		```zsh
		src="/home/mehdi/Bedroom/Backups/venvs"
		file_extension=".pip.txt"
		
		cd $src
		for d in *$file_extension ; do
			vname=${d/$file_extension/}
			mkvirtualenv $vname
			workon $vname
			pip install -r $d
		done
		```

* **.config**
	* `user-dirs.conf`
	* `user-dirs.dirs`
	* `gspread`

* **JetBrains** -> export `settings.zip`
* Chrome -> export `cookies`
* `/var/cache/locate/updatedb`
* backup postgres databases
	* `psql`
		* `\l` lists databases
	* `pg_dump [dbname] > file.psqldb` backs up
		* `psql [dbname] < file.psqldb` restores
	* `pg_dumpall > file.psqlcluster` backups up entire cluster (reserves roles, ...)
		* `psql -f file.psqlcluster postgres`
	* remember, when using pgdump, the postgres user should have write access to the desired directory used. e.g. `/tmp`
* obsidian plugins & settings
* `/etc/tsocks`
* gnome extensions names
	* `ls -la ~/.local/share/gnome-shell/extensions > ~/.gnome-ext.bak`
	* dash to dock: `/org/gnome/shell/extensions/dash-to-dock/`
	* impatience
	* persian calendar: `/org/gnome/shell/extensions/persian-calendar/`
	* simple timer
	* stopwatch
	* task widget
	* user themes
	* vitals: `/org/gnome/shell/extensions/vitals/`
	* pomodoro
	* desktop icons ng
	* removable drive menu
	* ubuntu appindicators
	* ubuntu dock
	* wokspace indicator
* backup each google chrome extensions:
	* #todo 
* gnome
	* [gnome terminal](https://askubuntu.com/questions/967517/how-to-backup-gnome-terminal-emulator-settings)
		* Based on [this article](https://github.com/linuxmint/Cinnamon/wiki/Backing-up-and-restoring-your-cinnamon-settings-(dconf)), you can dump your settings using:
			* `dconf dump /org/gnome/terminal/ > gnome-terminal.dconf.bak`
		* Reset (wipe out) the settings before loading a new one (probably not really required):
			* `dconf reset -f /org/gnome/terminal/`
		* Load the saved settings:
			* `dconf load /org/gnome/terminal/ < gnome-terminal.dconf.bak`
	* gnome nautilus: `/org/gnome/nautilus/`
	* gnome-text-editor: `/org/gnome/TextEditor/`
	* evince: `/org/gnome/evince/`
	* pomodoro: `/org/gnome/pomodoro/`

### Restore
#### Home
* `Bedroom` dir
	* `Backups` dir
	* `Desktop` dir
	* `Documents` dir
	* `Downloads` dir
	* `Pictures` dir
	* `Projects` dir
	* `Scripts` dir
	* `VBoxVMs` dir
	* `Videos` dir
* `.logins` dir: contains .files which contain user passwords
* `.android` dir: contains android sdk files
* `.aria2c`
* `.cache` dir
	* `google-chrome` dir
* `.config` dir
	* `aria2` dir
	* `artha.conf`
	* `artha.log`: list of words looked up
	* `autostart` dir
	* `google-chrome` dir
	* `htop/htoprc`
	* `libreoffice` dir
	* `nautilus/search-metadata`
	* `neofetch/config.conf`
	* `ulauncher` dir
		* `settings.json`
		* `ext_preferences` dir
	* `user-dirs.dirs`
	* `user-dirs.conf`
	* `user-dirs.dirs.backup`
	* `user-dirs.locale`
* `.gitconfig`
* `.ipython`
* `.local` dir
	* `backgrounds` dir
* `.mehdirc`
* `.mehdi.d` dir
	* This is an advancement of `.mehdirc`.
* `.profile`
* `.profile.bak`
* `.psql_history`
* `.pypirc`
* `.python_history`
* `.ssh` dir (maybe?? be careful!)
* `.vimrc`
* `.vim` dir
	* `colors` dir
* `.wdm`
* `.wget-hsts`
* `.zshrc`
* `.zshrc.zni`

#### Root
* `/etc` dir
	* `at.deny`
	* `anacrontab`
	* `cron*` dirs and files
	* `environment`
	* `environment.d`
	* `fstab`
	* `hosts`
	* `hosts.allow`
	* `hosts.deny`
	* `postgresql` dir
		* beware version differences: this is psql-14
		* `environment`
		* `pg_ctl.conf`
		* `pg_hba.conf`
		* `pg_ident.conf`
		* `postgresql.conf`
		* `start.conf`
	* `postgresql-common` dir
		* `createcluster.conf`
	* `redis` dir
	* `rsyslog.conf`
	* `ssh/ssh_config`
	* `sudoers`
	* `sudoers.d` dir
	* `systemd` dir
		* `journald.conf`
		* `networkd.conf`
		* `resolved.conf`
		* `system.conf`
		* `user.conf`
	* `tsocks.conf`
	* `ufw` dir
	* `vim/` dir
	* `wgetrc`
* `/root` dir
	* `.bash_history`
	* `.bashrc`
	* `.config/htop/htoprc`
	* `.profile`
	* `.selected_editor`
	* `.wget-hsts`
* `/usr` dir
	* `local/etc/v2ray` dir
	* `share` dir
		* this is an unexplored territory
* `/var/cache/apt/archives` dir