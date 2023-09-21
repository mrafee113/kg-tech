### Installation
* [[SRE/Kubernetes/Kubespray|Kubespray]]
* [mrafee113/kubespray-vagrant](https://github.com/mrafee113/kubespray-vagrant)

### Tutorials
* [[SRE/Kubernetes/Tutorials/Basics|Basics]]
* [[SRE/Kubernetes/Tutorials/The Hard Way|The Hard Way]]

### Concepts


### Addons
> [[SRE/Kubernetes/Addons/Addons|addons]]
* [[SRE/Kubernetes/Addons/MetalLB|MetalLB]]

### Docs: Table of Contents
> [source](https://kubernetes.io/docs/)

* sum: `35.53 + 60% * 22.05 + 5% * 10.13 = 49' 15"`
* `4hpd` -> `12.48days`

* [Concepts](https://kubernetes.io/docs/concepts/): `0"` + `35' 32"`
	* [Overview](https://kubernetes.io/docs/concepts/overview/): `20"` + `3' 29"`
		* [Objects in Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/): `19"` + `2' 34"`
			* [Kubernetes Object Management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/): `17"`
			* [Object Names and IDs](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/): `15"`
			* [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/): `27"`
			* [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/): `17"`
			* [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/): `15"`
			* [Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/): `14"`
			* [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/): `17"`
			* [Owners and Dependants](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/): `16"`
			* [Recommended Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/): `16"`
		* [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/): `19"`
		* [The Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/): `19"`
	* [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/): `0"` + `1' 59"`
		* [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/): `34"`
		* [Communication between Nodes and the Control Plane](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/): `17"`
		* [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/): `19"`
		* [About cgroups v2](https://kubernetes.io/docs/concepts/architecture/cgroups/): `16"`
		* [Container Runtime Interface](https://kubernetes.io/docs/concepts/architecture/cri/): `14"`
		* [Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/): `19"`
	* [Containers](https://kubernetes.io/docs/concepts/containers/): `14"` + `1' 22"`
		* [Images](https://kubernetes.io/docs/concepts/containers/images/): `32"`
		* [Container Environment](https://kubernetes.io/docs/concepts/containers/container-environment/): `13"`
		* [Runtime Class](https://kubernetes.io/docs/concepts/containers/runtime-class/): `17"`
		* [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/): `20"`
	* [Workloads](https://kubernetes.io/docs/concepts/workloads/): `16"` + `11' 53"`
		* [Pods](https://kubernetes.io/docs/concepts/workloads/pods/): `28"` + `2' 42"`
			* [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/): `39"`
			* [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/): `32"`
			* [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/): `24"`
			* [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/): `14"`
			* [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/): `18"`
			* [User Namespaces](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/): `20"`
			* [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/): `15"`
		* [Workload Resources](https://kubernetes.io/docs/concepts/workloads/controllers/): `15"` + `9' 10"`
			* [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/): `5' 34"`
			* [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/): `31"`
			* [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/): `32"`
			* [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/): `25"`
			* [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/): `58"`
			* [Automatic Cleanup for Finished Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/): `15"`
			* [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/): `25"`
			* [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/): `30"`
	* [Services, Load Balancing, and Networking](https://kubernetes.io/docs/concepts/services-networking/): `17"` + `3' 5"`
		* [Service](https://kubernetes.io/docs/concepts/services-networking/service/): `47"`
		* [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/): `43"`
		* [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/): `22"`
		* [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/): `31"`
		* [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/): `26"`
		* [Service ClusterIP allocation](https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/): `16"`
	* [Storage](https://kubernetes.io/docs/concepts/storage/): `0"` + `4' 30"`
		* [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/): `57"`
		* [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/): `57"`
		* [Projected Volumes](https://kubernetes.io/docs/concepts/storage/projected-volumes/): `21"`
		* [Ephemeral Volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/): `22"`
		* [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/): `32"`
		* [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/): `16"`
		* [Volume Snapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/): `20"`
		* [Volume Snapshot Classes](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/): `14"`
		* [CSI Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/): `15"`
		* [Storage Capacity](https://kubernetes.io/docs/concepts/storage/storage-capacity/): `16"`
	* [Configuration](https://kubernetes.io/docs/concepts/configuration/): `0"` + `2' 13"`
		* [Configuration Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/): `19"`
		* [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/): `24"`
		* [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/): `43"`
		* [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/): `47"`
	* [Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/): `0"` + `2' 33"`
		* [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/): `16"`
		* [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/): `39"`
		* [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/): `24"`
		* [Pod Priority and Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/): `28"`
		* [Node-Pressure Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/): `30"`
		* [API-Initiated Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/): `16"`
	* [Cluster Administration](https://kubernetes.io/docs/concepts/cluster-administration/): `14"` + `3' 7"`
		* [Managing Resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/): `24"`
		* [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/): `14"`
		* [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/): `29"`
		* [Metrics for Kubernetes System Components](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/): `19"`
		* [System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/): `22"`
		* [Proxies in Kubernetes](https://kubernetes.io/docs/concepts/cluster-administration/proxies/): `13`
		* [API Priorities and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/): `49"`
		* [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/): `17"`
* [Tasks](https://kubernetes.io/docs/tasks/): `0"` + `22' 3"`
	* [Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/): `0"` + `4' 15"`
		* [Manage Memory, CPU, and API Resources](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/): `0"` + `1' 52"`
			* [Configure Default Memory Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/): `19"`
			* [Configure Default CPU Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/): `18"`
			* [Configure Minimum and Maximum Memory Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/): `21"`
			* [Configure Minimum and Maximum CPU Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/): `21"`
			* [Configure Memory and CPU Quotas for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/): `18"`
			* [Configure a Pod Quota for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/): `15"`
		* [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/): `25"`
		* [Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/): `17"`
		* [Namespaces Walkthrough](https://kubernetes.io/docs/tasks/administer-cluster/namespaces-walkthrough/): `22"`
		* [Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/): `22"`
		* [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/): `17"`
		* [Share a Cluster with Namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/): `24"`
		* [Use Cascading Deletion in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/): `16"`
	* [Configure Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/): `0"` + `5' 13"`
		* [Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/): `25"`
		* [Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/): `22"`
		* [Resize CPU and Memory Resources to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/): `21"`
		* [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/): `20"`
		* [Configure a Pod to use a Volume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/): `17"`
		* [Configure a Pod to use a PersistentVolume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/): `23"`
		* [Configure a Pod to use a ProjectedVolume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/): `15"`
		* [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/): `28"`
		* [Configure Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/): `37"`
		* [Assign Pods to Nodes](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/): `16"`
		* [Assign Pods to Nodes using NodeAffinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/): `18"`
		* [Configure Pod Initialization](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/): `15"`
		* [Attach Handlers to Container Lifecycle Events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/): `15"`
		* [Configure a Pod to Use a ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/): `41"`
	* [Monitoring, Logging, and Debugging](https://kubernetes.io/docs/tasks/debug/): `0"` + `4' 9"`
		* [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/): `0"` + `2' 2"`
			* [Debug Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/): `18"`
			* [Debug Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/): `36"`
			* [Debug a StatefulSet](https://kubernetes.io/docs/tasks/debug/debug-application/debug-statefulset/): `13"`
			* [Determine the Reason for Pod Failure](https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/): `16"`
			* [Debugging Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/): `39"`
		* [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/): `0"` + `2' 7"`
			* [Resource Metrics Pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/): `19"`
			* [Tools for Monitoring Resources](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/): `16"`
			* [Monitor Node Health](https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/): `22"`
			* [Debugging Kubernetes nodes with crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/): `30"`
			* [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/): `24"`
			* [Debugging Kubernetes Nodes with Kubectl](https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/): `16"`
	* [Managing Kubernetes Objects](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/): `0"` + `2' 31"`
		* [Declarative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/): `50"`
		* [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/): `36"`
		* [Managing Kubernetes Objects using Imperative Commands](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/): `18"`
		* [Imperative Management of Kubernetes Objects using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/): `17"`
		* [Update API Objects in-place using kubectl patch](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/): `30"`
	* [Managing Secrets](https://kubernetes.io/docs/tasks/configmap-secret/): `0"` + `48"`
		* [Managing Secrets using kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/): `17"`
		* [Managing Secrets using Configuration Files](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/): `17"`
		* [Managing Secrets using Kustomize](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/): `14"`
	* [Inject Data into Applications](https://kubernetes.io/docs/tasks/inject-data-application/): `0"` + `1' 57"`
		* [Define a Command and Arguments for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/): `15"`
		* [Define Dependant Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/): `16"`
		* [Define Environment Variables for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/): `16"`
		* [Expose Pod Information to Containers through Environment Variables](https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/): `21"`
		* [Expose Pod Information to Containers through Files](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/): `23"`
		* [Distribute Credentials Securely using Secrets](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/): `26"`
	* [Run Applications](https://kubernetes.io/docs/tasks/run-application/): `0"` + `41"`
		* [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/): `25"`
		* [Accessing the Kubernetes API from a Pod](https://kubernetes.io/docs/tasks/run-application/access-api-from-pod/): `16"`
	* [Run Jobs](https://kubernetes.io/docs/tasks/job/): `0"` + `17"`
		* [Running Automated tasks with a CronJob](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/): `17"`
	* [Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/): `0"` + `2' 12"`
		* [Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/): `21"`
		* [Use Port Forwarding to Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/): `17"`
		* [Use a Service to Access an Application in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/): `18"`
		* [Connect a Frontend to a Backend Using Services](https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/): `24"`
		* [Create an External Load Balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/): `20"`
		* [List all Container Images Running in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/): `15"`
		* [Access Services Running on Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster-services/): `17"`
* [Reference](https://kubernetes.io/docs/reference/): `0"` + `10' 8"`
	* [Glossary](https://kubernetes.io/docs/reference/glossary/?fundamental=true): `19"`
	* [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/): `7' 59"`
	* [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/): `0"` don't read for now...
	* [Kubectl](https://kubernetes.io/docs/reference/kubectl/): `30"` + `40"`
		* [Kubectl Cheat sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/): `40"`
		* [Kubectl Commands](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands): `0"`