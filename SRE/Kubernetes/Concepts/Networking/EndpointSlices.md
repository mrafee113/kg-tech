> [source](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)

* Kubernetes' *EndpointSlice* API provides a way to track network endpoints within a Kubernetes cluster. EndpointSlices offer a more scalable and extensible alternative to [Endpoints](https://kubernetes.io/docs/concepts/services-networking/service/#endpoints).

### EndpointSlice API
* In Kubernetes, an EndpointSlice contains references to a set of network endpoints. The control plane automatically creates EndpointSlices for any Kubernetes Service that has a [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) specified. These EndpointSlices include references to all the Pods that match the Service selector. EndpointSlices group network endpoints together by unique combinations of protocol, port number, and Service name.
* EndpointSlices can act as the source of truth for [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) when it comes to how to route internal traffic.
