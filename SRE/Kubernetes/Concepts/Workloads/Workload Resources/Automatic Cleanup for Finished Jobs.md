> [source](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)

* When your Job has finished, it's useful to keep that Job in the API (and not immediately delete the Job) so that you can tell whether the Job succeeded or failed.
* Kubernetes' TTL-after-finished [controller](https://kubernetes.io/docs/concepts/architecture/controller/) provides a TTL (time to live) mechanism to limit the lifetime of Job objects that have finished execution.

### Cleanup for finished Jobs
* The TTL-after-finished controller is only supported for Jobs. You can use this mechanism to clean up finished Jobs (either `Complete` or `Failed`) automatically by specifying the `.spec.ttlSecondsAfterFinished` field of a Job, as in this [example](https://kubernetes.io/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically).
* The TTL-after-finished controller assumes that a Job is eligible to be cleaned up TTL seconds after the Job has finished. The timer starts once the status condition of the Job changes to show that the Job is either `Complete` or `Failed`; once the TTL has expired, that Job becomes eligible for [cascading](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#cascading-deletion) removal. When the TTL-after-finished controller cleans up a job, it will delete it cascadingly, that is to say it will delete its dependent objects together with it.
* Kubernetes honors object lifecycle guarantees on the Job, such as waiting for [finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/).
* You can set the TTL seconds at any time. Here are some examples for setting the `.spec.ttlSecondsAfterFinished` field of a Job:
	* Specify this field in the Job manifest, so that a Job can be cleaned up automatically some time after it finishes.
	* Manually set this field of existing, already finished Jobs, so that they become eligible for cleanup.
	* Use a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) to set this field dynamically at Job creation time. Cluster administrators can use this to enforce a TTL policy for finished jobs.
	* Use a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) to set this field dynamically after the Job has finished, and choose different TTL values based on job status, labels. For this case, the webhook needs to detect changes to the `.status` of the Job and only set a TTL when the Job is being marked as completed.
	* Write your own controller to manage the cleanup TTL for Jobs that match a particular [selector-selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### Caveats
#### Updating TTL for finished Jobs
You can modify the TTL period, e.g. `.spec.ttlSecondsAfterFinished` field of Jobs, after the job is created or has finished. If you extend the TTL period after the existing `ttlSecondsAfterFinished` period has expired, Kubernetes doesn't guarantee to retain that Job, even if an update to extend the TTL returns a successful API response.

#### Time Skew
Because the TTL-after-finished controller uses timestamps stored in the Kubernetes jobs to determine whether the TTL has expired or not, this feature is sensitive to time skew in your cluster, which may cause the control plane to clean up Job objects at the wrong time.
Clocks aren't always correct, but the difference should be very small. Please be aware of this risk when setting a non-zero TTL.