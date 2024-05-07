> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)

* Read the [Kubectl book](https://kubectl.docs.kubernetes.io/) for details of managing objects by Kubectl.

### Management techniques

> [!Warning]
> A Kubernetes object should be managed using only one technique. Mixing and matching techniques for the same object results in undefined behavior.

|Management technique|Operates on|Recommended environment|Supported writers|Learning curve|
|---|---|---|---|---|
|Imperative commands|Live objects|Development projects|1+|Lowest|
|Imperative object configuration|Individual files|Production projects|1|Moderate|
|Declarative object configuration|Directories of files|Production projects|1+|Highest|

### Imperative commands
* When using imperative commands, a user operates directly on live objects in a cluster. The user provides operations to the kubectl command as arguments or flags.
* This is the recommended way to get started or to run a one-off task in a cluster. Because this technique operates directly on live objects, it provides no history of previous configurations.
* Trade-Offs
	* Advantages compared to object configuration:
		* Commands are expressed as a single action word.
		* Commands require only a single step to make changes to the cluster.
	* Disadvantages compared to object configuration:
		* Commands do not integrate with change review processes.
		* Commands do not provide an audit trail associated with changes.
		* Commands do not provide a source of records except for what is live.
		* Commands do not provide a template for creating new objects.

### Imperative object configuration
* In imperative object configuration, the kubectl command specifies the operation (create, replace, etc.), optional flags and at least one file name. The file specified must contain a full definition of the object in YAML or JSON format.

> [!Warning]
> The imperative `replace` command replaces the existing spec with the newly provided one, dropping all changes to the object missing from the configuration file. This approach should not be used with resource types whose specs are updated independently of the configuration file. Services of type `LoadBalancer`, for example, have their `externalIPs` field updated independently from the configuration by the cluster.

* Trade-Offs
	* Advantages compared to imperative commands:
		* Object configuration can be stored in a source control system such as Git.
		* Object configuration can integrate with processes such as reviewing changes before push and audit trails.
		* Object configuration provides a template for creating new objects.
	* Disadvantages compared to imperative commands:
		* Object configuration requires basic understanding of the object schema.
		* Object configuration requires the additional step of writing a YAML file.
	* Advantages compared to declarative object configuration:
		* Imperative object configuration behavior is simpler and easier to understand.
	* Disadvantages compared to declarative object configuration:
		* Imperative object configuration works best on files, not directories.
		* Updates to live objects must be reflected in configuration files, or they will be lost during the next replacement.

### Declarative object configuration
* When using declarative object configuration, a user operates on object configuration files stored locally, however the user does not define the operations to be taken on the files. Create, update, and delete operations are automatically detected per-object by kubectl. This enables working on directories, where different operations might be needed for different objects.
* Trade-Offs
	* Advantages compared to imperative object configuration:
		* Changes made directly to live objects are retained, even if they are not merged back into the configuration files.
		* Declarative object configuration has better support for operating on directories and automatically detecting operation types (create, patch, delete) per-object.
	* Disadvantages compared to imperative object configuration:
		* Declarative object configuration is harder to debug and understand results when they are unexpected.
		* Partial updates using diffs create complex merge and patch operations.
