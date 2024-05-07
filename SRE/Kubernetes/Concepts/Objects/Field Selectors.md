> [source](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/)

* Field selectors let you select Kubernetes objects based on the value of one or more resource fields. 
* Here are some examples of field selector queries:
	* `metadata.name=my-service`
	* `metadata.namespace!=default`
	* `status.phase=Pending`

> [!Note]
> Field selectors are essentially resource filters. By default, no selectors/filters are applied, meaning that all resources of the specified type are selected. This makes the `kubectl` queries `kubectl get pods` and `kubectl get pods --field-selector ""` equivalent.

* Supported fields: Supported field selectors vary by Kubernetes resource type. All resource types support the `metadata.name` and `metadata.namespace` fields. Using unsupported field selectors produces an error.
* Supported operators: You can use the `=`, `==`, and `!=` operators with field selectors (`=` and `==` mean the same thing). Note that set-based operators (`in`, `notin`, `exists`) are not supported for field selectors.
* Chained selectors: As with label and other selectors, field selectors can be chained together as a comma-separated list.
* Multiple resource types: You can use field selectors across multiple resource types.