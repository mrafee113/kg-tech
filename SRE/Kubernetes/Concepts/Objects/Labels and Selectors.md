> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
* Labels are key/value pairs that are attached to objects such as Pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. Labels can be used to organize and to select subsets of objects. Labels can be attached to objects at creation time and subsequently added and modified at any time. Each object can have a set of key/value labels defined. Each Key must be unique for a given object.
* Labels allow for efficient queries and watches and are ideal for use in UIs and CLIs. Non-identifying information should be recorded using *annotations*.

### Motivation
* Labels enable users to map their own organizational structures onto system objects in a loosely coupled fashion, without requiring clients to store these mappings.
* Service deployments and batch processing pipelines are often multi-dimensional entities (e.g., multiple partitions or deployments, multiple release tracks, multiple tiers, multiple micro-services per tier). Management often requires cross-cutting operations, which breaks encapsulation of strictly hierarchical representations, especially rigid hierarchies determined by the infrastructure rather than by users.
* Find examples of common labels at [Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/).

### Syntax and character set
* Labels are key/value pairs. Valid label keys have two segments: an optional prefix and name, separated by a slash `/`.
	* The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character with `-`, `_`, `.`, and alphanumerics between.
	* The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by `.`, not longer than 253 characters in total, followed by a `/`.
		* If the prefix is omitted, the label Key is presumed to be private to the user. Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation) which add labels to end-user objects must specify a prefix.
		* The `kubernetes.io/` and `k8s.io/` prefixes are reserved for Kubernetes core components.
* Valid label value:
	* must be 63 characters or less (can be empty)
	* unless empty, must begin and end with an alphanumeric character,
	* could contain `-`, `_`, `.`, and alphanumerics between.

### Label selectors
* Unlike names and UIDs, labels do not provide uniqueness. In general, we expect many objects to carry the same label(s).
* Via a label selector, the client/user can identify a set of objects. The label selector is the core grouping primitive in Kubernetes.
* The API currently supports two types of selectors: equality-based and set-based. A label selector can be made of multiple requirements which are comma-separated. In the case of multiple requirements, all must be satisfied so the comma separator acts as a logical AND `&&` operator.

> [!Note]
> For some API types, such as ReplicaSets, the label selectors of two instances must not overlap within a namespace, or the controller can see that as conflicting instructions and fail to determine how many replicas should be present.

> [!Caution]
> For both equality-based and set-based conditions there is no logical OR (||) operator. Ensure your filter statements are structured accordingly.

#### Equality-based requirement
Equality- or inequality-based requirements allow filtering by label keys and values. Matching objects must satisfy all of the specified label constraints, though they may have additional labels as well. Three kinds of operators are admitted `=`, `==`, `!=`. The first two represent equality (and are synonyms), while the latter represents inequality.

#### Set-based requirement
* Set-based label requirements allow filtering keys according to a set of values. Three kinds of operators are supported: `in`, `notin` and `exists` (only the key identifier).
* Similarly the comma separator acts as an AND operator.
* Set-based requirements can be mixed with equality-based requirements.

#### Resources that support set-based requirement
* Newer resources, such as *Job*, *Deployment*, *ReplicaSet*, and *DaemonSet*, support set-based requirements as well.
* matchLabels is a map of `{key,value}` pairs. A single `{key,value}` in the matchLabels map is equivalent to an element of matchExpressions, whose key field is `key`, the operator is `In`, and the values array contains only `value`. matchExpressions is a list of pod selector requirements. Valid operators include `In`, `NotIn`, `Exists`, and `DoesNotExist`. The values set must be non-empty in the case of `In` and `NotIn`. All of the requirements, from both matchLabels and matchExpressions are `AND`ed together -- they must all be satisfied in order to match.
