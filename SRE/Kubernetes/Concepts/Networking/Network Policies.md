> [source](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

* If you want to control traffic flow at the IP address or port level (OSI layer 3 or 4), then you might consider using Kubernetes NetworkPolicies for particular applications in your cluster. NetworkPolicies are an application-centric construct which allow you to specify how a [pod](https://kubernetes.io/docs/concepts/workloads/pods/) is allowed to communicate with various network "entities" (we use the word "entity" here to avoid overloading the more common terms such as "endpoints" and "services", which have specific Kubernetes connotations) over the network. NetworkPolicies apply to a connection with a pod on one or both ends, and are not relevant to other connections.
* The entities that a Pod can communicate with are identified through a combination of the following 3 identifiers:
	* Other pods that are allowed (exception: a pod cannot block access to itself)
	* Namespaces that are allowed
	* IP blocks (exception: traffic to and from the node where a Pod is running is always allowed, regardless of the IP address of the Pod or the node)
* When defining a pod- or namespace- based NetworkPolicy, you use a [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to specify what traffic is allowed to and from the Pod(s) that match the selector.
* Meanwhile, when IP based NetworkPolicies are created, we define policies based on IP blocks (CIDR ranges).

### Prerequisites
Network policies are implemented by the [network plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/). To use network policies, you must be using a networking solution which supports NetworkPolicy. Creating a NetworkPolicy resource without a controller that implements it will have no effect.
