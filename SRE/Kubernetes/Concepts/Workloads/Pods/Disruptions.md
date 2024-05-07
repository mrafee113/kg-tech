> [source](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)

### Voluntary and involuntary disruptions
* Pods do not disappear until someone (a person or a controller) destroys them, or there is an unavoidable hardware or system software error.
* We call these unavoidable cases involuntary disruptions to an application. Examples are:
	* a hardware failure of the physical machine backing the node
	* cluster administrator deletes VM (instance) by mistake
	* cloud provider or hypervisor failure makes VM disappear
	* a kernel panic
	* the node disappears from the cluster due to cluster network partition
	* eviction of a pod due to the node being [out-of-resources](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/).
* We call other cases voluntary disruptions. These include both actions initiated by the application owner and those initiated by a Cluster Administrator.
* Typical application owner actions include:
	* deleting the deployment or other controller that manages the pod
	* updating a deployment's pod template causing a restart
	* directly deleting a pod (e.g. by accident)
* Cluster administrator actions include:
	* [Draining a node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) for repair or upgrade.
	* Draining a node from a cluster to scale the cluster down (learn about [Cluster Autoscaling](https://github.com/kubernetes/autoscaler/#readme)).
	* Removing a pod from a node to permit something else to fit on that node.
	* *These actions might be taken directly by the cluster administrator, or by automation run by the cluster administrator, or by your cluster hosting provider.*

> [!Caution]
> Not all voluntary disruptions are constrained by Pod Disruption Budgets. For example, deleting deployments or pods bypasses Pod Disruption Budgets.

### Dealing with disruptions
* Here are some ways to mitigate involuntary disruptions:
	* Ensure your pod [requests the resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource) it needs.
	* Replicate your application if you need higher availability. (Learn about running replicated [stateless](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/) and [stateful](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/) applications.)
	* For even higher availability when running replicated applications, spread applications across racks (using [anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)) or across zones (if using a [multi-zone cluster](https://kubernetes.io/docs/setup/multiple-zones).)
* The frequency of voluntary disruptions varies. On a basic Kubernetes cluster, there are no automated voluntary disruptions (only user-triggered ones). However, your cluster administrator or hosting provider may run some additional services which cause voluntary disruptions. For example, rolling out node software updates can cause voluntary disruptions. Also, some implementations of cluster (node) autoscaling may cause voluntary disruptions to defragment and compact nodes. Your cluster administrator or hosting provider should have documented what level of voluntary disruptions, if any, to expect. Certain configuration options, such as [using PriorityClasses](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) in your pod spec can also cause voluntary (and involuntary) disruptions.

### Pod disruption budgets
* Kubernetes offers features to help you run highly available applications even when you introduce frequent voluntary disruptions.
* As an application owner, you can create a PodDisruptionBudget (PDB) for each application. A PDB limits the number of Pods of a replicated application that are down simultaneously from voluntary disruptions. For example, a quorum-based application would like to ensure that the number of replicas running is never brought below the number needed for a quorum. A web front end might want to ensure that the number of replicas serving load never falls below a certain percentage of the total.
* Cluster managers and hosting providers should use tools which respect PodDisruptionBudgets by calling the Eviction API instead of directly deleting pods or deployments.
* For example, the `kubectl drain` subcommand lets you mark a node as going out of service. When you run `kubectl drain`, the tool tries to evict all of the Pods on the Node you're taking out of service. The eviction request that kubectl submits on your behalf may be temporarily rejected, so the tool periodically retries all failed requests until all Pods on the target node are terminated, or until a configurable timeout is reached.
* A PDB specifies the number of replicas that an application can tolerate having, relative to how many it is intended to have. For example, a Deployment which has a `.spec.replicas: 5` is supposed to have 5 pods at any given time. If its PDB allows for there to be 4 at a time, then the Eviction API will allow voluntary disruption of one (but not two) pods at a time.
* The "intended" number of pods is computed from the `.spec.replicas` of the workload resource that is managing those pods. The control plane discovers the owning workload resource by examining the `.metadata.ownerReferences` of the Pod.
* [Involuntary disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#voluntary-and-involuntary-disruptions) cannot be prevented by PDBs; however they do count against the budget.
* Pods which are deleted or unavailable due to a rolling upgrade to an application do count against the disruption budget, but workload resources (such as Deployment and StatefulSet) are not limited by PDBs when doing rolling upgrades. Instead, the handling of failures during application updates is configured in the spec for the specific workload resource.
* It is recommended to set `AlwaysAllow` [Unhealthy Pod Eviction Policy](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#unhealthy-pod-eviction-policy) to your PodDisruptionBudgets to support eviction of misbehaving applications during a node drain. The default behavior is to wait for the application pods to become [healthy](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#healthiness-of-a-pod) before the drain can proceed.
* When a pod is evicted using the eviction API, it is gracefully [terminated](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination), honoring the `terminationGracePeriodSeconds` setting in its [PodSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#podspec-v1-core).

### How to perform disruptive actions on your cluster
* If you are a Cluster Administrator, and you need to perform a disruptive action on all the nodes in your cluster, such as a node or system software upgrade, here are some options:
	* Accept downtime during the upgrade.
	* Failover to another complete replica cluster.
		* No downtime, but may be costly both for the duplicated nodes and for human effort to orchestrate the switchover.
	* Write disruption tolerant applications and use PDBs.
		* No downtime.
		* Minimal resource duplication.
		* Allows more automation of cluster administration.
		* Writing disruption-tolerant applications is tricky, but the work to tolerate voluntary disruptions largely overlaps with work to support autoscaling and tolerating involuntary disruptions.
