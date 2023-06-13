> [source](https://docs.docker.com/compose/compose-file/)

* The Compose file is a [YAML](https://yaml.org/) file defining services, networks, and volumes for a Docker application.

### Table of contents
* [[SRE/Docker/Composefile reference/Composefile reference#Application model|Application model]]
* [[SRE/Docker/Composefile reference/Composefile reference#The compose file|The compose file]]
* [[SRE/Docker/Composefile reference/Composefile reference#Profiles|Profiles]]
* [[SRE/Docker/Composefile reference/Composefile reference#Version and name top-level element|Version and name]]
* [[SRE/Docker/Composefile reference/Services|Services]]
* [[SRE/Docker/Composefile reference/Composefile reference#Network top-level element|Networks]]
* [[SRE/Docker/Composefile reference/Composefile reference#Volumes top-level element|Volumes]]
* [[SRE/Docker/Composefile reference/Composefile reference#Configs top-level element|Configs]]
* [[SRE/Docker/Composefile reference/Composefile reference#Secrets top-level element|Secrets]]
* [[SRE/Docker/Composefile reference/Composefile reference#Fragments|Fragments]]
* [[SRE/Docker/Composefile reference/Composefile reference#Extensions|Extensions]]
* [[SRE/Docker/Composefile reference/Composefile reference#Interpolation|Interpolation]]

### Application model
> [source](https://docs.docker.com/compose/compose-file/02-model/)

* Computing components of an application are defined as [Services](https://docs.docker.com/compose/compose-file/05-services/). 
* A Service is an abstract concept implemented on platforms by running the same container image (and configuration) one or more times.

* Services communicate with each other through [Networks](https://docs.docker.com/compose/compose-file/06-networks/).
* A Network is a platform capability abstraction to establish an IP route between containers within services connected together.

* Services store and share persistent data into [Volumes](https://docs.docker.com/compose/compose-file/07-volumes/).
* The specification describes such a persistent data as a high-level filesystem mount with global options.

* Some services require configuration data that is dependent on the runtime or platform. For this, the specification defines a dedicated concept: [Configs](https://docs.docker.com/compose/compose-file/08-configs/).
* From a Service container point of view, Configs are comparable to Volumes, in that they are files mounted into the container. But the actual definition involves *distinct platform resources and services*, which are abstracted by this type.

* A [Secret](https://docs.docker.com/compose/compose-file/09-secrets/) is a specific flavor of configuration data for sensitive data that SHOULD NOT be exposed without security considerations.
* Secrets are made available to services as files mounted into their containers, but the platform-specific resources to provide sensitive data are specific enough to deserve a distinct concept and definition within the Compose specification.

* A **Project** is an individual deployment of an application specification on a platform.
* A project’s name is used to group resources together and isolate them from other applications or other installation of the same Compose specified application with distinct parameters.
*  Compose implementation creating resources on a platform MUST prefix resource names by project and set the label `com.docker.compose.project`.

* Project name can be set explicitly by top-level `name` attribute. Compose implementation MUST offer a way for user to set a custom project name and override this name, so that the same `compose.yaml` file can be deployed twice on the same infrastructure, without changes, by just passing a distinct name.
* Project name MUST contain only lowercase letters, decimal digits, dashes, and underscores, and MUST begin with a lowercase letter or decimal digit.

### The compose file
> [source](https://docs.docker.com/compose/compose-file/03-compose-file/)

* The Compose file is a [YAML](http://yaml.org/) file defining [version](https://docs.docker.com/compose/compose-file/04-version-and-name/) (DEPRECATED), [services](https://docs.docker.com/compose/compose-file/05-services/) (REQUIRED), [networks](https://docs.docker.com/compose/compose-file/06-networks/), [volumes](https://docs.docker.com/compose/compose-file/07-volumes/), [configs](https://docs.docker.com/compose/compose-file/08-configs/) and [secrets](https://docs.docker.com/compose/compose-file/09-secrets/).
* The default path for a Compose file is `compose.yaml` (preferred) or `compose.yml` in working directory.
* Compose implementations SHOULD also support `docker-compose.yaml` and `docker-compose.yml` for backward compatibility. If both files exist, Compose implementations MUST prefer canonical `compose.yaml` one.

* Multiple Compose files can be combined together to define the application model. The combination of YAML files MUST be implemented by appending/overriding YAML elements based on Compose file order set by the user.
* Simple attributes and maps get overridden by the highest order Compose file, lists get merged by appending. Relative paths MUST be resolved based on the **first** Compose file’s parent folder, whenever complimentary files being merged are hosted in other folders. As some Compose file elements can both be expressed as single strings or complex objects, merges MUST apply to the expanded form.

### Profiles
* Profiles allow to adjust the Compose application model for various usages and environments. A Compose implementation SHOULD allow the user to define a set of active profiles.

* The Services top-level element supports a `profiles` attribute to define a list of named profiles.
* Services without a `profiles` attribute set MUST always be enabled.
* A service MUST be ignored by the Compose implementation when none of the listed `profiles` match the active ones, unless the service is explicitly targeted by a command. In that case its `profiles` MUST be added to the set of active profiles.
* All other top-level elements are not affected by `profiles` and are always active.

> [!Warning]
> There was an example that explained how the automatically enabling of a profile works. This one was good.

### Version and name top-level element
> [source](https://docs.docker.com/compose/compose-file/04-version-and-name/)

* Top-level `version` property is defined by the specification for backward compatibility but is only informative.
* A Compose implementation SHOULD NOT use this version to select an exact schema to validate the Compose file, but prefer the most recent schema at the time it has been designed.

* Compose implementations SHOULD validate whether they can fully parse the Compose file. If some fields are unknown, typically because the Compose file was written with fields defined by a newer version of the specification, Compose implementations SHOULD warn the user. Compose implementations MAY offer options to ignore unknown fields (as defined by [“loose”](https://docs.docker.com/compose/compose-file/01-status/#requirements-and-optional-attributes) mode).

* Top-level `name` property is defined by the specification as project name to be used if user doesn’t set one explicitly.
* Compose implementations MUST offer a way for user to override this name, and SHOULD define a mechanism to compute a default project name to be used if the top-level `name` element is not set.
* Whenever project name is defined by top-level `name` or by some custom mechanism, it MUST be exposed for [interpolation](https://docs.docker.com/compose/compose-file/12-interpolation/) and environment variable resolution as `COMPOSE_PROJECT_NAME`
```yaml
services:
  foo:
    image: busybox
    environment:
      - COMPOSE_PROJECT_NAME
    command: echo "I'm running ${COMPOSE_PROJECT_NAME}"
```

### Network top-level element
> [source](https://docs.docker.com/compose/compose-file/06-networks/)

* Networks are the layer that allow services to communicate with each other.
* The networking model exposed to a service is limited to a simple IP connection with target services and external resources, while the Network definition allows fine-tuning the actual implementation provided by the platform.

* etworks can be created by specifying the network name under a top-level `networks` section.
* Services can connect to networks by specifying the network name under the service [`networks`](https://docs.docker.com/compose/compose-file/05-services/#networks) subsection

#### `driver`
* specifies which driver should be used for this network. Compose implementations MUST return an error if the driver is not available on the platform.
* Default and available values are platform specific. Compose specification MUST support the following specific drivers: `none` and `host`
	- `host` use the host’s networking stack
	- `none` disable networking

#### `host` or `none`
* The syntax for using built-in networks such as `host` and `none` is different, as such networks implicitly exist outside the scope of the Compose implementation.
* To use them, one MUST define an external network with the name `host` or `none` and an alias that the Compose implementation can use (`hostnet` and `nonet` in the following examples), then grant the service access to that network using its alias.
```yaml
services:
  web:
    networks:
      hostnet: {}

networks:
  hostnet:
    external: true
    name: host
```
```yaml
services:
  web:
    ...
    networks:
      nonet: {}

networks:
  nonet:
    external: true
    name: none
```

#### `driver_opts`
* specifies a list of options as key-value pairs to pass to the driver for this network. These options are driver-dependent - consult the [driver’s documentation](https://docs.docker.com/network/drivers/) for more information. Optional.

#### `attachable`
* If `attachable` is set to `true`, then standalone containers SHOULD be able to attach to this network, in addition to services.
* If a standalone container attaches to the network, it can communicate with services and other standalone containers that are also attached to the network.

#### `enable_ipv6`
* enable IPv6 networking on this network.

#### `ipam`
* specifies custom a IPAM configuration. This is an object with several properties, each of which is optional:
	- `driver`: Custom IPAM driver, instead of the default.
	- `config`: A list with zero or more configuration elements, each containing:
	    - `subnet`: Subnet in CIDR format that represents a network segment
	    - `ip_range`: Range of IPs from which to allocate container IPs
	    - `gateway`: IPv4 or IPv6 gateway for the master subnet
	    - `aux_addresses`: Auxiliary IPv4 or IPv6 addresses used by Network driver, as a mapping from hostname to IP
	- `options`: Driver-specific options as a key-value mapping.
```yaml
ipam:
  driver: default
  config:
    - subnet: 172.28.0.0/16
      ip_range: 172.28.5.0/24
      gateway: 172.28.5.254
      aux_addresses:
        host1: 172.28.1.5
        host2: 172.28.1.6
        host3: 172.28.1.7
  options:
    foo: bar
    baz: "0"
```
* chatGPT prompt: `docker compose file network attribute allows ipam configurations. What is ipam?`
	* In the context of Docker Compose, IPAM stands for IP Address Management. It is a feature that allows you to manage the allocation and assignment of IP addresses to the containers within a Docker network.
	* Each network can have its own IPAM configuration, which specifies how IP addresses are assigned to the containers within that network.
	* When you specify IPAM configurations for a network in the Docker Compose file, you can control aspects such as the IP address range, subnet, gateway, and other options related to IP address management.
	* By using IPAM configurations, you can have more control over the IP address assignment within your Docker network, ensuring that containers are assigned IP addresses according to your specific requirements.

#### `internal`
* By default, Compose implementations MUST provides external connectivity to networks.
* `internal`, when set to `true`, allows creating an externally isolated network.

#### `labels`
* Add metadata to containers using Labels. Can use either an array or a dictionary.
* Users SHOULD use reverse-DNS notation to prevent labels from conflicting with those used by other software.
```yaml
labels:
  com.example.description: "Financial transaction network"
  com.example.department: "Finance"
  com.example.label-with-empty-value: ""
```
```yaml
labels:
  - "com.example.description=Financial transaction network"
  - "com.example.department=Finance"
  - "com.example.label-with-empty-value"
```
* Compose implementations MUST set `com.docker.compose.project` and `com.docker.compose.network` labels.

#### `external`
* If set to `true`, `external` specifies that this network’s lifecycle is maintained outside of that of the application. Compose Implementations SHOULD NOT attempt to create these networks, and SHOULD raise an error if one doesn’t exist.
* If `external` is set to `true` and network configuration has other but `name` attributes set, considering resource is not managed by compose lifecycle, Compose Implementations SHOULD reject the Compose file as invalid.

* In the example below, `proxy` is the gateway to the outside world. Instead of attempting to create a network, Compose implementations SHOULD interrogate the platform for an existing network simply called `outside` and connect the `proxy` service’s containers to it.
```yaml
services:
  proxy:
    image: awesome/proxy
    networks:
      - outside
      - default
  app:
    image: awesome/app
    networks:
      - default

networks:
  outside:
    external: true
```

#### `name`
* `name` sets a custom name for this network. The name field can be used to reference networks which contain special characters. The name is used as is and will **not** be scoped with the project name.
```yaml
networks:
  network1:
    name: my-app-net
```
* It can also be used in conjunction with the `external` property to define the platform network that the Compose implementation should retrieve, typically by using a parameter so the Compose file doesn’t need to hard-code runtime specific values:
```yaml
networks:
  network1:
    external: true
    name: "${NETWORK_ID}"
```

### Volumes top-level element
> [source](https://docs.docker.com/compose/compose-file/07-volumes/)

* Volumes are persistent data stores implemented by the platform.
* The Compose specification offers a neutral abstraction for services to mount volumes, and configuration parameters to allocate them on infrastructure.

* The `volumes` section allows the configuration of named volumes that can be reused across multiple services.
* An entry under the top-level `volumes` key can be empty, in which case it uses the platform’s default configuration for creating a volume.

#### `driver`
* Specify which volume driver should be used for this volume.
* Default and available values are platform specific. If the driver is not available, the Compose implementation MUST return an error and stop application deployment.

#### `driver_opts`
* specifies a list of options as key-value pairs to pass to the driver for this volume. 
* Those options are driver-dependent.

#### `external`
* If set to `true`, `external` specifies that this volume already exists on the platform and its lifecycle is managed outside of that of the application.
* If `external` is set to `true` and volume configuration has other but `name` attributes set, considering resource is not managed by compose lifecycle, Compose Implementations SHOULD reject the Compose file as invalid.

#### `labels`
* `labels` are used to add metadata to volumes. You can use either an array or a dictionary.
* It’s recommended that you use reverse-DNS notation to prevent your labels from conflicting with those used by other software.
```yaml
labels:
  com.example.description: "Database volume"
  com.example.department: "IT/Ops"
  com.example.label-with-empty-value: ""
```
```yaml
labels:
  - "com.example.description=Database volume"
  - "com.example.department=IT/Ops"
  - "com.example.label-with-empty-value"
```
* Compose implementation MUST set `com.docker.compose.project` and `com.docker.compose.volume` labels.

#### `name`
* `name` set a custom name for this volume. The name field can be used to reference volumes that contain special characters.
* The name is used as is and will **not** be scoped with the stack name.
```yaml
volumes:
  data:
    name: "my-app-data"
```
* It can also be used in conjunction with the `external` property. In that case the name of the volume used to lookup for actual volume on platform is set separately from the name used to refer to it within the Compose file:
```yaml
volumes:
  db-data:
    external:
      name: actual-name-of-volume
```
* This makes it possible to make this lookup name a parameter of the Compose file, so that the model ID for volume is hard-coded but the actual volume ID on platform is set at runtime during deployment:
```yaml
volumes:
  db-data:
    external:
      name: ${DATABASE_VOLUME}
```

### Configs top-level element
> [source](https://docs.docker.com/compose/compose-file/08-configs/)

* Configs allow services to adapt their behaviour without the need to rebuild a Docker image.
* Configs are comparable to Volumes **from a service point of view** as they are mounted into service’s container’s filesystem.
* The actual implementation detail to get the configuration provided by the platform can be set from the Configuration definition.

* When granted access to a config, the config content is mounted as a file in the container.
* The location of the mount point within the container defaults to `/<config-name>` in Linux containers.

* By default, the config MUST be owned by the user running the container command but can be overridden by service configuration.
* By default, the config MUST have world-readable permissions (mode 0444), unless service is configured to override this.

* Services can only access configs when explicitly granted by a [`configs`](https://docs.docker.com/compose/compose-file/05-services/#configs) subsection.
* The top-level `configs` declaration defines or references configuration data that can be granted to the services in this application. The source of the config is either `file` or `external`.
	- `file`: The config is created with the contents of the file at the specified path.
	- `external`: If set to true, specifies that this config has already been created. Compose implementation does not attempt to create it, and if it does not exist, an error occurs.
	- `name`: The name of the config object on Platform to lookup. This field can be used to reference configs that contain special characters. The name is used as is and will **not** be scoped with the project name.

* In this example, `<project_name>_http_config` is created when the application is deployed, by registering the content of the `httpd.conf` as configuration data.
```yaml
configs:
  http_config:
    file: ./httpd.conf
```
* Alternatively, `http_config` can be declared as external. The Compose implementation will lookup `http_config` to expose configuration data to relevant services.
```yaml
configs:
  http_config:
    external: true
```
* External configs lookup can also use a distinct key by specifying a `name`. The following example modifies the previous one to lookup for config using a parameter `HTTP_CONFIG_KEY`. The the actual lookup key will be set at deployment time by [interpolation](https://docs.docker.com/compose/compose-file/12-interpolation/) of variables, but exposed to containers as hard-coded ID `http_config`.
```yaml
configs:
  http_config:
    external: true
    name: "${HTTP_CONFIG_KEY}"
```
* If `external` is set to `true` and the configuration has other but `name` attributes set, considering resource is not managed by compose lifecycle, Compose Implementations SHOULD reject the Compose file as invalid.
* Compose file need to explicitly grant access to the configs to relevant services in the application.

### Secrets top-level element
> [source](https://docs.docker.com/compose/compose-file/09-secrets/)

* Secrets are a flavour of Configs focusing on sensitive data, with specific constraint for this usage.
* As the platform implementation may significantly differ from Configs, dedicated Secrets section allows to configure the related resources.

* The top-level `secrets` declaration defines or references sensitive data that can be granted to the services in this application.
*  The source of the secret is either `file` or `external`.
	- file at the specified path.
	- `environment`: The secret is created with the value of an environment variable.
	- `external`: If set to true, specifies that this secret has already been created. Compose implementation does not attempt to create it, and if it does not exist, an error occurs.
	- `name`: The name of the secret object in Docker. This field can be used to reference secrets that contain special characters. The name is used as is and will **not** be scoped with the project name.

* In this example, `server-certificate` secret is created as `<project_name>_server-certificate` when the application is deployed, by registering content of the `server.cert` as a platform secret.
```yaml
secrets:
  server-certificate:
    file: ./server.cert
```

* In this example, `token` secret is created as `<project_name>_token` when the application is deployed, by registering content of the `OAUTH_TOKEN` environment variable as a platform secret.
```yaml
secrets:
  token:
    environment: "OAUTH_TOKEN"
```

* Alternatively, `server-certificate` can be declared as external. The Compose implementation will lookup `server-certificate` secret to expose to relevant services.
```yaml
secrets:
  server-certificate:
    external: true
```

* External secrets lookup can also use a distinct key by specifying a `name`. The following example modifies the previous one to look up for secret using a parameter `CERTIFICATE_KEY`. The the actual lookup key will be set at deployment time by [interpolation](https://docs.docker.com/compose/compose-file/12-interpolation/) of variables, but exposed to containers as hard-coded ID `server-certificate`.
```yaml
secrets:
  server-certificate:
    external: true
    name: "${CERTIFICATE_KEY}"
```
* If `external` is set to `true` and secret configuration has other but `name` attributes set, considering resource is not managed by compose lifecycle, Compose implementations SHOULD reject the Compose file as invalid.
* Compose file needs to explicitly grant access to the secrets to relevant services in the application.

### Fragments
> [source](https://docs.docker.com/compose/compose-file/10-fragments/)

* With Docker Compose you can use built-in [YAML](http://www.yaml.org/spec/1.2/spec.html#id2765878) features to make your Compose file neater and more efficient. Anchors and aliases let you create re-usable blocks. This is useful if you start to find common configurations that span multiple services. Having re-usable blocks minimizes potential mistakes.
* Anchors are created using the `&` sign. The sign is followed by an alias name. You can use this alias with the `*` sign later to reference the value following the anchor. Make sure there is no space between the `&` and the `*` characters and the following alias name.
* You can use more than one anchor and alias in a single Compose file.

#### Example 1
```yaml
volumes:
  db-data: &default-volume
    driver: default
  metrics: *default-volume
```
* In the example above, a `default-volume` anchor is created based on the `db-data` volume. It is later reused by the alias `*default-volume` to define the `metrics` volume.
* Anchor resolution **MUST** take place before [variables interpolation](https://docs.docker.com/compose/compose-file/12-interpolation/), so variables can’t be used to set anchors or aliases.

#### Example 2
```yaml
services:
  first:
    image: my-image:latest
    environment: &env
      - CONFIG_KEY
      - EXAMPLE_KEY
      - DEMO_VAR
  second:
    image: another-image:latest
    environment: *env
```
* If you have an anchor that you want to use in more than one service, use it in conjunction with an [extension](https://docs.docker.com/compose/compose-file/11-extension/) to make your Compose file easier to maintain.

#### Example 3
* You may want to partially override values. Compose follows the rule outlined by [YAML merge type](http://yaml.org/type/merge.html).
* In the following example, `metrics` volume specification uses alias to avoid repetition but overrides `name` attribute:
```yaml
services:
  backend:
    image: awesome/database
    volumes:
      - db-data
      - metrics
volumes:
  db-data: &default-volume
    driver: default
    name: "data"
  metrics:
    <<: *default-volume
    name: "metrics"
```

#### Example 4
* You can also extend the anchor to add additional values.
```yaml
services:
  first:
    image: my-image:latest
    environment: &env
      FOO: BAR
      ZOT: QUIX
  second:
    image: another-image:latest
    environment:
      <<: *env
      YET_ANOTHER: VARIABLE
```
* Note that [YAML merge](https://docs.docker.com/compose/compose-file/10-fragments/(http://yaml.org/type/merge.html)) only applies to mappings, and can’t be used with sequences. In previous example, the environment variables MUST be declared using the `FOO: BAR` mapping syntax, while the sequence syntax `- FOO=BAR` is only valid when no fragments are involved.

### Extensions
> [source](https://docs.docker.com/compose/compose-file/11-extension/)

* As with [Fragments](https://docs.docker.com/compose/compose-file/10-fragments/), Extensions can be used to make your Compose file more efficient and easier to maintain. Extensions can also be used with [anchors and aliases](https://docs.docker.com/compose/compose-file/10-fragments/).
* Use the prefix `x-` on any top-level element to modularize configurations that you want to reuse. They can be used within any structure in a Compose file as Docker Compose ignores any fields that start with `x-`. This is the sole exception for Compose implementations to silently ignore unrecognized fields.
* The contents of any `x-` section is unspecified by Compose specification, so it can be used to enable custom features. If the compose implementation encounters an unknown extension field it MUST NOT fail, but COULD warn the user about the unknown field.

#### Example 1
```yaml
x-custom:
  foo:
    - bar
    - zot

services:
  webapp:
    image: awesome/webapp
    x-foo: bar
```
* For platform extensions, it is highly recommended to prefix extension by platform/vendor name, the same way browsers add support for [custom CSS features](https://www.w3.org/TR/2011/REC-CSS2-20110607/syndata.html#vendor-keywords)
```yaml
service:
  backend:
    deploy:
      placement:
        x-aws-role: "arn:aws:iam::XXXXXXXXXXXX:role/foo"
        x-aws-region: "eu-west-3"
        x-azure-region: "france-central"
```

#### Example 2
```yaml
x-env: &env
  environment:
    - CONFIG_KEY
    - EXAMPLE_KEY
 
services:
  first:
    <<: *env
    image: my-image:latest
  second:
    <<: *env
    image: another-image:latest
```
* In this example, the environment variables do not belong to either of the services. They’ve been lifted out completely, into the `x-env` extension field. This defines a new node which contains the environment field. A YAML anchor is used (`&env`) so both services can reference the extension field’s value as `*env`.

#### Example 3
```yaml
x-function: &function
 labels:
   function: "true"
 depends_on:
   - gateway
 networks:
   - functions
 deploy:
   placement:
     constraints:
       - 'node.platform.os == linux'
services:
 # Node.js gives OS info about the node (Host)
 nodeinfo:
   <<: *function
   image: functions/nodeinfo:latest
   environment:
     no_proxy: "gateway"
     https_proxy: $https_proxy
 # Uses `cat` to echo back response, fastest function to execute.
 echoit:
   <<: *function
   image: functions/alpine:health
   environment:
     fprocess: "cat"
     no_proxy: "gateway"
     https_proxy: $https_proxy
```
* The `nodeinfo` and `echoit` services both use merge it in, then set their specific image and environment.

#### Example 4
* Using [YAML merge](https://docs.docker.com/compose/compose-file/11-extension/yaml.org/type/merge.html) it is also possible to use multiple extensions and shared and override additional for specific needs:
```yaml
x-environment: &default-environment
  FOO: BAR
  ZOT: QUIX
x-keys: &keys
  KEY: VALUE
services:
  frontend:
    image: awesome/webapp
    environment: 
      << : [*default-environment, *keys]
      YET_ANOTHER: VARIABLE
```
* Note that [YAML merge](https://docs.docker.com/compose/compose-file/11-extension/(http://yaml.org/type/merge.html)) only applies to mappings, and can’t be used with sequences. In previous example, the environment variables MUST be declared using the `FOO: BAR` mapping syntax, while the sequence syntax `- FOO=BAR` is only valid when no fragments are involved.

#### Specifying byte values
* Values express a byte value as a string in `{amount}{byte unit}` format: The supported units are `b` (bytes), `k` or `kb` (kilo bytes), `m` or `mb` (mega bytes) and `g` or `gb` (giga bytes).
```yaml
2b
    1024kb
    2048k
    300m
    1gb
```

#### Specifying durations
* Values express a duration as a string in the form of `{value}{unit}`. The supported units are `us` (microseconds), `ms` (milliseconds), `s` (seconds), `m` (minutes) and `h` (hours). Values can combine multiple values without separator.
```yaml
10ms
  40s
  1m30s
  1h5m30s20ms
```

### Interpolation
> [source](https://docs.docker.com/compose/compose-file/12-interpolation/)

* Values in a Compose file can be set by variables and interpolated at runtime. Compose files use a Bash-like syntax `${VARIABLE}`
* Both `$VARIABLE` and `${VARIABLE}` syntax is supported. Default values can be defined inline using typical shell syntax:
	- `${VARIABLE:-default}` evaluates to `default` if `VARIABLE` is unset or empty in the environment.
	- `${VARIABLE-default}` evaluates to `default` only if `VARIABLE` is unset in the environment.
- Similarly, the following syntax allows you to specify mandatory variables:
	- `${VARIABLE:?err}` exits with an error message containing `err` if `VARIABLE` is unset or empty in the environment.
	- `${VARIABLE?err}` exits with an error message containing `err` if `VARIABLE` is unset in the environment.
- Interpolation can also be nested:
	- `${VARIABLE:-${FOO}}`
	- `${VARIABLE?$FOO}`
	- `${VARIABLE:-${FOO:-default}}`
- Other extended shell-style features, such as `${VARIABLE/foo/bar}`, are not supported by the Compose specification.
- You can use a `$$` (double-dollar sign) when your configuration needs a literal dollar sign. This also prevents Compose from interpolating a value, so a `$$` allows you to refer to environment variables that you don’t want processed by Compose.
```yaml
web:
  build: .
  command: "$$VAR_NOT_INTERPOLATED_BY_COMPOSE"
```
* If the Compose implementation can’t resolve a substituted variable and no default value is defined, it MUST warn the user and substitute the variable with an empty string.
* As any values in a Compose file can be interpolated with variable substitution, including compact string notation for complex elements, interpolation MUST be applied _before_ merge on a per-file basis.
* Interpolation applies only to YAML _values_, not to _keys_. For the few places where keys are actually arbitrary user-defined strings, such as [labels](https://docs.docker.com/compose/compose-file/12-interpolation/#labels) or [environment](https://docs.docker.com/compose/compose-file/12-interpolation/#environment), an alternate equal sign syntax MUST be used for interpolation to apply:
```yaml
services:
  foo:
    labels:
      "$VAR_NOT_INTERPOLATED_BY_COMPOSE": "BAR"
```
```yaml
services:
  foo:
    labels:
      - "$VAR_INTERPOLATED_BY_COMPOSE=BAR"
```