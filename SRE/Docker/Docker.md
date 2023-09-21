# Reference
> [source](https://docs.docker.com/reference/)

* [[SRE/Docker/CLI Reference|Docker Command-Line]]
* [[SRE/Docker/Dockerfile Reference|Dockerfile]]
* [[SRE/Docker/Composefile reference/Composefile reference|Composefile]]
* [[SRE/Docker/Installation|Installation]]

# Manuals
> [source](https://docs.docker.com/desktop/)
> The source url seems misleading. But the manuals are stored there. They are accessible through the left pane of the webpage.

* [[SRE/Docker/Compose Manual|Docker Compose]]

## Docker: Get Started
> [source](https://docs.docker.com/get-started/)

##### What is a container?
* Simply put, a container is a sandboxed process on your machine that is isolated from all other processes on the host machine.
* That isolation leverages [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time.
* Docker has worked to make these capabilities approachable and easy to use. To summarize, a container:
	* Is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
	* Can be run on local machines, virtual machines or deployed to the cloud.
	* Is portable (can be run on any OS).
	* Is isolated from other containers and runs its own software, binaries, and configurations.

##### What is a container image?
* When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image.
* Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc.
* The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

# todo
* Concepts
	* Images
	* Containers
	* Artifacts
	* Registries
	* Context
	* Networks
	* Volumes
	* Secrets
* Manuals
	* Networks
	* Storage
* Reference
	* Daemon (dockerd)
* Compose
	* [Compose file build reference](https://docs.docker.com/compose/compose-file/build/)
	* [Compose file deploy reference](https://docs.docker.com/compose/compose-file/deploy/)
	* [Compose CLI Reference](https://docs.docker.com/compose/reference/)

# Old
* commands
	- `docker run [container]`
	  if the image exists, a container will be run. else, it will first be downloaded.
	- `docker ps`
	  lists all containers
	- `docker stop [container name]/[container id]`
	- `docker rm [container]`
	  remove a stopped or exited container permanently
	- `docker images`
	  list available images on our host
	- `docker rmi [image]`
	  to remove an image; no containers should be running off of it
	- `docker pull [image]`
	  to only download image
	- `docker exec [container] [command + args]`
	  to run commands on a running container (os)
	- `docker run -d [container]`
	  run the container in detached mode from the cli
	- `docker attach [container id]`
	  reattach the running container to the cli
	- `docker run -p [os port]:[docker host port] [container]`
	  map a os port to a port in docker host for network access to containers
	- `docker inspect [container]`
	- `docker logs [container]`