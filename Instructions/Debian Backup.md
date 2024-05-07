* Docker
* **virtualenv names and freeze**
	* backup: `venvs-backup-modules /tmp/venvs`
	* restore: `venvs-restore-modules <backup-dir> [--proxy]`
* **JetBrains** -> export `settings.zip`
* Chrome -> export `cookies` [webstore](https://chrome.google.com/webstore/detail/cookie-backup-and-restore/cndobhdcpmpilkebeebeecgminfhkpcj)
* `/var/cache/locate/updatedb`
* backup postgres databases
	* `psql`
		* `\l` lists databases
	* `pg_dump [dbname] > file.psqldb` backs up
		* `psql < file.psqldb` restores
	* `pg_dumpall > file.psqlcluster` backups up entire cluster (reserves roles, ...)
		* `psql -f file.psqlcluster postgres`
	* remember, when using pgdump, the postgres user should have write access to the desired directory used. e.g. `/tmp`
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
	* [ADHD Reader](https://chromewebstore.google.com/detail/adhd-reader/gcbchiambcokahmamemkoadlanaealmf)
	* (deactive) [AI Prompt Genius](https://chromewebstore.google.com/detail/ai-prompt-genius/jjdnakkfjnnbbckhifcfchagnpofjffo)
	* [Aria2 Explorer](https://chromewebstore.google.com/detail/aria2-explorer/mpkodccbngfoacfalldjimigbofkhgjn)
	* [BitWarden](https://chromewebstore.google.com/detail/bitwarden-password-manage/nngceckbapebfimnlniiiahkandclblb)
	* [BlipRead](https://chrome.google.com/webstore/detail/pimmlmgpidiceckodhdifoppcidlndbp)
	* [Cookie Backup and Restore](https://chrome.google.com/webstore/detail/cndobhdcpmpilkebeebeecgminfhkpcj)
	* *backup* [Custom Search Engine](https://chrome.google.com/webstore/detail/kelahdmegihhooaelnaahkeggodajdjf)
	* *backup* [Dark Reader](https://chrome.google.com/webstore/detail/eimadpbcbfnmbkopoojfekhnkhdbieeh)
	* [Daxab](https://chrome.google.com/webstore/detail/enakmcmeealkdoeindgoeogldodhdeda)
	* [Gnome shell integration](https://chrome.google.com/webstore/detail/gphhapmejobijbbhgpjhcjognlahblep)
	* [Google docs offline](https://chrome.google.com/webstore/detail/ghbmnnjooekpmoecnnnilnnbdlolhkhi)
	* [gkeep fullscreen](https://chrome.google.com/webstore/detail/kcfmkpjpemonceecfpgamaahlkfpjhdk)
	* (deactive) [grammarly](https://chrome.google.com/webstore/detail/kbfnbcaeplbcioakkpcpgfkobkghlhen)
	* *backup* [highlight this](https://chrome.google.com/webstore/detail/fgmbnmjmbjenlhbefngfibmjkpbcljaj)
	* [input tab gkeep](https://chrome.google.com/webstore/detail/bmfmbanhkhjhfeckobkcecohknhlnamb)
	* *backup* [proxy switchyomega](https://chrome.google.com/webstore/detail/padekgcemlokbadohgkifijomclgjgif)
	* [Reader Mode](https://chrome.google.com/webstore/detail/llimhhconnjiflfimocjggfjdlmlhblm)
	* [ruffle flash emulator](https://chrome.google.com/webstore/detail/donbcfbmhbcapadipfkeojnmajbakjdc)
	* [save to gdrive](https://chrome.google.com/webstore/detail/gmbmikajjgmnabiglmofipeabaddhgne)
	* [superpower gpt](https://chrome.google.com/webstore/detail/amhmeenmapldpjdedekalnfifgnpfnkc)
	* [video speed controller](https://chrome.google.com/webstore/detail/nffaoalbilbmmfgbnbgppjihopabppdk)
	* *backup* [webtime tracker](https://chromewebstore.google.com/detail/webtime-tracker/ppaojnbmmaigjmlpjaldnkgnklhicppk)
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
    * tilix: `/com/gexperts/Tilix/` 
* authenticator
* export/import vscode profile

### Restore
#### Home
* `Bedroom` dir
* `.android` dir: contains android sdk files
* `.aria2c`
* `.bash_history`
* `.bashrc`
* `.dir_colors`
* `.config` dir
	* `aria2` dir
	* `artha.conf`
	* `artha.log`: list of words looked up
	* `autostart` dir
    * `gspread` dir
	* `htop/htoprc`
	* `libreoffice` dir
	* `nautilus/search-metadata`
	* `neofetch/config.conf`
    * `obsidian` dir
        * `Dictionaries/*`
        * `Custom Dictionary.txt`
        * `Custom Dictionary.txt.backup`
        * `Preferences`
    * `tilix` dir
	* `ulauncher` dir
		* `settings.json`
		* `ext_preferences` dir
	* `user-dirs.dirs`
	* `user-dirs.conf`
	* `user-dirs.locale`
	* `hakuneko-desktop/hakuneko.settings`
	* `mcomix`
* `.docker` dir
* `.FBReader` dir
    * `network.xml`
    * `options.xml`
    * `ui.xml`
* `.gitconfig`
* `.histfile`
* `.ipython`
* `.kube` dir
* `.lesshst`
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
* `.todo-txt` dir
* `.tldr-userpath`
* `.vagrant.d` dir
* `.vimrc`
* `.vim` dir
	* `colors` dir
* `.wdm`
* `.wget-hsts`
* `.zshrc`
* `.zshrc.zni`

#### Root
* `/etc` dir
    * `apt` dir
        * `sources.list`
        * `sources.list.d/*` dir
        * `apt.conf.d/` dir
            * `20auto-upgrades`
            * `70debconf`
        * `preferences.d/*` dir
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
    * `tsocks.*`
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
    * `local/share/ca-certificates` dir
	* `share` dir
		* this is an unexplored territory
* `/var/cache/apt/archives` dir
