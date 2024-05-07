> [source](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

* A Job creates one or more Pods and will continue to retry execution of the Pods until a specified number of them successfully terminate. As pods successfully complete, the Job tracks the successful completions. When a specified number of successful completions is reached, the task (i.e., Job) is complete. Deleting a Job will clean up the Pods it created. Suspending a Job will delete its active Pods until the Job is resumed again.
* A simple case is to create one Job object in order to reliably run one Pod to completion. The Job object will start a new Pod if the first Pod fails or is deleted (for example due to a node hardware failure or a node reboot).
* You can also use a Job to run multiple Pods in parallel.
* If you want to run a Job (either a single task, or several in parallel) on a schedule, see [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/).

### Writing a Job spec
* As with all other Kubernetes config, a Job needs `apiVersion`, `kind`, and `metadata` fields.
* A Job also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).
* **Job Labels**: Job labels will have `batch.kubernetes.io/` prefix for `job-name` and `controller-uid`.
* **Pod Template**
	* The `.spec.template` is the only required field of the `.spec`.
	* The `.spec.template` is a pod template. It has exactly the same schema as a Pod, except it is nested and does not have an `apiVersion` or kind.
	* In addition to required fields for a Pod, a pod template in a Job must specify appropriate labels (see [pod selector](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-selector)) and an appropriate restart policy.
	* Only a [`RestartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) equal to `Never` or `OnFailure` is allowed.
* **Pod Selector**: The `.spec.selector` field is optional. In almost all cases you should not specify it. See section [specifying your own pod selector](https://kubernetes.io/docs/concepts/workloads/controllers/job/#specifying-your-own-pod-selector).

#### Parallel execution for Jobs
* There are three main types of task suitable to run as a Job:
	1. Non-parallel Jobs
		* normally, only one Pod is started, unless the Pod fails.
		* the Job is complete as soon as its Pod terminates successfully.
	2. Parallel Jobs with a fixed completion count:
		* specify a non-zero positive value for `.spec.completions`.
		* the Job represents the overall task, and is complete when there are `.spec.completions` successful Pods.
		* when using `.spec.completionMode="Indexed"`, each Pod gets a different index in the range `0` to `.spec.completions-1`.
	3. Parallel Jobs with a *work queue*:
		* do not specify `.spec.completions`, default to `.spec.parallelism`.
		* the Pods must coordinate amongst themselves or an external service to determine what each should work on. For example, a Pod might fetch a batch of up to N items from the work queue.
		* each Pod is independently capable of determining whether or not all its peers are done, and thus that the entire Job is done.
		* when any Pod from the Job terminates with success, no new Pods are created.
		* once at least one Pod has terminated with success and all Pods are terminated, then the Job is completed with success.
		* once any Pod has exited with success, no other Pod should still be doing any work for this task or writing any output. They should all be in the process of exiting.
* For a non-parallel Job, you can leave both `.spec.completions` and `.spec.parallelism` unset. When both are unset, both are defaulted to 1.
* For a fixed completion count Job, you should set `.spec.completions` to the number of completions needed. You can set `.spec.parallelism`, or leave it unset and it will default to 1.
* For a *work queue* Job, you must leave `.spec.completions` unset, and set `.spec.parallelism` to a non-negative integer.
* For more information about how to make use of the different types of job, see the [job patterns](https://kubernetes.io/docs/concepts/workloads/controllers/job/#job-patterns) section.

##### Controlling Parallelism
* The requested parallelism (`.spec.parallelism`) can be set to any non-negative value. If it is unspecified, it defaults to 1. If it is specified as 0, then the Job is effectively paused until it is increased.
* Actual parallelism (number of pods running at any instant) may be more or less than requested parallelism, for a variety of reasons:
	* For *fixed completion count* Jobs, the actual number of pods running in parallel will not exceed the number of remaining completions. Higher values of `.spec.parallelism` are effectively ignored.
	* For *work queue* Jobs, no new Pods are started after any Pod has succeeded -- remaining Pods are allowed to complete, however.
	* If the Job [Controller](https://kubernetes.io/docs/concepts/architecture/controller/) has not had time to react.
	* If the Job controller failed to create Pods for any reason (lack of `ResourceQuota`, lack of permission, etc.), then there may be fewer pods than requested.
	* The Job controller may throttle new Pod creation due to excessive previous pod failures in the same Job.
	* When a Pod is gracefully shut down, it takes time to stop.

#### Completion mode
* Jobs with fixed completion count - that is, jobs that have non null `.spec.completions` - can have a completion mode that is specified in `.spec.completionMode`:
	* `NonIndexed` (default): the Job is considered complete when there have been `.spec.completions` successfully completed Pods. In other words, each Pod completion is homologous to each other. Note that Jobs that have null `.spec.completions` are implicitly `NonIndexed`.
	* `Indexed`: the Pods of a Job get an associated completion index from `0` to `.spec.completions-1`. The index is available through four mechanisms:
		* The Pod annotation `batch.kubernetes.io/job-completion-index`.
		* The Pod label `batch.kubernetes.io/job-completion-index`. Note the feature gate `PodIndexLabel` must be enabled to use this label, and it is enabled by default.
		* As part of the Pod hostname, following the pattern `$(job-name)-$(index)`. When you use an Indexed Job in combination with a [Service](https://kubernetes.io/docs/concepts/services-networking/service/), Pods within the Job can use the deterministic hostnames to address each other via DNS. For more information about how to configure this, see [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/).
		* From the containerized task, in the environment variable `JOB_COMPLETION_INDEX`.
	* The Job is considered complete when there is one successfully completed Pod for each index. For more information about how to use this mode, see Indexed Job for Parallel Processing with Static Work Assignment.

### Handling Pod and Container failures
* A container in a Pod may fail for a number of reasons, such as because the process in it exited with a non-zero exit code, or the container was killed for exceeding a memory limit, etc. If this happens, and the `.spec.template.spec.restartPolicy = "OnFailure"`, then the Pod stays on the node, but the container is re-run. Therefore, your program needs to handle the case when it is restarted locally, or else specify `.spec.template.spec.restartPolicy = "Never"`. See [pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#example-states) for more information on `restartPolicy`.
* An entire Pod can also fail, for a number of reasons, such as when the pod is kicked off the node (node is upgraded, rebooted, deleted, etc.), or if a container of the Pod fails and the `.spec.template.spec.restartPolicy = "Never"`. When a Pod fails, then the Job controller starts a new Pod. This means that your application needs to handle the case when it is restarted in a new pod. In particular, it needs to handle temporary files, locks, incomplete output and the like caused by previous runs.
* By default, each pod failure is counted towards the `.spec.backoffLimit` limit, see [pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy). However, you can customize handling of pod failures by setting the Job's [pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy).
* Additionally, you can choose to count the pod failures independently for each index of an [Indexed](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) Job by setting the `.spec.backoffLimitPerIndex` field (for more information, see [backoff limit per index](https://kubernetes.io/docs/concepts/workloads/controllers/job/#backoff-limit-per-index)).
* Note that even if you specify `.spec.parallelism = 1` and `.spec.completions = 1` and `.spec.template.spec.restartPolicy = "Never"`, the same program may sometimes be started twice.
* If you do specify `.spec.parallelism` and `.spec.completions` both greater than `1`, then there may be multiple pods running at once. Therefore, your pods must also be tolerant of concurrency.
* When the [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) `PodDisruptionConditions` and `JobPodFailurePolicy` are both enabled, and the `.spec.podFailurePolicy` field is set, the Job controller does not consider a terminating Pod (a pod that has a `.metadata.deletionTimestamp` field set) as a failure until that Pod is terminal (its `.status.phase` is `Failed` or `Succeeded`). However, the Job controller creates a replacement Pod as soon as the termination becomes apparent. Once the pod terminates, the Job controller evaluates `.backoffLimit` and `.podFailurePolicy` for the relevant Job, taking this now-terminated Pod into consideration.
* If either of these requirements is not satisfied, the Job controller counts a terminating Pod as an immediate failure, even if that Pod later terminates with phase: `"Succeeded"`.

#### Pod backoff failure policy
* There are situations where you want to fail a Job after some amount of retries due to a logical error in configuration etc. To do so, set `.spec.backoffLimit` to specify the number of retries before considering a Job as failed. The back-off limit is set by default to `6`. Failed Pods associated with the Job are recreated by the Job controller with an exponential back-off delay (10s, 20s, 40s ...) capped at six minutes.
* The number of retries is calculated in two ways:
	* The number of Pods with `.status.phase = "Failed"`.
	* When using `restartPolicy = "OnFailure"`, the number of retries in all the containers of Pods with `.status.phase` equal to `Pending` or `Running`.
* If either of the calculations reaches the `.spec.backoffLimit`, the Job is considered failed.

> [!Note]
> If your job has `restartPolicy = "OnFailure"`, keep in mind that your Pod running the Job will be terminated once the job backoff limit has been reached. This can make debugging the Job's executable more difficult. We suggest setting `restartPolicy = "Never"` when debugging the Job or using a logging system to ensure output from failed Jobs is not lost inadvertently.

#### Backoff limit per index
> [!Note]
> You can only configure the backoff limit per index for an [Indexed](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) Job, if you have the `JobBackoffLimitPerIndex` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) enabled in your cluster.

* When you run an [indexed](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) Job, you can choose to handle retries for pod failures independently for each index. To do so, set the `.spec.backoffLimitPerIndex` to specify the maximal number of pod failures per index.
* When the per-index backoff limit is exceeded for an index, Kubernetes considers the index as failed and adds it to the `.status.failedIndexes` field. The succeeded indexes, those with a successfully executed pods, are recorded in the `.status.completedIndexes` field, regardless of whether you set the `backoffLimitPerIndex` field.
* Note that a failing index does not interrupt execution of other indexes. Once all indexes finish for a Job where you specified a backoff limit per index, if at least one of those indexes did fail, the Job controller marks the overall Job as failed, by setting the Failed condition in the status. The Job gets marked as failed even if some, potentially nearly all, of the indexes were processed successfully.
* You can additionally limit the maximal number of indexes marked failed by setting the `.spec.maxFailedIndexes` field. When the number of failed indexes exceeds the `maxFailedIndexes` field, the Job controller triggers termination of all remaining running Pods for that Job. Once all pods are terminated, the entire Job is marked failed by the Job controller, by setting the Failed condition in the Job status.
* Additionally, you may want to use the per-index backoff along with a [pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy). When using per-index backoff, there is a new `FailIndex` action available which allows you to avoid unnecessary retries within an index.

#### Pod failure policy
> [!Note]
> You can only configure a Pod failure policy for a Job if you have the `JobPodFailurePolicy` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) enabled in your cluster. Additionally, it is recommended to enable the `PodDisruptionConditions` feature gate in order to be able to detect and handle Pod disruption conditions in the Pod failure policy (see also: [Pod disruption conditions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions#pod-disruption-conditions)).

* A Pod failure policy, defined with the `.spec.podFailurePolicy` field, enables your cluster to handle Pod failures based on the container exit codes and the Pod conditions.
* In some situations, you may want to have a better control when handling Pod failures than the control provided by the [Pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy), which is based on the Job's `.spec.backoffLimit`. These are some examples of use cases:
	* To optimize costs of running workloads by avoiding unnecessary Pod restarts, you can terminate a Job as soon as one of its Pods fails with an exit code indicating a software bug.
	* To guarantee that your Job finishes even if there are disruptions, you can ignore Pod failures caused by disruptions (such as [preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption), [API-initiated eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/) or [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)-based eviction) so that they don't count towards the `.spec.backoffLimit` limit of retries.
* You can configure a Pod failure policy, in the `.spec.podFailurePolicy` field, to meet the above use cases. This policy can handle Pod failures based on the container exit codes and the Pod conditions.
* The second rule of the Pod failure policy, specifying the `Ignore` action for failed Pods with condition `DisruptionTarget` excludes Pod disruptions from being counted towards the `.spec.backoffLimit` limit of retries.

> [!Note]
> If the Job failed, either by the Pod failure policy or Pod backoff failure policy, and the Job is running multiple Pods, Kubernetes terminates all the Pods in that Job that are still Pending or Running.

* These are some requirements and semantics of the API:
	* if you want to use a `.spec.podFailurePolicy` field for a Job, you must also define that Job's pod template with `.spec.restartPolicy` set to Never.
	* the Pod failure policy rules you specify under `spec.podFailurePolicy.rules` are evaluated in order. Once a rule matches a Pod failure, the remaining rules are ignored. When no rule matches the Pod failure, the default handling applies.
	* you may want to restrict a rule to a specific container by specifying its name `inspec.podFailurePolicy.rules[*].onExitCodes.containerName`. When not specified the rule applies to all containers. When specified, it should match one the container or `initContainer` names in the Pod template.
	* you may specify the action taken when a Pod failure policy is matched by `spec.podFailurePolicy.rules[*].action`. Possible values are:
		* `FailJob`: use to indicate that the Pod's job should be marked as Failed and all running Pods should be terminated.
		* `Ignore`: use to indicate that the counter towards the `.spec.backoffLimit` should not be incremented and a replacement Pod should be created.
		* `Count`: use to indicate that the Pod should be handled in the default way. The counter towards the `.spec.backoffLimit` should be incremented.
		* `FailIndex`: use this action along with backoff limit per index to avoid unnecessary retries within the index of a failed pod.

> [!Note]
> When you use a `podFailurePolicy`, the job controller only matches Pods in the `Failed` phase. Pods with a deletion timestamp that are not in a terminal phase (`Failed` or `Succeeded`) are considered still terminating. This implies that terminating pods retain a [tracking finalizer](https://kubernetes.io/docs/concepts/workloads/controllers/job/#job-tracking-with-finalizers) until they reach a terminal phase. Kubelet transitions deleted pods to a terminal phase (see: [Pod Phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)). This ensures that deleted pods have their finalizers removed by the Job controller.

> [!Note]
> When Pod failure policy is used, the Job controller recreates terminating Pods only once these Pods reach the terminal `Failed` phase. This behavior is similar to `podReplacementPolicy: Failed`. For more information, see [Pod replacement policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-replacement-policy).

#todo