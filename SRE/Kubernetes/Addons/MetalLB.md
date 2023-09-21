> [metallb.univers.tf](https://metallb.universe.tf/)

### Why?
* Kubernetes does not offer an implementation of network load balancers (Services of type LoadBalancer) for bare-metal clusters. The implementations of network load balancers that Kubernetes does ship with are all glue code that calls out to various IaaS platforms (GCP, AWS, Azure…). If you’re not running on a supported IaaS platform (GCP, AWS, Azure…), LoadBalancers will remain in the “pending” state indefinitely when created.
* Bare-metal cluster operators are left with two lesser tools to bring user traffic into their clusters, “NodePort” and “externalIPs” services. Both of these options have significant downsides for production use, which makes bare-metal clusters second-class citizens in the Kubernetes ecosystem.
* MetalLB aims to redress this imbalance by offering a network load balancer implementation that integrates with standard network equipment, so that external services on bare-metal clusters also “just work” as much as possible.

### Concepts
> [source](https://metallb.universe.tf/concepts/)

* MetalLB hooks into your Kubernetes cluster, and provides a network load-balancer implementation. In short, it allows you to create Kubernetes services of type LoadBalancer in clusters that don’t run on a cloud provider, and thus cannot simply hook into paid products to provide load balancers.

#### Address Allocation
* In a Kubernetes cluster on a cloud provider, you request a load balancer, and your cloud platform assigns an IP address to you. In a bare-metal cluster, MetalLB is responsible for that allocation.
* MetalLB cannot create IP addresses out of thin air, so you do have to give it pools of IP addresses that it can use. MetalLB will take care of assigning and unassigning individual addresses as services come and go, but it will only ever hand out IPs that are part of its configured pools.
* How you get IP address pools for MetalLB depends on your environment. If you’re running a bare-metal cluster in a colocation facility, your hosting provider probably offers IP addresses for lease. In that case, you would lease, say, a /26 of IP space (64 addresses), and provide that range to MetalLB for cluster services.
* Alternatively, your cluster might be purely private, providing services to a nearby LAN but not exposed to the internet. In that case, you could pick a range of IPs from one of the private address spaces (so-called RFC1918 addresses), and assign those to MetalLB. Such addresses are free, and work fine as long as you’re only providing cluster services to your LAN.
* Or, you could do both! MetalLB lets you define as many address pools as you want, and doesn’t care what “kind” of addresses you give it.

### Installation
> [source](https://metallb.universe.tf/installation/)

#### Manifest
* `kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.11/config/manifests/metallb-native.yaml`
* This will deploy MetalLB to your cluster, under the `metallb-system` namespace. The components in the manifest are:
	* The `metallb-system/controller` deployment. This is the cluster-wide controller that handles IP address assignments.
	* The `metallb-system/speaker` daemonset. This is the component that speaks the protocol(s) of your choice to make the services reachable.
	* Service accounts for the controller and speaker, along with the RBAC permissions that the components need to function.

### Configuration
> [source](https://metallb.universe.tf/configuration/)

#### Defining The IPs To Assign To The Load Balancer Services
* In order to assign an IP to the services, MetalLB must be instructed to do so via the `IPAddressPool` CR.
* All the IPs allocated via `IPAddressPools` contribute to the pool of IPs that MetalLB uses to assign IPs to services.
```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.168.10.0/24
  - 192.168.9.1-192.168.9.5
  - fc00:f853:0ccd:e799::/124
```
* Multiple instances of `IPAddressPool`s can co-exist and addresses can be defined by CIDR, by range, and both IPV4 and IPV6 addresses can be assigned.