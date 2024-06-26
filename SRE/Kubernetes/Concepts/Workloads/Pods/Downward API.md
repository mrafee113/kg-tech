> [source](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/)

* It is sometimes useful for a container to have information about itself, without being overly coupled to Kubernetes. The downward API allows containers to consume information about themselves or the cluster without using the Kubernetes client or API server.
* An example is an existing application that assumes a particular well-known environment variable holds a unique identifier. One possibility is to wrap the application, but that is tedious and error-prone, and it violates the goal of low coupling. A better option would be to use the Pod's name as an identifier, and inject the Pod's name into the well-known environment variable.
* In Kubernetes, there are two ways to expose Pod and container fields to a running container:
	* as [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
	* as [files in the downward API volume](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

### Available fields
* Only some Kubernetes API fields are available through the downward API. This section lists which fields you can make available.
* You can pass information from available Pod-level fields using `fieldRef`. At the API level, the `spec` for a Pod always defines at least one [Container](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container). You can pass information from available Container-level fields using `resourceFieldRef`.

#### Information available via `fieldRef`
* For some Pod-level fields, you can provide them to a container either as an environment variable or using a `downwardAPI` volume. The fields available via either mechanism are:
	* `metadata.name`
	* `metadata.namespace`
	* `metadata.uid`
	* `metadata.annotations['<KEY>']`
	* `metadata.labels['<KEY>']`
* The following information is available through environment variables but not as a `downwardAPI` volume `fieldRef`:
	* `spec.serviceAccountName`: the name of the pod's [service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
	* `spec.nodeName`
	* `status.hostIP`: the primary IP address of the node to which the Pod is assigned
	* `status.hostIPs`: the IP addresses is a dual-stack version of `status.hostIP`, the first is always the same as `status.hostIP`. The field is available if you enable the `PodHostIPs` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).
	* `status.podIP`: the pod's primary IP address (usually, its IPv4 address)
	* `status.podIPs`: the IP addresses is a dual-stack version of `status.podIP`, the first is always the same as `status.podIP`
* The following information is available through a `downwardAPI` volume `fieldRef`, but not as environment variables:
	* `metadata.lebels`: all of the pod's labels, formatted as `label-key="escaped-label-value"` with one label per line
	* `metadata.annotations`: all of the pod's annotations, formatted as `annotation-key="escaped-annotation-value"` with one annotation per line

#### Information available via `resourceFieldRef`
* These container-level fields allow you to provide information about [requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) for resources such as CPU and memory.
	* `resource: limits.cpu`
	* `resource: requests.cpu`
	* `resource: limits.memory`
	* `resource: requests.memory`
	* `resource: limits.hugepages-*`
	* `resource: requests.hugepages-*`
	* `resource: limits.ephemeral-storage`
	* `resource: requests.ephemeral-storage`
* **Fallback information for resource limits**: If CPU and memory limits are not specified for a container, and you use the downward API to try to expose that information, then the kubelet defaults to exposing the maximum allocatable value for CPU and memory based on the [node allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) calculation.
