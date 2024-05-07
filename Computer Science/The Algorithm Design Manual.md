> [springer: The Algorithm Design Manual 3rd Edition](https://link.springer.com/book/10.1007/978-3-030-54256-6)
> [algorist.com](https://www.algorist.com/)

> [!Example] Planning
> `total-pages` $= 659$
> `words-per-page` $= 500$
> `words-per-min` $= 85$
> `min-per-page` $=$ `words-per-page` $/$ `words-per-min` $= 500 / 85$ $= 5.88235$
> `total-hours` $=$ `total-pages` $*$ `min-per-page` $/ 60$ $= 659 * 5.88235 / 60$ $= 64.607$
>
> `avg-performance` $= 95\%$
> `hour-per-day` $= 4$
> `reading-day-duration` $=$ `total-hours` $/$ `hour-per-day` $*$ `avg-performance` $= 64.607 / 4 * (1 / 0.95) -> 17\ days$
> 
> `start-date`: $15\ Azar$
> `day-duration`: $45$
> `deadline-date`: $30\ Dey$
> `practice-day-duration`: `day-duration` $-$ `reading-day-duration` $= 45 - 17$ $= 28$
> `practice-time-duration`: `practice-day-duration` $*$ `hour-per-day` $= 28 * 4$ $= 112$
> 
> > [!Info] Section Formula
> > `hour-per-page` $= 0.09803$
> > `min-per-page` $= 5.88235$
> > `practice-time-duration` $= 112$
> > > [!Exmaple] Example
> > > `Chapter 1: Introduction to Algorithm Design`
> > > 	`section-pages` $= 24$
> > > 	`section-reading-time-duration` = `section-pages` $*$ `hour-per-page` $= 2^{'}\ 21^"$
> > > 	`section-practice-time-duration` = `section-pages` $/$ `total-pages` $*$ `practice-time-duration` $= 24 / 659 * 112$ $= 4^{'}\ 4^"$

## Part I: Practical Algorithm Design
### Chapter 1: Introduction to Algorithm Design
> `pg: 24`
> `time req: 2' 22"`
> `time done: 1' 49"`
> `performance: 130%`
>
> `practice time req: 4' 5"`

* What is an algorithm? An algorithm is a procedure to accomplish a specific task. An algorithm is the idea behind any reasonable computer program.
* To be interesting, an algorithm must solve a general, well-specified problem. An algorithmic problem is specified by describing the complete set of instances it must work on and of its output after running on one of these instances. This distinction, between a problem and an instance of a problem, is fundamental.
* Determining that you are dealing with a general problem instead of an instance is your first step towards solving it.
* An algorithm is a procedure that takes any of the possible input instances and transforms it to the desired output.
* There are three desirable properties for a good algorithm. We seek algorithms that are **correct** and **eficient**, while being **easy** to implement.
* These goals may not be simultaneously achievable. In industrial settings, any program that seems to give good enough answers without slowing the application down is often acceptable, regardless of whether a better algorithm exists. The issue of finding the best possible answer or achieving maximum eficiency usually arises in industry only after serious performance or legal troubles.
* It is seldom obvious whether a given algorithm correctly solves a given problem. Correct algorithms usually come with a proof of correctness, which is an explanation of why we know that the algorithm must take every instance of the problem to the desired result. It is important to demonstrate why "*it’s obvious*" never sufices as a proof of correctness, and is usually ﬂat-out wrong.

> [!Error] 1.1 Robot Tour Optimization

> [!Info] There is a fundamental difference between algorithms, procedures that always produce a correct result, and heuristics, which may usually do a good job but provide no guarantee of correctness.

> [!Error] 1.2 Selecting the Right Jobs

* Ensuring the optimal answer over all possible inputs is a dificult but often achievable goal.
* Seeking counterexamples that break pretender algorithms is an important part of the algorithm design process.
* Eficient algorithms are often lurking out there; this book will develop your skills to help you find them.

> [!Warning] Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.

> [!Error] 1.3 Reasoning About Correctness

* We need tools to distinguish correct algorithms from incorrect ones, the primary one of which is called a **proof**.
* A proof is indeed a demonstration.
* Proofs are useful only when they are honest, crisp arguments that explain why an algorithm satisfies a non-trivial correctness property.
* Correct algorithms require careful exposition, and efforts to show both correctness and not incorrectness.

> [!subsubsection] 1.3.1 Problems and Properties

* Before we start thinking about algorithms, we need a careful description of the problem that needs to be solved.
* Problem specifications have two parts:
	1. the set of allowed input instances, and
	2. the required properties of the algorithm’s output.
* It is impossible to prove the correctness of an algorithm for a fuzzily-stated problem.
* Put another way, ask the wrong question and you will get the wrong answer.

> [!Tip] An important and honorable technique in algorithm design is to narrow the set of allowable instances until there is a correct and eficient algorithm.

> [!Warning] There are two common traps when specifying the output requirements of a problem.
> * The first is asking an ill-defined question.
> * The second trap involves creating compound goals.

> [!subsubsection] 1.3.2 Expressing Algorithms

> [!Tip] The heart of any algorithm is an $idea$. If your idea is not clearly revealed when you express an algorithm, then you are using too low-level a notation to describe it.

> [!subsubsection] 1.3.3 Demonstrating Incorrectness

* The best way to prove that an algorithm is incorrect is to produce an instance on which it yields an incorrect answer.
* Such instances are called **counterexamples**.
* No rational person will ever defend the correctness of an algorithm after a counter-example has been identified. Very simple instances can instantly defeat reasonable-looking heuristics with a quick touché.
---
* Good counterexamples have two important properties:
* **Verifiability**: To demonstrate that a particular instance is a counterexample to a particular algorithm, you must be able to:
	1. calculate what answer your algorithm will give in this instance, and
	2. display a better answer so as to prove that the algorithm didn’t find it.
* **Simplicity**: Good counterexamples have all unnecessary details stripped away. They make clear exactly $why$ the proposed algorithm fails. Simplicity is important because you must be able to hold the given instance in your head in order to reason about it. Once a counterexample has been found, it is worth simplifying it down to its essence.
---
* Hunting for counterexamples is a skill worth developing. It bears some similarity to the task of developing test sets for computer programs, but relies more on inspiration than exhaustion. Here are some techniques to aid your quest:
* **Think Small**: Amateur algorists tend to draw a big messy instance and then stare at it helplessly. The pros look carefully at several small examples, because they are easier to verify and reason about.
* **Think Exhaustively**: There are usually only a small number of possible instances for the first non-trivial value of $n$.
* **Hunt for the Weakness**: If a proposed algorithm is of the form “always take the biggest” (better known as the *greedy algorithm*), think about why that might prove to be the wrong thing to do.
* **Go for a tie**: A devious way to break a greedy heuristic is to provide instances where everything is the same size. Suddenly the heuristic has nothing to base its decision on, and perhaps has the freedom to return something suboptimal as the answer.
* **Seek Extremes**: Many counter-examples are mixtures of huge and tiny, left and right, few and many, near and far. It is usually easier to verify or reason about extreme examples than more muddled ones.

> [!Tip] Searching for counterexamples is the best way to disprove the correctness of a heuristic.

> [!Error] 1.4 Induction and Recursion

* Recursion is mathematical induction in action.

> [!Tip] Mathematical induction is usually the right way to verify the correctness of a recursive or incremental insertion algorithm.

> [!Error] 1.5 Modeling the Problem

* $Modeling$ is the art of formulating your application in terms of precisely described, well-understood problems.
* Real-world applications involve real-world objects. Most algorithms, however, are designed to work on rigorously defined abstract structures such as permutations, graphs, and sets. To exploit the algorithms literature, you must learn to describe your problem abstractly, in terms of procedures on such fundamental structures.

> [!subsubsection] 1.5.1 Combinatorial Objects

* The act of modeling reduces your application to one of a small number of existing problems and structures. Such a process is inherently constraining, and certain details might not fit easily into the given target problem. Also, certain problems can be modeled in several different ways, some much better than others.

> [!Tip] Modeling your application in terms of well-defined structures and algorithms is the most important single step towards a solution.

> [!subsubsection] 1.5.2 Recursive Objects

* Learning to think recursively is learning to look for big things that are made from smaller things of exactly the same $type$ as the big thing.

> [!Error] 1.6 Proof by Contradiction

* *The Oxford English Dictionary* defines an algorist as “one skillful in reckonings or figuring.”

> [!Error] 1.9 Estimation

* When you don’t know the right answer, the best thing to do is guess.
* Principled guessing is called $estimation$.
* Estimation problems are best solved through some kind of logical reasoning process, typically a mix of principled calculations and analogies. Principled calculations give the answer as a function of quantities that either you already know, can look up on Google, or feel confident enough to guess. Analogies reference your past experiences, recalling those that seem similar to some aspect of the problem at hand.
* A best practice in estimation is to try to solve the problem in different ways and see if the answers generally agree in magnitude. All of these are within a factor of two of each other, giving me confidence that my answer is about right.
* A sound reasoning process matters a lot more here than the actual numbers you get.

### Chapter 2: Algorithm Analysis
> `pg: 29`
> `time req: 2' 51"`
> `time done: 1' 16"`
> `performance: 225%`
>
> `practice time req: 4' 56"`

![[Computer Science/algo-manual-images/2.3-running-times-common-functions.png]]

$$n! \gg c^n \gg n^3 \gg n^2 \gg n^{1+\epsilon} \gg n\log n \gg n \gg \sqrt{n} \gg$$
$$\log^2n \gg \log n \gg \frac{\log n}{\log{\log n}} \gg \log{\log n} \gg \alpha(n) \gg 1$$

### Chapter 3: Data Structures
> `pg: 34`
> `time req: 3' 20"`
> `time done: 1' 34"`
> `performance: 212%`
>
> `practice time req: 5' 47"`

* Putting the right data structure into a slow program can work the same wonders as transplanting fresh parts into a sick patient.

> [!Error] 3.1 Contiguous vs Linked Data Structures

* Data structures can be neatly classified as either $contiguous$ or $linked$, depending upon whether they are based on arrays or pointers.
* $Contiguously\ allocated\ structures$ are composed of single slabs of memory, and include arrays, matrices, heaps, and hash tables.
* $Linked\ data\ structures$ are composed of distinct chunks of memory bound together by pointers, and include lists, trees, and graph adjacency lists.

> [!subsubsection] 3.1.1 Arrays

* Advantages:
	* **Constant-time access given the index**
	* **Space eficiency**: Arrays consist purely of data, so no space is wasted with links or other formatting information. Further, end-of-record information is not needed because arrays are built from fixed-size records.
	* **Memory locality**: Many programming tasks require iterating through all the elements of a data structure. Arrays are good for this because they exhibit excellent memory locality. Physical continuity between successive data accesses helps exploit the high-speed cache memory on modern computer architectures.
* The downside of arrays is that we cannot adjust their size in the middle of a program’s execution. We can compensate by allocating extremely large arrays, but this can waste space.
---
* Actually, we can eficiently enlarge arrays as we need them, through the miracle of $dynamic\ arrays$.
	* Suppose we start with an array of size $1$, and double its size from $m$ to $2m$ whenever we run out of space.
	* This doubling process allocates a new contiguous array of size $2m$,
	* copies the contents of the old array to the lower half of the new one,
	* and then returns the space used by the old array to the storage allocation system.
* The apparent waste in this procedure involves recopying the old contents on each expansion.
* The primary thing lost in using dynamic arrays is the guarantee that each insertion takes constant time in the worst case. Note that all accesses and most insertions will be fast, except for those relatively few insertions that trigger array doubling. What we get instead is a promise that the nth element insertion will be completed quickly enough that the total effort expended so far will still be $O(n)$.

> [!subsubsection] 3.1.3: Linked Structures vs Static Arrays

* advantages of linked structures over arrays:
	* Overﬂow on linked structures never occurs unless the memory is actually full.
	* Insertion and deletion are simpler than for static arrays.
	* With large records, moving pointers is easier and faster than moving the items themselves.

> [!Error] 3.2 Containers: Stacks and Queues

* The term $container$ denotes an abstract data type that permits storage and retrieval of data items independent of content.
* Containers are distinguished by the particular retrieval order they support.
* In the two most important types of containers, this retrieval order depends on the insertion order:
	* **Stacks** support retrieval by last-in, first-out (LIFO) order.
	* **Queues** support retrieval in first-in, first-out (fiFO) order.

> [!Error] 3.7 Hashing

* Hash tables are a very practical way to maintain a dictionary.
* They exploit the fact that looking an item up in an array takes constant time once you have its index.
* A $hash\ function$ is a mathematical function that maps keys to integers.
* We will use the value of our hash function as an index into an array, and store our item at that position.
---
* The first step of the hash function is usually to map each key (here the string $S$) to a big integer. Let $α$ be the size of the alphabet on which $S$ is written. Let $char(c)$ be a function that maps each symbol of the alphabet to a unique integer from $0$ to $α − 1$. The function
	* $H(S) = \alpha^{|S|} + \displaystyle\sum_{i=0}^{|S| - 1} \alpha^{|S| - (i+1)} \times char(s_i)$
	* maps each string to a unique (but large) integer by treating the characters of the string as “digits” in a base-$α$ number system.
* This creates unique identifier numbers, but they are so large they will quickly exceed the number of desired slots in our hash table (denoted by $m$). We must reduce this number to an integer between $0$ and $m − 1$, by taking the remainder $H^{'}(S) = H(S)\ mod\ m$.
* This works on the same principle as a roulette wheel. The ball travels a long distance, around and around the circumference-$m$ wheel $\lfloor \frac{H(S)}{m}\rfloor$ times before settling down to a random bin. If the table size is selected with enough finesse (ideally $m$ is a large prime not too close to $2^i − 1$), the resulting hash values should be fairly uniformly distributed.

> [!subsubsection] 3.7.1 Collision Resolution

* No matter how good our hash function is, we had better be prepared for collisions, because two distinct keys will at least occasionally hash to the same value.
---
* There are two different approaches for maintaining a hash table:
* $Chaining$ represents a hash table as an array of $m$ linked lists (“buckets”). The $i$th list will contain all the items that hash to the value of $i$. Search, insertion, and deletion thus reduce to the corresponding problem in linked lists. If the $n$ keys are distributed uniformly in a table, each list will contain roughly $n/m$ elements, making them a constant size when $m ≈ n$.
* Chaining is very natural, but devotes a considerable amount of memory to pointers. This is space that could be used to make the table larger, which reduces the likelihood of collisions. In fact, the highest-performing hash tables generally rely on an alternative method called open addressing.
* $Open\ addressing$ maintains the hash table as a simple array of elements (not buckets). Each cell is initialized to null. On each insertion, we check to see whether the desired cell is empty; if so, we insert the item there. But if the cell is already occupied, we must find some other place to put the item. The simplest possibility (called $sequential\ probing$) inserts the item into the next open cell in the table. Provided the table is not too full, the contiguous runs of non-empty cells should be fairly short, hence this location should be only a few cells away from its intended position.
* Searching for a given key now involves going to the appropriate hash value and checking to see if the item there is the one we want. If so, return it. Otherwise we must keep checking through the length of the run. Deletion in an open addressing scheme can get ugly, since removing one element might break a chain of insertions, making some elements inaccessible. We have no alternative but to reinsert all the items in the run that follows the new hole.

> [!subsubsection] 3.7.2 Duplicate Detection via Hashing

* The key idea of hashing is to represent a large object (be it a key, a string, or a substring) by a single number.

### Chapter 4: Sorting
> `pg: 31`
> `time req: 3' 3"`
> `time done: 2' 48"`
> `performance: 108%`
>
> `practice time req: 5' 17"`
> `practice time done: 7' 30"`
> `p-performance: 70.4%`

> [!Error] 4.1 Applications of Sorting

* An important algorithm design technique is to use sorting as a basic building block, because many other problems become easy once a set of items is sorted.

> [!Error] 4.3 Heapsort: Fast Sorting via Data Structures

> [!subsubsection] 4.3.1 Heaps

* Power in any hierarchically structured organization is reﬂected by a tree, where each node in the tree represents a person, and edge $(x, y)$ implies that $x$ directly supervises (or dominates) $y$. The person at the root sits at the “top of the heap.”
* In this spirit, a heap-labeled tree is defined to be a binary tree such that the key of each node dominates the keys of its children. In a $min-heap$, a node dominates its children by having a smaller key than they do, while in a $max- heap$ parent nodes dominate by being bigger.
* The most natural implementation of this binary tree would store each key in a node with pointers to its two children. But as with binary search trees, the memory used by the pointers can easily outweigh the size of keys, which is the data we are really interested in. The heap is a slick data structure that enables us to represent binary trees without using any pointers. We store data as an array of keys, and use the position of the keys to $implicitly$ play the role of the pointers.
* We store the root of the tree in the first position of the array, and its left and right children in the second and third positions, respectively. In general, we store the $2^{l−1}$ keys of the $l$th level of a complete binary tree from left to right in positions $2^{l−1}$ to $2^l − 1$. We assume that the array starts with index 1 to simplify matters.

> [!subsubsection] 4.3.2 Constructing Heaps
> 

* Heaps can be constructed incrementally, by inserting each new element into the left-most open spot in the array, namely the $(n + 1)$st position of a previously $n$-element heap.
* This ensures the desired balanced shape of the heap-labeled tree, but does not maintain the dominance ordering of the keys. The new key might be less than its parent in a min-heap, or greater than its parent in a max-heap.
* The solution is to swap any such dissatisfied element with its parent. The old parent is now happy, because it is properly dominated. The other child of the old parent is still happy, because it is now dominated by an element even more extreme than before. The new element is now happier, but may still dominate its new parent. So we recur at a higher level, $bubbling$ up the new key to its proper position in the hierarchy. Since we replace the root of a subtree by a larger one at each step, we preserve the heap order elsewhere.
* This swap process takes constant time at each level. Since the height of an $n$-element heap is $\lfloor lg n\rfloor$, each insertion takes at most $O(\log n)$ time. A heap of $n$ elements can thus be constructed in $O(n \log n)$ time through $n$ insertions.

> [!subsubsection] 4.3.3 Extracting the Minimum

* Removing the top element leaves a hole in the array. This can be filled by moving the element from the right-most leaf (sitting in the nth position of the array) into the first position.
* The shape of the tree has been restored but (as after insertion) the labelling of the root may no longer satisfy the heap property. Indeed, this new root may be dominated by both of its children. The root of this min-heap should be the smallest of three elements, namely the current root and its two children. If the current root is dominant, the heap order has been restored. If not, the dominant child should be swapped with the root and the problem pushed down to the next level.
* This dissatisfied element $bubbles$ down the heap until it dominates all its children, perhaps by becoming a leaf node and ceasing to have any. This percolate-down operation is also called $heapify$, because it merges two heaps (the subtrees below the original root) with a new key.
* We will reach a leaf after $\lfloor lg n\rfloor$ bubble down steps, each constant time. Thus, root deletion is completed in $O(\log n)$ time.
* Repeatedly exchanging the maximum element with the last element and calling heapify yields an $O(n \log n)$ sorting algorithm, named **heapsort**.
---
* Heapsort is a great sorting algorithm.
* It is simple to program.
* It runs in worst-case $O(n \log n)$ time, which is the best that can be expected from any sorting algorithm.
* It is an in-place sort, meaning it uses no extra memory over the array containing the elements to be sorted.
* Although other algorithms prove slightly faster in practice, you won’t go wrong using heapsort for sorting data that sits in the computer’s main memory.

> [!subsubsection] 4.3.5 Sorting via Incremental Insertion

* Consider a different approach to sorting via eficient data structures. Select the next element from the unsorted set, and put it into it’s proper position in the sorted set:
	```cpp
	for (i = 1; i < n; i++) {
		j = i;
		while ((j > 0) && (s[j] < s[j - 1])) {
			swap(&s[j], &s[j - 1]);
			j = j-1;
		}
	}
	```
* Although insertion sort takes $O(n^2)$ in the worst case, it performs considerably better if the data is almost sorted, since few iterations of the inner loop sufice to sift it into the proper position.
* Insertion sort is perhaps the simplest example of the incremental insertion technique, where we build up a complicated structure on $n$ items by first building it on $n − 1$ items and then making the necessary changes to add the last item.
* Note that faster sorting algorithms based on incremental insertion follow from more eficient data structures. Insertion into a balanced search tree takes $O(\log n)$ per operation, or a total of $O(n \log n)$ to construct the tree. An in-order traversal reads through the elements in sorted order to complete the job in linear time.

> [!Error] 4.5 Mergesort: Sorting by Divide and Conquer

> [!Warning] Go read this section to understand its complexity analysis.

> [!Error] 4.6 Quicksort: Sorting by Randomization

* Suppose we select an arbitrary item p from the n items we seek to sort. Quicksort separates the $n − 1$ other items into two piles: a low pile containing all the elements that are $< p$, and a high pile containing all the elements that are $≥ p$. Low and high denote the array positions into which we place the respective piles, leaving a single slot between them for $p$.
* Such partitioning buys us two things.
	* first, the pivot element $p$ ends up in the exact array position it will occupy in the final sorted order.
	* Second, after partitioning no element ﬂips to the other side in the final sorted order.
	* **Thus, we can now sort the elements to the left and the right of the pivot independently!**
	* This gives us a recursive sorting algorithm, since we can use the partitioning approach to sort each subproblem. The algorithm must be correct, because each element ultimately ends up in the proper position:
	```cpp
	void quicksort(item_type s[], int l, int h) {
		int p;
		/* index of partition */
		if (l < h) {
			p = partition(s, l, h);
			quicksort(s, l, p - 1);
			quicksort(s, p + 1, h);
		}
	}
	```
* We can partition the array in one linear scan for a particular pivot element by maintaining three sections of the array: less than the pivot (to the left of $firsthigh$), greater than or equal to the pivot (between $firsthigh$ and $i$), and unexplored (to the right of $i$), as implemented below:
```cpp
int partition(item_type s[], int l, int h) {
	int i;
	/* counter */
	int p;
	/* pivot element index */
	int firsthigh; /* divider position for pivot element */
	p = h;
	/* select last element as pivot */
	firsthigh = l;
	for (i = l; i < h; i++) {
		if (s[i] < s[p]) {
			swap(&s[i], &s[firsthigh]);
			firsthigh++;
		}
	}
	swap(&s[p], &s[firsthigh]);
	return(firsthigh);
}
```
* Since the partitioning step consists of at most $n$ swaps, it takes linear time in the number of keys. But how long does the entire quicksort take?
	* As with mergesort, quicksort builds a recursion tree of nested subranges of the $n$-element array.
	* As with mergesort, quicksort spends linear time processing (now partitioning instead of mergeing) the elements in each subarray on each level.
	* As with mergesort, quicksort runs in $O(n · h)$ time, where $h$ is the height of the recursion tree.
* The dificulty is that the height of the tree depends upon where the pivot element ends up in each partition. If we get very lucky and happen to repeatedly pick the median element as our pivot, the subproblems are always half the size of those at the previous level.
* The height represents the number of times we can halve $n$ until we get down to $1$, meaning $h = \lceil lg n\rceil$. This happy situation corresponds to the best case of quicksort.
* Now suppose we consistently get unlucky, and our pivot element always splits the array as unequally as possible. This implies that the pivot element is always the biggest or smallest element in the sub-array. After this pivot settles into its position, we will be left with one subproblem of size $n − 1$. After doing linear work we have reduced the size of our problem by just one measly element. It takes a tree of height $n − 1$ to chop our array down to one element per level, for a worst case time of $Θ(n^2)$.
* Thus, the worst case for quicksort is worse than heapsort or mergesort. To justify its name, quicksort had better be good in the average case. Understanding why requires some intuition about random sampling.

> [!subsubsection] 4.6.2 Randomized Algorithms

* Randomization is a powerful tool to improve algorithms with bad worst-case but good average-case complexity. It can be used to make algorithms more robust to boundary cases and more eficient on highly structured input instances that confound heuristic decisions (such as sorted input to quicksort).
* It often lends itself to simple algorithms that provide expected-time performance guarantees, which are otherwise obtainable only using complicated deterministic algorithms.

> [!Error] 4.7 Distribution Sort: Sorting via Bucketing

* To sort names for a class roster or the telephone book, we could first partition them according to the first letter of the last name. This will create twenty-six different piles, or buckets, of names. Observe that any name in the J pile must occur after all names in the I pile, and before any name in the K pile. Therefore, we can proceed to sort each pile individually and just concatenate the sorted piles together at the end.
* Assuming the names are distributed evenly among the buckets, the resulting twenty-six sorting problems should each be substantially smaller than the original problem. By now further partitioning each pile based on the second letter of each name, we can generate smaller and smaller piles. The set of names will be completely sorted as soon as every bucket contains only a single name. Such an algorithm is commonly called $bucketsort$ or $distribution\ sort$.
* Bucketing is a very effective idea whenever we are confident that the distribution of data will be roughly uniform. It is the idea that underlies hash tables, kd-trees, and a variety of other practical data structures. The downside of such techniques is that the performance can be terrible when the data distribution is not what we expected. Although data structures such as balanced binary trees offer guaranteed worst-case behavior for any input distribution, no such promise exists for heuristic data structures on unexpected input distributions.

### Chapter 5: Divide and Conquer
> `pg: 20`
> `time req: 1' 58"`
> `time done: 1' 38"`
> `performance: 120%`
>
> `practice time req: 3' 24"`
> `practice time done: 5' 22"`
> `p-performance: 63%`

* One of the most powerful techniques for solving problems is to break them down into smaller, more easily solved pieces. Smaller problems are less overwhelming, and they permit us to focus on details that are lost when we are studying the whole thing.
* A recursive algorithm starts to become apparent whenever we can break the problem into smaller instances of the same type of problem.
* Two important algorithm design paradigms are based on breaking problems down into smaller problems. Dynamic programming, which typically removes one element from the problem, solves the smaller problem, and then adds back the element to the solution of this smaller problem in the proper way. Divide and conquer instead splits the problem into (say) halves, solves each half, then stitches the pieces back together to form a full solution.

> [!Error] 5.4 Solving Divide-and-Conquer Recurrences

* Divide-and-conquer recurrences of the form $T(n) = aT (n/b) + f(n)$ are generally easy to solve, because the solutions typically fall into one of three distinct cases:
1. If $f(n) = O(n^{\log_b a−\epsilon})$ for some constant $\epsilon > 0$, then $T(n) = Θ(n^{\log_b a})$.
	* heap construction and matrix multiplication
	* cost: *Too many leaves* – If the number of leaf nodes outweighs the overall internal evaluation cost, the total running time is $O(n^{\log_b a})$.
2. If $f(n) = Θ(n^{\log_b a})$, then $T(n) = Θ(n^{\log_b a}\ \lg n)$.
	* mergesort
	* cost: *Equal work per level* – As we move down the tree, each problem gets smaller but there are more of them to solve. If the sums of the internal evaluation costs at each level are equal, the total running time is the cost per level ($n^{\log_b a}$) times the number of levels ($\log_b n$), for a total running time of $O(n^{\log_b a}\ \lg n)$.
1. If $f(n) = Ω(n^{\log_b a+\epsilon})$ for some constant $\epsilon > 0$, and if $af(n/b) ≤ cf(n)$ for some $c < 1$, then $T(n) = Θ(f(n))$.
	* This generally arises with clumsier algorithms, where the cost of combining the subproblems dominates everything.
	* cost: *Too expensive a root* – If the internal evaluation cost grows very rapidly with $n$, then the cost of the root evaluation may dominate everything. Then the total running time is $O(f(n))$.

> [!Error] 5.7 Parallel Algorithms

* $Two$ heads are better than $one$, and more generally, $n$ heads better than $n − 1$.

> [!Error] 5.9 Convolution (\*)

* The $convolution$ of two arrays (or vectors) $A$ and $B$ is a new vector $C$ such that
	* $C[k] = \displaystyle\sum_{j=0}^{m-1} A[j] · B[k-j]$
* If we assume that $A$ and $B$ are of length $m$ and $n$ respectively, and indexed starting from $0$, the natural range on $C$ is from $C[0]$ to $C[n + m − 2]$. The values of all out-of-range elements of $A$ and $B$ are interpreted as zero, so they do not contribute to any product.
* An example of convolution that you are familiar with is $polynomial\ multiplication$.
* Convolution multiplies every possible pair of elements from $A$ and $B$, and hence it seems like we should require quadratic time to get these $n + m − 1$ numbers. But in a miracle akin to sorting, there exists a clever divide-and-conquer algorithm that runs in $O(n \log n)$ time, assuming that $n ≥ m$.

> [!subsubsection] 5.9.1 Applications of Convolution

* Going from $O(n^2)$ to $O(n \log n)$ is as big a win for convolution as it was for sorting. Taking advantage of it requires recognizing when you are doing a convolution operation. Convolutions often arise when you are trying all possible ways of doing things that add up to $k$, for a large range of values of $k$, or when sliding a mask or pattern $A$ over a sequence $B$ and calculating at each position.
---
* $Integer\ Multiplication$
	* We can interpret integers as polynomials in any base $b$. For example, $632 = 6 · b^2 + 3 · b^1 + 2 · b^0$ , where $b = 10$.
	* Polynomial multiplication behaves like integer multiplication without carrying.
* $Cross\text{-}Correlation$
* $Moving\ Average\ filters$
	* Often we are tasked with smoothing time series data by averaging over a window.
	* Perhaps we want $C[i−1] = 0.25B[i−1]+ 0.5B[i] + 0.25B[i + 1]$ over all positions $i$.
	* This is just another convolution, where $A$ is the vector of weights within the window around $B[i]$.
* $String\ Matching$
	* We are given a text string $S$ and a pattern string $P$ , and seek to identify all locations in $P$ where $P$ may be found.
	* The sliding window approach is suggestive of being a convolution with the reversed pattern $P^R$.
	* Suppose our strings have an alphabet of size $α$. We can represent each character by a binary vector of length $α$ having exactly one non-zero bit.
		* Say $a = 10$ and $b = 01$ for the alphabet $\{a, b\}$. Then we can encode the strings $S$ and $P$ above as $S = 1001101001100110$ and $P = 100110$.
		* The dot product over a window will be $m$ on an even-numbered position of $s$ iff $p$ starts at that position in the text.
	* So fast convolution can identify all locations of $p$ in $s$ in $O(n \log n)$ time.

> [!Warning] Learn to recognize possible convolutions. A magical $Θ(n \log n)$ algorithm instead of $O(n^2)$ is your reward for seeing this.

### Chapter 6: Hashing and Randomized Algorithms
> `pg: 23`
> `time req: 2' 16"`
> `time done: 38"`
> `performance: 357%`
>
> `practice time req: 3' 55"`

* Relaxing the demand for either *always correct* or *always eficient* can lead to useful algorithms that still have performance guarantees.
* Randomized algorithms are not merely heuristics: any bad performance is due to getting unlucky on coin ﬂips, rather than adversarial input data.
* We classify randomized algorithms into two types, depending upon whether they guarantee correctness or eficiency:
	* $Las\ Vegas\ algorithms$: These randomized algorithms guarantee correctness, and are usually (but not always) eficient.
		* Quicksort
	* $Monte\ Carlo\ algorithms$: These randomized algorithms are probably efficient, and usually (but not always) produce the correct answer or something close to it.
		* Representative of this class are random sampling methods, where we return the best solution found in the course of (say) 1,000,000 random samples.
* One blessing of randomized algorithms is that they tend to be very simple to describe and implement. Eliminating the need to worry about rare or unlikely situations makes it possible to avoid complicated data structures and other contortions. These clean randomized algorithms are often intuitively appealing, and relatively easy to design.
* However, randomized algorithms are frequently quite dificult to analyze rigorously. Probability theory is the mathematics we need for the analysis of randomized algorithms, and is of necessity both formal and subtle. Probabilistic analysis often involves algebraic manipulation of long chains of inequalities that looks frightening, and relies on tricks and experience.

> [!Error] 6.2 Understanding Balls and Bins

> [!Warning] Didn't understand a word from this section on.

### Chapter 7: Graph Traversal
> `pg: 38`
> `time req: 3' 44"`
> `time done: 4' 11"`
> `performance: 89%`
>
> `practice time req: 6' 28"`
> `practice time done: 3' 10"`
> `p-performance: 204%`

> [!Error] 7.1 Flavour of Graphs

* $Cyclic$ vs $Acyclic$
	* A cycle is a closed path of $3$ or more vertices that has no repeating vertices except the start/end point.
	* An acyclic graph does not contain any cycles.
	* Trees are undirected graphs that are connected and acyclic. They are the simplest interesting graphs. Trees are inherently recursive structures, because cutting any edge leaves two smaller trees.
	* Directed acyclic graphs are called $DAGs$.
	* They arise naturally in scheduling problems, where a directed edge $(x, y)$ indicates that activity $x$ must occur before $y$.
	* An operation called topological sorting orders the vertices of a DAG to respect these precedence constraints. Topological sorting is typically the first step of any algorithm on a DAG.
* $Implicit$ vs $Explicit$
	* Certain graphs are not explicitly constructed and then traversed, but built as we use them.
	* It is often easier to work with an implicit graph than to explicitly construct and store the entire thing prior to analysis.

> [!Error] 7.2 Data Structures for Graphs

* Selecting the right graph data structure can have an enormous impact on performance. Your two basic choices are adjacency matrices and adjacency lists. We assume the graph $G = (V, E)$ contains $n$ vertices and $m$ edges.

| Comparison | Winner |
| :- | :-: |
| faster to test if $(x, y)$ is in graph? | adjacency matrices |
| faster to find the degree of a vertex? | adjacency lists |
| less memory on sparse graphs? | adjacency lists $(m + n)$ vs. $(n^2)$ |
| less memory on dense graphs? | adjacency matrices (a small win) |
| edge insertion or deletion? | adjacency matrices $O(1)$ vs. $O(d)$ |
| faster to traverse the graph? | adjacency lists $Θ(m + n)$ vs. $Θ(n^2)$ |
| better for most problems? | adjacency lists |

---
* $Adjacency\ matrix$
	* We can represent $G$ using an $n × n$ matrix $M$, where element $M[i, j] = 1$ if $(i, j)$ is an edge of $G$, and $0$ if it isn’t.
	* This allows fast answers to the question “is $(i, j)$ in $G$?”, and rapid updates for edge insertion and deletion.
	* It may use excessive space for graphs with many vertices and relatively few edges, however.
* Consider a graph that represents the street map of Manhattan in New York City. Every junction of two streets will be a vertex of the graph. Neighboring junctions are connected by edges. How big is this graph? Manhattan is basically a grid of $15$ avenues each crossing roughly $200$ streets. This gives us about $3,000$ vertices and $6,000$ edges, since almost all vertices neighbor four other vertices and each edge is shared between two vertices. This is a modest amount of data to store, yet an adjacency matrix would have $3,000 × 3,000 = 9,000,000$ elements, almost all of them empty!
* There is some potential to save space by packing multiple bits per word or using a symmetric-matrix data structure (e.g. triangular matrix) for undirected graphs. But these methods lose the simplicity that makes adjacency matrices so appealing and, more critically, remain inherently quadratic even for sparse graphs.
---
> [!Tip] Adjacency lists are the right data structure for most applications of graphs.
* $Adjacency\ lists$
* We can more eficiently represent sparse graphs by using linked lists to store the neighbors of each vertex.
* Adjacency lists require pointers, but are not frightening once you have experience with linked structures.
* Adjacency lists make it harder to verify whether a given edge $(i, j)$ is in $G$, since we must search through the appropriate list to find the edge.
* However, it is surprisingly easy to design graph algorithms that avoid any need for such queries.
* Typically, we sweep through all the edges of the graph in one pass via a breadth-first or depth-first traversal, and update the implications of the current edge as we visit it.
---
* $Adjacency\ lists\ data\ structure$
```cpp
#define MAXV 100                 /* maximum number of vertices */
typedef struct edgenode {
	int y;                       /* adjacency info */
	int weight;                  /* edge weight, if any */
	struct edgenode *next;       /* next edge in list */
} edgenode;

typedef struct {
	edgenode *edges[MAXV + 1];   /* adjacency info */
	int degree[MAXV + 1];        /* outdegree of each vertex */
	int nvertices;               /* number of vertices in the graph */
	int edges;                   /* number of edges in the graph */
	int directed;                /* is the graph directed? */
} graph;
```
* We represent directed edge $(x, y)$ by an $edgenode$ $y$ in $x$’s adjacency list.
* The degree field of the graph counts the number of meaningful entries for the given vertex.
* An undirected edge $(x, y)$ appears twice in any adjacency-based graph structure, once as $y$ in $x$’s list, and the other as $x$ in $y$’s list.
* The Boolean ﬂag directed identifies whether the given graph is to be interpreted as directed or undirected.
* To demonstrate the use of this data structure, we show how to read a graph from a file. A typical graph file format consists of an initial line giving the number of vertices and edges in the graph, followed by a list of the edges, one vertex pair per line.
* We start by initialising the structure:
```cpp
void initialize_graph(graph *g, bool directed) {
	int i;	/* counter */
	
	g->nvertices = 0;
	g->nedges = 0;
	g->directed = directed;
	
	for (i = 1; i <= MAXV; i++) {
		g->degree[i] = 0;
	}
	
	for (i = 1; i <= MAXV; i++) {
		g->edges[i] = NULL;
	}
}
```
* Then we actually read the graph file, inserting each edge into this structure:
```cpp
void read_graph(graph *g, bool directed) {
	int i;     /* counter */
	int m;     /* number of edges */
	int x, y;  /* vertices in edge (x,y) */
	
	initialize_graph(g, directed);
	
	scanf("%d %d", &(g->nvertices), &m);
	
	for (i = 1; i <= m; i++) {
		scanf("%d %d", &x, &y);
		insert_edge(g, x, y, directed);
	}
}
```
* The critical routine is $insert\_edge$. The new $edgenode$ is inserted at the beginning of the appropriate adjacency list, since order doesn’t matter. We parameterise our insertion with the directed Boolean ﬂag, to identify whether we need to insert two copies of each edge or only one. Note the use of recursion to insert the copy:
```cpp
void insert_edge(graph *g, int x, int y, bool directed) {
	edgenode *p;     /* temporary pointer */

	p = malloc(sizeof(edgenode));   /* allocate edgenode storage */

	p->weight = 0;
	p->y = y;
	p->next = g->edges[x];

	g->edges[x] = p; /* insert at head of list */

	g->degree[x]++;
	
	if (!directed) {
		insert_edge(g, y, x, true);
	} else {
		g->nedges++;
	}
}
```
* Printing the associated graph is just a matter of two nested loops: one through the vertices, and the second through adjacent edges:
```cpp
void print_graph(graph *g) {
	int i;       /* counter */
	edgenode *p; /* temporary pointer */
	
	for (i = 1; i <= g->nvertices; i++) {
		printf("%d: ", i);
		p = g->edges[i];
		while (p != NULL) {
			printf(" %d", p->y);
			p = p->next;
		}
		printf("\n");
	}
}
```

> [!Error] 7.3 War Story I

* Three main lessons can be taken away from our experience developing $Combinatorica$:
* $To\ make\ a\ program\ run\ faster,\ just\ wait$ – Sophisticated hardware eventually trickles down to everybody. We observe a speedup of more than $200$-fold for the original version of $Combinatorica$ as a consequence of $15$ years of hardware evolution. In this context, the further speedups we obtained from upgrading the package become particularly dramatic.
* $Asymptotics\ eventually\ do\ matter$ – It was my mistake not to anticipate future developments in technology. While no one has a crystal ball, it is fairly safe to say that future computers will have more memory and run faster than today’s. This gives the edge to asymptotically more eficient algorithms/data structures, even if their performance is close on today’s instances. If the implementation complexity is not substantially greater, play it safe and go with the better algorithm.
* $Constant\ factors\ can\ matter$ – With the growing importance of the study of networks, $Wolfram\ Research$ has recently moved basic graph data structures into the core of $Mathematica$. This permits them to be written in a compiled instead of interpreted language, speeding all operations by about a factor of $10$ over $Combinatorica$. Speeding up a computation by a factor of $10$ is often very important, taking it from a week down to a day, or a year down to a month. Constants can matter in practice.

> [!Error] 7.4 War Story II

> [!Tip]
> Even elementary problems like initializing data structures can prove to be bottlenecks in algorithm development. Programs working with large amounts of data must run in linear or near-linear time. Such tight performance demands leave no room to be sloppy. Once you focus on the need for linear-time performance, an appropriate algorithm or heuristic can usually be found to do the job.

> [!Error] 7.5 Traversing a Graph

* Perhaps the most fundamental graph problem is to visit every edge and vertex in a graph in a systematic way.
* Indeed, all the basic bookkeeping operations on graphs (such as printing or copying graphs, and converting between alternative representations) are applications of graph traversal.
* Mazes are naturally represented by graphs, where each graph vertex denotes a junction of the maze, and each graph edge denotes a passageway in the maze. Thus, any graph traversal algorithm must be powerful enough to get us out of an arbitrary maze. For eficiency, we must make sure we don’t get trapped in the maze and visit the same place repeatedly. For correctness, we must do the traversal in a systematic way to guarantee that we find a way out of the maze.
* Our search must take us through every edge and vertex in the graph.
* The key idea behind graph traversal is to mark each vertex when we first visit it and keep track of what we have not yet completely explored. Bread crumbs and unravelled threads have been used to mark visited places in fairy-tale mazes, but we will rely on Boolean ﬂags or enumerated types.
* Each vertex will exist in one of three states:
	* $Undiscovered$: the vertex is in its initial, virgin state.
	* $Discovered$: the vertex has been found, but we have not yet checked out all its incident edges.
	* $Processed$: the vertex after we have visited all of its incident edges.
* Obviously, a vertex cannot be processed until after we discover it, so the state of each vertex progresses from $undiscovered$ to $discovered$ to processed over $the$ course of the traversal.
* We must also maintain a structure containing the vertices that we have $discovered$ but not yet completely $processed$. Initially, only the single start vertex is considered to be $discovered$. To completely explore a vertex $v$, we must evaluate each edge leaving $v$. If an edge goes to an $undiscovered$ vertex $x$, we mark $x$ $discovered$ and add it to the list of work to do in the future. If an edge goes to a $processed$ vertex, we ignore that vertex, because further contemplation will tell us nothing new about the graph. Similarly, we can ignore any edge going to a $discovered$ but not $processed$ vertex, because that destination already resides on the list of vertices to process.
* Each undirected edge will be considered exactly twice, once when each of its endpoints is explored. Directed edges will be considered only once, when exploring the source vertex. Every edge and vertex in the connected component must eventually be visited. Why? Suppose that there exists a vertex $u$ that remains unvisited, whose neighbor $v$ was visited. This neighbor $v$ will eventually be explored, after which we will certainly visit $u$. Thus, we must find everything that is there to be found.

> [!Error] 7.6 Breadth-first Search

* At some point during the course of a traversal, every node in the graph changes state from $undiscovered$ to $discovered$.
* In a breadth-first search of an undirected graph, we assign a direction to each edge, from the $discoverer$ $u$ to the $discovered$ $v$. We thus denote $u$ to be the parent of $v$.
* Since each node has exactly one parent, except for the root, this defines a tree on the vertices of the graph.
* This tree defines a shortest path from the root to every other node in the tree. This property makes breadth-first search very useful in shortest path problems.
```pseudocode
BFS(G, s)
	Initialize each vertex u ∈ V[G] so
		state[u] = “undiscovered”
		p[u] = nil, i.e. no parent is in the BFS tree
	state[s] = “discovered”
	Q = {s}
	while Q != ∅ do
		u = dequeue[Q]
		process vertex u if desired
		for each vertex v that is adjacent to u
			process edge (u, v) if desired
			if state[v] = “undiscovered” then
				state[v] = “discovered”
				p[v] = u
				enqueue[Q, v]
		state[u] = “processed”
```
* The graph edges that do not appear in the breadth-first search tree also have special properties. For undirected graphs, non-tree edges can point only to vertices on the same level as the parent vertex, or to vertices on the level directly below the parent. These properties follow easily from the fact that each path in the tree must be a shortest path in the graph. For a directed graph, a back-pointing edge $(u, v)$ can exist whenever $v$ lies closer to the root than $u$ does.
---
* **Implementation**
```cpp
bool processed[MAXV+1];  /* which vertices have been processed */
bool discovered[MAXV+1]; /* which vertices have been found */
int parent[MAXV+1];      /* discovery relation */
```
* Each vertex is initialized as $undiscovered$:
```cpp
void initialize_search(graph *g) {
	int i; /* counter */
	time = 0;
	for (i = 0; i <= g->nvertices; i++) {
		processed[i] = false;
		discovered[i] = false;
		parent[i] = -1;
	}
}
```
* Once a vertex is discovered, it is placed on a queue. Since we process these vertices in first-in, first-out (fiFO) order, the oldest vertices are expanded first, which are exactly those closest to the root:
```cpp
void bfs(graph *g, int start) {
	queue q;     /* queue of vertices to visit */
	int v;       /* current vertex */
	int y;       /* successor vertex */
	edgenode *p; /* temporary pointer */
	
	init_queue(&q);
	enqueue(&q, start);
	discovered[start] = true;
	
	while (!empty_queue(&q)) {
		v = dequeue(&q);
		process_vertex_early(v);
		processed[v] = true;
		p = g->edges[v];
		while (p != NULL) {
			y = p->y;
			if ((!processed[y]) || g->directed) {
				process_edge(v, y);
			}
			if (!discovered[y]) {
				enqueue(&q,y);
				discovered[y] = true;
				parent[y] = v;
			}
			p = p->next;
		}
		process_vertex_late(v);
	}
}
```

> [!subsubsection] 7.6.1 Exploiting Traversal

* The exact behavior of $\text{bfs}$ depends upon the functions $\text{process\_vertex\_early()}$, $\text{process\_vertex\_late()}$, and $\text{process\_edge()}$. Through these functions, we can customise what the traversal does as it makes its one oficial visit to each edge and each vertex. Initially, we will do all vertex processing on entry, so $\text{process\_vertex\_late()}$ returns without action:
```cpp
void process_vertex_late(int v) {}
```
* By setting the active functions to
```cpp
void process_vertex_early(int v) {
	printf("processed vertex %d\n", v);
}
void process_edge(int x, int y) {
	printf("processed edge (%d,%d)\n", x, y);
}
```
* we print each vertex and edge exactly once.
* If we instead set process edge to
```cpp
void process_edge(int x, int y) {
	nedges = nedges + 1;
}
```
* we get an accurate count of the number of edges. Different algorithms perform different actions on vertices or edges as they are encountered. These functions give us the freedom to easily customise these actions.

> [!subsubsection] 7.6.2 finding Paths

* The parent array that is filled over the course of $\text{bfs()}$ is very useful for finding interesting paths through a graph.
* The vertex that first discovered vertex $i$ is defined as the $\text{parent[i]}$.
* Every vertex is discovered once during the course of traversal, so every node has a parent, except for the start node.
* This parent relation defines a tree of discovery, with the start node as the root of the tree.
* Because vertices are discovered in order of increasing distance from the root, this tree has a very important property. The unique tree path from the root to each node $x ∈ V$ uses the smallest number of edges (or equivalently, intermediate nodes) possible on any root-to-$x$ path in the graph.
* We can reconstruct this path by following the chain of ancestors from $x$ to the root. Note that we have to work backward. We cannot find the path from the root to $x$, because this does not agree with the direction of the parent pointers. Instead, we must find the path from $x$ to the root. Since this is the reverse of how we normally want the path, we can either (1) store it and then explicitly reverse it using a stack, or (2) let recursion reverse it for us, as follows:
```cpp
void find_path(int start, int end, int parents[]) {
	if ((start == end) || (end == -1)) {
		printf("\n%d", start);
	} else {
		find_path(start, parents[end], parents);
		printf(" %d", end);
	}
}
```
* There are two points to remember when using breadth-first search to find a shortest path from $x$ to $y$:
	* first, the shortest path tree is only useful if $BFS$ was performed with $x$ as the root of the search.
	* Second, $BFS$ gives the shortest path only if the graph is unweighted.

> [!Error] 7.7 Applications of Breadth-first Search

* Many elementary graph algorithms perform one or two traversals of the graph, while doing something along the way. Properly implemented using adjacency lists, any such algorithm is destined to be linear, since $BFS$ runs in $O(n + m)$ time for both directed and undirected graphs. This is optimal, since this is as fast as one can ever hope to just read an $n$-vertex, $m$-edge graph. 
* The trick is seeing when such traversal approaches are destined to work.

> [!subsubsection] 7.7.1 Connected Components

> [!Info] Reminder: $Connected\ Components$
> We say that a graph is connected if there is a path between any two vertices. Every person can reach every other person through a chain of links if the friendship graph is $connected$. A $connected\ component$ of an undirected graph is a maximal set of vertices such that there is a path between every pair of vertices. The components are separate “pieces” of the graph such that there is no connection between the pieces. If we envision tribes in remote parts of the world that have not yet been encountered, each such tribe would form a separate connected component in the friendship graph. A remote hermit, or extremely uncongenial fellow, would represent a connected component of one vertex.

* An amazing number of seemingly complicated problems reduce to finding or counting connected components.
* Connected components can be found using breadth-first search, since the vertex order does not matter.
* We begin by performing a search starting from an arbitrary vertex. Anything we discover during this search must be part of the same connected component. We then repeat the search from any undiscovered vertex (if one exists) to define the next component, and so on until all vertices have been found:
```cpp
void connected_components(graph *g) {
	int c;  /* component number */
	int i;  /* counter */
	initialize_search(g);
	c = 0;
	for (i = 1; i <= g->nvertices; i++) {
		if (!discovered[i]) {
			c = c + 1;
			printf("Component %d:", c);
			bfs(g, i);
			printf("\n");
		}
	}
}
```

> [!subsubsection] 7.7.2 Two-Coloring Graphs

* The $vertex\text{-}coloring$ problem seeks to assign a label (or color) to each vertex of a graph such that no edge links any two vertices of the same color. We can easily avoid all conﬂicts by assigning each vertex a unique color. However, the goal is to use as few colors as possible. Vertex coloring problems often arise in scheduling applications, such as register allocation in compilers.

> [!info] Reminder: $Bipartite\ Graphs$
> A graph is $bipartite$ if it can be colored without conﬂicts while using only two colors.

* Bipartite graphs are important because they arise naturally in many applications.
* Consider the “mutually interested-in” graph in a heterosexual world, where people consider only those of opposing gender. In this simple model, gender would define a two-coloring of the graph. But how can we find an appropriate two-coloring of such a graph, thus separating men from women? Suppose we declare by fiat that the starting vertex is “male.” All vertices adjacent to this man must be “female,” provided the graph is indeed bipartite.
* We can augment breadth-first search so that whenever we discover a new vertex, we color it the opposite of its parent. We check whether any non-tree edge links two vertices of the same color. Such a conﬂict means that the graph cannot be two-colored. If the process terminates without conﬂicts, we have constructed a proper two-coloring.
```cpp
void twocolor(graph *g) {
	int i;   /* counter */
	for (i = 1; i <= (g->nvertices); i++) {
		color[i] = UNCOLORED;
	}
	bipartite = true;
	initialize_search(g);
	for (i = 1; i <= (g->nvertices); i++) {
		if (!discovered[i]) {
			color[i] = WHITE;
			bfs(g, i);
		}
	}
}

void process_edge(int x, int y) {
	if (color[x] == color[y]) {
		bipartite = false;
		printf("Warning: not bipartite, due to (%d,%d)\n", x, y);
	}
	color[y] = complement(color[x]);
}

int complement(int color) {
	if (color == WHITE) {
		return(BLACK);
	}
	if (color == BLACK) {
		return(WHITE);
	}
	return(UNCOLORED);
}
```

> [!Error] 7.8 Depth-first Search

* The difference between $BFS$ and $DFS$ lies in the order in which they explore vertices. This order depends completely upon the container data structure used to store the discovered but not processed vertices.
	* $Queue$: By storing the vertices in a first-in, first-out (fiFO) queue, we explore the oldest unexplored vertices first. Our explorations thus radiate out slowly from the starting vertex, defining a breadth-first search.
	* $Stack$: By storing the vertices in a last-in, first-out (LIFO) stack, we explore the vertices by forging steadily along a path, visiting a new neighbor if one is available, and backing up only when we are surrounded by previously discovered vertices. Our explorations thus quickly wander away from the starting point, defining a depth-first search.
* Our implementation of $dfs$ maintains a notion of traversal time for each vertex. Our time clock ticks each time we enter or exit a vertex. We keep track of the entry and exit times for each vertex.
```pseudocode
DFS(G, u)
	state[u] = “discovered”
	process vertex u if desired
	time = time + 1
	entry[u] = time
	for each vertex v that is adjacent to u
		process edge (u, v) if desired
		if state[v] = “undiscovered” then
			p[v] = u
			DFS(G, v)
	state[u] = “processed”
	exit[u] = time
	time = time + 1
```
* The time intervals have interesting and useful properties with respect to depth-first search:
	* $Who\ is\ an\ ancestor?$: Suppose that $x$ is an ancestor of $y$ in the $DFS$ tree. This implies that we must enter $x$ before $y$, since there is no way we can be born before our own parent or grandparent! We also must exit $y$ before we exit $x$, because the mechanics of $DFS$ ensure we cannot exit $x$ until after we have backed up from the search of all its descendants. Thus, the time interval of $y$ must be properly nested within the interval of ancestor $x$.
	* $How\ many\ descendants?$ – The difference between the exit and entry times for $v$ tells us how many descendants $v$ has in the $DFS$ tree. The clock gets incremented on each vertex entry and vertex exit, so half the time difference denotes the number of descendants of $v$.
* We will use these entry and exit times in several applications of depth-first search, particularly topological sorting and biconnected/strongly connected components.
* The other important property of a depth-first search is that it partitions the edges of an undirected graph into exactly two classes:
	* The $tree\ edges$ discover new vertices, and are those encoded in the parent relation.
	* $Back\ edges$ are those whose other endpoint is an ancestor of the vertex being expanded, so they point back into the tree.
* An amazing property of depth-first search is that all edges fall into one of these two classes. Why can’t an edge go to a sibling or cousin node, instead of an ancestor? All nodes reachable from a given vertex v are expanded before we finish with the traversal from v, so such topologies are impossible for undirected graphs. This edge classification proves fundamental to the correctness of $DFS$-based algorithms.
---
* **Implementation**
```cpp
void dfs(graph *g, int v) {
	edgenode *p;   /* temporary pointer */
	int y;         /* successor vertex */
	if (finished) {
		return;    /* allow for search termination */
	}
	discovered[v] = true;
	time = time + 1;
	entry_time[v] = time;
	process_vertex_early(v);
	p = g->edges[v];
	while (p != NULL) {
		y = p->y;
		if (!discovered[y]) {
			parent[y] = v;
			process_edge(v, y);
			dfs(g, y);
		} else if (((!processed[y]) && (parent[v] != y)) || (g->directed)) {
			process_edge(v, y);
		}
		if (finished) {
			return;
		}
		p = p->next;
	}
	process_vertex_late(v);
	time = time + 1;
	exit_time[v] = time;
	processed[v] = true;
}
```
* Depth-first search uses essentially the same idea as $backtracking$. Both involve exhaustively searching all possibilities by advancing if it is possible, and backing up only when there is no remaining unexplored possibility for further advance. Both are most easily understood as recursive algorithms.

> [!Error] 7.9 Applications of Depth-first Search

* The correctness of a $DFS$-based algorithm depends upon specifics of exactly when we process the edges and vertices. We can process vertex $v$ either before we have traversed any outgoing edge from $v$ ($\text{process\_vertex\_early()}$), or after we have finished processing all of them ($\text{process\_vertex\_late()}$). Sometimes we will take special actions at both times, say $\text{process\_vertex\_early()}$ to initialize a vertex-specific data structure, which will be modified on edge-processing operations and then analyzed afterwards using $\text{process\_vertex\_late()}$.
* In undirected graphs, each edge $(x, y)$ sits in the adjacency lists of vertex $x$ and $y$. There are thus two potential times to process each edge $(x, y)$, namely when exploring $x$ and when exploring $y$. The labelling of edges as tree edges or back edges occurs the first time the edge is explored. This first time we see an edge is usually a logical time to do edge-specific processing. Sometimes, we may want to take different action the second time we see an edge.

> [!subsubsection] 7.9.1 finding Cycles

* Back edges are the key to finding a cycle in an undirected graph. If there is no back edge, all edges are tree edges, and no cycle exists in a tree. But $any$ back edge going from $x$ to an ancestor $y$ creates a cycle with the tree path from $y$ to $x$. Such a cycle is easy to find using $dfs$:
```cpp
void process_edge(int x, int y) {
	if (parent[y] != x) {   /* found back edge! */
		printf("Cycle from %d to %d:", y, x);
		find_path(y, x, parent);
		finished = true;
	}
}
```
* The correctness of this cycle detection algorithm depends upon processing each undirected edge exactly once. We use the finished ﬂag to terminate after finding the first cycle. Without it we would waste time discovering a new cycle with every back edge before stopping; a complete graph has $Θ(n^2)$ such cycles.

> [!subsubsection] 7.9.2 Articulation Vertices

> [!Info] Definition: $Articulation\ Vertex$
> An $articulation\ vertex$ or $cut\text{-}node$ is a single vertex whose deletion disconnects a connected component of the graph.

* Any graph that contains an articulation vertex is inherently fragile, because deleting $v$ causes a loss of connectivity between other nodes.

> [!Info] Definition: $Graph\ Connectivity$
> In general, the $connectivity$ of a graph is the smallest number of vertices whose deletion will disconnect the graph. The connectivity is $1$ if the graph has an articulation vertex. More robust graphs without such a vertex are said to be $biconnected$.

* What might the depth-first search tree tell us about articulation vertices?
* This tree connects all the vertices of a connected component of the graph. If the $DFS$ tree represented the entirety of the graph, all internal (non-leaf) nodes would be articulation vertices, since deleting any one of them would separate a leaf from the root. But blowing up a leaf would not disconnect the tree, because it connects no one but itself to the main trunk.
* The root of the search tree is a special case. If it has only one child, it functions as a leaf. But if the root has two or more children, its deletion disconnects them, making the root an articulation vertex.
* General graphs are more complex than trees. But a depth-first search of a general graph partitions the edges into tree edges and back edges. Think of these back edges as security cables linking a vertex back to one of its ancestors. The security cable from $x$ back to $y$ ensures that none of the vertices on the tree path between $x$ and $y$ can be articulation vertices. Delete any of these vertices, and the security cable will still hold all of them to the rest of the tree.
* finding articulation vertices requires keeping track of the extent to which back edges (i.e., security cables) link chunks of the $DFS$ tree back to ancestor nodes.
* Let $\text{reachable\_ancestor[v]}$ denote the earliest reachable ancestor of vertex $v$, meaning the oldest ancestor of $v$ that we can reach from a descendant of $v$ by using a back edge. Initially, $\text{reachable\_ancestor[v] = v}$:
```cpp
int reachable_ancestor[MAXV+1]; /* earliest reachable ancestor of v */
int tree_out_degree[MAXV+1];    /* DFS tree outdegree of v */
void process_vertex_early(int v) {
	reachable_ancestor[v] = v;
}
```
* We update $\text{reachable\_ancestor[v]}$ whenever we encounter a back edge that takes us to an earlier ancestor than we have previously seen. The relative age/rank of our ancestors can be determined from their $\text{entry\_time}$’s:
```cpp
void process_edge(int x, int y) {
	int class;   /* edge class */
	class = edge_classification(x, y);
	if (class == TREE) {
		tree_out_degree[x] = tree_out_degree[x] + 1;
	}
	
	if ((class == BACK) && (parent[x] != y)) {
		if (entry_time[y] < entry_time[reachable_ancestor[x]]) {
			reachable_ancestor[x] = y;
		}
	}
}
```
* The key issue is determining how the reachability relation impacts whether vertex $v$ is an articulation vertex. There are three cases. Note that these cases are not mutually exclusive. A single vertex $v$ might be an articulation vertex for multiple reasons:
	* $Root\ cut\text{-}nodes$ – If the root of the $DFS$ tree has two or more children, it must be an articulation vertex. No edges from the subtree of the second child can possibly connect to the subtree of the first child.
	* $Bridge\ cut\text{-}nodes$ – If the earliest reachable vertex from $v$ is $v$, then deleting the single edge ($parent[v]$, $v$) disconnects the graph. Clearly $parent[v]$ must be an articulation vertex, since it cuts $v$ from the graph. Vertex $v$ is also an articulation vertex unless it is a leaf of the $DFS$ tree. For any leaf, nothing falls off when you cut it.
	* $Parent\ cut\text{-}nodes$ – If the earliest reachable vertex from $v$ is the parent of $v$, then deleting the parent must sever $v$ from the tree unless the parent is the root. This is always the case for the deeper vertex of a bridge, unless it is a leaf.
* The routine below systematically evaluates each of these three conditions as we back up from the vertex after traversing all outgoing edges.
* We use $entry\_time[v]$ to represent the age of vertex $v$. The reachability time $time\_v$ calculated below denotes the oldest vertex that can be reached using back edges. Getting back to an ancestor above $v$ rules out the possibility of $v$ being a $cut\text{-}node$:
```cpp
void process_vertex_late(int v) {
	bool root;         /* is parent[v] the root of the DFS tree? */
	int time_v;        /* earliest reachable time for v */
	int time_parent;   /* earliest reachable time for parent[v] */
	if (parent[v] == -1) { /* test if v is the root */
		if (tree_out_degree[v] > 1) {
			printf("root articulation vertex: %d \n",v);
		}
		return;
	}
	root = (parent[parent[v]] == -1); /* is parent[v] the root? */
	if (!root) {
		if (reachable_ancestor[v] == parent[v]) {
			printf("parent articulation vertex: %d \n", parent[v]);
		}
		if (reachable_ancestor[v] == v) {
			printf("bridge articulation vertex: %d \n",parent[v]);
			if (tree_out_degree[v] > 0) {  /* is v is not a leaf? */
				printf("bridge articulation vertex: %d \n", v);
			}
		}
	}
	time_v = entry_time[reachable_ancestor[v]];
	time_parent = entry_time[reachable_ancestor[parent[v]]];
	if (time_v < time_parent) {
		reachable_ancestor[parent[v]] = reachable_ancestor[v];
	}
}
```
* The last lines of this routine govern when we back up from a node’s highest reachable ancestor to its parent, namely whenever it is higher than the parent’s earliest ancestor to date.
* We can alternatively talk about vulnerability in terms of edge failures instead of vertex failures. Perhaps our vandal would find it easier to cut a cable instead of blowing up a switching station. A single edge whose deletion disconnects the graph is called a $bridge$; any graph without such an edge is said to be $edge\text{-}biconnected$.
* Identifying whether a given edge $(x, y)$ is a bridge is easily done in linear time, by deleting the edge and testing whether the resulting graph is connected. In fact all bridges can be identified in the same $O(n + m)$ time using $DFS$. Edge $(x, y)$ is a bridge if $(1)$ it is a tree edge, and $(2)$ no back edge connects from $y$ or below to $x$ or above. This can be computed with a appropriate modification to the $process\_late\_vertex$ function.

> [!Error] 7.10 Depth-first Search on Directed Graphs

* When traversing $undirected$ graphs, every edge is either in the depth-first search tree or will be a back edge to an ancestor in the tree. It is important to understand why. Might we encounter a “forward edge” $(x, y)$, directed toward a descendant vertex? No, because in this case, we would have first traversed $(x, y)$ while exploring $y$, making it a back edge. Might we encounter a “cross edge” $(x, y)$, linking two unrelated vertices? Again no, because we would have first discovered this edge when we explored $y$, making it a tree edge.
* But for directed graphs, depth-first search labellings can take on a wider range of possibilities. Indeed, all four of the edge cases can occur in traversing directed graphs. This classification still proves useful in organizing algorithms on directed graphs, because we typically take a different action on edges from each different class.
* The correct labeling of each edge can be readily determined from the state, discovery time, and parent of each vertex, as encoded in the following function:
```cpp
int edge_classification(int x, int y) {
	if (parent[y] == x) {
		return(TREE);
	}
	if (discovered[y] && !processed[y]) {
		return(BACK);
	}
	if (processed[y] && (entry_time[y]>entry_time[x])) {
		return(FORWARD);
	}
	if (processed[y] && (entry_time[y]<entry_time[x])) {
		return(CROSS);
	}
	printf("Warning: self loop (%d,%d)\n", x, y);
	return -1;
}
```

> [!subsubsection] 7.10.1 Topological Sorting

* Topological sorting is the most important operation on directed acyclic graphs ($DAG$s). It orders the vertices on a line such that all directed edges go from left to right. Such an ordering cannot exist if the graph contains a directed cycle, because there is no way you can keep moving right on a line and still return back to where you started from!
* Each $DAG$ has at least one topological sort. The importance of topological sorting is that it gives us an ordering so we can process each vertex before any of its successors. Suppose the directed edges represented precedence constraints, such that edge $(x, y)$ means job $x$ must be done before job $y$. Any topological sort then defines a feasible schedule. Indeed, there can be many such orderings for a given $DAG$.
* But the applications go deeper. Suppose we seek the shortest (or longest) path from $x$ to $y$ in a $DAG$. No vertex $v$ appearing after $y$ in the topological order can possibly contribute to any such path, because there will be no way to get from $v$ back to $y$. We can appropriately process all the vertices from left to right in topological order, considering the impact of their outgoing edges, and know that we will have looked at everything we need before we need it. Topological sorting proves very useful in essentially any algorithmic problem on $DAG$s.
* Topological sorting can be performed eficiently using depth-first search. A directed graph is a $DAG$ iff no back edges are encountered. Labeling the vertices in the reverse order that they are marked processed defines a topological sort of a $DAG$. Why? Consider what happens to each directed edge $(x, y)$ as we encounter it exploring vertex $x$:
	* If $y$ is currently undiscovered, then we start a $DFS$ of $y$ before we can continue with $x$. Thus, $y$ must be marked processed before $x$ is, so $x$ appears before $y$ in the topological order, as it must.
	* If $y$ is discovered but not processed, then $(x, y)$ is a back edge, which is impossible in a $DAG$ because it creates a cycle.
	* If $y$ is processed, then it will have been so labeled before $x$. Therefore, $x$ appears before $y$ in the topological order, as it must.
```cpp
void process_vertex_late(int v) {
	push(&sorted, v);
}

void process_edge(int x, int y) {
	int class; /* edge class */
	class = edge_classification(x, y);
	if (class == BACK) {
		printf("Warning: directed cycle found, not a DAG\n");
	}
}

void topsort(graph *g) {
	int i;  /* counter */
	init_stack(&sorted);
	for (i = 1; i <= g->nvertices; i++) {
		if (!discovered[i]) {
			dfs(g, i);
		}
	}
	print_stack(&sorted); /* report topological order */
}
```
* We push each vertex onto a stack as soon as we have evaluated all outgoing edges. The top vertex on the stack always has no incoming edges from any vertex on the stack. Repeatedly popping them off yields a topological ordering.

> [!subsubsection] 7.10.2 Strongly Connected Components

* A directed graph is $strongly\ connected$ if there is a directed path between any two vertices. Road networks had better be strongly connected: otherwise there will be places you can drive to but not drive home from without violating one-way signs.
* It is straightforward to use graph traversal to test whether a graph $G = (V, E)$ is strongly connected in linear time. The graph is strongly connected iff from any vertex $v$ in $G$ $(1)$ all vertices are reachable from $v$ and $(2)$ all vertices can reach $v$. To test if condition $(1)$ holds, we can do a $BFS$ or $DFS$ traversal from $v$ to establish whether all vertices get discovered. If so, all must be reachable from $v$.
* To test if there are paths from every vertex to $v$, we construct the transpose graph $G^T = (V, E^{'})$, which has the same vertex and edge set as $G$ but with all edges reversed—that is, directed edge $(x, y) ∈ E$ iff $(y, x) ∈ E^{'}$ .
```cpp
graph *transpose(graph *g) {
	graph *gt;   /* transpose of graph g */
	int x;       /* counter */
	edgenode *p; /* temporary pointer */
	gt = (graph *) malloc(sizeof(graph));
	initialize_graph(gt, true); /* initialize directed graph */
	gt->nvertices = g->nvertices;
	for (x = 1; x <= g->nvertices; x++) {
		p = g->edges[x];
		while (p != NULL) {
			insert_edge(gt, p->y, x, true);
			p = p->next;
		}
	}
	return(gt);
}
```
* Any path from $v$ to $z$ in $G^T$ corresponds to a path from $z$ to $v$ in $G$. By doing a second $DFS$, this one from $v$ in $G^T$, we identify all vertices that have paths to $v$ in $G$.
* All directed graphs can be partitioned into strongly connected components, such that a directed path exists between every pair of vertices in the component. The set of such components can be determined using a more subtle variation of this double $DFS$ approach:
```cpp
void strong_components(graph *g) {
	graph *gt;  /* transpose of graph g */
	int i;      /* counter */
	int v;      /* vertex in component */
	init_stack(&dfs1order);
	initialize_search(g);
	for (i = 1; i <= (g->nvertices); i++) {
		if (!discovered[i]) {
			dfs(g, i);
		}
	}
	gt = transpose(g);
	initialize_search(gt);
	components_found = 0;
	while (!empty_stack(&dfs1order)) {
		v = pop(&dfs1order);
		if (!discovered[v]) {
			components_found ++;
			printf("Component %d:", components_found);
			dfs2(gt, v);
			printf("\n");
		}
	}
}
```
* The first traversal pushes the vertices on a stack in the reverse order they were processed, just as with topological sort. The connection makes sense: $DAG$s are directed graphs where each vertex forms its own strongly connected component. On a $DAG$, the top vertex on the stack will be one that cannot reach any other vertex. The bookkeeping here is identical to topological sort:
```cpp
void process_vertex_late(int v) {
	push(&dfs1order,v);
}
```
* The second traversal, on the transposed graph, behaves like the connected component algorithm, except we consider starting vertices in the order they appear on the stack. Each traversal from $v$ will discover all reachable vertices from the transpose $G^T$ , meaning the vertices that have paths to $v$ in $G$. These reachable vertices define the strongly connected component of $v$, because they represent the least reachable vertices in $G$:
```cpp
void process_vertex_early2(int v) {
	printf(" %d", v);
}
```
* The correctness of this is subtle. Observe that first $DFS$ places vertices on the stack in groups based on reachability from successive starting vertices in the original directed graph $G$. Thus, the vertices in the top group have the property that none were reachable from any earlier group vertex. The second traversal in $G^T$ , starting from the last vertex $v$ of $G$, finds all the reachable vertices from $v$ in $G^T$ that themselves reach $v$, meaning they define a strongly connected component.

### Chapter 8: Weighted Graph Algorithms
> `pg: 34`
> `time req: 3' 20"`
> `time done: 3' 22"`
> `performance: 99%`
>
> `practice time req: 5' 47"`

> [!Error] 8.1 Minimum Spanning Trees

* A spanning tree of a connected graph $G = (V, E)$ is a subset of edges from $E$ forming a tree connecting all vertices of $V$. For edge-weighted graphs, we are particularly interested in the $minimum\ spanning\ tree$—the spanning tree whose sum of edge weights is as small as possible.
* Minimum spanning trees are the answer whenever we need to connect a set of points (representing cities, homes, junctions, or other locations) cheaply using the smallest amount of roadway, wire, or pipe.
* Any tree is the smallest possible connected graph in terms of number of edges, but the minimum spanning tree is the smallest connected graph in terms of edge weight.
* A minimum spanning tree minimises the total edge weight over all possible spanning trees. However, there can be more than one minimum spanning tree of a given graph.
* Indeed, all spanning trees of an unweighted (or equally weighted) graph $G$ are minimum spanning trees, since each contains exactly $n − 1$ equal-weight edges. Such a spanning tree can be found using either $DFS$ or $BFS$.

> [!subsubsection] 8.1.1 Prim's Algorithm

* Prim’s minimum spanning tree algorithm starts from one vertex and grows the rest of the tree one edge at a time until all vertices are included.
* Greedy algorithms make the decision of what to do next by selecting the best local option from all available choices without regard to the global structure.
* Since we seek the tree of minimum weight, the natural greedy algorithm for minimum spanning tree ($MST$) repeatedly selects the smallest weight edge that will enlarge the number of vertices in the tree.
---
* **Implementation**
* Prim’s algorithm grows the minimum spanning tree in stages, starting from a given vertex. At each iteration, we add one new vertex into the spanning tree. A greedy algorithm sufices for correctness: we always add the lowest- weight edge linking a vertex in the tree to a vertex on the outside. The simplest implementation of this idea would assign to each vertex a Boolean variable denoting whether it is already in the tree (the array $intree$ in the code below), and then search all edges at each iteration to find the minimum-weight edge with exactly one $intree$ vertex.
* Our implementation is somewhat smarter. It keeps track of the cheapest edge linking every non-tree vertex in the tree. The cheapest such edge over all remaining non-tree vertices gets added in the next iteration. We must update the costs of getting to the non-tree vertices after each insertion. However, since the most recently inserted vertex is the only change in the tree, all possible edge-weight updates must come from its outgoing edges:
```cpp
int prim(graph *g, int start) {
	int i;                /* counter */
	edgenode *p;          /* temporary pointer */
	bool intree[MAXV+1];  /* is the vertex in the tree yet? */
	int distance[MAXV+1]; /* cost of adding to tree */
	int v;                /* current vertex to process */
	int w;                /* candidate next vertex */
	int dist;             /* cheapest cost to enlarge tree */
	int weight = 0;       /* tree weight */
	for (i = 1; i <= g->nvertices; i++) {
		intree[i] = false;
		distance[i] = MAXINT;
		parent[i] = -1;
	}
	distance[start] = 0;
	v = start;
	while (!intree[v]) {
		intree[v] = true;
		if (v != start) {
			printf("edge (%d,%d) in tree \n",parent[v],v);
			weight = weight + dist;
		}
		p = g->edges[v];
		while (p != NULL) {
			w = p->y;
			if ((distance[w] > p->weight) && (!intree[w])) {
				distance[w] = p->weight;
				parent[w] = v;
			}
			p = p->next;
		}
		dist = MAXINT;
		for (i = 1; i <= g->nvertices; i++) {
			if ((!intree[i]) && (dist > distance[i])) {
				dist = distance[i];
				v = i;
			}
		}
	}
	return(weight);
}
```
---
* **Analysis**
* Prim’s algorithm is correct, but how eficient is it? This depends on which data structures are used to implement it. In the pseudocode, Prim’s algorithm makes $n$ iterations sweeping through all $m$ edges on each iteration—yielding an $O(mn)$ algorithm.
* But our implementation avoids the need to test all $m$ edges on each pass. It only considers the $≤ n$ cheapest known edges represented in the parent array and the $≤ n$ edges out of a new tree vertex $v$ to update parent. By maintaining a Boolean ﬂag along with each vertex to denote whether it is in the tree, we test whether the current edge joins a tree with a non-tree vertex in constant time.
* The result is an $O(n^2)$ implementation of Prim’s algorithm, and a good illustration of the power of data structures to speed up algorithms. In fact, more sophisticated priority-queue data structures lead to an $O(m + n\ lg\ n)$ implementation, by making it faster to find the minimum-cost edge to expand the tree at each iteration.
* The minimum spanning tree itself can be reconstructed in two different ways.
	* The simplest method would be to augment this procedure with statements that print the edges as they are found, and totals the weight of all selected edges to get the cost.
	* Alternatively, the tree topology is encoded by the parent array, so it completely describes edges in the minimum spanning tree.

> [!subsubsection] 8.1.2 Kruskal's Algorithm

* Kruskal’s algorithm is an alternative approach to finding minimum spanning trees that proves more eficient on sparse graphs.
* Like Prim’s, Kruskal’s algorithm is greedy. Unlike Prim’s, it does not start with a particular vertex.
* Kruskal might produce a different spanning tree than Prim’s algorithm, although both will have the same weight.
* Kruskal’s algorithm builds up connected components of vertices, culminating in the complete minimum spanning tree. Initially, each vertex forms its own separate component in the tree-to-be. The algorithm repeatedly considers the lightest remaining edge and tests whether its two endpoints lie within the same connected component. If so, this edge will be discarded, because adding it would create a cycle. If the endpoints lie in different components, we insert the edge and merge the two components into one. Since each connected component always is a tree, we never need to explicitly test for cycles.
* What is the time complexity of Kruskal’s algorithm? Sorting the $m$ edges takes $O(m\ lg\ m)$ time. The while loop makes at most $m$ iterations, each testing the connectivity of two trees plus an edge. In the most simple-minded implementation, this can be done by breadth-first or depth-first search in the sparse partial tree graph with at most $n$ edges and $n$ vertices, thus yielding an $O(mn)$ algorithm.
* However, a faster implementation results if we can implement the component test in faster than $O(n)$ time. In fact, a clever data structure called union–find, can support such queries in $O(lg\ n)$ time. With this data structure, Kruskal’s algorithm runs in $O(m\ lg\ m)$ time, which is faster than Prim’s for sparse graphs.
```cpp
int kruskal(graph *g) {
	int i;                 /* counter */
	union_find s;          /* union-find data structure */
	edge_pair e[MAXV+1];   /* array of edges data structure */
	int weight=0;          /* cost of the minimum spanning tree */
	union_find_init(&s, g->nvertices);
	to_edge_array(g, e);
	qsort(&e,g->nedges, sizeof(edge_pair), &weight_compare);
	for (i = 0; i < (g->nedges); i++) {
		if (!same_component(&s, e[i].x, e[i].y)) {
			printf("edge (%d,%d) in MST\n", e[i].x, e[i].y);
			weight = weight + e[i].weight;
			union_sets(&s, e[i].x, e[i].y);
		}
	}
	return(weight);
}
```

> [!subsubsection] 8.1.3 The Union-find Data Structure

* A set partition parcels out the elements of some universal set (say the integers $1$ to $n$) into a collection of disjoint subsets, where each element is in exactly one subset. Set partitions naturally arise in graph problems such as connected components (each vertex is in exactly one connected component) and vertex coloring (a vertex may be white or black in a bipartite graph, but not both or neither).
* The connected components in a graph can be represented as a set partition. For Kruskal’s algorithm to run eficiently, we need a data structure that eficiently supports the following operations:
	* $Same\ component(v_1, v_2)$ – Do vertices $v_1$ and $v_2$ occur in the same connected component of the current graph?
	* $Merge\ components(C_1, C_2)$ – Merge the given pair of connected components into one component in response to the insertion of an edge between them.
* The two obvious data structures for this task each support only one of these operations eficiently. Explicitly labeling each element with its component number enables the same component test to be performed in constant time, but updating the component numbers after a merger would require linear time. Alternatively, we can treat the merge components operation as inserting an edge in a graph, but then we must run a full graph traversal to identify the connected components on demand.
* The union–find data structure represents each subset as a “backwards” tree, with pointers from a node to its parent. Each node of this tree contains a set element, and the name of the set is taken from the key at the root. For reasons that will become clear, we also keep track of the number of elements in the subtree rooted in each vertex $v$:
```cpp
typedef struct {
	int p[SET_SIZE+1];     /* parent element */
	int size[SET_SIZE+1];  /* number of elements in subtree i */
	int n;                 /* number of elements in set */
} union_find;
```
* We implement our desired component operations in terms of two simpler operations, $union$ and $find$:
	* $find(i)$ – find the root of the tree containing element $i$, by walking up the parent pointers until there is nowhere to go. Return the label of the root.
	* $Union(i,j)$ – Link the root of one of the trees (say containing $i$) to the root of the tree containing the other (say $j$) so $find(i)$ now equals $find(j)$.
* We seek to minimise the time it takes to execute the worst possible sequence of unions and finds. Tree structures can be very unbalanced, so we must limit the height of our trees. Our most obvious means of control is the choice of which of the two component roots becomes the root of the merged component on each union.
* To minimise the tree height, it is better to make the smaller tree the subtree of the bigger one. Why? The heights of all the nodes in the root subtree stay the same, but the height of the nodes merged into this tree all increase by one. Thus, merging in the smaller tree leaves the height unchanged on the larger set of vertices.
---
```cpp
void union_find_init(union_find *s, int n) {
	int i; /* counter */
	for (i = 1; i <= n; i++) {
		s->p[i] = i;
		s->size[i] = 1;
	}
	s->n = n;
}
```
```cpp
int find(union_find *s, int x) {
	if (s->p[x] == x) {
		return(x);
	}
	return(find(s, s->p[x]));
}
```
```cpp
void union_sets(union_find *s, int s1, int s2) {
	int r1, r2;   /* roots of sets */
	r1 = find(s, s1);
	r2 = find(s, s2);
	if (r1 == r2) {
		return;   /* already in same set */
	}
	if (s->size[r1] >= s->size[r2]) {
		s->size[r1] = s->size[r1] + s->size[r2];
		s->p[r2] = r1;
	} else {
		s->size[r2] = s->size[r1] + s->size[r2];
		s->p[r1] = r2;
	}
}
```
```cpp
bool same_component(union_find *s, int s1, int s2) {
	return (find(s, s1) == find(s, s2));
}
```
---
* On each union, the tree with fewer nodes becomes the child. But how tall can such a tree get as a function of the number of nodes in it? Consider the smallest possible tree of height $h$. Single-node trees have height $1$. The smallest tree of height $2$ has two nodes: it is made from the union of two single-node trees. Merging in more single-node trees won’t further increase the height, because they just become children of the rooted tree of height $2$. Only when we merge two height $2$ trees together can we get a tree of height $3$, now with at least four nodes.
* See the pattern? We must double the number of nodes in the tree to get an extra unit of height. How many doublings can we do before we use up all $n$ nodes? At most $lg\ n$ doublings can be performed. Thus, we can do both unions and finds in $O(\log n)$, fast enough to make Kruskal’s algorithm eficient on sparse graphs. In fact, union–find can be done even faster.

> [!subsubsection] 8.1.4 Variations on Minimum Spanning Trees

* The algorithms that construct minimum spanning trees can also be used to solve several closely related problems.
* $Maximum\ spanning\ trees$ – Suppose an evil telephone company is contracted to connect a bunch of houses together, such that they will be paid a price proportional to the amount of wire they install. Naturally, they will seek to build the most expensive possible spanning tree! The maximum spanning tree of any graph can be found by simply negating the weights of all edges and running Prim’s or Kruskal’s algorithm. The most negative spanning tree in the negated graph is the maximum spanning tree in the original.
* $Minimum\ product\ spanning\ trees$ – Suppose we seek the spanning tree that minimises the product of edge weights, assuming all edge weights are positive. Since $lg(a · b) = lg(a) + lg(b)$, the minimum spanning tree on a graph whose edge weights are replaced with their logarithms gives the minimum product spanning tree on the original graph.
* $Minimum\ bottleneck\ spanning\ tree$ – Sometimes we seek a spanning tree that minimises the maximum edge weight over all possible trees. In fact, every minimum spanning tree has this property. Such bottleneck spanning trees have interesting applications when the edge weights are interpreted as costs, capacities, or strengths. A less eficient but conceptually simpler way to solve such problems might be to delete all “heavy” edges from the graph and ask whether the result is still connected. These kinds of tests can be done with $BFS$ or $DFS$.
---
* The minimum spanning tree of a graph is unique if all m edge weights in the graph are distinct. Otherwise the order in which Prim’s/Kruskal’s algorithm breaks ties determines which minimum spanning tree is returned.
* There are two important variants of a minimum spanning tree that are not solvable with the techniques presented in this section.
* $Steiner\ tree$ – Suppose we want to wire a bunch of houses together, but have the freedom to add extra intermediate vertices to serve as a shared junction. This problem is known as a minimum Steiner tree.
* $Low\text{-}degree\ spanning\ tree$ – Alternatively, what if we want to find the minimum spanning tree where the highest degree of a node in the tree is small? The lowest max-degree tree possible would be a simple path, consisting of $n − 2$ nodes of degree $2$ and two endpoints of degree $1$. Such a path that visits each vertex once is called a $Hamiltonian\ path$.

> [!Error] 8.2 Shortest Paths

* A $path$ is a sequence of edges connecting two vertices. There are typically an enormous number of possible paths connecting two nodes in any given road or social network. The path that minimises the sum of edge weights, that is, the shortest path, is likely to be the most interesting, reﬂecting the fastest travel path or the closest kinship between the nodes.
* A shortest path from $s$ to $t$ in an unweighted graph can be identified using a breadth-first search from $s$. The minimum-link path is recorded in the breadth-first search tree, and hence provides the shortest path when all edges have equal weight.
* But $BFS$ does not sufice to find shortest paths in weighted graphs. The shortest weighted path might require a large number of edges, just as the fastest route from home to ofice may involve complicated backroad shortcuts.

> [!subsubsection] 8.2.1 Dijkstra's Algorithm

* Dijkstra’s algorithm is the method of choice for finding shortest paths in an edge-weighted and/or vertex-weighted graph. Starting from a particular vertex $s$, it finds the shortest path from $s$ to all other vertices in the graph, including your desired destination $t$.
* Suppose the shortest path from $s$ to $t$ in graph $G$ passes through a particular intermediate vertex $x$. Clearly, the best $s$-to-$t$ path must contain the shortest path from $s$ to $x$ as its prefix, because if it doesn’t we can improve the path by starting with the shorter $s$-to-$x$ prefix. Thus, we must compute the shortest path from $s$ to $x$ before we find the path from $s$ to $t$.
* Dijkstra’s algorithm proceeds in a series of rounds, where each round establishes the shortest path from $s$ to some new vertex. Specifically, $x$ is the vertex that minimises $dist(s, v_i) + w(v_i, x)$ over all unfinished vertices $v_i$. Here $w(a, b)$ denotes the weight of the edge from vertex $a$ to vertex $b$, and $dist(a, b)$ is the length of the shortest path between them.
* This suggests a dynamic programming-like strategy. The shortest path from $s$ to itself is trivial, so $dist(s, s) = 0$. If $(s, y)$ is the lightest edge incident to $s$, then $dist(s, y) = w(s, y)$. Once we determine the shortest path to a node $x$, we check all the outgoing edges of $x$ to see whether there is a shorter path from $s$ through $x$ to some unknown vertex.
	* $$
\begin{flalign}
&\quad \text{ShortestPath-Dijkstra(}G,\ s,\ t\text{):} \\
&\quad known = \{s\} \\
&\quad \text{for each vertex } v \text{in} G,\ dist[v] = ∞ \\
&\quad dist[s] = 0 \\
&\quad \text{for each edge }(s,\ v),\ dist[v] = w(s, v) \\
&\quad last = s \\
&\quad \text{while (} last \ne t\text{)} \\
&\quad \quad \text{select } v_{next} \text{, the unknown vertex minimizing } dist[v] \\
&\quad \quad \text{for each edge (} v_{next}, x\text{) } dist[x] = min[dist[x],\ dist[v_{next}] + w(v_{next},\ x)] \\
&\quad \quad last = v_{next} \\
&\quad \quad known = known ∪ \{v_{next}\}
&&\end{flalign}
$$
* The basic idea is very similar to Prim’s algorithm. In each iteration, we add exactly one vertex to the tree of vertices for which we know the shortest path from $s$. As in Prim’s, we keep track of the best path seen to date for all vertices outside the tree, and insert them in order of increasing cost.
* In fact, the only difference between Dijkstra’s and Prim’s algorithms is how they rate the desirability of each outside vertex. In the minimum spanning tree algorithm, we sought to minimise the weight of the next potential tree edge. In shortest path, we want to identify the closest outside vertex (in shortest-path distance) to $s$. This desirability is a function of both the new edge weight and the distance from $s$ to the tree vertex it is adjacent to.
---
```cpp
int dijkstra(graph *g, int start) {
	int i;                /* counter */
	edgenode *p;          /* temporary pointer */
	bool intree[MAXV+1];  /* is the vertex in the tree yet? */
	int distance[MAXV+1]; /* cost of adding to tree */
	int v;                /* current vertex to process */
	int w;                /* candidate next vertex */
	int dist;             /* cheapest cost to enlarge tree */
	int weight = 0;       /* tree weight */
	for (i = 1; i <= g->nvertices; i++) {
		intree[i] = false;
		distance[i] = MAXINT;
		parent[i] = -1;
	}
	distance[start] = 0;
	v = start;
	while (!intree[v]) {
		intree[v] = true;
		if (v != start) {
			printf("edge (%d,%d) in tree \n",parent[v],v);
			weight = weight + dist;
		}
		p = g->edges[v];
		while (p != NULL) {
			w = p->y;
			if (distance[w] > (distance[v]+p->weight)) {
				/* CHANGED FROM PRIM CODE */
				distance[w] = distance[v]+p->weight;
				/* CHANGED FROM PRIM CODE */
				parent[w] = v;
				/* CHANGED FROM PRIM CODE */
			}
			p = p->next;
		}
		dist = MAXINT;
		for (i = 1; i <= g->nvertices; i++) {
			if ((!intree[i]) && (dist > distance[i])) {
				dist = distance[i];
				v = i;
			}
		}
	}
	return(weight);
}
```
* This algorithm defines a shortest-path spanning tree rooted in $s$. For unweighted graphs, this would be the breadth-first search tree, but in general it provides the shortest path from s to all other vertices, not just t.
---
* **Analysis**
* What is the running time of Dijkstra’s algorithm? As implemented here, the complexity is $O(n^2)$, exactly the same running time as a proper version of Prim’s algorithm. This is because, except for the extension condition, it is exactly the same algorithm as Prim’s.
* The length of the shortest path from start to a given vertex $t$ is exactly the value of $distance[t]$. How do we use Dijkstra to find the actual path? We follow the backward $parent$ pointers from $t$ until we hit start (or $-1$ if no such path exists), exactly as was done in the $BFS$/$DFS$ $\text{find\_path()}$ routine.
* Dijkstra works correctly only on graphs without negative-cost edges. The reason is that during the execution we may encounter an edge with weight so negative that it changes the cheapest way to get from $s$ to some other vertex already in the tree. Indeed, the most cost-effective way to get from your house to your next-door neighbor would be to repeatedly cycle through the lobby of any bank offering you enough free money to make the detour worthwhile. Unless that bank limits its reward to one per customer, you might so benefit by making an unlimited number of trips through the lobby that you would never actually reach your destination!

> [!subsubsection] 8.3.2 All-Pairs Shortest Path

* Suppose you want to find the "center" vertex in a graph—the one that minimises the longest or average distance to all the other nodes. This might be the best place to start a new business. Or perhaps you need to know a graph’s diameter—the largest shortest-path distance over all pairs of vertices. This might correspond to the longest possible time it can take to deliver a letter or network packet. These and other applications require computing the shortest path between all pairs of vertices in a given graph.
* We could solve all-pairs shortest path by calling Dijkstra’s algorithm from each of the $n$ possible starting vertices. But Floyd’s all-pairs shortest-path algorithm is a slick way to construct this $n × n$ distance matrix from the original weight matrix of the graph.
* Floyd’s algorithm is best employed on an adjacency matrix data structure, which is no extravagance since we must store all $n^2$ pairwise distances anyway. Our adjacency matrix type allocates space for the largest possible matrix, and keeps track of how many vertices are in the graph:
```cpp
typedef struct {
	int weight[MAXV+1][MAXV+1];  /* adjacency/weight info */
	int nvertices;               /* number of vertices in graph */
} adjacency_matrix;
```
* The critical issue in an adjacency matrix implementation is how we denote the edges absent from the graph. A common convention for unweighted graphs denotes graph edges by $1$ and non-edges by $0$. This gives exactly the wrong interpretation if the numbers denote edge weights, because the non-edges get interpreted as a free ride between vertices. Instead, we should initialize each non-edge to `MAXINT`. This way we can both test whether it is present and automatically ignore it in shortest-path computations.
* There are several ways to characterize the shortest path between two nodes in a graph. The Floyd–Warshall algorithm starts by numbering the vertices of the graph from $1$ to $n$. We use these numbers not to label the vertices, but to order them. Define $W[i, j]^k$ to be the length of the shortest path from $i$ to $j$ using only vertices numbered from $1,\ 2,\ ...,\ k$ as possible intermediate vertices.
* What does this mean? When $k = 0$, we are allowed no intermediate vertices, so the only allowed paths are the original edges in the graph. The initial all-pairs shortest-path matrix thus consists of the initial adjacency matrix. We will perform $n$ iterations, where the $k$th iteration allows only the first $k$ vertices as possible intermediate steps on the path between each pair of vertices $x$ and $y$.
* With each iteration, we allow a richer set of possible shortest paths by adding a new vertex as a possible intermediary. The $k$th vertex helps only if there is a shortest path that goes through $k$, so
	* $$\begin{flalign}W[i, j]^k = min(W[i, j]^{k-1},\ W[i,k]^{k-1} + W[k,j]^{k-1})&&\end{flalign}$$
* The correctness of this is somewhat subtle, and I encourage you to convince yourself of it. Indeed, it is a great example of dynamic programming. But there is nothing subtle about how simple the implementation is.
```cpp
void floyd(adjacency_matrix *g) {
	int i, j;       /* dimension counters */
	int k;          /* intermediate vertex counter */
	int through_k;  /* distance through vertex k */
	for (k = 1; k <= g->nvertices; k++) {
		for (i = 1; i <= g->nvertices; i++) {
			for (j = 1; j <= g->nvertices; j++) {
				through_k = g->weight[i][k]+g->weight[k][j];
				if (through_k < g->weight[i][j]) {
					g->weight[i][j] = through_k;
				}
			}
		}
	}
}
```
* The Floyd–Warshall all-pairs shortest-path algorithm runs in $O(n^3)$ time, which is asymptotically no better than $n$ calls to Dijkstra’s algorithm. However, the loops are so tight and the program so short that it runs better in practice. It is notable as one of the rare graph algorithms that work better on adjacency matrices than adjacency lists.
* The output of Floyd’s algorithm, as it is written, does not enable one to reconstruct the actual shortest path between any given pair of vertices. These paths can be recovered if we retain a parent matrix $P$ containing our choice of the last intermediate vertex used for each vertex pair $(x, y)$. Say this value is $k$. The shortest path from $x$ to $y$ is the concatenation of the shortest path from $x$ to $k$ with the shortest path from $k$ to $y$, which can be reconstructed recursively given the matrix $P$ . Note, however, that most all-pairs applications only need the resulting distance matrix. These are the jobs that Floyd’s algorithm was designed for.

> [!subsubsection] 8.3.3 Transitive Closure

* Floyd’s algorithm has another important application, that of computing transitive closure. We are often interested in which vertices in a directed graph are reachable from a given node. As an example, consider the blackmail graph, where there is a directed edge $(i, j)$ if person $i$ has sensitive-enough private information on person $j$ so that $i$ can get $j$ to do whatever they want. You wish to hire one of these $n$ people to be your personal representative. Who has the most power in terms of blackmail potential?
* A simplistic answer would be the vertex of highest out-degree, but an even better representative would be the person who has blackmail chains leading to the most other parties. Steve might only be able to blackmail Miguel directly, but if Miguel can blackmail everyone else then Steve is the person you want to hire.
* The vertices reachable from any single node can be computed using breadth-first or depth-first search. But the complete set of relationships can be found using an all-pairs shortest path. If the shortest path from $i$ to $j$ remains `MAXINT` after running Floyd’s algorithm, you can be sure that no directed path exists from $i$ to $j$. Any vertex pair of weight less than `MAXINT` must be reachable, both in the graph-theoretic and blackmail senses of the word.

> [!Error] 8.5 Network Flows and Bipartite Matching

* An edge-weighted graph can be interpreted as a network of pipes, where the weight of an edge determines the capacity of the pipe. Capacities can be thought of as a function of the cross-sectional area of the pipe. A wide pipe might be able to carry $10$ units of ﬂow, that is, the amount of material in a given time, whereas a narrower pipe can only carry $5$ units. The $network\ flow\ problem$ asks for the maximum amount of ﬂow that can be sent from vertices $s$ to $t$ in a given weighted graph $G$ while respecting the maximum capacities of each pipe.

> [!subsubsection] 8.5.1 Bipartite Matching

* While the network ﬂow problem is of independent interest, its primary importance lies in solving other important graph problems. A classic example is $bipartite\ matching$. A matching in a graph $G = (V, E)$ is a subset of edges $E^{'} ⊂ E$ such that no two edges of $E^{'}$ share a vertex. A matching pairs off certain vertices such that every vertex is in at most one such pair.
* Graph $G$ is bipartite or two-colorable if the vertices can be divided into two sets, $L$ and $R$, such that all edges in $G$ have one vertex in $L$ and one vertex in $R$.
* The maximum cardinality bipartite matching can be readily found using network ﬂow. Create a source node $s$ that is connected to every vertex in $L$ by an edge of weight $1$. Create a sink node $t$ and connect it to every vertex in $R$ by an edge of weight $1$. finally, assign each edge in the central bipartite graph $G$ a weight of $1$. Now, the maximum possible ﬂow from $s$ to $t$ defines the largest matching in $G$. Certainly we can find a ﬂow as large as the matching, by using the matching edges and their source-to-sink connections. Further, there can be no other solution that achieves greater ﬂow, because we can’t possibly get more than one ﬂow unit through any given vertex.

> [!subsubsection] 8.5.2 Computing Network Flow

> [!Warning] Didn't understand a word!

> [!Error] 8.6 Randomized Min-Cut

> [!Warning] Didn't understand a word!

> [!Error] 8.7 Design Graphs, not Algorithms

* Proper modeling is the key to making effective use of graph algorithms. Several properties of graphs have been defined, and eficient algorithms for computing them developed.
* The secret is learning to design graphs, not algorithms. We have already seen a few instances of this idea:
	* The $maximum\ spanning\ tree$ can be found by negating the edge weights of the input graph $G$ and using a $minimum\ spanning\ tree$ algorithm on the result. The spanning tree of $−G$ that has the most negative weight will define the maximum-weight tree in $G$.
	* To solve bipartite matching, we constructed a special network ﬂow graph such that the maximum ﬂow corresponds to a matching having the largest number of edges.

> [!Tip] Take-Home Lesson
> Designing novel graph algorithms is very hard, so don’t do it. Instead, try to design graphs that enable you to use classical algorithms to model your problem.

### Chapter 9: Combinatorial Search
> `pg: 22`
> `time req: 2' 10"`
> `time done: 1' 25"`
> `performance: 152%`
>
> `practice time req: 3' 45"`

> [!Error] 9.1 Backtracking

* Backtracking is a systematic way to run through all the possible configurations of a search space.
* These configurations may represent all possible arrangements of objects (permutations) or all possible ways of building a collection of them (subsets).
* What these problems have in common is that we must generate each possible configuration exactly once. Avoiding repetitions and missed configurations means that we must define a systematic generation order.
* We will model our combinatorial search solution as a vector $a = (a_1, a_2, ..., a_n)$, where each element $a_i$ is selected from a finite ordered set $S_i$.
	* Such a vector might represent an arrangement where $a_i$ contains the $i\text{th}$ element of the permutation.
	* Or perhaps $a$ is a Boolean vector representing a given subset $S$, where $a_i$ is true if the $i\text{th}$ element of the universal set is in $S$.
	* The solution vector can even represent a sequence of moves in a game or a path in a graph, where $a_i$ contains the $i\text{th}$ game move or graph edge in the sequence.
* At each step in the backtracking algorithm, we try to extend a given partial solution $a = (a_1, a_2, ..., \bf{a_k})$ by adding another element at the end. After this extension, we must test whether what we now have is a complete solution: if so, we should print it or count it. If not, we must check whether the partial solution is still potentially extendable to some complete solution.
* Backtracking constructs a tree of partial solutions, where each node represents a partial solution. There is an edge from $x$ to $y$ if node $y$ was created by extending $x$. This tree of partial solutions provides an alternative way to think about backtracking, for the process of constructing the solutions corresponds exactly to doing a depth-first traversal of the backtrack tree. Viewing backtracking as a depth-first search on an implicit graph yields a natural recursive implementation of the basic algorithm.
* $$
\begin{flalign}
&\quad \text{Backtrack-DFS}(a, k) \\
&\quad \quad \text{if } a = (a_1, a_2, ..., a_k) \text{ is a solution, report it.} \\
&\quad \quad \text{else} \\
&\quad \quad \quad k = k + 1 \\
&\quad \quad \quad \text{construct } S_k \text{, the set of candidates for position } k \text{ of } a \\
&\quad \quad \quad \text{while } S_k \ne ∅ \text{ do} \\
&\quad \quad \quad \quad a_k = a_n \text{ element in } S_k \\
&\quad \quad \quad \quad S_k = S_k − \{a_k\} \\
&\quad \quad \quad \quad \text{Backtrack-DFS}(a, k)
&&\end{flalign}
$$
* Although a breadth-first search could also be used to enumerate solutions, a depth-first search is greatly preferred because it uses much less space.
	* The current state of a search is completely represented by the path from the root to the current depth-first search node. This requires space proportional to the height of the tree.
	* In breadth-first search, the queue stores all the nodes at the current level, which is proportional to the width of the search tree. For most interesting problems, the width of the tree grows exponentially with its height.
---
* **Implementation**
```cpp
void backtrack(int a[], int k, data input) {
	int c[MAXCANDIDATES]; /* candidates for next position */
	int nc;               /* next position candidate count */
	int i;                /* counter */
	if (is_a_solution(a, k, input)) {
		process_solution(a, k,input);
	} else {
		k = k + 1;
		construct_candidates(a, k, input, c, &nc);
		for (i = 0; i < nc; i++) {
			a[k] = c[i];
			make_move(a, k, input);
			backtrack(a, k, input);
			unmake_move(a, k, input);
			if (finished) {
				return; /* terminate early */
			} 
		}
	}
}
```
* Study how recursion yields an elegant and easy implementation of the backtracking algorithm. Because a new candidates array $c$ is allocated with each recursive procedure call, the subsets of not-yet-considered extension candidates at each position will not interfere with each other.
* The application-specific parts of this algorithm consist of five subroutines:
* $\text{is\_a\_solution}(a,\ k,\ input)$ – This Boolean function tests whether the first $k$ elements of vector $a$ form a complete solution for the given problem. The last argument, $input$, allows us to pass general information into the routine. We can use it to specify $n$—the size of a target solution. This makes sense when constructing permutations or subsets of $n$ elements, but other data may be relevant when constructing variable-sized objects such as sequences of moves in a game.
* $\text{construct\_candidates}(a,\ k,\ input,\ c,\ \&nc)$ – This routine fills an array $c$ with the complete set of possible candidates for the $k\text{th}$ position of $a$, given the contents of the first $k − 1$ positions. The number of candidates returned in this array is denoted by $nc$. Again, $input$ may be used to pass auxiliary information.
* $\text{process\_solution}(a,\ k,\ input)$ – This routine prints, counts, stores, or processes a complete solution once it is constructed.
* $\text{make\_move}(a,\ k,\ input)$ and $\text{unmake\_move}(a,\ k,\ input)$ – These routines enable us to modify a data structure in response to the latest move, as well as clean up this data structure if we decide to take back the move. Such a data structure can always be rebuilt from scratch using the solution vector $a$, but this can be ineficient when each move involves small incremental changes that can easily be undone.

> [!Error] 9.2 Examples of Backtracking

* To really understand how backtracking works, you must see how such objects as permutations and subsets can be constructed by defining the right state spaces.

> [!subsubsection] 9.2.1 Constructing all Subsets

* Designing an appropriate state space to represent combinatorial objects starts by counting how many objects need representing. How many subsets are there of an $n$-element set, say the integers $\{1, ..., n\}$? $2^n$.
* Each subset is described by the elements that are contained in it. To construct all $2^n$ subsets, we set up a Boolean array/vector of $n$ cells, where the value of $a_i$ (true or false) signifies whether the $i\text{th}$ item is in the given subset. In the scheme of our general backtrack algorithm, $S_k = (true,\ false)$ and $a$ is a solution whenever $k = n$. We can now construct all subsets with simple implementations of $\text{is\_a\_solution}()$, $\text{construct\_candidates}()$, and $\text{process\_solution}()$.
```cpp
int is_a_solution(int a[], int k, int n) {
	return (k == n);
}
```
```cpp
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
	c[0] = true;
	c[1] = false;
	*nc = 2;
}
```
```cpp
void process_solution(int a[], int k, int input) {
	int i; /* counter */
	printf("{");
	for (i = 1; i <= k; i++) {
		if (a[i] == true) {
			printf(" %d", i);
		}
	}
	printf(" }\n");
}
```
* finally, we must instantiate the call to backtrack with the right arguments. Specifically, this means giving a pointer to the empty solution vector, setting $k = 0$ to denote that it is in fact empty, and specifying the number of elements in the universal set:
```cpp
void generate_subsets(int n) {
	int a[NMAX]; /* solution vector */
	backtrack(a, 0, n);
}
```

> [!subsubsection] 9.2.2 Constructing all Permutations

* Counting permutations of $\{1,\ ...,\ n\}$ is a necessary prerequisite to generating them. There are $n$ distinct choices for the value of the first element of a permutation. Once we have fixed $a_1$, there are $n − 1$ candidates remaining for the second position, since we can have any value except $a_1$ in this slot (because repetitions are forbidden in permutations). Repeating this argument yields a total of $n! = \prod_{i=1}^n i$ distinct permutations.
* This counting argument suggests a suitable representation. Set up an array/vector $a$ of $n$ cells. The set of candidates for the $i\text{th}$ position will be all elements that have not appeared in the $(i − 1)$ elements of the partial solution, corresponding to the first $i − 1$ elements of the permutation.
* In the scheme of the general backtrack algorithm, $S_k = \{1,\ ...,\ n\} − \{a_1,\ ...,\ a_k\}$, and $a$ is a solution whenever $k = n$:
```cpp
void construct_candidates(int a[], int k, int n, int c[], int *nc) {
	int i;              /* counter */
	bool in_perm[NMAX]; /* what is now in the permutation? */
	for (i = 1; i < NMAX; i++) {
		in_perm[i] = false;
	}
	for (i = 1; i < k; i++) {
		in_perm[a[i]] = true;
	}
	*nc = 0;
	for (i = 1; i <= n; i++) {
		if (!in_perm[i]) {
			c[ *nc ] = i;
			*nc = *nc + 1;
		}
	}
}
```
* Testing whether $i$ is a candidate for the $k\text{th}$ slot in the permutation could be done by iterating through all $k − 1$ elements of $a$ and verifying that none of them matched. However, we prefer to set up a bit-vector data structure  to keep track of which elements are in the partial solution. This gives a constant-time legality check.
```cpp
void process_solution(int a[], int k, int input) {
	int i; /* counter */
	for (i = 1; i <= k; i++) {
		printf(" %d", a[i]);
	}
	printf("\n");
}
```
```cpp
int is_a_solution(int a[], int k, int n) {
	return (k == n);
}
```
```cpp
void generate_permutations(int n) {
	int a[NMAX]; /* solution vector */
	backtrack(a, 0, n);
}
```

> [!subsubsection] 9.2.3 Constructing all Paths in a Graph

* In a simple path no vertex appears more than once. Enumerating all the simple $s$ to $t$ paths in a given graph is a more complicated problem than just listing permutations or subsets. There is no explicit formula that counts solutions as a function of the number of edges or vertices, because the number of paths depends upon the structure of the graph.
* The input data we must pass to backtrack to construct the paths consists of the input graph $g$, the source vertex $s$, and target vertex $t$:
```cpp
typedef struct {
	int s;   /* source vertex */
	int t;   /* destination vertex */
	graph g; /* graph to find paths in */
} paths_data;
```
* The starting point of any path from $s$ to $t$ is always $s$. Thus, $s$ is the only candidate for the first position and $S_1 = \{s\}$. The possible candidates for the second position are the vertices $v$ such that $(s, v)$ is an edge of the graph, for the path wanders from vertex to vertex using edges to define the legal steps. In general, $S_{k+1}$ consists of the set of vertices adjacent to $a_k$ that have not been used elsewhere in the partial solution $a$.
```cpp
void construct_candidates(int a[], int k, paths_data *g, int c[],
int *nc) {
	int i;                /* counters */
	bool in_sol[NMAX+1];  /* what's already in the solution? */
	edgenode *p;          /* temporary pointer */
	int last;             /* last vertex on current path */
	for (i = 1; i <= g->g.nvertices; i++) {
		in_sol[i] = false;
	}
	for (i = 0; i < k; i++) {
		in_sol[a[i]] = true;
	}
	if (k == 1) {
		c[0] = g->s;      /* always start from vertex s */
		*nc = 1;
	} else {
		*nc = 0;
		last = a[k-1];
		p = g->g.edges[last];
		while (p != NULL) {
			if (!in_sol[ p->y ]) {
				c[*nc] = p->y;
				*nc= *nc + 1;
			}
			p = p->next;
		}
	}
}
```
```cpp
int is_a_solution(int a[], int k, paths_data *g) {
	return (a[k] == g->t);
}
```
```cpp
void process_solution(int a[], int k, paths_data *input) {
	int i;  /* counter */
	solution_count ++;
	printf("{");
	for (i = 1; i <= k; i++) {
		printf(" %d",a[i]);
	}
	printf(" }\n");
}
```

> [!Error] 9.3 Search Pruning

* Backtracking ensures correctness by enumerating all possibilities. A correct algorithm to find the optimal travelling salesman tour constructs all $n!$ permutations of the $n$ vertices of graph $G$. For each permutation, we check whether all edges implied by the tour really exist in $G$ and if so add the weights of these edges together. The tour with minimum weight is the solution.
* However, it is wasteful to construct all the permutations first and then analyze them later. Suppose our search started from vertex $v_1$, and it happened that vertex-pair $(v_1,\ v_2)$ was not an edge in $G$. The $(n − 2)!$ permutations enumerated starting with $(v_1,\ v_2)$ as its prefix would be a complete waste of effort. Much better would be to stop the search after $[v_1,\ v_2]$ and then continue from $[v_1,\ v_3]$. By restricting the set of next elements to reﬂect only legal moves with respect to the current partial configuration, we significantly reduce the total search complexity.
* $Pruning$ is the technique of abandoning a search direction the instant we can establish that a given partial solution cannot be extended into a full solution. For travelling salesman, we seek the cheapest tour that visits all vertices. Suppose that in the course of our search we find a tour $t$ whose cost is $C_t$. Later, we may have a partial solution $a$ whose edge sum $C_a ≥ C_t$ . Is there any reason to continue exploring this node? No, because any tour with $a$ as its prefix will have cost greater than tour $t$, and hence is doomed to be non-optimal. Cutting away such failed partial tours from the search tree as soon as possible can have an enormous impact on running time.
* Exploiting symmetry is another avenue for reducing combinatorial search. Pruning away partial solutions equivalent to those previously considered requires recognizing underlying symmetries in the search space. For example, consider the state of our $TSP$ search after we have tried all partial positions beginning with $v_1$. Does it pay to continue the search with partial solutions beginning with $v_2$? No. Any tour starting and ending at $v_2$ can be viewed as a rotation of one starting and ending at $v_1$, for $TSP$ tours are closed cycles. There are thus only $(n − 1)!$ distinct tours on $n$ vertices, not $n!$. By restricting the first element of the tour to $v_1$, we save a factor of $n$ in time without missing any interesting solutions. Detecting such symmetries can be subtle, but once identified they can usually be easily exploited.

> [!Tip] Take-Home Lesson
> Combinatorial search, when augmented with tree-pruning techniques, can be used to find the optimal solution for small optimisation problems. How small depends upon the specific problem, but typical size limits are somewhere between **twenty** and **a hundred** items.

> [!Error] 9.5 War Story: Covering Chessboards

> [!Tip] Take-Home Lesson
> Clever pruning can make short work of surprisingly hard combinatorial search problems. Proper pruning will have a greater impact on search time than other factors like data structures or programming language.

> [!Error] 9.6 Best-first Search

* An important idea to speed up search is to explore your best options before the less promising choices. In the backtrack implementation presented above, the search order was determined by the sequence of elements generated by the construct candidates routine. Items near the front of the candidates array were tried before those further back. A good candidate ordering can have a very powerful effect on the time to solve the problem.
* The examples so far in this chapter have focused on existential search problems, where we look for a single solution (or all solutions) satisfying a given set of constraints. Optimisation problems seek the solution with the lowest or highest value of some objective function. A simple strategy to deal with optimisation problems is to construct all possible solutions, and then report the one that scores best by the optimisation criterion. But this can be expensive. Much better would be to generate solutions in order from best to worst, and report the best as soon as we can prove it is the best.
* $\text{Best-first search}$, also called branch and bound, assigns a cost to every partial solution we have generated. We use a priority queue (named $q$ below) to keep track of these partial solutions by cost, so the most promising partial solution can be easily identified and expanded. As in backtracking, we explore the next partial solution by testing if it is a solution and calling process solution if it is. We identify all ways to expand this partial solution by calling construct candidates, each of which gets inserted into the priority queue with its associated cost. A generic best-first search, which we apply to the travelling salesman problem ($TSP$), is implemented as follows:
```cpp
void branch_and_bound (tsp_solution *s, tsp_instance *t) {
	int c[MAXCANDIDATES]; /* candidates for next position */
	int nc;               /* next position candidate count */
	int i;                /* counter */
	first_solution(&best_solution,t);
	best_cost = solution_cost(&best_solution, t);
	initialize_solution(s,t);
	extend_solution(s,t,1);
	pq_init(&q);
	pq_insert(&q,s);
	while (top_pq(&q).cost < best_cost) {
		*s = extract_min(&q);
		if (is_a_solution(s, s->n, t)) {
			process_solution(s, s->n, t);
		}
		else {
			construct_candidates(s, (s->n)+1, t, c, &nc);
			for (i=0; i<nc; i++) {
				extend_solution(s,t,c[i]);
				pq_insert(&q,s);
				contract_solution(s,t);
			}
		}
	}
}
```
* The extend solution and contract solution routines handle the book-keeping of creating and pricing the partial solutions associated with each new candidate:
```cpp
void extend_solution(tsp_solution *s, tsp_instance *t, int v) {
	s->n++;
	s->p[s->n] = v;
	s->cost = partial_solution_lb(s,t);
}
```
```cpp
void contract_solution(tsp_solution *s, tsp_instance *t) {
	s->n--;
	s->cost = partial_solution_lb(s,t);
}
```
* What should be the cost of a partial solution? There are $(n − 1)!$ circular permutations on $n$ points, so we can represent each tour as an $n$-element permutation starting with $1$ so there are no repetitions. Partial solutions construct a prefix of the tour starting with vertex $v1$, so a natural cost function might be the sum of the edge weights on this prefix source. An interesting property of such a cost function is that it serves as a lower bound on the cost of any expanded tour, assuming that all edge weights are positive.
* But does the first full solution from a best-first search have to be an optimal solution? No, not necessarily. There was certainly no cheaper partial solution available when we pulled it off the priority queue. But extending this partial solution came with a cost, that of the next edge we added to this tour. It is certainly possible that a slightly more costly partial tour might be finishable using a less-expensive next edge, thus producing a better solution.
* Thus, to get the global optimal, we must continue to explore the partial solutions coming off the priority queue until they are more expensive than the best solution we already know about. Note that this requires that the cost function for partial solutions be a lower bound on the cost of an optimal solution. Otherwise, there might be something deeper in the queue that would expand to a better solution. That would leave us with no choice but to expand everything on the priority queue completely to be sure we found the right solution.

> [!Error] 9.7 The A* Heuristic

* Best-first search can take a while, even if our partial cost function is a lower bound on the optimal tour, so we can stop as soon as we have a solution cheaper than the best unexplored partial solution. Consider the partial solutions we will encounter on a search for the optimal travelling salesman tour. Costs increase with the number of edges in the partial solution, so partial solutions with few nodes will always look more promising than longer ones nearer to completion. Even the most awful prefix path on $n/2$ nodes will likely be cheaper than the optimal solution on all $n$ nodes, meaning that we must expand all partial solutions until their prefix cost is greater than the cost of the best full tour. This will be horribly expensive to work through.
* The A* heuristic (pronounced “A-star”) is an elaboration on the branch-and-bound search presented above, where at each iteration we expanded the best (cheapest) partial solution that we have found so far. The idea is to use a lower bound on the cost of all possible partial solution extensions that is stronger than just the cost of the current partial tour. This will make promising partial solutions look more interesting than those that have the fewest vertices.
* How can we lower bound the cost of the full tour, which contains $n$ edges, from a partial solution with $k$ vertices (and thus $k − 1$ edges)? We know it will eventually get $n − k + 1$ additional edges. If $\text{minlb}$ is a lower bound on the cost of any edge, specifically the distance between the two closest points, adding $(n − k + 1) × \text{minlb}$ gives a cost lower bound that is much more realistic for the partial solution:
```cpp
double partial_solution_cost(tsp_solution *s, tsp_instance *t) {
	int i;              /* counter */
	double cost = 0.0;  /* cost of solution */
	for (i = 1; i < (s->n); i++) {
		cost = cost + distance(s, i, i + 1, t);
	}
	return(cost);
}
```
```cpp
double partial_solution_lb(tsp_solution *s, tsp_instance *t) {
	return(partial_solution_cost(s,t) + (t->n - s->n + 1) * minlb);
}
```
* Best-first search is sort of like breadth-first search. A disadvantage of $BFS$ over $DFS$ is the space required. A backtracking/$DFS$ tree uses memory proportional to the height of the tree, but a best-first/$BFS$ tree requires maintaining all partial solutions, more akin to the width of the tree.
* Space will kill you quicker than time. To get an answer from a slow program you just have to be patient enough, but a program that crashes because of lack of memory will not give an answer no matter how long you wait.

> [!Tip] Take-Home Lesson
> The promise of a given partial solution is not just its cost, but also includes the potential cost of the remainder of the solution. A tight solution cost estimate which is still a lower bound makes best-first search much more eficient.

### Chapter 10: Dynamic Programming
> `pg: 39`
> `time req: 3' 50"`
> `time done: 2' 11"`
> `performance: 175%`
>
> `practice time req: 6' 38"`

* The most challenging algorithmic problems involve optimisation, where we seek to find a solution that maximises or minimises an objective function. Travelling salesman is a classic optimisation problem, where we seek the tour visiting all vertices of a graph at minimum total cost. But it is easy to propose $TSP$ “algorithms” that generate reasonable-looking solutions but do not always produce the minimum cost tour.
* Algorithms for optimisation problems require proof that they always return the best possible solution. Greedy algorithms that make the best local decision at each step are typically eficient, but usually do not guarantee global optimality. Exhaustive search algorithms that try all possibilities and select the best always produce the optimum result, but usually at a prohibitive cost in terms of time complexity.
* Dynamic programming combines the best of both worlds. It gives us a way to design custom algorithms that systematically search all possibilities (thus guaranteeing correctness) while storing intermediate results to avoid recomputing (thus providing eficiency). By storing the consequences of all possible decisions and using this information in a systematic way, the total amount of work is minimised.
* After you understand it, dynamic programming is probably the easiest algorithm design technique to apply in practice. In fact, I find that dynamic programming algorithms are often easier to reinvent than to try to look up. That said, until you understand dynamic programming, it seems like magic. You have to figure out the trick before you can use it.
* Dynamic programming is a technique for eficiently implementing a recursive algorithm by storing partial results. It requires seeing that a naive recursive algorithm computes the same subproblems over and over and over again. In such a situation, storing the answer for each subproblem in a table to look up instead of recompute can lead to an eficient algorithm. Dynamic programming starts with a recursive algorithm or definition. Only after we have a correct recursive algorithm can we worry about speeding it up by using a results matrix.
* Dynamic programming is generally the right method for optimisation problems on combinatorial objects that have an inherent left-to-right order among components. Left-to-right objects include character strings, rooted trees, polygons, and integer sequences. Dynamic programming is best learned by carefully studying examples until things start to click. I present several war stories where dynamic programming played the decisive role to demonstrate its utility in practice.

> [!Error] 10.1 Caching vs Computation

* Dynamic programming is essentially a tradeoff of space for time.

> [!Error] 10.3 Longest Increasing Subsequence

* There are three steps involved in solving a problem by dynamic programming:
	1. Formulate the answer you want as a recurrence relation or recursive algorithm.
	2. Show that the number of different parameter values taken on by your recurrence is bounded by a (hopefully small) polynomial.
	3. Specify an evaluation order for the recurrence so the partial results you need are always available when you need them.

> [!Tip] Take-Home Lesson
> Once you understand dynamic programming, it can be easier to work out such algorithms from scratch than to try to look them up.

> [!Error] 10.8 Parsing Context-Free Grammers

> [!Tip] Take-Home Lesson
> For optimisation problems on left-to-right objects, such as characters in a string, elements of a permutation, points around a polygon, or leaves in a search tree, dynamic programming likely leads to an eficient algorithm to find the optimal solution.

> [!Error] 10.9 Limitations of Dynamic Programming: TSP

* Dynamic programming doesn’t always work. It is important to see why it can fail, to help avoid traps leading to incorrect or ineficient algorithms.

> [!subsubsection] 10.9.1 When is Dynamic Programming Correct?

* Dynamic programming algorithms are only as correct as the recurrence relations they are based on.
* Dynamic programming can be applied to any problem that obeys the $principle\ of\ optimality$.
	* Roughly stated, this means that partial solutions can be optimally extended given the $state$ after the partial solution, instead of the specifics of the partial solution itself.
	* For example, in deciding whether to extend an approximate string matching by a substitution, insertion, or deletion, we did not need to know the sequence of operations that had been performed to date. In fact, there may be several different edit sequences that achieve a cost of $C$ on the first $p$ characters of pattern $P$ and $t$ characters of string $T$.
	* Future decisions are made based on the consequences of previous decisions, not the actual decisions themselves.
* Problems do not satisfy the principle of optimality when the specifics of the operations matter, as opposed to just their cost.
* Properly formulated, however, many combinatorial problems respect the principle of optimality.

> [!Error] 10.9.2 When is Dynamic Programming Efficient?

* The running time of any dynamic programming algorithm is a function of two things:
	1. the number of partial solutions we must keep track of, and
	2. how long it takes to evaluate each partial solution.
	* The first issue—namely the size of the state space—is usually the more pressing concern.
* In all of the examples we have seen, the partial solutions are completely described by specifying the possible stopping places in the input. This is because the combinatorial objects being worked on (typically strings and numerical sequences) have an implicit order defined upon their elements. This order cannot be scrambled without completely changing the problem. Once the order is fixed, there are relatively few possible stopping places or states, so we get eficient algorithms.
* When the objects are not firmly ordered, however, we likely have an exponential number of possible partial solutions.

> [!Tip] Take-Home Lesson
> Without an inherent left-to-right ordering on the objects, dynamic programming is usually doomed to require exponential space and time.

> [!Error] 10.10 War Story: What's Past is Prolog

> [!Tip] Take-Home Lesson
> The global optimum (found perhaps using dynamic programming) is often noticeably better than the solution found by typical heuristics. How important this improvement is depends on your application, but it can never hurt.

### Chapter 11: NP-Completeness
> `pg: 29`
> `time req: 2' 51"`
> `time done: 1' 33"`
> `performance: 183%`
>
> `practice time req: 4' 56"`

* The truth is that the theory of NP-completeness is an immensely useful tool for the algorithm designer, even though all it provides are negative results. The theory of NP-completeness enables us to focus our efforts more productively, by revealing when the search for an eficient algorithm is doomed to failure. Whenever one tries and fails to show a problem is hard, that suggests there may well be an eficient algorithm to solve it.
* The theory of NP-completeness also enables us to identify which properties make a particular problem hard. This can provide direction to model it in different ways, or exploit more benevolent characteristics of the problem. Developing a sense for which problems are hard is an important skill for algorithm designers, and only comes from hands-on experience with proving hardness.

> [!Error] 11.1 Problems and Reductions

> [!subsubsection] 11.1.1 the Key Idea

* A translation of instances from one type of problem to instances of another such that the answers are preserved is what we mean by a $reduction$.

> [!Tip] Take-Home Lesson
> Reductions are a way to show that two problems are essentially identical. A fast algorithm (or the lack of one) for one of the problems implies a fast algorithm (or the lack of one) for the other.

> [!subsubsection] 11.1.2 Decision Problems

* Reductions translate between problems so that their answers are identical in every problem instance. Problems differ in the range or type of possible answers. The travelling salesman problem returns a permutation of vertices as the answer, while other types of problems may return strings or numbers as answers, perhaps restricted to positive numbers or integers.
* The simplest interesting class of problems have answers restricted to true and false. These are called $decision$ problems. It proves convenient to reduce/translate answers between decision problems because both only allow true and false as possible answers.

> [!Error] 11.2 Reductions for Algorithms

* Reductions are an honourable way to generate new algorithms from old ones. Whenever we can translate the input for a problem $\text{we want to solve}$ into input for a problem $\text{we know how to solve}$, we can compose the translation and the solution into an algorithm to deal with our problem.

> [!Error] 11.3 Elementary Hardness Reductions

![[Computer Science/algo-manual-images/NP-problemset.png]]

> [!Error] 11.4 Satisfiability
> 

* To demonstrate the hardness of problems by using reductions, we must start from a single problem that is absolutely, certifiably, undeniably hard to compute. The mother of all NP-complete problems is a logic problem named $satisfiability$:
* $\color{yellow}Problem$: $\color{cyan}Satisfiability\ (SAT)$
* $\color{yellow}Input$: A set of Boolean variables $V$ and a set of logic clauses $C$ over $V$.
* $\color{yellow}Output$: Does there exist a satisfying truth assignment for $C$—in other words, a way to set each of the variables $\{v_1, ..., v_n\}$ either true or false so that every clause contains at least one true literal?
* For a combination of social and technical reasons, it is well accepted that satisﬁability is a hard problem; one for which no worst-case polynomial-time algorithm exists. Literally every top-notch algorithm expert in the world (and countless lesser lights) has directly or indirectly tried to come up with a fast algorithm to test whether any given set of clauses is satisﬁable. All have failed. Furthermore, many strange and impossible-to-believe things in the ﬁeld of computational complexity have been shown to be true if there exists a fast satisﬁability algorithm. Proving something is as hard as satisﬁability means that it is hard.

> [!subsubsection] 11.4.1 3-Satisfiability

* Satisﬁability’s role as the ﬁrst NP-complete problem implies that the problem is hard to solve in the worst case. But certain special-case instances of the problem are not necessarily so tough.
* Since it is so easy to determine whether clause sets with exactly one literal per clause are satisﬁable, we are interested in slightly larger classes. How many literals per clause do you need to turn the problem from polynomial to hard? This transition occurs when each clause contains three literals, that is,
* $\color{yellow}Problem$: $\color{cyan}3\text{-}Satisfiability\ (3\text{-}SAT)$
* $\color{yellow}Input$: A collection of clauses $C$ where each clause contains exactly $3$ literals, over a set of Boolean variables $V$.
* $\color{yellow}Output$: Is there a truth assignment to $V$ such that each clause is satisﬁed?

> [!Error] 11.5 Creative Reductions from SAT

> [!Tip] Take-Home Lesson
> A small set of NP-complete problems (3-SAT, vertex cover, integer partition, and Hamiltonian cycle) suﬃce to prove the hardness of most other hard problems.

> [!Error] 11.6 The Art of Proving Hardness

* Proving that problems are hard is a skill. But once you get the hang of it, reductions can be surprisingly straightforward and pleasurable to do. Indeed, the dirty little secret of NP-completeness proofs is that they are usually easier to create than explain, in much the same way that it can be easier to rewrite old code than to understand and modify it.
* It takes experience to judge which problems are likely to be hard. The quickest way to gain this experience is through careful study of the catalogue. Slightly changing the wording of a problem can make the difference between it being polynomial or NP-complete.
---
$\text{I offer the following advice to those seeking to prove the hardness of a given problem:}$
* Make your source problem as simple (meaning restricted) as possible.
* Make your target problem as hard as possible.
* Select the right source problem for the right reason.
* Amplify the penalties for making the undesired selection.
* Think strategically at a high level, then build gadgets to enforce tactics.
* When you get stuck, switch between looking for an algorithm and a reduction.

### Chapter 12: Dealing with Hard Problems
> `pg: 38`
> `time req: 3' 44"`
> `time done: 1' 52"`
> `performance: 200%`
>
> `practice time req: 6' 28"`

* For the practical person, demonstrating that a problem is NP-complete is never the end of the line. Presumably, there was a reason why you wanted to solve it in the ﬁrst place. That application won’t go away after you learn there is no polynomial-time algorithm. You still seek a program that solves the problem of interest. All you know is that you won’t ﬁnd one that quickly solves the problem to optimality in the worst case.
* There are still three possibilities:
	* $Algorithms\ fast\ in\ the\ average\ case$ – Examples of such algorithms include backtracking algorithms with substantial pruning.
	* $Heuristics$ – Heuristic methods like simulated annealing or greedy approaches can be used to quickly ﬁnd a solution, albeit with no guarantee that it will be the best one.
	* $Approximation\ algorithms$ – The theory of NP-completeness stipulates that it is hard to get the exact answer. With clever, problem-speciﬁc heuristics, we can get provably close to the optimal answer on all possible instances.

> [!Error] 12.1 Approximation Algorithms

* Approximation algorithms produce solutions with a guarantee attached, namely that the quality of the optimal solution is provably bounded by the quality of your heuristic solution. Thus, no matter what your input instance is and how lucky you are, such an approximation algorithm is destined to produce a correct answer. Furthermore, provably good approximation algorithms are often conceptually simple, fast, and easy to program.
* One thing that is usually not clear, however, is how well the solution from an approximation algorithm compares to what you might get from a heuristic that gives you no guarantees. The answer may be worse, or it could be better. Leaving your money in a bank savings account may guarantee you 3% interest without risk. Still, you likely will do much better investing your money in stocks than leaving it in the bank, even though performance is not guaranteed.
* One way to get the best of approximation algorithms and unwashed heuristics is to run both of them on the given problem instance, and pick the solution giving the better result. This way, you will get a solution that comes with a guarantee and a second chance to do even better. When it comes to heuristics for hard problems, sometimes you can have it both ways.
---
* Randomization is a very powerful tool for developing approximation algorithms. Its role is to make bad special cases go away by making it very unlikely that they will occur. The careful analysis of such probabilities often requires sophisticated eﬀorts, but the heuristics themselves are generally very simple and easy to implement.

> [!Error] 12.4 When Average is Good Enough

* For certain optimisation problems, all (or most) of the solutions are seemingly close to the best possible. Recognising this yields very simple approximation algorithms with provable guarantees, that can often be reﬁned by the heuristic search strategies into something even better.

> [!Error] 12.5 Set Cover

> [!Tip] Take-Home Lesson
> Approximation algorithms guarantee answers that are always close to the optimal solution. They can provide a practical approach to dealing with NP-complete problems.

> [!Error] 12.6 Heuristic Search Methods

* Backtracking gave us a method to ﬁnd the best of all possible solutions, as scored by a given objective function. However, any algorithm searching all conﬁgurations is doomed to be impossibly expensive on large instances. Heuristic search methods provide an alternate approach to diﬃcult combinatorial optimisation problems.
* Heuristic search algorithms have an air of voodoo about them, but how they work and why one method can work better than another follows logically enough if you think them through.
* In particular, we will look at three diﬀerent heuristic search methods: random sampling, gradient descent search, and simulated annealing.
* All three heuristics share two common components:
	* $Solution\ candidate\ representation$ – This is a complete yet concise description of possible solutions for the problem, just like we used for backtracking. For travelling salesman, the solution space consists of $(n − 1)!$ elements—namely all possible circular permutations of the vertices. We need a data structure that can represent each element of the solution space. For TSP, the candidate solutions can naturally be represented using an array $S$ of $n − 1$ vertices, where $S_i$ deﬁnes the $(i + 1)$st vertex on the tour starting from $v_1$.
	* $Cost\ function$ – Search methods need a cost or evaluation function to assess the quality of each possible solution. Our search heuristic identiﬁes the element with the best score—either the highest or lowest depending upon the nature of the problem. For $TSP$, the cost function for evaluating candidate solutions $S$ just sums up the weights of all edges $(S_i, S_{i+1})$, where $S_0$ and $S_n$ both denote $v_1$.

> [!subsubsection] 12.6.1 Random Sampling

* The simplest approach to search in a solution space uses random sampling, also known as the Monte Carlo method. We repeatedly construct random solutions and evaluate them, stopping as soon as we get a good enough solution, or (more likely) when we get tired of waiting. We report the best solution found over the course of our sampling.
* True random sampling requires that we select elements from the solution space $uniformly\ at\ random$. This means that each of the elements of the solution space must have an equal probability of being the next candidate selected. Such sampling can be a subtle problem.
* When might random sampling do well?
* $When\ there\ is\ a\ large\ proportion\ of\ acceptable\ solutions$ – Finding a piece of hay in a haystack is easy, since almost anything you grab is a straw. When good solutions are plentiful, a random search should ﬁnd one quickly. Finding prime numbers is a domain where a random search proves successful. Generating large random prime numbers for keys is an important aspect of cryptographic systems such as $RSA$. Roughly one out of every $ln\ n$ integers is prime, so only a modest number of random samples need to be taken to discover primes that are several hundred digits long.
* $When\ there\ is\ no\ coherence\ in\ the\ solution\ space$ – Random sampling is the right thing to do when there is no sense of when we are getting closer to a solution. Suppose you wanted to ﬁnd one of your friends who has a social security number that ends in $00$. There is not much else you can do but tap an arbitrary fellow on the shoulder and ask. No cleverer method will be better than random sampling. Consider again the problem of hunting for a large prime number. Primes are scattered quite arbitrarily among the integers. Random sampling is as systematic as anything else would be.

> [!subsubsection] 12.6.2 Local Search

* Now suppose you want to hire an algorithms expert as a consultant to solve your problem. You could dial a phone number at random, ask if they are an algorithms expert, and hang up if they say no. After many repetitions you will eventually ﬁnd one, but it would probably be more eﬃcient to ask the person on the phone for someone more likely to be an algorithms expert, and call them up instead.
* A local search scans the neighbourhood around elements in the solution space. Think of each such candidate solution $x$ as a vertex, with a directed edge $(x, y)$ to every other candidate solution $y$ that is a neighbor of $x$. Our search proceeds from $x$ to the most promising candidate in $x$’s neighbourhood.
* We certainly do not want to explicitly construct this neighbourhood graph for any sizeable solution space. Think about $TSP$, which will have $(n − 1)!$ vertices in this graph. We are conducting a heuristic search precisely because we cannot hope to do this many operations in a reasonable amount of time.
* Instead, we want a general transition mechanism that takes us to a nearby solution by slightly modifying the current one. Typical transition mechanisms include swapping a random pair of items or changing (inserting or deleting) a single item in the solution.
* Local search heuristics start from an arbitrary element of the solution space, and then scan the neighbourhood looking for a favourable transition to take. In a favourable vertex swap, the four edges we insert are cheaper than the four edges we delete, a computation performed by the $\text{transition}$ function. In a greedy hill-climbing procedure, we try to ﬁnd the top of a mountain (or alternately, the lowest point in a ditch) by starting at some arbitrary point and taking any step that leads in the direction we want to travel. We repeat until we have reached a point where all our neighbors lead us in the wrong direction. We are now King of the Hill, or for a minimisation problem Dean of the Ditch.
* Hill climbing and closely related heuristics such as greedy search or local search are great at ﬁnding local optima quickly, but often fail to ﬁnd the globally best solution.
* When does local search do well?
	* $When\ there\ is\ great\ coherence\ in\ the\ solution\ space$ – Hill climbing is at its best when the solution space consists of exactly one hill. No matter where you start on the hill, there is always a direction to walk up until you are at the absolute global maximum.
		* Many natural problems have this property. We can think of a binary search as starting in the middle of a search space, where exactly one of the two possible directions we can walk will get us closer to the target key. The simplex algorithm for linear programming is nothing more than hill climbing over the right solution space, yet it guarantees us the optimal solution to any linear programming problem.
	* $Whenever\ the\ cost\ of\ incremental\ evaluation\ is\ much\ cheaper\ than\ global\ evaluation$ – It costs $Θ(n)$ to evaluate the cost of an arbitrary $n$-vertex candidate $TSP$ solution, because we must sum up the cost of each edge in the circular permutation describing the tour. Once that is found, however, the cost of the tour after swapping a given pair of vertices can be determined in constant time.
		* If we are given a very large value of $n$ and a very small budget of how much time we can spend searching, we are better oﬀ using it to do a bunch of incremental evaluations than a few random samples, even if we are looking for a needle in a haystack.
* The primary drawback of a local search is that there isn’t anything more for us to do after we ﬁnd the local optimum. Sure, if we have more time we could restart from diﬀerent random points, but in landscapes of many low hills we are unlikely to stumble on the optimum.

> [!subsubsection] 12.6.3 Simulated Annealing

* Simulated annealing is a heuristic search procedure that allows occasional transitions leading to more expensive (and hence inferior) solutions. This may not sound like progress, but it helps keep our search from getting stuck in local optima. That poor fellow trapped on the second ﬂoor of the ski lodge would do better to break the glass and jump out the window if they really want to reach the top of the mountain.
* The inspiration for simulated annealing comes from the physical process of cooling molten materials down to the solid state. $\text{I ignored the details...}$
* What relevance does this have for combinatorial optimisation? A physical system, as it cools, seeks to reach a minimum-energy state. Minimising the total energy is a combinatorial optimisation problem for any set of discrete particles.
* Through random transitions generated according to the given probability distribution, we can mimic the physics to solve arbitrary combinatorial optimisation problems.

> [!Tip] Take-Home Lesson
> Don’t worry about this molten metal business. Simulated annealing is eﬀective because it spends much more of its time working on good elements of the solution space than on bad ones, and because it avoids getting trapped in local optimum.

* As with a local search, the problem representation includes both a representation of the solution space and an easily computable cost function $C(s)$ measuring the quality of a given solution. The new component is the cooling schedule, whose parameters govern how likely we are to accept a bad transition as a function of time.
* At the beginning of the search, we are eager to use randomness to explore the search space widely, so the probability of accepting a bad transition should be high. As the search progresses, we seek to limit transitions to local improvements and optimisations. This cooling schedule can be regulated by the following parameters:
	* $Initial\ system\ temperature$ – Typically $T_1 = 1$.
	* $Temperature\ decrement\ function$ – Typically $T_i = α·T_{i−1}$, where $0.8 ≤ α ≤ 0.99$. This implies an exponential decay in the temperature, as opposed to a linear decay.
	* $Number\ of\ iterations\ between\ temperature\ change$ – Typically, $1,000$ iterations or so might be permitted before lowering the temperature. Also, it generally pays to stay at a given temperature for multiple rounds so long as we are making progress there.
	* $Acceptance\ criteria$ – A typical criterion is to accept any good transition, and also accept a bad transition whenever $e^{\frac{C(s_{i-1})-C(s_i)}{k_B T}} > r$ where $r$ is a random number $0 ≤ r < 1$. The “Boltzmann” constant $k_B$ scales this cost function so that almost all transitions are accepted at the starting temperature.
	* $Stop\ criteria$ – Typically, when the value of the current solution has not changed or improved within the last iteration or so, the search is terminated and the current solution reported.

> [!Info] Implementation
> - [annealing.h](https://www3.cs.stonybrook.edu/~skiena/algorist/book/programs/annealing.h)
> - [annealing.c](https://www3.cs.stonybrook.edu/~skiena/algorist/book/programs/annealing.c)

> [!Tip] Take-Home Lessson
> Simulated annealing is a simple but eﬀective technique for eﬃciently obtaining good but not optimal solutions to combinatorial search problems.

### Chapter 13: How to Design Algorithms
> `pg: 7`
> `time req: 42"`
> `time done: 32"`
> `performance: 131%`
>
> `practice time req: 1' 12"`

* Designing the right algorithm for a given application is a major creative act—that of taking a problem and pulling a solution out of the air. The space of choices you can make in algorithm design is enormous, leaving you plenty of freedom to hang yourself.
* This book has been designed to make you a better algorithm designer. The techniques presented in Part I provide the basic ideas underlying all combinatorial algorithms. The problem catalogue of Part II will help you with modeling your application, and inform you what is known about the relevant problems. However, being a successful algorithm designer requires more than book knowledge. It requires a certain attitude—the right problem-solving approach. It is diﬃcult to teach this mindset in a book, yet getting it is essential to becoming a successful algorithm designer.
* The key to algorithm design (or any other problem-solving task) is to proceed by asking yourself questions to guide your thought process. “What if we do this? What if we do that?” Should you get stuck on the problem, the best thing to do is move onto the next question. In any group brainstorming session, the most useful person in the room is the one who keeps asking “Why can’t we do it this way?”; not the nitpicker who keeps telling them why. Because he or she will eventually stumble on an approach that can’t be shot down.
* By clearly articulating your reasoning as to why something doesn’t work, you can check whether you have glossed over a possibility that you didn’t think hard enough about. It is amazing how often the reason you can’t ﬁnd a convincing explanation for something is because your conclusion is wrong.
* The distinction between strategy and tactics is important to keep aware of during any design process. Strategy represents the quest for the big picture—the framework around which we construct our path to the goal. Tactics are used to win the minor battles we must ﬁght along the way. In problem-solving, it is important to repeatedly check whether you are thinking on the right level. If you do not have a global strategy of how to attack your problem, it is pointless to worry about the tactics. An example of a strategic question is “Can I model my application as a graph algorithm problem?” A tactical question might be “Should I use an adjacency list or adjacency matrix data structure to represent my graph?” Of course, such tactical decisions are critical to the ultimate quality of the solution, but they can be properly evaluated only in light of a successful strategy.
* Too many people freeze up in their thinking when faced with a design problem. After reading or hearing the problem, they sit down and realise that they $don’t\ know\ what\ to\ do\ next$. Avoid this fate. Follow the sequence of questions I provide below and in most of the catalogue problem sections. I will try to tell you what to do next.
---
1. Do I really understand the problem?
	1. What exactly does the input consist of?
	2. What exactly are the desired results or output?
	3. Can I construct an input example small enough to solve by hand? What happens when I try to solve it?
	4. How important is it to my application that I always ﬁnd the optimal answer? Might I settle for something close to the best answer?
	5. How large is a typical instance of my problem? Will I be working on $10$ items? $1,000$ items? $1,000,000$ items? More?
	6. How important is speed in my application? Must the problem be solved within one second? One minute? One hour? One day?
	7. How much time and eﬀort can I invest in implementation? Will I be limited to simple algorithms that can be coded up in a day, or do I have the freedom to experiment with several approaches and see which one is best?
	8. Am I trying to solve a numerical problem? A graph problem? A geometric problem? A string problem? A set problem? Which formulation seems easiest?
2. Can I ﬁnd a simple algorithm or heuristic for my problem?
	1. Will brute force solve my problem correctly by searching through all subsets or arrangements and picking the best one?
		1. If so, why am I sure that this algorithm always gives the correct answer?
		2. How do I measure the quality of a solution once I construct it?
		3. Does this simple, slow solution run in polynomial or exponential time? Is my problem small enough that a brute-force solution will suﬃce?
		4. Am I certain that my problem is suﬃciently well deﬁned to actually have a correct solution?
	2. Can I solve my problem by repeatedly trying some simple rule, like picking the biggest item ﬁrst? The smallest item ﬁrst? A random item ﬁrst?
		1. If so, on what types of inputs does this heuristic work well? Do these correspond to the data that might arise in my application?
		2. On what inputs does this heuristic work badly? If no such examples can be found, can I show that it always works well?
		3. How fast does my heuristic come up with an answer? Does it have a simple implementation?
3. Is my problem in the catalogue of algorithmic problems in the back of this book?
	1. What is known about the problem? Is there an available implementation that I can use?
	2. Did I look in the right place for my problem? Did I browse through all the pictures? Did I look in the index under all possible keywords?
4. Are there special cases of the problem that I know how to solve?
	1. Can I solve the problem eﬃciently when I ignore some of the input parameters?
	2. Does the problem become easier to solve when some of the input parameters are set to trivial values, such as 0 or 1?
	3. How can I simplify the problem to the point where I can solve it eﬃciently? Why can’t this special-case algorithm be generalized to a wider class of inputs?
	4. Is my problem a special case of a more general problem in the catalog?
5. Which of the standard algorithm design paradigms are most relevant to my problem?
	1. Is there a set of items that can be sorted by size or some key? Does this sorted order make it easier to ﬁnd the answer?
	2. Is there a way to split the problem into two smaller problems, perhaps by doing a binary search? How about partitioning the elements into big and small, or left and right? Does this suggest a divide-and-conquer algorithm?
	3. Does the set of input objects have a natural left-to-right order among its components, like the characters in a string, elements of a permutation, or the leaves of a rooted tree? Could I use dynamic programming to exploit this order?
	4. Are there certain operations being done repeatedly, such as searching, or ﬁnding the largest/smallest element? Can I use a data structure to speed up these queries? Perhaps a dictionary/hash table or a heap/priority queue?
	5. Can I use random sampling to select which object to pick next? What about constructing many random conﬁgurations and picking the best one? Can I use a heuristic search technique like simulated annealing to zoom in on a good solution?
	6. Can I formulate my problem as a linear program? How about an integer program?
	7. Does my problem resemble satisﬁability, the travelling salesman problem, or some other NP-complete problem? Might it be NP-complete and thus not have an eﬃcient algorithm? Is it in the problem list in the back of Garey and Johnson?
6. Am I still stumped? Go back to the beginning and work through these questions again. Did any of my answers change during my latest trip through the list?

## Part II: The Hitchhiker's Guide to Algorithms
### Chapter 14: A Catalog of Algorithmic Problems
> `pg: 3`
> `time req: 18"`
> `practice time req: 31"`

### Chapter 15: Data Structures
> `pg: 27`
> `time req: 2' 39"`
> `practice time req: 4' 36"`

### Chapter 16: Numerical Problems
> `pg: 41`
> `time req: 4' 2"`
> `practice time req: 6' 59"`

### Chapter 17: Combinatorial Problems
> `pg: 37`
> `time req: 3' 38"`
> `practice time req: 6' 18"`

### Chapter 18: Graph Problems: Polynomial Time
> `pg: 45`
> `time req: 4' 25"`
> `practice time req: 7' 39"`

### Chapter 19: Graph Problems: NP-Hard
> `pg: 37`
> `time req: 3' 38"`
> `practice time req: 6' 18"`

### Chapter 20: Computational Geometry
> `pg: 57`
> `time req: 5' 36"`
> `practice time req: 9' 42"`

### Chapter 21: Set and String Problems
> `pg: 37`
> `time req: 3' 38"`
> `practice time req: 6' 18"`

### Chapter 22: Algorithmic Resources
> `pg: 7`
> `time req: 42"`
> `practice time req: 1' 12"`
