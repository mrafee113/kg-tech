> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)

* Finalizers are namespaced keys that tell Kubernetes to wait until specific conditions are met before it fully deletes resources marked for deletion. Finalizers alert [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to clean up resources the deleted object owned.
* When you tell Kubernetes to delete an object that has finalizers specified for it, the Kubernetes API marks the object for deletion by populating `.metadata.deletionTimestamp`, and returns a 202 status code (HTTP "Accepted"). The target object remains in a terminating state while the control plane, or other components, take the actions defined by the finalizers. After these actions are complete, the controller removes the relevant finalizers from the target object. When the `metadata.finalizers` field is empty, Kubernetes considers the deletion complete and deletes the object.
* You can use finalizers to control [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) of resources. For example, you can define a finalizer to clean up related resources or infrastructure before the controller deletes the target resource.
	* You can use finalizers to control [garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) of [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects) by alerting [controllers](https://kubernetes.io/docs/concepts/architecture/controller/) to perform specific cleanup tasks before deleting the target resource.
* Finalizers don't usually specify the code to execute. Instead, they are typically lists of keys on a specific resource similar to annotations. Kubernetes specifies some finalizers automatically, but you can also specify your own.

### How finalizers work
* When you create a resource using a manifest file, you can specify finalizers in the `metadata.finalizers` field.
* When you attempt to delete the resource, the API server handling the delete request notices the values in the `finalizers` field and does the following:
	* Modifies the object to add a `metadata.deletionTimestamp` field with the time you started the deletion.
	* Prevents the object from being removed until all items are removed from its `metadata.finalizers` field
	* Returns a 202 status code (HTTP "Accepted")
* The controller managing that finalizer notices the update to the object setting the `metadata.deletionTimestamp`, indicating deletion of the object has been requested. The controller then attempts to satisfy the requirements of the finalizers specified for that resource. Each time a finalizer condition is satisfied, the controller removes that key from the resource's finalizers field. When the finalizers field is emptied, an object with a `deletionTimestamp` field set is automatically deleted. You can also use finalizers to prevent deletion of unmanaged resources.

> [!Note]
> - When you `DELETE` an object, Kubernetes adds the deletion timestamp for that object and then immediately starts to restrict changes to the `.metadata.finalizers` field for the object that is now pending deletion. You can remove existing finalizers (deleting an entry from the finalizers list) but you cannot add a new finalizer. You also cannot modify the `deletionTimestamp` for an object once it is set.
> - After the deletion is requested, you can not resurrect this object. The only way is to delete it and make a new similar object.

### Owner references, labels, and finalizers
* Like [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels), [owner references](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/) describe the relationships between objects in Kubernetes, but are used for a different purpose. When a [controller](https://kubernetes.io/docs/concepts/architecture/controller/) manages objects like Pods, it uses labels to track changes to groups of related objects. For example, when a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) creates one or more Pods, the Job controller applies labels to those pods and tracks changes to any Pods in the cluster with the same label.
* The Job controller also adds owner references to those Pods, pointing at the Job that created the Pods. If you delete the Job while these Pods are running, Kubernetes uses the owner references (not labels) to determine which Pods in the cluster need cleanup.
* Kubernetes also processes finalizers when it identifies owner references on a resource targeted for deletion. *I think this means it's recursive.*
* In some situations, finalizers can block the deletion of dependent objects, which can cause the targeted owner object to remain for longer than expected without being fully deleted. In these situations, you should check finalizers and owner references on the target owner and dependent objects to troubleshoot the cause.

> [!Note]
> In cases where objects are stuck in a deleting state, avoid manually removing finalizers to allow deletion to continue. Finalizers are usually added to resources for a reason, so forcefully removing them can lead to issues in your cluster. This should only be done when the purpose of the finalizer is understood and is accomplished in another way (for example, manually cleaning up some dependent object).

