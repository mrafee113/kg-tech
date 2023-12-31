### Sources
* [Visual Git Cheatsheet](https://ndpsoftware.com/git-cheatsheet.html#loc=local_repo;)
* [Git Immersion](https://gitimmersion.com/)
* [Github Learning Lab](https://github.com/apps/github-learning-lab)
* [Visualizing Git Concepts with D3](https://onlywei.github.io/explain-git-with-d3/#commit)
* [Official Git Documentation](https://git-scm.com/docs)
* Git Pro Book
* [Learn Git Branching](https://learngitbranching.js.org/)

### Commands
* `git init` create a repository
	* create a `.git` dir along which contains the repository index
* `git add [file]`
	* Git focuses on the changes to a file rather than the file itself. When you say `git add file`, you are not telling git to add the file to the repository. Rather you are saying that git should make note of the current state of that file to be committed later.
* `git commit`
	* `-m/--message [message]`
		* If this is omitted, the proper (which can be set by a variety of variables) editor pops up to record the message.
	* `-a/--all` If files are modified or deleted, git commit does not take them into consideration unless they have been staged using `git add`. Except using this flag will do the job.
	* `--amend`: Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual , and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as `-m`, `-F`, `-c`, etc. The new commit has the same parents and author as the current one.
* `git status`
* `git restore`
	* discard changes that haven't yet been staged.
* `git log`
	* list git commits
	* `--pretty[=<format>]` or `--format[=<format>]`
		* `oneline`
		* `short`
		* `medium`
		* `full`
		* `fuller`
		* `reference`
		* `email`
		* `raw`
		* `format:<string>`
		* `tformat:<string>`
		* see "PRETTY FORMATS" section in git-log(1)
	* `--max-count=<number>`
	* `--since=<date string>`
	* `--until=<date string>`
	* `--author=<name>`
	* `--all`
	* `--date=short`
	* `--graph`
* `git checkout [commit hash]`
	* `-b <new-branch>`: Creates the branch `<new-branch>` and start it at `<start-point>`; if          it already exists, then reset it to `<start-point>`. This is equivalent to running `git branch` with `-f`; see git-branch(1) for details.
	* If a `branch` is used instead of the `[commit hash]`, HEAD will be changed to the latest commit in that branch.
	* Instead of `[commit hash]`, you can use `[tag name]`.
		* If `tag name` is followed by `^`, the resulting string points to the parent commit of the commit which corresponds to the tagname.
		* If `tag name` is followed by `~<number>`, the resulting string points to the `<number>th` commit of the commit which corresponds to the tagname.
	* Instead of `[commit hash]`, you can use `[file]`, which reverts the designated file's content to the repository's version. *This is for files that have changed, but not yet staged.*
* `git switch`
* `git tag [tag name]`
	* `-d/--delete` deletes existing tags given the name
* `git reset [commit] [file]`
	* For files that have been staged, but not yet commited. This will remove the index pertaining to the changes staged on the `file`. Then you can use `git checkout <file>` to clear the changes if you want.
	* When given a commit reference (i.e. a hash, branch or tag name), the `reset` command will:
		1.  Rewrite the current branch to point to the specified commit.
		2. Optionally reset the staging area to match the specified commit.
		3. Optionally reset the working directory to match the specified commit.
	* `--hard`: Resets the index and working tree. Any changes to tracked files in the working tree since `<commit>` are discarded. Any untracked files or directories in the way of writing any tracked files are simply deleted.
	* Resets on local branches are generally safe. Any “accidents” can usually be recovered from by just resetting again with the desired commit. However, if the branch is shared on remote repositories, resetting can confuse other users sharing the branch.
* `git revert [commit]`
	* This creates a new commit, to remove the changes of the local repo to the mentioned commit. A new commit means that the changes are visible through the `git log`.
	* Be careful with this, as it may remove uncommited changes.
* `git mv [file] [directory]`
	* Informs git that `file` has been deleted and `directory/file` has been created. Also the changes will be automatically staged, ready to be commited.
* `git rm [pathspec]`
	* Git removes the specified file from the working directory and the git index. The changes will be staged, ready to be commited.
* `git branch`
	* With no arguments, it's like `git branch --list`.
	* `-l/--list` shows the list of branches, with an optional argument of `patterns`.
	* `-r/--remote` lists/works remote branches.
	* `-a/--all` lists/works both local and remote branches.
	* `-t/--track` links a local branch with a remote one
* `git merge`
	* Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch. This command is used by git pull to incorporate changes from another repository and can be used by hand to merge changes from one branch into another.
	* `git merge [branch]` merges the `<branch>` into the current working branch.
* `git rebase`
	* If instead of `git merge` we use `git rebase`,  things would be different. The final result of the rebase is very similar to the merge. The first branch now contains all of its changes, as well as all the changes from the second branch. However, the commit tree is quite different. The commit tree for the first branch has been rewritten so that the second branch is a part of the commit history. This leaves the chain of commits linear and much easier to read.
	* When to rebase? When to merge? Don't use rebase when:
		1. If the branch is public and shared with others. Rewriting publicly shared branches will tend to screw up other members of the team.
		2. When the _exact_ history of the commit branch is important (since rebase rewrites the commit history).
		* Given the above guidelines, I tend to use rebase for short-lived, local branches and merge for branches in the public repository.
* `git remote`
	* `git remote show origin`
	* `git remote add `
* `git fetch`
* `git pull`
	* equals `git fetch` followed by `git merge origin/<branch>`
* `git clone`
	* `--bare` I didn't get the point of this.
* `git daemon` for starting git server

> [!Question] ChatGPT
> **In git:**
> 1. **How can I see the changes of a file that hasn't been `git add`ed?**
> 	You can use the `git diff` command followed by the path to the file.
>>	`git diff path/to/your/file.txt`
>
>    This command will show the difference between the current state of the file in your working directory and the last committed version.
>>
> 2. **How can I see the changes of a file that has only been `git add`ed but not `git commit`ed?**
>	You can use the same git diff command with the `--staged` (or `--cached`) option to view the changes in the staging area.
>>	`git diff --staged path/to/your/file.txt`
>
>    This will show the difference between the version of the file in the last commit and the staged changes.
>>
> 1. **How can I see the changes of a file that has been committed given the file and the commit?**
>    Use the git show command followed by the commit hash and the path to the file.
>>	`git show <commit-hash>:path/to/your/file.txt`
>
>    This command will display the changes made to the specified file in that specific commit.
### .git Directory
* `.git/objects` dir: Contains a bunch of 2 letter name directories. The directory names are the first two letters of the sha1 hash of the object stored in git. Each folder contains one or more binary files with commit hashes as their names. They obviously correspond to each commit.
* `.git/config` file: This is a project-specific configuration file. Config entries in here will override the config entries in the `.gitconfig` file in your home directory, at least for this project.
* `.git/refs/heads` dir: This directory contains the branch pointers, each of which contain a commit hash.
* `.git/refs/tags` dir: This directory contains the tag pointers, each of which contain a commit hash.
* `.git/HEAD` file: contains the commit hash that head points to
* `git catfile [hash]` inspects a git object
	* `-t` shows the object type
	* `-p` pretty prints the contents based on type

> [!Question] ChatGPT
> **Name and explain GIT pointers**
>
> In Git, pointers are fundamental mechanisms that help track and manage different aspects of the version control system, including branches, commits, and more. Here are some of the key Git pointers and their explanations:
> 1. **HEAD:** The `HEAD` pointer represents the current snapshot or commit in the repository. It is essentially a reference to the latest commit on the currently checked-out branch. It allows you to know which commit you're currently working on. 
> 2. **Branches:** Branches are pointers that point to specific commits in the repository. When you create a new branch, Git creates a new pointer that references the commit you were on when you created the branch. As you make new commits on the branch, the branch pointer moves forward to point to the latest commit. 
> 3. **Tags:** Tags are similar to branches in that they are also pointers, but they are used to mark specific points in history as significant milestones, like releases. Unlike branches, tags don't move as new commits are added; they remain fixed at the specific commit they were created on. 
> 4. **Remote Branches:** Remote branches are pointers that track branches on remote repositories, such as those on GitHub. These pointers allow your local repository to know about the state of branches in the remote repository and facilitate synchronization between the local and remote copies of the code. 
> 5. **Detached `HEAD`:** A detached `HEAD` occurs when `HEAD` is directly pointing to a commit rather than a branch. This usually happens when you check out a specific commit using its hash. In this state, any new commits you make will not be part of any branch and can potentially be lost if you switch branches. 
> 6. **`ORIG_HEAD`:** The `ORIG_HEAD` pointer is used by Git to keep track of the previous state of `HEAD` before a potentially dangerous operation, like a `git reset` or `git merge`. This allows you to undo the operation if needed. 
>
> These pointers play a crucial role in Git's functionality, allowing you to navigate, track changes, and manage the history of your codebase effectively. Understanding these pointers is essential for efficiently working with version control in Git.
