1. What is Kubernetes, and why is it important for container orchestration?
	Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides features like load balancing, self-healing, service discovery, and rolling updates, making it easier to manage complex microservices architectures.
2. Explain the concept of a Kubernetes Pod.
	A Pod is the smallest deployable unit in Kubernetes. It represents a single instance of a running process or workload in a cluster. A Pod can contain one or more tightly coupled containers that share the same network namespace and storage, making them suitable for co-located components.
3. What is a Kubernetes Deployment?
	A Kubernetes Deployment is a resource that manages the deployment of ReplicaSets, ensuring that a specified number of pod replicas are running and that they match the desired state defined in the Deployment. Deployments also support rolling updates and rollbacks.
4. What is the purpose of Kubernetes Services?
	Kubernetes Services provide an abstraction to enable network connectivity between Pods and other Kubernetes resources. They allow applications to communicate with each other using a stable IP address or DNS name, regardless of Pod rescheduling or scaling.
5. Explain the difference between Kubernetes StatefulSets and Deployments.
	Kubernetes StatefulSets are designed for managing stateful applications that require stable network identities and persistent storage. StatefulSets provide ordered pod deployment, stable network identities, and persistent storage. Deployments focus on stateless applications and offer rolling updates and scaling capabilities.
6. How do you scale a Kubernetes Deployment?
	To scale a Kubernetes Deployment, you can use the `kubectl scale` command or update the `replicas` field in the Deployment's YAML file. For example: ```sh kubectl scale deployment my-deployment --replicas=3 ```
7. What are Kubernetes Namespaces, and why are they used?
	Kubernetes Namespaces provide a way to partition and isolate resources within a cluster. They help organize resources and prevent naming conflicts by creating separate logical clusters within the same physical cluster.
8. How does Kubernetes handle self-healing?
	Kubernetes achieves self-healing by monitoring the health of Pods and other resources. If a Pod becomes unhealthy or crashes, Kubernetes automatically restarts it or replaces it with a new instance, ensuring that the desired state is maintained.
9. What is a Kubernetes Node?
	A Kubernetes Node is a worker machine in the cluster that runs containerized applications. It is responsible for running Pods and providing the necessary runtime environment. Nodes are managed by the control plane and can be physical or virtual machines.
10. Explain the difference between a DaemonSet and a Deployment.
	A DaemonSet ensures that all (or some) Nodes run a copy of a Pod, while a Deployment ensures a desired number of replicas are running in total across the cluster. DaemonSets are used for system-level applications, while Deployments are used for stateless applications. 
