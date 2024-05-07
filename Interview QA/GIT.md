1. What is Git, and why is it used in software development?
	Git is a distributed version control system that helps teams manage and track changes to source code and collaborate efficiently. It allows developers to work on the same project simultaneously, keeping track of changes, branching, and merging code. Git is crucial in software development to maintain version history, enable collaboration, and facilitate rollbacks if issues arise.
2. What is a Git repository?
	A Git repository is a directory that contains all the files, history, and metadata related to a project. It stores the complete history of changes made to the project's source code and allows users to collaborate, track changes, and manage different versions of the project.
3. Explain the difference between Git and GitHub.
	Git is a version control system, while GitHub is a web-based platform that provides hosting services for Git repositories. GitHub offers features like collaboration tools, issue tracking, pull requests, and a user-friendly interface to interact with Git repositories.
4. What is a Git branch?
	A Git branch is a separate line of development within a Git repository. It allows developers to work on features, bug fixes, or experiments independently without affecting the main codebase. Branches can later be merged back into the main branch (often called the "master" or "main" branch) to incorporate changes.
5. How can you create a new Git branch?
	To create a new branch, you can use the command: ```sh git checkout -b new-branch-name ```
6. Explain what a Git commit is.
	A Git commit is a snapshot of changes made to the files in a Git repository. Each commit represents a unique set of changes with a commit message that explains the purpose of the changes. Commits help track the history of a project and provide a way to revert changes if needed.
7. What is a "merge conflict" in Git?
	A merge conflict occurs when Git is unable to automatically merge two branches due to conflicting changes made to the same part of a file. Developers need to manually resolve these conflicts by choosing which version of the changes to keep.
8. How do you resolve a merge conflict?
	To resolve a merge conflict, follow these steps: 
	1. Use `git status` to identify conflicted files.
	2. Open each conflicted file and manually edit to choose the desired changes.
	3. After editing, use `git add` to mark the file as resolved.
	4. Complete the merge using `git commit`.
9. What is a pull request in Git?
	A pull request (PR) is a feature commonly used on platforms like GitHub to propose changes from one branch to another. It allows team members to review, discuss, and approve code changes before they are merged into the main branch.
10. How do you revert a commit in Git?
	To revert a commit, you can use the command: ```sh git revert commit-hash ``` This creates a new commit that undoes the changes introduced by the specified commit. 
11. Explain the difference between rebasing and merge in Git?
	• Git rebase is a command that allows developers to integrate changes from one branch to another.
	• Git merge is a command that allows you to merge branches from Git.
	Git rebase and merge both integrate changes from one branch into another. Where they differ is how they used. Git rebase moves a feature branch into a master. Git merge adds a new commit, preserving the history.
	(If you’re working alone or on a small team, use rebase. If you’re working with a big team, use merge.)
12. How to revert a commit that has already been pushed and made public?
	There are two processes through which you can revert a commit:
	1. Remove or fix the bad file in a new commit and push it to the remote repository. Then commit it to the remote repository using:
		`git commit –m “commit message”`
	2. Create a new commit to undo all the changes that were made in the bad commit. Use the following command:
		`git revert <commit id>`
13. How will you find a list of files that has been modified in a particular commit?
	The command to get a list of files that has been changed in a particular commit is:
	`git diff-tree –r {commit hash}`
	• `-r` flag allows the command to list individual files
	• commit hash lists all the files that were changed or added in the commit. 
14. Explain about “`git cherry-pick`”?
	This command enables you to pick up commits from a branch within a repository and apply it to another branch. This command is useful to undo changes when any commit is accidentally made to the wrong branch. Then, you can switch to the correct branch and use this command to git cherry-pick the commit.
15. Can you tell the difference between git pull and git fetch?
	Git pull command pulls new changes or commits from a particular branch from your central repository and updates your target branch in your local repository. (Git pull = git fetch + git merge)
	Git fetch is also used for the same purpose but it works in a slightly different way. When you perform a git fetch, it pulls all new commits from the desired branch and stores it in a new branch in your local repository. If you want to reflect these changes in your target branch, git fetch must be followed with a git merge.
16. What is origin in Git?
	Origin refers to the remote repository that a project was originally cloned from and is used instead of the original repository’s URL.
17. What is the difference between resetting and reverting?
	git reset changes the state of the branch to a previous one by removing all of the states after the desired commit,
	git revert does it through the creation of new reverting commits and keeping the original one intact.
18. What is ‘staging area’ or ‘index’ in Git?
	That before completing the commits, it can be formatted and reviewed in an intermediate area known as ‘Staging Area’ or ‘Index’. Every change is first verified in the staging area and then that change is committed to the repository.
19. What is Head in Git?
	Git maintains a variable for referencing, called HEAD to the latest commit in the recent checkout branch. So if we make a new commit in the repo then the pointer or HEAD is going to move or change its position to point to a new commit.
20. What is the purpose of branching and its types?
	It allows the user to switch between the branches to keep the current work in sync without disturbing master branches and other developer’s work as per their requirements.
	· Feature branching — A feature branch model keeps all of the changes for a particular feature inside of a branch. When the feature is fully tested and validated by automated tests, the branch is then merged into master.
	· Task branching — In this branch, each task is implemented on its own branch with the task key included in the branch name. It is easy to see which code implements which task, just look for the task key in the branch name.
	· Release branching — Once the develop branch has acquired enough features for a release, you can clone that branch to form a Release branch. Creating this branch starts the next release cycle, so no new features can be added after this point, only bug fixes, documentation generation, and other release-oriented tasks should go in this branch. Once it is ready to ship, the release gets merged into master and tagged with a version number.