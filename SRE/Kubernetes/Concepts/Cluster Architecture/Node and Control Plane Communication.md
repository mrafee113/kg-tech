> [source](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/)

* This document catalogs the communication paths between the [API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) and the Kubernetes cluster. The intent is to allow users to customize their installation to harden the [network](https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster) configuration such that the cluster can be run on an untrusted network (or on fully public IPs on a cloud provider).

### Node to Control Plane
* Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes (or the pods they run) terminates at the API server. None of the other control plane components are designed to expose remote services. The API server is configured to listen for remote connections on a secure HTTPS port (typically 443) with one or more forms of client [authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) enabled. One or more forms of [authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) should be enabled, especially if [anonymous requests](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#anonymous-requests) or [service account tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens) are allowed.
* [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) that wish to connect to the API server can do so securely by leveraging a service account so that Kubernetes will automatically inject the public root certificate and a valid bearer token into the pod when it is instantiated. The kubernetes service (in default namespace) is configured with a virtual IP address that is redirected (via [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)) to the HTTPS endpoint on the API server.
* The default operating mode for connections from the nodes and pod running on the nodes to the control plane is secured by default and can run over untrusted and/or public networks.

### Control Plane to Node
* There are two primary communication paths from the control plane (the API server) to the nodes. The first is from the API server to the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) process which runs on each node in the cluster. The second is from the API server to any node, pod, or service through the API server's proxy functionality.

#### API server to kubelet
* The connections from the API server to the kubelet are used for:
	* Fetching logs for pods.
	* Attaching (usually through kubectl) to running pods.
	* Providing the kubelet's port-forwarding functionality.
* These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle attacks and **unsafe** to run over untrusted and/or public networks.
	* To verify this connection, use the `--kubelet-certificate-authority` flag to provide the API server with a root certificate bundle to use to verify the kubelet's serving certificate.
	* If that is not possible, use [SSH tunneling](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#ssh-tunnels) between the API server and kubelet if required to avoid connecting over an untrusted or public network.
	* Finally, [Kubelet authentication and/or authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/) should be enabled to secure the kubelet API.

#### API server to nodes, pods, and services
The connections from the API server to a node, pod, or service default to plain HTTP connections and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So while the connection will be encrypted, it will not provide any guarantees of integrity. These connections are not currently safe to run over untrusted or public networks.

#### Konnectivity service
* As a replacement to the SSH tunnels (deprecated), the Konnectivity service provides TCP level proxy for the control plane to cluster communication. The Konnectivity service consists of two parts: the Konnectivity server in the control plane network and the Konnectivity agents in the nodes network. The Konnectivity agents initiate connections to the Konnectivity server and maintain the network connections. After enabling the Konnectivity service, all control plane to nodes traffic goes through these connections.
* Follow the [Konnectivity service task](https://kubernetes.io/docs/tasks/extend-kubernetes/setup-konnectivity/) to set up the Konnectivity service in your cluster.
