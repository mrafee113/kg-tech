> [source](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

* The core of Kubernetes' [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) is the [API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver). The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another.
* The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes.
* Most operations can be performed through the [kubectl](https://kubernetes.io/docs/reference/kubectl/) command-line interface or other command-line tools, such as [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/), which in turn use the API. However, you can also access the API directly using REST calls.
* **Persistence**: Kubernetes stores the serialized state of objects by writing them into [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/).
