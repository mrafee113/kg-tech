> [source](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

* Kubernetes creates DNS records for Services and Pods. You can contact Services with consistent DNS names instead of IP addresses.
* Kubernetes publishes information about Pods and Services which is used to program DNS. Kubelet configures Pods' DNS so that running containers can lookup Services by name rather than IP.
* Services defined in the cluster are assigned DNS names. By default, a client Pod's DNS search list includes the Pod's own namespace and the cluster's default domain.