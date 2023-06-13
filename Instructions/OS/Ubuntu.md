##### change power options
##### add persian keyboard (with keypad)
---
##### fix brightness controller
* obviously only if it doesn't work
* `sudo gnome-text-editor /etc/default/grub`
	```bash
	GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor acpi_osi=linux"
	GRUB_CMDLINE_LINUX=""
	```
* `sudo update-grub`
* also change nvidia drivers to recommended in gnome software updates
* don't forget to restart
---
##### [asus-fan-control](https://github.com/dominiksalvet/asus-fan-control)
---
##### mount drive to startup with disks
---
##### [v2ray](https://github.com/v2fly/fhs-install-v2ray)
* `curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh > v2ray-install-script.sh`
* `bash v2ray-install-scripts.sh`
* `systemctl enable v2ray`
* `systemctl start v2ray`
* restore `/usr/local/etc/v2ray/config.json`
* `service v2ray restart`
---
##### destroy [snap](https://www.debugpoint.com/remove-snap-ubuntu/)
* `sudo snap --purge firefox`
* `sudo snap --purge snap-store`
* `sudo snap --purge gnome-3-38-2004`
* `sudo snap --purge gtk-common-themes`
* `sudo snap --purge snapd-desktop-integration`
* `sudo snap --purge bare`
* `sudo snap --purge core20`
* `sudo snap --purge core22`
* purge the rest from `snap list`
* at last: `sudo snap --purge snapd`
* `sudo apt remove --purge --autoremove snapd`
* prevent `apt update` bringing snap back:
	* `sudo -H vim /etc/apt/preferences.d/nosnap.pref` :
	* `Package: snapd`
	* `Pin: release a=*`
	* `Pin-Priority: -10`
* `sudo apt update`
* `sudo apt install --install-suggest gnome-software`
* `sudo add-apt-repository ppa:mozillateam/ppa`
* `sudo apt update`
* `sudo apt install -t 'o=LP-PPA-mozillateam' firefox`
* `echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | sudo tee /etc/apt/apt.conf.d/51unattended-upgrade-firefox`
* `sudo -H vim /etc/apt/preferences.d/mozillateamppa`
	* `Package: firefox*`
	* `Pin: release o=LP-PPA-mozillateam`
	* `Pin-Priority: 501`
---
##### home
###### create customized home folders
* create `Bedroom` dir in `home`
* create `Corridor` dir in `home`
	* create sym links to `Corridor`
		* e.g. `ln -s /media/mehdi/DATA /home/mehdi/Corridor/data`
* create `Backups` in `Bedroom`
* restore `Projects` to `Bedroom`
* restore `Scripts` to `Bedroom`
* create `Tweakroom` in `home`
	* create symlinks from actual config files
		* e.g. ln -s `/home/mehdi/.mehdirc` `/home/mehdi/Tweakroom/mehdirc`
		* #todo create a list of config files that I tweak, **here**!

###### setup default home directories (within Bedroom)
* `vim ~/.config/user-dirs.dirs`
	```bash
	XDG_DESKTOP_DIR="$HOME/Bedroom/Desktop"
	XDG_DOWNLOAD_DIR="$HOME/Bedroom/Downloads"
	XDG_PICTURES_DIR="$HOME/Bedroom/Pictures"
	XDG_VIDEOS_DIR="$HOME/Bedroom/Videos"
	XDG_DOCUMENTS_DIR="$HOME/Bedroom/Documents"
	```
* `cp -rv /etc/xdg/user-dirs.conf ~/.config/user-dirs.conf`
* `vim ~/.config/user-dirs.conf`
	* `enabled=False`

###### change nautilus startup folder
* `cp -rv /usr/share/applications/org.gnome.Nautilus.desktop ~/.local/share/applications`
* `cd ~/.local/share/appliactions`
* `chmod +x org.gnome.Nautilus.desktop`
* `vim org.gnome.Nautilus.desktop`
	* `DBusActivatable=true`    -> comment out
	* `Exec=nautilus --new-window /home/mehdi/Bedroom`
		* under `[Desktop Action new-window]`
		* do not change the FIRST Exec under `[Desktop Entry]`
