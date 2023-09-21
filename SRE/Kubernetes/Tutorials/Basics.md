 > [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

* What can Kubernetes do for you?
	With modern web services, users expect applications to be available 24/7, and developers expect to deploy new versions of those applications several times a day. Containerization helps package software to serve these goals, enabling applications to be released and updated without downtime. Kubernetes helps you make sure those containerized applications run where and when you want, and helps them find the resources and tools they need to work. Kubernetes is a production-ready, open source platform designed with Google's accumulated experience in container orchestration, combined with best-of-breed ideas from the community.

## Deploy an App: using kubectl to create a deployment
> [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)

* Objectives
	* Learn about application Deployments.
	* Deploy your first app on Kubernetes with kubectl.

### Kubernetes Deployments
* Once you have a running Kubernetes cluster, you can deploy your containerized applications on top of it. To do so, you create a Kubernetes Deployment. The Deployment instructs Kubernetes how to create and update instances of your application. Once you've created a Deployment, the Kubernetes control plane schedules the application instances included in that Deployment to run on individual Nodes in the cluster.
* Once the application instances are created, a Kubernetes Deployment controller continuously monitors those instances. If the Node hosting an instance goes down or is deleted, the Deployment controller replaces the instance with an instance on another Node in the cluster. **This provides a self-healing mechanism to address machine failure or maintenance.**
* In a pre-orchestration world, installation scripts would often be used to start applications, but they did not allow recovery from machine failure. By both creating your application instances and keeping them running across Nodes, Kubernetes Deployments provide a fundamentally different approach to application management.

### Deploying your first app on Kubernetes
![](https://d33wubrfki0l68.cloudfront.net/8700a7f5f0008913aa6c25a1b26c08461e4947c7/cfc2c/docs/tutorials/kubernetes-basics/public/images/module_02_first_app.svg)
* You can create and manage a Deployment by using the Kubernetes command line interface, kubectl. Kubectl uses the Kubernetes API to interact with the cluster. In this module, you'll learn the most common kubectl commands needed to create Deployments that run your applications on a Kubernetes cluster.
* When you create a Deployment, you'll need to specify the container image for your application and the number of replicas that you want to run. You can change that information later by updating your Deployment; Modules [5](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/) and [6](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) of the bootcamp discuss how you can scale and update your Deployments.
* For your first Deployment, you'll use a hello-node application packaged in a Docker container that uses NGINX to echo back all the requests. (If you didn't already try creating a hello-node application and deploying it using a container, you can do that first by following the instructions from the [Hello Minikube tutorial](https://kubernetes.io/docs/tutorials/hello-minikube/)).

#### kubectl basics
* The common format of a kubectl command is: `kubectl [action] [resource]`
* This performs the specified action (like `create`, `describe` or `delete`) on the specified resource (like node or deployment). You can use `--help` after the subcommand to get additional info about possible parameters (for example: `kubectl get nodes --help`).
* Check that kubectl is configured to talk to your cluster, by running the `kubectl version` command.
* To view the nodes in the cluster, run the `kubectl get nodes` command.

#### Deploy an App
* `kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1`
* Great! You just deployed your first application by creating a deployment. This performed a few things for you:
	* searched for a suitable node where an instance of the application could be run (we have only 1 available node)
	* scheduled the application to run on that Node
	* configured the cluster to reschedule the instance on a new Node when needed

##### View the App
* Pods that are running inside Kubernetes are running on a private, isolated network. By default they are visible from other pods and services within the same Kubernetes cluster, but not outside that network. When we use kubectl, we're interacting through an API endpoint to communicate with our application.
* We will cover other options on how to expose your application outside the Kubernetes cluster later, in [Module 4](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/).
* The `kubectl proxy` command can create a proxy that will forward communications into the cluster-wide, private network. The proxy can be terminated by pressing control-C and won't show any output while its running. You need to open a second terminal window to run the proxy.
	* We now have a connection between our host (the terminal) and the Kubernetes cluster. The proxy enables direct access to the API from these terminals.
	* You can see all those APIs hosted through the proxy endpoint. For example, we can query the version directly through the API using the curl command:
		* `curl http://localhost:8001/version`
* The API server will automatically create an endpoint for each pod, based on the pod name, that is also accessible through the proxy.
	* First we need to get the Pod name, and we'll store in the environment variable POD_NAME:
	```bash
	export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
	echo Name of the Pod: $POD_NAME
	```
	* You can access the Pod through the proxied API, by running:
	```bash
	curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/
	```
* In order for the new Deployment to be accessible without using the proxy, a Service is required which will be explained in [Module 4](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/).

## Explore Your App
### Viewing Pods and Nodes
> [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)

* Objectives
	* Learn about Kubernetes Pods.
	* Learn about Kubernetes Nodes.
	* Troubleshoot deployed applications.

#### Kubernetes Pods
* When you created a Deployment in Module [2](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/), Kubernetes created a **Pod** to host your application instance. A Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker), and some shared resources for those containers. Those resources include:
	* Shared storage, as Volumes
	* Networking, as a unique cluster IP address
	* Information about how to run each container, such as the container image version or specific ports to use
* A Pod models an application-specific "logical host" and can contain different application containers which are relatively tightly coupled. For example, a Pod might include both the container with your Node.js app as well as a different container that feeds the data to be published by the Node.js webserver. The containers in a Pod share an IP Address and port space, are always co-located and co-scheduled, and run in a shared context on the same Node.
* Pods are the atomic unit on the Kubernetes platform. When we create a Deployment on Kubernetes, that Deployment creates Pods with containers inside them (as opposed to creating containers directly). Each Pod is tied to the Node where it is scheduled, and remains there until termination (according to restart policy) or deletion. In case of a Node failure, identical Pods are scheduled on other available Nodes in the cluster.

![](https://d33wubrfki0l68.cloudfront.net/fe03f68d8ede9815184852ca2a4fd30325e5d15a/98064/docs/tutorials/kubernetes-basics/public/images/module_03_pods.svg)

#### Nodes
* A Pod always runs on a Node. A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the control plane.
* A Node can have multiple pods, and the Kubernetes control plane automatically handles scheduling the pods across the Nodes in the cluster. The control plane's automatic scheduling takes into account the available resources on each Node.
* Every Kubernetes Node runs at least:
	* Kubelet, a process responsible for communication between the Kubernetes control plane and the Node; it manages the Pods and the containers running on a machine.
	* A container runtime (like Docker) responsible for pulling the container image from a registry, unpacking the container, and running the application.
![](https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg)

#### Troubleshooting with Kubectl
* The most common operations can be done with the following kubectl subcommands:
	* `kubectl get` - list resources
	* `kubectl describe` - show detailed information about a resource
	* `kubectl logs` - print the logs from a container in a pod
	* `kubectl exec` - execute a command on a container in a pod
##### Check application configuration
* Let's verify that the application we deployed in the previous scenario is running. We'll use the `kubectl` get command and look for existing Pods:
	* `kubectl get pods`
	* If no pods are running, please wait a couple of seconds and list the Pods again. You can continue once you see one Pod running.
* Next, to view what containers are inside that Pod and what images are used to build those containers we run the kubectl describe pods command:
	* `kubectl describe pods`
	* We see here details about the Pod’s container: IP address, the ports used and a list of events related to the lifecycle of the Pod.
	* The output of the describe subcommand is extensive and covers some concepts that we didn’t explain yet, but don’t worry, they will become familiar by the end of this bootcamp.
	* Note: the describe subcommand can be used to get detailed information about most of the Kubernetes primitives, including Nodes, Pods, and Deployments. The describe output is designed to be human readable, not to be scripted against.

##### Show the app in the terminal
* Recall that Pods are running in an isolated, private network - so we need to proxy access to them so we can debug and interact with them. To do this, we'll use the `kubectl proxy` command to run a proxy in a second terminal.
	```bash
	kubectl proxy # on another terminal
	export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
	echo Name of the Pod: $POD_NAME
	curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
	```
	* The URL is the route to the API of the Pod.

##### View the container logs
* Anything that the application would normally send to standard output becomes logs for the container within the Pod. We can retrieve these logs using the kubectl logs command:
	* `kubectl logs "$POD_NAME"`
	* Note: We don't need to specify the container name, because we only have one container inside the pod.

##### Executing command on the container
* We can execute commands directly on the container once the Pod is up and running. For this, we use the `exec` subcommand and use the name of the Pod as a parameter.
	* `kubectl exec "$POD_NAME" -- env`

## Expose your App Publicly
### Using a Service to Expose your App
> [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)

* Objectives
	* Learn about a Service in Kubernetes
	* Understand how labels and selectors relate to a Service
	* Expose an application outside a Kubernetes cluster using a Service

#### Overview of Kubernetes Services
* Kubernetes [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) are mortal. Pods have a [lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/). When a worker node dies, the Pods running on the Node are also lost. A [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) might then dynamically drive the cluster back to the desired state via the creation of new Pods to keep your application running. As another example, consider an image-processing backend with 3 replicas. Those replicas are exchangeable; the front-end system should not care about backend replicas or even if a Pod is lost and recreated. That said, each Pod in a Kubernetes cluster has a unique IP address, even Pods on the same Node, so there needs to be a way of automatically reconciling changes among Pods so that your applications continue to function.
* A Service in Kubernetes is an abstraction which defines a logical set of Pods and a policy by which to access them. Services enable a loose coupling between dependent Pods. A Service is defined using YAML or JSON, like all Kubernetes object manifests. The set of Pods targeted by a Service is usually determined by a label selector (see below for why you might want a Service without including a selector in the spec).
* Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. Services allow your applications to receive traffic. Services can be exposed in different ways by specifying a `type` in the spec of the Service:
	* `ClusterIP` (default) - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
	* `NodePort` - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`. Superset of *ClusterIP*.
	* `LoadBalancer` - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of *NodePort*.
	* `ExternalName` - Maps the Service to the contents of the externalName field (e.g. `foo.bar.example.com`), by returning a CNAME record with its value. No proxying of any kind is set up. This type requires v1.7 or higher of kube-dns, or CoreDNS version 0.0.8 or higher.
* More information about the different types of Services can be found in the [Using Source IP](https://kubernetes.io/docs/tutorials/services/source-ip/) tutorial. Also see [Connecting Applications with Services](https://kubernetes.io/docs/tutorials/services/connect-applications-service/).
* Additionally, note that there are some use cases with Services that involve not defining a `selector` in the spec. A Service created without `selector` will also not create the corresponding Endpoints object. This allows users to manually map a Service to specific endpoints. Another possibility why there may be no selector is you are strictly using `type: ExternalName`.

#### Services and Labels
* A Service routes traffic across a set of Pods. Services are the abstraction that allows pods to die and replicate in Kubernetes without impacting your application. Discovery and routing among dependent Pods (such as the frontend and backend components in an application) are handled by Kubernetes Services.
* Services match a set of Pods using [labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels), a grouping primitive that allows logical operation on objects in Kubernetes. Labels are key/value pairs attached to objects and can be used in any number of ways:
	* Designate objects for development, test, and production
	* Embed version tags
	* Classify an object using tags

![](https://d33wubrfki0l68.cloudfront.net/7a13fe12acc9ea0728460c482c67e0eb31ff5303/2c8a7/docs/tutorials/kubernetes-basics/public/images/module_04_labels.svg)

* Labels can be attached to objects at creation time or later on. They can be modified at any time.

##### Create a new Service
* `kubectl get services`
* We have a Service called kubernetes that is created by default when minikube (kubespray was the same) starts the cluster. 
* To create a new service and expose it to external traffic we'll use the expose command with NodePort as parameter.
	* `kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080`
	* `kctl get services`
	* We have now a running Service called kubernetes-bootcamp. Here we see that the Service received a unique cluster-IP, an internal port and an external-IP (the IP of the Node).
* To find out what port was opened externally (for the type: NodePort Service) we’ll run the `describe service` subcommand:
	* `kubectl describe services/kubernetes-bootcamp`
* Create an environment variable called `NODE_PORT` that has the value of the Node port assigned:
	```bash
	export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
	echo "NODE_PORT=$NODE_PORT"
	```
	* Now we can test that the app is exposed outside of the cluster using curl, the IP address of the Node and the externally exposed port:
		* `curl http://"$(minikube ip):$NODE_PORT"`

##### Using Labels
* The Deployment created automatically a label for our Pod. With the `describe deployment` subcommand you can see the name (the key) of that label:
	* `kubectl describe deployment kubernetes-bootcamp`
	* Let’s use this label to query our list of Pods.
	* `kubectl get pods -l app=kubernetes-bootcamp`
	* You can do the same to list the existing Services:
	* `kubectl get service -l app=kubernetes-bootcamp`
* Get the name of the Pod and store it in the `POD_NAME` environment variable:
	```bash
	export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
	echo "Name of the Pod: $POD_NAME"
	```
	* To apply a new label we use the `label` subcommand followed by the object type, object name and the new label.
	* `kubectl label pods "$POD_NAME" version=v1`
	* `kubectl describe pods "$POD_NAME"`
	* `kubectl get pods -l version=v1`

#### Deleting a Service
* To delete Services you can use the `delete service` subcommand. Labels can be used also here:
	* `kubectl delete service -l app=kubernetes-bootcamp`
	* to confirm: `kubectl get services`
	* to confirm route exposure: `curl http://"$(minikube ip):$NODE_PORT"`
	* confirm app running: `kubectl exec -ti $POD_NAME -- curl http://localhost:8080`
	* We see here that the application is up. This is because the Deployment is managing the application. To shut down the application, you would need to delete the Deployment as well.

## Scale your App
### Running Multiple Instances of your App
> [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/)

* Objectives
	* Scale an app using kubectl

#### Scaling an application
* Previously we created a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), and then exposed it publicly via a [Service](https://kubernetes.io/docs/concepts/services-networking/service/). The Deployment created only one Pod for running our application. When traffic increases, we will need to scale the application to keep up with user demand.
* Scaling is accomplished by changing the number of replicas in a Deployment.

![](https://d33wubrfki0l68.cloudfront.net/30f75140a581110443397192d70a4cdb37df7bfc/b5f56/docs/tutorials/kubernetes-basics/public/images/module_05_scaling2.svg)

* Scaling out a Deployment will ensure new Pods are created and scheduled to Nodes with available resources. Scaling will increase the number of Pods to the new desired state. Kubernetes also supports [autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) of Pods, but it is outside of the scope of this tutorial. Scaling to zero is also possible, and it will terminate all Pods of the specified Deployment.
* Running multiple instances of an application will require a way to distribute the traffic to all of them. **Services have an integrated load-balancer** that will distribute network traffic to all Pods of an exposed Deployment. Services will monitor continuously the running Pods using endpoints, to ensure the traffic is sent only to available Pods.
* Once you have multiple instances of an application running, you would be able to do Rolling updates without downtime. We'll cover that in the next section of the tutorial.

#### Scaling a Deployment
* `kubectl get deployments`
	```text
	NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
	kubernetes-bootcamp   1/1     1            1           11m
	```
	* We should have 1 Pod. If not, run the command again. This shows:
		* *NAME* lists the names of the Deployments in the cluster.
		* *READY* shows the ratio of CURRENT/DESIRED replicas
		* *UP-TO-DATE* displays the number of replicas that have been updated to achieve the desired state.
		* *AVAILABLE* displays how many replicas of the application are available to your users.
		* *AGE* displays the amount of time that the application has been running.
* To see the ReplicaSet created by the Deployment, run `kubectl get rs`.
	* Notice that the name of the ReplicaSet is always formatted as `[DEPLOYMENT-NAME]-[RANDOM-STRING]`. The random string is randomly generated and uses the *pod-template-hash* as a seed.
* Two important columns of this output are:
	* *DESIRED* displays the desired number of replicas of the application, which you define when you create the Deployment. This is the desired state.
	* *CURRENT* displays how many replicas are currently running.
* Next, let’s scale the Deployment to 4 replicas.
	* `kubectl scale deployments/kubernetes-bootcamp --replicas=4`
	* `kubectl get deployments`
	* `kubectl get pods -l app=kubernetes-bootcamp -o wide`

#### Load Balancing
* Let's check that the Service is load-balancing the traffic. To find out the exposed IP and Port we can use the describe service as we learned in the previous part of the tutorial:
	* `kubectl describe services/kubernetes-bootcamp`
* Create an environment variable called NODE_PORT that has a value as the Node port:
	```bash
	export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
	echo NODE_PORT=$NODE_PORT
	curl http://"$(minikube ip):$NODE_PORT" # run mutiple times
	```
	* Running `curl` multiple times hits multiple pods. This demonstrates that load balancing is working.

#### Scaling Down
* To scale down the Deployment to 2 replicas, run again the scale subcommand:
	* `kubectl scale deployments/kubernetes-bootcamp --replicas=2`
	* `kubectl get pods -l app=kubernetes-bootcamp -o wide`

## Update your App
### Performing a Rolling Update
> [source](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

* Objectives
	* Perform a rolling update using kubectl

#### Updating an application
* Users expect applications to be available all the time and developers are expected to deploy new versions of them several times a day. In Kubernetes this is done with rolling updates. Rolling updates allow Deployments' update to take place with zero downtime by incrementally updating Pods instances with new ones. The new Pods will be scheduled on Nodes with available resources.
* In the previous module we scaled our application to run multiple instances. This is a requirement for performing updates without affecting application availability. **By default**, the maximum number of Pods that can be unavailable during the update and the maximum number of new Pods that can be created, is one. **Both options can be configured to either numbers or percentages (of Pods).** In Kubernetes, updates are versioned and any Deployment update can be reverted to a previous (stable) version.

![](https://d33wubrfki0l68.cloudfront.net/6d8bc1ebb4dc67051242bc828d3ae849dbeedb93/fbfa8/docs/tutorials/kubernetes-basics/public/images/module_06_rollingupdates4.svg)

* Similar to application Scaling, if a Deployment is exposed publicly, the Service will load-balance the traffic only to available Pods during the update. An available Pod is an instance that is available to the users of the application.
* Rolling updates allow the following actions:
	* Promote an application from one environment to another (via container image updates)
	* Rollback to previous versions
	* Continuous Integration and Continuous Delivery of applications with zero downtime

#### Update the version of the app
* `kubectl get deployments`
* `kubectl get pods`
* To view the current image version of the app, run the `describe pods` subcommand and look for the `Image` field.
* To update the image of the application to version 2, use the set image subcommand, followed by the deployment name and the new image version:
	* `kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2`
	* The command notified the Deployment to use a different image for your app and initiated a rolling update. Check the status of the new Pods, and view the old one terminating with `kubectl get pods`.

#### Verify an update
```bash
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"
curl http://"$(minikube ip):$NODE_PORT"
```
* Every time you run the curl command, you will hit a different Pod. Notice that all Pods are now running the latest version (v2).
* You can also confirm the update by running the rollout status subcommand:
	* `kubectl rollout status deployments/kubernetes-bootcamp`

#### Roll back an update
* `kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10`
* `kubectl get deployments`
* Notice that the output doesn't list the desired number of available Pods. Run `kubectl get pods` to list all Pods.
* Notice that some of the Pods have a status of **ImagePullBackOff**.
* To get more insight into the problem, run `kubectl describe pods`.
* In the `Events` section of the output for the affected Pods, notice that the v10 image version did not exist in the repository.
* To roll back the deployment to your last working version, use the rollout undo subcommand:
	* `kubectl rollout undo deployments/kubernetes-bootcamp`
	* The `rollout undo` command reverts the deployment to the previous known state (v2 of the image). Updates are versioned and you can revert to any previously known state of a Deployment.
* Remember to clean up your local cluster
	* `kubectl delete deployments/kubernetes-bootcamp services/kubernetes-bootcamp`