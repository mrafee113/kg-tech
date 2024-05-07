> [source](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarantee the availability of a specified number of identical Pods.

### How a ReplicaSet works
* A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods it should create to meet the number of replicas criteria. A ReplicaSet then fulfills its purpose by creating and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod template.
* A ReplicaSet is linked to its Pods via the Pods' [`metadata.ownerReferences`](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#owners-dependents) field, which specifies what resource the current object is owned by. All Pods acquired by a ReplicaSet have their owning ReplicaSet's identifying information within their `ownerReferences` field. It's through this link that the ReplicaSet knows of the state of the Pods it is maintaining and plans accordingly.

### When to use a ReplicaSet
* A ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless you require custom update orchestration or don't require updates at all.
* This actually means that you may never need to manipulate ReplicaSet objects: use a Deployment instead, and define your application in the spec section.

### Non-template Pod acquisitions
* While you can create bare Pods with no problems, it is strongly recommended to make sure that the bare Pods do not have labels which match the selector of one of your ReplicaSets. The reason for this is because a ReplicaSet is not limited to owning Pods specified by its template-- it can acquire other Pods in the manner specified in the previous sections.
* In this manner, a ReplicaSet can own a non-homogenous set of Pods

### Writing a ReplicaSet manifest
* As with all other Kubernetes API objects, a ReplicaSet needs the `apiVersion`, `kind`, and `metadata` fields.
* A ReplicaSet also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).
	* **`.spec.template`**: The `.spec.template` is a pod template which is also required to have labels in place. Be careful not to overlap with the selectors of other controllers, lest they try to adopt this Pod. For the template's [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) field, `.spec.template.spec.restartPolicy`, the only allowed value is `Always`, which is the default.
	* **`.spec.selector`**: In the ReplicaSet, `.spec.template.metadata.labels` must match `.spec.selector`, or it will be rejected by the API.
		* **Note**: For 2 ReplicaSets specifying the same `.spec.selector` but different `.spec.template.metadata.labels` and `.spec.template.spec` fields, each ReplicaSet ignores the Pods created by the other ReplicaSet.
	* **`.spec.replicas`**: You can specify how many Pods should run concurrently by setting `.spec.replicas`. The ReplicaSet will create/delete its Pods to match this number. Default is 1.

### Working with ReplicaSets
* **Deleting a ReplicaSet and its Pods**
	* To delete a ReplicaSet and all of its Pods, use [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete). The [Garbage collector](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) automatically deletes all of the dependent Pods by default.
* **Deleting just a ReplicaSet**
	* You can delete a ReplicaSet without affecting any of its Pods using [`kubectl delete`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete) with the `--cascade=orphan` option. 
	* Once the original is deleted, you can create a new ReplicaSet to replace it. As long as the old and new `.spec.selector` are the same, then the new one will adopt the old Pods. However, it will not make any effort to make existing Pods match a new, different pod template. To update Pods to a new spec in a controlled way, use a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment), as ReplicaSets do not support a rolling update directly.
* **Isolating Pods from a ReplicaSet**
	* You can remove Pods from a ReplicaSet by changing their labels. This technique may be used to remove Pods from service for debugging, data recovery, etc. Pods that are removed in this way will be replaced automatically ( assuming that the number of replicas is not also changed).
* **Scaling a ReplicaSet**
	* A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas` field. The ReplicaSet controller ensures that a desired number of Pods with a matching label selector are available and operational.
	* When scaling down, the ReplicaSet controller chooses which pods to delete by sorting the available pods to prioritize scaling down pods based on the following general algorithm:
		1. Pending (and unschedulable) pods are scaled down first
		2. If `controller.kubernetes.io/pod-deletion-cost` annotation is set, then the pod with the lower value will come first.
		3. Pods on nodes with more replicas come before pods on nodes with fewer replicas.
		4. If the pods' creation times differ, the pod that was created more recently comes before the older pod (the creation times are bucketed on an integer log scale when the `LogarithmicScaleDown` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled)
	* If all of the above match, then selection is random.

### Alternatives to ReplicaSets
* **Deployment**: [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) is an object which can own ReplicaSets and update them and their Pods via declarative, server-side rolling updates. While ReplicaSets can be used independently, today they're mainly used by Deployments as a mechanism to orchestrate Pod creation, deletion and updates. When you use Deployments you don't have to worry about managing the ReplicaSets that they create. Deployments own and manage their ReplicaSets. As such, it is recommended to use Deployments when you want ReplicaSets.
* **Bare Pods**: Unlike the case where a user directly created Pods, a ReplicaSet replaces Pods that are deleted or terminated for any reason, such as in the case of node failure or disruptive node maintenance, such as a kernel upgrade. For this reason, we recommend that you use a ReplicaSet even if your application requires only a single Pod. Think of it similarly to a process supervisor, only it supervises multiple Pods across multiple nodes instead of individual processes on a single node. A ReplicaSet delegates local container restarts to some agent on the node such as Kubelet.
* **Job**: Use a [`Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/) instead of a ReplicaSet for Pods that are expected to terminate on their own (that is, batch jobs).
* **DaemonSet**: Use a [`DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) instead of a ReplicaSet for Pods that provide a machine-level function, such as machine monitoring or machine logging. These Pods have a lifetime that is tied to a machine lifetime: the Pod needs to be running on the machine before other Pods start, and are safe to terminate when the machine is otherwise ready to be rebooted/shutdown.
