> [source](https://kubernetes.io/docs/concepts/configuration/overview/)

* This is a living document. If you think of something that is not on this list but might be useful to others, please don't hesitate to file an issue or submit a PR.

### General Configuration Tips
* When defining configurations, specify the latest stable API version.
* Configuration files should be stored in version control before being pushed to the cluster. This allows you to quickly roll back a configuration change if necessary. It also aids cluster re-creation and restoration.
* Write your configuration files using YAML rather than JSON. Though these formats can be used interchangeably in almost all scenarios, YAML tends to be more user-friendly.
* Group related objects into a single file whenever it makes sense. One file is often easier to manage than several. See the [guestbook-all-in-one.yaml](https://github.com/kubernetes/examples/tree/master/guestbook/all-in-one/guestbook-all-in-one.yaml) file as an example of this syntax.
* Note also that many `kubectl` commands can be called on a directory. For example, you can call `kubectl apply` on a directory of config files.
* Don't specify default values unnecessarily: simple, minimal configuration will make errors less likely.
* Put object descriptions in annotations, to allow better introspection.

> [!Note]
> There is a breaking change introduced in the [YAML 1.2](https://yaml.org/spec/1.2.0/#id2602744) boolean values specification with respect to [YAML 1.1](https://yaml.org/spec/1.1/#id864510). This is a known [issue](https://github.com/kubernetes/kubernetes/issues/34146) in Kubernetes. YAML 1.2 only recognizes **true** and **false** as valid booleans, while YAML 1.1 also accepts **yes**, **no**, **on**, and **off** as booleans. However, Kubernetes uses YAML parsers that are mostly compatible with YAML 1.1, which means that using **yes** or **no** instead of **true** or **false** in a YAML manifest may cause unexpected errors or behaviors. To avoid this issue, it is recommended to always use true or false for boolean values in YAML manifests, and to quote any strings that may be confused with booleans, such as "**yes**" or "**no**".
>
> Besides booleans, there are additional specifications changes between YAML versions. Please refer to the [YAML Specification Changes](https://spec.yaml.io/main/spec/1.2.2/ext/changes) documentation for a comprehensive list.

### "Naked" Pods versus ReplicaSets, Deployments, and Jobs
* Don't use naked Pods (that is, Pods not bound to a [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) or [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)) if you can avoid it. Naked Pods will not be rescheduled in the event of a node failure.
* A Deployment, which both creates a ReplicaSet to ensure that the desired number of Pods is always available, and specifies a strategy to replace Pods (such as [RollingUpdate](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-update-deployment)), is almost always preferable to creating Pods directly, except for some explicit [`restartPolicy: Never`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) scenarios. A [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) may also be appropriate.

### Services
* Create a [Service](https://kubernetes.io/docs/concepts/services-networking/service/) before its corresponding backend workloads (Deployments or ReplicaSets), and before any workloads that need to access it. When Kubernetes starts a container, it provides environment variables pointing to all the Services which were running when the container was started. For example, if a Service named `foo` exists, all containers will get the following variables in their initial environment:
	```bash
	FOO_SERVICE_HOST=<the host the Service is running on>
	FOO_SERVICE_PORT=<the port the Service is running on>
	```
	* *This does imply an ordering requirement* - any `Service` that a `Pod` wants to access must be created before the `Pod` itself, or else the environment variables will not be populated. DNS does not have this restriction.
* Don't specify a `hostPort` for a Pod unless it is absolutely necessary. When you bind a Pod to a `hostPort`, it limits the number of places the Pod can be scheduled, because each <`hostIP`, `hostPort`, `protocol`> combination must be unique. If you don't specify the `hostIP` and `protocol` explicitly, Kubernetes will use `0.0.0.0` as the default `hostIP` and `TCP` as the default protocol.
	* If you only need access to the port for debugging purposes, you can use the [apiserver proxy](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#manually-constructing-apiserver-proxy-urls) or [`kubectl port-forward`](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/).
	* If you explicitly need to expose a Pod's port on the node, consider using a [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) Service before resorting to `hostPort`.
* Avoid using `hostNetwork`, for the same reasons as `hostPort`.
* Use [headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) (which have a `ClusterIP` of `None`) for service discovery when you don't need `kube-proxy` load balancing.