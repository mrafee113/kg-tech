> [source](https://kubernetes.io/docs/concepts/services-networking/)

* [[SRE/Kubernetes/Concepts/Networking/Service|Service]]
* [[SRE/Kubernetes/Concepts/Networking/Ingress|Ingress]]
* [[SRE/Kubernetes/Concepts/Networking/EndpointSlices|EndpointSlices]]
* [[SRE/Kubernetes/Concepts/Networking/Network Policies|Network Policies]]
* [[SRE/Kubernetes/Concepts/Networking/DNS for Services and Pods|DNS for Services and Pods]]
* 

---
### The Kubernetes Network Model
* Every `Pod` in a cluster gets its own unique cluster-wide IP address. This means you do not need to explicitly create links between `Pods` and you almost never need to deal with mapping container ports to host ports.
* This creates a clean, backwards-compatible model where `Pods` can be treated much like VMs or physical hosts from the perspectives of port allocation, naming, service discovery, [load balancing](https://kubernetes.io/docs/concepts/services-networking/ingress/#load-balancing), application configuration, and migration.
* Kubernetes imposes the following fundamental requirements on any networking implementation (barring any intentional network segmentation policies):
	* pods can communicate with all other pods on any other [node](https://kubernetes.io/docs/concepts/architecture/nodes/) without NAT
	* agents on a node (e.g. system daemons, kubelet) can communicate with all pods on that node

> [!Note]
> Note: For those platforms that support `Pods` running in the host network (e.g. Linux), when pods are attached to the host network of a node they can still communicate with all pods on all nodes without NAT.

* This model is not only less complex overall, but it is principally compatible with the desire for Kubernetes to enable low-friction porting of apps from VMs to containers. If your job previously ran in a VM, your VM had an IP and could talk to other VMs in your project. This is the same basic model.
* Kubernetes IP addresses exist at the `Pod` scope - containers within a `Pod` share their network namespaces - including their IP address and MAC address. This means that containers within a `Pod` can all reach each other's ports on `localhost`. This also means that containers within a `Pod` must coordinate port usage, but this is no different from processes in a VM. This is called the "IP-per-pod" model.
* How this is implemented is a detail of the particular container runtime in use.
* It is possible to request ports on the `Node` itself which forward to your Pod` `(called host ports), but this is a very niche operation. How that forwarding is implemented is also a detail of the container runtime. The `Pod` itself is blind to the existence or non-existence of host ports.
* Kubernetes networking addresses four concerns:
	* Containers within a Pod [use networking to communicate](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) via loopback.
	* Cluster networking provides communication between different Pods.
	* The [Service](https://kubernetes.io/docs/concepts/services-networking/service/) API lets you [expose an application running in Pods](https://kubernetes.io/docs/tutorials/services/connect-applications-service/) to be reachable from outside your cluster.
		* [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) provides extra functionality specifically for exposing HTTP applications, websites and APIs.
	* You can also use Services to [publish services only for consumption inside your cluster](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).
* The [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/) tutorial lets you learn about Services and Kubernetes networking with a hands-on example.
* [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/) explains how to set up networking for your cluster, and also provides an overview of the technologies involved.