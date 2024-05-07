## Docker Command Line
> [source](https://docs.docker.com/engine/reference/commandline/cli/)

* `docker` subcommands
	`attach`, `build`, `builder`, `checkpoint`, `commit`, `config`, `container`, `context`, `cp`, `create`, `diff`, `events`, `exec`, `export`, `history`, `image`, `images`, `import`, `info`, `inspect`, `kill`, `load`, `login`, `logout`, `logs`, `manifest`, `network`, `node`, `pause`, `plugin`, `port`, `ps`, `pull`, `push`, `rename`, `restart`, `rm`, `rmi`, `run`, `save`, `search`, `secret`, `service`, `stack`, `start`, `stats`, `stop`, `swarm`, `system`, `tag`, `top`, `trust`, `unpause`, `update`, `version`, `volume`, `wait`

### `docker inspect`
> [source](https://docs.docker.com/engine/reference/commandline/inspect/)

* Return low-level information on docker objects
* usage: `docker inspect [OPTIONS] NAME|ID [NAME|ID...]`
* Docker inspect provides detailed information on constructs controlled by Docker.
* By default, `docker inspect` will render results in a JSON array.
* options
	* `--format/-f` format output using a custom template
	* `--size/-s` : display total file sizes if the type is container
		* This adds two additional fields to the `docker inspect` output. This option only works for containers. The container doesn’t have to be running.
		* The two additional fields:
			* `SizeRootFs`: the total size of all the files in the container, in bytes.
			* `SizeRw`: the size of the files that have been created or changed in the container, compared to it’s image, in bytes.
	* `--type` : return json for specified type
		* `container|image|node|network|secret|service|volume|task|plugin`
		* The `docker inspect` command matches any type of object by either ID or name. In some cases multiple type of objects (for example, a container and a volume) exist with the same name, making the result ambiguous.
		* To restrict `docker inspect` to a specific type of object, use the `--type` option.

### `docker events`
> [source](https://docs.docker.com/engine/reference/commandline/events/)

* Get real time events from the server
* usage: `docker events [OPTIONS]`
* **Note**: The difference between `docker events` and `docker logs` as I've come to understand, is that events are logs that are produced by docker itself. And logs are produced by docker containers.
* Use `docker events` to get real-time events from the server. These events differ per Docker object type. Different event types have different scopes. Local scoped events are only seen on the node they take place on, and swarm scoped events are seen on all managers.
* Only the last 1000 log events are returned. You can use filters to further limit the number of events returned.
* **Warning**: For the rest of command explanation, examples, and options, refer to the source.

### `docker commit`
> [source](https://docs.docker.com/engine/reference/commandline/commit/)

* Create a new image from a container's changes
* usage: `docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]`
* It can be useful to commit a container’s file changes or settings into a new image. This allows you to debug a container by running an interactive shell, or to export a working dataset to another server. Generally, it is better to use Dockerfiles to manage your images in a documented and maintainable way.
* The commit operation will not include any data contained in volumes mounted inside the container.
* options
	* `--author/-a` : e.g. `Jogn Hannibal Smith <hannibal@a-team.com>`
	* `--change/-t` : apply Dockerfile instruction to the created image
		* The `--change` option will apply `Dockerfile` instructions to the image that is created. Supported `Dockerfile` instructions: `CMD`|`ENTRYPOINT`|`ENV`|`EXPOSE`|`LABEL`|`ONBUILD`|`USER`|`VOLUME`|`WORKDIR`
	* `--message/-m` : commit message
	* `--pause/-p` : pause container during commit
		* By default, the container being committed and its processes will be paused while the image is committed. This reduces the likelihood of encountering data corruption during the process of creating the commit. If this behavior is undesired, set the `--pause` option to false.

### `docker context`
> [source](https://docs.docker.com/engine/reference/commandline/context/)

* Manage contexts.
* usage: `docker context COMMAND`
* commands
	* [`create`](https://docs.docker.com/engine/reference/commandline/context_create/)
	* [`export`](https://docs.docker.com/engine/reference/commandline/context_export/)
	* [`import`](https://docs.docker.com/engine/reference/commandline/context_import/)
	* [`inspect`](https://docs.docker.com/engine/reference/commandline/context_inspect/)
	* [`ls`](https://docs.docker.com/engine/reference/commandline/context_ls/)
	* [`rm`](https://docs.docker.com/engine/reference/commandline/context_rm/)
	* [`show`](https://docs.docker.com/engine/reference/commandline/context_show/)
	* [`update`](https://docs.docker.com/engine/reference/commandline/context_update/)
	* [`use`](https://docs.docker.com/engine/reference/commandline/context_use/)

### `docker info`
> [source](https://docs.docker.com/engine/reference/commandline/info/)

* Display system-wide information
* usage: `docker info [OPTIONS]`
* This command displays system wide information regarding the Docker installation. Information displayed includes the kernel version, number of containers and images. The number of images shown is the number of unique images. The same image tagged under different names is counted only once.
* Depending on the storage driver in use, additional information can be shown, such as pool name, data file, metadata file, data space used, total data space, metadata space used,`` and total metadata space.
* The data file is where the images are stored and the metadata file is where the meta data regarding those images are stored. When run for the first time Docker allocates a certain amount of data space and meta data space from the space available on the volume where `/var/lib/docker` is mounted.
* `--format/-f` : format output using a custom template

### `docker wait`
> [source](https://docs.docker.com/engine/reference/commandline/wait/)

* Block until one or more containers stop, then print their exit codes
* usage: `docker wait CONTAINER [CONTAINER...]`

### `docker image`
> [source](https://docs.docker.com/engine/reference/commandline/image/)

* Manage images
* usage: `docker image COMMAND`
* repetetive subcommands found in `docker` subcommands
	`build`, `history`, `import`, `inspect`, `load`, `ls`, `pull`, `push`, `rm`, `save`, `tag`

#### `docker pull`
> [source](https://docs.docker.com/engine/reference/commandline/pull/)

* Download an image from a registry
* usage: `docker pull [OPTIONS] NAME[:TAG|@DIGEST]`
* Most of your images will be created on top of a base image from the [Docker Hub](https://hub.docker.com/) registry.
* [Docker Hub](https://hub.docker.com/) contains many pre-built images that you can `pull` and try without needing to define and configure your own.
* To download a particular image, or set of images (i.e., a repository), use `docker pull`.
* **Proxy Configuration**: If you are behind an HTTP proxy server, for example in corporate settings, before open a connect to registry, you may need to configure the Docker daemon’s proxy settings, refer to the [dockerd command-line reference](https://docs.docker.com/engine/reference/commandline/dockerd/#proxy-configuration) for details.
* **Concurrent Downloads**: By default the Docker daemon will pull three layers of an image at a time. If you are on a low bandwidth connection this may cause timeout issues and you may want to lower this via the `--max-concurrent-downloads` daemon option. See the [daemon documentation](https://docs.docker.com/engine/reference/commandline/dockerd/) for more details.
* options
	* `--all-tags/-a` : download all tagged images in the repository
	* `--disable-content-trust` : *default=true*. skip image verification
	* `--quiet/-q` : suppress verbose output

#### `docker image prune`
> [source](https://docs.docker.com/engine/reference/commandline/image_prune/)

* Remove unused images
* usage: `docker image prune [OPTIONS]`
* Remove all dangling images. If `-a` is specified, will also remove all images not referenced by any container.
* options
	* `--all/-a` : remove all unused images, not just dangling ones
	* `--filter` : provide filter values (e.g. `until=<timestamp>`)
	* `--force/-f` : do not prompt for confirmation

#### `docker images`
> [source](https://docs.docker.com/engine/reference/commandline/images/)

* List images
* usage: `docker images [OPTIONS] [REPOSITORY[:TAG]]`
* The default `docker images` will show all top level images, their repository and tags, and their size.
* Docker images have intermediate layers that increase reusability, decrease disk usage, and speed up `docker build` by allowing each step to be cached. These intermediate layers are not shown by default.
* options
	* `--all/-a` : show all images (default hides intermediate images)
	* `--filter/-f` : filter output based on a condition provided
	* `--format` : format output based on a custom template
	* `--no-trunc` : list full-length image IDs
	* `--quiet/-q` : only show image IDs
	* `--digests` : show image digests
		* Images that use the v2 or later format have a content-addressable identifier called a `digest`. As long as the input used to generate the image is unchanged, the digest value is predictable.

#### `docker build`
> [source](https://docs.docker.com/engine/reference/commandline/build/)

* Build an image from a Dockerfile
* usage: `docker build [OPTIONS] PATH | URL | -`
* The `docker build` command builds Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified `PATH` or `URL`. The build process can refer to any of the files in the context. For example, your build can use a [_COPY_](https://docs.docker.com/engine/reference/builder/#copy) instruction to reference a file in the context.
* options
	* `--add-hosts=[host]:[ip]` : adds `host ip` to `/etc/hosts` file
	* `--disable-content-trust` : *default=true*. skips image verification
	* `--file/-f` : *default=`PATH/Dockerfile`*. **name** of the Dockerfile
	* `--label` : set metadata for an image
	* `--memory/-m` : memory limit
	* `--network` : set the networking mode for the run instructions during build
	* `--rm` : *default=true*. remove intermediate containers after a successful build
	* `--force-rm` : always remove intermediate containers
	* `--tag/-t` : name and optionally a tag in the `name:tag` format. can be used multiple times.
	* `--build-arg [var-name]=[var-value]`
		* This passes variables to docker **during** the build process.
		* Unlike Dockerfile ENV instruction, these variables will not persists in the image containers.
		* You can use it multiple times.
	* `--target [stage-name]`
		* Sets a multi-staged Dockerfile stage as a final stage to conclude the build of an image.
	* `--output` [this](https://docs.docker.com/engine/reference/commandline/build/#output) chooses the default behavior of createing images as a result. like creating tarballs or sth. 
	* there are also some other cpu and memory limiting options
* `.dockerignore` can be used in the *context* to avoid using some things in the image

#### `docker builder prune`
> [source](https://docs.docker.com/engine/reference/commandline/builder_prune/)

* Remove build cache
* usage: `docker builder prune`
* options
	* `--all/-a` : remove all unused build cache, not just dangling ones
	* `--filter` : e.g. `until=24h`
	* `--force/-f` : don't prompt for confirmation

#### `docker history`
> [source](https://docs.docker.com/engine/reference/commandline/history/)

* Show the history of an image
* usage: `docker history [OPTIONS] IMAGE`
* options
	* `--format` : format output using a custom template
	* `--human/-H` : *default=true*. print sizes and dates in human readable format
	* `--no-trunc` : don't truncate output
	* `--quiet/-q` : only show image IDs

#### `docker load`
> [source](https://docs.docker.com/engine/reference/commandline/load/)

* Load an image from a tar archive or STDIN
* usage: `docker load [OPTIONS]`
* Load an image or repository from a tar archive (even if compressed with gzip, bzip2, or xz) from a file or STDIN. It restores both images and tags.
* options
	* `--input/-i` : read from tar archive file instead of STDIN
	* `--quiet/-q` : suppress the load output
* The difference between this and `docker import` as explained by ChatGPT, is that `docker export` does not preserve container history or metadata. It creates a new image with a new ID. `docker save` on the other hand saves the image and its metadata including, layers, tags, and history.

#### `docker save`
> [source](https://docs.docker.com/engine/reference/commandline/save/)

* Save one or more images to a tar archive (streamed to STDOUT by default)
* usage: `docker save [OPTIONS] IMAGE [IMAGE...]`
* Produces a tarred repository to the standard output stream. Contains all parent layers, and all tags + versions, or specified `repo:tag`, for each argument provided.
* `--output/-o` : write to a file instead of STDOUT

#### `docker rmi`
> [source](https://docs.docker.com/engine/reference/commandline/rmi/)

* Remove one or more images
* usage: `docker rmi [OPTIONS] IMAGE [IMAGE...]`
* Removes (and un-tags) one or more images from the host node.
* If an image has multiple tags, using this command with the tag as a parameter only removes the tag.
*  If the tag is the only one for the image, both the image and the tag are removed.
* This does not remove images from a registry.
* You cannot remove an image of a running container unless you use the `-f` option.
* options
	* `--force/-f`
	* `--no-prune` : do not delete untagged parents

#### `docker search`
> [source](https://docs.docker.com/engine/reference/commandline/search/)

* Search [docker hub](https://hub.docker.com/?_gl=1*17g0aeb*_ga*MTU0Nzg1NDQwMi4xNjg2MDMzMTQ5*_ga_XJWPQMJYHQ*MTY4NjM4MjMzNy4xNi4xLjE2ODYzODIzNDEuNTYuMC4w) for images
* usage: `docker search [OPTIONS] TERM`
* options
	* `--filter/-f`
	* `--format` : pretty print search using a Go template
	* `--limit` : max number of results
	* `--no-trunc`

#### `docker tag`
> [source](https://docs.docker.com/engine/reference/commandline/tag/)

* Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
* usage: `docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`
* A full image name has the following format and components:
	* `[HOST[:PORT_NUMBER]/]PATH`
	* `HOST` : The optional registry hostname specifies where the image is located. The hostname must comply with standard DNS rules, but may not contain underscores. If the hostname is not specified, the command uses Docker’s public registry at `registry-1.docker.io` by default. Note that `docker.io` is the canonical reference for Docker’s public registry.
	* `PORT_NUMBER` : If a hostname is present, it may optionally be followed by a registry port number in the format `:8080`.
	* `PATH`
		* The path consists of slash-separated components.
		* Each component may contain lowercase letters, digits and separators. A separator is defined as a period, one or two underscores, or one or more hyphens.
		* A component may not start or end with a separator.
		* While the [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec) supports more than two slash-separated components, most registries only support two slash-separated components.
		* For Docker’s public registry, the path format is as follows:
			* `[NAMESPACE/]REPOSITORY` : The first, optional component is typically a user’s or an organization’s namespace. The second, mandatory component is the repository name. When the namespace is not present, Docker uses `library` as the default namespace.
* After the image name, the optional `TAG` is a custom, human-readable manifest identifier that is typically a specific version or variant of an image.
	* The tag must be valid ASCII and can contain lowercase and uppercase letters, digits, underscores, periods, and hyphens. 
	* It cannot start with a period or hyphen and must be no longer than 128 characters.
	* If the tag is not specified, the command uses `latest` by default.

### `docker container`
* manage containers
* repetetive subcommands found in `docker` subcommands
	`attach`, `commit`, `cp`, `create`, `diff`, `exec`, `export`, `inspect`, `kill`, `logs`, `ls`, `pause`, `port`, `rename`, `restart`, `rm`, `run`, `start`, `stats`, `stop`, `top`, `unpause`, `update`, `wait`

#### `docker container prune`
> [source](https://docs.docker.com/engine/reference/commandline/container_prune/)

* Remove all stopped containers
* usage: `docker container prune [OPTIONS]`
* options
	* `--filter` :  [it](https://docs.docker.com/engine/reference/commandline/container_prune/#filter) filters, e.g. `until=<timestamp>`
	* `--force/-f` : do not prompt for confirmation

#### `docker ps`
> [source](https://docs.docker.com/engine/reference/commandline/ps/)

* List containers
* usage: `docker ps [OPTIONS]`
* options
	* `--all/-a` : show all containers (default shows just running)
	* `--filter/-f` : filter output based on condition provided
		* `id`
		* `name`
		* `label`
		* `exited` : an integer representing the container's exit code
		* `status` : one of `created`, `restarting`, `running`, `removing`, `paused`, `exited`, or `dead`
		* `ancestor` : filters containers which share a given image as an ancestor. Expressed as `<image-name>[:<tag>]`, `<image id>`, or `<image@digest>`
		* `before` or `since` : filters containers created before or after a given container ID or name
		* `volume`
		* `network`
		* `publish` or `expose` : filters containers which publish or expose a given port. Expressed as `<port>[/<proto>]` or `<startport-endport>/[<proto>]`
		* `health` : filters containers based on their healthcheck status. One of `starting`, `healthy`, `unhealthy` or `none`
		* `is-task` : filters containers that are a “task” for a service. Boolean option (`true` or `false`)
	* `--format` : format using a custom template
		* `.ID`
		* `.Image` : image ID
		* `.Command`
		* `.CreatedAt`
		* `.RunningFor`
		* `.Ports`
		* `.State` : container status
		* `.Status` : container status with details about duration and health-status
		* `.Size`
		* `.Names`
		* `.Labels`
		* `.Mounts` : names of the volumes mounted on this container
		* `.Networks` : names of the networks attached to this container
	* `--last/-n` : *default:`-1`*. show n last created containers (includes all states)
	* `--latest/-l` : show the latest created container
	* `--no-trunc`
	* `--quiet/-q`
	* `--size/-s` : display total file sizes
	
#### `docker create`
> [source](https://docs.docker.com/engine/reference/commandline/create/)

* Create a new container
* usage: `docker create [OPTIONS] IMAGE [COMMAND] [ARG...]`
* The `docker container create` (or shorthand: `docker create`) command creates a new container from the specified image, without starting it.
* When creating a container, the docker daemon creates a writeable container layer over the specified image and prepares it for running the specified command. The container ID is then printed to `STDOUT`. This is similar to `docker run -d` except the container is never started. You can then use the `docker container start` (or shorthand: `docker start`) command to start the container at any point.
* This is useful when you want to set up a container configuration ahead of time so that it is ready to start when you need it. The initial status of the new container is `created`.
* The `docker create` command shares most of its options with the `docker run` command (which performs a `docker create` before starting it).
* options: refer to `docker run` reference

#### `docker logs`
> [source](https://docs.docker.com/engine/reference/commandline/logs/)

* Fetch the logs of a container
* usage: `docker logs [OPTIONS] CONTAINER`
* The `docker logs` command batch-retrieves logs present at the time of execution.
* For more information about selecting and configuring logging drivers, refer to [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/).
* The `docker logs --details` command will add on extra attributes, such as environment variables and labels, provided to `--log-opt` when creating the container.
* options
	* `--details`
		* This will add on extra attributes, such as environment variables and labels, provided to `--log-opt` when creating the container.
	* `--follow/-f` : follow log output (continuous stream)
	* `--since` : e.g. `2013-01-02T13:23:37Z` e.g. `42m`
	* `--until`
	* `--tail/-n` : *default=`all`*
	* `--timestamps/-t` : show timestamps

#### `docker attach`
> [source](https://docs.docker.com/engine/reference/commandline/attach/)

* Attach local standard input, output, and error streams to a running container
* usage: `docker attach [options] CONTAINER`
* Use `docker attach` to attach your terminal’s standard input, output, and error (or any combination of the three) to a running container using the container’s ID or name. This allows you to view its ongoing output or to control it interactively, as though the commands were running directly in your terminal.

> [!Note]
> The `attach` command will display the output of the `ENTRYPOINT/CMD` process. This can appear as if the attach command is hung when in fact the process may simply not be interacting with the terminal at that time.

* You can attach to the same contained process multiple times simultaneously, from different sessions on the Docker host.
* `--no-stdin` = do not attach STDIN

#### `docker cp`
> [source](https://docs.docker.com/engine/reference/commandline/cp/)

* Copy files/folders between a container and the local filesystem
* usage *copy from*: `docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-`
* usage *copy to*: `docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH`
* The `docker cp` utility copies the contents of `SRC_PATH` to the `DEST_PATH`. You can copy from the container’s file system to the local machine or the reverse, from the local filesystem to the container.
* If `-` is specified for either the `SRC_PATH` or `DEST_PATH`, you can also stream a tar archive from `STDIN` or to `STDOUT`.
* The `CONTAINER` can be a running or stopped container.
*  The `SRC_PATH` or `DEST_PATH` can be a file or directory.
* The `docker cp` command assumes container paths are relative to the container’s `/` (root) directory. This means supplying the initial forward slash is optional.
* The `cp` command behaves like the Unix `cp -a` command in that directories are copied recursively with permissions preserved if possible. Ownership is set to the user and primary group at the destination. For example, files copied to a container are created with `UID:GID` of the root user. Files copied to the local machine are created with the `UID:GID` of the user which invoked the `docker cp` command.
* options
	* `--archive/-a` : archive mode (copy all uid/gid info)
	* `--follow-link/-L` : always follow symbolic links in `SRC_PATH`
	* `--quiet/-q` : suppress progress output during copy. Progress output is automatically suppressed if no terminal is attached
* It is not possible to copy certain system files such as resources under `/proc`, `/sys`, `/dev`, [tmpfs](https://docs.docker.com/engine/reference/commandline/run/#tmpfs), and mounts created by the user in the container.

#### `docker diff`
> [source](https://docs.docker.com/engine/reference/commandline/diff/)

* Inspect changes to files or directories on a container’s filesystem
* usage: `docker diff CONTAINER`
* List the changed files and directories in a container᾿s filesystem since the container was created. Three different types of change are tracked:
	* `A` : a file or directory was added
	* `D` : a file or directory was deleted
	* `C` : a file or directory was changed
* You can use the full or shortened container ID or the container name set using `docker run --name` option.

#### `docker exec`
> [source](https://docs.docker.com/engine/reference/commandline/exec/)

* Execute a command in a running container
* usage: `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]`
* The `docker exec` command runs a new command in a running container.
* The command started using `docker exec` only runs while the container’s primary process (`PID 1`) is running, *and it is not restarted if the container is restarted*.
* `COMMAND` runs in the default directory of the container. If the underlying image has a custom directory specified with the WORKDIR directive in its Dockerfile, this directory is used instead.
* `COMMAND` must be an executable. A chained or a quoted command does not work. For example, `docker exec -it my_container sh -c "echo a && echo b"` does work, but `docker exec -it my_container "echo a && echo b"` does not.
* options
	* `--detach/-d` : run command in the background
	* `--env/-e` : set environment variables
	* `--env-file` : read in a file of environment variables
	* `--interactive/-i` : keep STDIN open even if not attached
	* `--privileged` : give extended privileges to the command
	* `--tty/-t` : allocate a pseudo-TTY
	* `--user/-u` : username or uid `<name|uid>[:<group|gid>]`
	* `--workdir/-w` : working directoryy inside the container

#### `docker import`
> [source](https://docs.docker.com/engine/reference/commandline/import/)

* Import the contents from a tarball to create a filesystem image
* usage: `docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]`
* options
	* `--change/-c` : apply Dockerfile instructions to the created image
	* `--message/-m` : set commit message for imported image

#### `docker export`
> [source](https://docs.docker.com/engine/reference/commandline/export/)

* Export a container’s filesystem as a tar archive
* usage: `docker export [OPTIONS] CONTAINER`
* The `docker export` command does not export the contents of volumes associated with the container. If a volume is mounted on top of an existing directory in the container, `docker export` will export the contents of the _underlying_ directory, not the contents of the volume.
* Refer to [Backup, restore, or migrate data volumes](https://docs.docker.com/storage/volumes/#back-up-restore-or-migrate-data-volumes) in the user guide for examples on exporting data in a volume.
* `--output/-o` : write to a file instead of STDOUT

#### `docker kill`
> [source](https://docs.docker.com/engine/reference/commandline/kill/)

* Kill one or more running containers
* usage: `docker kill [OPTIONS] CONTAINER [CONTAINER...]`
* The `docker kill` subcommand kills one or more containers. The main process inside the container is sent `SIGKILL` signal (default), or the signal that is specified with the `--signal` option.
* `--signal/-s` signal to send the container

#### `docker pause`
> [source](https://docs.docker.com/engine/reference/commandline/pause/)

* Pause all processes within one or more containers
* usage: `docker pause CONTAINER [CONTAINER...]`
* The `docker pause` command suspends all processes in the specified containers.
* On Linux, this uses the freezer cgroup.
* Traditionally, when suspending a process the `SIGSTOP` signal is used, which is observable by the process being suspended. With the freezer cgroup the process is unaware, and unable to capture, that it is being suspended, and subsequently resumed.See the [freezer cgroup documentation](https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt) for further details.

#### `docker unpause`
> [source](https://docs.docker.com/engine/reference/commandline/unpause/)

* Unpause all processes within one or more containers
* usage: `docker unpause CONTAINER [CONTAINER...]`
* The `docker unpause` command un-suspends all processes in the specified containers. On Linux, it does this using the freezer cgroup.
* See the [freezer cgroup documentation](https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt) for further details.

#### `docker port`
> [source](https://docs.docker.com/engine/reference/commandline/port/)

* List port mappings or a specific mapping for the container
* usage: `docker port CONTAINER [PRIVATE_PORT[/PROTO]]`

#### `docker rename`
> [source](https://docs.docker.com/engine/reference/commandline/rename/)

* Rename a container
* usage: `docker rename CONTAINER NEW_NAME`

#### `docker restart`
> [source](https://docs.docker.com/engine/reference/commandline/restart/)

* Restart one or more containers
* usage: `docker restart [OPTIONS] CONTAINER [CONTAINER...]`
* options
	* `--signal/-s` : signal to send to the container
	* `--time/-t` : seconds to wait before killing the container

#### `docker rm`
> [source](https://docs.docker.com/engine/reference/commandline/rm/)

* Remove one or more containers
* usage: `docker rm [OPTIONS] CONTAINER [CONTAINER...]`
* options
	* `--force/-f` : force the removal of a running container (uses SIGKILL)
	* `--link/-l` : remove the specified link
	* `--volumes/-v` : remove anynymous volumes associated with the container

#### `docker start`
> [source](https://docs.docker.com/engine/reference/commandline/start/)

* Start one or more stopped containers
* usage: `docker start [OPTIONS] CONTAINER [CONTAINER...]`
* options
	* `--attach/-a`
	* `--detach-keys`
	* `--interactive/-i`

#### `docker stop`
> [source](https://docs.docker.com/engine/reference/commandline/stop/)

* Stop one or more running containers
* usage: `docker stop [OPTIONS] CONTAINER [CONTAINER...]`
* The main process inside the container will receive `SIGTERM`, and after a grace period, `SIGKILL`. The first signal can be changed with the `STOPSIGNAL` instruction in the container’s Dockerfile, or the `--stop-signal` option to `docker run`.
* options
	* `--signal/-s` : signal to send to the container
	* `--time/-t` : seconds to wait before killing the container

#### `docker stats`
> [source](https://docs.docker.com/engine/reference/commandline/stats/)

* Display a live stream of container(s) resource usage statistics
* usage: `docker stats [OPTIONS] [CONTAINERS...]`
* The `docker stats` command returns a live data stream for running containers. You can specify a stopped container but stopped containers do not return any data.
* If you need more detailed information about a container’s resource usage, use the `/containers/(id)/stats` API endpoint.

> [!Note]
> The `PIDS` column contains the number of processes and kernel threads created by that container. Threads is the term used by Linux kernel. Other equivalent terms are “lightweight process” or “kernel task”, etc. A large number in the `PIDS` column combined with a small number of processes (as reported by `ps` or `top`) may indicate that something in the container is creating many threads.

* options
	* `--all/-a` : show all containers (default just shows running)
	* `--format`
	* `--no-stream` : disable streaming stats and only print the first result
	* `--no-trunc` : do not truncate output

#### `docker top`
> [source](https://docs.docker.com/engine/reference/commandline/top/)

* Display the running processes of a container
* usage: `docker top CONTAINER [ps OPTIONS]`

#### `docker update`
> [source](https://docs.docker.com/engine/reference/commandline/update/)

* Update configuration of one or more containers
* usage: `docker update [OPTIONS] CONTAINER [CONTAINER...]`
* The `docker update` command dynamically updates container configuration. You can use this command to prevent containers from consuming too many resources from their Docker host. With a single command, you can place limits on a single container or on many. To specify more than one container, provide space-separated list of container names or IDs.
* With the exception of the `--kernel-memory` option, you can specify these options on a running or a stopped container. On kernel version older than 4.6, you can only update `--kernel-memory` on a stopped container or on a running container with kernel memory initialized.
* options comprise hardware limitations

#### `docker run`
> [source](https://docs.docker.com/engine/reference/commandline/run/)

* Create and run a new container from an image
* usage: `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
* The `docker run` command runs a command in a new container, pulling the image if needed and starting the container.
* options
	* `--workdir/-w` : working dir inside the container
	* `--attach/-a` : attach to STDIN, STDOUT or STDERR
	* `--detach/-d` : run container in background and print container ID
	* `--detach-keys` : override the key sequence for detaching a container
	* `--env/-e`
	* `--env-file` : read in a file of environment variables
	* `--add-host` : adda a custom host-to-ip mapping `host:ip`
	* `--hostname/-h` : container host name
	* `--interactive/-i` : keep STDIN open even if not attached
	* `--ip`
	* `--ip6`
	* `--label/-l` : set meta data on a container
	* `--label-file` : read in a line delimited file of labels
	* `--link` : add link to another container
	* `--link-local-ip` :? container ipv4/ipv6 link-local addresses
	* `--mount` : attach a filesystem mount
	* `--name`
	* `--network`
	* `--network-alias` : add network-scoped alias for the container
	* `--privileged` : give extended privileges to this container
	* `--rm` : automatically remove the container, when it exits
	* `--tty/-t` : allocate a pseudo-TTY
	* `--volume/-v` : bind mount a volume
	* `--volumes-from` : mount volumes from the specified container(s)
	* `--cgroup-parent` :? optional parent cgroup for the container
	* `--cidfile` : write the container ID to the file
	* there are some `cpu` related options :)
	* `--device` :? add a host device to the container
	* there are also more options for `device`
	* `--disable-content-trust` : *default=true*. skip image verification
	* there are some options for `dns`
	* `--entrypoint` : override the default `ENTRYPOINT` of the image
	* `--expose` : expose a port or a range of ports
	* `--group-add` :? add additional groups to join
	* there are some options for `health`
	* `--help`
	* `--init` :? run an init inside the container that forwards signals and reaps processes
	* there are some `io` options available
	* `--isolation` :? container isolation technology
	* there are some `memory` options
	* `--publish/-p` :? publish a container's port to the host
	* `--publish-all/-P` :? publish all container's ports to random ports
	* `--pull` : *default=`missing`*. pull image before running: `always`, `missing`, `never`
	* `--quiet/-q` : suppress the pull output
	* `--read-only` : mount the container's root filesystem as read-only
	* `--restart` : *default=`no`*. restart policy apply when a container exits
	* `--runtime` : runtime to use for this container
	* `--security-opt`
	* `--sig-proxy` : *default=true*. proxy received signals to the process
	* `--stop-signal` : signal to stop the container
	* `--stop-timeout` : timeout to stop a container
	* `--user/-u` : username or UID `<name|uid>[:<group|gid>]`
	* `--userns` : user namespace to use
	* `--volume-driver`

### `docker network`
> [source](https://docs.docker.com/engine/reference/commandline/network/)

* Manage networks
* usage: `docker network COMMAND`

#### `docker network connect`
> [source](https://docs.docker.com/engine/reference/commandline/network_connect/)

* Connect a container to a network
* usage: `docker network connect [OPTIONS] NETWORK CONTAINER`
*  You can connect a container by name or by ID.
* Once connected, the container can communicate with other containers in the same network.
* options
	* `--alias` : add network-scoped alias for the container
	* `--driver-opt` : driver options for the network
	* `--ip` : ipv4 addr
	* `--ipv6` : ipv6 addr
	* `--link` : add link to another container
	* `--link-local-ip` : add a link-local address for the container

#### `docker network create`
> [source](https://docs.docker.com/engine/reference/commandline/network_create/)

* Create a network
* usage: `docker network create [OPTIONS] NETWORK`
* options
	* `--driver/-d` : *default=`bridge`*.
		* The `DRIVER` accepts `bridge` or `overlay` which are the built-in network drivers.
		* If you have installed a third party or your own custom network driver you can specify that `DRIVER` here also.
		* If you don’t specify the `--driver` option, the command automatically creates a `bridge` network for you.
		* When you install Docker Engine it creates a `bridge` network automatically. This network corresponds to the `docker0` bridge that Engine has traditionally relied on.
		* When you launch a new container with `docker run` it automatically connects to this bridge network.
		* You cannot remove this default bridge network, but you can create new ones using the `network create` command.
		* Bridge networks are isolated networks on a single Engine installation.
		* If you want to create a network that spans multiple Docker hosts each running an Engine, you must enable Swarm mode, and create an `overlay` network. To read more about overlay networks with Swarm mode, see [“_use overlay networks_”](https://docs.docker.com/network/overlay/).
	* `--label` : set metadata on a network
	* `--opt/-o` : set driver specific options
	* `--attachable` :? enable manual container attachment
	* `--aux-address` :? auxiliary ipv4 or ipv6 addresses used by network driver
	* `--config-from` : the network from which to copy the configuration
	* `--config-only` :? create a configuration only network
	* `--gateway` : ip gateway for the master subnet
	* `--internal` : restrict external access to the network
	* `--ip-range` : allocate container ip from a sub-range
	* `--ipam-driver` :? ip address management driver
	* `--ipam-opt`
	* `--ipv6` : enable ipv6 networking
	* `--scope`
	* `--subnet` : subnet in CIDR format that represents a network segment

#### `docker network disconnect`
> [source](https://docs.docker.com/engine/reference/commandline/network_disconnect/)

* Disconnect a container from a network
* usage: `docker network disconnect [OPTIONS] NETWORK CONTAINER`
* Disconnects a container from a network. The container must be running to disconnect it from the network.
* `--force/-f` : force the container to disconnect from a network

#### `docker network ls`
> [source](https://docs.docker.com/engine/reference/commandline/network_ls/)

* List networks
* usage: `docker network ls [OPTIONS]`
* Lists all the networks the Engine `daemon` knows about. This includes the networks that span across multiple hosts in a cluster.
* options
	* `--filter/-f` : provide filter values e.g. `driver=bridge`
	* `--format` : format output using a custom template
	* `--no-trunc` : do not truncate the output
	* `--quiet/-q` only display network IDs

#### `docker network prune`
> [source](https://docs.docker.com/engine/reference/commandline/network_prune/)

* Remove all unused networks
* usage: `docker network prune [OPTIONS]`
* Remove all unused networks. Unused networks are those which are not referenced by any containers.
* options
	* `--filter` : provide filter values
	* `--force/-f` : do not prompt for confirmation

#### `docker network rm`
> [source](https://docs.docker.com/engine/reference/commandline/network_rm/)

* Remove one or more networks
* usage: `docker network rm NETWORK [NETWORK...]`
* Removes one or more networks by name or identifier. To remove a network, you must first disconnect any containers connected to it.
* `--force/-f` : do not error if the network does not exist

### `docker volume`
> [source](https://docs.docker.com/engine/reference/commandline/volume/)

* Manage volumes
* usage: `docker volume COMMAND`
* Manage volumes. You can use subcommands to create, inspect, list, remove, or prune volumes.

#### `docker volume create`
> [source](https://docs.docker.com/engine/reference/commandline/volume_create/)

* Create a volume
* usage: `docker volume create [OPTIONS] [VOLUME]`
* Creates a new volume that containers can consume and store data in. If a name is not specified, Docker generates a random name.
* options
	* `--availability` : *default=`active`*. cluster volume availability: `active`, `pause`, `drain`
	* `--driver/-d` : *default=`local`*. specify volume driver name
	* `--group` : cluster volume group
	* `--label` : set metadata for a volume
	* `--limit-bytes` : minimum size of the cluster volume in bytes
	* `--required-bytes` : maximum size of the cluster volume in bytes
	* `--opt/-o` : driver options
	* `--scope` : *default=`single`*. cluster volume access scope: `single`, `multi`
	* `--secret`
	* `--sharing` : *default=`none`.* cluster volume access sharing: `none`, `readonly`, `onewriter`, `all`
	* `--type` : *default=`block`*. cluster volume access type: `block`, `mount`

#### `docker volume ls`
> [source](https://docs.docker.com/engine/reference/commandline/volume_ls/)

* List volumes
* usage: `docker volume ls [OPTIONS]`
* options
	* `--cluster` : display only cluster volumes. and use cluster volume list formatting.
	* `--filter/-f`
		* `dangling` : boolean. `true`, `false`, `0`, `1`
		* `driver`
		* `label` : `label=<key>` or `label=<key>=<value>`
		* `name`
	* `--format`
	* `--quiet/-q`

#### `docker volume prune`
> [source](https://docs.docker.com/engine/reference/commandline/volume_prune/)

* Remove all unused local volumes
* usage: `docker volume prune [OPTIONS]`
* Remove all unused local volumes. Unused local volumes are those which are not referenced by any containers. By default, it only removes anonymous volumes.
* options
	* `--all/-a` : remove all unsed volumes, not just anonymous ones
	* `--filter`
	* `--force/-f`

#### `docker volume rm`
> [source](https://docs.docker.com/engine/reference/commandline/volume_rm/)

* Remove one or more volumes
* usage: `docker volume rm [OPTIONS] VOLUME [VOLUME...]`
* Remove one or more volumes. You cannot remove a volume that is in use by a container.
* `--force/-f` : force the removal

### `docker system`
> [source](https://docs.docker.com/engine/reference/commandline/system/)

* manage docker
* usage: `docker system COMMAND`

#### `docker system df`
> [source](https://docs.docker.com/engine/reference/commandline/system_df/)

* Show docker disk usage
* usage: `docker system df [OPTIONS]`
* The `docker system df` command displays information regarding the amount of disk space used by the docker daemon.
* options
	* `--format`
	* `--verbose/-v`

#### `docker system prune`
> [source](https://docs.docker.com/engine/reference/commandline/system_prune/)

* Remove unused data
* usage: `docker system prune [OPTIONS]`
* Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.
* options
	* `--all/-a` : remove all unused images not just dangling ones
	* `--filter`
	* `--force/-f` : do not prompt for confirmation
	* `--volumes` : prune volumes