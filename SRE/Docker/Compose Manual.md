 > [source](https://docs.docker.com/compose/)

* Compose is a tool for defining and running multi-container Docker applications.
* With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.
* Compose works in all environments: production, staging, development, testing, as well as CI workflows.
*  It also has commands for managing the whole lifecycle of your application:
	- Start, stop, and rebuild services
	- View the status of running services
	- Stream the log output of running services
	- Run a one-off command on a service

### Key features and use cases
> [source](https://docs.docker.com/compose/features-uses/)

#### Key features
##### Have multiple isolated environments on a single host
* Compose uses a project name to isolate environments from each other. You can make use of this project name in several different contexts:
	* on a dev host, to create multiple copies of a single environment, **such as** when you want to run a stable copy for each feature branch of a project
	* on a CI server, to keep builds from interfering with each other, you can set the project name to a unique build number
	* on a shared host or dev host, to prevent different projects, which may use the same service names, from interfering with each other
* The default project name is the basename of the project directory. You can set a custom project name by using the [`-p` command line option](https://docs.docker.com/compose/reference/) or the [`COMPOSE_PROJECT_NAME` environment variable](https://docs.docker.com/compose/environment-variables/envvars/#compose_project_name).
* The default project directory is the base directory of the Compose file. A custom value for it can be defined with the `--project-directory` command line option.

##### Preserves volume data when containers are created
* Compose preserves all volumes used by your services. When `docker compose up` runs, if it finds any containers from previous runs, it copies the volumes from the old container to the new container. This process ensures that any data you’ve created in volumes isn’t lost.

##### Only recreate containers that have changed
* Compose caches the configuration used to create a container. When you restart a service that has not changed, Compose re-uses the existing containers. Re-using containers means that you can make changes to your environment very quickly.

##### Supports variables and moving a composition between environments
* Compose supports variables in the Compose file. You can use these variables to customize your composition for different environments, or different users. See [Variable substitution](https://docs.docker.com/compose/compose-file/compose-file-v3/#variable-substitution) (in reference) for more details.
* You can extend a Compose file using the `extends` field or by creating multiple Compose files. See [extends](https://docs.docker.com/compose/extends/) for more details.

#### Common use cases
##### Development environments
* When you’re developing software, the ability to run an application in an isolated environment and interact with it is crucial. The Compose command line tool can be used to create the environment and interact with it.
* The [Compose file](https://docs.docker.com/compose/compose-file/) provides a way to document and configure all of the application’s service dependencies (databases, queues, caches, web service APIs, etc). Using the Compose command line tool you can create and start one or more containers for each dependency with a single command (`docker compose up`).
* Together, these features provide a convenient way for developers to get started on a project. Compose can reduce a multi-page “developer getting started guide” to a single machine readable Compose file and a few commands.

##### Automated testing environments
* An important part of any Continuous Deployment or Continuous Integration process is the automated test suite. Automated end-to-end testing requires an environment in which to run tests. Compose provides a convenient way to create and destroy isolated testing environments for your test suite. By defining the full environment in a [Compose file](https://docs.docker.com/compose/compose-file/), you can create and destroy these environments in just a few commands:
```bash
docker compose up -d
./run_tests
docker compose down
```

##### Single host deployments
* Compose has traditionally been focused on development and testing workflows, but with each release we’re making progress on more production-oriented features.
* For details on using production-oriented features, see [compose in production](https://docs.docker.com/compose/production/) in this documentation.

### Environment variables
> [overview](https://docs.docker.com/compose/environment-variables/)
> [explore ways to set an environment variable](https://docs.docker.com/compose/environment-variables/set-environment-variables/)
> [understand environment variable precedence](https://docs.docker.com/compose/environment-variables/envvars-precedence/)
> [use an environment file](https://docs.docker.com/compose/environment-variables/env-file/)
> [change pre-defined environment variables](https://docs.docker.com/compose/environment-variables/envvars/)
* How the table works:
	* Each column represents a context from where you can set a value, or substitute in a value for `TAG`.
	* The columns `Host OS environment` and `.env file` is listed only as an illustration lookup. In reality, they don’t result in a variable in the container by itself.
	* Each row represents a combination of contexts where `TAG` is set, substituted, or both.

|#|`docker compose run --env`|`environment` attribute|`env_file` attribute|Image `ENV`|`Host OS` environment|`.env` file||Result|
|---|---|---|---|---|---|---|---|---|
|1|-|-|-|-|`TAG=1.4`|`TAG=1.3`||-|
|2|-|-|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.5`**|
|3|`TAG`|-|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.4`**|
|4|-|-|`TAG`|`TAG=1.5`|-|`TAG=1.3`||**`TAG=1.3`**|
|5|`TAG`|-|-|`TAG=1.5`|-|`TAG=1.3`||**`TAG=1.3`**|
|6|`TAG=1.8`|-|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.8`**|
|7|-|`TAG`|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.4`**|
|8|`TAG`|`TAG=1.7`|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.4`**|
|9|`TAG=1.8`|`TAG=1.7`|-|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.8`**|
|10|`TAG=1.8`|-|`TAG=1.6`|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.8`**|
|11|`TAG=1.8`|`TAG=1.7`|`TAG=1.6`|`TAG=1.5`|`TAG=1.4`|`TAG=1.3`||**`TAG=1.8`**|
|12|-|-|`TAG=1.6`|`TAG=1.5`|`TAG=1.4`|-||**`TAG=1.6`**|
|13|-|`TAG=1.7`|-|`TAG=1.5`|`TAG=1.4`|-||**`TAG=1.7`**|

### Using service profiles
> [source](https://docs.docker.com/compose/profiles/)

* Profiles help you adjust the Compose application model for various uses and environments by selectively enabling services. This is achieved by assigning each service to zero or more profiles. If unassigned, the service is always started but if assigned, it is only started if the profile is activated.
* This allows you to define additional services in a single `docker-compose.yml` file that should only be started in specific scenarios, for example for debugging or development tasks.

#### Assigning profiles to services
* Services are associated with profiles through the [`profiles` attribute](https://docs.docker.com/compose/compose-file/05-services/#profiles) which takes an array of profile names:
```yaml
services:
  frontend:
    image: frontend
    profiles: ["frontend"]

  phpmyadmin:
    image: phpmyadmin
    depends_on:
      - db
    profiles:
      - debug

  backend:
    image: backend

  db:
    image: mysql
```
* Here the services `frontend` and `phpmyadmin` are assigned to the profiles `frontend` and `debug` respectively and as such are only started when their respective profiles are enabled.
* Services without a `profiles` attribute are always enabled. In this case running `docker compose up` would only start `backend` and `db`.
* Valid profiles names follow the regex format of `[a-zA-Z0-9][a-zA-Z0-9_.-]+`.

> [!Tip]
> The core services of your application shouldn’t be assigned `profiles` so they are always enabled and automatically started.

#### Enable profiles
* To enable profiles supply the `--profile` [command-line option](https://docs.docker.com/compose/reference/) or use the [`COMPOSE_PROFILES` environment variable](https://docs.docker.com/compose/environment-variables/envvars/#compose_profiles).
	* `docker compose --profile debug up`
	* `COMPOSE_PROFILES=debug docker compose up`

### Extend services in compose
> [source](https://docs.docker.com/compose/extends/)

* Compose supports two methods of sharing common configuration:
	1. Extend an entire Compose file by [using multiple Compose files](https://docs.docker.com/compose/extends/#multiple-compose-files)
	2. Extend individual services with [the `extends` field](https://docs.docker.com/compose/extends/#extending-services)

#### Multiple compose files
* Using multiple Compose files lets you customize a Compose application for different environments or different workflows.
* By default, Compose reads two files, a `docker-compose.yml` and an optional `docker-compose.override.yml` file. By convention, the `docker-compose.yml` contains your base configuration. The override file, as its name implies, can contain configuration overrides for existing services or entirely new services.
* If a service is defined in both files, Compose merges the configurations using the rules described in [Adding and overriding configuration](https://docs.docker.com/compose/extends/#adding-and-overriding-configuration).
* To use multiple override files, or an override file with a different name, you can use the `-f/--file` option to specify the list of files. Compose merges files in the order they’re specified on the command line. See the [`docker compose` command reference](https://docs.docker.com/compose/reference/) for more information about using `-f/--file`.
* When you use multiple configuration files, you must make sure all paths in the files are relative to the base Compose file (the first Compose file specified with `-f`). This is required because override files need not be valid Compose files. Override files can contain small fragments of configuration. Tracking which fragment of a service is relative to which path is difficult and confusing, so to keep paths easier to understand, all paths must be defined relative to the base file.

#### Extending services
* Docker Compose’s `extends` keyword enables the sharing of common configurations among different files, or even different projects entirely. Extending services is useful if you have several services that reuse a common set of configuration options. Using `extends` you can define a common set of service options in one place and refer to it from anywhere.
* Keep in mind that `volumes_from` and `depends_on` are never shared between services using `extends`. These exceptions exist to avoid implicit dependencies; you always define `volumes_from` locally. This ensures dependencies between services are clearly visible when reading the current file. Defining these locally also ensures that changes to the referenced file don’t break anything.
* When defining any service in `docker-compose.yml`, you can declare that you are extending another service like this:
```yaml
services:
  web:
    extends:
      file: common-services.yml
      service: webapp
```
* This instructs Compose to re-use the configuration for the `webapp` service defined in the `common-services.yml` file. Suppose that `common-services.yml` looks like this:
```yaml
services:
  webapp:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - "/data"
```

#### Adding and overriding configuration
* Compose copies configurations from the original service over to the local one. If a configuration option is defined in both the original service and the local service, the local value _replaces_ or _extends_ the original value.
* For single-value options like `image`, `command` or `mem_limit`, the new value replaces the old value.
* For the **multi-value options** `ports`, `expose`, `external_links`, `dns`, `dns_search`, and `tmpfs`, Compose concatenates both sets of values.
* In the case of `environment`, `labels`, `volumes`, and `devices`, Compose “merges” entries together with locally-defined values taking precedence. For `environment` and `labels`, the environment variable or label name determines which value is used.
* Entries for `volumes` and `devices` are merged using the mount path in the container.

### Networking in compose
> [source](https://docs.docker.com/compose/networking/)

* For full details of the network configuration options available, see the following references:
	- [Top-level `networks` key](https://docs.docker.com/compose/compose-file/06-networks/)
	- [Service-level `networks` key](https://docs.docker.com/compose/compose-file/05-services/#networks)

* By default Compose sets up a single [network](https://docs.docker.com/engine/reference/commandline/network_create/) for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.

> [!Note]
> Your app’s network is given a name based on the “project name”, which is based on the name of the directory it lives in. You can override the project name with either the [`--project-name` flag](https://docs.docker.com/compose/reference/) or the [`COMPOSE_PROJECT_NAME` environment variable](https://docs.docker.com/compose/environment-variables/envvars/#compose_project_name).

* For example, suppose your app is in a directory called `myapp`, and your `docker-compose.yml` looks like this:
```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres
    ports:
      - "8001:5432"
```
* When you run `docker compose up`, the following happens:
	1. A network called `myapp_default` is created.
	2. A container is created using `web`’s configuration. It joins the network `myapp_default` under the name `web`.
	3. A container is created using `db`’s configuration. It joins the network `myapp_default` under the name `db`.
* Each container can now look up the hostname `web` or `db` and get back the appropriate container’s IP address. For example, `web`’s application code could connect to the URL `postgres://db:5432` and start using the Postgres database.
* It is important to note the distinction between `HOST_PORT` and `CONTAINER_PORT`. In the above example, for `db`, the `HOST_PORT` is `8001` and the container port is `5432` (postgres default). ***Networked service-to-service communication uses the `CONTAINER_PORT`.*** When `HOST_PORT` is defined, the service is accessible outside the swarm as well.
* Within the `web` container, your connection string to `db` would look like `postgres://db:5432`, and from the host machine, the connection string would look like `postgres://{DOCKER_IP}:8001` for example `postgres://localhost:8001` if your container is running locally.
	* **THIS IS AMAZING!! WHYYYYY????** #todo 

#### Update containers on the network
* If you make a configuration change to a service and run `docker compose up` to update it, the old container is removed and the new one joins the network under a different IP address but the same name. Running containers can look up that name and connect to the new address, but the old address stops working.
* If any containers have connections open to the old container, they are closed. It is a container’s responsibility to detect this condition, look up the name again and reconnect.

> [!Tip]
> Reference containers by name, not IP, whenever possible. Otherwise you’ll need to constantly update the IP address you use.

#### Link containers
* Links allow you to define extra aliases by which a service is reachable from another service. They are not required to enable services to communicate. By default, any service can reach any other service at that service’s name. In the following example, `db` is reachable from `web` at the hostnames `db` and `database`:
```yaml
services:

  web:
    build: .
    links:
      - "db:database"
  db:
    image: postgres
```
* See the [links reference](https://docs.docker.com/compose/compose-file/05-services/#links) for more information.

#### Multi-host networking
* When deploying a Compose application on a Docker Engine with [Swarm mode enabled](https://docs.docker.com/engine/swarm/), you can make use of the built-in `overlay` driver to enable multi-host communication.
* Overlay networks are always created as `attachable`. You can optionally set the [`attachable`](https://docs.docker.com/compose/compose-file/06-networks/#attachable) property to `false`.
* Consult the [Swarm mode section](https://docs.docker.com/engine/swarm/), to see how to set up a Swarm cluster, and the [Getting started with multi-host networking](https://docs.docker.com/network/network-tutorial-overlay/) to learn about multi-host overlay networks.

#### Specify custom networks
* Instead of just using the default app network, you can specify your own networks with the top-level `networks` key. This lets you create more complex topologies and specify [custom network drivers](https://docs.docker.com/engine/extend/plugins_network/) and options. You can also use it to connect services to externally-created networks which aren’t managed by Compose.
* Each service can specify what networks to connect to with the service-level `networks` key, which is a list of names referencing entries under the top-level `networks` key.
* Networks can be configured with static IP addresses by setting the [ipv4_address and/or ipv6_address](https://docs.docker.com/compose/compose-file/05-services/#ipv4_address-ipv6_address) for each attached network.
* Networks can also be given a [custom name](https://docs.docker.com/compose/compose-file/06-networks/#name):
```yaml
services:
  # ...
networks:
  frontend:
    name: custom_frontend
    driver: custom-driver-1
```

#### Configure the default network
* Instead of, or as well as, specifying your own networks, you can also change the settings of the app-wide default network by defining an entry under `networks` named `default`.

#### Use a pre-existing network
* If you want your containers to join a pre-existing network, use [`external` option](https://docs.docker.com/compose/compose-file/06-networks/#external)
* Instead of attempting to create a network called `[projectname]_default`, Compose looks for a network called `my-pre-existing-network` and connects your app’s containers to it.

### Using compose in production
> [source](https://docs.docker.com/compose/production/)

* When you define your app with Compose in development, you can use this definition to run your application in different environments such as CI, staging, and production.
* The easiest way to deploy an application is to run it on a single server, similar to how you would run your development environment. If you want to scale up your application, you can run Compose apps on a Swarm cluster.

#### Modify your compose file for production
* You may need to make changes to your app configuration to make it ready for production. These changes might include:
	* Removing any volume bindings for application code, so that code stays inside the container and can’t be changed from outside
	* Binding to different ports on the host
	* Setting environment variables differently, such as reducing the verbosity of logging, or to specify settings for external services such as an email server
	* Specifying a restart policy like [`restart: always`](https://docs.docker.com/compose/compose-file/05-services/#restart) to avoid downtime
	* Adding extra services such as a log aggregator
* For this reason, consider defining an additional Compose file, say `production.yml`, which specifies production-appropriate configuration. This configuration file only needs to include the changes you want to make from the original Compose file. The additional Compose file is then applied over the original `docker-compose.yml` to create a new configuration.
	* `docker compose -f docker-compose.yml -f production.yml up -d`

#### Deploying changes
* When you make changes to your app code, remember to rebuild your image and recreate your app’s containers. To redeploy a service called `web`, use:
```bash
docker compose build web
docker compose up --no-deps -d web
```
* This first command rebuilds the image for `web` and then stops, destroys, and recreates just the `web` service. The `--no-deps` flag prevents Compose from also recreating any services which `web` depends on.

#### Running compose on a single server
* You can use Compose to deploy an app to a remote Docker host by setting the `DOCKER_HOST`, `DOCKER_TLS_VERIFY`, and `DOCKER_CERT_PATH` environment variables appropriately. See also [Compose CLI environment variables](https://docs.docker.com/compose/environment-variables/envvars/).
* Once you’ve set up your environment variables, all the normal `docker compose` commands work with no further configuration.

### Using secrets in compose
> [source](https://docs.docker.com/compose/use-secrets/)

* [Resources](https://docs.docker.com/compose/use-secrets/#resources):
	- [Secrets top-level element](https://docs.docker.com/compose/compose-file/09-secrets/)
	- [Secrets attribute for services top-level element](https://docs.docker.com/compose/compose-file/05-services/#secrets)

* A secret is any piece of data, such as a password, certificate, or API key, that shouldn’t be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.
* Docker Compose provides a way for you to use secrets without having to use environment variables to store information. If you’re injecting passwords and API keys as environment variables, you risk unintentional information exposure. Environment variables are often available to all processes, and it can be difficult to track access. They can also be printed in logs when debugging errors without your knowledge. Using secrets mitigates these risks.

* Getting a secret into a container is a two-step process. First, define the secret using the [top-level secrets attribute in your Compose file](https://docs.docker.com/compose/compose-file/09-secrets/). Next, update your service definitions to reference the secrets they require with the [secrets attribute](https://docs.docker.com/compose/compose-file/05-services/#secrets). Compose grants access to secrets on a per-service basis.
* Unlike the other methods, this permits granular access control within a service container via standard filesystem permissions.
* In the following example, the frontend service is given access to the `my_secret` secret. In the container, `/run/secrets/my_secret` is set to the contents of the file `./my_secret.txt`.
```yaml
services:
  myapp:
    image: myapp:latest
    secrets:
      - my_secret
secrets:
  my_secret:
    file: ./my_secret.txt
```
* In the advanced example above:
	* The `secrets` attribute under each service defines the secrets you want to inject into the specific container.
	* The top-level secrets section defines the variables `db_password` and `db_root_password` and provides the file that populates their values.
	* The deployment of each container means Docker creates a temporary filesystem mount under `/run/secrets/<secret_name>` with their specific values.

### Control startup order
> [source](https://docs.docker.com/compose/startup-order/)

* You can control the order of service startup and shutdown with the [depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on) option. Compose always starts and stops containers in dependency order, where dependencies are determined by `depends_on`, `links`, `volumes_from`, and `network_mode: "service:..."`.
* A good example of when you might use this is an application which needs to access a database. If both services are started with `docker compose up`, there is a chance this will fail since the application service might start before the database service and won’t find a database able to handle its SQL statements.
* On startup, Compose does not wait until a container is “ready”, only until it’s running. This can cause issues if, for example, you have a relational database system that needs to start its own services before being able to handle incoming connections.
* The solution for detecting the ready state of a service is to use the `condition` attribute with one of the following options:
	- `service_started`
	- `service_healthy`. This specifies that a dependency is expected to be “healthy”, which is defined with `healthcheck`, before starting a dependent service.
	- `service_completed_successfully`. This specifies that a dependency is expected to run to successful completion before starting a dependent service.