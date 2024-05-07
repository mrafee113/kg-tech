> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)

* In addition to supporting tooling, the recommended labels describe applications in a way that can be queried.
* The metadata is organized around the concept of an application. Kubernetes is not a platform as a service (PaaS) and doesn't have or enforce a formal notion of an application. Instead, applications are informal and described with metadata. The definition of what an application contains is loose.

> [!Note]
> These are recommended labels. They make it easier to manage applications but aren't required for any core tooling.

* Shared labels and annotations share a common prefix: `app.kubernetes.io`. Labels without a prefix are private to users. The shared prefix ensures that shared labels do not interfere with custom user labels.

### Labels
* In order to take full advantage of using these labels, they should be applied on every resource object.

|Key|Description|Example|Type|
|---|---|---|---|
|`app.kubernetes.io/name`|The name of the application|`mysql`|string|
|`app.kubernetes.io/instance`|A unique name identifying the instance of an application|`mysql-abcxzy`|string|
|`app.kubernetes.io/version`|The current version of the application (e.g., a [SemVer 1.0](https://semver.org/spec/v1.0.0.html), revision hash, etc.)|`5.7.21`|string|
|`app.kubernetes.io/component`|The component within the architecture|`database`|string|
|`app.kubernetes.io/part-of`|The name of a higher level application this one is part of|`wordpress`|string|
|`app.kubernetes.io/managed-by`|The tool being used to manage the operation of an application|

### Applications and instances of applications
* An application can be installed one or more times into a Kubernetes cluster and, in some cases, the same namespace.
* The name of an application and the instance name are recorded separately. This enables the application and instance of the application to be identifiable. Every instance of an application must have a unique name.
