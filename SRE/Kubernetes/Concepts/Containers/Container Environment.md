> [source](https://kubernetes.io/docs/concepts/containers/container-environment/)

* The Kubernetes Container environment provides several important resources to Containers:
	* A filesystem, which is a combination of an [image](https://kubernetes.io/docs/concepts/containers/images/) and one or more [volumes](https://kubernetes.io/docs/concepts/storage/volumes/).
	* Information about the Container itself.
	* Information about other objects in the cluster.

### Container Information
* The hostname of a Container is the name of the Pod in which the Container is running. It is available through the `hostname` command or the [`gethostname`](https://man7.org/linux/man-pages/man2/gethostname.2.html) function call in libc.
* The Pod name and namespace are available as environment variables through the [downward API](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/).
* User defined environment variables from the Pod definition are also available to the Container, as are any environment variables specified statically in the container image.

### Cluster information
* A list of all services that were running when a Container was created is available to that Container as environment variables. This list is limited to services within the same namespace as the new Container's Pod and Kubernetes control plane services.
* For a service named foo that maps to a Container named bar, the following variables are defined:
	```bash
	FOO_SERVICE_HOST=<the host the service is running on>
	FOO_SERVICE_PORT=<the port the service is running on>
	```
* Services have dedicated IP addresses and are available to the Container via DNS, if [DNS addon](https://releases.k8s.io/v1.28.2/cluster/addons/dns/) is enabled.