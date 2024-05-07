##### Links
* [apps.ankiweb.net](https://apps.ankiweb.net/)
	* [download](https://apps.ankiweb.net/#download)
	* [installing & troubleshooting](https://docs.ankiweb.net/platform/linux/installing.html)

#### Required Packages
* `glibc`: `gcc --version`
* `dpkg -l | grep libwayland-client`
* `dpkg -l | grep systemd`
* `sudo apt install libxcb-xinerama0 libxcb-cursor0 libnss3`
* `sudo apt install zstd`

#### Install
* `tar xaf Downloads/anki-*.tar.zst`
* `cd anki-*`
* `sudo ./install.sh`