> [source](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/)

This page provides an overview of ephemeral containers: a special type of container that runs temporarily in an existing [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) to accomplish user-initiated actions such as troubleshooting. You use ephemeral containers to inspect services rather than to build applications.

### Understanding ephemeral containers
* [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) are the fundamental building block of Kubernetes applications. Since Pods are intended to be disposable and replaceable, you cannot add a container to a Pod once it has been created. Instead, you usually delete and replace Pods in a controlled fashion using [deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).
* Sometimes it's necessary to inspect the state of an existing Pod, however, for example to troubleshoot a hard-to-reproduce bug. In these cases you can run an ephemeral container in an existing Pod to inspect its state and run arbitrary commands.

#### What is an ephemeral container?
* Ephemeral containers differ from other containers in that they lack guarantees for resources or execution, and they will never be automatically restarted, so they are not appropriate for building applications. Ephemeral containers are described using the same `ContainerSpec` as regular containers, but many fields are incompatible and disallowed for ephemeral containers.
	* Ephemeral containers may not have ports, so fields such as `ports`, `livenessProbe`, `readinessProbe` are disallowed.
	* Pod resource allocations are immutable, so setting `resources` is disallowed.
	* For a complete list of allowed fields, see the [EphemeralContainer reference documentation](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#ephemeralcontainer-v1-core).
* Ephemeral containers are created using a special `ephemeralcontainers` handler in the API rather than by adding them directly to `pod.spec`, so it's not possible to add an ephemeral container using `kubectl edit`.
* Like regular containers, you may not change or remove an ephemeral container after you have added it to a Pod.

> [!Note]
> Ephemeral containers are not supported by static pods.

### Uses for ephemeral containers
* Ephemeral containers are useful for interactive troubleshooting when `kubectl exec` is insufficient because a container has crashed or a container image doesn't include debugging utilities.
* In particular, [distroless images](https://github.com/GoogleContainerTools/distroless) enable you to deploy minimal container images that reduce attack surface and exposure to bugs and vulnerabilities. Since distroless images do not include a shell or any debugging utilities, it's difficult to troubleshoot distroless images using `kubectl exec` alone.
* When using ephemeral containers, it's helpful to enable [process namespace sharing](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) so you can view processes in other containers.