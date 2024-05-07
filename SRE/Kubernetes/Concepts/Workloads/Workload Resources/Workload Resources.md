> [source](https://kubernetes.io/docs/concepts/workloads/controllers/)

* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/Deployments|Deployments]]
* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/ReplicaSet|ReplicaSet]]
* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/StatefulSet|StatefulSet]]
* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/Jobs|Jobs]]
* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/Automatic Cleanup for Finished Jobs|Automatic Cleanup for Finished Jobs]]
* [[SRE/Kubernetes/Concepts/Workloads/Workload Resources/CronJob|CronJob]]

---
* Kubernetes provides several built-in APIs for declarative management of your [workloads](https://kubernetes.io/docs/concepts/workloads/) and the components of those workloads.
* Ultimately, your applications run as containers inside [Pods](https://kubernetes.io/docs/concepts/workloads/pods/); however, managing individual Pods would be a lot of effort. For example, if a Pod fails, you probably want to run a new Pod to replace it. Kubernetes can do that for you.
* You use the Kubernetes API to create a workload [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) that represents a higher abstraction level than a Pod, and then the Kubernetes [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) automatically manages Pod objects on your behalf, based on the specification for the workload object you defined.