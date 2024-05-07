> [source](https://kubernetes.io/docs/concepts/containers/images/)

* A container image represents binary data that encapsulates an application and all its software dependencies. Container images are executable software bundles that can run standalone and that make very well defined assumptions about their runtime environment.
* You typically create a container image of your application and push it to a registry before referring to it in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/).

### Updating images
When you first create a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/), Pod, or other object that includes a Pod template, then by default the pull policy of all containers in that pod will be set to `IfNotPresent` if it is not explicitly specified. This policy causes the [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) to skip pulling an image if it already exists.

#### Image pull policy
* The `imagePullPolicy` for a container and the tag of the image affect when the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) attempts to pull (download) the specified image.
* values:
	* `IfNotPresent`: the image is pulled only if it is not already present locally.
	* `Always`: every time the kubelet launches a container, the kubelet queries the container image registry to resolve the name to an image [digest](https://docs.docker.com/engine/reference/commandline/pull/#pull-an-image-by-digest-immutable-identifier). If the kubelet has a container image with that exact digest cached locally, the kubelet uses its cached image; otherwise, the kubelet pulls the image with the resolved digest, and uses that image to launch the container.
	* `Never`: the kubelet does not try fetching the image. If the image is somehow already present locally, the kubelet attempts to start the container; otherwise, startup fails. See [pre-pulled images](https://kubernetes.io/docs/concepts/containers/images/#pre-pulled-images) for more details.
* The caching semantics of the underlying image provider make even `imagePullPolicy: Always` efficient, as long as the registry is reliably accessible. Your container runtime can notice that the image layers already exist on the node so that they don't need to be downloaded again.
* To make sure the Pod always uses the same version of a container image, you can specify the image's digest; replace `<image-name>:<tag>` with `<image-name>@<digest>`.
	* When using image tags, if the image registry were to change the code that the tag on that image represents, you might end up with a mix of Pods running the old and new code. An image digest uniquely identifies a specific version of the image, so Kubernetes runs the same code every time it starts a container with that image name and digest specified. Specifying an image by digest fixes the code that you run so that a change at the registry cannot lead to that mix of versions.

##### Default image pull policy
* When you (or a controller) submit a new Pod to the API server, your cluster sets the `imagePullPolicy` field when specific conditions are met (presuming you omitted `imagePullPolicy`):
	* The `imagePullPolicy` is automatically set to `IfNotPresent` when you specify the digest for the container image, you specify the tag for the container image that isn't `:latest`.
	* The `imagePullPolicy` is automatically set to `Always` when you set the tag for the container image as `:latest`, or when you don't specify the tag for the container image.

#### ImagePullBackOff
* When a kubelet starts creating containers for a Pod using a container runtime, it might be possible the container is in [Waiting](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-state-waiting) state because of ImagePullBackOff.
* The status ImagePullBackOff means that a container could not start because Kubernetes could not pull a container image (for reasons such as invalid image name, or pulling from a private registry without `imagePullSecret`). The `BackOff` part indicates that Kubernetes will keep trying to pull the image, with an increasing back-off delay.
* Kubernetes raises the delay between each attempt until it reaches a compiled-in limit, which is 300 seconds (5 minutes).

### Using a private registry
* Private registries may require keys to read images from them.
* Credentials can be provided in several ways:
	* Configuring Nodes to Authenticate to a Private Registry (e.g. [pull an image from a private registry task](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry))
		* all pods can read any configured private registries
		* requires node configuration by cluster administrator
	* Kubelet Credential Provider to dynamically fetch credentials for private registries (e.g. [configure a kubelet image credential provider](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/))
		* kubelet can be configured to use credential provider exec plugin for the respective private registry.
	* Pre-pulled Images
		* all pods can use any images cached on a node
		* requires root access to all nodes to set up
	* Specifying `ImagePullSecrets` on a Pod (kubernetes preferred way)
		* only pods which provide own keys can access the private registry
	* Vendor-specific or local extensions
		* if you're using a custom node configuration, you (or your cloud provider) can implement your mechanism for authenticating the node to the container registry.