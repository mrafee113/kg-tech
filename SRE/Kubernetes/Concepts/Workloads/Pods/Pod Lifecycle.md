> [source](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

* Pods follow a defined lifecycle, starting in the `Pending` [[SRE/Kubernetes/Concepts/Workloads/Pods/Pod Lifecycle#Pod phase|phase]], moving through `Running` if at least one of its primary containers starts OK, and then through either the `Succeeded` or `Failed` phases depending on whether any container in the Pod terminated in failure.
* Whilst a Pod is running, the kubelet is able to restart containers to handle some kind of faults. Within a Pod, Kubernetes tracks different container [states](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states) and determines what action to take to make the Pod healthy again.
* In the Kubernetes API, Pods have both a specification and an actual status. The status for a Pod object consists of a set of [Pod conditions](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions). You can also inject [custom readiness information](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate) into the condition data for a Pod, if that is useful to your application.
* Pods are only [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/) once in their lifetime. Once a Pod is scheduled (assigned) to a Node, the Pod runs on that Node until it stops or is [terminated](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

### Pod lifetime
* Like individual application containers, Pods are considered to be relatively ephemeral (rather than durable) entities. Pods are created, assigned a unique ID ([UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids)), and scheduled to nodes where they remain until termination (according to restart policy) or deletion. If a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/) dies, the Pods scheduled to that node are [scheduled for deletion](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) after a timeout period.
* Pods do not, by themselves, self-heal. If a Pod is scheduled to a [node](https://kubernetes.io/docs/concepts/architecture/nodes/) that then fails, the Pod is deleted; likewise, a Pod won't survive an eviction due to a lack of resources or Node maintenance. Kubernetes uses a higher-level abstraction, called a [controller](https://kubernetes.io/docs/concepts/architecture/controller/), that handles the work of managing the relatively disposable Pod instances.
* A given Pod (as defined by a UID) is never "rescheduled" to a different node; instead, that Pod can be replaced by a new, near-identical Pod, with even the same name if desired, but with a different UID.
* When something is said to have the same lifetime as a Pod, such as a [volume](https://kubernetes.io/docs/concepts/storage/volumes/), that means that the thing exists as long as that specific Pod (with that exact UID) exists. If that Pod is deleted for any reason, and even if an identical replacement is created, the related thing (a volume, in this example) is also destroyed and created anew.

### Pod phase
* A Pod's status field is a [PodStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podstatus-v1-core) object, which has a phase field.
* The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The phase is not intended to be a comprehensive rollup of observations of container or Pod state, nor is it intended to be a comprehensive state machine.
* The number and meanings of Pod phase values are tightly guarded. Other than what is documented here, nothing should be assumed about Pods that have a given `phase` value.

|Value|Description|
|---|---|
|`Pending`|The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.|
|`Running`|The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting.|
|`Succeeded`|All containers in the Pod have terminated in success, and will not be restarted.|
|`Failed`|All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system.|
|`Unknown`|For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.|

> [!Note]
> When a Pod is being deleted, it is shown as `Terminating` by some kubectl commands. This `Terminating` status is not one of the Pod phases. A Pod is granted a term to terminate gracefully, which defaults to 30 seconds.

* The kubelet transitions deleted Pods, except for [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) and [force-deleted Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced) without a finalizer, to a terminal phase (`Failed` or `Succeeded` depending on the exit statuses of the pod containers) before their deletion from the API server.
* If a node dies or is disconnected from the rest of the cluster, Kubernetes applies a policy for setting the `phase` of all Pods on the lost node to Failed.

### Container states
* As well as the [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) of the Pod overall, Kubernetes tracks the state of each container inside a Pod. You can use [container lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) to trigger events to run at certain points in a container's lifecycle.
* Once the [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) assigns a Pod to a Node, the kubelet starts creating containers for that Pod using a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes). There are three possible container states: `Waiting`, `Running`, and `Terminated`.
* Each state has a specific meaning:
	* `Waiting`: If a container is not in either the `Running` or `Terminated` state, it is `Waiting`. A container in the `Waiting` state is still running the operations it requires in order to complete start up: for example, pulling the container image from a container image registry, or applying [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) data. When you use `kubectl` to query a Pod with a container that is `Waiting`, you also see a Reason field to summarize why the container is in that state.
	* `Running`: The `Running` status indicates that a container is executing without issues. If there was a `postStart` hook configured, it has already executed and finished. When you use `kubectl` to query a Pod with a container that is `Running`, you also see information about when the container entered the `Running` state.
	* `Terminated`: A container in the `Terminated` state began execution and then either ran to completion or failed for some reason. When you use `kubectl` to query a Pod with a container that is Terminated, you see a reason, an exit code, and the start and finish time for that container's period of execution.
* If a container has a `preStop` hook configured, this hook runs before the container enters the Terminated state.

### Container restart policy
* The `spec` of a Pod has a `restartPolicy` field with possible values `Always`, `OnFailure`, and `Never`. The default value is `Always`.
* The `restartPolicy` applies to all containers in the Pod. `restartPolicy` only refers to restarts of the containers by the kubelet on the same node. After containers in a Pod exit, the kubelet restarts them with an exponential back-off delay (10s, 20s, 40s, …), that is capped at five minutes. Once a container has executed for 10 minutes without any problems, the kubelet resets the restart backoff timer for that container.

### Pod conditions
* A Pod has a PodStatus, which has an array of [PodConditions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podcondition-v1-core) through which the Pod has or has not passed. Kubelet manages the following PodConditions:
	* `PodScheduled`: the Pod has been scheduled to a node.
	* `PodReadyToStartContainers`: (alpha feature; must be [enabled explicitly](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network)) the Pod sandbox has been successfully created and networking configured.
	* `ContainersReady`: all containers in the Pod are ready.
	* `Initialized`: all init containers have completed successfully.
	* `Ready`: the Pod is able to serve requests and should be added to the load balancing pools of all matching Services.

|Field name|Description|
|---|---|
|`type`|Name of this Pod condition.|
|`status`|Indicates whether that condition is applicable, with possible values "`True`", "`False`", or "`Unknown`".|
|`lastProbeTime`|Timestamp of when the Pod condition was last probed.|
|`lastTransitionTime`|Timestamp for when the Pod last transitioned from one status to another.|
|`reason`|Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition.|
|`message`|Human-readable message indicating details about the last status transition.|

### Container probes
A *probe* is a diagnostic performed periodically by the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) on a container. To perform a diagnostic, the kubelet either executes code within the container, or makes a network request.

#### Check mechanisms
* There are four different ways to check a container using a probe. Each probe must define exactly one of these four mechanisms:
	* `exec`: Executes a specified command inside the container. The diagnostic is considered successful if the command exits with a status code of 0.
	* `grpc`: Performs a remote procedure call using [gRPC](https://grpc.io/). The target should implement [gRPC health checks](https://grpc.io/grpc/core/md_doc_health-checking.html). The diagnostic is considered successful if the status of the response is `SERVING`.
	* `httpGet`: Performs an HTTP `GET` request against the Pod's IP address on a specified port and path. The diagnostic is considered successful if the response has a status code greater than or equal to 200 and less than 400.
	* `tcpSocket`: Performs a TCP check against the Pod's IP address on a specified port. The diagnostic is considered successful if the port is open. If the remote system (the container) closes the connection immediately after it opens, this counts as healthy.

> [!Caution]
> Unlike the other mechanisms, `exec` probe's implementation involves the creation/forking of multiple processes each time when executed. As a result, in case of the clusters having higher pod densities, lower intervals of `initialDelaySeconds`, `periodSeconds`, configuring any probe with exec mechanism might introduce an overhead on the cpu usage of the node. In such scenarios, consider using the alternative probe mechanisms to avoid the overhead.

#### Probe outcome
* Each probe has one of three results:
	* `Success`: The container passed the diagnostic.
	* `Failure`: The container failed the diagnostic.
	* `Unknown`: The diagnostic failed (no action should be taken, and the kubelet will make further checks).

#### Types of probe
* The kubelet can optionally perform and react to three kinds of probes on running containers:
	* `livenessProbe`: Indicates whether the container is running. If the liveness probe fails, the kubelet kills the container, and the container is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). If a container does not provide a liveness probe, the default state is `Success`.
		* [**When should you use a liveness probe?**](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-liveness-probe)
	* `readinessProbe`: Indicates whether the container is ready to respond to requests. If the readiness probe fails, the endpoints controller removes the Pod's IP address from the endpoints of all Services that match the Pod. The default state of readiness before the initial delay is `Failure`. If a container does not provide a readiness probe, the default state is `Success`.
		* [**When should you use a readiness probe?**](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-readiness-probe)
	* `startupProbe`: Indicates whether the application within the container is started. All other probes are disabled if a startup probe is provided, until it succeeds. If the startup probe fails, the kubelet kills the container, and the container is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy). If a container does not provide a startup probe, the default state is `Success`.
		* [**When should you use a startup probe?**](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#when-should-you-use-a-startup-probe)
* For more information about how to set up a liveness, readiness, or startup probe, see [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

### Termination of pods
* Because Pods represent processes running on nodes in the cluster, it is important to allow those processes to gracefully terminate when they are no longer needed (rather than being abruptly stopped with a KILL signal and having no chance to clean up).
* The design aim is for you to be able to request deletion and know when processes terminate, but also be able to ensure that deletes eventually complete. When you request deletion of a Pod, the cluster records and tracks the intended grace period before the Pod is allowed to be forcefully killed. With that forceful shutdown tracking in place, the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) attempts graceful shutdown.
* Typically, with this graceful termination of the pod, kubelet makes requests to the container runtime to attempt to stop the containers in the pod by first sending a TERM (aka. SIGTERM) signal, with a grace period timeout, to the main process in each container. The requests to stop the containers are processed by the container runtime asynchronously. There is no guarantee to the order of processing for these requests. Many container runtimes respect the STOPSIGNAL value defined in the container image and, if different, send the container image configured STOPSIGNAL instead of TERM. Once the grace period has expired, the KILL signal is sent to any remaining processes, and the Pod is then deleted from the [API Server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver). If the kubelet or the container runtime's management service is restarted while waiting for processes to terminate, the cluster retries from the start including the full original grace period.

#### Forced pod termination
> [!Caution]
> Forced deletions can be potentially disruptive for some workloads and their Pods.

* By default, all deletes are graceful within 30 seconds. The kubectl delete command supports the `--grace-period=<seconds>` option which allows you to override the default and specify your own value.
* Setting the grace period to 0 forcibly and immediately deletes the Pod from the API server. If the Pod was still running on a node, that forcible deletion triggers the kubelet to begin immediate cleanup.

> [!Note]
> You must specify an additional flag `--force` along with `--grace-period=0` in order to perform force deletions.

* When a force deletion is performed, the API server does not wait for confirmation from the kubelet that the Pod has been terminated on the node it was running on. It removes the Pod in the API immediately so a new Pod can be created with the same name. On the node, Pods that are set to terminate immediately will still be given a small grace period before being force killed.

> [!Caution]
> Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.

* If you need to force-delete Pods that are part of a StatefulSet, refer to the task documentation for [deleting Pods from a StatefulSet](https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/).

### Garbage collection of pods
* For failed Pods, the API objects remain in the cluster's API until a human or [controller](https://kubernetes.io/docs/concepts/architecture/controller/) process explicitly removes them.
* The Pod garbage collector (PodGC), which is a controller in the control plane, cleans up terminated Pods (with a phase of `Succeeded` or `Failed`), when the number of Pods exceeds the configured threshold (determined by `terminated-pod-gc-threshold` in the kube-controller-manager). This avoids a resource leak as Pods are created and terminated over time.
* Additionally, PodGC cleans up any Pods which satisfy any of the following conditions:
	* are orphan Pods - bound to a node which no longer exists,
	* are unscheduled terminating Pods,
	* are terminating Pods, bound to a non-ready node tainted with `node.kubernetes.io/out-of-service`, when the `NodeOutOfServiceVolumeDetach` feature gate is enabled.
