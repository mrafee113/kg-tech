### Ubuntu
> [source](https://docs.docker.com/engine/install/ubuntu/)

* Before you can install Docker Engine, you must first make sure that any conflicting packages (including older docker packages) are uninstalled.

#### Add Docker apt repo
1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```
2. Add Docker’s official GPG key:
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
3. Use the following command to set up the repository:
```bash
echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu   "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
	sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### Install Docker Engine
1. Update the apt package index:
```bash
sudo apt update
```
2. Install Docker Engine, containerd, and Docker Compose.
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
3. Configure vpn for bypassing Iran's sanctions.
```bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo vim /etc/systemd/system/docker.service.d/proxy.conf
```
```text
## vim proxy.conf
[Service]
Environment="HTTP_PROXY=socks5://192.168.1.105:10808"
Environment="HTTPS_PROXY=socks5://192.168.1.105:10808"
```
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```
4. Verify that the Docker Engine installation is successful by running the `hello-world` image.
```bash
sudo docker login
sudo docker run hello-world
```

* Add user to docker group
```bash
# make sure docker group exists
grep '^docker:' /etc/groups
# if it does not, create it:
sudo groupadd docker
# add user to docker group
sudo usermod -aG docker $USER
# logout & login to update group memberships
```

### Debian
> [source](https://docs.docker.com/engine/install/debian/)
* `sudo apt update`
* `sudo apt install ca-certificates curl gnupg`
* add the official gpg ring
	* `sudo install -m 0755 -d /etc/apt/keyrings`
	* `curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`
	* `sudo chmod a+r /etc/apt/keyrings/docker.gpg`
* set up the repo
	```sh
	echo \
	  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
	  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
	  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	```
* install docker engine
	* `sudo apt update`
	* `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
* configure vpn for bypassing sanctions against iran
	* `sudo mkdir -p /etc/systemd/system/docker.service.d`
	* `sudo vim /etc/systemd/system/docker.service.d/proxy.conf`
	* proxy.conf
		```
			[Service]
			Environment="HTTP_PROXY=socks5://192.168.1.105:10808"
			Environment="HTTPS_PROXY=socks5://192.168.1.105:10808"
		```
	* `sudo systemctl daemon-reload`
	* `sudo systemctl restart docker`
* verify installation
	* `sudo docker login`
	* `sudo docker run hello-world`