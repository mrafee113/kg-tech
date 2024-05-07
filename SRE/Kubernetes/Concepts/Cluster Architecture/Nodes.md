> [source](https://kubernetes.io/docs/concepts/architecture/nodes/)

* Kubernetes runs your [workload](https://kubernetes.io/docs/concepts/workloads/) by placing containers into Pods to run on Nodes. A node may be a virtual or physical machine, depending on the cluster. Each node is managed by the [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) and contains the services necessary to run [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).
* The [components](https://kubernetes.io/docs/concepts/overview/components/#node-components) on a node include the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet), a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes), and the [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/).

### Management
* There are two main ways to have Nodes added to the [API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver):
	1. The kubelet on a node self-registers to the control plane
	2. You (or another human user) manually add a Node object
* After you create a Node object, or the kubelet on a node self-registers, the control plane checks whether the new Node object is valid. Kubernetes creates a Node object internally (the representation). Kubernetes checks that a kubelet has registered to the API server that matches the metadata.name field of the Node. If the node is healthy (i.e. all necessary services are running), then it is eligible to run a Pod. Otherwise, that node is ignored for any cluster activity until it becomes healthy.

> [!Note]
> Kubernetes keeps the object for the invalid Node and continues checking to see whether it becomes healthy.
> You, or a [controller](https://kubernetes.io/docs/concepts/architecture/controller/), must explicitly delete the Node object to stop that health checking.

* The name of a Node object must be a valid [DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names#dns-subdomain-names).

### Node heartbeats
* Heartbeats, sent by Kubernetes nodes, help your cluster determine the availability of each node, and to take action when failures are detected.
* For nodes there are two forms of heartbeats:
	* Updates to the .status of a Node.
	* Lease objects within the kube-node-lease [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces). Each Node has an associated Lease object.

### Node controller
* The node [controller](https://kubernetes.io/docs/concepts/architecture/controller/) is a Kubernetes control plane component that manages various aspects of nodes.
* The node controller has multiple roles in a node's life. The first is assigning a CIDR block to the node when it is registered (if CIDR assignment is turned on).
* The second is keeping the node controller's internal list of nodes up to date with the cloud provider's list of available machines. When running in a cloud environment and whenever a node is unhealthy, the node controller asks the cloud provider if the VM for that node is still available. If not, the node controller deletes the node from its list of nodes.
* The third is monitoring the nodes' health. The node controller is responsible for:
	* In the case that a node becomes unreachable, updating the `Ready` condition in the Node's `.status` field. In this case the node controller sets the `Ready` condition to `Unknown`.
	* If a node remains unreachable: triggering [API-initiated eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/) for all of the Pods on the unreachable node. By default, the node controller waits 5 minutes between marking the node as Unknown and submitting the first eviction request.

#### Rate limits on eviction
* In most cases, the node controller limits the eviction rate to --node-eviction-rate (default 0.1) per second, meaning it won't evict pods from more than 1 node per 10 seconds.
* The node eviction behavior changes when a node in a given availability zone becomes unhealthy. The node controller checks what percentage of nodes in the zone are unhealthy (the `Ready` condition is `Unknown` or `False`) at the same time:
	* If the fraction of unhealthy nodes is at least `--unhealthy-zone-threshold` (default 0.55), then the eviction rate is reduced.
	* If the cluster is small (i.e. has less than or equal to` --large-cluster-size-threshold` nodes - default 50), then evictions are stopped.
	* Otherwise, the eviction rate is reduced to `--secondary-node-eviction-rate` (default 0.01) per second.
* The reason these policies are implemented per availability zone is because one availability zone might become partitioned from the control plane while the others remain connected. If your cluster does not span multiple cloud provider availability zones, then the eviction mechanism does not take per-zone unavailability into account.
* A key reason for spreading your nodes across availability zones is so that the workload can be shifted to healthy zones when one entire zone goes down. Therefore, if all nodes in a zone are unhealthy, then the node controller evicts at the normal rate of `--node-eviction-rate`. The corner case is when all zones are completely unhealthy (none of the nodes in the cluster are healthy). In such a case, the node controller assumes that there is some problem with connectivity between the control plane and the nodes, and doesn't perform any evictions. (If there has been an outage and some nodes reappear, the node controller does evict pods from the remaining nodes that are unhealthy or unreachable).
* The node controller is also responsible for evicting pods running on nodes with `NoExecute` taints, unless those pods tolerate that taint. The node controller also adds [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) corresponding to node problems like node unreachable or not ready. This means that the scheduler won't place Pods onto unhealthy nodes.

### Resource capacity tracking
* Node objects track information about the Node's resource capacity: for example, the amount of memory available and the number of CPUs. Nodes that [self register](https://kubernetes.io/docs/concepts/architecture/nodes/#self-registration-of-nodes) report their capacity during registration. If you [manually](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration) add a Node, then you need to set the node's capacity information when you add it.
* The Kubernetes [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/) ensures that there are enough resources for all the Pods on a Node. The scheduler checks that the sum of the requests of containers on the node is no greater than the node's capacity. That sum of requests includes all containers managed by the kubelet, but excludes any containers started directly by the container runtime, and also excludes any processes running outside of the kubelet's control.

> [!Note]
> If you want to explicitly reserve resources for non-Pod processes, see [reserve resources for system daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#system-reserved).

### Graceful node shutdown
* The kubelet attempts to detect node system shutdown and terminates pods running on the node.
* Kubelet ensures that pods follow the normal [pod termination process](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) during the node shutdown. During node shutdown, the kubelet does not accept new Pods (even if those Pods are already bound to the node).
* The Graceful node shutdown feature depends on systemd since it takes advantage of [systemd inhibitor locks](https://www.freedesktop.org/wiki/Software/systemd/inhibit/) to delay the node shutdown with a given duration.
* Graceful node shutdown is controlled with the `GracefulNodeShutdown` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).
* Note that by default, both configuration options described below, `shutdownGracePeriod` and `shutdownGracePeriodCriticalPods` are set to zero, thus not activating the graceful node shutdown functionality. To activate the feature, the two kubelet config settings should be configured appropriately and set to non-zero values.
* Once systemd detects or notifies node shutdown, the kubelet sets a `NotReady` condition on the Node, with the `reason` set to "node is shutting down". The kube-scheduler honors this condition and does not schedule any Pods onto the affected node; other third-party schedulers are expected to follow the same logic. This means that new Pods won't be scheduled onto that node and therefore none will start.
* The kubelet also rejects Pods during the `PodAdmission` phase if an ongoing node shutdown has been detected, so that even Pods with a [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for `node.kubernetes.io/not-ready:NoSchedule` do not start there.
* At the same time when kubelet is setting that condition on its Node via the API, the kubelet also begins terminating any Pods that are running locally.
* During a graceful shutdown, kubelet terminates pods in two phases:
	* Terminate regular pods running on the node.
	* Terminate [critical pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical) running on the node.
* Graceful node shutdown feature is configured with two [KubeletConfiguration](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/) options:
	* `shutdownGracePeriod`: Specifies the total duration that the node should delay the shutdown by. This is the total grace period for pod termination for both regular and critical pods.
	* `shutdownGracePeriodCriticalPods`: Specifies the duration used to terminate critical pods during a node shutdown. This value should be less than `shutdownGracePeriod`.

> [!Note]
> There are cases when Node termination was cancelled by the system (or perhaps manually by an administrator). In either of those situations the Node will return to the `Ready` state. However, Pods which already started the process of termination will not be restored by kubelet and will need to be re-scheduled.

### Non-graceful node shutdown handling
* A node shutdown action may not be detected by kubelet's Node Shutdown Manager, either because the command does not trigger the inhibitor locks mechanism used by kubelet or because of a user error.
* When a node is shutdown but not detected by kubelet's Node Shutdown Manager, the pods that are part of a StatefulSet will be stuck in terminating status on the shutdown node and cannot move to a new running node. This is because kubelet on the shutdown node is not available to delete the pods so the StatefulSet cannot create a new pod with the same name. If there are volumes used by the pods, the VolumeAttachments will not be deleted from the original shutdown node so the volumes used by these pods cannot be attached to a new running node. As a result, the application running on the StatefulSet cannot function properly. If the original shutdown node comes up, the pods will be deleted by kubelet and new pods will be created on a different running node. If the original shutdown node does not come up, these pods will be stuck in terminating status on the shutdown node forever.
	* To mitigate the above situation, a user can manually add the taint `node.kubernetes.io/out-of-service` with either `NoExecute` or `NoSchedule` effect to a Node marking it out-of-service. If the `NodeOutOfServiceVolumeDetach` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled on [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/), and a Node is marked out-of-service with this taint, the pods on the node will be forcefully deleted if there are no matching tolerations on it and volume detach operations for the pods terminating on the node will happen immediately. This allows the Pods on the out-of-service node to recover quickly on a different node.
* During a non-graceful shutdown, Pods are terminated in the two phases:
	* Force delete the Pods that do not have matching `out-of-service` tolerations.
	* Immediately perform detach volume operation for such pods.
