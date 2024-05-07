* Each object in your cluster has a Name that is unique for that type of resource. Every Kubernetes object also has a UID that is unique across your whole cluster.
* For non-unique user-provided attributes, Kubernetes provides *labels* and *annotations*.

### Names
* name: A client-provided string that refers to an object in a resource URL, such as `/api/v1/pods/some-name`.
* Only one object of a given kind can have a given name at a time. However, if you delete the object, you can make a new object with the same name.
* **Names must be unique across all API versions of the same resource. API resources are distinguished by their API group, resource type, namespace (for namespaced resources), and name. In other words, API version is irrelevant in this context.**

> [!Note]
> In cases when objects represent a physical entity, like a Node representing a physical host, when the host is re-created under the same name without deleting and re-creating the Node, Kubernetes treats the new host as the old one, which may lead to inconsistencies.

Below are four types of commonly used name constraints for resources.

#### DNS Subdomain Names
* Most resource types require a name that can be used as a DNS subdomain name as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123). This means the name must:
	* contain no more than 253 characters
	* contain only lowercase alphanumeric characters, `-` or `.`
	* start with an alphanumeric character
	* end with an alphanumeric character

#### RFC 1123 Label Names
> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names)

#### RFC 1035 Label Names
> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names)

#### Path Segment Name
Some resource types require their names to be able to be safely encoded as a path segment. In other words, the name may not be `.` or `..` and the name may not contain `/` or `%`.

### UIDs
* A Kubernetes systems-generated string to uniquely identify objects.
* Every object created over the whole lifetime of a Kubernetes cluster has a distinct UID. It is intended to distinguish between historical occurrences of similar entities.
* Kubernetes UIDs are universally unique identifiers (also known as UUIDs).