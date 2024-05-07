> [source](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)

* Node-pressure eviction is the process by which the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) proactively terminates pods to reclaim resources on nodes.
* The [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) monitors resources like memory, disk space, and filesystem inodes on your cluster's nodes. When one or more of these resources reach specific consumption levels, the kubelet can proactively fail one or more pods on the node to reclaim resources and prevent starvation.
* During a node-pressure eviction, the kubelet sets the [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) for the selected pods to `Failed`, and terminates the Pod.
* Node-pressure eviction is not the same as [API-initiated eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/).
* The kubelet does not respect your configured [PodDisruptionBudget](https://kubernetes.io/docs/reference/glossary/?all=true#term-pod-disruption-budget) or the pod's `terminationGracePeriodSeconds`. If you use [soft eviction thresholds](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#soft-eviction-thresholds), the kubelet respects your configured `eviction-max-pod-grace-period`. If you use [hard eviction thresholds](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#hard-eviction-thresholds), the kubelet uses a `0s` grace period (immediate shutdown) for termination.