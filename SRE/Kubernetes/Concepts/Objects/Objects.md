> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/)

* [[SRE/Kubernetes/Concepts/Objects/Object Management|Object Management]]
* [[SRE/Kubernetes/Concepts/Objects/Object Names and IDs|Object Names and IDs]]
* [[SRE/Kubernetes/Concepts/Objects/Labels and Selectors|Labels and Selectors]]
* [[SRE/Kubernetes/Concepts/Objects/Namespaces|Namespaces]]
* [[SRE/Kubernetes/Concepts/Objects/Annotations|Annotations]]
* [[SRE/Kubernetes/Concepts/Objects/Field Selectors|Field Selectors]]
* [[SRE/Kubernetes/Concepts/Objects/Finalizers|Finalizers]]
* [[SRE/Kubernetes/Concepts/Objects/Owners and Dependents|Owners and Dependents]]
* [[SRE/Kubernetes/Concepts/Objects/Recommended Labels|Recommended Labels]]

### Understanding Kubernetes Objects
* Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Specifically, they can describe:
	* What containerized applications are running (and on which nodes)
	* The resources available to those applications
	* The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance
* A Kubernetes object is a "record of intent"--once you create the object, the Kubernetes system will constantly work to ensure that object exists. By creating an object, you're effectively telling the Kubernetes system what you want your cluster's workload to look like; this is your cluster's desired state.

#### Object spec and status
* Almost every Kubernetes object includes two nested object fields that govern the object's configuration: the object `spec` and the object `status`.
* For objects that have a spec, you have to set this when you create the object, providing a description of the characteristics you want the resource to have: its desired state.
* The `status` describes the current state of the object, supplied and updated by the Kubernetes system and its components. The Kubernetes control plane continually and actively manages every object's actual state to match the desired state you supplied.
* For more information on the object spec, status, and metadata, see the [Kubernetes API Conventions](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md).

#### Describing a kubernetes object
When you create an object in Kubernetes, you must provide the object spec that describes its desired state, as well as some basic information about the object (such as a name). When you use the Kubernetes API to create the object, that API request must include that information as JSON in the request body. Most often, you provide the information to kubectl in file known as a manifest. By convention, manifests are YAML (you could also use JSON format). Tools such as kubectl convert the information from a manifest into JSON or another supported serialization format when making the API request over HTTP.

#### Required fields
* In the manifest for the Kubernetes object you want to create, you'll need to set values for the following fields:
	* `apiVersion` - Which version of the Kubernetes API you're using to create this object
	* `kind` - What kind of object you want to create
	* `metadata` - Data that helps uniquely identify the object, including a name string, UID, and optional namespace
	* `spec` - What state you desire for the object
* The precise format of the object spec is different for every Kubernetes object, and contains nested fields specific to that object. The [Kubernetes API Reference](https://kubernetes.io/docs/reference/kubernetes-api/) can help you find the spec format for all of the objects you can create using Kubernetes.
