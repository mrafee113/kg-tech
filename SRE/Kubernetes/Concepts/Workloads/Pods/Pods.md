> [source](https://kubernetes.io/docs/concepts/workloads/pods/)

* [[SRE/Kubernetes/Concepts/Workloads/Pods/Pod Lifecycle|Pod Lifecycle]]
* [[SRE/Kubernetes/Concepts/Workloads/Pods/Init Containers|Init Containers]]
* [[SRE/Kubernetes/Concepts/Workloads/Pods/Disruptions|Disruptions]]
* [[SRE/Kubernetes/Concepts/Workloads/Pods/Ephemeral Containers|Ephemeral Containers]]
* [[SRE/Kubernetes/Concepts/Workloads/Pods/Pod QoS Classes|Pod Quality of Service Classes]]
* [[SRE/Kubernetes/Concepts/Workloads/Pods/Downward API|Downward API]]

---
* *Pods* are the smallest deployable units of computing that you can create and manage in Kubernetes.
* A Pod (as in a pod of whales or pea pod) is a group of one or more [containers](), with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled. In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.
* As well as application containers, a Pod can contain [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) that run during Pod startup. You can also inject [ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) for debugging if your cluster offers this.

### What is a Pod?
* The shared context of a Pod is a set of Linux namespaces, cgroups, and potentially other facets of isolation - the same things that isolate a [container](https://kubernetes.io/docs/concepts/containers/). Within a Pod's context, the individual applications may have further sub-isolations applied.
* A Pod is similar to a set of containers with shared namespaces and shared filesystem volumes.

#### Workload resources for managing pods
* Pods in a Kubernetes cluster are used in two main ways:
	* **Pods that run a single container**. The "one-container-per-Pod" model is the most common Kubernetes use case; in this case, you can think of a Pod as a wrapper around a single container; Kubernetes manages Pods rather than managing the containers directly.
	* **Pods that run multiple containers that need to work together**. A Pod can encapsulate an application composed of multiple co-located containers that are tightly coupled and need to share resources. These co-located containers form a single cohesive unit of service—for example, one container serving data stored in a shared volume to the public, while a separate sidecar container refreshes or updates those files. The Pod wraps these containers, storage resources, and an ephemeral network identity together as a single unit.

> [!Note]
> Grouping multiple co-located and co-managed containers in a single Pod is a relatively advanced use case. You should use this pattern only in specific instances in which your containers are tightly coupled.

* Each Pod is meant to run a single instance of a given application. If you want to scale your application horizontally, you should use multiple Pods, one for each instance. In Kubernetes, this is typically referred to as replication. Replicated Pods are usually created and managed as a group by a workload resource and its [controller](https://kubernetes.io/docs/concepts/architecture/controller/).

#### How pods manage multiple containers
* Pods are designed to support multiple cooperating processes (as containers) that form a cohesive unit of service. The containers in a Pod are automatically co-located and co-scheduled on the same physical or virtual machine in the cluster. The containers can share resources and dependencies, communicate with one another, and coordinate when and how they are terminated.
* Some Pods have [init containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-init-container) as well as [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container). By default, init containers run and complete before the app containers are started.
* Pods natively provide two kinds of shared resources for their constituent containers: [networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking) and [storage](https://kubernetes.io/docs/concepts/workloads/pods/#pod-storage).

### Working with pods
* You'll rarely create individual Pods directly in Kubernetes—even singleton Pods. This is because Pods are designed as relatively ephemeral, disposable entities. When a Pod gets created (directly by you, or indirectly by a [controller](https://kubernetes.io/docs/concepts/architecture/controller/)), the new Pod is scheduled to run on a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/) in your cluster. The Pod remains on that node until the Pod finishes execution, the Pod object is deleted, the Pod is evicted for lack of resources, or the node fails.

> [!Note]
> Restarting a container in a Pod should not be confused with restarting a Pod. A Pod is not a process, but an environment for running container(s). A Pod persists until it is deleted.

#### Pod templates
* Controllers for [workload](https://kubernetes.io/docs/concepts/workloads/) resources create Pods from a pod template and manage those Pods on your behalf.
* PodTemplates are specifications for creating Pods, and are included in workload resources.
* Each controller for a workload resource uses the `PodTemplate` inside the workload object to make actual Pods. The `PodTemplate` is part of the desired state of whatever workload resource you used to run your app.
* Modifying the pod template or switching to a new pod template has no direct effect on the Pods that already exist. If you change the pod template for a workload resource, that resource needs to create replacement Pods that use the updated template.
* On Nodes, the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) does not directly observe or manage any of the details around pod templates and updates; those details are abstracted away. That abstraction and separation of concerns simplifies system semantics, and makes it feasible to extend the cluster's behavior without changing existing code.

### Pod update and replacement
* As mentioned in the previous section, when the Pod template for a workload resource is changed, the controller creates new Pods based on the updated template instead of updating or patching the existing Pods.
* Kubernetes doesn't prevent you from managing Pods directly. It is possible to update some fields of a running Pod, in place. However, Pod update operations like [`patch`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#patch-pod-v1-core), and [`replace`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#replace-pod-v1-core) have some limitations:
	* Most of the metadata about a Pod is immutable. For example, you cannot change the `namespace`, `name`, `uid`, or `creationTimestamp` fields; the `generation` field is unique. It only accepts updates that increment the field's current value.
	* If the `metadata.deletionTimestamp` is set, no new entry can be added to the `metadata.finalizers` list.
	* Pod updates may not change fields other than `spec.containers[*].image`, `spec.initContainers[*].image`, `spec.activeDeadlineSeconds` or `spec.tolerations`. For `spec.tolerations`, you can only add new entries.
	* When updating the `spec.activeDeadlineSeconds` field, two types of updates are allowed:
		1. setting the unassigned field to a positive number;
		2. updating the field from a positive number to a smaller, non-negative number.

### Resource sharing and communication
#### Storage in pods
A Pod can specify a set of shared storage [volumes](https://kubernetes.io/docs/concepts/storage/volumes/). All containers in the Pod can access the shared volumes, allowing those containers to share data. Volumes also allow persistent data in a Pod to survive in case one of the containers within needs to be restarted. See [Storage](https://kubernetes.io/docs/concepts/storage/) for more information on how Kubernetes implements shared storage and makes it available to Pods.

#### Pod networking
Each Pod is assigned a unique IP address for each address family. Every container in a Pod shares the network namespace, including the IP address and network ports. Inside a Pod (and only then), the containers that belong to the Pod can communicate with one another using `localhost`. When containers in a Pod communicate with entities outside the Pod, they must coordinate how they use the shared network resources (such as ports). Within a Pod, containers share an IP address and port space, and can find each other via `localhost`. The containers in a Pod can also communicate with each other using standard inter-process communications like SystemV semaphores or POSIX shared memory. Containers in different Pods have distinct IP addresses and can not communicate by OS-level IPC without special configuration. Containers that want to interact with a container running in a different Pod can use IP networking to communicate. There's more about this in the [networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/) section.

### Static pods
* Static Pods are managed directly by the kubelet daemon on a specific node, without the [API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) observing them. Whereas most Pods are managed by the control plane, for static Pods, the kubelet directly supervises each static Pod (and restarts it if it fails).
* Static Pods are always bound to one [Kubelet](https://kubernetes.io/docs/reference/generated/kubelet) on a specific node. The main use for static Pods is to run a self-hosted control plane: in other words, using the kubelet to supervise the individual [control plane components](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components).
* The kubelet automatically tries to create a [mirror Pod](https://kubernetes.io/docs/reference/glossary/?all=true#term-mirror-pod) on the Kubernetes API server for each static Pod. This means that the Pods running on a node are visible on the API server, but cannot be controlled from there. See the guide [Create static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod) for more information.

> [!Note]
> The spec of a static Pod cannot refer to other API objects (e.g., ServiceAccount, ConfigMap, Secret, etc).
