> [source](https://docs.docker.com/engine/reference/builder/)

* Docker can build images automatically by reading the instructions from a `Dockerfile`.
* A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.

### Format
* Here is the format of the `Dockerfile`:
```dockerfile
# Comment
INSTRUCTION arguments
```
* The instruction is not case-sensitive. However, convention is for them to be UPPERCASE to distinguish them from arguments more easily.
* Docker runs instructions in a `Dockerfile` in order.
* A `Dockerfile` **must begin with a `FROM` instruction**. This may be after [parser directives](https://docs.docker.com/engine/reference/builder/#parser-directives), [comments](https://docs.docker.com/engine/reference/builder/#format), and globally scoped [ARGs](https://docs.docker.com/engine/reference/builder/#arg).
* The `FROM` instruction specifies the [_Parent Image_](https://docs.docker.com/glossary/#parent-image) from which you are building.
* `FROM` may only be preceded by one or more `ARG` instructions, which declare arguments that are used in `FROM` lines in the `Dockerfile`.
* Docker treats lines that _begin_ with `#` as a comment, unless the line is a valid [parser directive](https://docs.docker.com/engine/reference/builder/#parser-directives).

### Parser Directives
* Parser directives are optional, and affect the way in which subsequent lines in a `Dockerfile` are handled.
* Parser directives do not add layers to the build, and will not be shown as a build step.
*  Parser directives are written as a special type of comment in the form `# directive=value`.
* **A single directive may only be used once.**
* Once a comment, empty line or builder instruction has been processed, Docker *no longer* looks for parser directives. Instead it treats anything formatted as a parser directive as a comment and does not attempt to validate if it might be a parser directive. Therefore, all parser directives must be at the very top of a `Dockerfile`.
* Parser directives are not case-sensitive. However, convention is for them to be lowercase. Convention is also to include a blank line following any parser directives.
* If a parser directive is precisely after a comment, it will be invalid as a parser directive and will be considered as a comment.
* Supported parser directives: `syntax`, [`escape`](https://docs.docker.com/engine/reference/builder/#escape)

### Environment Replacement
> [source](https://docs.docker.com/engine/reference/builder/#environment-replacement)

* Environment variables (declared with [the `ENV` statement](https://docs.docker.com/engine/reference/builder/#env)) can also be used in certain instructions as variables to be interpreted by the `Dockerfile`.
* Environment variables are notated in the `Dockerfile` either with `$variable_name` or `${variable_name}`. They are treated equivalently and the brace syntax is typically used to address issues with variable names with no whitespace, like `${foo}_bar`.
* Example (parsed representation is displayed after the `#`):
```Dockerfile
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux
```
* Environment variables are supported by the following list of instructions in the `Dockerfile`:
	`ADD`, `COPY`, `ENV`, `EXPOSE`, `FROM`, `LABEL`, `STOPSIGNAL`, `USER`, `VOLUME`, `WORKDIR`, `ONBUILD`

### `.dockerignore` file
> [source](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

* Before the docker CLI sends the context to the docker daemon, it looks for a file named `.dockerignore` in the root directory of the context. If this file exists, the CLI modifies the context to exclude files and directories that match patterns in it. This helps to avoid unnecessarily sending large or sensitive files and directories to the daemon and potentially adding them to images using `ADD` or `COPY`.

### `FROM`
> [source](https://docs.docker.com/engine/reference/builder/#from)

* usage: `FROM [--platform=<platform>] <image> [AS <name>]`
	* or: `FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]`
	* or: `FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]`
* The `FROM` instruction initializes a new build stage and sets the [_Base Image_](https://docs.docker.com/glossary/#base-image) for subsequent instructions.
	* As such, a valid `Dockerfile` must start with a `FROM` instruction.
	* The image can be any valid image – it is especially easy to start by **pulling an image** from the [_Public Repositories_](https://docs.docker.com/docker-hub/repos/).
* `ARG` is the only instruction that may precede `FROM` in the `Dockerfile`. See [Understand how ARG and FROM interact](https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact).
* `FROM` can appear multiple times within a single `Dockerfile` to create multiple images or use one build stage as a dependency for another. Simply make a note of the last image ID output by the commit before each new `FROM` instruction. Each `FROM` instruction clears any state created by previous instructions.
* Optionally a name can be given to a new build stage by adding `AS name` to the `FROM` instruction. The name can be used in subsequent `FROM` and `COPY --from=<name>` instructions to refer to the image built in this stage.
* The `tag` or `digest` values are optional. If you omit either of them, the builder assumes a `latest` tag by default. The builder returns an error if it cannot find the `tag` value.

### `RUN`
> [source](https://docs.docker.com/engine/reference/builder/#run)

* RUN has 2 forms:
	* `RUN <command>` (_shell_ form, the command is run in a shell, which by default is `/bin/sh -c` on Linux)
	* `RUN ["executable", "param1", "param2"]` (_exec_ form)
* The `RUN` instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the `Dockerfile`.
* Layering `RUN` instructions and generating commits conforms to the core concepts of Docker where commits are cheap and containers can be created from any point in an image’s history, much like source control.
* The default shell for the _shell_ form can be changed using the `SHELL` command.
* **Note**: The _exec_ form is parsed as a JSON array, which means that you must use double-quotes (“) around words not single-quotes (‘).
* Unlike the _shell_ form, the _exec_ form does not invoke a command shell. This means that normal shell processing does not happen. For example, `RUN [ "echo", "$HOME" ]` will not do variable substitution on `$HOME`. If you want shell processing then either use the _shell_ form or execute a shell directly, for example: `RUN [ "sh", "-c", "echo $HOME" ]`. When using the exec form and executing a shell directly, as in the case for the shell form, it is the shell that is doing the environment variable expansion, not docker.

#### `RUN --mount`
> [source](https://docs.docker.com/engine/reference/builder/#run---mount)

* `RUN --mount` allows you to create filesystem mounts that the build can access. This can be used to:
	* Create bind mount to the host filesystem or other build stages
	* Access build secrets or ssh-agent sockets
	* Use a persistent package management cache to speed up your build
* Syntax: `--mount=[type=<TYPE>][,option=<value>[,option=<value>]...]`
* Mount types:
	* `bind` (default) : Bind-mount context directories (read-only).
	* `cache` : Mount a temporary directory to cache directories for compilers and package managers.
	* `secret` : Allow the build container to access secure files such as private keys without baking them into the image.
	* `ssh` : Allow the build container to access SSH keys via SSH agents, with support for passphrases.

#### `RUN --network`
> [source](https://docs.docker.com/engine/reference/builder/#run---network)

* `RUN --network` allows control over which networking environment the command is run in.
* Syntax: `--network=<TYPE>`
* Network types:
	* `default` (default) : Run in the default network.
	* `none` : Run with no network access.
	* `host` : Run in the host's network environment.

#### `RUN --security`
> [source](https://docs.docker.com/engine/reference/builder/#run---security)

* With `--security=insecure`, builder runs the command without sandbox in insecure mode, which allows to run flows requiring elevated privileges (e.g. containerd). This is equivalent to running `docker run --privileged`.

> [!Warning]
> In order to access this feature, entitlement `security.insecure` should be enabled when starting the buildkitd daemon with `--allow-insecure-entitlement security.insecure` flag or in [buildkitd config](https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md), and for a build request with [`--allow security.insecure` flag](https://docs.docker.com/engine/reference/commandline/buildx_build/#allow).

### `CMD`
> [source](https://docs.docker.com/engine/reference/builder/#cmd)

* The `CMD` instruction has three forms:
	* `CMD ["executable","param1","param2"]` (_exec_ form, this is the preferred form)
	* `CMD ["param1","param2"]` (as _default parameters to ENTRYPOINT_)
	* `CMD command param1 param2` (_shell_ form)
* There can only be one `CMD` instruction in a `Dockerfile`. If you list more than one `CMD` then only the last `CMD` will take effect.
* **The main purpose of a `CMD` is to provide defaults for an executing container.** These defaults can include an executable, or they can omit the executable, in which case you must specify an `ENTRYPOINT` instruction as well.
* If `CMD` is used to provide default arguments for the `ENTRYPOINT` instruction, both the `CMD` and `ENTRYPOINT` instructions should be specified with the JSON array format.
* If you would like your container to run the same executable every time, then you should consider using `ENTRYPOINT` in combination with `CMD`. See [_ENTRYPOINT_](https://docs.docker.com/engine/reference/builder/#entrypoint).
* If the user specifies arguments to `docker run` then they will override the default specified in `CMD`.

### `LABEL`
> [source](https://docs.docker.com/engine/reference/builder/#label)

* usage: `LABEL <key>=<value> <key>=<value> <key>=<value> ...`
* The `LABEL` instruction adds metadata to an image. A `LABEL` is a key-value pair. To include spaces within a `LABEL` value, use quotes and backslashes as you would in command-line parsing.
* An image can have more than one label.
* You can specify multiple labels on a single line.

### `EXPOSE`
> [source](https://docs.docker.com/engine/reference/builder/#expose)

* usage: `EXPOSE <port> [<port>/<protocol>...]`
* The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified.
* The `EXPOSE` instruction does not actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To actually publish the port when running the container, use the `-p` flag on `docker run` to publish and map one or more ports, or the `-P` flag to publish all exposed ports and map them to high-order ports.
* To expose on both TCP and UDP, include two lines.
* Regardless of the `EXPOSE` settings, you can override them at runtime by using the `-p` flag.
* To set up port redirection on the host system, see [using the -P flag](https://docs.docker.com/engine/reference/run/#expose-incoming-ports).

### `ENV`
> [source](https://docs.docker.com/engine/reference/builder/#env)

* usage: `ENV <key>=<value> ...`
* The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment for all subsequent instructions in the build stage and can be [replaced inline](https://docs.docker.com/engine/reference/builder/#environment-replacement) in many as well.
* The `ENV` instruction allows for multiple `<key>=<value> ...` variables to be set at one time.
* The environment variables set using `ENV` will persist when a container is run from the resulting image. You can view the values using `docker inspect`, and change them using `docker run --env <key>=<value>`.
* A stage inherits any environment variables that were set using `ENV` by its parent stage or any ancestor. Refer [here](https://docs.docker.com/build/building/multi-stage/) for more on multi-staged builds.
* If an environment variable is only needed during build, and not in the final image, consider setting a value for a single command instead:
```Dockerfile
RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y
```
* Or using [`ARG`](https://docs.docker.com/engine/reference/builder/#arg), which is not persisted in the final image:
```Dockerfile
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y ...
```

### `ADD`
> [source](https://docs.docker.com/engine/reference/builder/#add)

* ADD has two forms:
	* `ADD [--chown=<user>:<group>] [--chmod=<perms>] [--checksum=<checksum>] <src>... <dest>`
	* `ADD [--chown=<user>:<group>] [--chmod=<perms>] ["<src>",... "<dest>"]`
* The `ADD` instruction copies new files, directories or remote file URLs from `<src>` and adds them to the filesystem of the image at the path `<dest>`.
* Multiple `<src>` resources may be specified but if they are files or directories, their paths are interpreted as relative to the source of the context of the build.
* Each `<src>` may contain wildcards.
* The `<dest>` is an absolute path, or a path relative to `WORKDIR`, into which the source will be copied inside the destination container.
* When adding files or directories that contain special characters (such as `[` and `]`), you need to escape those paths following the Golang rules to prevent them from being treated as a matching pattern.
* All new files and directories are created with a UID and GID of 0, unless the optional `--chown` flag specifies a given username, groupname, or UID/GID combination to request specific ownership of the content added.
	* The format of the `--chown` flag allows for either username and groupname strings or direct integer UID and GID in any combination.
	* Providing a username without groupname or a UID without GID will use the same numeric UID as the GID.
	* If a username or groupname is provided, the container’s root filesystem `/etc/passwd` and `/etc/group` files will be used to perform the translation from name to integer UID or GID respectively.
	* If the container root filesystem does not contain either `/etc/passwd` or `/etc/group` files and either user or group names are used in the `--chown` flag, the build will fail on the `ADD` operation. Using numeric IDs requires no lookup and will not depend on container root filesystem content.
	```Dockerfile
	ADD --chown=55:mygroup files* /somedir/
	ADD --chown=bin files* /somedir/
	ADD --chown=1 files* /somedir/
	ADD --chown=10:11 files* /somedir/
	ADD --chown=myuser:mygroup --chmod=655 files* /somedir/
	```
* In the case where `<src>` is a remote file URL, the destination will have permissions of 600. If the remote file being retrieved has an HTTP `Last-Modified` header, the timestamp from that header will be used to set the `mtime` on the destination file. However, like any other file processed during an `ADD`, `mtime` will not be included in the determination of whether or not the file has changed and the cache should be updated.

> [!Note]
> If you build by passing a `Dockerfile` through STDIN (`docker build - < somefile`), there is no build context, so the `Dockerfile` can only contain a URL based `ADD` instruction.

* If your URL files are protected using authentication, you need to use `RUN wget`, `RUN curl` or use another tool from within the container as the `ADD` instruction does not support authentication.
* `ADD` obeys the following rules:
	* The `<src>` path must be inside the _context_ of the build; you cannot `ADD ../something /something`, because the first step of a `docker build` is to send the context directory (and subdirectories) to the docker daemon.
	* If `<src>` is a URL and `<dest>` does not end with a trailing slash, then a file is downloaded from the URL and copied to `<dest>`.
	* If `<src>` is a URL and `<dest>` does end with a trailing slash, then the filename is inferred from the URL and the file is downloaded to `<dest>/<filename>`. For instance, `ADD http://example.com/foobar /` would create the file `/foobar`. The URL must have a nontrivial path so that an appropriate filename can be discovered in this case (`http://example.com` will not work).
	* If `<src>` is a directory, the entire contents of the directory are copied, including filesystem metadata.
		* The directory itself is not copied, just its contents.
	* If `<src>` is a _local_ tar archive in a recognized compression format (identity, gzip, bzip2 or xz) then it is unpacked as a directory. Resources from _remote_ URLs are **not** decompressed. When a directory is copied or unpacked, it has the same behavior as `tar -x`, the result is the union of:
		1. Whatever existed at the destination path and
		2. The contents of the source tree, with conflicts resolved in favor of “2.” on a file-by-file basis.
		* Whether a file is identified as a recognized compression format or not is done solely based on the contents of the file, not the name of the file. For example, if an empty file happens to end with `.tar.gz` this will not be recognized as a compressed file and **will not** generate any kind of decompression error message, rather the file will simply be copied to the destination.
	* If `<src>` is any other kind of file, it is copied individually along with its metadata. In this case, if `<dest>` ends with a trailing slash `/`, it will be considered a directory and the contents of `<src>` will be written at `<dest>/base(<src>)`.
	* If multiple `<src>` resources are specified, either directly or due to the use of a wildcard, then `<dest>` must be a directory, and it must end with a slash `/`.
	* If `<dest>` does not end with a trailing slash, it will be considered a regular file and the contents of `<src>` will be written at `<dest>`.
	* If `<dest>` doesn’t exist, it is created along with all missing directories in its path.
* For `COPY --link`, refer to `COPY --link`.

### `COPY`
> [source](https://docs.docker.com/engine/reference/builder/#copy)

* COPY has two forms:
	* `COPY [--chown=<user>:<group>] [--chmod=<perms>] <src>... <dest>`
	* `COPY [--chown=<user>:<group>] [--chmod=<perms>] ["<src>",... "<dest>"]`
* Pretty much similar to `ADD`.
* Optionally `COPY` accepts a flag `--from=<name>` that can be used to set the source location to a previous build stage (created with `FROM .. AS <name>`) that will be used instead of a build context sent by the user. In case a build stage with a specified name can’t be found an image with the same name is attempted to be used instead.
* `COPY` obeys some rules which also happen to belong to the rules specified in `ADD`'s rules; but `ADD` has way more rules.
	* The `<src>` path must be inside the _context_ of the build; you cannot `COPY ../something /something`, because the first step of a `docker build` is to send the context directory (and subdirectories) to the docker daemon.
	* If `<src>` is a directory, the entire contents of the directory are copied, including filesystem metadata.
		* The directory itself is not copied, just its contents.
	* If `<src>` is any other kind of file, it is copied individually along with its metadata. In this case, if `<dest>` ends with a trailing slash `/`, it will be considered a directory and the contents of `<src>` will be written at `<dest>/base(<src>)`.
	* If multiple `<src>` resources are specified, either directly or due to the use of a wildcard, then `<dest>` must be a directory, and it must end with a slash `/`.
	* If `<dest>` does not end with a trailing slash, it will be considered a regular file and the contents of `<src>` will be written at `<dest>`.
	* If `<dest>` doesn’t exist, it is created along with all missing directories in its path.

#### `COPY --link`
> [source](https://docs.docker.com/engine/reference/builder/#copy---link)

> [!Note]
> Added in [`docker/dockerfile:1.4`](https://docs.docker.com/engine/reference/builder/#syntax)

* Enabling this flag in `COPY` or `ADD` commands allows you to copy files with enhanced semantics where your files remain independent on their own layer and don’t get invalidated when commands on previous layers are changed.
* When `--link` is used your source files are copied into an empty destination directory. That directory is turned into a layer that is linked on top of your previous state.
> [!Warning]
> Read the rest from the source. You need to understand multi-staged builds.

### `COPY` vs `ADD`
> I asked chatGPT "what's the difference between docker ADD and COPY instructions?", and here's the answer.

1. **Source and Destination:**
    - `COPY` requires you to explicitly specify both the source and destination paths. The source can be a file or a directory on the host or a previous build stage, and the destination is a path within the Docker image.
    - `ADD` allows you to specify a source path similar to `COPY`, but it also supports URLs and automatically handles tar extraction. It is more flexible than `COPY` but can have some unexpected behaviors.
2. **URLs and Automatic Extraction:**
    - `COPY` is straightforward and copies the files or directories from the source path to the destination in the Docker image.
    - `ADD` has additional functionality. If the source is a URL, `ADD` can download the file and place it in the Docker image. Additionally, if the source is a tar archive, `ADD` automatically extracts it to the destination directory in the image.
3. **Caching:**
    - `COPY` is a simple operation that only copies the files from the source to the destination. It has better caching capabilities, meaning that if the source files haven't changed, the cache can be used, and subsequent builds can be faster.
    - `ADD` is a more complex operation that involves potential extraction and URL fetching. Because of this, Docker doesn't perform caching in the same way for `ADD` instructions. If any changes are made to the source file or URL, Docker will re-execute the `ADD` instruction and invalidate the cache for that step and all subsequent steps.
* In general, it is recommended to use `COPY` for most cases, as it is simpler, more explicit, and has better caching behavior. `ADD` should be used when you specifically need its additional features, such as URL fetching or automatic tar extraction.

### `ENTRYPOINT`
> [source](https://docs.docker.com/engine/reference/builder/#entrypoint)

* ENTRYPOINT has two forms:
	* The _exec_ form, which is the preferred form:
		`ENTRYPOINT ["executable", "param1", "param2"]`
	* The _shell_ form:
		`ENTRYPOINT command param1 param2`
* An `ENTRYPOINT` allows you to configure a container that will run as an executable.
* For example, the following starts nginx with its default content, listening on port 80:
	`docker run -i -t --rm -p 80:80 nginx`
* Command line arguments to `docker run <image>` will be appended after all elements in an _exec_ form `ENTRYPOINT`, and will override all elements specified using `CMD`. This allows arguments to be passed to the entry point, i.e., `docker run <image> -d` will pass the `-d` argument to the entry point. You can override the `ENTRYPOINT` instruction using the `docker run --entrypoint` flag.
* The _shell_ form prevents any `CMD` or `run` command line arguments from being used, but has the disadvantage that your `ENTRYPOINT` will be started as a subcommand of `/bin/sh -c`, which does not pass signals. This means that the executable will not be the container’s `PID 1` - and will _not_ receive Unix signals - so your executable will not receive a `SIGTERM` from `docker stop <container>`.
* Only the last `ENTRYPOINT` instruction in the `Dockerfile` will have an effect.

#### Understand how `CMD` and `ENTRYPOINT` interact
> [source](https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact)

* Both `CMD` and `ENTRYPOINT` instructions define what command gets executed when running a container. There are few rules that describe their co-operation.
	1. ***Dockerfile should specify at least one of `CMD` or `ENTRYPOINT` commands.***
	2. `ENTRYPOINT` should be defined when using the container as an executable.
	3. `CMD` should be used as a way of defining default arguments for an `ENTRYPOINT` command or for executing an ad-hoc command in a container.
	4. `CMD` will be overridden when running the container with alternative arguments.

> [!Note]
> If `CMD` is defined from the base image, setting `ENTRYPOINT` will reset `CMD` to an empty value. In this scenario, `CMD` must be defined in the current image to have a value.

### `VOLUME`
> [source](https://docs.docker.com/engine/reference/builder/#volume)

* usage: `VOLUME ["/data"]`
* The `VOLUME` instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. The value can be a JSON array, `VOLUME ["/var/log/"]`, or a plain string with multiple arguments, such as `VOLUME /var/log` or `VOLUME /var/log /var/db`. For more information/examples and mounting instructions via the Docker client, refer to [_Share Directories via Volumes_](https://docs.docker.com/storage/volumes/) documentation.
* The `docker run` command initializes the newly created volume with any data that exists at the specified location within the base image. For example, consider the following Dockerfile snippet:
* The `docker run` command initializes the newly created volume with any data that exists at the specified location within the base image.
* Keep the following things in mind about volumes in the `Dockerfile`.
	* **Changing the volume from within the Dockerfile**: If any build steps change the data within the volume after it has been declared, those changes will be discarded.
	* **The host directory is declared at container run-time**: The host directory (the mountpoint) is, by its nature, host-dependent. This is to preserve image portability, since a given host directory can’t be guaranteed to be available on all hosts. For this reason, you can’t mount a host directory from within the Dockerfile. The `VOLUME` instruction does not support specifying a `host-dir` parameter. You must specify the mountpoint when you create or run the container.

### `USER`
> [source](https://docs.docker.com/engine/reference/builder/#user)

* usage: `USER <user>[:<group>]`
	* or: `USER <UID>[:<GID>]`
* The `USER` instruction sets the user name (or UID) and optionally the user group (or GID) to use as the default user and group for the remainder of the current stage. The specified user is used for `RUN` instructions and at runtime, runs the relevant `ENTRYPOINT` and `CMD` commands.

> [!Note]
> > Note that when specifying a group for the user, the user will have _only_ the specified group membership. Any other configured group memberships will be ignored.

> [!Warning]
> When the user doesn’t have a primary group then the image (or the next instructions) will be run with the `root` group.

### `WORKDIR`
> [source](https://docs.docker.com/engine/reference/builder/#workdir)

* usage: `WORKDIR /path/to/workdir`
* The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the `Dockerfile`.
* If the `WORKDIR` doesn’t exist, it will be created even if it’s not used in any subsequent `Dockerfile` instruction.
* The `WORKDIR` instruction can be used multiple times in a `Dockerfile`. If a relative path is provided, it will be relative to the path of the previous `WORKDIR` instruction.
* The `WORKDIR` instruction can resolve environment variables previously set using `ENV`. You can only use environment variables explicitly set in the `Dockerfile`.
* If not specified, the default working directory is `/`. In practice, if you aren’t building a Dockerfile from scratch (`FROM scratch`), the `WORKDIR` may likely be set by the base image you’re using.
* ***Therefore, to avoid unintended operations in unknown directories, it is best practice to set your `WORKDIR` explicitly.***

### `ARG`
> [source](https://docs.docker.com/engine/reference/builder/#arg)

* usage: `ARG <name>[=<default value>]`
* The `ARG` instruction defines a variable that users can pass at build-time to the builder with the `docker build` command using the `--build-arg <varname>=<value>` flag. If a user specifies a build argument that was not defined in the Dockerfile, the build outputs a warning.

> [!Warning]
> It is not recommended to use build-time variables for passing secrets like GitHub keys, user credentials etc. Build-time variable values are visible to any user of the image with the `docker history` command.
> 
> Refer to the [`RUN --mount=type=secret`](https://docs.docker.com/engine/reference/builder/#run---mounttypesecret) section to learn about secure ways to use secrets when building images.

* Default value
	* An `ARG` instruction can optionally include a default value:
		* `ARG user1=mehdi`
	* If an `ARG` instruction has a default value and if there is no value passed at build-time, the builder uses the default.
* Scope
	* An `ARG` variable definition comes into effect from the line on which it is defined in the `Dockerfile` not from the argument’s use on the command-line or elsewhere. For example, consider this Dockerfile:
	* An `ARG` instruction goes out of scope at the end of the build stage where it was defined. To use an argument in multiple stages, each stage must include the `ARG` instruction.
* You can use an `ARG` or an `ENV` instruction to specify variables that are available to the `RUN` instruction. Environment variables defined using the `ENV` instruction always override an `ARG` instruction of the same name.
* Unlike an `ARG` instruction, `ENV` values are always persisted in the built image.
	* One can leverage the use of `ENV` to persist data to the final image.
* Docker has a set of predefined `ARG` variables that you can use without a corresponding `ARG` instruction in the Dockerfile.
	- `HTTP_PROXY`, `http_proxy`, `HTTPS_PROXY`, `https_proxy`, `FTP_PROXY`, `ftp_proxy`, `NO_PROXY`, `no_proxy`, `ALL_PROXY`, `all_proxy`
	- By default, these pre-defined variables are excluded from the output of `docker history`. Excluding them reduces the risk of accidentally leaking sensitive authentication information in an `HTTP_PROXY` variable.

### `ONBUILD`
> [source](https://docs.docker.com/engine/reference/builder/#onbuild)

### `STOPSIGNAL`
> [source](https://docs.docker.com/engine/reference/builder/#stopsignal)

### `HEALTHCHECK`
> [source](https://docs.docker.com/engine/reference/builder/#healthcheck)

### `SHELL`
> [source](https://docs.docker.com/engine/reference/builder/#shell)

* usage: `SHELL ["executable", "parameters"]`
* The `SHELL` instruction allows the default shell used for the _shell_ form of commands to be overridden. The default shell on Linux is `["/bin/sh", "-c"]`.
* The `SHELL` instruction _must_ be written in JSON form in a Dockerfile.
* The `SHELL` instruction can appear multiple times. Each `SHELL` instruction overrides all previous `SHELL` instructions, and affects all subsequent instructions.
* The following instructions can be affected by the `SHELL` instruction when the _shell_ form of them is used in a Dockerfile: `RUN`, `CMD` and `ENTRYPOINT`.
* The `SHELL` instruction can also be used on Linux should an alternate shell be required such as `zsh`, `csh`, `tcsh` and others.

### Here-Documents
> [source](https://docs.docker.com/engine/reference/builder/#here-documents)

> [!Note]
> Added in [`docker/dockerfile:1.4`](https://docs.docker.com/engine/reference/builder/#syntax)

* Here-documents allow redirection of subsequent Dockerfile lines to the input of `RUN` or `COPY` commands. If such command contains a [here-document](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_07_04) the Dockerfile considers the next lines until the line only containing a here-doc delimiter as part of the same command.
* e.g. Running a multi-line script:
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM debian
	RUN <<EOT bash
	  set -ex
	  apt-get update
	  apt-get install -y vim
	EOT
	```
	* If the command only contains a here-document, its contents is evaluated with the default shell.
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM debian
	RUN <<EOT
	  mkdir -p foo/bar
	EOT
	```
	* Alternatively, shebang header can be used to define an interpreter.
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM python:3.6
	RUN <<EOT
	#!/usr/bin/env python
	print("hello world")
	EOT
	```
	* More complex examples may use multiple here-documents.
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM alpine
	RUN <<FILE1 cat > file1 && <<FILE2 cat > file2
	I am
	first
	FILE1
	I am
	second
	FILE2
	```
* e.g. Creating inline files:
	* In `COPY` commands source parameters can be replaced with here-doc indicators. Regular here-doc [variable expansion and tab stripping rules](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_07_04) apply.
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM alpine
	ARG FOO=bar
	COPY <<-EOT /app/foo
		hello ${FOO}
	EOT
	```
	```Dockerfile
	# syntax=docker/dockerfile:1
	FROM alpine
	COPY <<-"EOT" /app/script.sh
		echo hello ${FOO}
	EOT
	RUN FOO=abc ash /app/script.sh
	```
