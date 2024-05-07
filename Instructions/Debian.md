##### sudo
* `su -`
* `usermod -aG sudo <username>`
* reboot
---
##### change power options
##### add persian keyboard (with keypad)
##### change timezone
---
##### fix brightness controller
* obviously only if it doesn't work
* `sudo gnome-text-editor /etc/default/grub`
	```bash
	GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor acpi_osi=linux"
	GRUB_CMDLINE_LINUX=""
	```
* `sudo update-grub`
* don't forget to restart
---
##### [nvidia](https://wiki.debian.org/NvidiaGraphicsDrivers)
* add `non-free` and `contrib` to `/etc/apt/sources.list`
* `sudo apt update`
* `sudo apt install linux-headers-amd64`
* `sudo apt install nvidia-driver firmware-misc-non-free`
* reboot
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
	XDG_DESKTOP_DIR="$HOME/Bedroom/Desktop"
	XDG_PICTURES_DIR="$HOME/Bedroom/Pictures"
	XDG_VIDEOS_DIR="$HOME/Bedroom/Videos"
	XDG_DOCUMENTS_DIR="$HOME/Bedroom/Documents"
	```
* `cp -rv /etc/xdg/user-dirs.conf ~/.config/user-dirs.conf`
* `vim ~/.config/user-dirs.conf`
	* `enabled=False`
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
##### apt backports, testing and unstable
* [apt-pinning](https://jaqque.sbih.org/kplug/apt-pinning.html)
* `/etc/apt/sources.list`
```
deb     <url> <dist-name> main contrib non-free non-free-firmware
deb-src <url> <dist-name> main contrib non-free non-free-firmware

deb     <url> <dist-name>-backports main contrib non-free
deb-src <url> <dist-name>-backports main contrib non-free

deb     <url> <dist-name>-security main non-free-firmware
deb-src <url> <dist-name>-security main non-free-firmware

deb     <url> <dist-name>-updates main contrib non-free non-free-firmware
deb-src <url> <dist-name>-updates main contrib non-free non-free-firmware

# apt-pinning
deb <url> stable   main non-free contrib
deb <url> testing  main non-free contrib
deb <url> unstable main non-free contrib
```
* add this line to `/etc/apt/apt.conf.d/70debconf`:
    * `APT::Cache-Limit "100000000";`
* `sudo vim /etc/apt/preferences.d/90non-stable.pref`
```
Package: *
Pin: release a=stable
Pin-Priority: 700

Package: *
Pin: release a=testing
Pin-Priority: 650

Package: *
Pin: release a=unstable
Pin-Priority: 600
```
* `sudo apt update`
##### auto-upgrade
* create this file `/etc/apt/apt.conf.d/20auto-upgrades`:
```
APT::Periodic::Update-Package-Lists "0";
APT::Periodic::Download-Upgradeable-Packages "0";
APT::Periodic::AutocleanInterval "0";
APT::Periodic::Unattended-Upgrade "0";
```
##### upgrade
* `sudo apt update`
* `sudo apt upgrade`
* `sudo apt-get dist-upgrade`
---
##### virtualenvwrapper
* `sudo apt install virtualenvwrapper`
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
* `sudo apt install pv`
* `sudo apt install icdiff`
* `sudo apt install xclip`
* `sudo apt install python3-pip`
* `sudo apt install git curl wget httpie exa vim`
* `sudo apt install fbreader`
* `sudo apt install gparted htop ipython3 testdisk fzf`
* `sudo apt install vlc vlc-l10n vlc-plugin-access-extra vlc-plugin-base vlc-plugin-qt vlc-plugin-video-output vlc-plugin-video-splitter vlc-plugin-visualization`
* `sudo apt install ripgrep fd-find aria2 ipython3 jmtpfs locate`
* `sudo apt install openshot-qt`
* `sudo apt install apt-transport-https ca-certificates gnupg lsb-release`
* `sudo apt install bat exa broot gping duf jq`
* `sudo apt install net-tools traceroute ethtool netstat nmap tcpdump iptraf mtr ncftp yafc lsscsi qbittorrent`
* `sudo apt install rar unrar zip unzip p7zip-full p7zip-rar`
* `sudo apt install redis-tools syncthing neofetch`
* [my tldr-sh-client](https://github.com/mrafee113/tldr-sh-client)
	* alternatively: [`tldr`](https://github.com/raylee/tldr-sh-client)
    * alt2: `sudo apt install tldr`
* `sudo apt install at todotxt-cli`
* `sudo apt install gnome-shell-pomodoro gnome-shell-pomodoro-data`
* `sudo apt install meld` (diff gui)
* `sudo apt install dconf-editor`
* `sudo apt install python3-launchpadlib`
* `sudo apt install mcomix`
* install hakuneko
* install hitomi downloader
* peek: gif video recorder
	* `sudo add-apt-repository ppa:peek-developers/stable`
	* `sudo apt update`
	* `sudo apt install peek`
* discord
	* set push to talk to `Left-Ctrl + Left-Alt`
* virtualbox/vmware
---
##### nekoray
* [releases](https://github.com/Matsuridayo/nekoray/releases)
---
##### ULauncher
```bash
sudo apt update && sudo apt install -y gnupg
gpg --keyserver keyserver.ubuntu.com --recv 0xfaf1020699503176
gpg --export 0xfaf1020699503176 | sudo tee /usr/share/keyrings/ulauncher-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/ulauncher-archive-keyring.gpg] \
          http://ppa.launchpad.net/agornostal/ulauncher/ubuntu jammy main" \
          | sudo tee /etc/apt/sources.list.d/ulauncher-jammy.list
