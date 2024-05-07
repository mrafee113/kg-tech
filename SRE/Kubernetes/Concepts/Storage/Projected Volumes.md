> [source](https://kubernetes.io/docs/concepts/storage/projected-volumes/)

### Introduction
* A `projected` volume maps several existing volume sources into the same directory.
* Currently, the following types of volume sources can be projected:
	* [`secret`](https://kubernetes.io/docs/concepts/storage/volumes/#secret)
	* [`downwardAPI`](https://kubernetes.io/docs/concepts/storage/volumes/#downwardapi)
	* [`configMap`](https://kubernetes.io/docs/concepts/storage/volumes/#configmap)
	* [`serviceAccountToken`](https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken)
* All sources are required to be in the same namespace as the Pod. For more details, see the [all-in-one volume](https://git.k8s.io/design-proposals-archive/node/all-in-one-volume.md) design document.
