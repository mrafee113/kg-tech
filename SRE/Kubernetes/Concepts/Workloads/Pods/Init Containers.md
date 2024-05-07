> [source](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

* Init containers are specialized containers that run before app containers in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/). Init containers can contain utilities or setup scripts not present in an app image.
* You can specify init containers in the Pod specification alongside the containers array (which describes app containers).

### Understanding init containers
* A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) can have multiple containers running apps within it, but it can also have one or more init containers, which are run before the app containers are started.
* Init containers are exactly like regular containers, except:
	* Init containers always run to completion.
	* Each init container must complete successfully before the next one starts.
* If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds. However, if the Pod has a `restartPolicy` of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.
* To specify an init container for a Pod, add the `initContainers` field into the [Pod specification](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec), as an array of container items (similar to the app containers field and its contents). See [Container](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) in the API reference for more details.
* The status of the init containers is returned in `.status.initContainerStatuses` field as an array of the container statuses (similar to the `.status.containerStatuses` field).

#### Differences from regular containers
* Init containers support all the fields and features of app containers, including resource limits, [volumes](https://kubernetes.io/docs/concepts/storage/volumes/), and security settings. However, the resource requests and limits for an init container are handled differently, as documented in [Resource sharing within containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#resource-sharing-within-containers).
* Also, init containers do not support lifecycle, `livenessProbe`, `readinessProbe`, or `startupProbe` because they must run to completion before the Pod can be ready.
* If you specify multiple init containers for a Pod, kubelet runs each init container sequentially. Each init container must succeed before the next can run. When all of the init containers have run to completion, kubelet initializes the application containers for the Pod and runs them as usual.

### Using init containers
* Because init containers have separate images from app containers, they have some advantages for start-up related code:
	* Init containers can contain utilities or custom code for setup that are not present in an app image. For example, there is no need to make an image `FROM` another image just to use a tool like `sed`, `awk`, `python`, or `dig` during setup.
	* The application image builder and deployer roles can work independently without the need to jointly build a single app image.
	* Init containers can run with a different view of the filesystem than app containers in the same Pod. Consequently, they can be given access to [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that app containers cannot access.
	* Because init containers run to completion before any app containers start, init containers offer a mechanism to block or delay app container startup until a set of preconditions are met. Once preconditions are met, all of the app containers in a Pod can start in parallel.
	* Init containers can securely run utilities or custom code that would otherwise make an app container image less secure. By keeping unnecessary tools separate you can limit the attack surface of your app container image.

### Detailed behavior
* During Pod startup, the kubelet delays running init containers until the networking and storage are ready. Then the kubelet runs the Pod's init containers in the order they appear in the Pod's spec.
* Each init container must exit successfully before the next container starts. If a container fails to start due to the runtime or exits with failure, it is retried according to the Pod `restartPolicy`. However, if the Pod `restartPolicy` is set to Always, the init containers use `restartPolicy` OnFailure.
* A Pod cannot be `Ready` until all init containers have succeeded. The ports on an init container are not aggregated under a Service. A Pod that is initializing is in the `Pending` state but should have a condition `Initialized` set to false.
* If the Pod [restarts](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#pod-restart-reasons), or is restarted, all init containers must execute again.
* Changes to the init container spec are limited to the container image field. Altering an init container image field is equivalent to restarting the Pod.
* Because init containers can be restarted, retried, or re-executed, init container code should be idempotent. In particular, code that writes to files on `EmptyDirs` should be prepared for the possibility that an output file already exists.
* Init containers have all of the fields of an app container. However, Kubernetes prohibits `readinessProbe` from being used because init containers cannot define readiness distinct from completion. This is enforced during validation.