sudo apt update && sudo apt install ulauncher
```
* `sudo apt install ulauncher`
* plugins
	* [file-search](https://github.com/brpaz/ulauncher-file-search)
	* [calculate-anything](https://github.com/tchar/ulauncher-albert-calculate-anything)
	* [ukill](https://github.com/isacikgoz/ukill)
	* [better-file-browser](https://github.com/fisadev/ulauncher-better-file-browser)
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
##### debian settings
* change background
	* `cp -rv [photo] ~/.local/share/backgrounds/`
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
##### gnome-tweaks
* `sudo apt install gnome-tweaks chrome-gnome-shell gnome-shell-extensions`

###### config
* general
	* over-amplification
* apprearance `sudo apt install yaru-theme-gnome-shell yaru-theme-gtk yaru-theme-icon`
	* applications: `Yaru-red-dark`
	* cursor: `Yaru`
	* icons: `Yaru-red-dark`
	* shell: `Yaru-red-dark`
    * Legacy Applications: `Yaru-red-dark`
* top bar
	* date
	* seconds
* window titlebars
	* double-click toggle maximize
	* middle-click minimize
	* secondary-click menu
    * titlebar buttons
        * maximize
        * minimize
        * right

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
	* `%MM %Y/%M/%D`
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
	* fan: cpu
    * fan: gpu
	* temperature: average
	* network: wlp3s0 down
	* network: wlp3s0 up
* impatience
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

##### tilix
* global
	* require \<control\> modifier to edit title on click
	* close window when last session is closed
	* strip first character of paste if comment of variable declaration
    * strip trailing whitespaces and linebreak characters on paste
* appearance
    * window style: normal
    * terminal title style: small
    * tab position: top
    * theme variant: dark
    * default session name: ${title}
    * application title: ${username}@${hostname}:${directory}
    * use a wide handle for splitters
    * place the sidebar on the right
    * show the terminal title even if it's the only terminal
    * use overlay scrollbars
    * use tabs instead of sidebar

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
	* `git clone https://github.com/zsh-users/zsh-completions ${ZSH}/plugins/zsh-completions`
	* add this in `.zshrc` before `$ZSH/oh-my-zsh.sh`: `fpath+=${ZSH}/plugins/zsh-completions/src`
* ports: `git clone https://github.com/caarlos0-graveyard/ports ${ZSH}/plugins/ports`
* [dracula dircolors](https://draculatheme.com/dircolors)
```bash
git clone https://github.com/dracula/dircolors.git /tmp/dircolors
mkdir -p ~/.dir_colors
cp /tmp/dircolors ~/.dir_colors/dracula.dircolors
ln -s /home/<user>/.dir_colors/dracula.dircolors /home/<user>/.dir_colors/dircolors
```
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
##### locate
* `sudo apt install locate`
* restore backup `/var/cache/locate/updatedb`
* update indexes: `sudo updatedb`
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
##### bash completion
* `sudo apt install bash-completion`
* `pip completion --zsh >> ~/.zshrc` or restore `.zshrc`
---
##### Obsidian
* https://obsidian.md/download
---
##### useless packages
```bash
for pkg in \
    gnome-mines gnome-mahjong gnome-sudoku gnome-2048 \
    gnome-weather gnome-maps gnome-klotski gnome-nibbles \
    gnome-robots gnome-taquin gnome-tetravex \
    aisleriot thunderbird transmission-gtk rhythmbox \
    totem libtotem-plparser18:amd64 libtotem-plparser-common \
    evolution five-or-more four-in-a-row hitori lightsoff \
    quadrapassel iagno swell-foop synaptic tali; do

    dpkg-query --status "$pkg" 2>1 >/dev/null
    if [ $? -ne 0 ]; then continue; fi
    
    sudo apt purge --autoremove "$pkg"
done
```
---
##### vim plugins
* install pathogen
* [ansible-vim](https://github.com/pearofducks/ansible-vim) : `git clone https://github.com/pearofducks/ansible-vim ~/.vim/bundle/ansible-vim`
---
##### Etcetera
* Beancount: [[Apps/Beancount#Installation]]
* Vagrant: [[SRE/Vagrant/Installation]]
* Docker: [[SRE/Docker/Installation]]
* Anki: [[Apps/Anki]]
