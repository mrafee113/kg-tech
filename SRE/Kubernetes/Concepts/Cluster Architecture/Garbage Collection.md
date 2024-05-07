> [source](https://kubernetes.io/docs/concepts/architecture/garbage-collection/)

* Garbage collection is a collective term for the various mechanisms Kubernetes uses to clean up cluster resources. This allows the clean up of resources like the following:
	* [Terminated pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)
	* [Completed Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)
	* [Objects without owner references](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#owners-dependents)
	* [Unused containers and container images](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images)
	* [Dynamically provisioned PersistentVolumes with a StorageClass reclaim policy of Delete](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#delete)
	* [Stale or expired CertificateSigningRequests (CSRs)](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#request-signing-process)
	* [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) deleted in the following scenarios:
		* On a cloud when the cluster uses a [cloud controller manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/)
		* On-premises when the cluster uses an addon similar to a cloud controller manager
	* [Node Lease objects](https://kubernetes.io/docs/concepts/architecture/nodes/#heartbeats)

### Owners and dependents
* Many objects in Kubernetes link to each other through [owner references](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/). Owner references tell the control plane which objects are dependent on others. Kubernetes uses owner references to give the control plane, and other API clients, the opportunity to clean up related resources before deleting an object. In most cases, Kubernetes manages owner references automatically.
* Owner references help different parts of Kubernetes avoid interfering with objects they don’t control.

### Cascading deletion
* Kubernetes checks for and deletes objects that no longer have owner references, like the pods left behind when you delete a ReplicaSet. When you delete an object, you can control whether Kubernetes deletes the object's dependents automatically, in a process called cascading deletion. There are two types of cascading deletion, as follows:
	* Foreground cascading deletion
	* Background cascading deletion
* You can also control how and when garbage collection deletes resources that have owner references using Kubernetes [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/).

#### Foreground cascading deletion
* In foreground cascading deletion, the owner object you're deleting first enters a deletion in progress state. In this state, the following happens to the owner object:
	* The Kubernetes API server sets the object's `metadata.deletionTimestamp` field to the time the object was marked for deletion.
	* The Kubernetes API server also sets the `metadata.finalizers` field to `foregroundDeletion`.
	* The object remains visible through the Kubernetes API until the deletion process is complete.
* After the owner object enters the deletion in progress state, the controller deletes the dependents. After deleting all the dependent objects, the controller deletes the owner object. At this point, the object is no longer visible in the Kubernetes API.
* During foreground cascading deletion, the only dependents that block owner deletion are those that have the `ownerReference.blockOwnerDeletion=true` field. See Use [foreground cascading deletion](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/#use-foreground-cascading-deletion) to learn more.

#### Background cascading deletion
* In background cascading deletion, the Kubernetes API server deletes the owner object immediately and the controller cleans up the dependent objects in the background. By default, Kubernetes uses background cascading deletion unless you manually use foreground deletion or choose to orphan the dependent objects.
* See Use [background cascading deletion](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/#use-background-cascading-deletion) to learn more.

### Garbage collection of unused  containers and images
* The [kubelet](https://kubernetes.io/docs/reference/generated/kubelet) performs garbage collection on unused images every five minutes and on unused containers every minute. You should avoid using external garbage collection tools, as these can break the kubelet behavior and remove containers that should exist.
* To configure options for unused container and image garbage collection, tune the kubelet using a [configuration file](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/) and change the parameters related to garbage collection using the [KubeletConfiguration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/) resource type.

#### Container image lifecycle
* Kubernetes manages the lifecycle of all images through its image manager, which is part of the kubelet, with the cooperation of [cadvisor](https://github.com/google/cadvisor/). The kubelet considers the following disk usage limits when making garbage collection decisions:
	* `HighThresholdPercent`
	* `LowThresholdPercent`
* Disk usage above the configured `HighThresholdPercent` value triggers garbage collection, which deletes images in order based on the last time they were used, starting with the oldest first. The kubelet deletes images until disk usage reaches the `LowThresholdPercent` value.

#### Container garbage collection
* The kubelet garbage collects unused containers based on the following variables, which you can define:
	* `MinAge`: the minimum age at which the kubelet can garbage collect a container. Disable by setting to 0.
	* `MaxPerPodContainer`: the maximum number of dead containers each Pod can have. Disable by setting to less than 0.
	* `MaxContainers`: the maximum number of dead containers the cluster can have. Disable by setting to less than 0.
* In addition to these variables, the kubelet garbage collects unidentified and deleted containers, typically starting with the oldest first.

> [!Note]
> The kubelet only garbage collects the containers it manages.

### Configuring garbage collection
* You can tune garbage collection of resources by configuring options specific to the controllers managing those resources. The following pages show you how to configure garbage collection:
	* [Configuring cascading deletion of Kubernetes objects](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/)
	* [Configuring cleanup of finished Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)
