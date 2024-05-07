* [[SRE/Kubernetes/Concepts/Objects/Objects|Kubernetes Objects]]
* [[SRE/Kubernetes/Concepts/Components|Kubernetes Components]]
* [[SRE/Kubernetes/Concepts/API|Kubernetes API]]
* [[SRE/Kubernetes/Concepts/Cluster Architecture/Cluster Architecture|Cluster Architecture]]
* [[SRE/Kubernetes/Concepts/Containers/Containers|Containers]]
* [[SRE/Kubernetes/Concepts/Workloads/Workloads|Workloads]]
* [[SRE/Kubernetes/Concepts/Networking/Networking|Services, Load Balancing, and Networking]]
* [[SRE/Kubernetes/Concepts/Storage/Storage|Storage]]
* [[SRE/Kubernetes/Concepts/Configuration/Configuration|Configuration]]
* [[SRE/Kubernetes/Concepts/Scheduling Preemption Eviction/Scheduling Preemption Eviction|Scheduling, Preemption and Eviction]]
* [[SRE/Kubernetes/Concepts/Cluster Administration/Cluster Administration|Cluster Administration]]

### Overview
> [source](https://kubernetes.io/docs/concepts/overview/)
##### Going back in time
![](https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg)
* **Traditional deployment era**: Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.
* **Virtualized deployment era**
	* As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.
	* Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.
* **Container deployment era**
	* Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.
	* Containers have become popular because they provide extra benefits, such as:
		* Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use.
		* Continuous development, integration, and deployment: provides for reliable and frequent container image build and deployment with quick and efficient rollbacks (due to image immutability).
		* Dev and Ops separation of concerns: create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
		* Observability: not only surfaces OS-level information and metrics, but also application health and other signals.
		* Environmental consistency across development, testing, and production: runs the same on a laptop as it does in the cloud.
		* Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine.
		* Resource isolation: predictable application performance.
		* Resource utilization: high efficiency and density.