* logout
---
##### depr: windscribe.deb
* `sudo apt install ./windscribe-version.deb`
* to reset config
	* `sudo rm -rf /etc/windscribe/* /usr/local/windscribe/*`
---
##### chrome .deb
* `sudo apt install ./chrome.deb`
---
##### depr: fix snap firefox
* **fixed before in *destroy snap***
* `sudo snap remove firefox`
* `sudo apt remove --purge firefox`
* `sudo add-apt-repository ppa:mozillateam/ppa`
	* [omgubuntu.co.uk](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04)
* `sudo apt install firefox`
---
##### upgrade
* `sudo apt-get update`
* `sudo apt-get upgrade`
* `sudo apt-get dist-upgrade`
---
##### virtualenvwrapper
* `sudo apt install python3-pip`
* `sudo pip install virtualenv virtualenvwrapper`
* [readthedocs.io](https://virtualenvwrapper.readthedocs.io/en/latest/)
	* `pip install virtualenvwrapper`
	* `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3`
	* `export WORKON_HOME=~/.venvs`
	* `source /usr/local/bin/virtualenvwrapper.sh`
	* `workon systemvenv`
	* or: restore `.mehdirc`
* `mkvirtualenv system_venv`
* restore venvs backed up and frozen
	* alternative idea: instead of restoring, create a requirements file for each so bullshit packages are not included. That way you are not forced to keep the versions and install the latest version of each package. If you don't do that and just pip freeze and remove versions and then restore, versions will colide.
---
##### apt pkgs
* `sudo apt install git curl wget httpie exa vim`
* `sudo apt install gparted htop ipython3 testdisk fzf`
* `sudo apt install vlc vlc-l10n vlc-plugin-access-extra vlc-plugin-base vlc-plugin-qt vlc-plugin-video-output vlc-plugin-video-splitter vlc-plugin-visualization`
* *depc*: `snap install spotify discord telegram-desktop`
* `sudo apt install ripgrep fd-find aria2 ipython3 jmtpfs locate`
* `sudo add-apt-repository ppa:openshot.developers/ppa; sudo apt install openshot-qt`
* `sudo apt install apt-transport-https ca-certificates gnupg lsb-release`
* `sudo apt install bat exa broot gping duf jq`
* `sudo apt install net-tools traceroute ethtool netstat nmap tcpdump iptraf mtr ncftp yafc lsscsi qbittorrent`
* `sudo apt install rar unrar zip unzip p7zip-full p7zip-rar`
* `sudo apt install redis-tools syncthing neofetch`
* `sudo apt install tldr`
	* alternatively: [`tldr`](https://github.com/raylee/tldr-sh-client)
* `sudo apt install gnome-shell-pomodoro gnome-shell-pomodoro-data`
* `sudo apt install dconf-editor`
* peek: gif video recorder
	* `sudo add-apt-repository ppa:peek-developers/stable`
	* `sudo apt update`
	* `sudo apt install peek`
* discord
	* set push to talk to `Left-Ctrl + Left-Alt`
* virtualbox/vmware
---
##### ULauncher
* `sudo apt install ulauncher`
* plugins
	* [file-search](https://github.com/brpaz/ulauncher-file-search)
	* [calculate-anything](https://github.com/tchar/ulauncher-albert-calculate-anything)
	* [ukill](https://github.com/isacikgoz/ukill)
	* [better-file-browser](https://github.com/fisadev/ulauncher-better-file-browser)
	* [gnome-tracker](https://github.com/dalanicolai/gnome-tracker-extension)
* settings
	* hotkey: ctrl+shift+space
	* color theme: elementary dark
	* launch at login
	* number of frequent apps to show: 5
	* clear input on hide
* shortcuts
	* google search - g - `https://google.com/search?q=%s`
	* stack overflow - so - `https://stackoverflow.com/search?q=%s`
	* wikipedia - wiki - `https://en.wikipedia.org/wiki/%s`
---
##### depc: telegram
* alternative: web version
---
##### pycharm
###### install
* download .zip from soft98.ir
* unzip soft98_zip_file.zip
* `cd [soft98_pycharm_folder]`
* `tar xvzf pycharm-professional-version.tar.gz`
* `mkdir ~/.local/JetBrains`
* `cp -rv pycharm-version ~/.local/JetBrains`
* `cd ~/.local/JetBrains/pycharm-professional-version/bin`
* `./pycharm.sh`
###### crack
* `cd [download_dir]/[pycharm-professional-version]/[crack]`
* `cp -rv jetbrais.jar ~/.local/JetBrains`
* run IDE
	* IDE Menu `Configure/Help` -> `Edit Custom VM options`
		* `-javaagent:/home/mehdi/.local/JetBrains/jetbrains.jar` -> append and save
		* restart IDE
	* IDE Menu `configure` -> `manage license`
		* `license server` -> `discover servers (autofill)` -> `okay`
###### config pycharm
* restore `settings.zip`
* set proxy: `http://localhost:10809`
* plugins
	* json parser
	* gitToolBox
	* .env files support
	* .ignore
	* docker
	* bash support
	* string manipulation
	* csv
	* doc-aware search everywhere
	* envfile
	* ide eval reset
	* rainbow brackets
	* selenium ui testing
	* xpathview + xslt
---
##### depr: vscode
* `sudo apt install ./vscode.deb`
* terminal # Ctrl+Shift+\` 
* extensions
	* Python (microsoft)
	* Djaneiro
	* Darcula IntelliJ Theme
	* material icon theme
	* Git History
* vscode commands -> `CTRL+SHIFT+P`
* select python enterpreter
* file -> preference -> settings -> json -> add:
```json
	"editor.formatOnSave": true,
	"editor.rulers": [
		80,
		120
	],
	"files.exclude": {
		"**/.git": true,
		"**/.svn": true,
		"**/.hg": true,
		"**/CVS": true,
		"**/.DS_Store": true,
		".vscode": true,
		"**/*.pyc": true,
		"**/.idea": true,
		"**/.github": true,
	},
	"workbench.editor.enablePreview": false,
	"editor.minimap.enabled": true,
	"python.linting.pylintArgs": [
		"--load-plugins",
		"pylint_django"
	]
```
* `pip install autopep8`
* `pip install pylint`
* restart vscode
* hints
	* code .
	* code --add {dir} -> add folder to windows
	* code --diff {file} {file} -> compare
	* code --new-window -> open new empty window
	* code --reuse-window -> open new tab
	* code --install-extension-id \[{extension-id}/{extension-vsix-path}\]
---
##### ubuntu settings
* change background
	* `cp -rv [photo] ~/.local/share/backgrounds/`
* *depr*: added online google account
* ubuntu desktop
	* icons
	* small
	* topleft
	* show personal folder: `no`
	* dock -> dont show volumes
* multitasking
	* hot-corner
* sound: click
* display
	* set night light to `20:00-05:00`
* keyboard shortcuts
	* home folder: `Alt+Return`
	* Launch Calculator: `Super+Return`
	* Switch applications: `Disabled`
	* Switch windows: `Alt+Tab`
	* Switch windows of an application: `Super+Tab`
	* Restore the keyboard shortcuts: `Disabled`
	* Hide window: `Super+Down`
	* Restore window: `Disabled`
	* Toggle fullscreen mode: `Alt+F10`
	* Toggle Maximization state: `Super+Up`
	* Move window one workspace to the left: `Shift+Ctrl+Alt+Left`
	* Move window one workspace to the right: `Shift+Ctrl+Alt+Right`
* add persian keyboard
* fix date & time
* region: set format to `uk`
---
##### depr: pdfstudioviewer
* [qoppa.com](https://download.qoppa.com/pdfstudioviewer/PDFStudioViewer_linux64.deb)
---
##### gnome-tweaks
* `sudo apt install gnome-tweaks chrome-gnome-shell gnome-shell-extensions`

###### config
* general
	* over-amplification
* apprearance
	* applications: `Yaru-Dark`
	* cursor: `Xcursor-breeze-snow`
	* icons: Yaru
	* shell: `Matcha-sea`
* top bar
	* battery percentage
	* date
	* seconds
* window titlebars
	* double-click toggle maximize
	* middle-click minimize
	* secondary-click menu
---
##### manually install gnome-shell-connector
* https://wiki.gnome.org/Projects/GnomeShellIntegration/Installation
* dependencies
	* python 3.8+
	* `apt install meson`
	* gnome-shell
	* PyGObject
	* DBus
* `sudo -i`
* `cd /tmp`
* `git -c http.proxy=http://localhost:10809 http.sslVerify=false clone https://gitlab.gnome.org/nE0sIghT/gnome-browser-connector.git`
* `cd gnome-browser-connector`
* `meson --prefix=/usr builddir`
* `meson install -C builddir`
* restart gnome-shell
	* `Alt+F2`, r, enter
	* or: `killall -SIGQUIT gnome-shell`
* now you can use gnome-shell-extensions

##### manually install an extension
* `MY_EXT_UUID=$(unzip -p [zipfile] metadata.json | jq -r '.uuid')`
* `unzip -q -o [zipfile] -d ~/.local/share/gnome-shell/extensions/$MY_EXT_UUID`
* restart gnome: `killall -SIGQUIT gnome-shell`

##### extensions
* user themes
* *depr*: refresh wifi connections
* depr: activities configurator
* removable drive menu
* *depr*: panel-osd
* *depr*: remove dropdown arrows
* *incompatible*: Steal My Focus (by sstent)
* *depr*: Auto Move Windows
* desktop icons
* simple timer (majortom)
* stopwatch
* persian calendar
	* all check
	* `%MM %D/%M/%Y`
* dash to dock
	* position and size
		* position on screen: `bottom`
		* intelligent autohide
			* autohide
			* enable in fullscreen mode
			* push to show
			* dodge windows: only focused application's windows
			* `0.200`
			* `0.200`
			* `0.250`
			* `100`
		* dock size limit: `90%`
		* panel mode: `uncheck`
		* icon size limit `44px`
	* launchers
		* show favorite applications
		* show running applications
		* show open windows previews
		* isolate workspaces
		* isolate monitors: `uncheck`
		* show applications icon
		* move... : `uncheck`
		* animate show applications
		* show trash: `uncheck`
		* show mounted: `uncheck`
	* behavior
		* use keybo...
		* cycle through
		* click action
			* `shift+click`: show window previews
			* `middle-click`: minimize window
			* `shift+middle-click`: launch new instance
		* switch workspace
	* appearance
		* built-in theme: `uncheck`
		* shrink: `uncheck`
		* customize windo: `dots`
		* dash color: `#183635`
		* customize opacity: fixed: `56%`
		* force straight: `uncheck`
* *incompatible*: wintile
* vitals
	* processor: usage
	* memory: usage
	* fan
	* temperature: average
	* network: wlp3s0 down
	* network: wlp3s0 up
* impatience
---
##### vimix theme & Yaru icon pack
* `sudo apt install vimix yaru-theme-icon`
* change at tweaks
	* cursor: `yaru`
	* icons: `yaru-red-dark`
	* shell: `yaru-olive-dark`
	* legacy-application: `yaru-red-dark`
---
##### terminal preferrences
 * inside `colors` tab
* scheme: `solarized dark`
	* background: `#003628`
	* terminal-text-color: `#839496`
	* 2nd: (palette color 1) `#E35656`
	* 3rd: (palette color 2) `#957113`
	* 7th: (palette color 6) `#2AA198`
	* 9th: (palette color 8) `#146A09`
* [a plethora of color schemes](https://gogh-co.github.io/Gogh/)
	* 83: Grass
	* 112: Kokuban
	* 132: Mono Green
	* 197: Solarized Dark
	* 05: Adventure Time
* [dracula themes](https://draculatheme.com/gnome-terminal)
---
##### broot
* https://packages.azlux.fr/
---
##### zsh
* `sudo apt-get install zsh`
* `sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"`
* theme: `spaceship`
	* `git clone https://github.com/spaceship-prompt/spaceship-prompt.git "/home/mehdi/.oh-my-zsh/themes/spaceship-prompt" --depth=1`
	* `ln -s "/home/mehdi/.oh-my-zsh/themes/spaceship-prompt/spaceship.zsh-theme" "/home/mehdi/.oh-my-zsh/themes/spaceship.zsh-theme"`
* zsh-syntax-highlighting: `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH}/plugins/zsh-syntax-highlighting`
* zsh-autosuggestions: `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH}/plugins/zsh-autosuggestions`
* zsh-completions
	* `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH}/plugins/zsh-autosuggestions`
	* add this in `.zshrc` before `$ZSH/oh-my-zsh.sh`: `fpath+=${ZSH}/plugins/zsh-completions/src`
* ports: `git clone https://github.com/caarlos0-graveyard/ports ${ZSH}/plugins/ports`
* plugins
	* geeky
		```zsh
		plugins=(
				git
				zsh-interactive-cd  # sudo apt install fzf
				zsh-syntax-highlighting
				zsh-completions
				common-aliases
				compleat
				dirhistory
				django
				docker
				httpie
				vagrant
				pip
				ports
				celery
				command-not-found
				colored-man-pages
				history
					# wd
					# wd add {name}
					# wd !add {name} -> overwrite existing
					# wd {name}      -> change directory
					# wd ..
					# wd ...
					# wd rm {name}
					# wd list        -> ~/.warpc
					# wd ls {name}   -> list files of warp point
					# wd path {name}
					# wd show
					# wd clean       -> remove wd-s to non-existent dirs
				web-search
				copydir
		)
		```
	* noob
		```zsh
		plugins=(
		        git
		        zsh-interactive-cd
		        zsh-syntax-highlighting
		        zsh-autosuggestions
		        zsh-completions
		        common-aliases
		        ports
		        compleat
		        command-not-found
		        history
		)
		```
---
##### depr: pass
* https://www.passwordstore.org/
* https://git.zx2c4.com/password-store/about/
* `sudo apt install pass`
* `sudo apt install pass-extension-tomb`
* `git clone https://github.com/roddhjav/pass-update/`
* `cd pass-update`
* `sudo make install`
* `cd ..`
* `sudo rm -r pass-update`
* `mkdir ~/.password-store`
* `cd ~/.password-store`
* `mkdir .extensions`
* `git clone https://github.com/roddhjav/pass-import/ pass-import-extension`
* `cd pass-import-extension`
* deactivate -> be on local python -> not `system_venv`
* make local \#python3-setuptools \#pip3 yaml
---
##### postgresql
###### install
* `sudo apt install postgresql postgresql-contrib`
* `sudo -u postgres psql`
* `sudo -u postgres createuser --interactive` \#ubuntu user name (`mehdi`)
* `sudo -u postgres createdb mehdi`
* `sudo -u mehdi psql`
* restore databases
###### psycopg2
* `sudo apt install libpq-dev python3-dev`
---
##### depr: sublimetext
* install: [sublimetext.com/docs](https://www.sublimetext.com/docs/linux_repositories.html)
* `wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null`
* `echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list`
* `sudo apt update`
* `sudo apt install sublime-text`
* install package control
	* tools -> package control
* restore settings
---
##### locate
* `sudo apt install locate`
* restore backup `/var/cache/locate/updatedb`
* update indexes: `sudo updatedb`
---
##### depr: tor
* uses socks5
* `sudo apt install tor obfs4proxy tor-geoipdb torsocks`
* get torlogs using `journalctl -extf Tor`
* get tor bridges from https://bridges.torproject.org/
* edit `torrc` and add at the end:
```bash
	UseBridges 1
	ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
	Bridge obfs4 ip:port hash-of-your-obfs4-bridge
```
* `sudo systemctl restart tor@default.service`
* tor port: `9050`
* change tor nodes
```bash
	EntryNodes {ne}, {de}
	ExitNodes {us}, {ne}, {de}
	StrictNodes 1
```
---
##### depr: privoxy
* can port socks5 to http/https
* `sudo apt install privoxy`
* edit `/etc/privoxy/config` -> uncomment/add:
	* `forward-socks5 / 127.0.0.1:9050 .`
* `sudo systemctl enable privoxy.service`
* `sudo systemctl start privoxy.service`
* privoxy port: `8118`
---
##### depr: torsocks
* torify terminal commands
* if torsocks does not work:
	* command does not support socks5
	* use http/https (no need for torsocks):
	* export http_proxy="http://127.0.0.1:8118/"
	* export https_proxy="https://127.0.0.1:8118/"
---
##### syncthing
* `sudo apt install syncthing`
* open web gui with `http://127.0.0.1:8384/`
	* add device `Redmi Note 9 Pro`
	* add folder `~/Documents/Obsidian`
		* share it with phone
		* ignore pattern `.obsidian`
		* advanced
			* `watch for changes`
			* interval `3600s`
			* `Alphabetic` pull order
			* `send`
---
##### depr: Draw.io
* download `.deb` file from github
---
##### depr: [recoll](https://www.lesbonscomptes.com/recoll/pages/index-recoll.html)
* os search utility
* `sudo add-apt-repository ppa:recoll-backports/recoll-1.15-on`
* `sudo apt update`
* `sudo apt isntall recoll`
* `sudo apt install python3-recoll gssp-recoll`
* `sudo apt install poppler-utils` -> for pdftotext
* `sudo apt install pdftk` -> for indexing pdf attachments
* `sudo apt install gir1.2-poppler-0.18` -> for indexing pdf annotations
* `deactivate; pip install epub`
* add this to ULauncher plugins: [`gnome-tracker-extension`][https://github.com/dalanicolai/gnome-tracker-extension]
	* `gnome-text-editor` instead of `gedit`
* settings
	* Index Settings: restore `recoll.conf`
	* `recoll.conf` examle
		 ```sh
		textfilemaxmbs = 50
		topdirs = /etc /home/mehdi/.config /home/mehdi/Bedroom /usr/share/applications \
		/var/redis
		skippedPaths = /etc/alternatives /etc/apparmor.d /etc/brltty /etc/console-setup \
		/etc/fonts /etc/libreoffice /etc/pam.d /etc/sane.d \
		/etc/ssl /etc/X11 /etc/xdg /home/mehdi/.config/Bitwarden \
		/home/mehdi/.config/google-chrome /home/mehdi/.config/JetBrains \
		/home/mehdi/.config/libreoffice /home/mehdi/.config/notion-app-enhanced \
		/home/mehdi/.config/obsidian /home/mehdi/.config/sublime-text \
		/home/mehdi/Bedroom/Backups /home/mehdi/Corridor \
		/home/mehdi/snap /media
		processwebqueue = 1
		webcachekeepinterval = 
		```
	* Crontab
		* days of week = `5` (fri)
		* hours = `9`
		* minutes = `0`
---
##### depr: flathub
* preferably never use this. it's like snap!!
* `sudo apt install flatpak`
* `sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`
---
##### depr: cubic
* `sudo add-apt-repository ppa:cubic-wizard/release`
* `sudo apt install cubic`
---
##### bash completion
* `sudo apt install bash-completion`
* `pip completion --zsh >> ~/.zshrc` or restore `.zshrc`
---
##### useless packages
* `sudo apt purge --autoremove gnome-mines aisleriot gnome-mines gnome-mahjongg gnome-sudoku`
* `sudo apt purge --autoremove thunderbird`
* `sudo apt purge --autoremove transmission-gtk`
* `sudo apt purge --autoremove rhythmbox totem libtotem-plparser18:amd64 libtotem-plparser-common`
---
##### Steam: CSGO
* `sudo apt install steam`
* username: `jesus_chwist`
* password: old typical password
* restore the csgo data