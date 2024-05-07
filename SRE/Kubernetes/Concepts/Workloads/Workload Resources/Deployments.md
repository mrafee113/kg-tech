> [source](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

* A Deployment provides declarative updates for [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) and [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/).
* You describe a desired state in a Deployment, and the Deployment [Controller](https://kubernetes.io/docs/concepts/architecture/controller/) changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

> [!Note]
> Do not manage ReplicaSets owned by a Deployment.

### Use case
* [Create a Deployment to rollout a ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment). The ReplicaSet creates Pods in the background. Check the status of the rollout to see if it succeeds or not.
* [Declare the new state of the Pods](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment) by updating the PodTemplateSpec of the Deployment. A new ReplicaSet is created and the Deployment manages moving the Pods from the old ReplicaSet to the new one at a controlled rate. Each new ReplicaSet updates the revision of the Deployment.
* [Rollback to an earlier Deployment revision](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment) if the current state of the Deployment is not stable. Each rollback updates the revision of the Deployment.
* [Scale up the Deployment to facilitate more load](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#scaling-a-deployment).
* [Pause the rollout of a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#pausing-and-resuming-a-deployment) to apply multiple fixes to its PodTemplateSpec and then resume it to start a new rollout.
* [Use the status of the Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#deployment-status) as an indicator that a rollout has stuck.
* [Clean up older ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#clean-up-policy) that you don't need anymore.

### Creating a deployment
* In a deployment yaml file, the `.spec.selector` field defines how the created ReplicaSet finds which Pods to manage. In some cases, you select a label that is defined in the Pod template. However, more sophisticated selection rules are possible, *as long as the Pod template itself satisfies the rule*.

> [!Note]
> The `.spec.selector.matchLabels` field is a map of `{key,value}` pairs. A single `{key,value}` in the `matchLabels` map is equivalent to an element of `matchExpressions`, whose key field is `key`, the operator is `In`, and the values array contains only `value`. All of the requirements, from both `matchLabels` and `matchExpressions`, must be satisfied in order to match.

* To see the Deployment run `kubectl get deployments/<deployment-name>`
	* When you inspect the Deployments in your cluster, the following fields are displayed:
		* `NAME` lists the names of the Deployments in the namespace.
		* `READY` displays how many replicas of the application are available to your users. It follows the pattern ready/desired.
		* `UP-TO-DATE` displays the number of replicas that have been updated to achieve the desired state.
		* `AVAILABLE` displays how many replicas of the application are available to your users.
		* `AGE` displays the amount of time that the application has been running.
* To see the Deployments rollout status, run `kubectl rollout status deployment/<deployment-name>`.
* To see the ReplicaSet(s) created by the Deployment, run `kubectl get rs`. 
	* ReplicaSet output shows the following fields:
		* `NAME` lists the names of the ReplicaSets in the namespace. Notice that the name of the ReplicaSet is always formatted as `[DEPLOYMENT-NAME]-[HASH]`. This name will become the basis for the Pods which are created. The `HASH` string is the same as the `pod-template-hash` label on the ReplicaSet.
		* `DESIRED` displays the desired number of replicas of the application, which you define when you create the Deployment. This is the desired state.
		* `CURRENT` displays how many replicas are currently running.
		* `READY` displays how many replicas of the application are available to your users.
		* `AGE` displays the amount of time that the application has been running.
* To see the labels automatically generated for each Pod, run `kubectl get pods --show-labels`.

> [!Tip]
> Do not overlap labels or selectors with other controllers (including other Deployments and StatefulSets). Kubernetes doesn't stop you from overlapping, and if multiple controllers have overlapping selectors those controllers might conflict and behave unexpectedly.

### Updating a deployment

> [!Note]
> A Deployment's rollout is triggered if and only if the Deployment's Pod template (that is, `.spec.template`) is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

* Deployment ensures that only a certain number of Pods are down while they are being updated. By default, it ensures that at least 75% of the desired number of Pods are up (25% max unavailable).
* Deployment also ensures that only a certain number of Pods are created above the desired number of Pods. By default, it ensures that at most 125% of the desired number of Pods are up (25% max surge).

> [!Note]
> Kubernetes doesn't count terminating Pods when calculating the number of `availableReplicas`, which must be between `replicas - maxUnavailable` and `replicas + maxSurge`. As a result, you might notice that there are more Pods than expected during a rollout, and that the total resources consumed by the Deployment is more than `replicas + maxSurge` until the `terminationGracePeriodSeconds` of the terminating Pods expires.

#### Rollover
* Rollover is also known as multiple updates in-flight
* Each time a new Deployment is observed by the Deployment controller, a ReplicaSet is created to bring up the desired Pods. If the Deployment is updated, the existing ReplicaSet that controls Pods whose labels match `.spec.selector` but whose template does not match `.spec.template` are scaled down. Eventually, the new ReplicaSet is scaled to `.spec.replicas` and all old ReplicaSets is scaled to 0.
* If you update a Deployment while an existing rollout is in progress, the Deployment creates a new ReplicaSet as per the update and start scaling that up, and rolls over the ReplicaSet that it was scaling up previously -- it will add it to its list of old ReplicaSets and start scaling it down.
* For example, suppose you create a Deployment to create 5 replicas of `nginx:1.14.2`, but then update the Deployment to create 5 replicas of `nginx:1.16.1`, when only 3 replicas of `nginx:1.14.2` had been created. In that case, the Deployment immediately starts killing the 3 `nginx:1.14.2` Pods that it had created, and starts creating `nginx:1.16.1` Pods. It does not wait for the 5 replicas of `nginx:1.14.2` to be created before changing course.

### Rolling back a deployment
* Sometimes, you may want to rollback a Deployment; for example, when the Deployment is not stable, such as crash looping. By default, all of the Deployment's rollout history is kept in the system so that you can rollback anytime you want (you can change that by modifying revision history limit).

> [!Note]
> A Deployment's revision is created when a Deployment's rollout is triggered. This means that the new revision is created if and only if the Deployment's Pod template (`.spec.template`) is changed, for example if you update the labels or container images of the template. Other updates, such as scaling the Deployment, do not create a Deployment revision, so that you can facilitate simultaneous manual- or auto-scaling. This means that when you roll back to an earlier revision, only the Deployment's Pod template part is rolled back.

> [!Note]
>  The Deployment controller stops the bad rollout automatically, and stops scaling up the new ReplicaSet. This depends on the `rollingUpdate` parameters (`maxUnavailable` specifically) that you have specified. Kubernetes by default sets the value to 25%.

#### Checking rollout history of a deployment
* Check the revisions of the deployment: `kubectl rollout history deployment/<deployment-name>`
* To see the details of each revision: `kubectl rollout history deployment/<deployment-name> --revision=<rev-id>`

#### Rolling back to a previous revision
* To roll back one revision: `kubectl rollout undo deployment/<deployment-name>`
* To roll back to a specific revision: `kubectl rollout undo deployment/<deployment-name> --revision=<rev-id>`
* For more details about rollout related commands, read [`kubectl rollout`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout).

### Scaling a deployment
* `kubectl scale deployment/<deployment-name> --replicas=[number]`
* Assuming [horizontal Pod autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) is enabled in your cluster, you can set up an autoscaler for your Deployment and choose the minimum and maximum number of Pods you want to run based on the CPU utilization of your existing Pods.
	* `kubectl autoscale deployment/<deployment-name> --min=[number] --max=[number] --cpu-percent=[number]`

#### Proportional scaling
* RollingUpdate Deployments support running multiple versions of an application at the same time. When you or an autoscaler scales a RollingUpdate Deployment that is in the middle of a rollout (either in progress or paused), the Deployment controller balances the additional replicas in the existing active ReplicaSets (ReplicaSets with Pods) in order to mitigate risk. This is called proportional scaling.

> [!Warning]
> I did not understand the example from the docs, so I asked ChatGPT.

Here's a step-by-step explanation based on the documentation you provided:
1. **Initial Deployment**:
   - You start with a Deployment that has 10 replicas. This means you have 10 identical Pods running your application.
   - You have specified `maxSurge=3` and `maxUnavailable=2` as part of your Deployment configuration. These settings control how many new replicas can be created and how many old replicas can be unavailable during the rolling update.
2. **Image Update**:
   - You decide to update the Docker image used by your Deployment to a new version. You use `kubectl set image` to trigger this update.
   - Kubernetes starts a new rollout, creating a new ReplicaSet (e.g., `nginx-deployment-1989198191`) with the updated image.
   - However, the rollout is blocked because of the `maxUnavailable` setting, which ensures that there are no more than 2 unavailable Pods at any given time.
3. **Scaling Request**:
   - While the rollout is in progress, a scaling request is initiated, and the autoscaler increases the number of replicas to 15. This means you want a total of 15 Pods running your application.
4. **Proportional Scaling**:
   - This is where proportional scaling comes into play. Instead of adding all 5 new replicas to the new ReplicaSet (`nginx-deployment-1989198191`), Kubernetes spreads the new replicas across both the old and new ReplicaSets.
   - In your example, 3 replicas are added to the old ReplicaSet (`nginx-deployment-618515232`), and 2 replicas are added to the new ReplicaSet (`nginx-deployment-1989198191`).
   - The decision on how many replicas go where is based on proportions. More replicas are added to the ReplicaSet with more existing replicas (bigger proportions), while fewer replicas are added to the new ReplicaSet (lower proportions).
   - The intention is to minimize the disruption caused by the update by gradually moving traffic from the old ReplicaSet to the new one.
5. **Rollout Progress**:
   - Over time, as the new replicas become healthy and ready, the rollout process moves all replicas to the new ReplicaSet (`nginx-deployment-1989198191`).
   - Eventually, you reach the desired state, which is 15 replicas of your application.
6. **Final State**:
   - When the rollout is complete, you can verify the status using `kubectl get deploy` and `kubectl get rs` commands.
   - The `kubectl get deploy` command shows the desired, current, up-to-date, and available replicas, giving you an overview of the Deployment's state.

In summary, proportional scaling is a mechanism that helps distribute new replicas across both old and new ReplicaSets during a rolling update, helping to ensure a smooth and gradual transition to the updated version of your application while adhering to specified availability constraints.

### Pausing and resuming a rollout of a deployment
* When you update a Deployment, or plan to, you can pause rollouts for that Deployment before you trigger one or more updates. When you're ready to apply those changes, you resume rollouts for the Deployment. This approach allows you to apply multiple fixes in between pausing and resuming without triggering unnecessary rollouts.
* pause: `kubectl rollout pause deployment/<deployment-name>`
	* When paused, if you update the deployment, no revisions will be created. You can update as many times as you want. The initial state of the Deployment prior to pausing its rollout will continue its function, but new updates to the Deployment will not have any effect as long as the Deployment rollout is paused.
* resume: `kubectl rollout deployment/<deployment-name>`

> [!Note]
> You cannot rollback a paused Deployment until you resume it.

### Deployment status
* A Deployment enters various states during its lifecycle. It can be [progressing](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#progressing-deployment) while rolling out a new ReplicaSet, it can be [complete](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#complete-deployment), or it can [fail to progress](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#failed-deployment).

#### Progressing deployment
* Kubernetes marks a Deployment as progressing when one of the following tasks is performed:
	* The Deployment creates a new ReplicaSet.
	* The Deployment is scaling up its newest ReplicaSet.
	* The Deployment is scaling down its older ReplicaSet(s).
	* New Pods become ready or available (ready for at least [MinReadySeconds](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#min-ready-seconds)).
* When the rollout becomes “progressing”, the Deployment controller adds a condition with the following attributes to the Deployment's `.status.conditions`:
	* `type: Progressing`
	* `status: "True"`
	* `reason: NewReplicaSetsCreated` | `reason: FoundNewReplicaSet` | `reason: ReplicaSetUpdated`
* You can monitor the progress for a Deployment by using kubectl `rollout status`.

#### Complete deployment
* Kubernetes marks a Deployment as complete when it has the following characteristics:
	* All of the replicas associated with the Deployment have been updated to the latest version you've specified, meaning any updates you've requested have been completed.
	* All of the replicas associated with the Deployment are available.
	* No old replicas for the Deployment are running.
* When the rollout becomes “complete”, the Deployment controller sets a condition with the following attributes to the Deployment's `.status.conditions`:
	* `type: Progressing`
	* `status: "True"`
	* `reason: NewReplicaSetAvailable`
* This Progressing condition will retain a status value of "True" until a new rollout is initiated. The condition holds even when availability of replicas changes (which does instead affect the `Available` condition).
* You can check if a Deployment has completed by using `kubectl rollout status`. If the rollout completed successfully, `kubectl rollout status` returns a zero exit code.

#### Failed deployment
* Your Deployment may get stuck trying to deploy its newest ReplicaSet without ever completing. This can occur due to some of the following factors:
	* Insufficient quota
	* Readiness probe failures
	* Image pull errors
	* Insufficient permissions
	* Limit ranges
	* Application runtime misconfiguration
* One way you can detect this condition is to specify a deadline parameter in your Deployment spec: ([`.spec.progressDeadlineSeconds`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#progress-deadline-seconds)). It denotes the number of seconds the Deployment controller waits before indicating (in the Deployment status) that the Deployment progress has stalled.
* Once the deadline has been exceeded, the Deployment controller adds a DeploymentCondition with the following attributes to the Deployment's `.status.conditions`:
	* `type: Progressing`
	* `status: False`
	* `reason: ProgressDeadlineExceeded`
* This condition can also fail early and is then set to status value of "False" due to reasons as `ReplicaSetCreateError`. Also, the deadline is not taken into account anymore once the Deployment rollout completes.
* See the [Kubernetes API conventions](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#typical-status-properties) for more information on status conditions.

> [!Note]
> Kubernetes takes no action on a stalled Deployment other than to report a status condition with reason: `ProgressDeadlineExceeded`. Higher level orchestrators can take advantage of it and act accordingly, for example, rollback the Deployment to its previous version.

> [!Note]
> If you pause a Deployment rollout, Kubernetes does not check progress against your specified deadline. You can safely pause a Deployment rollout in the middle of a rollout and resume without triggering the condition for exceeding the deadline.

### Clean up policy
* You can set `.spec.revisionHistoryLimit` field in a Deployment to specify how many old ReplicaSets for this Deployment you want to retain. The rest will be garbage-collected in the background. By default, it is 10.

> [!Note]
> Explicitly setting this field to 0, will result in cleaning up all the history of your Deployment thus that Deployment will not be able to roll back.

### Canary deployment
If you want to roll out releases to a subset of users or servers using the Deployment, you can create multiple Deployments, one for each release, following the canary pattern described in [managing resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#canary-deployments).

### Writing a deployment spec
#### Pod template
* The `.spec.template` and `.spec.selector` are the only required fields of the `.spec`.
* In addition to required fields for a Pod, a Pod template in a Deployment must specify appropriate labels and an appropriate restart policy. For labels, make sure not to overlap with other controllers. See [selector](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#selector).
* Only a `.spec.template.spec.restartPolicy` equal to `Always` is allowed, which is the default if not specified.

#### Replicas
* `.spec.replicas` is an optional field that specifies the number of desired Pods. It defaults to 1.
* If a [HorizontalPodAutoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (or any similar API for horizontal scaling) is managing scaling for a Deployment, don't set `.spec.replicas`.
	* Instead, allow the Kubernetes [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) to manage the `.spec.replicas` field automatically.

#### Selector
* `.spec.selector` is a required field that specifies a label selector for the Pods targeted by this Deployment.
* `.spec.selector` must match `.spec.template.metadata.labels`, or it will be rejected by the API.
* A Deployment may terminate Pods whose labels match the selector if their template is different from `.spec.template` or if the total number of such Pods exceeds `.spec.replicas`. It brings up new Pods with `.spec.template` if the number of Pods is less than the desired number.

> [!Note]
> You should not create other Pods whose labels match this selector, either directly, by creating another Deployment, or by creating another controller such as a ReplicaSet or a ReplicationController. If you do so, the first Deployment thinks that it created these other Pods. Kubernetes does not stop you from doing this.

* If you have multiple controllers that have overlapping selectors, the controllers will fight with each other and won't behave correctly.

#### Strategy
* `.spec.strategy` specifies the strategy used to replace old Pods by new ones.
* `.spec.strategy.type` can be "Recreate" or "RollingUpdate". "RollingUpdate" is the default value.

##### Recreate deployment
* All existing Pods are killed before new ones are created when `.spec.strategy.type==Recreate`.

> [!Note]
> This will only guarantee Pod termination previous to creation for upgrades. If you upgrade a Deployment, all Pods of the old revision will be terminated immediately. Successful removal is awaited before any Pod of the new revision is created. If you manually delete a Pod, the lifecycle is controlled by the ReplicaSet and the replacement will be created immediately (even if the old Pod is still in a Terminating state). If you need an "at most" guarantee for your Pods, you should consider using a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

##### Rolling update deployment
* The Deployment updates Pods in a rolling update fashion when `.spec.strategy.type==RollingUpdate`. You can specify `maxUnavailable` and `maxSurge` to control the rolling update process.
* **Max Unavailable**: `.spec.strategy.rollingUpdate.maxUnavailable` is an optional field that specifies the maximum number of Pods that can be unavailable during the update process. The value can be an absolute number (for example, 5) or a percentage of desired Pods (for example, 10%). The absolute number is calculated from percentage by *rounding down*. The value cannot be 0 if `.spec.strategy.rollingUpdate.maxSurge` is 0. The default value is 25%.
* **Max Surge**: `.spec.strategy.rollingUpdate.maxSurge` is an optional field that specifies the maximum number of Pods that can be created over the desired number of Pods. The value can be an absolute number (for example, 5) or a percentage of desired Pods (for example, 10%). The value cannot be 0 if `MaxUnavailable` is 0. The absolute number is calculated from the percentage by *rounding up*. The default value is 25%.

#### Progress deadline seconds
* `.spec.progressDeadlineSeconds` is an optional field that specifies the number of seconds you want to wait for your Deployment to progress before the system reports back that the Deployment has failed progressing - surfaced as a condition with `type: Progressing`, `status: "False"`. and `reason: ProgressDeadlineExceeded` in the status of the resource. The Deployment controller will keep retrying the Deployment. This defaults to 600. In the future, once automatic rollback will be implemented, the Deployment controller will roll back a Deployment as soon as it observes such a condition.
* If specified, this field needs to be greater than `.spec.minReadySeconds`.

#### Min ready seconds
`.spec.minReadySeconds` is an optional field that specifies the minimum number of seconds for which a newly created Pod should be ready without any of its containers crashing, for it to be considered available. This defaults to 0 (the Pod will be considered available as soon as it is ready). To learn more about when a Pod is considered ready, see [Container Probes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes).

#### Revision history limit
* A Deployment's revision history is stored in the ReplicaSets it controls.
* `.spec.revisionHistoryLimit` is an optional field that specifies the number of old ReplicaSets to retain to allow rollback. These old ReplicaSets consume resources in etcd and crowd the output of `kubectl get rs`. The configuration of each Deployment revision is stored in its ReplicaSets; therefore, once an old ReplicaSet is deleted, you lose the ability to rollback to that revision of Deployment. By default, 10 old ReplicaSets will be kept, however its ideal value depends on the frequency and stability of new Deployments.
* More specifically, setting this field to zero means that all old ReplicaSets with 0 replicas will be cleaned up. In this case, a new Deployment rollout cannot be undone, since its revision history is cleaned up.

#### Paused
* `.spec.paused` is an optional boolean field for pausing and resuming a Deployment. The only difference between a paused Deployment and one that is not paused, is that any changes into the PodTemplateSpec of the paused Deployment will not trigger new rollouts as long as it is paused. A Deployment is not paused by default when it is created.