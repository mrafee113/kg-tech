> [source](https://docs.docker.com/compose/compose-file/05-services/)

* A Service is an abstract definition of a computing resource within an application which can be scaled/replaced independently from other components.
* Services are backed by a set of containers, run by the platform according to replication requirements and placement constraints.
* Being backed by containers, Services are defined by a Docker image and set of runtime arguments.
* All containers within a service are identically created with these arguments.

* A Compose file MUST declare a `services` root element as a map whose keys are string representations of service names, and whose values are service definitions. 
* A service definition contains the configuration that is applied to each container started for that service.

* Each service MAY also include a Build section, which defines how to create the Docker image for the service.
* Compose implementations MAY support building docker images using this service definition.
* Build support is an OPTIONAL aspect of the Compose specification, and is described in detail in the [Build support](https://docs.docker.com/compose/compose-file/build/) documentation.

* Each Service defines runtime constraints and requirements to run its containers. The `deploy` section groups these constraints and allows the platform to adjust the deployment strategy to best match containers’ needs with available resources.
* Deploy support is an OPTIONAL aspect of the Compose specification, and is described in detail in the [Deployment support](https://docs.docker.com/compose/compose-file/deploy/) documentation.

#### Limiting resources
* `blkio_config` defines a set of configuration options to set block IO limits for this service.
	* `device_read_bps`, `device_write_bps`
		* Set a limit in bytes per second for read / write operations on a given device. Each item in the list MUST have two keys:
			- `path`: defining the symbolic path to the affected device.
			- `rate`: either as an integer value representing the number of bytes or as a string expressing a byte value.
	- `device_read_iops`, `device_write_iops`
		- Set a limit in operations per second for read / write operations on a given device. Each item in the list MUST have two keys:
			- `path`: defining the symbolic path to the affected device.
			- `rate`: as an integer value representing the permitted number of operations per second.
	- `weight` : Modify the proportion of bandwidth allocated to this service relative to other services. Takes an integer value between 10 and 1000, with 500 being the default.
	- `weight_device`
		- Fine-tune bandwidth allocation by device. Each item in the list must have two keys:
			- `path`: defining the symbolic path to the affected device.
			- `weight`: an integer value between 10 and 1000.
	- `cpu_count` : defines the number of usable CPUs for service container.
	- `cpu_percent` : defines the usable percentage of the available CPUs.
	- `cpu_shares` :  defines (as integer value) service container relative CPU weight versus other containers.
	- `cpu_period` : allow Compose implementations to configure CPU CFS (Completely Fair Scheduler) period when platform is based on Linux kernel.
	- `cpu_quota` : allow Compose implementations to configure CPU CFS (Completely Fair Scheduler) quota when platform is based on Linux kernel.
	- `cpu_rt_runtime` : configures CPU allocation parameters for platform with support for realtime scheduler. Can be either an integer value using microseconds as unit or a [duration](https://docs.docker.com/compose/compose-file/11-extension/#specifying-durations).
	- `cpu_rt_period` :  configures CPU allocation parameters for platform with support for realtime scheduler. Can be either an integer value using microseconds as unit or a [duration](https://docs.docker.com/compose/compose-file/11-extension/#specifying-durations).
	- `cpuset` : defines the explicit CPUs in which to allow execution. Can be a range `0-3` or a list `0,1`
	- `cap_add`
		- specifies additional container [capabilities](http://man7.org/linux/man-pages/man7/capabilities.7.html) as strings.
		```yaml
		cap_add:
			- ALL
		```
	 * `cap_drop` : specifies container [capabilities](http://man7.org/linux/man-pages/man7/capabilities.7.html) to drop as strings.

#### `cgroup_parent`
* specifies an OPTIONAL parent [cgroup](http://man7.org/linux/man-pages/man7/cgroups.7.html) for the container.
```yaml
cgroup_parent: m-executor-abcd
```

#### `command`
* overrides the default command declared by the container image (i.e. by Dockerfile’s `CMD`).
```yaml
command: bundle exec thin -p 3000
```
* The value can also be a list, in a manner similar to [Dockerfile](https://docs.docker.com/engine/reference/builder/#cmd):
```yaml
command: [ "bundle", "exec", "thin", "-p", "3000" ]
```
* If the value is `null`, the default command from the image MUST be used.
* If the value is `[]` (empty list) or `''` (empty string), the default command declared by the image MUST be ignored, i.e. overridden to be empty.

#### `configs`
> [source](https://docs.docker.com/compose/compose-file/05-services/#configs)

* `configs` grant access to configs on a per-service basis using the per-service `configs` configuration. Two different syntax variants are supported.
* Compose implementations MUST report an error if config doesn’t exist on platform or isn’t defined in the [`configs`](https://docs.docker.com/compose/compose-file/08-configs/) section of this Compose file.
* There are two syntaxes defined for configs.
	* Short syntax
		* The short syntax variant only specifies the config name. This grants the container access to the config and mounts it at `/<config_name>` within the container. The source name and destination mount point are both set to the config name.
		```yaml
		services:
		  redis:
		    image: redis:latest
		    configs:
		      - my_config
		      - my_other_config
		configs:
		  my_config:
		    file: ./my_config.txt
		  my_other_config:
		    external: true
		```
	* Long syntax
		* The long syntax provides more granularity in how the config is created within the service’s task containers.
			- `source`: The name of the config as it exists in the platform.
			- `target`: The path and name of the file to be mounted in the service’s task containers. Defaults to `/<source>` if not specified.
			- `uid` and `gid`: The numeric UID or GID that owns the mounted config file within the service’s task containers. Default value when not specified is USER running container.
			- `mode`: The [permissions](http://permissions-calculator.org/) for the file that is mounted within the service’s task containers, in octal notation. Default value is world-readable (`0444`). Writable bit MUST be ignored. The executable bit can be set.
		```yaml
		services:
		  redis:
		    image: redis:latest
		    configs:
		      - source: my_config
		        target: /redis_config
		        uid: "103"
		        gid: "103"
		        mode: 0440
		configs:
		  my_config:
		    external: true
		  my_other_config:
		    external: true
		```
* You can grant a service access to multiple configs, and you can mix long and short syntax.

#### `container_name`
* is a string that specifies a custom container name, rather than a generated default name.
```yaml
container_name: my-web-container
```
* Compose implementation MUST NOT scale a service beyond one container if the Compose file specifies a `container_name`. Attempting to do so MUST result in an error.
* If present, `container_name` SHOULD follow the regex format of `[a-zA-Z0-9][a-zA-Z0-9_.-]+`

#### `depends_on`
* expresses startup and shutdown dependencies between services.
* Short syntax
	* The short syntax variant only specifies service names of the dependencies. Service dependencies cause the following behaviors:
		* Compose implementations MUST create services in dependency order.
		* Compose implementations MUST remove services in dependency order.
	```yaml
	services:
	  web:
	    build: .
	    depends_on:
	      - db
	      - redis
	  redis:
	    image: redis
	  db:
	    image: postgres
	```
	* Compose implementations MUST guarantee dependency services have been started before starting a dependent service. Compose implementations MAY wait for dependency services to be “ready” before starting a dependent service.
* Long syntax
	* The long form syntax enables the configuration of additional fields that can’t be expressed in the short form.
		- `restart`: when `true` a Compose implementation MUST restart this service after it updated the dependency service. This applies to an explicit restart controlled by a Compose operation, and excludes automated restart by the container runtime after container died.
		- `condition`: condition under which dependency is considered satisfied
			- `service_started`: is an equivalent of the short syntax described above
			- `service_healthy`: specifies that a dependency is expected to be “healthy” (as indicated by [healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)) before starting a dependent service.
			- `service_completed_successfully`: specifies that a dependency is expected to run to successful completion before starting a dependent service.
	- Service dependencies cause the following behaviors:
		- Compose implementations MUST create services in dependency order.
		- Compose implementations MUST wait for healthchecks to pass on dependencies marked with `service_healthy`.
		- Compose implementations MUST remove services in dependency order.
	```yaml
	services:
	  web:
	    build: .
	    depends_on:
	      db:
	        condition: service_healthy
	        restart: true
	      redis:
	        condition: service_started
	  redis:
	    image: redis
	  db:
	    image: postgres
	```
	* Compose implementations MUST guarantee dependency services have been started before starting a dependent service. Compose implementations MUST guarantee dependency services marked with `service_healthy` are “healthy” before starting a dependent service.

#### `deploy`
* specifies the configuration for the deployment and lifecycle of services, as defined [here](https://docs.docker.com/compose/compose-file/deploy/).

#### `device_cgroup_rules`
> [source](https://docs.docker.com/compose/compose-file/05-services/#device_cgroup_rules)

#### `devices`
* defines a list of device mappings for created containers in the form of `HOST_PATH:CONTAINER_PATH[:CGROUP_PERMISSIONS]`.
```yaml
devices:
  - "/dev/ttyUSB0:/dev/ttyUSB0"
  - "/dev/sda:/dev/xvda:rwm"
```

#### DNS

##### `dns`
* defines custom DNS servers to set on the container network interface configuration. Can be a single value or a list.
```yaml
dns: 8.8.8.8
```
```yaml
dns:
  - 8.8.8.8
  - 9.9.9.9
```

##### `dns_opt`
* list custom DNS options to be passed to the container’s DNS resolver (`/etc/resolv.conf` file on Linux).
```yaml
dns_opt:
  - use-vc
  - no-tld-query
```

##### `dns_search`
* defines custom DNS search domains to set on container network interface configuration. Can be a single value or a list.
```yaml
dns_search: example.com
```
```yaml
dns_search:
  - dc1.example.com
  - dc2.example.com
```

#### `domainname`
* declares a custom domain name to use for the service container. MUST be a valid RFC 1123 hostname.

#### `entrypoint`
* declares the default entrypoint for the service container.
* This will override the `ENTRYPOINT` instruction from the service’s Dockerfile.
* If `entrypoint` is non-null, Compose implementations MUST also ignore out any default command from the image (i.e. `CMD` instruction in Dockerfile).
* See also: [`command`](https://docs.docker.com/compose/compose-file/05-services/#command) to set or override the default command to be executed by the entrypoint process.

* In its short-form, the value can be defined as a string:
```yaml
entrypoint: /code/entrypoint.sh
```
* Alternatively, the value can also be a list, in a manner similar to [Dockerfile](https://docs.docker.com/engine/reference/builder/#cmd):
```yaml
entrypoint:
  - php
  - -d
  - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
  - -d
  - memory_limit=-1
  - vendor/bin/phpunit
```

* If the value is `null`, the default entrypoint from the image MUST be used.
* If the value is `[]` (empty list) or `''` (empty string), the default entrypoint declared by the image MUST be ignored, i.e. overridden to be empty.

#### `env_file`
* `env_file` adds environment variables to the container based on file content.
```yaml
env_file: .env
```
* `env_file` can also be a list. The files in the list MUST be processed from the top down. For the same variable specified in two env files, the value from the last file in the list MUST stand.
```yaml
env_file:
  - ./a.env
  - ./b.env
```
* Relative path MUST be resolved from the Compose file’s parent folder. As absolute paths prevent the Compose file from being portable, Compose implementations SHOULD warn users when such a path is used to set `env_file`.
* Environment variables declared in the [environment](https://docs.docker.com/compose/compose-file/05-services/#environment) section MUST override these values – this holds true even if those values are empty or undefined.

##### Env_file format
* Each line in an env file MUST be in `VAR[=[VAL]]` format. Lines beginning with `#` MUST be ignored. Blank lines MUST also be ignored.
* The value of `VAL` is used as a raw string and not modified at all. If the value is surrounded by quotes (as is often the case for shell variables), the quotes MUST be **included** in the value passed to containers created by the Compose implementation.
* ***`VAL` MAY be omitted, in such cases the variable value is empty string. `=VAL` MAY be omitted, in such cases the variable is **unset**.***
```yaml
# Set Rails/Rack environment
RACK_ENV=development
VAR="quoted"
```

#### `environment`
* `environment` defines environment variables set in the container.
* `environment` can use either an array or a map. Any boolean values; true, false, yes, no, SHOULD be enclosed in quotes to ensure they are not converted to True or False by the YAML parser.
* Environment variables MAY be declared by a single key (no value to equals sign). In such a case Compose implementations SHOULD rely on some user interaction to resolve the value. If they do not, the variable is unset and will be removed from the service container environment.
* Map syntax:
```yaml
environment:
  RACK_ENV: development
  SHOW: "true"
  USER_INPUT:
```
* Array syntax:
```yaml
environment:
  - RACK_ENV=development
  - SHOW=true
  - USER_INPUT
```
* When both `env_file` and `environment` are set for a service, values set by `environment` have precedence.

#### `expose`
* `expose` defines the ports that Compose implementations MUST expose from container. These ports MUST be accessible to linked services and SHOULD NOT be published to the host machine. Only the internal container ports can be specified.

#### `extends`
* Extend another service, in the current file or another, optionally overriding configuration.
* You can use `extends` on any service together with other configuration keys.
* The `extends` value MUST be a mapping defined with a required `service` and an optional `file` key.
```yaml
extends:
  file: common.yml
  service: webapp
```

##### Restrictions
* The following restrictions apply to the service being referenced:
	* Services that have dependencies on other services cannot be used as a base. Therefore, any key that introduces a dependency on another service is incompatible with `extends`. The non-exhaustive list of such keys is: `links`, `volumes_from`, `container` mode (in `ipc`, `pid`, `network_mode` and `net`), `service` mode (in `ipc`, `pid` and `network_mode`), `depends_on`.
	- Services cannot have circular references with `extends`.
	- Compose implementations MUST return an error in all of these cases.

##### Finding referenced service
* `file` value can be:
	* Not present. This indicates that another service within the same Compose file is being referenced.
	* File path, which can be either:
		* Relative path. This path is considered as relative to the location of the main Compose file.
		* Absolute path.
* Service denoted by `service` MUST be present in the identified referenced Compose file. Compose implementations MUST return an error if:
	* Service denoted by `service` was not found
	* Compose file denoted by `file` was not found

##### Merging service definitions
* Two service definitions (_main_ one in the current Compose file and _referenced_ one specified by `extends`) MUST be merged in the following way:
	* Mappings: keys in mappings of _main_ service definition override keys in mappings of _referenced_ service definition. Keys that aren’t overridden are included as is.
	* Sequences: items are combined together into an new sequence. Order of elements is preserved with the _referenced_ items coming first and _main_ items after.
	* Scalars: keys in _main_ service definition take precedence over keys in the _referenced_ one.

###### Mappings
1. The following keys should be treated as mappings: `annotations`, `build.args`, `build.labels`, `build.extra_hosts`, `deploy.labels`, `deploy.update_config`, `deploy.rollback_config`, `deploy.restart_policy`, `deploy.resources.limits`, `environment`, `healthcheck`, `labels`, `logging.options`, `sysctls`, `storage_opt`, `extra_hosts`, `ulimits`.
* For example, the input below:
```yaml
services:
  common:
    image: busybox
    environment:
      TZ: utc
      PORT: 80
  cli:
    extends:
      service: common
    environment:
      PORT: 8080
```
* Produces the following configuration for the `cli` service. The same output is produced if array syntax is used.
```yaml
environment:
  PORT: 8080
  TZ: utc
image: busybox
```
2. Items under `blkio_config.device_read_bps`, `blkio_config.device_read_iops`, `blkio_config.device_write_bps`, `blkio_config.device_write_iops`, `devices` and `volumes` are also treated as mappings where key is the target path inside the container.
* For example, the input below:
```yaml
services:
  common:
    image: busybox
    volumes:
      - common-volume:/var/lib/backup/data:rw
  cli:
    extends:
      service: common
    volumes:
      - cli-volume:/var/lib/backup/data:ro
```
* Produces the following configuration for the `cli` service. Note that mounted path now points to the new volume name and `ro` flag was applied.
```yaml
image: busybox
volumes:
- cli-volume:/var/lib/backup/data:ro
```
3. If _referenced_ service definition contains `extends` mapping, the items under it are simply copied into the new _merged_ definition. Merging process is then kicked off again until no `extends` keys are remaining.
* For example, the input below:
```yaml
services:
  base:
    image: busybox
    user: root
  common:
    image: busybox
    extends:
      service: base
  cli:
    extends:
      service: common
```
* Produces the following configuration for the `cli` service. Here, `cli` services gets `user` key from `common` service, which in turn gets this key from `base` service.
```yaml
image: busybox
user: root
```

##### Sequences
* The following keys should be treated as sequences: `cap_add`, `cap_drop`, `configs`, `deploy.placement.constraints`, `deploy.placement.preferences`, `deploy.reservations.generic_resources`, `device_cgroup_rules`, `expose`, `external_links`, `ports`, `secrets`, `security_opt`. Any duplicates resulting from the merge are removed so that the sequence only contains unique elements.
* In case list syntax is used, the following keys should also be treated as sequences: `dns`, `dns_search`, `env_file`, `tmpfs`. Unlike sequence fields mentioned above, duplicates resulting from the merge are not removed.
* For example, the input below:
```yaml
services:
  common:
    image: busybox
    security_opt:
      - label:role:ROLE
  cli:
    extends:
      service: common
    security_opt:
      - label:user:USER
```
* Produces the following configuration for the `cli` service.
```yaml
image: busybox
security_opt:
- label:role:ROLE
- label:user:USER
```

##### Scalars
* Any other allowed keys in the service definition should be treated as scalars.

#### `external_links`
* `external_links` link service containers to services managed outside this Compose application.
* `external_links` define the name of an existing service to retrieve using the platform lookup mechanism.
* An alias of the form `SERVICE:ALIAS` can be specified.
```yaml
external_links:
  - redis
  - database:mysql
  - database:postgresql
```

#### `extra_hosts`
* `extra_hosts` adds hostname mappings to the container network interface configuration (`/etc/hosts` for Linux).
* Short syntax : use plain strings in a list. Values MUST set hostname and IP address for additional hosts in the form of `HOSTNAME:IP`.
```yaml
extra_hosts:
  - "somehost:162.242.195.82"
  - "otherhost:50.31.209.229"
```
* Long syntax : Alternatively, `extra_hosts` can be set as a mapping between hostname(s) and IP(s)
```yaml
extra_hosts:
  somehost: "162.242.195.82"
  otherhost: "50.31.209.229"
```

#### `group_add`
* `group_add` specifies additional groups (by name or number) which the user inside the container MUST be a member of.
* An example of where this is useful is when multiple containers (running as different users) need to all read or write the same file on a shared volume. That file can be owned by a group shared by all the containers, and specified in `group_add`.
```yaml
services:
  myservice:
    image: alpine
    group_add:
      - mail
```
* Running `id` inside the created container MUST show that the user belongs to the `mail` group, which would not have been the case if `group_add` were not declared.

#### `hostname`
* `hostname` declares a custom host name to use for the service container. MUST be a valid RFC 1123 hostname.

#### `image`
* `image` specifies the image to start the container from.
* Image MUST follow the Open Container Specification [addressable image format](https://github.com/opencontainers/org/blob/master/docs/docs/introduction/digests.md), as `[<registry>/][<project>/]<image>[:<tag>|@<digest>]`.
```yaml
image: redis
image: redis:5
image: redis@sha256:0ed5d5928d4737458944eb604cc8509e245c3e19d02ad83935398bc4b991aac7
image: library/redis
image: docker.io/library/redis
image: my_private.registry:5000/redis
```
* If the image does not exist on the platform, Compose implementations MUST attempt to pull it based on the `pull_policy`.
* `image` MAY be omitted from a Compose file as long as a `build` section is declared.
* Compose implementations without build support MUST fail when `image` is missing from the Compose file.

#### `labels`
* `labels` add metadata to containers. You can use either an array or a map.
* It’s recommended that you use reverse-DNS notation to prevent your labels from conflicting with those used by other software.
```yaml
labels:
  com.example.description: "Accounting webapp"
  com.example.department: "Finance"
  com.example.label-with-empty-value: ""
```
```yaml
labels:
  - "com.example.description=Accounting webapp"
  - "com.example.department=Finance"
  - "com.example.label-with-empty-value"
```

* Compose implementations MUST create containers with canonical labels:
	* `com.docker.compose.project` set on all resources created by Compose implementation to the user project name
	* `com.docker.compose.service` set on service containers with service name as defined in the Compose file
* The `com.docker.compose` label prefix is reserved. Specifying labels with this prefix in the Compose file MUST result in a runtime error.

#### `links`
* `links` defines a network link to containers in another service. Either specify both the service name and a link alias (`SERVICE:ALIAS`), or just the service name.
```yaml
web:
  links:
    - db
    - db:database
    - redis
```
* Containers for the linked service MUST be reachable at a hostname identical to the alias, or the service name if no alias was specified.
* Links are not required to enable services to communicate - when no specific network configuration is set, any service MUST be able to reach any other service at that service’s name on the `default` network. If services do declare networks they are attached to, `links` SHOULD NOT override the network configuration and services not attached to a shared network SHOULD NOT be able to communicate.
* Links also express implicit dependency between services in the same way as [depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on), **so they determine the order of service startup.**

#### `logging`
* `logging` defines the logging configuration for the service.
```yaml
logging:
  driver: syslog
  options:
    syslog-address: "tcp://192.168.0.42:123"
```
* The `driver` name specifies a logging driver for the service’s containers. The default and available values are platform specific. Driver specific options can be set with `options` as key-value pairs.

#### `network_mode`
* `network_mode` sets service containers network mode. Available values are platform specific, but Compose specification defines specific values which MUST be implemented as described if supported:
	* `none` which disables all container networking
	* `host` which gives the container raw access to host’s network interface
	* `service:{name}` which gives the containers access to the specified service only
	```yaml
	network_mode: "host"
	    network_mode: "none"
	    network_mode: "service:[service name]"
	```
* When set, `networks` attribute is not allowed and a Compose implementation SHOULD reject any Compose file containing both attributes

#### `networks`
* `networks` defines the networks that service containers are attached to, referencing entries under the [top-level `networks` key](https://docs.docker.com/compose/compose-file/06-networks/).
```yaml
services:
  some-service:
    networks:
      - some-network
      - other-network
```

##### `aliases`
* `aliases` declares alternative hostnames for this service on the network. Other containers on the same network can use either the service name or this alias to connect to one of the service’s containers.
* Since `aliases` are network-scoped, the same service can have different aliases on different networks.

> [!Note]
> A network-wide alias can be shared by multiple containers, and even by multiple services. If it is, then exactly which container the name resolves to is not guaranteed.

* The general format is shown here:
```yaml
services:
  some-service:
    networks:
      some-network:
        aliases:
          - alias1
          - alias3
      other-network:
        aliases:
          - alias2
```
* In the example below, service `frontend` will be able to reach the `backend` service at the hostname `backend` or `database` on the `back-tier` network, and service `monitoring` will be able to reach same `backend` service at `backend` or `mysql` on the `admin` network.
```yaml
services:
  frontend:
    image: awesome/webapp
    networks:
      - front-tier
      - back-tier

  monitoring:
    image: awesome/monitoring
    networks:
      - admin

  backend:
    image: awesome/backend
    networks:
      back-tier:
        aliases:
          - database
      admin:
        aliases:
          - mysql

networks:
  front-tier:
  back-tier:
  admin:
```

##### `ipv4_address`, `ipv6_address`
* Specify a static IP address for containers for this service when joining the network.
* The corresponding network configuration in the [top-level networks section](https://docs.docker.com/compose/compose-file/06-networks/) MUST have an `ipam` block with subnet configurations covering each static address.
```yaml
services:
  frontend:
    image: awesome/webapp
    networks:
      front-tier:
        ipv4_address: 172.16.238.10
        ipv6_address: 2001:3984:3989::10

networks:
  front-tier:
    ipam:
      driver: default
      config:
        - subnet: "172.16.238.0/24"
        - subnet: "2001:3984:3989::/64"
```

##### `link_local_ips`
* `link_local_ips` specifies a list of link-local IPs.
* Link-local IPs are special IPs which belong to a well known subnet and are purely managed by the operator, usually dependent on the architecture where they are deployed. Implementation is Platform specific.
```yaml
services:
  app:
    image: busybox
    command: top
    networks:
      app_net:
        link_local_ips:
          - 57.123.22.11
          - 57.123.22.13
networks:
  app_net:
    driver: bridge
```

##### `priority`
* `priority` indicates in which order Compose implementation SHOULD connect the service’s containers to its networks. If unspecified, the default value is 0.
* In the following example, the app service connects to app_net_1 first as it has the highest priority. It then connects to app_net_3, then app_net_2, which uses the default priority value of 0.
```yaml
services:
  app:
    image: busybox
    command: top
    networks:
      app_net_1:
        priority: 1000
      app_net_2:

      app_net_3:
        priority: 100
networks:
  app_net_1:
  app_net_2:
  app_net_3:
```

#### `mem_swappiness`
> [source](https://docs.docker.com/compose/compose-file/05-services/#mem_swappiness)

#### `memswap_limit`
> [source](https://docs.docker.com/compose/compose-file/05-services/#memswap_limit)

#### `ports`
* Exposes container ports.
* Port mapping MUST NOT be used with `network_mode: host` and doing so MUST result in a runtime error.

##### Short syntax
* The short syntax is a colon-separated string to set host IP, host port and container port in the form:
	* `[HOST:]CONTAINER[/PROTOCOL]` where:
		* `HOST` is `[IP:](port | range)`
		* `CONTAINER` is `port | range`
		* `PROTOCOL` to restrict port to specified protocol. `tcp` and `udp` values are defined by the specification, Compose implementations MAY offer support for platform-specific protocol names.
* Host IP, if not set, MUST bind to **all network interfaces**. Port can be either a single value or a range. Host and container MUST use equivalent ranges.
* Either specify both ports (`HOST:CONTAINER`), or just the container port. In the latter case, the Compose implementation SHOULD automatically allocate any unassigned host port.
* `HOST:CONTAINER` SHOULD always be specified as a (quoted) string, to avoid conflicts with [yaml base-60 float](https://yaml.org/type/float.html).
```yaml
ports:
  - "3000"
  - "3000-3005"
  - "8000:8000"
  - "9090-9091:8080-8081"
  - "49100:22"
  - "8000-9000:80"
  - "127.0.0.1:8001:8001"
  - "127.0.0.1:5000-5010:5000-5010"
  - "6060:6060/udp"
```

##### Long syntax
* The long form syntax allows the configuration of additional fields that can’t be expressed in the short form.
	- `target`: the container port
	- `published`: the publicly exposed port. Can be set as a range using syntax `start-end`, so it is defined as a string, then actual port SHOULD be assigned within this range based on available ports.
	- `host_ip`: the Host IP mapping, unspecified means all network interfaces (`0.0.0.0`)
	- `protocol`: the port protocol (`tcp` or `udp`), unspecified means any protocol
	- `mode`: `host` for publishing a host port on each node, or `ingress` for a port to be load balanced.
```yaml
ports:
  - target: 80
    host_ip: 127.0.0.1
    published: "8080"
    protocol: tcp
    mode: host

  - target: 80
    host_ip: 127.0.0.1
    published: "8000-9000"
    protocol: tcp
    mode: host
```

#### `privileged`
* `privileged` configures the service container to run with elevated privileges. Support and actual impacts are platform-specific.

#### `profiles`
* `profiles` defines a list of named profiles for the service to be enabled under. 
* When not set, service is always enabled.
* If present, `profiles` SHOULD follow the regex format of `[a-zA-Z0-9][a-zA-Z0-9_.-]+`.

#### `pull_policy`
> [source](https://docs.docker.com/compose/compose-file/05-services/#pull_policy)

#### `read_only`
* `read_only` configures service container to be created with a read-only filesystem.

#### `restart`
> [source](https://docs.docker.com/compose/compose-file/05-services/#restart)

#### `secrets`
* `secrets` grants access to sensitive data defined by [secrets](https://docs.docker.com/compose/compose-file/09-secrets/) on a per-service basis. Two different syntax variants are supported: the short syntax and the long syntax.
* Compose implementations MUST report an error if the secret doesn’t exist on the platform or isn’t defined in the [`secrets`](https://docs.docker.com/compose/compose-file/09-secrets/) section of the Compose file.

##### Short syntax
* The short syntax variant only specifies the secret name. This grants the container access to the secret and mounts it as read-only to `/run/secrets/<secret_name>` within the container. The source name and destination mountpoint are both set to the secret name.
* The following example uses the short syntax to grant the `frontend` service access to the `server-certificate` secret. The value of `server-certificate` is set to the contents of the file `./server.cert`.
```yaml
services:
  frontend:
    image: awesome/webapp
    secrets:
      - server-certificate
secrets:
  server-certificate:
    file: ./server.cert
```

##### Long syntax
* The long syntax provides more granularity in how the secret is created within the service’s containers.
	- `source`: The name of the secret as it exists on the platform.
	- `target`: The name of the file to be mounted in `/run/secrets/` in the service’s task container, or absolute path of the file if an alternate location is required. Defaults to `source` if not specified.
	- `uid` and `gid`: The numeric UID or GID that owns the file within `/run/secrets/` in the service’s task containers. Default value is USER running container.
	- `mode`: The [permissions](http://permissions-calculator.org/) for the file to be mounted in `/run/secrets/` in the service’s task containers, in octal notation. Default value is world-readable permissions (mode `0444`). The writable bit MUST be ignored if set. The executable bit MAY be set.
```yaml
services:
  frontend:
    image: awesome/webapp
    secrets:
      - source: server-certificate
        target: server.cert
        uid: "103"
        gid: "103"
        mode: 0440
secrets:
  server-certificate:
    external: true
```

##### `tmpfs`
* `tmpfs` mounts a temporary file system inside the container. Can be a single value or a list.
```yaml
tmpfs: /run
```
```yaml
tmpfs:
  - /run
  - /tmp
```

#### `tty`
* `tty` configures service container to run with a TTY.

#### `ulimits`
> [source](https://docs.docker.com/compose/compose-file/05-services/#ulimits)

#### `user`
* `user` overrides the user used to run the container process.
* Default is that set by image (i.e. Dockerfile `USER`), if not set, `root`.

#### `volumes`
* `volumes` defines mount host paths or named volumes that MUST be accessible by service containers.
* If the mount is a host path and is only used by a single service, it MAY be declared as part of the service definition instead of the top-level `volumes` key.
* To reuse a volume across multiple services, a named volume MUST be declared in the [top-level `volumes` key](https://docs.docker.com/compose/compose-file/07-volumes/).

##### Short syntax
* The short syntax uses a single string with colon-separated values to specify a volume mount (`VOLUME:CONTAINER_PATH`), or an access mode (`VOLUME:CONTAINER_PATH:ACCESS_MODE`).
	- `VOLUME`: MAY be either a host path on the platform hosting containers (bind mount) or a volume name
	- `CONTAINER_PATH`: the path in the container where the volume is mounted
	- `ACCESS_MODE`: a comma-separated `,` list of options. MAY be set to:
	    - `rw`: read and write access (default)
	    - `ro`: read-only access
	    - `z`: SELinux option indicating that the bind mount host content is shared among multiple containers
	    - `Z`: SELinux option indicating that the bind mount host content is private and unshared for other containers

##### Long syntax
* The long form syntax allows the configuration of additional fields that can’t be expressed in the short form.
	- `type`: the mount type `volume`, `bind`, `tmpfs` or `npipe`
	- `source`: the source of the mount, a path on the host for a bind mount, or the name of a volume defined in the [top-level `volumes` key](https://docs.docker.com/compose/compose-file/07-volumes/). Not applicable for a tmpfs mount.
	- `target`: the path in the container where the volume is mounted
	- `read_only`: flag to set the volume as read-only
	- `bind`: configure additional bind options
	    - `propagation`: the propagation mode used for the bind
	    - `create_host_path`: create a directory at the source path on host if there is nothing present. Do nothing if there is something present at the path. This is automatically implied by short syntax for backward compatibility with docker-compose legacy.
	    - `selinux`: the SELinux re-labeling option `z` (shared) or `Z` (private)
	- `volume`: configure additional volume options
	    - `nocopy`: flag to disable copying of data from a container when a volume is created
	- `tmpfs`: configure additional tmpfs options
	    - `size`: the size for the tmpfs mount in bytes (either numeric or as bytes unit)
	    - `mode`: the filemode for the tmpfs mount as Unix permission bits as an octal number
	- `consistency`: the consistency requirements of the mount. Available values are platform specific

#### `volumes_from`
* `volumes_from` mounts all of the volumes from another service or container, optionally specifying read-only access (ro) or read-write (rw). If no access level is specified, then read-write MUST be used.
* String value defines another service in the Compose application model to mount volumes from. The `container:` prefix, if supported, allows to mount volumes from a container that is not managed by the Compose implementation.
```yaml
volumes_from:
  - service_name
  - service_name:ro
  - container:container_name
  - container:container_name:rw
```

#### `working_dir`
* `working_dir` overrides the container’s working directory from that specified by the image (i.e. Dockerfile `WORKDIR`).