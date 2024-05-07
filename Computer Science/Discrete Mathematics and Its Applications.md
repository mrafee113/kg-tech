> [Discrete Mathematics and Its Applications - Kenneth H. Rosen](https://www.mheducation.com/highered/product/discrete-mathematics-applications-rosen/M9781259676512.html)
> [Companion Website](https://highered.mheducation.com/sites/125967651x/student_view0/index.html)
> 	- [Interactive Demonstrations](https://highered.mheducation.com/sites/125967651x/student_view0/interactive_demonstrations.html)
> 	- [Self Assessments](https://highered.mheducation.com/sites/125967651x/student_view0/self_assessments.html)
> 	- [Exploring Discrete Mathematics using Maple](https://highered.mheducation.com/sites/125967651x/student_view0/exploring_discrete_mathematics_using_maple.html)
> 	- [Exploring Discrete Mathematics using Mathematica](https://highered.mheducation.com/sites/125967651x/student_view0/exploring_discrete_mathematics_using_mathematica.html)
> 	- [Extra Examples](https://highered.mheducation.com/sites/125967651x/student_view0/extra_examples.html)
> 	- [A Guide to Writing Proofs](https://highered.mheducation.com/sites/125967651x/student_view0/a_guide_to_writing_proofs.html)
> 	- [Common Mistakes in Discrete Mathematics](https://highered.mheducation.com/sites/125967651x/student_view0/common_mistakes_in_discrete_mathematics.html)
> 	- [Advice on Writing Projects](https://highered.mheducation.com/sites/125967651x/student_view0/advice_on_writing_projects.html)
> 	- [Answers to Odd Numbered Exercises](https://highered.mheducation.com/sites/125967651x/student_view0/answers_to_odd-numbered_exercises.html)
> 	- [Web Resources Guide](https://highered.mheducation.com/sites/125967651x/student_view0/web_resources_guide.html)

> [!Example] Planning
> `total-pages` $= 738$
> `words-per-page` $= 500$
> `words-per-min` $= 75$
> `min-per-page` $=$ `words-per-page` $/$ `words-per-min` $= 500 / 75$ $= 6.66666$
> `total-hours` $=$ `total-pages` $*$ `min-per-page` $/ 60$ $= 738 * 6.66666 / 60$ $= 81.999991$
>
> `avg-performance` $= 95\%$
> `hour-per-day` $= 3$
> `reading-day-duration` $=$ `total-hours` $/$ `hour-per-day` $*$ `avg-performance` $= 81.999991 / 3 * (1 / 0.95) -> 29\ days$
> 
> `start-date`: $22\ mehr$
> `day-duration`: $45$
> `deadline-date`: $7\ Azar$
> `practice-day-duration`: `day-duration` $-$ `reading-day-duration` $= 45 - 29$ $= 16$
> `practice-time-duration`: `practice-day-duration` $*$ `hour-per-day` $= 16 * 3$ $= 48$
> 
> > [!Info] Section Formula
> > `hour-per-page` $= 0.11111$
> > `min-per-page` $= 6.66666$
> > `practice-time-duration` $= 48$
> > > [!Exmaple] Example
> > > `Chapter 1: The Foundations: Logic and Proofs`
> > > 	`section-pages` $= 84$
> > > 	`section-reading-time-duration` = `section-pages` $*$ `hour-per-page` $= 4^{'} 40^"$
> > > 	`section-practice-time-duration` = `section-pages` $/$ `total-pages` $*$ `practice-time-duration` $= 84 / 738 * 48$ $= 5.46$

> [!Example] Summary
> Left out chapters: `Chapter 12`, `Chapter 13`
> Left out practices: `2.4`, `2.5`, `3.2`, `3.3`, `4.1`, `4.3`, `4.5`, `4.6`, `5.2`, `5.3`, `5.4`, `5.5`, `Chapter 6`, `Chapter 7`, `Chapter 8`, `Chapter 9`, `Chapter 10`, `Chapter 11`, `Chapter 12`, `Chapter 13`
>
> `total-time-req` $= 80^{'} 36^"$
> `total-time-done` $= 59^{'} 24^"$
> `total-performance` $= 135\%$
> `date-done` $= 8\ Azar$
> ---
> `studied-pages` $= 738 - 73$ $= 665$
> `words-per-page` $= 500$
> `words-per-minute` $=$ `total-pages` $*$ `words-per-page` $/$ `total-time-done` $= 665 * 500 / (59.4 * 60) = 93\ \text{words-per-minute}$

![[Computer Science/discrete-math-images/discrete-math-and-apps-chapter-hierarchy.png]]
#### Chapter 1: The Foundations: Logic and Proofs
> [!Summary]
> `sum page: 97`
> `sum time req: 10' 40"`

* The rules of logic specify the meaning of mathematical statements.
	* For instance, these rules help us understand and reason with statements such as “There exists an integer that is not the sum of two squares”
* Logic is the basis of all mathematical reasoning, and of all automated reasoning.
* To understand mathematics, we must understand what makes up a correct mathematical argument, that is, a proof. Once we prove a mathematical statement is true, we call it a theorem.
* A collection of theorems on a topic organize what we know about this topic.
	* To learn a mathematical topic, a person needs to actively construct mathematical arguments on this topic, and not just read exposition.
	* Moreover, knowing the proof of a theorem often makes it possible to modify the result to ﬁt new situations.
* Everyone knows that proofs are important throughout mathematics, but many people ﬁnd it surprising how important proofs are in computer science.

##### 1.1 Propositional Logic
> `pg: 13`
> `time req: 1' 26"`
> `time done: 1' 57"`
> `performance: 74%`
> 
> `questions: 54`
> `questions done: 26`
> `practice time req: 50"`
> `practice time done: 1' 50"`
> `p-performance: 45%`

> [!Error] 1.1.1 Introduction

* The rules of logic give precise meaning to mathematical statements. These rules are used to distinguish between valid and invalid mathematical arguments.

> [!Error] 1.1.2 Propositions

* The basic building blocks of logic, are propositions. A proposition is a declarative sentence (that is, a sentence that declares a fact) that is either true or false, but not both.
	* `x + 1 = 2` is not a propositions because it is neither true or false. But it can be turned into one if the variables are provided with values.
* We use letters to denote **propositional variables** (or **sentential variables**), that is, variables that represent propositions, just as letters are used to denote numerical variables.
	* The conventional letters used for propositional variables are `p`, `q`, `r`, `s`, … .
* The **truth value** of a proposition is true, denoted by T, if it is a true proposition, and the truth value of a proposition is false, denoted by F, if it is a false proposition.
* Propositions that cannot be expressed in terms of simpler propositions are called **atomic propositions**.
* The area of logic that deals with propositions is called the **propositional calculus** or **propositional logic**. It was ﬁrst developed systematically by the Greek philosopher Aristotle more than 2300 years ago.
* Many mathematical statements are constructed by combining one or more propositions. New propositions, called **compound propositions**, are formed from existing propositions using **logical operators**.

> [!Info] Definition: `NOT`
> Let p be a proposition. The negation of p, denoted by ¬p, is the statement “It is not the case that p.”
> The proposition ¬p is read “not p.” The truth value of the negation of p, ¬p, is the opposite of the truth value of p.

| p | ¬p | The truth value table for `NOT` |
| :-: | :-: | :- |
| T | F |
| F | T |

* **Remark**: The notation for the negation operator is not standardized. Although ¬p and p are the most common notations used in mathematics to express the negation of p, other notations you might see are ∼p, −p, p′ , Np, and !p.
* The logical operators used to form new propositions are also called **connectives**.

> [!Info] Definition: `AND`
> a.k.a. conjunction. Let *p* and *q* be propositions. The conjunction of *p* and *q*, denoted by *p ∧ q*, is the proposition “*p* and *q*.” The conjunction *p ∧ q* is true when both *p* and *q* are true and is false otherwise.

| p | q | p ∧ q | The truth value table for `AND` |
| :-: | :-: | :-: | :- | 
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

> [!Info] Definition: `OR`
> a.k.a disjunction. Let *p* and *q* be propositions. The disjunction of *p* and *q*, denoted by *p ∨ q*, is the proposition “*p* or *q*.” The disjunction *p* ∨ *q* is false when both *p* and *q* are false and is true otherwise.

| p | q | p ∨ q | The truth value table for `OR` |
| :-: | :-: | :-: | :- | 
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

> [!Info] Definition: `XOR`
> Let *p* and *q* be propositions. The exclusive or of *p* and *q*, denoted by *p ⊕ q* (or *p* XOR *q*), is the proposition that is true when exactly one of *p* and *q* is true and is false otherwise.

| p | q | p ⊕ q | The truth value table for `XOR` |
| :-: | :-: | :-: | :- | 
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

> [!Error] 1.1.3 Conditional Statements

> [!Info] Definition: `p → q`
> Let *p* and *q* be propositions. The conditional statement *p* → *q* is the proposition “if *p*, then *q*.” The conditional statement *p* → *q* is false when *p* is true and *q* is false, and true otherwise. In the conditional statement *p* → *q*, *p* is called the hypothesis (or antecedent or premise) and *q* is called the conclusion (or consequence).

| p | q | p → q | The truth value table for `p → q` |
| :-: | :-: | :-: | :- | 
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

* The statement p → q is called a conditional statement because p → q asserts that q is true on the condition that p holds. A conditional statement is also called an **implication**.
* Because conditional statements play such an essential role in mathematical reasoning, a variety of terminology is used to express p → q. Common examples:
	* "if p, then q"
	* “if p, q”
	* “p is suﬃcient for q”
	* “q if p”
	* “q when p”
	* “a necessary condition for p is q”
	* “q unless ¬p”
	* “p implies q”
	* “p only if q”
	* “a suﬃcient condition for q is p”
	* “q whenever p”
	* “q is necessary for p”
	* “q follows from p”
	* “q provided that p”
* A useful way to understand the truth value of a conditional statement is to think of an obligation or a contract.
	* For example, the pledge many politicians make when running for oﬃce is “If I am elected, then I will lower taxes.” If the politician is elected, voters would expect this politician to lower taxes. Furthermore, if the politician is not elected, then voters will not have any expectation that this person will lower taxes, although the person may have suﬃcient inﬂuence to cause those in power to lower taxes. It is only when the politician is elected but does not lower taxes that voters can say that the politician has broken the campaign pledge. This last scenario corresponds to the case when p is true but q is false in p → q.
* **Remark**: Because some of the diﬀerent ways to express the implication p implies q can be confusing, we will provide some extra guidance.
	* To remember that “p only if q” expresses the same thing as “if p, then q,” note that “p only if q” says that p cannot be true when q is not true. That is, the statement is false if p is true, but q is false.
	* When p is false, q may be either true or false, because the statement says nothing about the truth value of q.
	* Be careful not to use “q only if p” to express p → q because this is incorrect. The word “only” plays an essential role here.
	* To see this, note that the truth values of “q only if p” and p → q are diﬀerent when p and q have diﬀerent truth values. To see why “q is necessary for p” is equivalent to “if p, then q,” observe that “q is necessary for p” means that p cannot be true unless q is true, or that if q is false, then p is false. This is the same as saying that if p is true, then q is true.
	* To see why “p is suﬃcient for q” is equivalent to “if p, then q,” note that “p is suﬃcient for q” means if p is true, it must be the case that q is also true. This is the same as saying that if p is true, then q is also true.
* To remember that “q unless ¬p” expresses the same conditional statement as “if p, then q,” note that “q unless ¬p” means that if ¬p is false, then q must be true. That is, the statement “q unless ¬p” is false when p is true but q is false, but it is true otherwise. Consequently, “q unless ¬p” and p → q always have the same truth value.
* When two compound propositions always have the same truth values, regardless of the truth values of its propositional variables, we call them **equivalent**.
* We can form some new conditional statements starting with a conditional statement p → q.
	* The proposition q → p is called the **converse** of p → q.
	* The **contrapositive** of p → q is the proposition ¬q → ¬p. This proposition is equivalent to p -> q.
	* The proposition ¬p → ¬q is called the **inverse** of p → q.
	* The converse and inverse of a conditional statement are equivalent.

> [!Info] Definition: `p ↔ q`
> Let *p* and *q* be propositions. The biconditional statement *p* ↔ *q* is the proposition “*p* if and only if *q*.” The biconditional statement *p* ↔ *q* is true when *p* and *q* have the same truth values, and is false otherwise. Biconditional statements are also called bi-implications.

| p | q | p ↔ q | The truth value table for `p ↔ q` |
| :-: | :-: | :-: | :- | 
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

* Note that the statement p ↔ q is true when both the conditional statements p → q and q → p are true and is false otherwise
	* That is why we use the words “if and only if” to express this logical connective and why it is symbolically written by combining the symbols → and ←.
* There are some other common ways to express p ↔ q:
	* “p is necessary and suﬃcient for q”
	* “if p then q, and conversely”
	* “p iﬀ q.”
		* "iff" is an abbreviated form of “if and only if.”
	* “p exactly when q.”
* Note that p ↔ q has exactly the same truth value as (p → q) ∧ (q → p).

> [!Error] 1.1.5 Precedence of Logical Operators

| Op |  Precedence | Precedence of Logical Operators |
| :-: | :-: | :- |
| ¬ | 1 |
| ∧ | 2 |
| ∨ | 3 |
| → | 4 |
| ↔ | 5 |

##### 1.2 Applications of Propositional Logic
> `pg: 7`
> `time req: 46"`
> `time done: 44"`
> `performance: 104%`
> 
> `questions: 47`
> `questions done: 23`
> `practice time req: 27"`
> `practice time done: 2' 23"`
> `p-performance: 18%`

> [!Error] 1.2.1 Introduction

* Statements in mathematics and the sciences and in natural language often are imprecise or ambiguous. To make such statements precise, they can be translated into the language of logic.
	* For example, logic is used in the speciﬁcation of software and hardware, because these speciﬁcations need to be precise before development begins.

> [!Error] 1.2.2 Translating English Sentences

* In particular, English (and every other human language) is often ambiguous. Translating sentences into compound statements removes the ambiguity.
* Note that this may involve making a set of reasonable assumptions based on the intended meaning of the sentence.

> [!Error] 1.2.4 Boolean Searches

* Logical connectives are used extensively in searches of large collections of information, such as indexes of Web pages. Because these searches employ techniques from propositional logic, they are called **Boolean searches**.

> [!Error] 1.2.5 Logic Puzzles

* Puzzles that can be solved using logical reasoning are known as **logic puzzles**.

##### 1.3 Propositional Equivalences
> `pg: 12`
> `time req: 1' 19"`
> `time done: 1' 30"`
> `performance: 88%`
> 
> `questions: 72`
> `questions done: 21`
> `practice time req: 46"`
> `practice time done: 2'`
> `p-performance: 38%`

> [!Error] 1.3.1 Introduction

> [!Info] Definition: `tautology`, `contradiction` and `contingency`
> A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it, is called a ***tautology*** (`p ∨ ¬p`). A compound proposition that is always false is called a ***contradiction*** (`p ∧ ¬p`). A compound proposition that is neither a tautology nor a contradiction is called a ***contingency***.

> [!Error] Logical Equivalences

* Compound propositions that have the same truth values in all possible cases are called **logically equivalent**. We can also deﬁne this notion as follows.

> [!Info] Definition: `logical equivalence`
> The compound propositions *p* and *q* are called logically equivalent if *p* ↔ *q* is a tautology. The notation *p* ≡ *q* denotes that *p* and *q* are logically equivalent.
>> [!Error] Attention
>> The proposition p ↔ q is a tautology **only when** *p* and *q* have the same truth values.

* **Remark**: The symbol ≡ is not a logical connective, and p ≡ q is not a compound proposition but rather is the statement that p ↔ q is a tautology. The symbol ⇔ is sometimes used instead of ≡ to denote logical equivalence.

| p | q | p -> q | q -> p | p ↔ q = (p -> q) ∧ (q -> p) |
| :-: | :-: | :-: | :-: | :-: |
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | T | F | F |
| F | F | T | T | T |

* In general, `2**n` rows are required if a compound proposition involves n propositional variables. Because of the rapid growth of `2**n` , more eﬃcient ways are needed to establish logical equivalences.
* Some common logical equivalences
	* Identity Laws
		* p∧T≡p
		* p∨F≡p
	* Domination Laws
		* p∨T≡T
		* p∧F≡F
	* Idempotent Laws
		* p∨p≡p
		* p∧p≡p
	* Double negation Law: ¬(¬p) ≡ p
	* Commutative Laws
		* p∨q≡q∨p
		* p∧q≡q∧p
	* Associative Laws
		* (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
		* (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
	* Distributive Laws
		* p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
		* p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
	* De Morgan's Laws
		* ¬(p ∧ q) ≡ ¬p ∨ ¬q
		* ¬(p ∨ q) ≡ ¬p ∧ ¬q
	* Absorption Laws
		* p ∨ (p ∧ q) ≡ p
		* p ∧ (p ∨ q) ≡ p
	* Negation Laws
		* p ∨ ¬p ≡ T
		* p ∧ ¬p ≡ F
* Logical Equivalences of Conditional Statements
	* p → q ≡ ¬p ∨ q
	* p → q ≡ ¬q → ¬p
	* p ∨ q ≡ ¬p → q
	* p ∧ q ≡ ¬(p → ¬q)
	* ¬(p → q) ≡ p ∧ ¬q
	* (p → q) ∧ (p → r) ≡ p → (q ∧ r)
	* (p → r) ∧ (q → r) ≡ (p ∨ q) → r
	* (p → q) ∨ (p → r) ≡ p → (q ∨ r)
	* (p → r) ∨ (q → r) ≡ (p ∧ q) → r
* Logical Equivalences of Biconditional Statements
	* p ↔ q ≡ (p → q) ∧ (q → p)
	* p ↔ q ≡ ¬p ↔ ¬q
	* p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)
	* ¬(p ↔ q) ≡ p ↔ ¬q

> [!Error] 1.3.5 Satisfiability

* A compound proposition is **satisﬁable** if there is an assignment of truth values to its variables that makes it true (that is, when it is a tautology or a contingency) (that is, when it *cannot* be False). 
	* When no such assignments exists, that is, when the compound proposition is false for all assignments of truth values to its variables, the compound proposition is unsatisﬁable.
	* Note that a compound proposition is unsatisﬁable if and only if its negation is true for all assignments of truth values to the variables, that is, if and only if its negation is a tautology.
* When we ﬁnd a particular assignment of truth values that makes a compound proposition true, we have shown that it is satisﬁable; such an assignment is called a **solution** of this particular satisﬁability problem.

> [!Question] ChatGPT
> > [!Info] Definition: `Logically Complete set of ops`
> > A collection of logical operators is called functionally complete if every compound proposition is logically equivalent to a compound proposition involving only these logical operators.
> 
> In propositional logic, statements are formed using logical operators such as AND (∧), OR (∨), NOT (¬), XOR (exclusive or), etc. A collection of logical operators is considered "functionally complete" if, using only these operators, you can express any possible compound proposition. In other words, you can build up any logical statement or formula using just the operators from this set.
>
> The key idea is that you should be able to represent the logical operations of conjunction, disjunction, and negation (or any other basic operations you choose) in terms of the operators in your functionally complete set.
>
> For example, if you have the set {AND, NOT} (conjunction and negation), it is functionally complete because you can express OR in terms of AND and NOT using De Morgan's Laws. Similarly, if you have the set {NAND} (which stands for NOT AND), it is functionally complete because you can express all other logical operations using just NAND.
>
> The paragraph is stating that if a set of logical operators is functionally complete, then any compound proposition (a combination of statements using these operators) can be expressed using only these operators. It emphasizes the idea of sufficiency in terms of the chosen set of logical operators to represent any logical relationship or operation.

##### 1.4 Predicates and Quantifiers
> `pg: 17`
> `time req: 1' 53"`
> `time done: 2' 6"`
> `performance: 90%`
> 
> `questions: 64`
> `questions done: 32`
> `practice time req: 1' 6"`
> `practice time done: 2' 34"`
> `p-performance: 42%`

> [!Error] 1.4.1 Introduction

* Propositional logic cannot adequately express the meaning of all statements in mathematics and in natural language. (examples in page 40)

> [!Error] 1.4.2 Predicates

* Statements involving variables, such as "x > 3", "x = y + 3", "x + y = z", "Computer x is under attack by and intruder", and "Computer x is functioning properly", are often found in mathematical assertions, in computer programs, and in system speciﬁcations. These statements are neither true nor false when the values of the variables are not speciﬁed.
* The statement “x is greater than 3” has two parts.
	* The ﬁrst part, the variable x, is the **subject** of the statement.
	* The second part—the **predicate**, “is greater than 3”—refers to a property that the subject of the statement can have.
* We can denote the statement “x is greater than 3” by P(x), where P denotes the predicate “is greater than 3” and x is the variable.
	* The statement P(x) is also said to be the value of the **propositional function** P at x.
	* Once a value has been assigned to the variable x, the statement P(x) becomes a proposition and has a truth value.
* In general, a statement involving the n variables `x1, x2, …, xn` can be denoted by `P(x1, x2, …, xn)`.
	* A statement of the form `P(x1, x2, …, xn)` is the value of the propositional function P at the n-tuple `(x1, x2, …, xn)`, and P is also called an n-place predicate or an n-ary predicate.
* **Preconditions** and **Postconditions**: Predicates are also used to establish the correctness of computer programs, that is, to show that computer programs always produce the desired output when given valid input. (Note that unless the correctness of a computer program is established, no amount of testing can show that it produces the desired output for all input values, unless every input value is tested.) The statements that describe valid input are known as **preconditions** and the conditions that the output should satisfy when the program has run are known as **postconditions**.

> [!Error] 1.4.3 Quantifiers

* When the variables in a propositional function are assigned values, the resulting statement becomes a proposition with a certain truth value. However, there is another important way, called **quantiﬁcation**, to create a proposition from a propositional function.
	* Quantiﬁcation expresses the extent to which a predicate is true over a range of elements. In English, the words all, some, many, none, and few are used in quantiﬁcations.
	* We will focus on two types of quantiﬁcation here:
		* universal quantiﬁcation, which tells us that a predicate is true for every element under consideration,
		* and existential quantiﬁcation, which tells us that there is one or more element under consideration for which the predicate is true.
	* The area of logic that deals with predicates and quantiﬁers is called the **predicate calculus**.
* **The Universal Quantifier**: Many mathematical statements assert that a property is true for all values of a variable in a particular domain, called the **domain of discourse** (or the **universe of discourse**), often just referred to as the **domain**. Such a statement is expressed using universal quantiﬁcation. The universal quantiﬁcation of P(x) for a particular domain is the proposition that asserts that P(x) is true for all values of x in this domain. Note that the domain speciﬁes the possible values of the variable x. The meaning of the universal quantiﬁcation of P(x) changes when we change the domain. The domain must always be speciﬁed when a universal quantiﬁer is used; without it, the universal quantiﬁcation of a statement is not deﬁned.

> [!Info] Definition: `universal quantifier`
> The universal quantiﬁcation of P(x) is the statement: “*P(x)* for all values of *x* in the domain.”
> 	
> The notation ∀xP(x) denotes the universal quantiﬁcation of P(x). Here ∀ is called the **universal quantiﬁer**. We read ∀xP(x) as “for all xP(x)” or “for every xP(x).” An element for which P(x) is false is called a **counterexample** to ∀xP(x).

* Besides “for all” and “for every,” universal quantiﬁcation can be expressed in many other ways, including “all of,” “for each,” “given any,” “for arbitrary,” “for each,” and “for any.”
* **Remark**: It is best to avoid using “for any x” because it is often ambiguous as to whether “any” means “every” or “some.” In some cases, “any” is unambiguous, such as when it is used in negatives: “There is not any reason to avoid studying.”

* A statement ∀xP(x) is false, where P(x) is a propositional function, if and only if P(x) is not always true when x is in the domain. One way to show that P(x) is not always true when x is in the domain is to ﬁnd a counterexample to the statement ∀xP(x). Note that a single counterexample is all we need to establish that ∀xP(x) is false. Example 9 illustrates how counterexamples are used.

* **The Existential Quantifier**: Many mathematical statements assert that there is an element with a certain property. Such statements are expressed using existential quantiﬁcation. With existential quantiﬁcation, we form a proposition that is true if and only if P(x) is true for at least one value of x in the domain.

> [!Info] Definition: `existential quantifier`
> The *existential quantiﬁcation* of *P(x)* is the proposition: “There exists an element *x* in the domain such that *P(x)*.”
> 
> We use the notation ∃*xP(x)* for the existential quantiﬁcation of *P(x)*. Here ∃ is called the existential quantiﬁer.
> 

* Besides the phrase “there exists,” we can also express existential quantiﬁcation in many other ways, such as by using the words “for some,” “for at least one,” or “there is.” The existential quantiﬁcation ∃xP(x) is read as
	* “There is an x such that P(x),”
	* “There is at least one x such that P(x),”
	* “For some xP(x).”

| Statement | When True? | When False? | Quantifiers |
| :-: | :-: | :-: |
| ∀*xP(x)* | *P(x)* is true for every *x*. | There is an *x* for which *P(x)* is false. |
| ∃*xP(x)* | There is an *x* for which *P(x)* is true. | *P(x)* is false for every *x*. |

* **The Uniqueness Quantifier**: We have now introduced universal and existential quantiﬁers. These are the most important quantiﬁers in mathematics and computer science. However, there is no limitation on the number of diﬀerent quantiﬁers we can deﬁne, such as “there are exactly two,” “there are no more than three,” “there are at least 100,” and so on. Of these other quantiﬁers, the one that is most often seen is the **uniqueness quantiﬁer**, denoted by ∃!. The notation ∃!*xP(x)* states “There exists a unique x such that P(x) is true.” (Other phrases for uniqueness quantiﬁcation include “there is exactly one” and “there is one and only one.”) For instance, `∃!x(x − 1 = 0)`, where the domain is the set of real numbers, states that there is a unique real number x such that `x − 1 = 0`. This is a true statement, as `x = 1` is the unique real number such that `x − 1 = 0`. Observe that we can use quantiﬁers and propositional logic to express uniqueness, so the uniqueness quantiﬁer can be avoided. Generally, it is best to stick with existential and universal quantiﬁers so that rules of inference for these quantiﬁers can be used.

> [!Error] 1.4.4 Quantifiers over Finite Domains

* When the domain of a quantiﬁer is ﬁnite, that is, when all its elements can be listed, quantiﬁed statements can be expressed using propositional logic. In particular, when the elements of the domain are `x1, x2, …, xn` , where n is a positive integer, the universal quantiﬁcation ∀xP(x) is the same as the conjunction `P(x1) ∧ P(x2) ∧ ⋯ ∧ P(xn)`, because this conjunction is true if and only if `P(x1), P(x2), …, P(xn)` are all true.
* Similarly, when the elements of the domain are `x1, x2, …, xn`, where n is a positive integer, the existential quantiﬁcation ∃xP(x) is the same as the disjunction `P(x1) ∨ P(x2) ∨ ⋯ ∨ P(xn)`, because this disjunction is true if and only if at least one of `P(x1), P(x2), …, P(xn)` is true.
* **Connections between Quantification and Looping**: It is sometimes helpful to think in terms of looping and searching when determining the truth value of a quantiﬁcation. Suppose that there are n objects in the domain for the variable x. To determine whether ∀xP(x) is true, we can loop through all n values of x to see whether P(x) is always true. If we encounter a value x for which P(x) is false, then we have shown that ∀xP(x) is false. Otherwise, ∀xP(x) is true. To see whether ∃xP(x) is true, we loop through the n values of x searching for a value for which P(x) is true. If we ﬁnd one, then ∃xP(x) is true. If we never ﬁnd such an x, then we have determined that ∃xP(x) is false. (Note that this searching procedure does not apply if there are inﬁnitely many values in the domain. However, it is still a useful way of thinking about the truth values of quantiﬁcations.)

> [!Error] 1.4.5 Quantifiers with Restricted Domains

* An abbreviated notation is often used to restrict the domain of a quantiﬁer. In this notation, a condition a variable must satisfy is included after the quantiﬁer.
	* `∀x < 0 (x2 > 0)` which can be expressed as `∀x(x < 0 → x2 > 0)`
	* `∀y ≠ 0 (y3 ≠ 0)` which can be expressed as `∀y(y ≠ 0 → y3 ≠ 0)`
	* `∃z > 0 (z2 = 2)` which can be expressed as `∃z(z > 0 ∧ z2 = 2)`
* Note that the restriction of a universal quantiﬁcation is the same as the universal quantiﬁcation of a *conditional statement*.
	* For instance, `∀x < 0 (x2 > 0)` is another way of expressing `∀x(x < 0 → x2 > 0)`.
* On the other hand, the restriction of an existential quantiﬁcation is the same as the existential quantiﬁcation of a *conjunction*.
	* For instance, `∃z > 0 (z2 = 2)` is another way of expressing `∃z(z > 0 ∧ z2 = 2)`.

> [!Error] 1.4.6 Precedence of Quantifiers

* The quantiﬁers ∀ and ∃ have higher precedence than all logical operators from propositional calculus. For example, `∀xP(x) ∨ Q(x)` is the disjunction of ∀xP(x) and Q(x). In other words, it means `(∀xP(x)) ∨ Q(x)` rather than `∀x(P(x) ∨ Q(x))`.

> [!Error] 1.4.7 Binding Variables

* When a quantiﬁer is used on the variable x, we say that this occurrence of the variable is bound. An occurrence of a variable that is not bound by a quantiﬁer or set equal to a particular value is said to be free. All the variables that occur in a propositional function must be bound or set equal to a particular value to turn it into a proposition. This can be done using a combination of universal quantiﬁers, existential quantiﬁers, and value assignments.
* The part of a logical expression to which a quantiﬁer is applied is called the scope of this quantiﬁer. Consequently, a variable is free if it is outside the scope of all quantiﬁers in the formula that specify this variable.

> [!Error] 1.4.8 Logical Equivalences involving Quantifiers

> [!Info] Definition
> Statements involving predicates and quantiﬁers are *logically equivalent* if and only if they have the same truth value no matter which predicates are substituted into these statements and which domain of discourse is used for the variables in these propositional functions. We use the notation S ≡ T to indicate that two statements S and T involving predicates and quantiﬁers are logically equivalent.

> [!Error] 1.4.9 Negating Quantified Expressions

* We will often want to consider the negation of a quantiﬁed expression. For instance, consider the negation of the statement: “Every student in your class has taken a course in calculus.”
	* This statement is a universal quantiﬁcation, namely, ∀xP(x),
	* where P(x) is the statement “x has taken a course in calculus” and the domain consists of the students in your class.
	* The negation of this statement is “It is not the case that every student in your class has taken a course in calculus.”
	* This is equivalent to “There is a student in your class who has not taken a course in calculus.”
	* And this is simply the existential quantiﬁcation of the negation of the original propositional function, namely, ∃x ¬P(x).
* This example illustrates the following logical equivalence:
	* ¬∀xP(x) ≡ ∃x ¬P(x).
	* ¬∃xQ(x) ≡ ∀x ¬Q(x).

| Negation | Equivalent Statement | When is negation True? | When False? | De Morgan's Laws for Quantifiers |
| :-: | :-: | :-: | :-: | :-: |
| ¬∃*xP(x)* | ∀*x*¬*P(x)* | For every x, P(x) is false. | There is an x for which P(x) is true. |
| ¬∀*xP(x)* | ∃*x*¬*P(x)* | There is an x for which P(x) is false. | P(x) is true for every x. |

* **Remark**: When the domain of a predicate P(x) consists of n elements, where n is a positive integer greater than one, the rules for negating quantiﬁed statements are exactly the same as De Morgan’s laws. This is why these rules are called De Morgan’s laws for quantiﬁers. When the domain has n elements `x1, x2, …, xn`, it follows that ¬∀xP(x) is the same as `¬(P(x1) ∧ P(x2) ∧ ⋯ ∧ P(xn))`, which is equivalent to `¬P(x1) ∨ ¬P(x2) ∨ ⋯ ∨ ¬P(xn)` by De Morgan’s laws, and this is the same as ∃x¬P(x). Similarly, ¬∃xP(x) is the same as `¬(P(x1) ∨ P(x2) ∨ ⋯ ∨ P(xn))`, which by De Morgan’s laws is equivalent to `¬P(x1) ∧ ¬P(x2) ∧ ⋯ ∧ ¬P(xn)`, and this is the same as ∀x¬P(x).

##### 1.5 Nested Quantifiers
> `pg: 9`
> `time req: 59"`
> `time done: 50"`
> `performance: 120%`
> 
> `questions: 52`
> `questions done: 13`
> `practice time req: 35"`
> `practice time done: 2'`
> `p-performance: 29%`

> [!Error] 1.5.2 Understanding Statements involving Nested Quantifiers

* **Thinking of Quantification as Loops**: In working with quantiﬁcations of more than one variable, it is sometimes helpful to think in terms of nested loops. (If there are inﬁnitely many elements in the domain of some variable, we cannot actually loop through all values. Nevertheless, this way of thinking is helpful in understanding nested quantiﬁers.)
	* For example, to see whether `∀x∀yP(x, y)` is true, we loop through the values for `x`, and for each `x` we loop through the values for `y`. If we ﬁnd that for all values of `x` that `P(x, y)` is true for all values of `y`, we have determined that `∀x∀yP(x, y)` is true. If we ever hit a value `x` for which we hit a value `y` for which `P(x, y)` is false, we have shown that `∀x∀yP(x, y)` is false.
	* Similarly, to determine whether `∀x∃yP(x, y)` is true, we loop through the values for `x`. For each `x` we loop through the values for `y` until we ﬁnd a `y` for which `P(x, y)` is true. If for every `x` we hit such a `y`, then `∀x∃yP(x, y)` is true; if for some `x` we never hit such a `y`, then `∀x∃yP(x, y)` is false.
	* To see whether `∃x∀yP(x, y)` is true, we loop through the values for `x` until we ﬁnd an `x` for which `P(x, y)` is always true when we loop through all values for `y`. Once we ﬁnd such an `x`, we know that `∃x∀yP(x, y)` is true. If we never hit such an `x`, then we know that `∃x∀yP(x, y)` is false.
	* Finally, to see whether `∃x∃yP(x, y)` is true, we loop through the values for `x`, where for each `x` we loop through the values for `y` until we hit an `x` for which we hit a `y` for which `P(x, y)` is true. The statement `∃x∃yP(x, y)` is false only if we never hit an `x` for which we hit a `y` such that `P(x, y)` is true.

> [!Error] 1.5.3 The Order of Quantifiers

* Many mathematical statements involve multiple quantiﬁcations of propositional functions involving more than one variable. It is important to note that the order of the quantiﬁers is important, unless all the quantiﬁers are universal quantiﬁers or all are existential quantiﬁers.

| Statement | When True? | When False? |
| :-: | :-: | :-: |
| ∀x∀yP(x, y) | P(x, y) is true for every pair x, y. | There is a pair x, y for which P(x, y) is false. |
| ∀y∀xP(x, y) | | |
| ∀x∃yP(x, y) | For every x there is a y for which P(x, y) is true. | There is an x such that P(x, y) is false for every y. |
| ∃x∀yP(x, y) | There is an x for which P(x, y) is true for every y. | For every x there is a y for which P(x, y) is false. |
| ∃x∃yP(x, y) | There is a pair x, y for which P(x, y) is true. | P(x, y) is false for every pair x, y. |
| ∃y∃xP(x, y) | | |

##### 1.6 Rules of Inference
> `pg: 9`
> `time req: 59"`
> `time done: 1' 20"`
> `performance: 73%`
>
> `questions: 35`
> `questions done: 12`
> `practice time req: 35"`
> `practice time done: 55"`
> `p-performance: 63%`

> [!Error] 1.6.1 Introduction

* Proofs in mathematics are valid arguments that establish the truth of mathematical statements.
* By an **argument**, we mean a sequence of statements that end with a conclusion.
* By **valid**, we mean that the conclusion, or ﬁnal statement of the argument, must follow from the truth of the preceding statements, or **premises**, of the argument.
	* That is, an argument is valid if and only if it is *impossible* for all the premises to be true and the conclusion to be false.
* To deduce new statements from statements we already have, we use rules of inference which are templates for constructing valid arguments. Rules of inference are our basic tools for establishing the truth of statements.
* The rules of inference are among the most important ingredients in producing valid arguments.
* There are some common forms of incorrect reasoning, called **fallacies**, which lead to invalid arguments.

> [!Error] 1.6.2 Valid Arguments in Propositional Logic

> [!Example] Sample: `form of an Argument`
> p -> q
> p
> ---
> ∴ q
> * ∴ is the symbol that denotes "therefore".

* An argument is valid, because its form is valid.
* To analyze an argument, we can replace propositions by propositional variables. This changes an argument to an **argument form**.
	* The validity of an argument follows from the validity of the form of the argument.

> [!Info] Definition
> An **argument** in propositional logic is a sequence of propositions. All but the ﬁnal proposition in the argument are called **premises** and the ﬁnal proposition is called the **conclusion**. An argument is **valid** if the truth of all its premises implies that the conclusion is true.
> An **argument form** in propositional logic is a sequence of compound propositions involving propositional variables. An argument form is **valid** if no matter which particular propositions are substituted for the propositional variables in its premises, the conclusion is true if the premises are all true.
* **Remark**: From the deﬁnition of a valid argument form we see that the argument form with premises `p1, p2, …, pn` and conclusion q is valid exactly when `(p1 ∧ p2 ∧ ⋯ ∧ pn ) → q` is a tautology.
* The key to showing that an argument in propositional logic is valid is to show that its argument form is valid.

> [!Error] 1.6.3 Rules of Inference for Propositional Logic

* Instead of using truth tables - which can be extremely tedious - we can ﬁrst establish the validity of some relatively simple argument forms, called **rules of inference**.

> [!Warning] Table 1: `Rules of Inference`

1. Modes Ponens (a.k.a law of detachment)
> tautology: (p ∧ (p → q)) → q
>> p
>> p -> q
>> --
>> ∴ q
2. Modus tollens
> (¬q ∧ (p → q)) → ¬p
>> ¬q
>> p→q
>> --
>> ∴ ¬p
3. Hypothetical syllogism
> ((p → q) ∧ (q → r)) → (p → r)
>> p -> q
>> q -> r
>> --
>> ∴ p -> r
4. Disjunctive syllogism
> ((p ∨ q) ∧ ¬p) → q
>> p∨q
>> ¬p
>> --
>> ∴ q
5. Addition
> p → (p ∨ q)
>> p
>> .--
>> ∴ p∨q
1. Simpliﬁcation
> (p ∧ q) → p
>> p ∧ q
>> .--
>> ∴ p
7. Conjunction
> ((p) ∧ (q)) → (p ∧ q)
>> p
>> q
>> --
>> ∴ p∧q
8. Resolution
> ((p ∨ q) ∧ (¬p ∨ r)) → (q ∨ r)
>> p∨q
>> ¬p ∨ r
>> --
>> ∴ q∨r

> [!Error] 1.6.5 Resolution

* Resolution can be used to build automatic theorem proving systems. 
* To construct proofs in propositional logic using resolution as the only rule of inference, the hypotheses and the conclusion must be expressed as **clauses**, where a clause is a disjunction of variables or negations of these variables.
* We can replace a statement in propositional logic that is not a clause by one or more equivalent statements that are clauses.
* For example, suppose we have a statement of the form `p ∨ (q ∧ r)`. Because `p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)`, we can replace the single statement `p ∨ (q ∧ r)` by two statements `p ∨ q` and `p ∨ r`, each of which is a clause. We can replace a statement of the form `¬(p ∨ q)` by the two statements `¬p` and `¬q` because De Morgan’s law tells us that `¬(p ∨ q) ≡ ¬p ∧ ¬q`. We can also replace a conditional statement `p → q` with the equivalent disjunction `¬p ∨ q`.

> [!Error] 1.6.6 Fallacies

* Several common fallacies arise in incorrect arguments. These fallacies resemble rules of inference, but are based on contingencies rather than tautologies.
* The proposition `((p → q) ∧ q) → p` is not a tautology, because it is false when `p` is false and `q` is true. However, there are many incorrect arguments that treat this as a tautology. In other words, they treat the argument with premises `p → q` and `q` and conclusion `p` as a valid argument form, which it is not. This type of incorrect reasoning is called the **fallacy of aﬃrming the conclusion**.
* The proposition `((p → q) ∧ ¬p) → ¬q` is not a tautology, because it is false when `p` is false and `q` is true. Many incorrect arguments use this incorrectly as a rule of inference. This type of incorrect reasoning is called the **fallacy of denying the hypothesis**.

> [!Error] 1.6.7 Rules of Inference for Quantified Statements

* **Universal instantiation** is the rule of inference used to conclude that `P(c)` is true, where `c` is a particular member of the domain, given the premise `∀xP(x)`. Universal instantiation is used when we conclude from the statement “All women are wise” that “Lisa is wise,” where Lisa is a member of the domain of all women.
>> ∀xP(x)
>> .--
>> ∴ P(c)
* **Universal generalization** is the rule of inference that states that `∀xP(x)` is true, given the premise that `P(c)` is true for all elements `c` in the domain. Universal generalization is used when we show that `∀xP(x)` is true by taking an arbitrary element `c` from the domain and showing that `P(c)` is true. The element `c` that we select must be an arbitrary, and not a speciﬁc, element of the domain. That is, when we assert from `∀xP(x)` the existence of an element `c` in the domain, we have no control over `c` and cannot make any other assumptions about `c` other than it comes from the domain. Universal generalization is used implicitly in many proofs in mathematics and is seldom mentioned explicitly. However, the error of adding unwarranted assumptions about the arbitrary element `c` when universal generalization is used is all too common in incorrect reasoning.
>> P(c) for an arbitrary c
>> .--
>> ∴ ∀xP(x)
* **Existential instantiation** is the rule that allows us to conclude that there is an element `c` in the domain for which `P(c)` is true if we know that `∃xP(x)` is true. We cannot select an arbitrary value of `c` here, but rather it must be a `c` for which `P(c)` is true. Usually we have no knowledge of what `c` is, only that it exists. Because it exists, we may give it a name (`c`) and continue our argument.
>> ∃xP(x)
>> .--
>> ∴ P(c) for some element c
* **Existential generalization** is the rule of inference that is used to conclude that `∃xP(x)` is true when a particular element `c` with `P(c)` true is known. That is, if we know one element `c` in the domain for which `P(c)` is true, then we know that `∃xP(x)` is true.
>> P(c) for some element c
>> ∴ ∃xP(x)

##### 1.7 Introduction to Proofs
> `pg: 12`
> `time req: 1' 19"`
> `time done: 2' 5"`
> `performance: 63%`
>
> `questions: 44`
> `questions done: 12`
> `practice time req: 46"`
> `practice time done: 2' 25"`
> `p-performance: 31%`

> [!Error] 1.7.1 Introduction

* A proof is a valid argument that establishes the truth of a mathematical statement.
	* A proof can use the hypotheses of the theorem, if any, axioms assumed to be true, and previously proven theorems.
	* Using these ingredients and rules of inference, the ﬁnal step of the proof establishes the truth of the statement being proved.
* In practice, the proofs of theorems designed for human consumption are almost always **informal proofs**, where more than one rule of inference may be used in each step, where steps may be skipped, where the axioms being assumed and the rules of inference used are not explicitly stated.

> [!Question] `define: axiom`
> a statement or proposition which is regarded as being established, accepted, or self-evidently true.
> `math::` a statement or *proposition* on which an abstractly defined structure is based.

> [!Error] 1.7.2 Some Terminology

* Formally, a **theorem** is a statement that can be shown to be true.
	* In mathematical writing, the term theorem is usually reserved for a statement that is considered at least somewhat important.
	* Less important theorems sometimes are called **propositions**. (Theorems can also be referred to as **facts** or **results**.)
	* A theorem may be the universal quantiﬁcation of a conditional statement with one or more premises and a conclusion. However, it may be some other type of logical statement.
* We demonstrate that a theorem is true with a **proof**. 
	* A proof is a valid argument that establishes the truth of a theorem.
	* The statements used in a proof can include **axioms** (or **postulates**), which are statements we  assume to be true, the premises, if any, of the theorem, and previously proven theorems.
	* Axioms may be stated using primitive terms that do not require deﬁnition, but all other terms used in theorems and their proofs must be deﬁned.
* Rules of inference, together with deﬁnitions of terms, are used to draw conclusions from other assertions, tying together the steps of a proof.
* A less important theorem that is helpful in the proof of other results is called a **lemma** (plural *lemmas* or *lemmata*).
	* Complicated proofs are usually easier to understand when they are proved using a series of lemmas, where each lemma is proved individually.
* A **corollary** is a theorem that can be established directly from a theorem that has been proved.
* A **conjecture** is a statement that is being proposed to be a true statement, usually on the basis of some partial evidence, a heuristic argument, or the intuition of an expert.
	* When a proof of a conjecture is found, the conjecture becomes a theorem. Many times conjectures are shown to be false, so they are not theorems.

> [!Question] `define: postulate`
> an assumption used as a basis for mathematical reasoning

> [!Error] 1.7.5 Direct Proofs

* A direct proof of a conditional statement p → q is constructed when the ﬁrst step is the assumption that p is true; subsequent steps are constructed using rules of inference, with the ﬁnal step showing that q must also be true.
* A direct proof shows that a conditional statement p → q is true by showing that if p is true, then q must also be true, so that the combination p true and q false never occurs.
* In a direct proof, we assume that p is true and use axioms, deﬁnitions, and previously proven theorems, together with rules of inference, to show that q must also be true.
* You will ﬁnd that direct proofs of many results are quite straightforward. Starting with the hypothesis and leading to the conclusion, the way forward is essentially dictated by the premises available at that step.

> [!Info] Definition
> The integer `n` is even if there exists an integer `k` such that `n = 2k`, and `n` is odd if there exists an integer `k` such that `n = 2k + 1`. (Note that every integer is either even or odd, and no integer is both even and odd.) Two integers have the *same parity* when both are even or both are odd; they have *opposite parity* when one is even and the other is odd.

> [!Error] 1.7.6 Prrof by Contraposition

* Direct proofs lead from the premises of a theorem to the conclusion. They begin with the premises, continue with a sequence of deductions, and end with the conclusion.
	* However, we will see that attempts at direct proofs often reach dead ends.
	* We need other methods of proving theorems of the form ∀x(P(x) → Q(x)).
	* Proofs of theorems of this type that are not direct proofs, that is, that do not start with the premises and end with the conclusion, are called **indirect proofs**.
* An extremely useful type of indirect proof is known as **proof by contraposition**. Proofs by contraposition make use of the fact that the conditional statement `p → q` is equivalent to its contrapositive, `¬q → ¬p`. This means that the conditional statement `p → q` can be proved by showing that its contrapositive, `¬q → ¬p`, is true. In a proof by contraposition of `p → q`, we take `¬q` as a premise, and using axioms, deﬁnitions, and previously proven theorems, together with rules of inference, we show that `¬p` must follow.

> [!Question] `define: vacuous`
> having or showing a lack of thought or intelligence; mindless.

* **Vacuous and Trivial Proofs**
	* We can quickly prove that a conditional statement `p → q` is true when we know that `p` is false, because `p → q` must be true when `p` is false. Consequently, if we can show that `p` is false, then we have a proof, called a vacuous proof, of the conditional statement `p → q`. Vacuous proofs are often used to establish special cases of theorems that state that a conditional statement is true for all positive integers \[i.e., a theorem of the kind `∀nP(n)`, where `P(n)` is a propositional function\]. (refer to section 5.1)
	* We can also quickly prove a conditional statement `p → q` if we know that the conclusion `q` is true. By showing that `q` is true, it follows that `p → q` must also be true. A proof of `p → q` that uses the fact that `q` is true is called a **trivial proof**. (refer to section 5.1)

* **A Little Proof Strategy**
	* When you are presented with a theorem of the form `∀x(P(x) → Q(x))`, which method should you use to attempt to prove it? Here's a few rules of thumb.
	* When you want to prove a statement of the form ∀x(P(x) → Q(x)), ﬁrst evaluate whether a direct proof looks promising. Begin by expanding the deﬁnitions in the hypotheses. Start to reason using these hypotheses, together with axioms and available theorems. If a direct proof does not seem to go anywhere (Examples 3 and 4), try the same thing with a proof by contraposition.
	* Hypotheses such as x is irrational or x ≠ 0 that are diﬃcult to reason from are a clue that an indirect proof might be your best bet.
	* Recall that in a proof by contraposition you assume that the conclusion of the conditional statement is false and use a direct proof to show this implies that the hypothesis must be false.
	* Often, you will ﬁnd that a proof by contraposition is easily constructed from the negation of the conclusion (Examples 7 and 8).

> [!Info] Definition: `rational real numbers`
> The real number `r` is rational if there exist integers `p` and `q` with `q ≠ 0` such that `r = p/q`. A real number that is not rational is called *irrational*.

> [!Error] 1.7.7 Proofs by Contradiction

* Suppose we want to prove that a statement `p` is true. Furthermore, suppose that we can ﬁnd a contradiction `q` such that `¬p → q` is true. Because `q` is false, but `¬p → q` is true, we can conclude that `¬p` is false, which means that p is true. How can we ﬁnd a contradiction `q` that might help us prove that `p` is true in this way?
* Because the statement `r ∧ ¬r` is a contradiction whenever r is a proposition, we can prove that `p` is true if we can show that `¬p → (r ∧ ¬r)` is true for some proposition `r`.
	* Proofs of this type are called proofs by contradiction.
	* Because a proof by contradiction does not prove a result directly, it is another type of *indirect proof*.
	* (refer to section 6.2)
* Proof by contradiction can be used to prove conditional statements.
	* In such proofs, we ﬁrst assume the negation of the conclusion.
	* We then use the premises of the theorem and the negation of the conclusion to arrive at a contradiction.
	* The reason that such proofs are valid rests on the logical equivalence of `p → q` and `(p ∧ ¬q) → F`.
		* To see that these statements are equivalent, simply note that each is false in exactly one case, namely, when `p` is true and `q` is false.
	* Note that we can rewrite a proof by contraposition of a conditional statement as a proof by contradiction.
	* In a proof of `p → q` by contraposition, we assume that `¬q` is true. We then show that `¬p` must also be true. To rewrite a proof by contraposition of `p → q` as a proof by contradiction, we suppose that both `p` and `¬q` are true. Then, we use the steps from the proof of `¬q → ¬p` to show that `¬p` is true. This leads to the contradiction `p ∧ ¬p`, completing the proof.
	* Note that we can also prove by contradiction that `p → q` is true by assuming that `p` and `¬q` are true, and showing that `q` must be also be true. This implies that `¬q` and `q` are both true, a contradiction. This observation tells us that we can turn a direct proof into a proof by contradiction.

* **Proofs of Equivalence**
	* To prove a theorem that is a biconditional statement, that is, a statement of the form `p ↔ q`, we show that `p → q` and `q → p` are both true. The validity of this approach is based on the tautology:
		* (p ↔ q) ↔ (p → q) ∧ (q → p)
	* Sometimes a theorem states that several propositions are equivalent. Such a theorem states that propositions `p1, p2, p3, …, pn` are equivalent. This can be written as
		* `p1 ↔ p2 ↔ ⋯ ↔ pn,`
	* which states that all n propositions have the same truth values, and consequently, that for all `i` and `j` with `1 ≤ i ≤ n` and `1 ≤ j ≤ n`, `pi` and `pj` are equivalent. One way to prove these are mutually equivalent is to use the tautology
		* `p1 ↔ p2 ↔ ⋯ ↔ pn ↔ (p1 → p2) ∧ (p2 → p3) ∧ ⋯ ∧ (pn → p1)`.
	* This shows that if the n conditional statements `p1 → p2, p2 → p3, …, pn → p1` can be shown to be true, then the propositions `p1, p2, …, pn` are all equivalent.
	* This is much more eﬃcient than proving that `pi → pj` for all `i ≠ j` with `1 ≤ i ≤ n` and `1 ≤ j ≤ n`. (Note that there are `n2 − n` such conditional statements.)
	* When we prove that a group of statements are equivalent, we can establish any chain of conditional statements we choose as long as it is possible to work through the chain to go from any one of these statements to any other statement.
		* For example, we can show that `p1`, `p2`, and `p3` are equivalent by showing that `p1 → p3, p3 → p2, and p2 → p1`.

* **Counterexamples**: To show that a statement of the form `∀xP(x)` is false, we need only ﬁnd a counterexample, that is, an example `x` for which `P(x)` is false. When presented with a statement of the form `∀xP(x)`, which we believe to be false or which has resisted all proof attempts, we look for a counterexample.

> [!Error] 1.7.8 Mistakes to Proofs

* There are many common errors made in constructing mathematical proofs.
* Among the most common errors are mistakes in arithmetic and basic algebra.
	* Even professional mathematicians make such errors, especially when working with complicated formulae.
	* Whenever you use such computations you should check them as carefully as possible.

> [!Error] 1.7.9 Just a Beginning

Constructing proofs is an art that can be learned only through experience, including writing proofs, having your proofs critiqued, and reading and analyzing other proofs.

> [!Error] Notes from the Solutions Manual

* Learning to construct good mathematical proofs takes years. There is no algorithm for constructing the proof of a true proposition (there is actually a deep theorem in mathematical logic that says this). Instead, the construction of a valid proof is an art, honed after much practice. There are two problems for the beginning student-figuring out the key ideas in a problem (what is it that really makes the proposition true?) and writing down the proof in acceptable mathematical language.
* Here are some general things to keep in mind in constructing proofs. First, of course, you need to find out exactly what is going on-why the proposition is true. This can take anywhere from ten seconds (for a really simple proposition) to a lifetime (some mathematicians have spent their entire careers trying to prove certain conjectures). For a typical student at this level, tackling a typical problem, the median might be somewhere around 15 minutes. This time should be spent looking at examples, making tentative assumptions, breaking the problem down into cases, perhaps looking at analogous but simpler problems, and in general bringing all of your mathematical intuition and training to bear.
* It is often easiest to give a proof by contradiction, since you get to assume the most (all the hypotheses as well as the negation of the conclusion), and all you have to do is to derive a contradiction. Another thing to try early in attacking a problem is to separate the proposition into several cases; proof by cases is a valid technique, if you make sure to include all the possibilities. In proving propositions, all the rules of inference are at your disposal, as well as axioms and previously proved results. Ask yourself what definitions, axioms, or other theorems might be relevant to the problem at hand. **The importance of constantly returning to the definitions cannot be overstated!**
* Once you think you see what is involved, you need to write down the proof. In doing so, pay attention both to content (does each statement follow logically? are you making any fallacious arguments? are you leaving out any cases or using hidden assumptions?) and to style. There are certain conventions in mathematical proofs, and you need to follow them. For example, you must use complete sentences and say exactly what you mean. (An equation is a complete sentence, with "equals" as the verb; however, a good proof will usually have more English words than mathematical symbols in it.) The point of a proof is to convince the reader that your line of argument is sound, and that therefore the proposition under discussion is true; put yourself in the reader's shoes, and ask yourself whether you are convinced.
* The more proofs you write, utilizing the different methods discussed in this section, the better you will become at it. As a bonus, your ability to construct and respond to nonmathematical arguments (politics, religion, or whatever) will be enhanced. Good luck!

##### 1.8 Proof Methods and Strategy
> `pg: 18`
> `time req: 1' 59"`
> `time done: 2' 3"`
> `performance: 96%`
>
> `questions: 52`
> `practice time req: 1' 10"`
> `practice time done: 25"`
> `p-performance: 280%`
> <span style="color: red">I gave up. I strongly dislike proofs!</span>

> [!Error] 1.8.2 Exhaustive Proof and Proof by Cases

* Sometimes we cannot prove a theorem using a single argument that holds for all possible cases. We now introduce a method that can be used to prove a theorem by considering diﬀerent cases separately. This method is based on a rule of inference that we will now introduce.
* To prove a conditional statement of the form
* `(p1 ∨ p2 ∨ ⋯ ∨ pn ) → q `
* the tautology
* `[(p1 ∨ p2 ∨ ⋯ ∨ pn ) → q] ↔ [(p1 → q) ∧ (p2 → q) ∧ ⋯ ∧ (pn → q)]`
* can be used as a rule of inference.
* This shows that the original conditional statement with a hypothesis made up of a disjunction of the propositions `p1, p2, …, pn` can be proved by proving each of the n conditional statements `pi → q`, i = 1, 2, …, n, individually.
* Such an argument is called a proof by cases. Sometimes to prove that a conditional statement `p → q` is true, it is convenient to use a disjunction `p1 ∨ p2 ∨ ⋯ ∨ pn` instead of `p` as the hypothesis of the conditional statement, where `p` and `p1 ∨ p2 ∨ ⋯ ∨ pn` are equivalent.

* **Exhaustive Proofs**: Some theorems can be proved by examining a relatively small number of examples. Such proofs are called **exhaustive proofs**, or **proofs by exhaustion** because these proofs proceed by exhausting all possibilities. An exhaustive proof is a special type of proof by cases where each case involves checking a single example. We now provide some illustrations of exhaustive proofs.
	* Proofs by exhaustion can tire out people and computers when the number of cases challenges the available processing power!
* **Proof by Cases**: A proof by cases must cover all possible cases that arise in a theorem. We illustrate proof by cases with a couple of examples. In each example, you should check that all possible cases are covered.
* **Leveraging Proof by Cases**: In particular, when it is not possible to consider all cases of a proof at the same time, a proof by cases should be considered. When should you use such a proof? Generally, look for a proof by cases when there is no obvious way to begin a proof, but when extra information in each case helps move the proof forward.
* **Without Loss of Generality**
	* In general, when the phrase “without loss of generality” is used in a proof (often abbreviated as WLOG), we assert that by proving one case of a theorem, no additional argument is required to prove other speciﬁed cases. That is, other cases follow by making straightforward changes to the argument, or by ﬁlling in some straightforward initial step.
	* Proofs by cases can often be made much more eﬃcient when the notion of without loss of generality is employed.
	* Incorrect use of this principle, however, can lead to unfortunate errors. Sometimes assumptions are made that lead to a loss in generality. Such assumptions can be made that do not take into account that one case may be substantially diﬀerent from others. This can lead to an incomplete, and possibly unsalvageable, proof. In fact, many incorrect proofs of famous theorems turned out to rely on arguments that used the idea of “without loss of generality” to establish cases that could not be quickly proved from simpler cases.
* **Common Errors with Exhaustive Proofs and Proof by Cases**: A common error of reasoning is to draw incorrect conclusions from examples. No matter how many separate examples are considered, a theorem is not proved by considering examples unless every possible case is covered. The problem of proving a theorem is analogous to showing that a computer program always produces the output desired. No matter how many input values are tested, unless all input values are tested, we cannot conclude that the program always produces the correct output.

> [!Error] 1.8.3 Existence Proofs

* Many theorems are assertions that objects of a particular type exist.
* A theorem of this type is a proposition of the form `∃xP(x)`, where `P` is a predicate.
* A proof of a proposition of the form `∃xP(x)` is called an **existence proof**.
* There are several ways to prove a theorem of this type.
* Sometimes an existence proof of `∃xP(x)` can be given by ﬁnding an element `a`, called a **witness**, such that `P(a)` is true. This type of existence proof is called **constructive**.
* It is also possible to give an existence proof that is **nonconstructive**; that is, we do not ﬁnd an element a such that `P(a)` is true, but rather prove that `∃xP(x)` is true in some other way.
	* One common method of giving a nonconstructive existence proof is to use proof by contradiction and show that the negation of the existential quantiﬁcation implies a contradiction.

> [!Error] 1.8.4 Uniqueness Proofs

* Some theorems assert the existence of a unique element with a particular property. In other words, these theorems assert that there is exactly one element with this property.
* To prove a statement of this type we need to show that an element with this property exists and that no other element has this property.
* The two parts of a **uniqueness proof** are:
	* <span style="color: orange">Existence:</span> We show that an element x with the desired property exists.
	* <span style="color: orange">Uniqueness:</span> We show that if x and y both have the desired property, then x = y.
* **Remark**: Showing that there is a unique element `x` such that `P(x)` is the same as proving the statement `∃x(P(x) ∧ ∀y(y ≠ x → ¬P(y)))`.

> [!Error] 1.8.5 Proof Strategies

* Finding proofs can be a challenging business.
	* When you are confronted with a statement to prove, you should ﬁrst replace terms by their deﬁnitions and then carefully analyze what the hypotheses and the conclusion mean.
	* After doing so, you can attempt to prove the result using one of the available methods of proof.

* **Forward and Backward Reasoning**
	* Whichever method you choose, you need a starting point for your proof.
	* To begin a direct proof of a conditional statement, you start with the premises. Using these premises, together with axioms and known theorems, you can construct a proof using a sequence of steps that leads to the conclusion. This type of reasoning, called *forward reasoning*, is the most common type of reasoning used to prove relatively simple results.
	* Similarly, with indirect reasoning you can start with the negation of the conclusion and, using a sequence of steps, obtain the negation of the premises.
	* Unfortunately, forward reasoning is often diﬃcult to use to prove more complicated results, because the reasoning needed to reach the desired conclusion may be far from obvious. In such cases it may be helpful to use *backward reasoning*. To reason backward to prove a statement `q`, we ﬁnd a statement `p` that we can prove with the property that `p → q`.
		* Note that it is not helpful to ﬁnd a statement `r` that you can prove such that `q → r`, because it is the fallacy of begging the question to conclude from `q → r` and `r` that `q` is true.

* **Adapting Existing Proofs**: An excellent way to look for possible approaches that can be used to prove a statement is to take advantage of existing proofs of similar results. Often an existing proof can be adapted to prove other facts. Even when this is not the case, some of the ideas used in existing proofs may be helpful. Because existing proofs provide clues for new proofs, you should read and understand the proofs you encounter in your studies.

#### Chapter 2: Basic Structures: Sets, Functions, Sequences, Sums, and Matrices
> [!Summary]
> `sum page: 76`
> `sum time req: 8' 23"`

* The concept of a function is extremely important in discrete mathematics.
* A function assigns to each element of a ﬁrst set exactly one element of a second set, where the two sets are not necessarily distinct.
* Functions play important roles throughout discrete mathematics. They are used to represent the computational complexity of algorithms, to study the size of sets, to count objects, and in a myriad of other ways.

##### 2.1 Sets
> `pg: 11`
> `time req: 1' 13"`
> `time done: 1' 36"`
> `performance: 76%`
>
> `questions: 51`
> `questions done: 19`
> `practice time req: 42"`
> `practice time done: 36"`
> `p-performance: 116%`

> [!Error] 2.1.1 Introduction

* The fundamental discrete structure on which all other discrete structures are built, is, the set.
* Sets are used to group objects together.
* Often, but not always, the objects in a set have similar properties.

> [!Info] Definition: `sets`
> A *set* is an unordered collection of distinct objects, called *elements* or *members* of the set. A set is said to contain its elements. We write `a ∈ A` to denote that `a` is an element of the set `A`. The notation `a ∉ A` denotes that `a` is not an element of the set `A`.
> > [!Warning] disclaimer
> > This definition is intuitive and is not part of a formal theory of sets.

* It is common for sets to be denoted using uppercase letters. Lowercase letters are usually used to denote elements of sets.
---
* One way to describe a set is to list all of the members of a set between braces `{}`. This way of describing a set is known as the **roster method**.
	* Sometimes the roster method is used to describe a set without listing all its members. Some members of the set are listed, and then *ellipses* (…) are used when the general pattern of the elements is obvious.
* Another way to describe a set is to use set builder notation.
	* We characterize all those elements in the set by stating the property or properties they must have to be members.
	* The general form of this notation is `{x ∣ x has property P}` and is read “the set of all x such that x has property P.”
---
* These sets, each denoted using a boldface letter, play an important role in discrete mathematics:
	* **N** = {0, 1, 2, 3, …}, the set of all **natural numbers**
	* **Z** = {… , −2, −1, 0, 1, 2, …}, the set of all **integers**
	* **Z+** = {1, 2, 3, …}, the set of all **positive integers**
	* **Q** = {p/q ∣ p ∈ Z, q ∈ Z, and q ≠ 0}, the set of all **rational numbers**
	* **R**, the set of all **real numbers**
	* **R+** , the set of all **positive real numbers**
	* **C**, the set of all **complex numbers**
---
* Among the sets studied in calculus and other subjects are **intervals**, sets of all the real numbers between two numbers a and b, with or without a and b. If a and b are real numbers with a ≤ b, we denote these intervals by
	* \[a, b\] = {x | a ≤ x ≤ b}
		* *closed interval from a to b*
	* \[a, b) = {x | a ≤ x < b}
	* (a, b\] = {x | a < x ≤ b}
	* (a, b) = {x | a < x < b}
		* *open interval from a to b*
---
* **Sets can have other sets as members**.
* **Remark**: Note that the concept of a datatype, or type, in computer science is built upon the concept of a set. In particular, a **datatype** or **type** is the name of a set, together with a set of operations that can be performed on objects from that set.
	* For example, boolean is the name of the set {0, 1}, together with operators on one or more elements of this set, such as AND, OR, and NOT.

> [!Info] Definition: `set equality`
> Two sets are equal if and only if they have the same elements. Therefore, if A and B are sets, then A and B are equal if and only if ∀x(x ∈ A ↔ x ∈ B). We write A = B if A and B are equal sets.

---
* **The Empty Set**
	* There is a special set that has no elements. This set is called the **empty set**, or **null set**, and is denoted by **∅**. The empty set can also be denoted by { }.
	* A set with one element is called a **singleton set**. A common error is to confuse the empty set ∅ with the set {∅}, which is a singleton set. The single element of the set {∅} is the empty set itself!
* **Native Set Theory**
	* Read page 124 of Discrete Mathematics - Kenneth H. Rosen

> [!Error] 2.1.3 Subsets

> [!Info] Definition: `subsets` and `supersets`
> The set `A` is a subset of `B`, and `B` is a superset of `A`, if and only if every element of `A` is also an element of `B`. We use the notation `A ⊆ B` to indicate that `A` is a subset of the set `B`. If, instead, we want to stress that `B` is a superset of `A`, we use the equivalent notation `B ⊇ A`. (So, `A ⊆ B` and `B ⊇ A` are equivalent statements.)

* We see that `A ⊆ B` if and only if the quantiﬁcation `∀x(x ∈ A → x ∈ B)` is true.
	* Note that to show that `A` is not a subset of `B` we need only ﬁnd one element `x ∈ A` with `x ∉ B`. Such an `x` is a counterexample to the claim that `x ∈ A` implies `x ∈ B`.
---
> [!Info] Theorem 1
> For every set S
> 1. `∅ ⊆ S`
> 2. `S ⊆ S`
>
> This shows that every nonempty set `S` is guaranteed to have at least two subsets, the empty set and the set `S` itself.

---
* When we wish to emphasize that a set `A` is a subset of a set `B` but that `A ≠ B`, we write `A ⊂ B` and say that `A` is a **proper subset** of `B`. For `A ⊂ B` to be true, it must be the case that `A ⊆ B` and there must exist an element `x` of `B` that is not an element of `A`. That is, `A` is a proper subset of `B` if and only if `∀x(x ∈ A → x ∈ B) ∧ ∃x(x ∈ B ∧ x ∉ A)`.

> [!Error] 2.1.4 The Size of a Set

> [!Info] Definition: `cardinality of sets`
> Let `S` be a set. If there are exactly `n` distinct elements in `S` where `n` is a nonnegative integer, we say that `S` is a ﬁnite set and that `n` is the cardinality of `S`. The cardinality of `S` is denoted by `|S|`.

* **Remark**: The term *cardinality* comes from the common usage of the term *cardinal number* as the size of a ﬁnite set.

> [!Info] Definition: `infinite sets`
> A set is said to be inﬁnite if it is not ﬁnite.

> [!Error] 2.1.5 Power Sets

* Many problems involve testing all combinations of elements of a set to see if they satisfy some property. To consider all such combinations of elements of a set `S`, we build a new set that has as its members all the subsets of `S`.

> [!Info] Definition: `power sets`
> Given `a` set `S`, the power set of `S` is the set of all subsets of the set `S`. The power set of `S` is denoted by `P(S)` (this is not *pee*).

* If a set has `n` elements, then its power set has `2n` elements.

> [!Error] 2.1.6 Cartesian Products

* The order of elements in a collection is often important. Because sets are unordered, a diﬀerent structure is needed to represent ordered collections. This is provided by **ordered n-tuples**.

> [!Info] Definition: `ordered n-tuples`
> The *ordered n-tuple* `(a1, a2, …, an)` is the ordered collection that has `a1` as its ﬁrst element, `a2` as its second element, …, and `an` as its nth element.

* We say that two ordered n-tuples are equal if and only if each corresponding pair of their elements is equal. In other words, `(a1, a2, …, an) = (b1, b2, …, bn)` if and only if `ai = bi` , for `i = 1, 2, … , n`.

> [!Info] Definition: `cartesian product of two sets`
> Let `A` and `B` be sets. The Cartesian product of `A` and `B`, denoted by `A × B`, is the set of all ordered pairs `(a, b)`, where `a ∈ A` and `b ∈ B`. Hence,
> - A × B = {(a, b) ∣ a ∈ A ∧ b ∈ B}.

* Note that the Cartesian products `A × B` and `B × A` are not equal unless `A = ∅` or `B = ∅`.

> [!Info] Definition: `cartesian product of more sets`
> The Cartesian product of the sets `A1, A2, …, An`, denoted by `A1 × A2 × ⋯ × An`, is the set of *ordered n-tuples* `(a1, a2, …, an)`, where `ai` belongs to `Ai` for `i = 1, 2, … , n`. In other words,
> - A1 × A2 × ⋯ × An = {(a1 , a2 , … , an ) ∣ ai ∈ Ai for i = 1, 2, … , n}.

* **Remark**: Note that when `A`, `B`, and `C` are sets, `(A × B) × C` is not the same as `A × B × C`.
* We use the notation `A**2` to denote `A × A`, the Cartesian product of the set `A` with itself. Similarly, `A**3` = `A × A × A`. More generally:
	* `An = {(a1, a2, …, an) ∣ ai ∈ A for i = 1, 2, … , n}.`
* A subset `R` of the Cartesian product `A × B` is called a **relation** from the set `A` to the set `B`. The elements of `R` are ordered pairs, where the ﬁrst element belongs to `A` and the second to `B`.
	* For example, `R = {(a, 0), (a, 1), (a, 3), (b, 1), (b, 2), (c, 0), (c, 3)}` is a relation from the set `{a, b, c}` to the set `{0, 1, 2, 3}`, and it is also a relation from the set `{a, b, c, d, e}` to the set `{0, 1, 3, 4)`.

> [!Error] 2.1.7 Using Set Notation with Quantifiers

* Sometimes we restrict the domain of a quantiﬁed statement explicitly by making use of a particular notation.
	* For example, `∀x ∈ S(P(x))` denotes the universal quantiﬁcation of `P(x)` over all elements in the set `S`. In other words, it is shorthand for `∀x(x ∈ S → P(x))`.
	* Similarly, `∃x ∈ S(P(x))` denotes the existential quantiﬁcation of `P(x)` over all elements in `S`. That is, it is shorthand for `∃x(x ∈ S ∧ P(x))`.

> [!Error] 2.1.8 Truth Sets and Quantifiers

* We will now tie together concepts from set theory and from predicate logic. Given a predicate `P`, and a domain `D`, we deﬁne the truth set of `P` to be the set of elements `x` in `D` for which `P(x)` is true. The truth set of `P(x)` is denoted by `{x ∈ D ∣ P(x)}`.

##### 2.2 Set Operations
> `pg: 11`
> `time req: 1' 13"`
> `time done: 58"`
> `performance: 125%`
> 
> `questions: 75`
> `practice time req: 42"`
> `practice time done: 28"`
> `p-performance: 150%`

> [!Error] 2.2.1 Introduction

> [!Info] Definition: `set union`
> Let `A` and `B` be sets. The *union* of the sets `A` and `B`, denoted by `A ∪ B`, is the set that contains those elements that are either in `A` or in `B`, or in both.

* An element `x` belongs to the union of the sets `A` and `B` if and only if `x` belongs to `A` or `x` belongs to `B`. This tells us that
	* A ∪ B = {x ∣ x ∈ A ∨ x ∈ B}.

> [!Info] Definition: `set intersection`
> Let `A` and `B` be sets. The *intersection* of the sets `A` and `B`, denoted by `A ∩ B`, is the set containing those elements in both `A` and `B`.

* An element `x` belongs to the intersection of the sets `A` and `B` if and only if `x` belongs to `A` and `x` belongs to `B`. This tells us that
	* A ∩ B = {x ∣ x ∈ A ∧ x ∈ B}.

> [!Info] Definition: `disjoint set`
> Two sets are called *disjoint* if their intersection is the empty set.

* We are often interested in ﬁnding the cardinality of a union of two ﬁnite sets `A` and `B`. Note that `|A| + |B|` counts each element that is in `A` but not in `B` or in `B` but not in `A` exactly once, and each element that is in both `A` and `B` exactly twice. Thus, if the number of elements that are in both `A` and `B` is subtracted from `|A| + |B|`, elements in `A ∩ B` will be counted only once. Hence,
	* |A ∪ B| = |A| + |B| − |A ∩ B|.
	* The generalization of this result to unions of an arbitrary number of sets is called the **principle of inclusion–exclusion**. The principle of inclusion–exclusion is an important technique used in enumeration.

> [!Info] Definition: `set difference`
> Let `A` and `B` be sets. The *diﬀerence* of `A` and `B`, denoted by `A − B`, is the set containing those elements that are in `A` but not in `B`. The diﬀerence of `A` and `B` is also called the complement of `B` with respect to `A`.

* **Remark**: The diﬀerence of sets `A` and `B` is sometimes denoted by `A∖B`.
* An element `x` belongs to the diﬀerence of `A` and `B` if and only if `x ∈ A` and `x ∉ B`. This tells us that
	* A − B = {x ∣ x ∈ A ∧ x ∉ B}.

* Once the universal set **U** has been speciﬁed, the complement of a set can be deﬁned.

> [!Info] Definition: `set complement`
> Let `U` be the universal set. The *complement* of the set `A`, denoted by `A'`, is the complement of `A` with respect to `U`. Therefore, the complement of the set `A` is `U − A`.

* An element belongs to `A'` if and only if `x ∉ A`. This tells us that
	* A' = {x ∈ U ∣ x ∉ A}.

> [!Error] 2.2.2 Set Identities

| Identity | Name | Set Identities |
| :- | :- | :- |
| A ∩ U = A | Identity Laws |
| A ∪ ∅ = A | |
| A ∪ U = U | Domination Laws |
| A ∩ ∅ = ∅ | |
| A ∪ A = A | Idempotent Laws |
| A ∩ A = A | |
| (A')' = A | Complementation Law |
| A ∪ B = B ∪ A | Commutative Laws |
| A ∩ B = B ∩ A | |
| A ∪ (B ∪ C) = (A ∪ B) ∪ C | Associative Laws |
| A ∩ (B ∩ C) = (A ∩ B) ∩ C | |
| A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) | Distributive Laws |
| A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) | |
| (A ∩ B)' = A' ∪ B' | De Morgan's Laws
| (A ∪ B)' = A' ∩ B' | |
| A ∪ (A ∩ B) = A | Absorption Laws |
| A ∩ (A ∪ B) = A | |
| A ∪ A' = U | Complement Laws
| A ∩ A' = ∅ | |

* Set identities can also be proved using **membership tables**. We consider each combination of the atomic sets (that is, the original sets used to produce the sets on each side) that an element can belong to and verify that elements in the same combinations of sets belong to both the sets in the identity. To indicate that an element is in a set, a 1 is used; to indicate that an element is not in a set, a 0 is used.
---
* **Methods of Proving Set Identities**
	* Subset Method: Show that each side of the identity is a subset of the other side.
	* Membership Table: For each possible combination of the atomic sets, show that an element in exactly these atomic sets must either belong to both sides or belong to neither side
	* Apply Existing Identities: Start with one side, transform it into the other side using a sequence of steps by applying an established identity.

> [!Error] 2.2.3 Generalized Unions and Intersections

> [!Info] Definition: `union of collection of sets`
> The *union* of a collection of sets is the set that contains those elements that are members of at least one set in the collection.

> [!Info] Definition: `intersection of collection of sets`
> The *intersection* of a collection of sets is the set that contains those elements that are members of all the sets in the collection.

> [!Error] 2.2.4 Computer Representation of Sets

* There are various ways to represent sets using a computer. One method is to store the elements of the set in an unordered fashion. However, if this is done, the operations of computing the union, intersection, or diﬀerence of two sets would be time consuming, because each of these operations would require a large amount of searching for elements. We will present a method for storing elements using an arbitrary ordering of the elements of the universal set. This method of representing sets makes computing combinations of sets easy.
* Assume that the universal set `U` is ﬁnite (and of reasonable size so that the number of elements of `U` is not larger than the memory size of the computer being used). First, specify an arbitrary ordering of the elements of `U`, for instance `a1`, `a2`, …, `an`. Represent a subset `A of U` with the bit string of length `n`, where the `ith` bit in this string is `1` if `ai` belongs to `A` and is `0` if `ai` does not belong to `A`.
* Using bit strings to represent sets, it is easy to ﬁnd complements of sets and unions, intersections, and diﬀerences of sets. To ﬁnd the bit string for the complement of a set from the bit string for that set, we simply change each `1` to a `0` and each `0` to `1`, because `x ∈ A` if and only if `x ∉ A`. Note that this operation corresponds to taking the negation of each bit when we associate a bit with a truth value—with `1` representing true and `0` representing false.
* To obtain the bit string for the union and intersection of two sets we perform bitwise Boolean operations on the bit strings representing the two sets. The bit in the `ith` position of the bit string of the union is `1` if either of the bits in the `ith` position in the two strings is `1` (or both are `1`), and is `0` when both bits are `0`. Hence, the bit string for the union is the bitwise OR of the bit strings for the two sets. The bit in the `ith` position of the bit string of the intersection is `1` when the bits in the corresponding position in the two strings are both `1`, and is `0` when either of the two bits is `0` (or both are). Hence, the bit string for the intersection is the bitwise AND of the bit strings for the two sets.

##### 2.3 Functions
> `pg: 15`
> `time req: 1' 39"`
> `time done: 1' 24"`
> `performance: 117%`
>
> `questions: 82`
> `practice time req: 58"`
> `practice time done: 50"`
> `p-performance: 116%`

> [!Question] ChatGPT
> Explain to me the domain, the codomain, the range, one-to-one-ness and onto-ness of functions.
>
> Certainly! Functions are fundamental concepts in mathematics, and understanding the terms you mentioned is crucial in the study of discrete mathematics.
>
> 1. **Domain:**
>    - The domain of a function is the set of all possible input values (independent variable) for which the function is defined. It represents the values that you can "plug into" the function to get an output.
>
> 2. **Codomain:**
>    - The codomain is the set of all possible output values (dependent variable) that the function could potentially produce. It is a larger set than the range and includes all possible values that the function might output.
> 
> 3. **Range:**
>    - The range of a function is the set of all actual output values that the function produces for the elements in the domain. In other words, it is the set of all possible results of the function.
> 
> 4. **One-to-One (Injective) Functions:**
>    - A function is said to be one-to-one (or injective) if each element in the domain maps to a unique element in the codomain. In other words, no two different elements in the domain map to the same element in the codomain.
> 
> 5. **Onto (Surjective) Functions:**
>    - A function is said to be onto (or surjective) if every element in the codomain is the image of at least one element in the domain. In other words, the range of the function covers the entire codomain.

> [!Error] 2.3.1 Introduction

> [!Info] Definition: `function`
> Let `A` and `B` be nonempty sets. A *function* `f` from `A` to `B` is an assignment of exactly one element of `B` to each element of `A`. We write `f(a) = b` if `b` is the unique element of `B` assigned by the function `f` to the element a of `A`. If `f` is a function from `A` to `B`, we write `f: A → B`.

* **Remark**: Functions are sometimes also called mappings or transformations.

> [!Info] Definition 2
> If `f` is a function from `A` to `B`, we say that `A` is the *domain* of `f` and `B` is the *codomain* of `f`. If `f(a) = b`, we say that `b` is the image of `a` and `a` is a *preimage* of b. The *range*, or *image*, of `f` is the set of all images of elements of `A`. Also, if `f` is a function from `A` to `B`, we say that `f` maps `A` to `B`.

* Two functions are **equal** when they have the same domain, have the same codomain, and map each element of their common domain to the same element in their common codomain.
	* Note that if we change either the domain or the codomain of a function, then we obtain a diﬀerent function.
	* If we change the mapping of elements, then we also obtain a diﬀerent function.
* A function is called **real-valued** if its codomain is the set of real numbers, and it is called **integer-valued** if its codomain is the set of integers.
	* Two real-valued functions or two integer-valued functions with the same domain can be added, as well as multiplied.

> [!Info] Definition: `function addition and multiplication`
> Let `f1` and `f2` be functions from `A` to `R`. Then `f1 + f2` and `f1.f2` are also functions from `A` to `R` deﬁned for all `x ∈ A` by
> - (f1 + f2)(x) = f1(x) + f2(x),
> - (f1.f2)(x) = f1(x).f2(x).

> [!Info] Definition: `image of a subset of the domain`
> Let `f` be a function from `A` to `B` and let `S` be a subset of `A`. The image of `S` under the function `f` is the subset of `B` that consists of the images of the elements of `S`. We denote the image of `S` by `f(S)`, so
>
> - f(S) = {t ∣ ∃s ∈ S (t = f(s))}.
>
> We also use the shorthand `{f(s) ∣ s ∈ S}` to denote this set.
>
> **Remark**: The notation `f(S)` for the image of the set `S` under the function `f` is potentially ambiguous. Here, `f(S)` denotes a set, and not the value of the function `f` for the set `S`.

> [!Error] 2.3.2 One-to-One and Onto Functions

> [!Info] Definition: `one-to-one functions`
> Some functions never assign the same value to two diﬀerent domain elements.
> A function `f` is said to be *one-to-one*, or an *injection*, if and only if `f(a) = f(b)` implies that `a = b` for all `a` and `b` in the domain of `f`. A function is said to be *injective* if it is one-to-one.

* **Remark**: We can express that `f` is one-to-one using quantiﬁers as `∀a∀b(f(a) = f(b) → a = b)` or equivalently `∀a∀b(a ≠ b → f(a) ≠ f(b))`, where the universe of discourse is the domain of the function.

> [!Info] Definition: `increasing and decreasing functions`
> A function `f` whose domain and codomain are subsets of the set of real numbers is called *increasing* if `f(x) ≤ f(y)`, and strictly increasing if `f(x) < f(y)`, whenever `x < y` and `x` and `y` are in the domain of `f`. Similarly, `f` is called decreasing if `f(x) ≥ f(y)`, and strictly decreasing if `f (x) > f(y)`, whenever `x < y` and `x` and `y` are in the domain of `f`. (The word strictly in this deﬁnition indicates a strict inequality.)
>
> - **Remark:**
> 	- increasing: ∀x∀y(x < y → f(x) ≤ f(y))
> 	- strictly increasing: ∀x∀y(x < y → f(x) < f(y))
> 	- decreasing: ∀x∀y(x < y → f(x) ≥ f(y))
> 	- strictly decreasing: ∀x∀y(x < y → f(x) > f(y))

* From these deﬁnitions, it can be shown that a function that is either strictly increasing or strictly decreasing must be one-to-one.

> [!Info] Definition: `onto functions`
> For some functions the range and the codomain are equal. That is, every member of the codomain is the image of some element of the domain. Functions with this property are called **onto** functions.
> A function `f` from `A` to `B` is called onto, or a *surjection*, if and only if for every element `b ∈ B` there is an element `a ∈ A` with `f(a) = b`. A function `f` is called subjective if it is onto.

* **Remark**: Remark: A function `f` is onto if `∀y∃x(f(x) = y)`, where the domain for `x` is the domain of the function and the domain for `y` is the codomain of the function.

> [!Info]
> Suppose that `f: A → B`.
> <span style="color: orange">To show that f is injective</span> Show that if `f(x) = f(y)` for arbitrary `x`, `y ∈ A`, then `x = y`.
> <span style="color: orange">To show that f is not injective</span> Find particular elements `x`, `y ∈ A` such that `x ≠ y` and `f(x) = f(y)`.
> <span style="color: orange">To show that f is surjective</span> Consider an arbitrary element `y ∈ B` and ﬁnd an element `x ∈ A` such that `f(x) = y`.
> <span style="color: orange">To show that f is not surjective</span> Find a particular `y ∈ B` such that `f(x) ≠ y` for all `x ∈ A`.

> [!Error] 2.3.3 Inverse Functions and Compositions of Functions

> [!Info] Definition: `inverse function`
> Let `f` be a one-to-one correspondence from the set `A` to the set `B`. The inverse function of `f` is the function that assigns to an element `b` belonging to `B` the unique element `a` in `A` such that `f(a) = b`. The inverse function of `f` is denoted by `f**−1` . Hence, `f**−1(b) = a` when `f(a) = b`.

* If a function `f` is not a one-to-one correspondence, we cannot deﬁne an inverse function of `f`. When `f` is not a one-to-one correspondence, either it is not one-to-one or it is not onto.

> [!Info] Definition: `composition of functions`
> Let `g` be a function from the set `A` to the set `B` and let `f` be a function from the set `B` to the set `C`. The *composition* of the functions `f` and `g`, denoted for all `a ∈ A` by `fog`, is the function from `A` to `C` deﬁned by `(fog)(a) = f(g(a))`.

* **Remark**: The commutative law does not hold for the composition of functions. `fog` and `gof` are not the same.

* When the composition of a function and its inverse is formed, in either order, an identity function is obtained.
	* `(f**−1of)(a) = f**−1(f(a)) = f**−1(b) = a`,
	* `(fof**−1)(b) = f(f**−1(b)) = f(a) = b`.
	* Consequently `f**−1of = tA` and `fof**−1 = tB` , where `tA` and `tB` are the identity functions on the sets `A` and `B`, respectively. That is, `(f**−1)**−1 = f` .

> [!Error] 2.3.4 The Graphs of Functions

> [!Info] Definition: `graph of function`
> Let `f` be a function from the set `A` to the set `B`. The graph of the function `f` is the set of ordered pairs `{(a, b) ∣ a ∈ A and f(a) = b}`.

> [!Error] 2.3.5 Some Important Functions

> [!Info] Definition: `floor and ceiling`
> The *ﬂoor function* assigns to the real number `x` the largest integer that is less than or equal to `x`. The value of the ﬂoor function at `x` is denoted by `⌊x⌋`.
> The ceiling function assigns to the real number `x` the smallest integer that is greater than or equal to `x`. The value of the ceiling function at `x` is denoted by `⌈x⌉`.

* The ﬂoor and ceiling functions are useful in a wide variety of applications, including those involving data storage and data transmission.
* Useful properties of the Floor and Ceiling Functions:
	* `⌊x⌋ = n` if and only if `n ≤ x < n + 1`
	* `⌈x⌉ = n` if and only if `n − 1 < x ≤ n`
	* `⌊x⌋ = n` if and only if `x − 1 < n ≤ x`
	* `⌈x⌉ = n` if and only if `x ≤ n < x + 1`
	* `x − 1 < ⌊x⌋ ≤ x ≤ ⌈x⌉ < x + 1`
	* `⌊−x⌋ = −⌈x⌉`
	* `⌈−x⌉ = −⌊x⌋`
	* `⌊x + n⌋ = ⌊x⌋ + n`
	* `⌈x + n⌉ = ⌈x⌉ + n`

> [!Error] 2.3.6 Partial Functions

* A program designed to evaluate a function may not produce the correct value of the function for all elements in the domain of this function. For example, a program may not produce a correct value because evaluating the function may lead to an inﬁnite loop or an overﬂow. Similarly, in abstract mathematics, we often want to discuss functions that are deﬁned only for a subset of the real numbers, such as `1/x`, `x`, and `arcsin(x)`. Also, we may want to use such notions as the “youngest child” function, which is undeﬁned for a couple having no children, or the “time of sunrise,” which is undeﬁned for some days above the Arctic Circle. To study such situations, we use the concept of a partial function.

> [!Info] Definition: `partial function`
> A partial function `f` from a set `A` to a set `B` is an assignment to each element `a` in a subset of `A`, called the domain of deﬁnition of `f`, of a unique element `b` in `B`. The sets `A` and `B` are called the domain and codomain of `f`, respectively. We say that `f` is undeﬁned for elements in `A` that are not in the domain of deﬁnition of `f`. When the domain of deﬁnition of `f` equals `A`, we say that `f` is a total function.

* **Remark**: We write `f : A → B` to denote that `f` is a partial function from `A` to `B`. Note that this is the same notation as is used for functions. The context in which the notation is used determines whether `f` is a partial function or a total function.
* **Example 34**: The function `f: Z → R` where `f(n) = n` is a partial function from `Z` to `R` where the domain of deﬁnition is the set of nonnegative integers. Note that `f` is undeﬁned for negative integers.

##### 2.4 Sequences and Summations
> `pg: 12`
> `time req: 1' 19"`
> `time done: 46"`
> `performance: 171%`
>
> `questions: 48`
> `practice time req: 46"`
> `pratice time done: 1"`
> `p-performance: 4600%`

> [!Error] 2.4.2 Sequences

* A sequence is a discrete structure used to represent an ordered list.

> [!Info] Definition: `sequence`
> A sequence is a function from a subset of the set of integers (usually either the set {0, 1, 2, …} or the set {1, 2, 3, …}) to a set `S`. We use the notation `an` to denote the image of the integer `n`. We call `an` a term of the sequence.

* We use the notation `{an}` to describe the sequence.
* Note that `an` represents an individual term of the sequence `{an}`.

> [!Info] Definition: `geometric progression`
> A geometric progression is a sequence of the form
>
> - a, ar, ar**2 , … , ar**n , …
>
> where the initial term a and the common ratio r are real numbers.

* **Remark**: A geometric progression is a discrete analogue of the exponential function `f(x) = ar**x` .

> [!Info] Definition: `arithmetic progression`
> An arithmetic progression is a sequence of the form
>
> - a, a + d, a + 2d, … , a + nd, …
>
> where the initial term a and the common diﬀerence d are real numbers.

* **Remark**: An arithmetic progression is a discrete analogue of the linear function `f(x) = dx + a`.

> [!Error] 2.4.3 Recurrence Relations

> [!Info] Definition: `recurrence relation`
> A *recurrence relation* for the sequence `{an}` is an equation that expresses an in terms of one or more of the previous terms of the sequence, namely, a0 , a1 , … , an−1 , for all integers n with n ≥ n0 , where n0 is a nonnegative integer. A sequence is called a *solution* of a recurrence relation if its terms satisfy the recurrence relation.

* The **initial conditions** for a recursively deﬁned sequence specify the terms that precede the ﬁrst term where the recurrence relation takes eﬀect.
* We say that we have solved the recurrence relation together with the initial conditions when we ﬁnd an explicit formula, called a **closed formula**, for the terms of the sequence.

> [!Error] 2.4.4 Special Integer Sequences

* A common problem in discrete mathematics is ﬁnding a closed formula, a recurrence relation, or some other type of general rule for constructing the terms of a sequence. Sometimes only a few terms of a sequence solving a problem are known; the goal is to identify the sequence. Even though the initial terms of a sequence do not determine the entire sequence (after all, there are inﬁnitely many diﬀerent sequences that start with any ﬁnite set of initial terms), knowing the ﬁrst few terms may help you make an educated conjecture about the identity of your sequence. Once you have made this conjecture, you can try to verify that you have the correct sequence.
* When trying to deduce a possible formula, recurrence relation, or some other type of rule for the terms of a sequence when given the initial terms, try to ﬁnd a pattern in these terms. You might also see whether you can determine how a term might have been produced from those preceding it. There are many questions you could ask, but some of the more useful are:
	* Are there runs of the same value? That is, does the same value occur many times in a row?
	* Are terms obtained from previous terms by adding the same amount or an amount that depends on the position in the sequence?
	* Are terms obtained from previous terms by multiplying by a particular amount?
	* Are terms obtained by combining previous terms in a certain way?
	* Are there cycles among the terms?

| nth Term | First 10 Terms | Some Useful Sequences |
| :- | :- | :- |
| n\*\*2 | 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, … |
| n\*\*3 | 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, … |
| n\*\*4 | 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, … |
| fibn | 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … |
| 2\*\*n | 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, … |
| 3\*\*n | 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, … |
| n! | 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, … |

> [!Error] 2.4.5 Summations

> [!Info] Theorem 1: `sum of terms of a geometric progression`
> If a and r are real numbers and r ≠ 0, then
> `sigma(j=0)(j=n)(ar**j)` =
> - if r ≠ 1 -> (ar\*\*(n+1) - a) / (r - 1)
> - if r = 1 -> (n + 1)a

| sum | closed form | useful summation formulae (page 176) |
| :- | :- | :- |
| `sigma(k=0)(n)(ar\*\*k) (r ≠ 0)` | `(ar(n + 1) - a) / (r - 1) (r ≠ 1)` |
| `sigma(k=1)(n)(k)` | `n(n+1)/2` |
| `sigma(k=1)(n)(k**2)` | `n(n+1)(2n+1)/6` |
| `sigma(k=1)(n)(k**3)` | `n**2.(n+1)**2/4` |
| `sigma(k=0)(∞)(x**k) (abs(x) < 1)` | `1/(1 - x)` |
| `sigma(k=0)(∞)(k.x**(k-1) (abs(x) < 1)` | `1/(1 - x)**2` |

##### 2.5 Cardinality of Sets
> `pg: 7`
> `time req: 46"`
> `time done: 35"`
> `performance: 131%`
>
> `questions: 41`
> `practice time req: 27"`

> [!Error] 2.5.1 Introduction

* We deﬁned the cardinality of a ﬁnite set as the number of elements in the set. We use the cardinalities of ﬁnite sets to tell us when they have the same size, or when one is bigger than the other. In this section we extend this notion to inﬁnite sets. That is, we will deﬁne what it means for two inﬁnite sets to have the same cardinality, providing us with a way to measure the relative sizes of inﬁnite sets.

> [!Info] Definition: `equality of cardinality`
> The sets `A` and `B` have the same cardinality if and only if there is a one-to-one correspondence from `A` to `B`. When `A` and `B` have the same cardinality, we write `|A| = |B|`.

* For inﬁnite sets the deﬁnition of cardinality provides a relative measure of the sizes of two sets, rather than a measure of the size of one particular set. We can also deﬁne what it means for one set to have a smaller cardinality than another set.

> [!Info] Definition: `comparison of cardinalities`
> If there is a one-to-one function from `A` to `B`, the cardinality of `A` is less than or the same as the cardinality of `B` and we write `|A| ≤ |B|`. Moreover, when `|A| ≤ |B|` and `A` and `B` have diﬀerent cardinality, we say that the cardinality of `A` is less than the cardinality of `B` and we write `|A| < |B|`.

> [!Error] 2.5.2 Countable Sets

> [!Info] Definition: `countable sets`
> A set that is either ﬁnite or has the same cardinality as the set of positive integers is called *countable*. A set that is not countable is called *uncountable*. When an inﬁnite set `S` is countable, we denote the cardinality of `S` by `ℵ0` (where `ℵ` is aleph, the ﬁrst letter of the Hebrew alphabet). We write `|S| = ℵ0` and say that `S` has cardinality “aleph null.”

> [!Warning]
> The set of positive **rational** numbers is countable.

> [!Error] 2.5.3 An Uncountable Set

> [!Warning]
> The set of positive **real** numbers is *un*countable.

> [!Info] Theorem 1
> If `A` and `B` are countable sets, then `A ∪ B` is also countable.

> [!Info] Theorem 2: `SCHRÖDER-BERNSTEIN Theorem`
> If `A` and `B` are sets with `|A| ≤ |B|` and `|B| ≤ |A|`, then `|A| = |B|`. In other words, if there are one-to-one functions `f` from `A` to `B` and `g` from `B` to `A`, then there is a one-to-one correspondence between `A` and `B`.

> [!Info] Definition: `computable functions`
> We say that a function is computable if there is a computer program in some programming language that ﬁnds the values of this function. If a function is not computable we say it is uncomputable.

##### 2.6 Matrices
> `pg: 20`
> `time req: 2' 13"`
> `time done: 32"`
> `performance: 415%`
>
> `questions: 35`
> `questions done: 6`
> `practice time req: 1' 18"`
> `practice time done: 31"`
> `p-performance: 283%`

> [!Error] 2.6.1 Introduction

> [!Info] Definition: `matrix`
> A *matrix* is a rectangular array of numbers. A matrix with `m` rows and `n` columns is called an `m × n` matrix. The plural of matrix is *matrices*. A matrix with the same number of rows as columns is called *square*. Two matrices are equal if they have the same number of rows and the same number of columns and the corresponding entries in every position are equal.

> [!Info] Definition: `matrix elements`
> Let `m` and `n` be positive integers and let
> - $$\begin{flalign}A=\begin{bmatrix}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
. & . & & .\\
. & . & & .\\
. & . & & .\\
a_{m1} & a_{m2} & ... & a_{mn}\\
\end{bmatrix}.&&\end{flalign}$$
>
> The `i`th row of `A` is the `1 × n` matrix `[ai1, ai2, …, ain]`. The `j`th column of `A` is the `m × 1` matrix.
>
> - $$\begin{flalign}\begin{bmatrix}
a_{1j}\\
a_{2j}\\
.\\
.\\
.\\
a_{mj}
\end{bmatrix}.&&\end{flalign}$$
>
> The `(i, j)`th element or entry of `A` is the element `aij` , that is, the number in the `i`th row and `j`th column of `A`. A convenient shorthand notation for expressing the matrix `A` is to write `A = [aij]`, which indicates that `A` is the matrix with its `(i, j)`th element equal to `aij`.

> [!Error] 2.6.2 The Matrix Arithmetic

> [!Info] Definition: `matrix sum`
> Let `A = [aij]` and `B = [bij]` be `m × n` matrices. The sum of `A` and `B`, denoted by `A + B`, is the `m × n` matrix that has `aij + bij` as its `(i, j)`th element. In other words, `A + B = [aij + bij]`.

* The sum of two matrices of the same size is obtained by adding elements in the corresponding positions.
* Matrices of diﬀerent sizes cannot be added, because such matrices will not both have entries in some of their positions.

> [!Info] Definition: `matrix product`
> Let `A` be an `m × k` matrix and `B` be a `k × n` matrix. The product of `A` and `B`, denoted by `AB`, is the `m × n` matrix with its `(i, j)`th entry equal to the sum of the products of the corresponding elements from the `i`th row of `A` and the `j`th column of `B`. In other words, if `AB = [cij]`, then
>
> - `cij = ai1.b1j + ai2.b2j + ⋯ + aik.bkj`.
>
> A product of two matrices is deﬁned only when the number of columns in the ﬁrst matrix equals the number of rows of the second matrix. Consequently, the product of two matrices is not deﬁned when the number of columns in the ﬁrst matrix and the number of rows in the second matrix are not the same.

* Although matrix multiplication is associative, as can easily be proved using the associativity of addition and multiplication of real numbers, matrix multiplication is *not* commutative. That is, if `A` and `B` are two matrices, it is not necessarily true that `AB` and `BA` are the same. In fact, it may be that only one of these two products is deﬁned. For instance, if `A` is `2 × 3` and `B` is `3 × 4`, then `AB` is deﬁned and is `2 × 4`; however, `BA` is not deﬁned, because it is impossible to multiply a `3 × 4` matrix and a `2 × 3` matrix.
* In general, suppose that `A` is an `m × n` matrix and `B` is an `r × s` matrix. Then `AB` is deﬁned only when `n = r` and `BA` is deﬁned only when `s = m`. Moreover, even when `AB` and `BA` are both deﬁned, they will not be the same size unless `m = n = r = s`. Hence, if both `AB` and `BA` are deﬁned and are the same size, then both `A` and `B` must be square and of the same size. Furthermore, even with `A` and `B` both `n × n` matrices, `AB` and `BA` are not necessarily equal.

> [!Error] 2.6.3 Transposes and Powers of Matrices

> [!Info] Definition: `identity matrix`
> The identity matrix of order `n` is the `n × n` matrix `In = [𝛿ij]`, (the Kronecker delta) where `𝛿ij = 1` if `i = j` and `𝛿ij = 0` if `i ≠ j`. Hence,
>
> - $$\begin{flalign}I_n=\begin{bmatrix}
1 & 0 & ... & 0\\
0 & 1 & ... & 0\\
. & . & & .\\
. & . & & .\\
. & . & & .\\
0 & 0 & ... & 1\\
\end{bmatrix}.&&\end{flalign}$$

* Multiplying a matrix by an appropriately sized identity matrix does not change this matrix. In other words, when `A` is an `m × n` matrix, we have `AIn = Im A = A`.
* Powers of square matrices can be deﬁned because matrix multiplication is associative. When `A` is an `n × n` matrix, we have
	* `A**0 = In`, `A**r = AAA ⋯ A`.

> [!Info] Definition: `matrix transposition`
> Let `A = [aij]` be an `m × n` matrix. The transpose of `A`, denoted by `At` , is the `n × m` matrix obtained by interchanging the rows and columns of `A`. In other words, if `At = [bij]`, then `bij = aji` for `i = 1, 2, … , n` and `j = 1, 2, … , m`.

> [!Info] Definition: `symmetric matrix`
> A square matrix `A` is called symmetric if `A = At` . Thus, `A = [aij]` is symmetric if `aij = aji` for all `i` and `j` with `1 ≤ i ≤ n` and `1 ≤ j ≤ n`.
> Matrices that do not change when their rows and columns are interchanged are often important.

* Note that a matrix is symmetric if and only if it is square and it is symmetric with respect to its main diagonal (which consists of entries that are in the `i`th row and `i`th column for some `i`).

> [!Error] 2.6.4 Zero-One Matrices

* A matrix all of whose entries are either 0 or 1 is called a **zero–one matrix**. Zero–one matrices are often used to represent discrete structures.
* Algorithms using these structures are based on Boolean arithmetic with zero–one matrices. This arithmetic is based on the Boolean operations `∧` and `∨`, which operate on pairs of bits.

> [!Info] Definition: `matrix join and meet`
> Let `A = [aij]` and `B = [bij]` be `m × n` zero–one matrices. Then the join of `A` and `B` is the zero–one matrix with `(i, j)`th entry `aij ∨ bij`. The join of `A` and `B` is denoted by `A ∨ B`. The meet of `A` and `B` is the zero–one matrix with `(i, j)`th entry `aij ∧ bij`. The meet of `A` and `B` is denoted by `A ∧ B`.

> [!Info] Definition: `matrix boolean product`
> Let `A = [aij]` be an `m × k` zero–one matrix and `B = [bij]` be a `k × n` zero–one matrix. Then the Boolean product of `A` and `B`, denoted by `A ⊙ B`, is the `m × n` matrix with `(i, j)`th entry `cij` where
>
> - `cij = (ai1 ∧ b1j) ∨ (ai2 ∧ b2j) ∨ ⋯ ∨ (aik ∧ bkj).`

* Note that the Boolean product of `A` and `B` is obtained in an analogous way to the ordinary product of these matrices, but with addition replaced with the operation `∨` and with multiplication replaced with the operation `∧`.

> [!Info] Definition: `boolean powers of a square zero-one matrix`
> Let `A` be a square zero–one matrix and let `r` be a positive integer. The `r`th Boolean power of `A` is the Boolean product of `r` factors of `A`. The `r`th Boolean product of `A` is denoted by `A**[r]` . Hence,
>
> - $$\begin{flalign}A^{[r]}=\underbrace{A \odot A \odot A \odot A ... \odot A}_\text{r\ times}.&&\end{flalign}$$
>
> (This is well deﬁned because the Boolean product of matrices is associative.) We also deﬁne `A**[0]` to be `In`.

#### Chapter 3: Algorithms
> [!Summary]
> `sum page: 37`
> `sum time req: 4' 5"`

> [!Question] ChatGPT
> > I'm learning discrete math from "Discrete Mathematics and Its Applications by Kenneth H. Rosen". Later on, after this book, I will study algorithms from "The Algorithms Manual by Steven Skiena". In discrete math there's a chapter called algorithms which consists of "3.1 algorithms", "3.2 the growth of functions", and "3.3 complexity of algorithms". How redundant is this chapter 3, since I'm going to study algorithms right after this?
>
> While there might be some overlap between the chapter on algorithms in your discrete mathematics book and the material you'll study in "The Algorithms Manual" by Steven Skiena, it's important to recognize that these books serve different purposes.
>
> The algorithms chapter in your discrete mathematics book likely provides a theoretical foundation for understanding algorithms, introducing concepts such as algorithmic efficiency, time complexity, and space complexity. This chapter may focus on the mathematical analysis of algorithms, helping you develop a theoretical understanding of how algorithms perform.
>
> On the other hand, "The Algorithms Manual" is likely to be more practical and hands-on. It may delve into specific algorithms, their implementations, and real-world applications. This book is likely to provide a more concrete and applied perspective on algorithm design and analysis.
> 
> In summary, while there might be some redundancy in terms of basic concepts, the two chapters are likely to have different emphases. The discrete mathematics chapter may provide a theoretical foundation, while the algorithms book may offer practical insights and implementations. Both perspectives are valuable and can complement each other, providing you with a well-rounded understanding of algorithms.

##### 3.1 Algorithms
> `pg: 13`
> `time req: 1' 26"`
> `time done: 39"`
> `performance: 220%`
>
> `questions: 72`
> `practice time req: 50"`
> `practice time done: 10"`
> `p-performance: 500%`

> [!Error] 3.1.1 Introduction

* Setting up the appropriate mathematical model is only part of the solution. To complete the solution, a method is needed that will solve the general problem using the model. Ideally, what is required is a procedure that follows a sequence of steps that leads to the desired answer. Such a sequence of steps is called an **algorithm**.

> [!Info] Definition: `algorithm`
> An *algorithm* is a ﬁnite sequence of precise instructions for performing a computation or for solving a problem.

* **Pseudocode** provides an intermediate step between an English language description of an algorithm and an implementation of this algorithm in a programming language.
* **Properties of Algorithms**
	* **Input**: An algorithm has input values from a speciﬁed set.
	* **Output**: From each set of input values an algorithm produces output values from a speciﬁed set. The output values are the solution to the problem.
	* **Definiteness**: The steps of an algorithm must be deﬁned precisely.
	* **Correctness**: An algorithm should produce the correct output values for each set of input values.
	* **Finiteness**: An algorithm should produce the desired output after a ﬁnite (but perhaps large) number of steps for any input in the set.
	* **Effectiveness**: It must be possible to perform each step of an algorithm exactly and in a ﬁnite amount of time.
	* **Generality**: The procedure should be applicable for all problems of the desired form, not just for a particular set of input values.

##### 3.2 The Growth of Functions
> `pg: 13`
> `time req: 1' 26"`
> `time done: 1' 22"`
> `performance: 104%`
>
> `questions: 77`
> `practice time req: 50"`

> [!Error] 3.2.1 Introduction

* One of the advantages of using big-O notation, which we introduce in this section, is that we can estimate the growth of a function without worrying about constant multipliers or smaller order terms. This means that, using big-O notation, we do not have to worry about the hardware and software used to implement an algorithm. Furthermore, using big-O notation, we can assume that the diﬀerent operations used in an algorithm take the same time, which simpliﬁes the analysis considerably.

> [!Error] 3.2.2 Big-O Notation

> [!Info] Definition: `big-o`
> Let `f` and `g` be functions from the set of integers or the set of real numbers to the set of real numbers. We say that `f(x)` is `O(g(x))` if there are constants `C` and `k` such that
>
> - |f(x)| ≤ C|g(x)|
>
> whenever `x > k`. \[This is read as “`f(x)` is big-oh of `g(x)`.”\]
> **Remark**: Intuitively, the deﬁnition that `f(x)` is `O(g(x))` says that `f(x)` grows slower than some ﬁxed multiple of `g(x)` as `x` grows without bound.

* The constants `C` and `k` in the deﬁnition of big-O notation are called witnesses to the relationship `f(x)` is `O(g(x))`. To establish that `f(x)` is `O(g(x))` we need only one pair of witnesses to this relationship. That is, to show that `f(x)` is `O(g(x))`, we need ﬁnd only one pair of constants `C` and `k`, the witnesses, such that `|f(x)| ≤ C|g(x)|` whenever `x > k`.
* Note that when there is one pair of witnesses to the relationship `f(x)` is `O(g(x))`, there are inﬁnitely many pairs of witnesses. To see this, note that if `C` and `k` are one pair of witnesses, then any pair `C′` and `k′` , where `C < C′` and `k < k′`, is also a pair of witnesses, because `|f(x)| ≤ C|g(x)| ≤ C′|g(x)|` whenever `x > k′ > k`.
* **Remark**: The fact that `f(x)` is `O(g(x))` is sometimes written `f(x) = O(g(x))`. However, the equals sign in this notation does not represent a genuine equality. Rather, this notation tells us that an inequality holds relating the values of the functions `f` and `g` for suﬃciently large numbers in the domains of these functions. However, it is acceptable to write `f(x) ∈ O(g(x))` because `O(g(x))` represents the set of functions that are `O(g(x))`.
* Note that if
	* `|f(x)| ≤ C|g(x)|` if `x > k`,
	* and if `|h(x)| > |g(x)|` for all `x > k`, then
	* `|f(x)| ≤ C|h(x)|` if `x > k`.
	* Hence, `f(x)` is `O(h(x))`.

> [!Error] 3.2.3 Big-O estimates for some important functions

* Polynomials can often be used to estimate the growth of functions. Instead of analyzing the growth of polynomials each time they occur, we would like a result that can always be used to estimate the growth of a polynomial. Theorem 1 does this. It shows that the leading term of a polynomial dominates its growth by asserting that a polynomial of degree `n` or less is `O(xn)`.

> [!Theorem 1]
> Let $f(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1x + a_0$, where $a_0, a_1, ..., a_{n-1}, a_n$ are real numbers. Then $f(x)$ is $O(x^n)$.

---
* Common functions sorted by growth rate:
	* $1,\ \log n,\ n,\ n\log n,\ n^2,\ 2^n,\ n!$
* If `d > c > 1`, then
	* $n^c\ \text{is}\ O(n^d),\ \text{but}\ n^d\ \text{is not}\ O(n^c).$
* Whenever `b > 1` and `c` and `d` are positive, we have
	* $(\log_b n)^c\ \text{is}\ O(n^d),\ \text{but}\ n^d\ \text{is not}\ (O(\log_b n)^c).$
* Whenever `d` is positive and `b > 1`, we have
	* $n^d\ \text{is}\ O(b^n),\ but\ b^n\ \text{is not}\ O(n^d).$
* When `c > b > 1` we have
	* $b^n\ \text{is}\ O(c^n),\ \text{but}\ c^n\ \text{is not}\ O(b^n).$
* If `c > 1`, we have
	* $c^n\ \text{is}\ O(n!),\ \text{but}\ n!\ \text{is not}\ O(c^n).$

> [!Error] 3.2.4 The Growth of Combinations of Functions

> [!Info] Theorem 2
> Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1 + f_2)(x)$ is $O(g(x))$, where $g(x) = (max(|g_1(x)|, |g_2(x)|)$ for all $x$.

> [!Info] Theorem 3
> Suppose that $f_1(x)$ is $O(g_1(x))$ and that $f_2(x)$ is $O(g_2(x))$. Then $(f_1f_2)(x)$ is $O(g_1(x)g_2(x))$.

> [!Error] 3.2.5 Big-Omega and Big-Theta Notations

* Big-O notation is used extensively to describe the growth of functions, but it has limitations. In particular, when `f(x)` is `O(g(x))`, we have an upper bound, in terms of `g(x)`, for the size of `f(x)` for large values of `x`. However, big-O notation does not provide a lower bound for the size of `f(x)` for large `x`. For this, we use big-Omega (big-Ω) notation. When we want to give both an upper and a lower bound on the size of a function `f(x)`, relative to a reference function `g(x)`, we use big-Theta (big-Θ) notation.

> [!Info] Definition: `big-Ω`
> Let `f` and `g` be functions from the set of integers or the set of real numbers to the set of real numbers. We say that `f(x)` is `Ω(g(x))` if there are constants `C` and `k` with `C` positive such that
>
> - |f(x)| ≥ C|g(x)|
>
> whenever `x > k`. \[This is read as “`f(x)` is big-Omega of `g(x)`.”\]
> There is a strong connection between big-O and big-Omega notation. In particular, `f(x)` is `Ω(g(x))` if and only if `g(x)` is `O(f(x))`.

* Often, it is important to know the order of growth of a function in terms of some relatively simple reference function such as `x**n` when `n` is a positive integer or `c**x` , where `c > 1`. Knowing the order of growth requires that we have both an upper bound and a lower bound for the size of the function. That is, given a function `f(x)`, we want a reference function `g(x)` such that `f(x)` is `O(g(x))` and `f(x)` is `Ω(g(x))`. Big-Theta notation, deﬁned as follows, is used to express both of these relationships, providing both an upper and a lower bound on the size of a function.

> [!Info] Definition: `big-Θ`
> Let `f` and `g` be functions from the set of integers or the set of real numbers to the set of real numbers. We say that `f(x)` is `Θ(g(x))` if `f(x)` is `O(g(x))` and `f(x)` is `Ω(g(x))`. When `f(x)` is `Θ(g(x))`, we say that `f` is big-Theta of `g(x)`, that `f(x)` is of order `g(x)`, and that `f(x)` and `g(x)` are of the same order.

* When `f(x)` is `Θ(g(x))`, it is also the case that `g(x)` is `Θ(f(x))`. Also note that `f(x)` is `Θ(g(x))` if and only if `f(x)` is `O(g(x))` and `g(x)` is `O(f(x))`. Furthermore, note that `f(x)` is `Θ(g(x))` if and only if there are positive real numbers `C1` and `C2` and a positive real number `k` such that
	* C1|g(x)| ≤ |f(x)| ≤ C2|g(x)|
	* whenever `x > k`. The existence of the constants `C1`, `C2`, and `k` tells us that `f(x)` is `Ω(g(x))` and that `f(x)` is `O(g(x))`, respectively.

> [!Info] Theorem 4
> Let $f(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0$, where $a_0, a_1, ... a_{n-1}, a_n$ are real numbers with $a_n \ne 0$. Then $f(x)$ is of order $x^n$.

##### 3.3 Complexity of Algorithms
> `pg: 11`
> `time req: 1' 13"`
> `time done: 1' 15"`
> `performance: 97%`
>
> `questions: 49`
> `practice time req: 42"`

> [!Error] 3.3.1 Introduction

* How can the eﬃciency of an algorithm be analyzed? One measure of eﬃciency is the time used by a computer to solve a problem using the algorithm, when input values are of a speciﬁed size. A second measure is the amount of computer memory required to implement the algorithm when input values are of a speciﬁed size.
* Questions such as these involve the **computational complexity** of the algorithm. An analysis of the time required to solve a problem of a particular size involves the **time complexity** of the algorithm. An analysis of the computer memory required involves the **space complexity** of the algorithm. Considerations of the time and space complexity of an algorithm are essential when algorithms are implemented. It is important to know whether an algorithm will produce an answer in a microsecond, a minute, or a billion years. Likewise, the required memory must be available to solve a problem, so that space complexity must be taken into account.

> [!Error] 3.3.2 Time Complexity

* **Worst-Case Complexity**: By the worst-case performance of an algorithm, we mean the largest number of operations needed to solve the given problem using this algorithm on input of speciﬁed size. Worst-case analysis tells us how many operations an algorithm requires to guarantee that it will produce a solution.
* **Average-Case Complexity**: Another important type of complexity analysis, besides worst-case analysis, is called average-case analysis. The average number of operations used to solve the problem over all possible inputs of a given size is found in this type of analysis. Average-case time complexity analysis is usually much more complicated than worst-case analysis.

> [!Error] 3.3.4 Algorithmic Paradigms

* Greedy algorithms provide an example of an **algorithmic paradigm**, that is, a general approach based on a particular concept that can be used to construct algorithms for solving a variety of problems.
* Algorithmic paradigms can serve as the basis for constructing eﬃcient algorithms for solving a wide range of problems.
* The most common algorithmic paradigms are: *Brute Force*, *Divide-and-Conquer*, *Dynamic Programming*, *Backtracking*, and *Probabilistic Algorithms*.
---
* **Brute Force Algorithms**
* In a brute-force algorithm, a problem is solved in the most straightforward manner based on the statement of the problem and the deﬁnitions of terms.
* Brute-force algorithms are designed to solve problems without regard to the computing resources required. For example, in some brute-force algorithms the solution to a problem is found by examining every possible solution, looking for the best possible.
* In general, brute-force algorithms are naive approaches for solving problems that do not take advantage of any special structure of the problem or clever ideas.
* Although brute-force algorithms are often ineﬃcient, they are often quite useful. A brute-force algorithm may be able to solve practical instances of problems, particularly when the input is not too large, even if it is impractical to use this algorithm for larger inputs.
* Furthermore, when designing new algorithms to solve a problem, the goal is often to ﬁnd a new algorithm that is more eﬃcient than a brute-force algorithm.

> [!Error] 3.3.5 Understanding the Complexity of Algorithms

| Complexity | Terminology |
| :- | :- |
| Θ(1) | constant |
| Θ(log n) | logarithmic |
| Θ(n) | linear |
| Θ(n log n) | linearithmic |
| Θ(n\*\*b) | polynomial |
| Θ(b\*\*n), where b > 1 | exponential |
| Θ(n!) | factorial |

---
* **Tractability**: A problem that is solvable using an algorithm with polynomial (or better) worst-case complexity is called **tractable**, because the expectation is that the algorithm will produce the solution to the problem for reasonably sized input in a relatively short time. However, if the polynomial in the big-Θ estimate has high degree (such as degree 100) or if the coeﬃcients are extremely large, the algorithm may take an extremely long time to solve the problem. Consequently, that a problem can be solved using an algorithm with polynomial worst-case time complexity is no guarantee that the problem can be solved in a reasonable amount of time for even relatively small input values. Fortunately, in practice, the degree and coeﬃcients of polynomials in such estimates are often small.
* **Intractability**: The situation is much worse for problems that cannot be solved using an algorithm with worst-case polynomial time complexity. Such problems are called **intractable**. Usually, but not always, an extremely large amount of time is required to solve the problem for the worst cases of even small input values. In practice, however, there are situations where an algorithm with a certain worst-case time complexity may be able to solve a problem much more quickly for most cases than for its worst case. When we are willing to allow that some, perhaps small, number of cases may not be solved in a reasonable amount of time, the average-case time complexity is a better measure of how long an algorithm takes to solve a problem. Many problems important in industry are thought to be intractable but can be practically solved for essentially all sets of input that arise in daily life. Another way that intractable problems are handled when they arise in practical applications is that instead of looking for exact solutions of a problem, approximate solutions are sought. It may be the case that fast algorithms exist for ﬁnding such approximate solutions, perhaps even with a guarantee that they do not diﬀer by very much from an exact solution.
* **Unsolvability**: Some problems even exist for which it can be shown that no algorithm exists for solving them. Such problems are called unsolvable (as opposed to solvable problems that can be solved using an algorithm).
---
* **P versus NP**
* The study of the complexity of algorithms goes far beyond what we can describe here. Note, however, that many solvable problems are believed to have the property that no algorithm with polynomial worst-case time complexity solves them, but that a solution, if known, can be checked in polynomial time. Problems for which a solution can be checked in polynomial time are said to belong to the **class NP** (tractable problems are said to belong to **class P**). The abbreviation NP stands for *nondeterministic polynomial* time.

> [!Question] ChatGPT
> > I don't understand this explanation. Explain it further and clearer.
>
> - **P** (polynomial time): An algorithm belongs to the class P if there exists a polynomial function that bounds the worst-case running time of the algorithm. In simple terms, P problems are efficiently solvable.
> - **NP** (non-deterministic polynomial time)
> 	- A problem is in the class NP if a given solution can be verified quickly (in polynomial time) by a deterministic algorithm. However, NP doesn't necessarily mean that the problem is efficiently solvable in terms of finding the solution.
> 	- **Existence of Polynomial-Time Verification**: For problems in NP, if someone claims to have a solution, we can verify the correctness of that solution relatively quickly. Imagine a problem where finding the solution might be difficult, but once you have a potential solution, you can check if it's correct efficiently.
> 	- **No Known Polynomial-Time Solution**: Importantly, for many problems in NP, we do not know if a polynomial-time algorithm exists to find the solution. This is an open question for various problems.

* There is also an important class of problems, called NP-complete problems, with the property that if any of these problems can be solved by a polynomial worst-case time algorithm, then all problems in the class NP can be solved by polynomial worst-case time algorithms.
* The P versus NP problem asks whether NP, the class of problems for which it is possible to check solutions in polynomial time, equals P, the class of tractable problems. If P ≠ NP, there would be some problems that cannot be solved in polynomial time, but whose solutions could be veriﬁed in polynomial time. The concept of NP-completeness is helpful in research aimed at solving the P versus NP problem, because NP-complete problems are the problems in NP considered most likely not to be in P, as every problem in NP can be reduced to an NP-complete problem in polynomial time. A large majority of theoretical computer scientists believe that P ≠ NP, which would mean that no NP-complete problem can be solved in polynomial time. One reason for this belief is that despite extensive research, no one has succeeded in showing that P = NP. In particular, no one has been able to ﬁnd an algorithm with worst-case polynomial time complexity that solves any NP-complete problem. The P versus NP problem is one of the most famous unsolved problems in the mathematical sciences (which include  theoretical computer science). It is one of the seven famous Millennium Prize Problems, of which six remain unsolved. A prize of $1,000,000 is oﬀered by the Clay Mathematics Institute for its solution.
---
* **Practical Considerations**
* Note that a `big-Θ` estimate of the time complexity of an algorithm expresses how the time required to solve the problem increases as the input grows in size. In practice, the best estimate (that is, with the smallest reference function) that can be shown is used. However, `big-Θ` estimates of time complexity cannot be directly translated into the actual amount of computer time used. One reason is that a `big-Θ` estimate `f(n)` is `Θ(g(n))`, where `f(n)` is the time complexity of an algorithm and `g(n)` is a reference function, means that `C1g(n) ≤ f(n) ≤ C2g(n)` when `n > k`, where `C1`, `C2`, and `k` are constants. So without knowing these constants in the inequality, this estimate cannot be used to determine a lower bound and an upper bound on the number of operations used in the worst case. As remarked before, the time required for an operation depends on the type of operation and the computer being used. Often, instead of a `big-Θ` estimate on the worst-case time complexity of an algorithm, we have only a `big-O` estimate. Note that a `big-O` estimate on the time complexity of an algorithm provides an upper, but not a lower, bound on the worst-case time required for the algorithm as a function of the input size. Nevertheless, for simplicity, we will often use `big-O` estimates when describing the time complexity of algorithms, with the understanding that `big-Θ` estimates would provide more information.

> [!Info]
> ![[Computer Science/discrete-math-images/3.3-algorithm-times.png]]
> - This displays the time needed to solve problems of various sizes with an algorithm using the indicated number `n` of bit operations, assuming that each bit operation takes `10**−11` seconds, a reasonable estimate of the time required for a bit operation using the fastest computers available in 2018.
> - Times of more than `10**100` years are indicated with an asterisk. In the future, these times will decrease as faster computers are developed.
> - We can use the times here to see whether it is reasonable to expect a solution to a problem of a speciﬁed size using an algorithm with known worst-case time complexity when we run this algorithm on a modern computer.

#### Chapter 4: Number Theory and Cryptography
> [!Summary]
> `sum page: 64`
> `sum time req: 7' 2"`

* The part of mathematics devoted to the study of the set of integers and their properties is known as number theory.

##### 4.1 Divisibility and Modular Arithmetic
> `pg: 8`
> `time req: 53"`
> `time done: 1'`
> `performance: 88%`
>
> `questions: 53`
> `practice time req: 31"`

> [!Error] 4.1.2 Division

> [!Info] Definition: `devision`
> If $a$ and $b$ are integers with $a \ne 0$, we say that $a$ divides $b$ if there is an integer $c$ such that $b = ac$ (or equivalently, if $\dfrac{b}{a}$ is an integer). When $a$ divides $b$ we say that $a$ is a factor or divisor of $b$, and that $b$ is a multiple of $a$. The notation $a ∣ b$ denotes that $a$ divides $b$. We write $a ̸ | b$ when $a$ does not divide $b$.
>
> **Remark**: We can express $a ∣ b$ using quantiﬁers as $\exists c(ac = b)$, where the universe of discourse is the set of integers.

> [!Info] Theorem 1
> Let $a$, $b$, and $c$ be integers, where $a \ne 0$. Then
> 1. if $a ∣ b$ and $a ∣ c$, then $a ∣ (b + c)$;
> 2. if $a ∣ b$, then $a ∣ bc$ for all integers $c$;
> 3. if $a ∣ b$ and $b ∣ c$, then $a ∣ c$.
>
> > [!Info] Corollary 1
> > If $a$, $b$, and $c$ are integers, where $a \ne 0$, such that $a ∣ b$ and $a ∣ c$, then $a ∣ mb + nc$ whenever $m$ and $n$ are integers.

> [!Error] 4.1.3 The Division Algorithm

> [!Info] Theorem 2: `The Division Algorithm`
> Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 \le r \lt d$, such that $a = dq + r$.

> [!Info] Definition
> In the equality given in the division algorithm, $d$ is called the divisor, $a$ is called the dividend, $q$ is called the quotient, and $r$ is called the remainder. This notation is used to express the quotient and remainder:
> - $q = a \ div\ d$, $r = a\ mod\ d$.

> [!Error] 4.1.4 Modular Arithmetic

* Because we are often interested only in remainders, we have special notations for them. We have already introduced the notation $a\ mod\ m$ to represent the remainder when an integer `a` is divided by the positive integer `m`. We now introduce a diﬀerent, but related, notation that indicates that two integers have the same remainder when they are divided by the positive integer `m`.

> [!Info] Definition: `congruence`
> If `a` and `b` are integers and `m` is a positive integer, then `a` is $congruent\ to\ b\ modulo\ m$ if `m` divides `a − b`. We use the notation $a ≡ b$ (`mod m`) to indicate that `a` is congruent to `b` modulo `m`. We say that $a ≡ b$ (`mod m`) is a **congruence** and that `m` is its **modulus** (plural **moduli**). If `a` and `b` are not congruent modulo `m`, we write $a ≢ b$ (`mod m`).

> [!Info] Theorem 3
> Let `a` and `b` be integers, and let `m` be a positive integer. Then `a ≡ b (mod m)` if and only if `a mod m = b mod m`.

> [!Info] Theorem 4
> Let `m` be a positive integer. The integers `a` and `b` are congruent modulo `m` if and only if there is an integer `k` such that `a = b + km`.

> [!Info] Theorem 5
> Let `m` be a positive integer. If `a ≡ b (mod m)` and `c ≡ d (mod m)`, then
> - `a + c ≡ b + d (mod m)`
> - and `ac ≡ bd (mod m).`

> [!Info] Corollary 2
> Let `m` be a positive integer and let `a` and `b` be integers. Then
> - `(a + b) mod m = ((a mod m) + (b mod m)) mod m`
> - `ab mod m = ((a mod m)(b mod m)) mod m`.

> [!Error] 4.1.5 Arithmetic Modulo m

* We can deﬁne arithmetic operations on $Z_{m}$ , the set of nonnegative integers less than `m`, that is, the set `{0, 1, … , m − 1}`. In particular, we deﬁne addition of these integers, denoted by $+_{m}$ by
	* $a\ +_{m}\ b = (a + b)\ mod\ m$,
	* where the addition on the right-hand side of this equation is the ordinary addition of integers, and we deﬁne multiplication of these integers, denoted by $⋅_{m}$ by
	* $a\ ⋅_{m}\ b = (a ⋅ b)\ mod\ m$,
	* where the multiplication on the right-hand side of this equation is the ordinary multiplication of integers. The operations $+_{m}$ and $⋅_{m}$ are called addition and multiplication modulo `m` and when we use these operations, we are said to be doing *arithmetic modulo m*.
* The operations $+_{m}$ and $⋅_{m}$ satisfy many of the same properties of ordinary addition and multiplication of integers. In particular, they satisfy these properties:
	* **Closure**: If `a` and `b` belong to $Z_{m}$ , then $a +_{m} b$ and $a ⋅+{m} b$ belong to $Z_{m}$.
	* **Associativity**: If `a`, `b`, and `c` belong to $Z_{m}$, then $(a +_{m} b) +_{m} c = a +_{m} (b +_{m} c)$ and $(a ⋅_{m} b) ⋅_{m} c = a ⋅_{m} (b ⋅_{m} c)$.
	* **Commutativity**: If `a` and `b` belong to $Z_{m}$ , then $a +_{m} b = b +_{m} a$ and $a ⋅_{m} b = b ⋅_{m} a$.
	* **Identity elements**: The elements `0` and `1` are identity elements for addition and multiplication modulo `m`, respectively. That is, if `a` belongs to $Z_{m}$ , then $a +_{m} 0 = 0 +_{m} a = a$ and $a ⋅_{m} 1 = 1 ⋅_{m} a = a$.
	* **Additive inverses**: If `a ≠ 0` belongs to $Z_{m}$ , then `m − a` is an additive inverse of a modulo `m` and `0` is its own additive inverse. That is, $a +_{m} (m − a) = 0$ and $0 +_{m} 0 = 0$.
	* **Distributivity**: If `a`, `b`, and `c` belong to $Z_{m}$ , then $a ⋅_{m} (b +_{m} c) = (a ⋅_{m} b) +m (a ⋅_{m} c)$ and $(a +_{m} b) ⋅_{m} c = (a ⋅_{m} c) +_{m} (b ⋅_{m} c)$.

##### 4.2 Integer Representations and Algorithms
> `pg: 9`
> `time req: 59"`
> `time done: 50"`
> `performance: 118%`
>
> `questions: 65`
> `practice time req: 35"`

> [!Error] 4.2.2 Representations of Integers

> [!Info] Definition: `base`
> Let `b` be an integer greater than `1`. Then if `n` is a positive integer, it can be expressed uniquely in the form
>
> - $n = a_k b_k + a_{k−1} b_{k−1} + ⋯ + a_1 b + a_0$,
>
> where `k` is a nonnegative integer, $a_0$, $a_1$, …, $a_k$ are nonnegative integers less than `b`, and $a_k \ne 0$.
> The representation of `n` given here is called the base `b` expansion of `n`.

* Each hexadecimal digit can be represented using four bits. For instance, we see that $(1110 0101)_2 = (E5)_{16}$ because $(1110)_2 = (E)_16$ and $(0101)_2 = (5)_{16}$. Bytes, which are bit strings of length eight, can be represented by two hexadecimal digits.
---
* **Base Conversion**
* We will now describe an algorithm for constructing the base `b` expansion of an integer `n`. First, divide `n` by `b` to obtain a quotient and remainder, that is,
	* $n = bq_0 + a_0$, $0 \le a_0 \lt b$.
* The remainder, $a_0$ , is the rightmost digit in the base `b` expansion of `n`. Next, divide $q_0$ by `b` to obtain
	* $q_0 = bq_1 + a_1$, $0 \le a_1 \lt b$.
* We see that $a_1$ is the second digit from the right in the base `b` expansion of `n`. Continue this process, successively dividing the quotients by `b`, obtaining additional base `b` digits as the remainders. This process terminates when we obtain a quotient equal to zero. It produces the base `b` digits of `n` from the right to the left.

> [!Error] 4.2.3 Modular Exponentiation

* In cryptography it is important to be able to ﬁnd $b^n\ mod\ m$ eﬃciently without using an excessive amount of memory, where `b`, `n`, and `m` are large integers. It is impractical to ﬁrst compute $b^n$ and then ﬁnd its remainder when divided by `m`, because $b^n$ can be a huge number and we will need a huge amount of computer memory to store such numbers. Instead, we can avoid time and memory problems by using an algorithm that employs the binary expansion of the exponent `n`.
* Before we present an algorithm for fast modular exponentiation based on the binary expansion of the exponent, ﬁrst observe that we can avoid using large amount of memory if we compute $b^n\ mod\ m$ by successively computing $b^k\ mod\ m$ for `k = 1, 2, … , n` using the fact that $b_{k+1}\ \textbf{mod}\ m = b(b_k\ \textbf{mod}\ m)\ \textbf{mod}\ m$ (by Corollary 2 of Theorem 5 of Section 4.1). (Recall that `1 ≤ b < m`.) However, this approach is impractical because it requires `n − 1` multiplications of integers and `n` might be huge.
* To motivate the fast modular exponentiation algorithm, we illustrate its basic idea. We will explain how to use the binary expansion of `n`, say $n = (a_{k−1} … a_1 a_0)_2$ , to compute $b_n$ . First, note that
	* $b_n = b^{a_{k−1} ⋅ 2^{k−1} + ⋯ + a_1 ⋅ 2 + a_0} = b^{a_{k−1} ⋅ 2^{k−1}} ⋯ b^{a_1 ⋅ 2} ⋅ b^{a_0}$.
* This shows that to compute $b^n$, we need only compute the values of $b$, $b^2$, $(b^2)^2 = b^4$, $(b^4)^2 = b^8$, …, $b^{2^k}$ . Once we have these values, we multiply the terms $b^2$ in this list, where $a_j = 1$. (For eﬃciency and to reduce space requirements, after multiplying by each term, we reduce the result modulo `m`.)
* This gives us $b^n$.
* For example, to compute $3^{11}$ we ﬁrst note that $11 = (1011)_2$ , so that $3^{11} = 3^8 3^2 3^1$. By successively squaring, we ﬁnd that $3^2 = 9$, $3^4 = 9^2 = 81$, and $3^8 = (81)^2 = 6561$. Consequently, $3^{11} = 3^8 3^2 3^1 = 6561 ⋅ 9 ⋅ 3 = 177,147$.
---
* The algorithm successively ﬁnds $b\ mod\ m$, $b^2\ mod\ m$, $b^4\ mod\ m$, …, $b^2\ mod\ m$ and multiplies together those terms $b^{2^j}\ mod\ m$ where $a_j = 1$, ﬁnding the remainder of the product when divided by `m` after each multiplication. Note that we need only perform $O(log_{2}(n))$ multiplications.
![[Computer Science/discrete-math-images/4.2-algorithm-5.png]]

> [!Error] Important Warning
> Please refer to page 268 of the book and read the algorithm and its example.
> > [!Info] Minor Explanation
> > The algorithm is basically doing the same thing as calculating the power $b^n$ and then taking a modulo, but with a different approach.
> > By using the binary representation of $n$, the algorithm iterates through each step of calculating the power, but this time, per each step, the algorithm takes the modulo of the result $x$ and the $power$ variable, so that no number becomes too large. This way it prevents overflow and overt computational complexity by some mathematical trick based on binary representations and the nature of modular exponentiation.

##### 4.3 Primes and Greatest Common Divisors
> `pg: 18`
> `time req: 1' 59"`
> `time done: 1' 42"`
> `performance: 116%`
>
> `questions: 57`
> `questions done: 11`
> `practice time req: 1' 10"`

> [!Error] 4.3.2 Primes

* A prime is an integer greater than `1` that is divisible by no positive integers other than `1` and itself.
* Every integer greater than 1 is divisible by at least two integers, because a positive integer is divisible by 1 and by itself. Positive integers that have exactly two diﬀerent positive integer factors are called **primes**.

> [!Info] Definition: `prime numbers`
> An *integer* `p` greater than `1` is called *prime* if the only positive factors of `p` are `1` and `p`. A positive integer that is greater than `1` and is not prime is called *composite*.
>
> **Remark**: The integer `1` is not prime, because it has only one positive factor. Note also that an integer `n` is composite if and only if there exists an integer `a` such that `a ∣ n` and `1 < a < n`.

> [!Info] Theorem 1: `the fundamental theorem of arithmetic`
> Every integer greater than `1` can be written uniquely as a prime or as the product of two or more primes, where the prime factors are written in order of nondecreasing size.

> [!Error] 4.3.3 Trial Division

* One procedure for showing that an integer is prime is based on the following observation.

> [!Info] Theorem 2
> If `n` is a composite integer, then `n` has a prime divisor less than or equal to $\sqrt{n}$.

* From Theorem 2, it follows that an integer is prime if it is not divisible by any prime less than or equal to its square root. This leads to the brute-force algorithm known as **trial division**. To use trial division we divide `n` by all primes not exceeding $\sqrt{n}$ and conclude that `n` is prime if it is not divisible by any of these primes.
* Because every integer has a prime factorization, it would be useful to have a procedure for ﬁnding this prime factorization. Consider the problem of ﬁnding the prime factorization of `n`. Begin by dividing `n` by successive primes, starting with the smallest prime, `2`. If `n` has a prime factor, then by Theorem 3 a prime factor `p` not exceeding $\sqrt{n}$ will be found. So, if no prime factor not exceeding $\sqrt{n}$ is found, then `n` is prime. Otherwise, if a prime factor `p` is found, continue by factoring $n/p$. Note that $n/p$ has no prime factors less than `p`. Again, if $n/p$ has no prime factor greater than or equal to `p` and not exceeding its square root, then it is prime. Otherwise, if it has a prime factor `q`, continue by factoring $n/(pq)$. This procedure is continued until the factorization has been reduced to a prime.

> [!Error] 4.3.6 Greatest Common Divisors and Least Common Multiples

* The largest integer that divides both of two integers is called the **greatest common divisor** of these integers.

> [!Info] Definition: `gcd`
> Let `a` and `b` be integers, not both zero. The largest integer `d` such that `d ∣ a` and `d ∣ b` is called the greatest common divisor of `a` and `b`. The greatest common divisor of `a` and `b` is denoted by `gcd(a, b)`.

* One simple yet brute-force way to ﬁnd the greatest common divisor of two integers is to ﬁnd all the positive common divisors of both integers and then take the largest divisor.

> [!Info] Definition: `relative prime`
> The integers `a` and `b` are *relatively prime* if their greatest common divisor is `1`.
> We have this definition, because it is often important to specify that two integers have no common positive divisor other than 1.

> [!Info] Definition: `pairwise relative prime`
> The integers $a_1, a_2, …, a_n$ are *pairwise relatively prime* if $gcd(a_i, a_j) = 1$ whenever $1 \le i < j \le n$.
> We make this definition, because we often need to specify that no two integers in a set of integers have a common positive divisor greater than 1.

---
* Another way to ﬁnd the greatest common divisor of two positive integers is to use the prime factorizations of these integers. Suppose that the prime factorizations of the positive integers $a$ and $b$ are
	* $a = p_1^{a_1} p_2^{a_2} ... p_n^{a_n}$,
	* $b = p_1^{b_1} p_2^{b_2} ... p_n^{b_n}$,
* where each exponent is a nonnegative integer, and where all primes occurring in the prime factorization of either $a$ or $b$ are included in both factorizations, with zero exponents if necessary. Then $gcd(a, b)$ is given by
	* $gcd(a, b) = p_1^{min(a_1, b_1)} p_2^{min(a_2, b_2)} ... p_n^{min(a_n, b_n)}$,
* where $min(x, y)$ represents the minimum of the two numbers $x$ and $y$. To show that this formula for $gcd(a, b)$ is valid, we must show that the integer on the right-hand side divides both $a$ and $b$, and that no larger integer also does. This integer does divide both $a$ and $b$, because the power of each prime in the factorization does not exceed the power of this prime in either the factorization of $a$ or that of $b$. Further, no larger integer can divide both $a$ and $b$, because the exponents of the primes in this factorization cannot be increased, and no other primes can be included.
---
* Prime factorizations can also be used to ﬁnd the **least common multiple** of two integers.

> [!Info] Definition: `lcm`
> The *least common multiple* of the positive integers `a` and `b` is the smallest positive integer that is divisible by both `a` and `b`. The least common multiple of `a` and `b` is denoted by `lcm(a, b)`.

* The least common multiple exists because the set of integers divisible by both $a$ and $b$ is nonempty (because $ab$ belongs to this set, for instance), and every nonempty set of positive integers has a least element. Suppose that the prime factorizations of $a$ and $b$ are as before. Then the least common multiple of $a$ and $b$ is given by
	* $lcm(a, b) = p_1^{max(a_1, b_1)} p_2^{max(a_2, b_2)} ... p_n^{max(a_n, b_n)}$,
* where $max(x, y)$ denotes the maximum of the two numbers $x$ and $y$. This formula is valid because a common multiple of $a$ and $b$ has at least $max(a_i, b_i)$ factors of $p_i$ in its prime factorization, and the least common multiple has no other prime factors besides those in $a$ and $b$.
---
* Theorem 5 gives the relationship between the greatest common divisor and least common multiple of two integers.

> [!Info] Theorem 5
> Let `a` and `b` be positive integers. Then
>
> - `ab = gcd(a, b) ⋅ lcm(a, b)`.

> [!Error] 4.3.7 The Euclidean Algorithm

* Computing the greatest common divisor of two integers directly from the prime factorizations of these integers is **ineﬃcient**. The reason is that it is time-consuming to ﬁnd prime factorizations. We will give a more eﬃcient method of ﬁnding the greatest common divisor, called the **Euclidean algorithm**.
* We will use successive divisions to reduce the problem of ﬁnding the greatest common divisor of two positive integers to the same problem with smaller integers, until one of the integers is zero.
* The Euclidean algorithm is based on the following result about greatest common divisors and the division algorithm.

> [!Info] Lemma 1
> Let `a = bq + r`, where `a`, `b`, `q`, and `r` are integers. Then `gcd(a, b) = gcd(b, r)`.

* Suppose that $a$ and $b$ are positive integers with $a \ge b$. Let $r_0 = a$ and $r_1 = b$. When we successively apply the division algorithm, we obtain
	* $r_0 = r_1 q_1 + r_2$   $0 \le r_2 \lt r_1$,
	* $r_1 = r_2 q_2 + r_3$   $0 \le r_3 \lt r_2$,
	* .
	* .
	* .
	* $r_{n-2} = r_{n-1} q_{n-1} + r_{n}$   $0 \le r_n \lt r_{n-1}$,
	* $r_{n-1} = r_n q_n$.
* Eventually a remainder of zero occurs in this sequence of successive divisions, because the sequence of remainders $a = r_0 \gt r_1 \gt r_2 \gt ⋯ \ge 0$ cannot contain more than $a$ terms. Furthermore, it follows from Lemma 1 that
	* $gcd(a, b) = gcd(r_0, r_1) = gcd(r_1, r_2) = ... = gcd(r_{n-1}, r_n) = gcd(r_n, r_0) = r_n$
* Hence, the greatest common divisor is the last nonzero remainder in the sequence of divisions.

> [!Error] 4.3.8 gcds as Linear Combinations

* An important result is that the greatest common divisor of two integers a and b can be expressed in the form $sa + tb$ where $s$ and $t$ are integers. In other words, $gcd(a, b)$ can be expressed as a linear combination with integer coeﬃcients of $a$ and $b$. We state this fact as Theorem 6.
	* For example, $gcd(6, 14) = 2$, and $2 = (−2) ⋅ 6 + 1 ⋅ 14$. 

> [!Info] Theorem 6: `bézout’s theorem`
> If `a` and `b` are positive integers, then there exist integers `s` and `t` such that `gcd(a, b) = sa + tb`.

> [!Info] Definition: `bézout coefficients and identity`
> If `a` and `b` are positive integers, then integers `s` and `t` such that `gcd(a, b) = sa + tb` are called bézout coeﬃcients of `a` and `b`. Also, the equation `gcd(a, b) = sa + tb` is called bézout’s identity.

---

* We will use Theorem 6 to develop several useful results. One of our goals will be to prove the part of the fundamental theorem of arithmetic asserting that a positive integer has at most one prime factorization. We will show that if a positive integer has a factorization into primes, where the primes are written in nondecreasing order, then this factorization is unique.
* First, we need to develop some results about divisibility.

> [!Info] Lemma 2
> If `a`, `b`, and `c` are positive integers such that `gcd(a, b) = 1` and `a ∣ bc`, then `a ∣ c`.

> [!Info] Lemma 3: a generalization of lemma 2
> If `p` is a prime and $p ∣ a_1 a_2 ⋯ a_n$ , where each $a_i$ is an integer, then $p ∣ a_i$ for some `i`.

---
* Lemma 2 can also be used to prove a result about dividing both sides of a congruence by the same integer.
* We have shown (Theorem 5 in Section 4.1) that we can multiply both sides of a congruence by the same integer. However, dividing both sides of a congruence by an integer does not always produce a valid congruence.
* Although we cannot divide both sides of a congruence by any integer to produce a valid congruence, we can **if** this integer is relatively prime to the modulus. Theorem 7 establishes this important fact.

> [!Info] Theorem 7
> Let `m` be a positive integer and let `a`, `b`, and `c` be integers. If `ac ≡ bc (mod m)` and `gcd(c, m) = 1`, then `a ≡ b (mod m)`.

##### 4.4 Solving Congruences
> `pg: 11`
> `time req: 1' 13"`
> `time done: 3' 31"`
> `performance: 34%`
>
> `questions: 67`
> `questions done: 13`
> `practice time req: 42"`
> `practice time done: 1' 55"`
> `p-performance: 36%`

> [!Error] 4.4.1 Introduction

* Solving linear congruences, which have the form `ax ≡ b (mod m)`, is an essential task in the study of number theory and its applications, just as solving linear equations plays an important role in calculus and linear algebra.

> [!Error] 4.4.2 Linear Congruences

* A congruence of the form `ax ≡ b (mod m)`, where `m` is a positive integer, `a` and `b` are integers, and `x` is a variable, is called a **linear congruence**. Such congruences arise throughout number theory and its applications.
* How can we solve the linear congruence $ax ≡ b (mod\ m)$, that is, how can we ﬁnd all integers $x$ that satisfy this congruence? One method that we will describe uses an integer $a$ such that $\bar{a}a ≡ 1 (mod\ m)$, if such an integer exists. Such an integer $\bar{a}$ is said to be an **inverse** of $a\ modulo\ m$. Theorem 1 guarantees that an inverse of $a\ modulo\ m$ exists whenever $a$ and $m$ are relatively prime.

> [!Info] Theorem 1
> If $a$ and $m$ are relatively prime integers and $m \gt 1$, then an inverse of $a\ modulo\ m$ exists. Furthermore, this inverse is unique modulo $m$. (That is, there is a unique positive integer $\bar{a}$ less than $m$ that is an inverse of a modulo $m$ and every other inverse of $a\ modulo\ m$ is congruent to $a\ modulo\ m$.)

* We can design a more eﬃcient algorithm than brute force to ﬁnd an inverse of $a\ modulo\ m$ when $gcd(a, m) = 1$ using the steps of the Euclidean algorithm (along with bézout's coefficients). By reversing these steps, we can ﬁnd a linear combination $sa + tm = 1$, where $s$ and $t$ are integers. Reducing both sides of this equation modulo $m$ tells us that $s$ is an inverse of $a\ modulo\ m$.
* Once we have an inverse $\bar{a}$ of $a\ modulo\ m$, we can solve the congruence $ax ≡ b (mod\ m)$ by multiplying both sides of the linear congruence by $\bar{a}$.
---
* **Example 1**: Find an inverse of $3\ modulo\ 7$ by ﬁrst ﬁnding Bézout coeﬃcients of $3$ and $7$.
* Because $gcd(3, 7) = 1$, Theorem 1 tells us that an inverse of $3\ modulo\ 7$ exists. The Euclidean algorithm ends quickly when used to ﬁnd the greatest common divisor of $3$ and $7$:
	* $7 = 2 ⋅ 3 + 1$
* From this equation we see that
	* $−2 ⋅ 3 + 1 ⋅ 7 = 1$.
* This shows that $−2$ and $1$ are Bézout coeﬃcients of $3$ and $7$. We see that $−2$ is an inverse of $3 modulo 7$. Note that every integer congruent to $−2 modulo 7$ is also an inverse of $3$, such as $5$, $−9$, $12$, and so on.
---
> [!Question] ChatGPT
> > I know the answer to "$5x + 1 ≡ 2\ (mod\ 6)$" is "$x ≡ 1\ (mod\ 6)$". How did this conclusion occur?
> 
> 1. $5x + 1 ≡ 2\ (mod\ 6)$
> 2. subtract 1 from both sides:
> 	- $5x ≡ 1\ (mod\ 6)$
> 3. Now, find the modular inverse of $5\ modulo\ 6$:
> 	- To find the modular inverse of $5\ modulo\ 6$, we are looking for a number $\bar{a}$ such that $5 × \bar{a} ≡ 1\ (mod\ 6)$. **In other words, we need to find a number $\bar{a}$ such that when you multiply it by $5$ and take the result $modulo\ 6$, you get $1$.**
> 	- The numbers $modulo\ 6$ are $\{0, 1, 2, 3, 4, 5\}$. Checking each of these, we find that $5 × 5 ≡ 25 ≡ 1\ (mod\ 6)$. Therefore, the modular inverse of $5 modulo 6$ is $5$.
> 4. Multiply both sides by the modular inverse:
> 	- $5 × 5x ≡ 5 × 1\ (mod\ 6)$
> 	- $x ≡ 5\ (mod\ 6)$
> 		- *note that coefficients can be reduced in modulo operations.*

> [!Error] 4.4.3 The Chinese Remainder Theorem

* The Chinese remainder theorem, named after the Chinese heritage of problems involving systems of linear congruences, states that when the moduli of a system of linear congruences are pairwise relatively prime, there is a unique solution of the system modulo the product of the moduli.

> [!Info] Theorem 2: `The Chinese Remainder Theorem`
> Let $m_1, m_2, …, m_n$ be pairwise relatively prime positive integers greater than one and $a_1, a_2, …, a_n$ arbitrary integers. Then the system
>
> - $x ≡ a_1 (mod\ m_1)$,
> - $x ≡ a_2 (mod\ m_2)$,
> - .
> - .
> - .
> - $x ≡ a_n (mod\ m_n)$,
>
> has a unique solution modulo $m = m_1 m_2 ⋯ m_n$ . (That is, there is a solution $x$ with $0 \le x \lt m$, and all other solutions are congruent $modulo\ m$ to this solution.)

* **Proof**
* We will show that a solution exists by describing a way to construct this solution.
* To construct a simultaneous solution, ﬁrst let
	* $M_k = m/m_k$
* for $k = 1, 2, …, n$. That is, $M_k$ is the product of the moduli except for $m_k$. Because $m_i$ and $m_k$ have no common factors greater than $1$ when $i \ne k$, it follows that $gcd(m_k, M_k) = 1$. Consequently, by Theorem 1, we know that there is an integer $y_k$, an inverse of $M_k\ modulo\ m_k$ , such that
	* $M_k y_k ≡ 1 (mod\ m_k)$.
* To construct a simultaneous solution, form the sum
	* $x = a_1 M_1 y_1 + a_2 M_2 y_2 + ... + a_n M_n y_n$.
* We will now show that $x$ is a simultaneous solution. First, note that because $M_j ≡ 0 (mod\ m_k)$ whenever $j \ne k$, all terms except the kth term in this sum are congruent to $0\ modulo\ m_k$ . Because $M_k y_k ≡ 1 (mod m_k)$ we see that
	* $x ≡ a_k M_k y_k ≡ a_k (mod\ m_k)$
* for $k = 1, 2, …, n$. We have shown that $x$ is a simultaneous solution to the $n$ congruences.
* Example 5 illustrates how to use the construction given in our proof of the Chinese remainder theorem to solve a system of congruences. We will solve the system given in Example 4, which arises in Sun-Tsu’s puzzle.
* **Example 5:** To solve the system of congruences in Example 4, ﬁrst let $m = 3 ⋅ 5 ⋅ 7 = 105$, $M_1 = m/3 = 35$, $M_2 = m/5 = 21$, and $M_3 = m/7 = 15$. We see that $2$ is an inverse of $M_1 = 35\ modulo\ 3$, because $35 ⋅ 2 ≡ 2 ⋅ 2 ≡ 1\ (mod\ 3)$; $1$ is an inverse of $M_2 = 21\ modulo\ 5$, because $21 ≡ 1\ (mod\ 5)$; and $1$ is an inverse of $M_3 = 15 (mod\ 7)$, because $15 ≡ 1\ (mod\ 7)$. The solutions to this system are those $x$ such that
	* $x ≡ a_1 M_1 y_1 + ... + a_3 M_3 y_3 = 140 + 63 + 30 = 233 ≡ 23\ (mod\ 105)$.
* It follows that $23$ is the smallest positive integer that is a simultaneous solution. We conclude that $23$ is the smallest positive integer that leaves a remainder of $2$ when divided by $3$, a remainder of $3$ when divided by $5$, and a remainder of $2$ when divided by $7$.
---
* Although the construction in Theorem 2 provides a general method for solving systems of linear congruences with pairwise relatively prime moduli, it can be easier to solve a system using a diﬀerent method. Example 6 illustrates the use of a method known as **back substitution**.
* **Example 6**: Use the method of back substitution to ﬁnd all integers $x$ such that $x ≡ 1\ (mod\ 5)$, $x ≡ 2\ (mod\ 6)$, and $x ≡ 3\ (mod\ 7)$.
* By Theorem 4 in Section 4.1, the ﬁrst congruence can be rewritten as an equality, $x = 5t + 1$, where $t$ is an integer. Substituting this expression for $x$ into the second congruence tells us that
	* $5t + 1 ≡ 2 (mod 6)$,
* which can be solved to show that $t ≡ 5 (mod 6)$. Using Theorem 4 in Section 4.1 again, we see that $t = 6u + 5$, where $u$ is an integer. Substituting this expression for $t$ back into the equation $x = 5t + 1$ tells us that $x = 5(6u + 5) + 1 = 30u + 26$. We insert this into the third equation to obtain
	* $30u + 26 ≡ 3\ (mod\ 7)$.
* Solving this congruence tells us that $u ≡ 6\ (mod\ 7)$ (as the reader should verify). Hence, Theorem 4 in Section 4.1 tells us that $u = 7v + 6$, where $v$ is an integer. Substituting this expression for $u$ into the equation $x = 30u + 26$ tells us that $x = 30(7v + 6) + 26 = 210u + 206$. Translating this back into a congruence, we ﬁnd the solution to the simultaneous congruences,
	* $x ≡ 206 (mod 210)$.

> [!Error] 4.4.4 Computer Arithmetic with Large Integers

* Suppose that $m_1, m_2, …, m_n$ are pairwise relatively prime moduli and let $m$ be their product. By the Chinese remainder theorem, we can show that an integer $a$ with $0 ≤ a < m$ can be uniquely represented by the n-tuple consisting of its remainders upon division by $m_i$, $i = 1, 2, …, n$. That is, we can uniquely represent $a$ by
	* $(a\ mod\ m_1, a\ mod\ m_2, …, a\ mod\ m_n)$.
---
* **Large Integer Arithmetic**
* To perform arithmetic with large integers, we select moduli $m_1, m_2, …, m_n$, where each $m_i$ is an integer greater than $2$, $gcd(m_i, m_j) = 1$ whenever $i \ne j$, and $m = m_1 m_2 ⋯ m_n$ is greater than the results of the arithmetic operations we want to carry out.
* Once we have selected our moduli, we carry out arithmetic operations with large integers by performing componentwise operations on the n-tuples representing these integers using their remainders upon division by $m_i$, $i = 1, 2, … , n$. Once we have computed the value of each component in the result, we recover its value by solving a system of $n$ congruences $modulo m_i$, $i = 1, 2, … , n$.
* This method of performing arithmetic with large integers has several valuable features. First, it can be used to perform arithmetic with integers larger than can ordinarily be carried out on a computer. Second, computations with respect to the diﬀerent moduli can be done in parallel, speeding up the arithmetic.
* **Example 8**: Suppose that performing arithmetic with integers less than $100$ on a certain processor is much quicker than doing arithmetic with larger integers. We can restrict almost all our computations to integers less than $100$ if we represent integers using their remainders modulo pairwise relatively prime integers less than $100$. For example, we can use the moduli of $99$, $98$, $97$, and $95$. (These integers are relatively prime pairwise, because no two have a common factor greater than $1$.)
* By the Chinese remainder theorem, every nonnegative integer less than $99 ⋅ 98 ⋅ 97 ⋅ 95 = 89,403,930$ can be represented uniquely by its remainders when divided by these four moduli. For example, we represent $123,684$ as $(33, 8, 9, 89)$, because $123,684\ mod\ 99 = 33$; $123,684\ mod\ 98 = 8$; $123,684\ mod\ 97 = 9$; and $123,684\ mod\ 95 = 89$. Similarly, we represent $413,456$ as $(32, 92, 42, 16)$.
* To ﬁnd the sum of $123,684$ and $413,456$, we work with these 4-tuples instead of these two integers directly. We add the 4-tuples componentwise and reduce each component with respect to the appropriate modulus. This yields
	* $(33, 8, 9, 89) + (32, 92, 42, 16)$
	* $= (65\ mod\ 99, 100\ mod\ 98, 51\ mod\ 97, 105\ mod\ 95)$
	* $= (65, 2, 51, 10)$.
* To ﬁnd the sum, that is, the integer represented by $(65, 2, 51, 10)$, we need to solve the system of congruences
	* $x ≡ 65\ (mod\ 99)$,
	* $x ≡ 2\ (mod\ 98)$,
	* $x ≡ 51\ (mod\ 97)$,
	* $x ≡ 10\ (mod\ 95)$.
* It can be shown that $537,140$ is the unique nonnegative solution of this system less than $89,403,930$. Consequently, $537,140$ is the sum. Note that it is only when we have to recover the integer represented by $(65, 2, 51, 10)$ that we have to do arithmetic with integers larger than $100$.
---
* Particularly good choices for moduli for arithmetic with large integers are sets of integers of the form $2^k − 1$, where $k$ is a positive integer, because it is easy to do binary arithmetic modulo such integers, and because it is easy to ﬁnd sets of such integers that are pairwise relatively prime. \[The second reason is a consequence of the fact that $gcd(2^a − 1, 2^b − 1) = 2^{gcd(a, b)} − 1$.] Suppose, for instance, that we can do arithmetic with integers less than $235$ easily on our computer, but that working with larger integers requires special procedures. We can use pairwise relatively prime moduli less than $235$ to perform arithmetic with integers as large as their product. For example, the integers $235 − 1$, $234 − 1$, $233 − 1$, $231 − 1$, $229 − 1$, $and 223 − 1$ are pairwise relatively prime. Because the product of these six moduli exceeds $2184$ , we can perform arithmetic with integers as large as $2184$ (as long as the results do not exceed this number) by doing arithmetic modulo each of these six moduli, none of which exceeds $235$.

> [!Error] 4.4.5 Fermat's Little Theorem

> [!Info] Theorem 3: `Fermat's Little Theorem`
> If $p$ is prime and a is an integer not divisible by $p$, then
>
> - $a^{p-1} ≡ 1\ (mod\ p) \impliedby a^{p-1} - 1 ≡ 0\ (mod\ p)$
>
> Furthermore, for every integer $a$ we have
>
> - $a^p ≡ a\ (mod\ p)$.

* **Example 9**: Find $7^{222}\ mod\ 11$.
* We can use Fermat’s little theorem to evaluate $7^{222}\ mod\ 11$ rather than using the fast modular exponentiation algorithm. By Fermat’s little theorem we know that $7^{10} ≡ 1\ (mod\ 11)$, so $(7^{10})^k ≡ 1\ (mod\ 11)$ for every positive integer $k$. To take advantage of this last congruence, we divide the exponent $222$ by $10$, ﬁnding that $222 = 22 ⋅ 10 + 2$. We now see that
	* $7^{222} = 7^{22 . 10 + 2} = (7^{10})^{22} 7^2 ≡ (1)^{22} . 49 ≡ 5\ (mod\ 11)$.
* It follows that $7^{222}\ mod\ 11 = 5$.
* Example 9 illustrated how we can use Fermat’s little theorem to compute $a^n\ mod\ p$, where $p$ is prime and $p$ does not devise $a$. First, we use the division algorithm to ﬁnd the quotient $q$ and remainder $r$ when $n$ is divided by $p − 1$, so that $n = q(p − 1) + r$, where $0 \le r \lt p − 1$. It follows that $a^n = a^{q(p−1)+r} = (a^{p−1})^q a^r ≡ 1^q a^r ≡ a^r\ (mod\ p)$. Hence, to ﬁnd $a^n\ mod\ p$, we only need to compute $a^r\ mod\ p$. We will take advantage of this simpliﬁcation many times in our study of number theory.

> [!Error] 4.4.6 Pseudoprimes

> [!Info] Definition: `pseudoprime`
> Let $b$ be a positive integer. If $n$ is a composite positive integer, and $b^{n−1} ≡ 1\ (mod\ n)$, then $n$ is called a *pseudoprime* to the base $b$.

> [!Info] Definition: `Carmichael number`
> A composite integer $n$ that satisﬁes the congruence $b^{n−1} ≡ 1\ (mod\ n)$ for all positive integers $b$ with $gcd(b, n) = 1$ is called a Carmichael number. (These numbers are named after *Robert Carmichael*, who studied them in the early twentieth century.)

> [!Error] 4.4.7 Primitive Roots and Discrete Logarithms

* In the set of positive real numbers, if $b > 1$, and $x = b^y$ , we say that $y$ is the logarithm of $x$ to the base $b$.

> [!Info] Definition: `primitive root`
> A *primitive root* $modulo\ a$ prime $p$ is an integer $r$ in $Z_p$ such that every nonzero element of $Z_p$ is a power of $r$.

* **Example 12**: Determine whether $2$ and $3$ are primitive roots modulo $11$.
	* When we compute the powers of $2$ in $Z_{11}$ , we obtain $2^{10} = 1$, $2^1 = 2$, $2^8 = 3$, $2^2 = 4$, $2^4 = 5$, $2^9 = 6$, $2^7 = 7$, $2^3 = 8$, $2^6 = 9$, $2^5 = 10$. Because every nonzero element of $Z_{11}$ is a power of $2$, $2$ is a primitive root of $11$.
	* When we compute the powers of $3\ modulo\ 11$, we obtain $3^1 = 3$, $3^2 = 9$, $3^3 = 5$, $3^4 = 4$, $3^5 = 1$. This pattern repeats when we compute higher powers of $3$. Because not all nonzero elements of $Z_{11}$ are powers of $3$, we conclude that $3$ is not a primitive root of $11$.
---
* An important fact in number theory is that there is a primitive root modulo $p$ for every prime $p$. Suppose that $p$ is prime and $r$ is a primitive root modulo $p$. If $a$ is an integer between $1$ and $p − 1$, that is, a nonzero element of $Z_p$ , we know that there is an unique exponent $e$ such that $r^e = a$ in $Z_p$ , that is, $r^e\ mod\ p = a$.

> [!Info] Definition: `discrete logarithm`
> Suppose that $p$ is a prime, $r$ is a primitive root modulo $p$, and $a$ is an integer between $1$ and $p − 1$ inclusive. If $r^e\ mod\ p = a$ and $0 \le e \le p − 1$, we say that $e$ is the discrete logarithm of $a\ modulo\ p$ to the base $r$ and we write $\log_{r} a = e$ (where the prime $p$ is understood).

* **Example 13**: Find the discrete logarithms of $3$ and $5$ $modulo\ 11$ to the base $2$.
* When we computed the powers of $2\ modulo\ 11$, we found that $2^8 = 3$ and $2^4 = 5$ in $Z_{11}$ . Hence, the discrete logarithms of $3$ and $5$ $modulo\ 11$ to the base $2$ are $8$ and $4$, respectively. (These are the powers of $2$ that equal $3$ and $5$, respectively, in $Z_{11}$ .) We write $\log_{2} 3 = 8$ and $\log_{2} 5 = 4$ (where the $modulus\ 11$ is understood and not explicitly noted in the notation).

##### 4.5 Applications of Congruences
> `pg: 6`
> `time req: 39"`
> `time done: 23"`
> `performance: 169%`
>
> `questions: 35`
> `practice time req: 23"`

> [!Error] 4.5.2 Pseudorandom Numbers

* Randomly chosen numbers are often needed for computer simulations. Diﬀerent methods have been devised for generating numbers that have properties of randomly chosen numbers. Because numbers generated by systematic methods are not truly random, they are called **pseudorandom numbers**.
* The most commonly used procedure for generating pseudorandom numbers is the **linear congruential method**. We choose four integers: the **modulus** $m$, **multiplier** $a$, **increment** $c$, and **seed** $x_0$ , with $2 \le a \lt m$, $0 \le c \lt m$, and $0 \le x_0 \lt m$. We generate a sequence of pseudorandom numbers $\{x_n\}$, with $0 \le x_n \lt m$ for all $n$, by successively using the recursively deﬁned function
	* $x_{n+1} = (ax_n + c)\ mod\ m$.
* Many computer experiments require the generation of pseudorandom numbers between $0$ and $1$. To generate such numbers, we divide numbers generated with a linear congruential generator by the modulus: that is, we use the numbers $x_n / m$.
* Most computers do use linear congruential generators to generate pseudorandom numbers. Often, a linear congruential generator with increment $c = 0$ is used. Such a generator is called a pure multiplicative generator. For example, the pure multiplicative generator with modulus $231 − 1$ and multiplier $75 = 16,807$ is widely used. With these values, it can be shown that $231 − 2$ numbers are generated before repetition begins.
* Pseudorandom numbers generated by linear congruential generators have long been used for many tasks. Unfortunately, it has been shown that sequences of pseudorandom numbers generated in this way do not share some important statistical properties that true random numbers have. Because of this, it is not advisable to use them for some tasks, such as large simulations. For such sensitive tasks, other methods are used to produce sequences of pseudorandom numbers, either using some sort of algorithm or sampling numbers arising from a random physical\ phenomenon.

##### 4.6 Cryptography
> `pg: 12`
> `time req: 1' 19"`
> `time done: 1' 34"`
> `performance: 84%`
>
> `questions: 35`
> `practice time req: 46"`

> [!Error] 4.6.2 Classical Cryptography

* One of the earliest known uses of cryptography was by Julius Caesar. He made messages secret by shifting each letter three letters forward in the alphabet (sending the last three letters of the alphabet to the ﬁrst three). This is **encryption**, that is, the process of making a message secret.
* To express Caesar’s encryption process mathematically, ﬁrst replace each letter by an element of $Z_{26}$ , that is, an integer from $0$ to $25$ equal to one less than its position in the alphabet. Caesar’s encryption method can be represented by the function $f$ that assigns to the nonnegative integer $p$, $p ≤ 25$, the integer $f(p)$ in the set $\{0, 1, 2, … , 25\}$ with
	* $f(p) = (p + 3)\ mod\ 26$.
* In the encrypted version of the message, the letter represented by $p$ is replaced with the letter represented by $(p + 3)\ mod\ 26$.
* To recover the original message from a secret message encrypted by the Caesar cipher, the function $f^{−1}$ , the inverse of $f$ , is used. Note that the function $f^{−1}$ sends an integer $p$ from $Z_{26}$ , to $f^{−1}(p) = (p − 3)\ mod\ 26$. In other words, to ﬁnd the original message, each letter is shifted back three letters in the alphabet, with the ﬁrst three letters sent to the last three letters of the alphabet. The process of determining the original message from the encrypted message is called **decryption**.
---
* There are various ways to generalize the Caesar cipher. For example, instead of shifting the numerical equivalent of each letter by $3$, we can shift the numerical equivalent of each letter by $k$, so that
	* $f(p) = (p + k)\ mod\ 26$.
* Such a cipher is called a shift cipher. Note that decryption can be carried out using
	* $f^{−1}(p) = (p − k)\ mod\ 26$.
* Here the integer k is called a key.
---
* We can generalize shift ciphers further to slightly enhance security by using a function of the form
	* $f(p) = (ap + b)\ mod\ 26$,
* where $a$ and $b$ are integers, chosen so that $f$ is a bijection. (The function $f(p) = (ap + b)\ mod\ 26$ is a bijection if and only if $gcd(a, 26) = 1$.) Such a mapping is called an *aﬃne transformation*, and the resulting cipher is called an *aﬃne cipher*.
* We will now show how to decrypt messages encrypted using an aﬃne cipher. Suppose that $c = (ap + b)\ mod\ 26$ with $gcd(a, 26) = 1$. To decrypt we need to show how to express $p$ in terms of $c$. To do this, we apply the encrypting congruence $c ≡ ap + b\ (mod\ 26)$, and solve it for $p$. To do this, we ﬁrst subtract $b$ from both sides, to obtain $c − b ≡ ap\ (mod\ 26)$. Because $gcd(a, 26) = 1$, we know that there is an inverse $\bar{a}$ of $a\ modulo\ 26$. Multiplying both sides of the last equation by a gives us $\bar{a}(c − b) ≡ \bar{a}ap\ (mod\ 26)$. Because $\bar{a}a ≡ 1\ (mod\ 26)$, this tells us that $p ≡ \bar{a}(c − b)\ (mod\ 26)$. This determines $p$ because $p$ belongs to $Z_{26}$ .
---
* **Cryptanalysis**
* The process of recovering plaintext from ciphertext without knowledge of both the encryption method and the key is known as **cryptanalysis** or **breaking codes**. In general, cryptanalysis is a diﬃcult process, especially when the encryption method is unknown.
---
* **Block Ciphers**
* Shift ciphers and aﬃne ciphers proceed by replacing each letter of the alphabet by another letter in the alphabet. Because of this, these ciphers are called **character** or **monoalphabetic** **ciphers**. Encryption methods of this kind are vulnerable to attacks based on the analysis of letter frequency in the ciphertext, as we just illustrated. We can make it harder to successfully attack ciphertext by replacing blocks of letters with other blocks of letters instead of replacing individual characters with individual characters; such ciphers are called **block ciphers**.
* We will now introduce a simple type of block cipher, called the **transposition cipher**. As a key we use a permutation $𝜎$ of the set $\{1, 2, … , m\}$ for some positive integer $m$, that is, a one-to-one function from $\{1, 2, … , m\}$ to itself. To encrypt a message we ﬁrst split its letters into blocks of size $m$. (If the number of letters in the message is not divisible by $m$ we add some random letters at the end to ﬁll out the ﬁnal block.) We encrypt the block $p_1 p_2 … p_m$ as $c_1 c_2 … c_m = p_{𝜎(1)} p_{𝜎(2)} … , p_{𝜎(m)}$ . To decrypt a ciphertext block $c_1 c_2 … c_m$, we transpose its letters using the permutation $𝜎 − 1$ , the inverse of $𝜎$.
---
> [!Info] Definition: `cryptosystems`
> A *cryptosystem* is a ﬁve-tuple ($\mathcal{P}$, $\mathcal{C}$, $\mathcal{K}$, $\mathcal{E}$, $\mathcal{D}$), where $\mathcal{P}$ is the set of plaintext strings, $\mathcal{C}$ is the set of ciphertext strings, $\mathcal{K}$ is the *keyspace* (the set of all possible keys), $\mathcal{E}$ is the set of encryption functions, and $\mathcal{D}$ is the set of decryption functions. We denote by $E_k$ the encryption function in $\mathcal{E}$ corresponding to the key $k$ and $D_k$ the decryption function in $\mathcal{D}$ that decrypts ciphertext that was encrypted using $E_k$ , that is, $D_k(E_k(p)) = p$, for all plaintext strings $p$.

* **Example 7**: Describe the family of shift ciphers as a cryptosytem.
* To encrypt a string of English letters with a shift cipher, we ﬁrst translate each letter to an integer between $0$ and $25$, that is, to an element of $Z_{26}$. We then shift each of these integers by a ﬁxed integer $modulo\ 26$, and ﬁnally, we translate the integers back to letters. To apply the deﬁnition of a cryptosystem to shift ciphers, we assume that our messages are already integers, that is, elements of $Z_{26}$ . That is, we assume that the translation between letters and integers is outside of the cryptosystem. Consequently, both the set of plaintext strings $\mathcal{P}$ and the set of ciphertext strings $\mathcal{C}$ are the set of strings of elements of $Z_{26}$ . The set of keys $\mathcal{K}$ is the set of possible shifts, so $\mathcal{K} = Z_{26}$ . The set $\mathcal{E}$ consists of functions of the form $E_k(p) = (p + k)\ mod\ 26$, and the set $\mathcal{D}$ of decryption functions is the same as the set of encrypting functions where $D_k(p) = (p − k)\ mod\ 26$.

> [!Error] 4.6.3 Public Key Cryptography

* All classical ciphers, including shift ciphers and aﬃne ciphers, are examples of **private key cryptosystems**. In a private key cryptosystem, once you know an encryption key, you can quickly ﬁnd the decryption key. So, knowing how to encrypt messages using a particular key allows you to decrypt messages that were encrypted using this key. For example, when a shift cipher is used with encryption key $k$, the plaintext integer $p$ is sent to
	* $c = (p + k)\ mod\ 26$.
* Decryption is carried out by shifting by $−k$; that is,
	* $p = (c − k)\ mod\ 26$.
* So knowing how to encrypt with a shift cipher also tells you how to decrypt.
---
* When a private key cryptosystem is used, two parties who wish to communicate in secret must share a secret key. Because anyone who knows this key can both encrypt and decrypt messages, two people who want to communicate securely need to securely exchange this key. The shift cipher and aﬃne cipher cryptosystems are private key cryptosystems. They are quite simple and are extremely vulnerable to cryptanalysis. However, the same is not true of many modern private key cryptosystems. In particular, the current US government standard for private key cryptography, the Advanced Encryption Standard (AES), is extremely complex and is considered to be highly resistant to cryptanalysis. AES is widely used in government and commercial communications. However, it still shares the property that for secure communications keys be shared. Furthermore, for extra security, a new key is used for each communication session between two parties, which requires a method for generating keys and securely sharing them.
* To avoid the need for keys to be shared by every pair of parties that wish to communicate securely, in the 1970s cryptologists introduced the concept of public key cryptosystems. When such cryptosystems are used, knowing how to send an encrypted message does not help decrypt messages. In such a system, everyone can have a publicly known encryption key. Only the decryption keys are kept secret, and only the intended recipient of a message can decrypt it, because, as far as it is currently known, knowledge of the encryption key does not let someone recover the plaintext message without an extraordinary amount of work (such as billions of years of computer time).
* The ﬁrst public key cryptosystems were invented in the mid-1970s. Many additional public key cryptosystems have been developed in the ensuing decades. We will introduce the most commonly used public key cryptosystem, known as the RSA system, in this book. Besides RSA, there are several other commonly used public key cryptosystems that are now used for many applications. These other public key cryptosystems will play an important role in the future when advances in commuting may make the RSA cryptosystem obsolete, as often happens in cryptography.
* Although public key cryptography has the advantage that two parties who wish to communicate securely do not need to exchange keys, it has the disadvantage that encryption and decryption can be extremely time-consuming. For many applications, this makes public key cryptography impractical. In such situations, private key cryptography is used instead. However, public key cryptography may still be used in the key exchange process.

> [!Error] 4.6.4 The RSA Cryptosystem

* In the RSA cryptosystem, each individual has an encryption key $(n, e)$, where $n = pq$, the modulus is the product of two large primes $p$ and $q$, say with $300$ digits each, and an exponent $e$ that is relatively prime to $(p − 1)(q − 1)$. To produce a usable key, two large primes must be found. This can be done quickly on a computer using probabilistic primality tests, referred to earlier in this section. However, the product of these primes $n = pq$, with approximately $600$ digits, cannot, as far as is currently known, be factored in a reasonable length of time. As we will see, this is an important reason why decryption cannot, as far as is currently known, be done quickly without a separate decryption key.
* **Remark**: With the steady increase of the speed of computers, the recommended size of the primes $p$ and $q$ used to produce a RSA public key has increased. But the larger $n$ is, the slower RSA encryption and decryption become. When considering this tradeoﬀ, the number of years a message needs to be remain secret is important. A more important consideration is that the development of quantum computing threatens the security of the RSA cryptosystem, because factorization algorithms have been developed for quantum computers that could then be used to quickly factor large primes. So, once quantum computing becomes practical, perhaps in the next $20$ to $30$ years, other public key cryptosystems that cannot be broken using quantum computing will need to be used.

> [!Error] 4.6.5 RSA Encryption

* To encrypt messages using a particular key $(n, e)$, we ﬁrst translate a plaintext message $M$ into sequences of integers. To do this, we ﬁrst translate each plaintext letter into a two-digit number, using the same translation we employed for shift ciphers, with one key diﬀerence. That is, we include an initial zero for the letters $A$ through $J$, so that $A$ is translated into $00$, $B$ into $01$, … , and $J$ into $09$. Then, we concatenate these two-digit numbers into strings of digits. Next, we divide this string into equally sized blocks of $2N$ digits, where $2N$ is the largest even number such that the number $2525$ … $25$ with $2N$ digits does not exceed $n$. (When necessary, we pad the plaintext message with dummy $Xs$ to make the last block the same size as all other blocks.)
* After these steps, we have translated the plaintext message $M$ into a sequence of integers $m_1, m_2, …, m_k$ for some integer $k$. Encryption proceeds by transforming each block $m_i$ to a ciphertext block $c_i$. This is done using the function
	* $c = m^e\ mod\ n$.
* (To perform the encryption, we use an algorithm for fast modular exponentiation) We leave the encrypted message as blocks of numbers and send these to the intended recipient. Because the RSA cryptosystem encrypts blocks of characters into blocks of characters, it is a block cipher.

> [!Error] 4.6.6 RSA Decryption

* The plaintext message can be quickly recovered from a ciphertext message when the decryption key $d$, an inverse of $e\ modulo\ (p − 1)(q − 1)$, is known. \[Such an inverse exists because $gcd(e, (p − 1)(q − 1)) = 1$.\] To see this, note that if $de ≡ 1\ (mod\ (p − 1)(q − 1))$, there is an integer $k$ such that $de = 1 + k(p − 1)(q − 1)$. It follows that
	* $c^d ≡ (m^e)^d = m^{de} = m^{1+k(p-1)(q-1)}\ (mod\ n)$.
* By Fermat’s little theorem \[assuming that $gcd(m, p) = gcd(m, q) = 1$, which holds except in rare cases], it follows that $m^{p−1} ≡ 1\ (mod\ p)$ and $m^{q−1} ≡ 1\ (mod\ q)$. Consequently,
	* $c^d ≡ m ⋅ (m^{p−1})^{k(q−1)} ≡ m ⋅ 1 = m\ (mod\ p)$
* and
	* $c^d ≡ m ⋅ (m^{q−1})^{k(p−1)} ≡ m ⋅ 1 = m\ (mod\ q)$.
* Because $gcd(p, q) = 1$, it follows by the Chinese remainder theorem that
	* $c^d ≡ m\ (mod\ pq)$.

> [!Error] 4.6.7 RSA as a Public Key System

* Why is the RSA cryptosystem suitable for public key cryptography? First, it is possible to rapidly construct a public key by ﬁnding two large primes $p$ and $q$, each with more than $300$ digits, and to ﬁnd an integer $e$ relatively prime to $(p − 1)(q − 1)$. When we know the factorization of the modulus $n$, that is, when we know $p$ and $q$, we can quickly ﬁnd an inverse $d$ of $e\ modulo\ (p − 1)(q − 1)$. \[This is done by using the Euclidean algorithm to ﬁnd Bézout coeﬃcients $s$ and $t$ for $d$ and $(p − 1)(q − 1)$, which shows that the inverse of $d\ modulo\ (p − 1)(q − 1)$ is $s\ mod\ (p − 1)(q − 1)$.] Knowing $d$ lets us decrypt messages sent using our key. However, no method is known to decrypt messages that is not based on ﬁnding a factorization of $n$, or that does not also lead to the factorization of $n$.
* Factorization is believed to be a diﬃcult problem, as opposed to ﬁnding large primes $p$ and $q$, which can be done quickly. The most eﬃcient factorization methods known (as of 2017) require billions of years to factor $600$-digit integers. Consequently, when $p$ and $q$ are $300$-digit primes, it is believed that messages encrypted using $n = pq$ as the modulus cannot be decrypted in a reasonable time unless the primes $p$ and $q$ are known.
* Although no polynomial-time algorithm is known for factoring large integers, active research is under way to ﬁnd new ways to eﬃciently factor integers. Integers that were thought, as recently as several years ago, to be far too large to be factored in a reasonable amount of time can now be factored routinely. Integers with more than $230$ digits have been factored using team eﬀorts. When new factorization techniques are found, it will be necessary to use larger primes to ensure the secrecy of messages. Unfortunately, messages that were considered secure earlier can be saved and subsequently decrypted by unintended recipients when it becomes feasible to factor the $n = pq$ in the key used for RSA encryption. (Note that the RSA system will be insecure once quantum computing is available.)
* The RSA method is now widely used. However, the most commonly used cryptosystems are private key cryptosystems. The use of public key cryptography, via the RSA system, is growing. Nevertheless, there are applications that use both private key and public key systems. For example, a public key cryptosystem, such as RSA, can be used to distribute private keys to pairs of individuals when they wish to communicate. These people then use a private key system for the encryption and decryption of messages.

> [!Error] 4.6.8 Cryptographic Protocols

* So far we have shown how cryptography can be used to make messages secure. However, there are many other important applications of cryptography. Among these applications are cryptographic protocols, which are exchanges of messages carried out by two or more parties to achieve a particular security goal. In particular, we will show how cryptography can be used to allow two people to exchange a secret key over an insecure communication channel. We will also show how cryptography can be used to send signed secret messages so that the recipient can be sure that the message came from the purported sender.
---
* **Key Exchange**: We now discuss a protocol that two parties can use to exchange a secret key over an insecure communications channel without having shared any information in the past. Generating a key that two parties can share is important for many applications of cryptography. For example, for two people to send secure messages to each other using a private key cryptosystem they need to share a common key. The protocol we will describe is known as the Diﬃe-Hellman key agreement protocol.
* Suppose that Alice and Bob want to share a common key. The protocol follows these steps, where the computations are done in $Z_p$ .
	1. Alice and Bob agree to use a prime $p$ and a primitive root $a$ of $p$.
	2. Alice chooses a secret integer $k_1$ and sends $a^{k_1}\ mod\ p$ to Bob.
	3. Bob chooses a secret integer $k_2$ and sends $a^{k_2}\ mod\ p$ to Alice.
	4. Alice computes $(a^{k_2})^{k_1}\ mod\ p$.
	5. Bob computes $(a^{k_1})^{k_2}\ mod\ p$.
* At the end of this protocol, Alice and Bob have computed their shared key, namely,
	* $(a^{k_2})^{k_1}\ mod\ p = (a^{k_1})^{k_2}\ mod\ p$.
* To analyze the security of this protocol, note that the messages sent in steps (1), (2), and (3) are not assumed to be sent securely. We can even assume that these communications were in the clear and that their contents are public information. So, $p$, $a$, $a^{k_1}\ mod\ p$, and $a^{k_2}\ mod\ p$ are assumed to be public information. The protocol ensures that $k_1$ , $k_2$ , and the common key $(a^{k_2})^{k_1}\ mod\ p = (a^{k_1})^{k_2}\ mod\ p$ are kept secret. To ﬁnd the secret information from this public information requires that an adversary solves instances of the discrete logarithm problem, because the adversary would need to ﬁnd $k_1$ and $k_2$ from $a^{k_1}\ mod\ p$ and $a^{k_2}\ mod\ p$, respectively. Furthermore, no other method is known for ﬁnding the shared key using just the public information. We have remarked that this is thought to be computationally infeasible when $p$ and $a$ are suﬃciently large. With the computing power available now, this system is considered unbreakable when $p$ has more than $300$ decimal digits and $k_1$ and $k_2$ have more than $100$ decimal digits each.
---
* **Digital Signatures**
* Not only can cryptography be used to secure the conﬁdentiality of a message, but it also can be used so that the recipient of the message knows that it came from the person they think it came from. We ﬁrst show how a message can be sent so that a recipient of the message will be sure that the message came from the purported sender of the message. In particular, we can show how this can be accomplished using the RSA cryptosystem to apply a digital signature to a message.
* Suppose that Alice’s RSA public key is $(n, e)$ and her private key is $d$. Alice encrypts a plaintext message $x$ using the encryption function $E_{(n,e)}(x) = x^e\ mod\ n$. She decrypts a ciphertext message $y$ using the decryption function $D_{(n,e)} = x^d\ mod\ n$. Alice wants to send the message $M$ so that everyone who receives the message knows that it came from her. Just as in RSA encryption, she translates the letters into their numerical equivalents and splits the resulting string into blocks $m_1, m_2, …, m_k$ such that each block is the same size, which is as large as possible so that $0 \le m_i \le n$ for $i = 1, 2, ..., k$. She then applies her decryption function $D_{(n,e)}$ to each block, obtaining $D_{n,e}(m_i)$, $i = 1, 2, … , k$. She sends the result to all intended recipients of the message.
* When a recipient receives her message, they apply Alice’s encryption function $E_{(n,e)}$ to each block, which everyone has available because Alice’s key $(n, e)$ is public information. The result is the original plaintext block because $E_{(n,e)}(D_{(n,e)}(x)) = x$. So, Alice can send her message to as many people as she wants and by signing it in this way, every recipient can be sure it came from Alice.
* We have shown that signed messages can be sent using the RSA cryptosystem. We can extend this by sending signed secret messages. To do this, the sender applies RSA encryption using the publicly known encryption key of an intended recipient to each block that was encrypted using the sender’s decryption transformation. The recipient then ﬁrst applies his private decryption transformation and then the sender’s public encryption transformation.

> [!Error] Homomorphic Encryption

* A cryptosystem, such as RSA, can be used to encrypt ﬁles to keep them secret. Today, many users store encrypted ﬁles in the cloud, where they reside on remote computers. It is often necessary to run programs using data from ﬁles stored on the cloud. These data are vulnerable to users with access to the remote computer where our data are stored if we run programs on the cloud without downloading these data. These data are also vulnerable to eavesdroppers when we download ﬁles, run programs on our computer, and upload the output to the cloud. Could we avoid these vulnerabilities by just running programs on encrypted data? Although this seems farfetched at ﬁrst blush, in 1979, soon after RSA was introduced, the question was proposed whether there was a cryptosystem that allowed arbitrary computations to be run on encrypted data that would produce the encryption of the unencrypted output produced by this unencrypted input. For such a cryptosystem, it would not be necessary to decrypt input data because the program could be run on a remote system without disclosing either the input or the output. So, the search began for a **fully homomorphic cryptosystem** that allows arbitrary computations to be run remotely on encrypted data.
* In 2009, Craig Gentry described the ﬁrst fully homomorphic cryptosystem, based on what is known as lattice-based cryptography. Unfortunately, no practical fully homomorphic cryptosystems have yet been developed, because all require extremely large amounts of processing and memory. However, there is hope that new advances will lead to practical fully homomorphic cryptosystems in the not so distant future.

#### Chapter 5: Induction and Recursion
> [!Summary]
> `sum page: 59`
> `sum time req: 6' 31"`

* Proofs using mathematical induction have two parts. First, they show that the statement holds for the positive integer $1$. Second, they show that if the statement holds for a positive integer then it must also hold for the next larger integer. Mathematical induction is based on the rule of inference that tells us that if $P(1)$ and $\forall k(P(k) → P(k + 1))$ are true for the domain of positive integers, then $∀nP(n)$ is true. Mathematical induction can be used to prove a tremendous variety of results. Understanding how to read and construct proofs by mathematical induction is a key goal of learning discrete mathematics.
* We described sets by listing their elements or by giving some property that characterizes these elements. We gave formulae for the values of functions. There is another important way to deﬁne such objects, based on mathematical induction. To deﬁne functions, some initial terms are speciﬁed, and a *rule* is given for ﬁnding subsequent values from values already known. (We brieﬂy touched on this sort of deﬁnition in Chapter 2 when we showed how sequences can be deﬁned using recurrence relations.) Sets can be deﬁned by listing some of their elements and giving rules for constructing elements from those already known to be in the set. Such deﬁnitions, called **recursive deﬁnitions**, are used throughout discrete mathematics and computer science. Once we have deﬁned a set recursively, we can use a proof method called **structural induction** to prove results about this set.
* When a procedure is speciﬁed for solving a problem, this procedure must always solve the problem correctly. Just testing to see that the correct result is obtained for a set of input values does not show that the procedure always works correctly. The correctness of a procedure can be guaranteed only by proving that it always yields the correct result. The ﬁnal section of this chapter contains an introduction to the techniques of program veriﬁcation. This is a formal technique to verify that procedures are correct. Program veriﬁcation serves as the basis for attempts under way to prove in a mechanical fashion that programs are correct.

##### 5.1 Mathematical Induction
> `pg: 20`
> `time req: 2' 13"`
> `time done: 1' 36"`
> `performance: 138%`
>
> `questions: 85`
> `questions done: 5`
> `practice time req: 1' 18"`
> `practice time done: 1' 1"`
> `p-performance: 127%`

> [!Error] 5.1.1 Introduction

* Suppose that we have an inﬁnite ladder and we want to know whether we can reach every step on this ladder. We know two things:
	1. We can reach the ﬁrst rung of the ladder.
	2. If we can reach a particular rung of the ladder, then we can reach the next rung.
* Can we conclude that we can reach every rung? By (1), we know that we can reach the ﬁrst rung of the ladder. Moreover, because we can reach the ﬁrst rung, by (2), we can also reach the second rung; it is the next rung after the ﬁrst rung. Applying (2) again, because we can reach the second rung, we can also reach the third rung. Continuing in this way, we can show that we can reach the fourth rung, the ﬁfth rung, and so on. For example, after 100 uses of (2), we know that we can reach the 101st rung. But can we conclude that we are able to reach every rung of this inﬁnite ladder? The answer is yes, something we can verify using an important proof technique called mathematical induction. That is, we can show that the statement that we can reach the nth rung of the ladder is true for all positive integers $n$.

> [!Error] 5.1.2 Mathematical Induction

> [!Warning] Disclaimer
> Unfortunately, using the terminology “mathematical induction” clashes with the terminology used to describe diﬀerent types of reasoning. In logic, deductive reasoning uses rules of inference to draw conclusions from premises, whereas inductive reasoning makes conclusions only supported, but not ensured, by evidence. Mathematical proofs, including arguments that use mathematical induction, are deductive, not inductive.

> [!Info] Principle of Mathematical Induction
> To prove that $P(n)$ is true for all positive integers $n$, where $P(n)$ is a propositional function, we complete two steps:
> - **Basis Step**: We verify that $P(1)$ is true.
> - **Inductive Step**: We show that the conditional statement $P(k) → P(k + 1)$ is true for all positive integers $k$.

* To complete the inductive step of a proof using the principle of mathematical induction, we assume that $P(k)$ is true for an arbitrary positive integer $k$ and show that under this assumption, $P(k + 1)$ must also be true. The assumption that $P(k)$ is true is called the **inductive hypothesis**.
* Once we complete both steps in a proof by mathematical induction, we have shown that $P(n)$ is true for all positive integers $n$, that is, we have shown that $∀nP(n)$ is true where the quantiﬁcation is over the set of positive integers. In the inductive step, we show that $∀k(P(k) → P(k + 1))$ is true, where again, the domain is the set of positive integers.
* Expressed as a rule of inference, this proof technique can be stated as
	* $(P(1) ∧ ∀ k(P(k) → P(k + 1))) → ∀ nP(n)$,
	* when the domain is the set of positive integers.
* To prove that the conditional statement $P(k) → P(k + 1)$ is true for every positive integer $k$, we need to show that $P(k + 1)$ cannot be false when $P(k)$ is true. This can be accomplished by assuming that $P(k)$ is true and showing that under this hypothesis $P(k + 1)$ must also be true.
* **Remark**: In a proof by mathematical induction it is not assumed that $P(k)$ is true for all positive integers! It is only shown that if it is assumed that $P(k)$ is true, then $P(k + 1)$ is also true. Thus, a proof by mathematical induction is not a case of begging the question, or circular reasoning.

> [!Error] 5.1.5 Guidelines for Proofs by Mathematical Induction

* ***Template for Proofs by Mathematical Induction***
1. Express the statement that is to be proved in the form “for all $n \ge b$, $P(n)$” for a ﬁxed integer $b$. For statements of the form “$P(n)$ for all positive integers $n$,” let $b = 1$, and for statements of the form “$P(n)$ for all nonnegative integers $n$,” let $b = 0$. For some statements of the form $P(n)$, such as inequalities, you may need to determine the appropriate value of $b$ by checking the truth values of $P(n)$ for small values of $n$.
2. Write out the words “Basis Step.” Then show that $P(b)$ is true, taking care that the correct value of $b$ is used. This completes the ﬁrst part of the proof.
3. Write out the words “Inductive Step” and state, and clearly identify, the inductive hypothesis, in the form “Assume that $P(k)$ is true for an arbitrary ﬁxed integer $k \ge b$.”
4. State what needs to be proved under the assumption that the inductive hypothesis is true. That is, write out what $P(k + 1)$ says.
5. Prove the statement $P(k + 1)$ making use of the assumption $P(k)$. (Generally, this is the most diﬃcult part of a mathematical induction proof. Decide on the most promising proof strategy and look ahead to see how to use the induction hypothesis to build your proof of the inductive step. Also, be sure that your proof is valid for all integers $k$ with $k \ge b$, taking care that the proof works for small values of $k$, including $k = b$.)
6. Clearly identify the conclusion of the inductive step, such as by saying “This completes the inductive step.”
7. After completing the basis step and the inductive step, state the conclusion, namely, “By mathematical induction, $P(n)$ is true for all integers $n$ with $n \ge b$”.

> [!Error] 5.1.7 Examples of Proofs by Mathematical Induction

> [!Warning]
> Page 346 contains inductive proofs about algorithms, in particular, the greedy algorithm. Check it out.

> [!Warning]
> Also, the examples seemed important. I skimmed.

##### 5.2 Strong Induction and Well-Ordering
> `pg: 9`
> `time req: 59"`
> `time done: 30"`
>
> `questions: 43`
> `practice time req: 35"`

> [!Error] 5.2.1 Introduction

* **Strong Induction** can often be used when we cannot easily prove a result using mathematical induction.
* The inductive steps in these two proof methods are diﬀerent.
	* In a proof by mathematical induction, the inductive step shows that if the inductive hypothesis $P(k)$ is true, then $P(k + 1)$ is also true.
	* In a proof by strong induction, the inductive step shows that if $P(j)$ is true for all positive integers $j$ not exceeding $k$, then $P(k + 1)$ is true. That is, for the inductive hypothesis we assume that $P( j)$ is true for $j = 1, 2, … , k$.

> [!Error] 5.2.2 Strong Induction

> [!Info] Strong Induction
> To prove that $P(n)$ is true for all positive integers $n$, where $P(n)$ is a propositional function, we complete two steps:
> - **Basis Step**: We verify that the proposition $P(1)$ is true.
> - **Inductive Step**: We show that the conditional statement $[P(1) ∧ P(2) ∧ ⋯ ∧ P(k)] → P(k + 1)$ is true for all positive integers $k$.

* Note that when we use strong induction to prove that $P(n)$ is true for all positive integers $n$, our inductive hypothesis is the assumption that $P(j)$ is true for $j = 1, 2, … , k$. That is, the inductive hypothesis includes all $k$ statements $P(1), P(2), … , P(k)$.
* Because we can use all $k$ statements $P(1), P(2), … , P(k)$ to prove $P(k + 1)$, rather than just the statement $P(k)$ as in a proof by mathematical induction, strong induction is a more ﬂexible proof technique. Because of this, some mathematicians prefer to always use strong induction instead of mathematical induction, even when a proof by mathematical induction is easy to ﬁnd.

> [!Warning] Disclaimer: `terminology`
> Strong induction is sometimes called the **second principle of mathematical induction** or **complete induction**. When the terminology “complete induction” is used, the principle of mathematical induction is called **incomplete induction**, a technical term that is a somewhat unfortunate choice because there is nothing incomplete about the principle of mathematical induction; after all, it is a valid proof technique.

---
* **Strong Induction and the Infinite Ladder**
* To better understand strong induction, consider the inﬁnite ladder in Section 5.1. Strong induction tells us that we can reach all rungs if
	1. we can reach the ﬁrst rung, and
	2. for every positive integer $k$, if we can reach all the ﬁrst $k$ rungs, then we can reach the $(k + 1)$st rung.
---

> [!Warning]
> I skimmed the examples. They seemed important.

##### 5.3 Recursive Definitions and Structural Inductions
> `pg: 14`
> `time req: 1' 33"`
> `time done: 56"`
> `performance: 166%`
>
> `questions: 67`
> `practice time req: 54"`

> [!Error] 5.3.1 Introduction

* Sometimes it is diﬃcult to deﬁne an object explicitly. However, it may be easy to deﬁne this object in terms of itself. This process is called **recursion**.
* We can use recursion to deﬁne sequences, functions, and sets. 
* When we deﬁne a set recursively, we specify some initial elements in a basis step and provide a rule for constructing new elements from those we already have in the recursive step. To prove results about recursively deﬁned sets we use a method called structural induction.

> [!Error] 5.3.2 Recursively Defined Functions

* We use two steps to deﬁne a function with the set of nonnegative integers as its domain:
	* **Basis Step**: Specify the value of the function at zero.
	* **Recursive Step**: Give a rule for ﬁnding its value at an integer from its values at smaller integers.
* Such a deﬁnition is called a **recursive** or **inductive** deﬁnition
* Recursively deﬁned functions are **well deﬁned**. That is, for every positive integer, the value of the function at this integer is determined in an unambiguous way. This means that given any positive integer, we can use the two parts of the deﬁnition to ﬁnd the value of the function at that integer, and that we obtain the same value no matter how we apply the two parts of the deﬁnition. This is a consequence of the principle of mathematical induction.

> [!Info] Theorem 1: `Lamé's theorem`
> Let $a$ and $b$ be positive integers with $a \ge b$. Then the number of divisions used by the Euclidean algorithm to ﬁnd $gcd(a, b)$ is less than or equal to ﬁve times the number of decimal digits in $b$.

> [!Error] 5.3.3 Recursively Defined Sets and Structures

* Just as in the recursive deﬁnition of functions, recursive definitions of sets have two parts, a **basis step** and a **recursive step**.
	* In the basis step, an initial collection of elements is speciﬁed. In the recursive step, rules for forming new elements in the set from those already known to be in the set are provided.
	* Recursive deﬁnitions may also include an **exclusion rule**, which speciﬁes that a recursively deﬁned set contains nothing other than those elements speciﬁed in the basis step or generated by applications of the recursive step.
	* In our discussions, we will always tacitly assume that the exclusion rule holds and no element belongs to a recursively deﬁned set unless it is in the initial collection speciﬁed in the basis step or can be generated using the recursive step one or more times.
---
* Recursive deﬁnitions play an important role in the study of strings. A string over an alphabet $Σ$ is a ﬁnite sequence of symbols from $Σ$. We can deﬁne $Σ∗$, the set of strings over $Σ$, recursively.

> [!Info] Definition: $Σ∗$
> The set $Σ∗$ of strings over the alphabet $Σ$ is deﬁned recursively by
> - **Basis Step**: $𝜆 ∈ Σ∗$ (where $𝜆$ is the empty string containing no symbols).
> - **Recursive Step**: If $w ∈ Σ∗$ and $x ∈ Σ$, then $wx ∈ Σ∗$.

* The basis step of the recursive deﬁnition of strings says that the empty string belongs to $Σ∗$. The recursive step states that new strings are produced by adding a symbol from $Σ$ to the end of strings in $Σ∗$. At each application of the recursive step, strings containing one additional symbol are generated.

> [!Info] Definition: `string concatenation`
> Two strings can be combined via the operation of concatenation. Let $Σ$ be a set of symbols and $Σ∗$ the set of strings formed from symbols in $Σ$. We can deﬁne the concatenation of two strings, denoted by $⋅$, recursively as follows.
> - **Basis Step**: If $w ∈ Σ∗$ , then $w ⋅ 𝜆 = w$, where $𝜆$ is the empty string.
> - **Recursive Step**: If $w_1 ∈ Σ∗$ and $w_2 ∈ Σ∗$ and $x ∈ Σ$, then $w_1 ⋅ (w_2 x) = (w_1 ⋅ w_2 )x$.

* The concatenation of the strings $w_1$ and $w_2$ is often written as $w_1 w_2$ rather than $w_1 ⋅ w_2$ . By repeated application of the recursive deﬁnition, it follows that the concatenation of two strings $w_1$ and $w_2$ consists of the symbols in $w_1$ followed by the symbols in $w_2$ . For instance, the concatenation of $w_1 = abra$ and $w_2 = cadabra$ is $w_1 w_2 = abracadabra$.

> [!Warning]
> I skipped some subsections... they were mostly proofs, and boring and straightforward at that.

##### 5.4 Recursive Algorithms
> `pg: 11`
> `time req: 1' 13"`
> `time done: 15"`
> `performance: 486%`
>
> `questions: 55`
> `practice time req: 42"`

> [!Error] 5.4.1 Introduction

* Sometimes we can reduce the solution to a problem with a particular set of input values to the solution of the same problem with smaller input values.
* When such a reduction can be done, the solution to the original problem can be found with a sequence of reductions, until the problem has been reduced to some initial case for which the solution is known.
* We will see that algorithms that successively reduce a problem to the same problem with smaller input are used to solve a wide variety of problems.

> [!Info] Definition: `recursive algorithm`
> An algorithm is called *recursive* if it solves a problem by reducing it to an instance of the same problem with smaller input.

> [!Error] 5.4.2 Proving Recursive Algorithms Correct

* Mathematical induction, and its variant strong induction, can be used to prove that a recursive algorithm is correct, that is, that it produces the desired output for all possible input values.

> [!Error] 5.4.3 Recursion and Iteration

* A recursive deﬁnition expresses the value of a function at a positive integer in terms of the values of the function at smaller integers. This means that we can devise a recursive algorithm to evaluate a recursively deﬁned function at a positive integer. Instead of successively reducing the computation to the evaluation of the function at smaller integers, we can start with the value of the function at one or more integers, the base cases, and successively apply the recursive deﬁnition to ﬁnd the values of the function at successive larger integers. Such a procedure is called **iterative**. Often an iterative approach for the evaluation of a recursively deﬁned sequence requires much less computation than a procedure using recursion (unless special-purpose recursive machines are used).
* It is sometimes preferable to use a recursive procedure even if it is less eﬃcient than the iterative procedure. In particular, this is true when the recursive approach is easily implemented and the iterative approach is not. (Also, machines designed to handle recursion may be available that eliminate the advantage of using iteration.)

##### 5.5 Program Correctness
> `pg: 5`
> `time req: 33"`
> `time done: 52"`
> `performance: 63%`
>
> `questions: 13`
> `practice time req: 19"`

> [!Error] 5.5.1 Introduction

* Suppose that we have designed an algorithm to solve a problem and have written a program to implement it. How can we be sure that the program always produces the correct answer? After all the bugs have been removed so that the syntax is correct, we can test the program with sample input. It is not correct if an incorrect result is produced for any sample input. But even if the program gives the correct answer for all sample input, it may not always produce the correct answer (unless all possible input has been tested). We need a proof to show that the program always gives the correct output.
* Program veriﬁcation, the proof of correctness of programs, uses the rules of inference and proof techniques described in this chapter, including mathematical induction. Because an incorrect program can lead to disastrous results, a large amount of methodology has been constructed for verifying programs. Eﬀorts have been devoted to automating program veriﬁcation so that it can be carried out using a computer. However, only limited progress has been made toward this goal. Indeed, some mathematicians and theoretical computer scientists argue that it will never be realistic to mechanize the proof of correctness of complex programs.

> [!Error] 5.5.2 Program Verification

* A program is said to be **correct** if it produces the correct output for every possible input.
* A proof that a program is correct consists of two parts.
	* The ﬁrst part shows that the correct answer is obtained if the program terminates. This part of the proof establishes the **partial correctness** of the program.
	* The second part of the proof shows that the program always terminates.
* To specify what it means for a program to produce the correct output, two propositions are used.
	* The ﬁrst is the **initial assertion**, which gives the properties that the input values must have.
	* The second is the **ﬁnal assertion**, which gives the properties that the output of the program should have, if the program did what was intended.

> [!Info] Definition
> A program, or program segment, $S$ is said to be partially correct with respect to the initial assertion $p$ and the ﬁnal assertion $q$ if whenever $p$ is true for the input values of $S$ and $S$ terminates, then $q$ is true for the output values of $S$. The notation $p{S}q$ indicates that the program, or program segment, $S$ is partially correct with respect to the initial assertion $p$ and the ﬁnal assertion $q$.
>
> Note: The notation $p{S}q$ is known as a *Hoare triple*. Tony Hoare introduced the concept of partial correctness.

> [!Error] 5.5.3 Rules of Inference

* A useful rule of inference proves that a program is correct by splitting the program into a sequence of subprograms and then showing that each subprogram is correct.
* Suppose that the program $S$ is split into subprograms $S_1$ and $S_2$ . Write $S = S_1 ; S_2$ to indicate that $S$ is made up of $S_1$ followed by $S_2$ . Suppose that the correctness of $S_1$ with respect to the initial assertion $p$ and ﬁnal assertion $q$, and the correctness of $S_2$ with respect to the initial assertion $q$ and the ﬁnal assertion $r$, have been established. It follows that if $p$ is true and $S_1$ is executed and terminates, then $q$ is true; and if $q$ is true, and $S_2$ executes and terminates, then $r$ is true. Thus, if $p$ is true and $S = S_1 ; S_2$ is executed and terminates, then $r$ is true. This rule of inference, called the composition rule, can be stated as:

> > 	$$
\begin{flalign}
	\frac{
		\begin{flalign}\begin{array}[b]{r}
			p\{S_1\}q\\
			q\{S_2\}r
		\end{array}&&\end{flalign}
	}{
		\therefore p\{S_1;S_2\}r
	}&&
\end{flalign}
$$

> [!Error] 5.5.4 Conditional Statements

* Suppose that a program segment has the form \[$\mathbf{if}\ \mathit{condition}\ \mathbf{then}\ S$\] where $S$ is a block of statements. Then $S$ is executed if condition is true, and it is not executed when condition is false. To verify that this segment is correct with respect to the initial assertion $p$ and ﬁnal assertion $q$, two things must be done. First, it must be shown that when $p$ is true and condition is also true, then $q$ is true after $S$ terminates. Second, it must be shown that when $p$ is true and condition is false, then $q$ is true (because in this case $S$ does not execute).
* This leads to the following rule of inference:

>> 	$$
	\begin{flalign}
		\frac{
			\begin{flalign}\begin{array}[b]{r}
				(p\ ∧\ \mathit{condition})\{S\}q\\
				(p\ ∧\ ¬\mathit{condition}) → q
			\end{array}&&\end{flalign}
		}{
			\therefore p\{\mathbf{if}\ \mathit{condition}\ \mathbf{then}\ S\}q
		}&&
	\end{flalign}
	$$

* Similarly, suppose that a program has a statement of the form \[$\mathbf{if}\ \mathit{condition}\ \mathbf{then}\ S_1\ \mathbf{else}\ S_2$\]. If condition is true, then $S_1$ executes; if condition is false, then $S_2$ executes. To verify that this program segment is correct with respect to the initial assertion $p$ and the ﬁnal assertion $q$, two things must be done. First, it must be shown that when $p$ is true and condition is true, then $q$ is true after $S_1$ terminates. Second, it must be shown that when $p$ is true and condition is false, then $q$ is true after $S_2$ terminates. This leads to the following rule of inference:

 >> 	$$
	\begin{flalign}
		\frac{
			\begin{flalign}\begin{array}[b]{r}
				(p\ ∧\ \mathit{condition})\{S_1\}q\\
				(p\ ∧\ ¬\mathit{condition})\{S_2\}q
			\end{array}&&\end{flalign}
		}{
			\therefore p\{\mathbf{if}\ \mathit{condition}\ \mathbf{then}\ S_1\ \mathbf{else}\ S_2\}q
		}&&
	\end{flalign}
	$$

> [!Error] 5.5.5 Loop Invariants

* To develop a rule of inference for program segments of the type \[$\mathbf{while}\ \mathit{condition}\ S$\], note that $S$ is repeatedly executed until condition becomes false. An assertion that remains true each time $S$ is executed must be chosen. Such an assertion is called a loop invariant. In other words, $p$ is a loop invariant if $(p ∧ \mathit{condition})\{S\}p$ is true.
* Suppose that $p$ is a loop invariant. It follows that if $p$ is true before the program segment is executed, $p$ and $¬\mathit{condition}$ are true after termination, if it occurs. This rule of inference is

 >> 	$$
	\begin{flalign}
		\frac{
			\begin{flalign}(p\ ∧\ \mathit{condition})\{S\}p&&\end{flalign}
		}{
			\therefore p\{\mathbf{while}\ \mathit{condition}\ S\}(¬\mathit{condition}\ ∧\ p)
		}&&
	\end{flalign}
	$$

#### Chapter 6: The Basics of Counting
> [!Summary]
> `sum page: 47`
> `sum time req: 5' 9"`

* Combinatorics, the study of arrangements of objects, is an important part of discrete mathematics.

##### 6.1 The Basics of Counting
> `pg: 12`
> `time req: 1' 19"`
> `time done: 49"`
> `performance: 161%`
>
> `questions: 78`
> `questions done: 7`
> `practice time req: 46"`
> `pracice time done: 41"`
> `p-performance: 112%`

> [!Error] 6.1.2 Basic Counting Principles

> [!Info] The Product Rule
> Suppose that a procedure can be broken down into a sequence of two tasks. If there are $n_11$ ways to do the ﬁrst task and for each of these ways of doing the ﬁrst task, there are $n_2$ ways to do the second task, then there are $n_1 n_2$ ways to do the procedure.
>
> The product rule applies when a procedure is made up of separate tasks.
>
> > [!Info] The Extended Product Rule
> > An extended version of the product rule is often useful. Suppose that a procedure is carried out by performing the tasks $T_1, T_2, …, T_m$ in sequence. If each task $T_i$, $i = 1, 2, … , n$, can be done in $n_i$ ways, regardless of how the previous tasks were done, then there are $n_1 ⋅ n_2 ⋅ ⋯ ⋅ n_m$ ways to carry out the procedure.
> >
> > This version of the product rule can be proved by mathematical induction from the product rule for two tasks

> [!Info] The Sum Rule
> If a task can be done either in one of $n_1$ ways or in one of $n_2$ ways, where none of the set of $n_1$ ways is the same as any of the set of $n_2$ ways, then there are $n_1 + n_2$ ways to do the task.
>
> > [!Info] The Extended Sum Rule
> > We can extend the sum rule to more than two tasks. Suppose that a task can be done in one of $n_1$ ways, in one of $n_2$ ways, … , or in one of $n_m$ ways, where none of the set of $n_i$ ways of doing the task is the same as any of the set of $n_j$ ways, for all pairs $i$ and $j$ with $1 \le i \lt j \le m$. Then the number of ways to do the task is $n_1 + n_2 + ⋯ + n_m$.
> >
> > This version of the sum rule can be proved using mathematical induction from the sum rule for two sets.

> [!Error] 6.1.4 The Subtraction Rule

* Suppose that a task can be done in one of two ways, but some of the ways to do it are common to both ways. In this situation, we cannot use the sum rule to count the number of ways to do the task. If we add the number of ways to do the tasks in these two ways, we get an overcount of the total number of ways to do it, because the ways to do the task that are common to the two ways are counted twice.
* To correctly count the number of ways to do the two tasks, we must subtract the number of ways that are counted twice. This leads us to an important counting rule.

> [!Info] The Subtraction Rule
> If a task can be done in either $n_1$ ways or $n_2$ ways, then the number of ways to do the task is $n_1 + n_2$ minus the number of ways to do the task that are common to the two diﬀerent ways.

* The subtraction rule is also known as the **principle of inclusion–exclusion**, especially when it is used to count the number of elements in the union of two sets.

> [!Error] 6.1.5 The Division Rule

> [!Info] The Division Rule
> There are $n/d$ ways to do a task if it can be done using a procedure that can be carried out in $n$ ways, and for every way $w$, exactly $d$ of the $n$ ways correspond to way $w$.
>
> **Remark**: The division rule comes in handy when it appears that a task can be done in $n$ diﬀerent ways, but it turns out that for each way of doing the task, there are $d$ equivalent ways of doing it. Under these circumstances, we can conclude that there are $n/d$ inequivalent ways of doing the task.

> [!Warning] Example
> > Suppose that an automated system has been developed that counts the legs of cows in a pasture. Suppose that this system has determined that in a farmer’s pasture there are exactly $572$ legs. How many cows are there is this pasture, assuming that each cow has *four* legs and that there are no other animals present?
>
> **Solution**: Let $n$ be the number of cow legs counted in a pasture. Because each cow has four legs, by the division rule we know that the pasture contains $n/4$ cows. Consequently, the pasture with $572$ cow legs has $572/4 = 143$ cows in it.

> [!Question] ChatGPT
> > I was trying to solve a counting problem in discrete mathematics.
> > > How many integers less than 100 are divisible by 7?
> >
> > The answer was "$\lfloor\frac{100}{7}\rfloor$".
> >
> > Though I have no grasp of this method of counting. How did dividing $100$ by $7$ give us the number of integers divisible by $7$? 
>
> Certainly! The key to understanding this lies in recognizing that when you divide a range of integers by a divisor, the quotient gives you the count of integers that are divisible by that divisor.
> In this case, you want to find how many integers less than $100$ are divisible by $7$. When you divide $100$ by $7$, you get a quotient and a remainder. The **quotient** represents **how many times $7$ can fit into $100$ completely**, and the remainder represents what's left over.

> [!Error] 6.1.6 Tree Diagrams

* Counting problems can be solved using **tree diagrams**.
* A tree consists of a root, a number of branches leaving the root, and possible additional branches leaving the endpoints of other branches.
* To use trees in counting, we use a branch to represent each possible choice. We represent the possible outcomes by the leaves, which are the endpoints of branches not having other branches starting at them.
* Note that when a tree diagram is used to solve a counting problem, the number of choices of which branch to follow to reach a leaf can vary.

> [!Info] You can read 3 examples with Figures from the book.

##### 6.2 The Pigeonhole Principle
> `pg: 7`
> `time req: 46"`
> `time done: 55"`
> `performance: 83%`
>
> `questions: 49`
> `practice time req: 27"`

> [!Error] 6.2.1 Introduction

> [!Info] Theorem 1: The Pigeonhole Principle
> If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects.

> [!Info] Corollary 1
> A function $f$ from a set with $k + 1$ or more elements to a set with $k$ elements is not one-to-one.

> [!Example]
> 1. Among any group of $367$ people, there must be at least two with the same birthday, because there are only $366$ possible birthdays.
> 2. In any group of $27$ English words, there must be at least two that begin with the same letter, because there are $26$ letters in the English alphabet.
> 3. How many students must be in a class to guarantee that at least two students receive the same score on the ﬁnal exam, if the exam is graded on a scale from $0$ to $100$ points?
> 	- There are $101$ possible scores on the ﬁnal. The pigeonhole principle shows that among any $102$ students there must be at least $2$ students with the same score.

> [!Error] 6.2.2 The Generalized Pigeonhole Principle

* The pigeonhole principle states that there must be at least two objects in the same box when there are more objects than boxes. However, even more can be said when the number of objects exceeds a multiple of the number of boxes.

> [!Info] Theorem 2: `The Generalized Pigeonhole Principle`
> If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil\frac{N}{k}\rceil$ objects.

* A common type of problem asks for the minimum number of objects such that at least $r$ of these objects must be in one of $k$ boxes when these objects are distributed among the boxes.
	* When we have $N$ objects, the generalized pigeonhole principle tells us there must be at least $r$ objects in one of the boxes as long as $\lceil\frac{N}{k}\rceil \ge r$.
	* The smallest integer $N$ with $\frac{N}{k} > r − 1$, namely, $N = k(r − 1) + 1$, is the smallest integer satisfying the inequality $\lceil\frac{N}{k}\rceil \ge r$.
	* Could a smaller value of $N$ suﬃce? The answer is no, because if we had $k(r − 1)$ objects, we could put $r − 1$ of them in each of the $k$ boxes and no box would have at least $r$ objects.
* When thinking about problems of this type, it is useful to consider how you can avoid having at least $r$ objects in one of the boxes as you add successive objects. To avoid adding a $r$th object to any box, you eventually end up with $r − 1$ objects in each box. There is no way to add the next object without putting an $r$th object in that box.

> [!Example]
> 5. Among $100$ people there are at least $⌈100/12⌉ = 9$ who were born in the same month.
> 6. What is the minimum number of students required in a discrete mathematics class to be sure that at least six will receive the same grade, if there are ﬁve possible grades, $A$, $B$, $C$, $D$, and $F$?
> 	- The minimum number of students needed to ensure that at least six students receive the same grade is the smallest integer $N$ such that $⌈N/5⌉ = 6$. The smallest such integer is $N = 5 ⋅ 5 + 1 = 26$. If you have only $25$ students, it is possible for there to be ﬁve who have received each grade so that no six students have received the same grade. Thus, $26$ is the minimum number of students needed to ensure that at least six students will receive the same grade.

##### 6.3 Permutations and Combinations
> `pg: 7`
> `time req: 46"`
> `time done: 42"`
> `performance: 109%`
>
> `questions: 48`
> `practice time req: 27"`

> [!Error] 6.3.2 Permutations

* A **permutation** of a set of distinct objects is an ordered arrangement of these objects.
* An ordered arrangement of r elements of a set is called an **r-permutation**.
* The number of r-permutations of a set with n elements is denoted by $P(n, r)$. We can ﬁnd $P(n, r)$ using the product rule.

> [!Info] Theorem 1
> If $n$ is a positive integer and $r$ is an integer with $1 ≤ r ≤ n$, then there are
>
> - $P(n, r) = n(n − 1)(n − 2) ⋯ (n − r + 1)$
>
> r-permutations of a set with $n$ distinct elements.

* Note that $P(n, 0) = 1$ whenever $n$ is a nonnegative integer because there is exactly one way to order zero elements. That is, there is exactly one list with no elements in it, namely the empty list.

> [!Info] Corollary 1
> If $n$ and $r$ are integers with $0 ≤ r ≤ n$, then $P(n, r) = \frac{n!}{(n - r)!}$.

> [!Error] 6.3.3 Combinations

* An **r-combination** of elements of a set is an unordered selection of $r$ elements from the set. Thus, an r-combination is simply a subset of the set with $r$ elements.
* he number of r-combinations of a set with $n$ distinct elements is denoted by $C(n, r)$. Note that $C(n, r)$ is also denoted by $\binom{n}{r}$ and is called a **binomial coeﬃcient**.
* We can determine the number of r-combinations of a set with $n$ elements using the formula for the number of r-permutations of a set. To do this, note that the r-permutations of a set can be obtained by ﬁrst forming r-combinations and then ordering the elements in these combinations.

> [!Info] Theorem 2
> The number of r-combinations of a set with $n$ elements, where $n$ is a nonnegative integer and $r$ is an integer with $0 ≤ r ≤ n$, equals
>
> - $C(n, r) = \frac{n!}{r!(n - r)!}$
>
> > [!Proof]
> > The $P(n, r)$ r-permutations of the set can be obtained by forming the $C(n, r)$ r-combinations of the set, and then ordering the elements in each r-combination, which can be done in $P(r, r)$ ways. Consequently, by the product rule,
> >
> > - $P(n, r) = C(n, r) ⋅ P(r, r)$
> >
> > This implies that
> > 
> > - $C(n, r) = \frac{P(n, r)}{P(r, r)} = \frac{n!/(n - r)!}{r!/(r -r)!} = \frac{n!}{r!(n - r)!}$
>
> This formula, although explicit, is not helpful when $C(n, r)$ is computed for large values of $n$ and $r$. The reasons are that it is practical to compute exact values of factorials exactly only for small integer values, and when ﬂoating point arithmetic is used, the formula may produce a value that is not an integer. When computing $C(n, r)$, ﬁrst note that when we cancel out $(n − r)!$ from the numerator and denominator of the expression for $C(n, r)$, we obtain
>
> - $C(n, r) = \frac{n!}{r!(n - r)!} = \frac{n(n - 1)...(n - r + 1)}{r!}$.
>
> Consequently, to compute $C(n, r)$ you can cancel out all the terms in the larger factorial in the denominator from the numerator and denominator, then multiply all the terms that do not cancel in the numerator and ﬁnally divide by the smaller factorial in the denominator.

> [!Info] Corollary 2
> Let $n$ and $r$ be nonnegative integers with $r \le n$. Then $C(n, r) = C(n, n − r)$.

##### 6.4 Binomial Coefficients and Identities
> `pg: 7`
> `time req: 46"`
> `time done: 37"`
> `performance: 124%`
>
> `questions: 43`
> `practice time req: 27"`

* The number of r-combinations from a set with $n$ elements is often denoted by $\binom{n}{r}$ . This number is also called a **binomial coeﬃcient** because these numbers occur as coeﬃcients in the expansion of powers of binomial expressions such as $(a + b)^n$ . 

> [!Error] 6.4.1 The Binomial Theorem

> [!Info] Theorem 1: `The Binomial Theorem`
> Let x and y be variables, and let n be a nonnegative integer. Then
>
> $$(x + y)^n = \displaystyle\sum_{j=0}^{n} \binom{n}{j} x^{n - j} y^j = \binom{n}{0} x^n + \binom{n}{1} x^{n - 1} y + ... + \binom{n}{n - 1} x y^{n - 1} + \binom{n}{n} y^n$$

> [!Info] Corollary 1
> Let $n$ be a nonnegative integer. Then
>
> - $\displaystyle\sum_{k = 0}^{n} \binom{n}{k} = 2^n$

> [!Info] Corollary 2
> Let $n$ be a positive integer. Then
>
> - $\displaystyle\sum_{k = 0}^{n} (-1)^k \binom{n}{k} = 0$
> - $\binom{n}{0} + \binom{n}{2} + \binom{n}{4} + ... = \binom{n}{1} + \binom{n}{3} + \binom{n}{5} = ...$

> [!Info] Corollary 3
> Let $n$ be a nonnegative integer. Then
>
> - $\displaystyle\sum_{k = 0}^{n} 2^k \binom{n}{k} = 3^n$

> [!Error] 6.4.2 Pascal's Identity and Triangle

* The binomial coeﬃcients satisfy many diﬀerent identities. We introduce one of the most important of these now.

> [!Info] Theorem 2: `Pascal's Identity`
> Let $n$ and $k$ be positive integers with $n \ge k$. Then
>
> - $\binom{n + 1}{k} = \binom{n}{k - 1} + \binom{n}{k}$

> [!Error] 6.4.3 Other Identities Involving Binomial Coefficients

> [!Info] Theorem 3: `Vandermonde's Identity`
> Let $m$, $n$, and $r$ be nonnegative integers with $r$ not exceeding either $m$ or $n$. Then
>
> - $\binom{m + n}{r} = \displaystyle\sum_{k = 0}^{r} \binom{m}{r - k} \binom{n}{k}$

> [!Info] Corollary 4
> If $n$ is a nonnegative integer, then
>
> - $\binom{2n}{n} = \displaystyle\sum_{k = 0}^{n} \binom{n}{k}^2$

>[!Info] Theorem 4
> Let $n$ and $r$ be nonnegative integers with $r \le n$. Then
>
> - $\binom{n + 1}{r + 1} = \displaystyle\sum_{j = r}^{n} \binom{j}{r}$

##### 6.5 Generalized Permutations and Combinations
> `pg: 10`
> `time req: 1' 6"`
> `time done: 59"`
> `performance: 111%`
>
> `questions: 68`
> `practice time req: 39"`

> [!Error] 6.5.2 Permutations with Repetition

> [!Info] Theorem 1
> The number of r-permutations of a set of $n$ objects with repetition allowed is $n^r$.

> [!Error] 6.5.3 Combinations with Repetitions

> [!Info] Theorem 2
> There are $C(n + r − 1, r) = C(n + r − 1, n − 1)$ r-combinations from a set with n elements when repetition of elements is allowed.

> [!Example] Example 3
> > How many ways are there to select ﬁve bills from a cash box containing $\$1$ bills, $\$2$ bills, $\$5$ bills, $\$10$ bills, $\$20$ bills, $\$50$ bills, and $\$100$ bills? Assume that the order in which the bills are chosen does not matter, that the bills of each denomination are indistinguishable, and that there are at least ﬁve bills of each type.
>
> Because the order in which the bills are selected does not matter and seven diﬀerent types of bills can be selected as many as ﬁve times, this problem involves counting 5-combinations with repetition allowed from a set with seven elements. Listing all possibilities would be tedious, because there are a large number of solutions. Instead, we will illustrate the use of a technique for counting combinations with repetition allowed.
> Suppose that a cash box has seven compartments, one to hold each type of bill. These compartments are separated by six dividers. The choice of ﬁve bills corresponds to placing ﬁve markers in the compartments holding diﬀerent types of bills.
> The number of ways to select ﬁve bills corresponds to the number of ways to arrange six bars and ﬁve stars in a row with a total of $11$ positions. Consequently, the number of ways to select the ﬁve bills is the number of ways to select the positions of the ﬁve stars from the $11$ positions. This corresponds to the number of unordered selections of $5$ objects from a set of $11$ objects, which can be done in $C(11, 5)$ ways. Consequently, there are
>
> $C(11, 5) = \frac{11!}{5!6!} = 462$
>
> ways to choose ﬁve bills from the cash box with seven types of bills.

| Type | Repetition Allowed? | Formula |
| :-: | :-: | :-: |
| r-permutations | no | $n! / (n - r)!$ |
| r-combinations | no | $n! / r!(n - r)!$ |
| r-permutations | yes | $n^r$ |
| r-combinations | yes | $(n + r - 1)! / r!(n - 1)!$ |

> [!Error] 6.5.4 Permutations with Indistinguishable Objects

* Some elements may be indistinguishable in counting problems. When this is the case, care must be taken to avoid counting things more than once. Consider Example 7.

> [!Example] Example 7
> > How many diﬀerent strings can be made by reordering the letters of the word SUCCESS?
>
> Because some of the letters of SUCCESS are the same, the answer is not given by the number of permutations of seven letters. This word contains three Ss, two Cs, one U, and one E. To determine the number of diﬀerent strings that can be made by reordering the letters, ﬁrst note that the three Ss can be placed among the seven positions in $C(7, 3)$ diﬀerent ways, leaving four positions free. Then the two Cs can be placed in $C(4, 2)$ ways, leaving two free positions. The U can be placed in $C(2, 1)$ ways, leaving just one position free. Hence E can be placed in $C(1, 1)$ way. Consequently, from the product rule, the number of diﬀerent strings that can be made is $C(7, 3) ⋅ C(4, 2) ⋅ C(2, 1) ⋅ C(1, 1)$

> [!Info] Theorem 3
> The number of diﬀerent permutations of $n$ objects, where there are $n_1$ indistinguishable objects of type $1$, $n_2$ indistinguishable objects of type $2, … , and n_k$ indistinguishable objects of type $k$, is
>
> - $$\begin{flalign}\frac{n!}{n_1!n_2!...n_k!}&&\end{flalign}$$

> [!Error] 6.5.5 Distributing Objects into Boxes

* Many counting problems can be solved by enumerating the ways objects can be placed into boxes (where the order these objects are placed into the boxes does not matter).
	* The objects can be either *distinguishable*, that is, diﬀerent from each other, or *indistinguishable*, that is, considered identical.
		* Distinguishable objects are sometimes said to be *labeled*, whereas indistinguishable objects are said to be *unlabeled*.
	* Similarly, boxes can be *distinguishable*, that is, diﬀerent, or *indistinguishable*, that is, identical.
		* Distinguishable boxes are often said to be *labeled*, while indistinguishable boxes are said to be *unlabeled*.
	* When you solve a counting problem using the model of distributing objects into boxes, you need to determine whether the objects are distinguishable and whether the boxes are distinguishable.
	* Although the context of the counting problem makes these two decisions clear, counting problems are sometimes ambiguous and it may be unclear which model applies.
	* In such a case it is best to state whatever assumptions you are making and explain why the particular model you choose conforms to your assumptions.
---
* **Distinguishable Objects and Distinguishable Boxes**

> [!Example] Example 8
> > How many ways are there to distribute hands of $5$ cards to each of four players from the standard deck of $52$ cards?
>
> We will use the product rule to solve this problem. To begin, note that the ﬁrst player can be dealt $5$ cards in $C(52, 5)$ ways. The second player can be dealt $5$ cards in $C(47, 5)$ ways, because only $47$ cards are left. The third player can be dealt $5$ cards in $C(42, 5)$ ways. Finally, the fourth player can be dealt $5$ cards in $C(37, 5)$ ways. Hence, the total number of ways to deal four players $5$ cards each is
>
> - $$\begin{flalign}C(52, 5) ⋅ C(47, 5) ⋅ C(42, 5) ⋅ C(37, 5) = \frac{52!}{47!5!} ⋅ \frac{47!}{42!5!} ⋅ \frac{42!}{37!5!} ⋅ \frac{37!}{32!5!}&&\end{flalign}$$

> [!Info] Theorem 4
> The number of ways to distribute n distinguishable objects into $k$ distinguishable boxes so that $n_i$ objects are placed into box $i$, $i = 1, 2, … , k$, equals
>
> - $\begin{flalign}\frac{n!}{n_1! n_2! ... n_k!}&&\end{flalign}$

---
* **Indistinguishable Objects and Distinguishable Boxes**
* Counting the number of ways of placing $n$ indistinguishable objects into $k$ distinguishable boxes turns out to be the same as counting the number of n-combinations for a set with $k$ elements when repetitions are allowed.
* The reason behind this is that there is a one-to-one correspondence between n-combinations from a set with $k$ elements when repetition is allowed and the ways to place $n$ indistinguishable balls into $k$ distinguishable boxes.
* To set up this correspondence, we put a ball in the $i$th bin each time the $i$th element of the set is included in the $n$ combination.

> [!Example] Example 9
> > How many ways are there to place $10$ indistinguishable balls into eight distinguishable bins?
>
> The number of ways to place $10$ indistinguishable balls into eight bins equals the number of 10-combinations from a set with eight elements when repetition is allowed. Consequently, there are
>
> - $$\begin{flalign}C(8 + 10 − 1, 10) = C(17, 10) = \frac{17!}{10!7!} = 19,448&&\end{flalign}$$

* This means that there are $C(n + r − 1, n − 1)$ ways to place $r$ indistinguishable objects into $n$ distinguishable boxes.
---
> [!Warning] Disclaimer
> The other two types seemed useless, so I skipped.

##### 6.6 Generating Permutations and Combinations
> `pg: 4`
> `time req: 26"`
> `time done: 4"`
> `performance: 650%`
>
> `questions: 17`
> `practice time req: 15"`

> [!Info] Disclaimer
> This chapter is about the algorithms to generate the actual permutations and combinations of given sets. e.g. `itertools.combinations` and `itertools.permutations`.

#### Chapter 7: Discrete Probability
> [!Summary]
> `sum page: 43`
> `sum time req: 4' 43"`

##### 7.1 An Introduction to Discrete Probability
> `pg: 6`
> `time req: 39"`
> `time done: 29"`
> `performance: 134%`
>
> `questions: 45`
> `practice time req: 23"`

> [!Error] 7.1.2 Finite Probability

* An **experiment** is a procedure that yields one of a given set of possible outcomes. The **sample space** of the experiment is the set of possible outcomes. An **event** is a subset of the sample space.

> [!Info] Definition: `Laplace's definition of the probability of an event`
> If $S$ is a ﬁnite nonempty sample space of equally likely outcomes, and $E$ is an event, that is, a subset of $S$, then the probability of $E$ is $p(E) = \frac{|E|}{|S|}$.

* According to Laplace’s deﬁnition, the probability of an event is between $0$ and $1$.

> [!Error] 7.1.3 Probabilities of Complements and Unions of Events

* We can use counting techniques to ﬁnd the probability of events derived from other events.

> [!Info] Theorem 1
> Let $E$ be an event in a sample space $S$. The probability of the event $\bar{E} = S − E$, the complementary event of $E$, is given by
>
> - $$\begin{flalign}p(\bar{E}) = 1 - p(E)&&\end{flalign}$$

> [!Info] Theorem 2
> Let $E_1$ and $E_2$ be events in the sample space $S$. Then
>
> - $$\begin{flalign}p(E_1 ∪ E_2) = p(E_1) + p(E_2) − p(E_1 ∩ E_2)&&\end{flalign}$$

##### 7.2 Probability Theory
> `pg: 15`
> `time req: 1' 39"`
> `time done: 1' 35"`
> `performance: 104%`
>
> `questions: 41`
> `practice time req: 58"`

> [!Error] 7.2.2 Assigning Probabilities

* Let $S$ be the sample space of an experiment with a ﬁnite or countable number of outcomes. We assign a probability $p(s)$ to each outcome $s$. We require that two conditions be met:
	* $(i)\ 0 \le p(s) \le 1$ for each $s \in S$
	* and
	* $(ii)\ \displaystyle\sum_{s \in S} p(s) = 1$.
* Condition $(i)$ states that the probability of each outcome is a nonnegative real number no greater than $1$. Condition $(ii)$ states that the sum of the probabilities of all possible outcomes should be $1$; that is, when we do the experiment, it is a certainty that one of these outcomes occurs. Indeed, conditions $(i)$ and $(ii)$ are met when Laplace’s deﬁnition of probabilities of equally likely outcomes is used and $S$ is ﬁnite.
* To model an experiment, the probability $p(s)$ assigned to an outcome $s$ should equal the limit of the number of times $s$ occurs divided by the number of times the experiment is performed, because this number grows without bound. (We will assume that all experiments discussed have outcomes that are predictable on the average, so that this limit exists. We also assume that the outcomes of successive trials of an experiment do not depend on past results.)

> [!Info] Definition
> Suppose that $S$ is a set with $n$ elements. The *uniform distribution* assigns the probability $1/n$ to each element of $S$.

> [!Info] Definition
> The probability of the event $E$ is the sum of the probabilities of the outcomes in $E$. That is,
>
> - $$\begin{flalign}p(E) = \displaystyle\sum_{s \in E} p(s)&&\end{flalign}$$ 

* Note that when there are $n$ outcomes in the event $E$, that is, if $E = {a_1, a_2, …, a_n}$, then $p(E) = \sum_{i=1}^{n} p(a_i)$. Note also that the uniform distribution assigns the same probability to an event that Laplace’s original deﬁnition of probability assigns to this event. The experiment of selecting an element from a sample space with a uniform distribution is called selecting an element of $S$ **at random**.

> [!Error] 7.2.3 Probabilities of Complements and Unions of Events

> [!Info] Theorem 1
> If $E_1, E_2, …$ is a sequence of pairwise disjoint events in a sample space $S$, then
>
> - $$\begin{flalign}p\Bigg(\bigcup_{i} E_i\Bigg) = \displaystyle\sum_{i} p(E_i)&&\end{flalign}$$
>
> (Note that this theorem applies when the sequence $E_1, E_2, …$ consists of a ﬁnite number or a countably inﬁnite number of pairwise disjoint events.)

> [!Error] 7.2.4 Conditional Probability

> [!Info] Definition
> Let $E$ and $F$ be events with $p(F) > 0$. The conditional probability of $E$ given $F$, denoted by $p(E ∣ F)$, is deﬁned as
>
> - $$\begin{flalign}p(E ∣ F) = \frac{p(E \cap F)}{p(F)}&&\end{flalign}$$

> [!Error] 7.2.5 Independence

* Suppose a coin is ﬂipped three times. Does knowing that the ﬁrst ﬂip comes up tails (event $F$) alter the probability that tails comes up an odd number of times (event $E$)? In other words, is it the case that $p(E ∣ F) = p(E)$?
* This equality is valid for the events $E$ and $F$, because $p(E ∣ F) = 1/2$ and $p(E) = 1/2$. Because this equality holds, we say that $E$ and $F$ are **independent events**. When two events are independent, the occurrence of one of the events gives no information about the probability that the other event occurs.

> [!Info] Definition
> The events $E$ and $F$ are independent if and only if $p(E ∩ F) = p(E)p(F)$.

> [!Info] Definition
> The events $E_1, E_2, …, E_n$ are pairwise independent if and only if $p(E_i ∩ E_j) = p(E_i)p(E_j)$ for all pairs of integers $i$ and $j$ with $1 \le i < j \le n$. These events are mutually independent if $p(E_{i_1} ∩ E_{i_2} ∩ ⋯ ∩ E_{i_m}) = p(E_{i_1})p(E_{i_2}) ⋯ p(E_{i_m})$ whenever $i_j, j = 1, 2, … , m$, are integers with $1 \le i_1 \lt i_2 \lt ⋯ \lt i_m \le n$ and $m \ge 2$.

> [!Error] 7.2.6 Bernoulli Trials and the Binomial Distribution

* Suppose that an experiment can have only two possible outcomes. For instance, when a bit is generated at random, the possible outcomes are 0 and 1. When a coin is ﬂipped, the possible outcomes are heads and tails. Each performance of an experiment with two possible outcomes is called a **Bernoulli trial**. In general, a possible outcome of a Bernoulli trial is called a **success** or a **failure**. If $p$ is the probability of a success and $q$ is the probability of a failure, it follows that $p + q = 1$.
* Many problems can be solved by determining the probability of $k$ successes when an experiment consists of $n$ mutually independent Bernoulli trials. (Bernoulli trials are mutually independent if the conditional probability of success on any given trial is $p$, given any information whatsoever about the outcomes of the other trials.)

> [!Example] Example 8
> > A coin is biased so that the probability of heads is $2/3$. What is the probability that exactly four heads come up when the coin is ﬂipped seven times, assuming that the ﬂips are independent?
>
> There are $27 = 128$ possible outcomes when a coin is ﬂipped seven times. The number of ways four of the seven ﬂips can be heads is $C(7, 4)$. Because the seven ﬂips are independent, the probability of each of these outcomes (four heads and three tails) is $(2/3)^4$ $(1/3)^3$ . Consequently, the probability that exactly four heads appear is
>
> - $$\begin{flalign}C(7, 4)(2/3)^4(1/3)^3 = \frac{35 ⋅ 16}{3^7}&&\end{flalign}$$

> [!Info] Theorem 2
> The probability of exactly $k$ successes in $n$ independent Bernoulli trials, with probability of success $p$ and probability of failure $q = 1 − p$, is
>
> - $$\begin{flalign}C(n, k)p^kq^{n-k}&&\end{flalign}$$
>
> We denote by $b(k; n, p)$ the probability of $k$ successes in $n$ independent Bernoulli trials with probability of success $p$ and probability of failure $q = 1 − p$. Considered as a function of $k$, we call this function the **binomial distribution**.

* Note that the sum of the probabilities that there are $k$ successes when $n$ independent Bernoulli trials are carried out, for $k = 0, 1, 2, … , n$, equals
* $\displaystyle\sum_{k = 0}^{n} C(n, k)p^kq^{n -k} = (p + q)^n = 1$
* as should be the case. The ﬁrst equality in this string of equalities is a consequence of the binomial theorem. The second equality follows because $q = 1 − p$.

> [!Error] 7.2.7 Random Variables

> [!Info] Definition: `random variable`
> A *random variable* is a function from the sample space of an experiment to the set of real numbers. That is, a random variable assigns a real number to each possible outcome.

> [!Info] Definition
> The distribution of a random variable $X$ on a sample space $S$ is the set of pairs $(r, p(X = r))$ for all $r ∈ X(S)$, where $p(X = r)$ is the probability that $X$ takes the value $r$. (The set of pairs in this distribution is determined by the probabilities $p(X = r)$ for $r ∈ X(S)$.)

##### 7.3 Bayes' Theorem
> `pg: 7`
> `time req: 46"`
> `time done: 41"`
> `performance: 112%`
>
> `questions: 23`
> `practice time req: 27"`

> [!Error] 7.3.2 Bayes' Theorem

* We illustrate the idea behind Bayes’ theorem with an example that shows that when extra information is available, we can derive a more realistic estimate that a particular event occurs. That is, suppose we know $p(F)$, the probability that an event $F$ occurs, but we have knowledge that an event $E$ occurs. Then the conditional probability that $F$ occurs given that $E$ occurs, $p(F ∣ E)$, is a more realistic estimate than $p(F)$ that $F$ occurs.

> [!Example] Example 1
> > We have two boxes. The ﬁrst contains two green balls and seven red balls; the second contains four green balls and three red balls. Bob selects a ball by ﬁrst choosing one of the two boxes at random. He then selects one of the balls in this box at random. If Bob has selected a red ball, what is the probability that he selected a ball from the ﬁrst box?
>
> Let $E$ be the event that Bob has chosen a red ball; $\bar{E}$ is the event that Bob has chosen a green ball. Let $F$ be the event that Bob has chosen a ball from the ﬁrst box; $F$ is the event that Bob has chosen a ball from the second box. We want to ﬁnd $p(F ∣ E)$, the probability that the ball Bob selected came from the ﬁrst box, given that it is red. By the deﬁnition of conditional probability, we have $p(F ∣ E) = p(F ∩ E)/p(E)$. Can we use the information provided to determine both $p(F ∩ E)$ and $p(E)$ so that we can ﬁnd $p(F ∣ E)$?
> First, note that because the ﬁrst box contains seven red balls out of a total of nine balls, we know that $p(E ∣ F) = 7/9$. Similarly, because the second box contains three red balls out of a total of seven balls, we know that $p(E ∣ \bar{F}) = 3/7$. We assumed that Bob selects a box at random, so $p(F) = p(\bar{F}) = 1/2$. Because $p(E ∣ F) = p(E ∩ F)/p(F)$, it follows that $p(E ∩ F) = p(E ∣ F)p(F) = \frac{7}{9} ⋅ \frac{1}{2} = \frac{7}{18}$ \[as we remarked earlier, this is one of the quantities we need to ﬁnd to determine $p(F ∣ E)$]\. Similarly, because $p(E ∣ \bar{F}) = p(E ∩ \bar{F})/p(\bar{F})$, it follows that $p(E ∩ \bar{F}) = p(E ∣ \bar{F})p(\bar{F}) = \frac{3}{7} ⋅ \frac{1}{2} = \frac{3}{14}$.
> We can now ﬁnd $p(E)$. Note that $E = (E ∩ F) ∪ (E ∩ \bar{F})$, where $E ∩ F$ and $E ∩ \bar{F}$ are disjoint sets. (If $x$ belongs to both $E ∩ F$ and $E ∩ \bar{F}$, then $x$ belongs to both $F$ and $\bar{F}$, which is impossible.) It follows that
>
> - $$\begin{flalign}p(E) = p(E ∩ F) + p(E ∩ \bar{F}) = \frac{7}{18} + \frac{3}{14} = \frac{49}{126} + \frac{27}{126} = \frac{76}{126} = \frac{38}{63}&&\end{flalign}$$
>
> We have now found both $p(F ∩ E) = 7/18$ and $p(E) = 38/63$. We conclude that
>
> - $$\begin{flalign}p(F | E ) = \frac{p(F ∩ E)}{p(E)} = \frac{7/18}{38/63} = \frac{49}{76} ≈ 0.645&&\end{flalign}$$
>
> Before we had any extra information, we assumed that the probability that Bob selected the ﬁrst box was $1/2$. However, with the extra information that the ball selected at random is red, this probability has increased to approximately $0.645$. That is, the probability that Bob selected a ball from the ﬁrst box increased from $1/2$, when no extra information was available, to $0.645$ once we knew that the ball selected was red.

> [!Info] Theorem 1: `Bayes' Theorem`
> Suppose that $E$ and $F$ are events from a sample space $S$ such that $p(E) ≠ 0$ and $p(F) ≠ 0$. Then
>
> - $$\begin{flalign}p(F | E) = \frac{p(E | F)p(F)}{p(E | F)p(F) + p(E | \bar{F})p(\bar{F})}&&\end{flalign}$$

---
* Note that in the statement of Bayes’ theorem, the events $F$ and $F$ are mutually exclusive and cover the entire sample space $S$ (that is, $F ∪ \bar{F} = S$). We can extend Bayes’ theorem to any collection of mutually exclusive events that cover the entire sample space $S$, in the following way.

> [!Info] Theorem 2: `Generalized Bayes' Theorem`
> Suppose that $E$ is an event from a sample space $S$ and that $F_1, F_2, …, F_n$ are mutually exclusive events such that $\bigcup_{i=1}^{n} F_i = S$. Assume that $p(E) ≠ 0$ and $p(F_i) ≠ 0$ for $i = 1, 2, … , n$. Then
>
> - $$\begin{flalign}p(F_j | E) = \frac{p(E | F_j)p(F_j)}{\sum_{i=1}^{n} p(E | F_i)p(F_i)}&&\end{flalign}$$

##### 7.4 Expected Value and Variance
> `pg: 15`
> `time req: 1' 39"`
> `time done: 1' 15"`
> `performance: 132%`
>
> `questions: 49`
> `practice time req: 58"`

> [!Error] 7.4.1 Introduction

* The **expected value** of a random variable is the sum over all elements in a sample space of the product of the probability of the element and the value of the random variable at this element. Consequently, the expected value is a weighted average of the values of a random variable. The expected value of a random variable provides a central point for the distribution of values of this random variable. We can solve many problems using the notion of the expected value of a random variable, such as determining who has an advantage in gambling games and computing the average-case complexity of algorithms. Another useful measure of a random variable is its **variance**, which tells us how spread out the values of this random variable are. We can use the variance of a random variable to help us estimate the probability that a random variable takes values far removed from its expected value.

> [!Error] 7.4.2 Expected Value

> [!Info] Definition: `expected value`
> The expected value, also called the *expectation* or *mean*, of the random variable $X$ on the sample space $S$ is equal to
>
> - $$\begin{flalign}E(X) = \displaystyle\sum_{s \in S} p(s)X(s)&&\end{flalign}$$
>
> The deviation of $X$ at $s ∈ S$ is $X(s) − E(X)$, the diﬀerence between the value of $X$ and the mean of $X$.

* When an experiment has relatively few outcomes, we can compute the expected value of a random variable directly from its deﬁnition. However, when an experiment has a large number of outcomes, it may be inconvenient to compute the expected value of a random variable directly from its deﬁnition. Instead, we can ﬁnd the expected value of a random variable by grouping together all outcomes assigned the same value by the random variable.

> [!Info] Theorem 1
> If $X$ is a random variable and $p(X = r)$ is the probability that $X = r$, so that $p(X = r) = \sum_{s \in S, X(s)=r} p(s)$, then
>
> - $$\begin{flalign}E(X) = \sum_{r \in X(S)} p(X = r)r&&\end{flalign}$$
>
> > [!Warning] I did not understand this at all!

> [!Info] Theorem 2
> The expected number of successes when $n$ mutually independent Bernoulli trials are performed, where $p$ is the probability of success on each trial, is $np$.

> [!Error] 7.4.3 Linearity of Expectations

> [!Info] Theorem 3
> If $X_i , i = 1, 2, … , n$ with $n$ a positive integer, are random variables on $S$, and if $a$ and $b$ are real numbers, then
>
> - $$\begin{flalign}(i)\ E(X_1 + X_2 + ... + X_n) = E(X_1) + E(X_2) + ... E(X_n)&&\end{flalign}$$
> - $$\begin{flalign}(ii)\ E(aX + b) = aE(X) + b&&\end{flalign}$$

> [!Error] 7.4.4 Average-Case Computational Complexity

* Computing the average-case computational complexity of an algorithm can be interpreted as computing the expected value of a random variable. Let the sample space of an experiment be the set of possible inputs $a_j, j = 1, 2, … , n$, and let $X$ be the random variable that assigns to $a_j$ the number of operations used by the algorithm when given $a_j$ as input. Based on our knowledge of the input, we assign a probability $p(a_j)$ to each possible input value $a_j$. Then, the average-case complexity of the algorithm is
$$\begin{flalign}E(X) = \displaystyle\sum_{j=1}^{n} p(a_j)X(a_j)&&\end{flalign}$$
* This is the expected value of X.
* Finding the average-case computational complexity of an algorithm is usually much more diﬃcult than ﬁnding its worst-case computational complexity, and often involves the use of sophisticated methods. However, there are some algorithms for which the analysis required to ﬁnd the average-case computational complexity is not diﬃcult.

> [!Error] 7.4.5 The Geometric Distribution

* We now turn our attention to a random variable with inﬁnitely many possible outcomes.
* The random variable X that equals the number of ﬂips expected before a coin comes up tails is an example of a random variable with a **geometric distribution**.

> [!Info] Definition
> A random variable $X$ has a geometric distribution with parameter $p$ if $p(X = k) = (1 − p)^{k−1} p$ for $k = 1, 2, 3, …, \infty$ where $p$ is a real number with $0 ≤ p ≤ 1$.

* Geometric distributions arise in many applications because they are used to study the time required before a particular event happens, such as the time required before we ﬁnd an object with a certain property, the number of attempts before an experiment succeeds, the number of times a product can be used before it fails, and so on.

> [!Info] Theorem 4
> If the random variable $X$ has the geometric distribution with parameter $p$, then $E(X) = 1/p$.

> [!Error] 7.4.6 Independent Random Variables

* We have already discussed independent events. We will now deﬁne what it means for two random variables to be independent.

> [!Info] Definition
> The random variables $X$ and $Y$ on a sample space $S$ are *independent* if
>
> - $$\begin{flalign}p(X = r_1 and Y = r_2) = p(X = r_1) ⋅ p(Y = r_2)&&\end{flalign}$$
>
> or in words, if the probability that $X = r_1$ and $Y = r_2$ equals the product of the probabilities that $X = r_1$ and $Y = r_2$ , for all real numbers $r_1$ and $r_2$.

> [!Info] Theorem 5
> If $X$ and $Y$ are independent random variables on a sample space $S$, then $E(XY) = E(X)E(Y)$.

> [!Error] 7.4.7 Variance

> [!Info] Definition: `variance`
> Let $X$ be a random variable on a sample space $S$. The variance of $X$, denoted by $V(X)$, is
>
> - $$\begin{flalign}V(X) = \displaystyle\sum_{s \in S} (X(s) - E(X))^2 p(s)&&\end{flalign}$$
>
> That is, $V(X)$ is the weighted average of the square of the deviation of $X$. The standard deviation of $X$, denoted $𝜎(X)$, is deﬁned to be $\sqrt{V(X)}$.

> [!Info] Theorem 6
> If $X$ is a random variable on a sample space $S$, then $V(X) = E(X^2) − E(X)^2$.

> [!Info] Corollary 1: `theorem 3 + theorem 6`
> If $X$ is a random variable on a sample space $S$ and $E(X) = 𝜇$, then $V(X) = E((X − 𝜇)^2)$.

> [!Info] Theorem 7: `bienaymé’s formula`
> If $X$ and $Y$ are two independent random variables on a sample space $S$, then $V(X + Y) = V(X) + V(Y)$. Furthermore, if $X_i$ , $i = 1, 2, … , n$, with $n$ a positive integer, are pairwise independent random variables on $S$, then $V(X_1 + X_2 + ⋯ + X_n ) = V(X_1) + V(X_2) + ⋯ + V(X_n)$.

> [!Error] 7.4.8 Chebyshev's Inequality

* How likely is it that a random variable takes a value far from its expected value? Chebyshev’s inequality, helps answer this question by providing an upper bound on the probability that the value of a random variable diﬀers from the expected value of the random variable by more than a speciﬁed amount.

> [!Info] Theorem 8: `Chebyshev's Inequality`
> Let $X$ be a random variable on a sample space $S$ with probability function $p$. If $r$ is a positive real number, then
>
> - $$\begin{flalign}p(|X(s) - E(X)| \ge r) \le V(X)/r^2&&\end{flalign}$$

#### Chapter 8: Advanced Counting Techniques
> [!Summary]
> `sum page: 53`
> `sum time req: 5' 49"`

##### 8.1 Applications of Recurrence Relations
> `pg: 10`
> `time req: 1' 6"`
> `time done: 34"`
> `performance: 194%`
>
> `questions: 57`
> `practice time req: 39"`

##### 8.2 Solving Linear Recurrence Relations
> `pg: 11`
> `time req: 1' 13"`
> `time done: 1' 13"`
> `performance: 100%`
> `questions: 53`
> `practice time req: 42"`

> [!Error] 8.2.1 Introduction

> [!Info] Definition
> A *linear homogeneous recurrence relation* of degree $k$ with constant coeﬃcients is a recurrence relation of the form
>
> - $$\begin{flalign}a_n = c_1a_{n-1} + c_2a_{n-2} + ... + c_ka_{n-k}&&\end{flalign}$$
>
> where $c_1, c_2, …, c_k$ are real numbers, and $c_k ≠ 0$.

* The recurrence relation in the deﬁnition is **linear** because the right-hand side is a sum of previous terms of the sequence each multiplied by a function of $n$. The recurrence relation is **homogeneous** because no terms occur that are not multiples of the $a_j$s. The coeﬃcients of the terms of the sequence are all **constants**, rather than functions that depend on $n$. The **degree** is $k$ because an is expressed in terms of the previous $k$ terms of the sequence.

> [!Example] Example 2
> The recurrence relation $a_n = a_{n−1} + a_{n−2}^2$ is not linear. The recurrence relation $H_n = 2H_{n−1} + 1$ is not homogeneous. The recurrence relation $B_n = nB_{n−1}$ does not have constant coeﬃcients.

* Linear homogeneous recurrence relations are studied for two reasons. 
	* First, they often occur in modelling of problems.
	* Second, they can be systematically solved.

> [!Error] 8.2.2 solving Linear Homogeneous Recurrence Relations with Constant Coefficients

* Recurrence relations may be diﬃcult to solve, but fortunately this is not the case for linear homogenous recurrence relations with constant coeﬃcients. We can use two key ideas to ﬁnd all their solutions. **First**, these recurrence relations have solutions of the form $a_n = r^n$ , where $r$ is a constant. To see this, observe that $a_n = r^n$ is a solution of the recurrence relation $a_n = c_1 a_{n−1} + c_2 a_{n−2} + ⋯ + c_k a_{n−k}$ if and only if
	* $$\begin{flalign}r^n = c_1 r^{n - 1} + c_2 r^{n - 2} + ... + c_k r^{n - k}&&\end{flalign}$$
* When both sides of this equation are divided by $r^{n−k}$ (when $r ≠ 0$) and the right-hand side is subtracted from the left, we obtain the equation
	* $$\begin{flalign}r^k - c_1 r^{k - 1} - c_2 r^{k - 2} - ... - c_{k - 1} r - c_k = 0&&\end{flalign}$$
* Consequently, the sequence $\{a_n\}$ with $a_n = r^n$ where $r ≠ 0$ is a solution if and only if $r$ is a solution of this last equation. We call this the characteristic equation of the recurrence relation. The solutions of this equation are called the characteristic roots of the recurrence relation. As we will see, these characteristic roots can be used to give an explicit formula for all the solutions of the recurrence relation.
* The other key observation is that a linear combination of two solutions of a linear homogeneous recurrence relation is also a solution. To see this, suppose that $s_n$ and $t_n$ are both solutions of $a_n = c_1 a_{n−1} + c_2 a_{n−2} + ⋯ + c_k a_{n−k}$. Then
	* $$\begin{flalign}s_n = c_1 s_{n - 1} + c_2 s_{n - 2} + ... + c_k s_{n - k}&&\end{flalign}$$
* and
	* $$\begin{flalign}t_n = c_1 t_{n-1} + c_2 t_{n-2} + ... + c_k s_{n-k}&&\end{flalign}$$
* Now suppose that b1 and b2 are real numbers. Then
$$\begin{flalign}b_1 s_n + b_2 t_n = b_1 (c_1 s_{n-1} + c_2s_{n-2} + ... c_ks_{n-k}) + b_2(c_1t_{n-1} + c_2t_{n-2} + ... + c_kt_{n-k})&&\end{flalign}$$
$$\begin{flalign}= c_1(b_1s_{n−1} + b_2 t_{n−1}) + c_2(b_1 s_{n−2} + b_2 t_{n−2}) + ⋯ + c_k (b_1 s_{n−k} + b_k t_{n−k} )&&\end{flalign}$$
* This means that $b_1 s_n + b_2 t_n$ is also a solution of the same linear homogeneous recurrence relation.
* Using these key observations, we will show how to solve linear homogeneous recurrence relations with constant coeﬃcients.
---
* **The Degree Two Case**: We now turn our attention to linear homogeneous recurrence relations of degree two. First, consider the case when there are two distinct characteristic roots.

> [!Info] Theorem 1
> Let $c_1$ and $c_2$ be real numbers. Suppose that $r^2 − c_1 r − c_2 = 0$ has two distinct roots $r_1$ and $r_2$ . Then the sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1 a_{n−1} + c_2 a_{n−2}$ if and only if $a_n = 𝛼_1 r_1^n + 𝛼_2 r_2^n$ for $n = 0, 1, 2, …$, where $𝛼_1$ and $𝛼_2$ are constants.

* Theorem 1 does not apply when there is one characteristic root of multiplicity two. If this happens, then $a_n = nr_0^n$ is another solution of the recurrence relation when $r_0$ is a root of multiplicity two of the characteristic equation. Theorem 2 shows how to handle this case.

> [!Info] Theorem 2
> Let $c_1$ and $c_2$ be real numbers with $c_2 ≠ 0$. Suppose that $r^2 − c_1 r − c_2 = 0$ has only one root $r_0$ . A sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = c_1 a_{n−1} + c_2 a_{n−2}$ if and only if $a_n = 𝛼_1 r_0^n + 𝛼_2 nr_0^n$, for $n = 0, 1, 2, …$ , where $𝛼_1$ and $𝛼_2$ are constants.

---
* **The General Case**: We will now state the general result about the solution of linear homogeneous recurrence relations with constant coeﬃcients, where the degree may be greater than two, under the assumption that the characteristic equation has distinct roots.

> [!Info] Theorem 3
> Let $c_1, c_2, …, c_k$ be real numbers. Suppose that the characteristic equation
>
> - $r^k - c_1 - ... c_k = 0$
>
> has $k$ distinct roots $r_1, r_2, …, r_k$. Then a sequence $\{a_n\}$ is a solution of the recurrence relation
>
> - $a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}$
>
> if and only if
>
> - $a_n = 𝛼_1 r_1^n + 𝛼_2 r_2^n + ... + 𝛼_k r_k^n$
>
> for $n = 0, 1, 2, …$ , where $𝛼_1, 𝛼_2, …, 𝛼_k$ are constants.

* We now state the most general result about linear homogeneous recurrence relations with constant coeﬃcients, allowing the characteristic equation to have multiple roots. The key point is that for each root r of the characteristic equation, the general solution has a summand of the form $P(n)r^n$, where $P(n)$ is a polynomial of degree $m − 1$, with $m$ the multiplicity of this root.

> [!Info] Theorem 4
> Let $c_1, c_2, …, c_k$ be real numbers. Suppose that the characteristic equation
>
> - $r^k − c_1 r^{k−1} − ⋯ − c_k = 0$
>
> has $t$ distinct roots $r_1, r_2, …, r_t$ with multiplicities $m_1, m_2, …, m_t$, respectively, so that $m_i ≥ 1$ for $i = 1, 2, … , t$ and $m_1 + m_2 + ⋯ + m_t = k$. Then a sequence $\{a_n\}$ is a solution of the recurrence relation
>
> - $a_n = c_1 a_{n−1} + c_2 a_{n−2} + ⋯ + c_k a_{n−k}$
>
> if and only if
>
> - $a_n = (𝛼_{1,0} + 𝛼_{1,1}n + ⋯ + 𝛼_{1,m_1-1} n^{m_1−1})r_1^n$
> 	- $+ (𝛼_{2,0} + 𝛼_{2,1}n + ⋯ + 𝛼_{2,m_2−1}n^{m_2−1})r_2^n$
> 	- $+ ⋯ + (𝛼_{t,0} + 𝛼_{t,1} n + ⋯ + 𝛼_{t,m_t−1} n^{m_t−1})r_t^n$
>
> for $n = 0, 1, 2, …$, where $𝛼_{i,j}$ are constants for $1 ≤ i ≤ t$ and $0 ≤ j ≤ m_i − 1$.

> [!Error] 8.2.3 Linear Nonhomogeneous Recurrence Relations with Constant Coefficients

> [!Example] Example 9
> Each of the recurrence relations $a_n = a_{n−1} + 2^n$, $a_n = a_{n−1} + a_{n−2} + n^2 + n + 1$, $a_n = 3a_{n−1} + n3^n$, and $a_n = a_{n−1} + a_{n−2} + a_{n−3} + n!$ is a linear nonhomogeneous recurrence relation with constant coeﬃcients. The associated linear homogeneous recurrence relations are $a_n = a_{n−1}$, $a_n = a_{n−1} + a_{n−2}$, $a_n = 3a_{n−1}$, and $a_n = a_{n−1} + a_{n−2} + a_{n−3}$ , respectively.

> [!Info] Theorem 6
> Suppose that $\{a_n\}$ satisﬁes the linear nonhomogeneous recurrence relation
>
> - $a_n = c_1 a_{n−1} + c_2 a_{n−2} + ⋯ + c_k a_{n−k} + F(n),$
>
> where $c_1, c_2, …, c_k$ are real numbers, and
>
> - $F(n) = (b_t n^t + b_{t−1} n^{t−1} + ⋯ + b_1 n + b_0)s^n,$
>
> where $b_0, b_1, …, b_t$ and $s$ are real numbers. When $s$ is not a root of the characteristic equation of the associated linear homogeneous recurrence relation, there is a particular solution of the form
>
> - $(p_t n^t + p_{t−1} n^{t−1} + ⋯ + p_1 n + p_0)s^n$.
>
> When $s$ is a root of this characteristic equation and its multiplicity is $m$, there is a particular solution of the form
>
> - $n^m(p_t n^t + p_{t−1} n^{t−1} + ⋯ + p_1 n + p_0)s^n$.

##### 8.3 Divide-and-Conquer Algorithms and Recurrence Relations
> `pg: 9`
> `time req: 59"`
> `time done: 50"`
> `performance: 118%`
>
> `questions: 37`
> `practice time req: 35"`

> [!Error] 8.3.2 Divide-and-Conquer Recurrence Relations

* Suppose that a recursive algorithm divides a problem of size $n$ into $a$ subproblems, where each subproblem is of size $n/b$ (for simplicity, assume that $n$ is a multiple of $b$; in reality, the smaller problems are often of size equal to the nearest integers either less than or equal to, or greater than or equal to, $n/b$). Also, suppose that a total of $g(n)$ extra operations are required in the conquer step of the algorithm to combine the solutions of the subproblems into a solution of the original problem. Then, if $f(n)$ represents the number of operations required to solve the problem of size $n$, it follows that $f$ satisﬁes the recurrence relation $f(n) = af(n/b) + g(n)$. This is called a **divide-and-conquer recurrence relation**.
* As Examples 1–5 show, recurrence relations of the form $f(n) = af(n/b) + g(n)$ arise in many diﬀerent situations. It is possible to derive estimates of the size of functions that satisfy such recurrence relations.
---
* Suppose that $f$ satisﬁes this recurrence relation whenever $n$ is divisible by $b$. Let $n = b^k$, where $k$ is a positive integer. Then
	* $f(n) = af(n/b) + g(n)$
		* $= a^2f(n/b^2) + ag(n/b) + g(n)$
		* $...$
		* $= a^k f(n/b^k) + \displaystyle\sum_{j = 0}^{k-1} a^j g(n/b^j)$.
* Because $n/b^k = 1$, it follows that
	* $f(n) = a^k f(1) + \displaystyle\sum_{j=0}^{k-1} a^j g(n/b^j)$.
---

> [!Info] Theorem 1
> Let $f$ be an increasing function that satisﬁes the recurrence relation
>
> - $f(n) = af(n/b) + c$
>
> whenever $n$ is divisible by $b$, where $a ≥ 1$, $b$ is an integer greater than $1$, and $c$ is a positive real number. Then
>
> - $$\begin{flalign}f(n) is \begin{cases}O(n^{\log_b a}) & \quad \text{if } a \gt 1\\ O(\log n) & \quad \text{if } a = 1\end{cases}&&\end{flalign}$$
>
> Furthermore, when $n = b^k$ and $a ≠ 1$, where $k$ is a positive integer,
>
> - $f(n) = C_1n^{\log_b a} + C_2$
>
> where $C_1 = f(1) + c/(a − 1)$ and $C_2 = −c/(a − 1)$.

* We now state a more general, and more complicated, theorem, which has Theorem 1 as a special case. This theorem (or more powerful versions, including big-Theta estimates) is sometimes known as the master theorem because it is useful in analyzing the complexity of many important divide-and-conquer algorithms.

> [!Info] Theorem 2: `Master Theorem`
> Let $f$ be an increasing function that satisﬁes the recurrence relation
>
> - $f(n) = af(n/b) + cn^d$
>
> whenever $n = b^k$, where $k$ is a positive integer, $a ≥ 1$, $b$ is an integer greater than $1$, and $c$ and $d$ are real numbers with $c$ positive and $d$ nonnegative. Then
>
> - $$\begin{flalign}f(n) is  \begin{cases} O(n^d) & \quad \text{if } a \lt b^d,\\ O(n^d \log n) & \quad \text{if } a = b^d,\\ O(n^{\log_b a}) & \quad \text{if } a \gt b^d \end{cases} &&\end{flalign}$$

##### 8.4 Generating Functions
> `pg: 12`
> `time req: 1' 19"`
> `time done: 30"`
> `performance: 263%`
>
> `questions: 62`
> `practice time req: 46"`

> [!Warning] This chapter didn't seem to be very useful in the study of algorithms for software engineering interview prep; so I completely skipped it.

##### 8.5 Inclusion-Exclusion
> `pg: 5`
> `time req: 33"`
> `time done: 15"`
> `performance: 200%`
>
> `questions: 31`
> `practice time req: 19"`

> [!Error] 8.5.1 Introduction

A discrete mathematics class contains 30 women and 50 sophomores. How many students in the class are either women or sophomores? This question cannot be answered unless more information is provided. Adding the number of women in the class and the number of sophomores probably does not give the correct answer, because women sophomores are counted twice. This observation shows that the number of students in the class that are either sophomores or women is the sum of the number of women and the number of sophomores in the class minus the number of women sophomores. A technique for solving such counting problems was introduced in Section 6.1. In this section we will generalize the ideas introduced in that section to solve problems that require us to count the number of elements in the union of more than two sets.

> [!Error] 8.5.2 The Principle of Inclusion-Exclusion

* We will now state and prove the **inclusion–exclusion principle** for $n$ sets, where $n$ is a positive integer. This priniciple tells us that we can count the elements in a union of $n$ sets by adding the number of elements in the sets, then subtracting the sum of the number of elements in all intersections of two of these sets, then adding the number of elements in all intersections of three of these sets, and so on, until we reach the number of elements in the intersection of all the sets. It is added when there is an odd number of sets and added when there is an even number of sets.

> [!Info] Theorem 1: `The Principle of Inclusion-Exclusion`
> Let $A_1, A_2, …$, An be ﬁnite sets. Then
> 
> - $$\begin{flalign}|A_1 \cup A_2 \cup ⋯ \cup A_n| = \displaystyle\sum_{1\le i \le n} |A_i| - \displaystyle\sum_{1 \le i \lt j \le n} |A_i \cap A_j| &&\end{flalign}$$
> 	- $$\begin{flalign}+ \displaystyle\sum_{1 \le i \lt j \lt k \le n} |A_i \cap A_j \cap A_k| - ⋯ + (-1)^{n+1} |A_1 \cap A_2 \cap ⋯ \cap A_n|&&\end{flalign}$$

* The inclusion–exclusion principle gives a formula for the number of elements in the union of $n$ sets for every positive integer $n$. There are terms in this formula for the number of elements in the intersection of every nonempty subset of the collection of the $n$ sets. Hence, there are $2^n − 1$ terms in this formula.

##### 8.6 Applications of Inclusion-Exclusion
> `pg: 6`
> `time req: 39"`
> `time done: 13"`
> `performance: 300%`
>
> `questions: 27`
> `practice time req: 23"`

> [!Error] 8.6.1 Introduction

* Many counting problems can be solved using the principle of inclusion–exclusion. For instance, we can use this principle to ﬁnd the number of primes less than a positive integer. Many problems can be solved by counting the number of onto functions from one ﬁnite set to another. The inclusion–exclusion principle can be used to ﬁnd the number of such functions. The well-known hatcheck problem can be solved using the principle of inclusion–exclusion. This problem asks for the probability that no person is given the correct hat back by a hatcheck person who gives the hats back randomly.

> [!Error] 8.6.2 An Alternative Form of Inclusion-Exclusion

> [!Warning] Example 1 was important but I did not understand it AT ALL!

> [!Warning] The rest of the section seemed useless so I skipped it.

#### Chapter 9: Relations
> [!Summary]
> `sum page: 60`
> `sum time req: 6' 35"`

##### 9.1 Relations and their Properties
> `pg: 10`
> `time req: 1' 6"`
> `time done: 51"`
> `performance: 129%`
>
> `questions: 62`
> `practice time req: 39"`

> [!Error] 9.1.1 Introduction

> [!Info] Definition
> Let $A$ and $B$ be sets. A *binary relation* from $A$ to $B$ is a subset of $A × B$.

* In other words, a binary relation from $A$ to $B$ is a set $R$ of ordered pairs, where the ﬁrst element of each ordered pair comes from $A$ and the second element comes from $B$. We use the notation $a\ R\ b$ to denote that $(a, b) ∈ R$ and $a\ \centernot{R}\ b$ to denote that $(a, b) ∉ R$. Moreover, when $(a, b)$ belongs to $R$, $a$ is said to be **related to** $b$ by $R$.

> [!Error] 9.1.2 Functions as Relations

* Recall that a function $f$ from a set $A$ to a set $B$ assigns exactly one element of $B$ to each element of $A$. The graph of $f$ is the set of ordered pairs $(a, b)$ such that $b = f(a)$. Because the graph of $f$ is a subset of $A × B$, it is a relation from $A$ to $B$. Moreover, the graph of a function has the property that every element of $A$ is the ﬁrst element of exactly one ordered pair of the graph.
* Conversely, if $R$ is a relation from $A$ to $B$ such that every element in $A$ is the ﬁrst element of exactly one ordered pair of $R$, then a function can be deﬁned with $R$ as its graph. This can be done by assigning to an element $a$ of $A$ the unique element $b ∈ B$ such that $(a, b) ∈ R$.
* A relation can be used to express a one-to-many relationship between the elements of the sets $A$ and $B$, where an element of $A$ may be related to more than one element of $B$. A function represents a relation where exactly one element of $B$ is related to each element of $A$.
* Relations are a generalization of graphs of functions; they can be used to express a much wider class of relationships between sets. (Recall that the graph of the function $f$ from $A$ to $B$ is the set of ordered pairs $(a, f(a))$ for $a ∈ A$.)

> [!Error] 9.1.3 Relations on a Set

> [!Info] Definition
> A *relation on a set* $A$ is a relation from $A$ to $A$.
> In other words, a relation on a set $A$ is a subset of $A × A$.

> [!Example] Example 6
> > How many relations are there on a set with $n$ elements?
>
> A relation on a set $A$ is a subset of $A × A$. Because $A × A$ has $n^2$ elements when $A$ has $n$ elements, and a set with $m$ elements has $2^m$ subsets, there are $2^{n^2}$ subsets of $A × A$. Thus, there are $2^{n^2}$ relations on a set with $n$ elements.

> [!Error] 9.1.4 Properties of Relations

> [!Info] Definition
> A relation $R$ on a set $A$ is called *reﬂexive* if $(a, a) ∈ R$ for every element $a ∈ A$.

> [!Info] Definition
> A relation $R$ on a set $A$ is called *symmetric* if $(b, a) ∈ R$ whenever $(a, b) ∈ R$, for all $a, b ∈ A$. 
> A relation $R$ on a set $A$ such that for all $a, b ∈ A$, if $(a, b) ∈ R$ and $(b, a) ∈ R$, then $a = b$ is called *antisymmetric*.

* The terms symmetric and antisymmetric are not opposites, because a relation can have both of these properties or may lack both of them. A relation cannot be both symmetric and antisymmetric if it contains some pair of the form $(a, b)$ in which $a ≠ b$.

> [!Info] Definition
> A relation $R$ on a set $A$ is called *transitive* if whenever $(a, b) ∈ R$ and $(b, c) ∈ R$, then $(a, c) ∈ R$, for all $a, b, c ∈ A$.

> [!Error] 9.1.5 Combining Relations

* Because relations from $A$ to $B$ are subsets of $A × B$, two relations from $A$ to $B$ can be combined in any way two sets can be combined.

> [!Example] Example 17
> Let $A = \{1, 2, 3\}$ and $B = \{1, 2, 3, 4\}$. The relations $R_1 = \{(1, 1), (2, 2), (3, 3)\}$ and $R_2 = \{(1, 1), (1, 2), (1, 3), (1, 4)\}$ can be combined to obtain
>
> - $R_1 \cup R_2 = \{(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (3, 3)\}$,
> - $R_1 \cap R_2 = \{(1, 1)\}$,
> - $R_1 − R_2 = \{(2, 2), (3, 3)\}$,
> - $R_2 − R_1 = \{(1, 2), (1, 3), (1, 4)\}$.

* There is another way that relations are combined that is analogous to the composition of functions.

> [!Info] Definition
> Let $R$ be a relation from a set $A$ to a set $B$ and $S$ a relation from $B$ to a set $C$. The composite of $R$ and $S$ is the relation consisting of ordered pairs $(a, c)$, where $a ∈ A$, $c ∈ C$, and for which there exists an element $b ∈ B$ such that $(a, b) ∈ R$ and $(b, c) ∈ S$. We denote the composite of $R$ and $S$ by $S ◦ R$.

* The powers of a relation $R$ can be recursively deﬁned from the deﬁnition of a composite of two relations.

> [!Info] Definition
> Let $R$ be a relation on the set $A$. The powers $R^n$, $n = 1, 2, 3, …$ , are deﬁned recursively by
>
> - $R^1 = R$ and $R^{n+1} = R^n ◦ R$.

* The following theorem shows that the powers of a transitive relation are subsets of this relation.

> [!Info] Theorem 1
> The relation $R$ on a set $A$ is transitive if and only if $R^n ⊆ R$ for $n = 1, 2, 3, …$.

##### 9.2 n-ary Relations and their Applications
> `pg: 9`
> `time req: 59"`
> `time done: 17"`
> `performance: 347%`
>
> `questions: 41`
> `practice time req: 35"`

> [!Error] 9.2.1 Introduction

* Relationships among elements of more than two sets often arise.
* We will study relationships among elements from more than two sets in this section. These relationships are called **n-ary relations**. These relations are used to represent computer databases. These representations help us answer queries about the information stored in databases.

> [!Error] 9.2.2 n-ary Relations

> [!Info] Definition
> Let $A_1, A_2, …, A_n$ be sets. An *$n$-ary relation* on these sets is a subset of $A_1 × A_2 × ⋯ × A_n$. The sets $A_1, A_2, …, A_n$ are called the *domains* of the relation, and $n$ is called its *degree*.

> [!Warning] This was mostly a showcase of the logical foundations of databases.
> I did learn that there exists such logic and it is not implied. So it'd be great to read the whole of it from a database book no 9 dedicated pages in discrete math.

##### 9.3 Representing Relations
> `pg: 6`
> `time req: 39"`
> `time done: 44"`
> `performance: 88%`
> `questions: 36`
> `practice time req: 23"`

> [!Error] 9.3.2 Representing Relations Using Matrices

* A relation between ﬁnite sets can be represented using a zero–one matrix.
* Suppose that $R$ is a relation from $A = {a_1, a_2, …, a_m}$ to $B = {b_1, b_2, …, b_n}$. The relation $R$ can be represented by the matrix $M_R = [m_{ij}]$, where
	* $$\begin{flalign}m_ij = \begin{cases} 1 \text{if } (a_i, b_j) \in R,\\ 0 \text{if } (a_i, b_j) \notin R \end{cases}&&\end{flalign}$$
* In other words, the zero–one matrix representing $R$ has a $1$ as its $(i, j)$ entry when $a_i$ is related to $b_j$ , and a $0$ in this position if $a_i$ is not related to $b_j$. (Such a representation depends on the orderings used for $A$ and $B$.)
---
* The matrix of a relation on a set, which is a square matrix, can be used to determine whether the relation has certain properties.
* Recall that a relation $R$ on $A$ is reﬂexive if $(a, a) ∈ R$ whenever $a ∈ A$. The relation $R$ is *reflexive* if and only if $m_{ii} = 1$, for $i = 1, 2, …, n$. In other words, $R$ is reﬂexive if all the elements on the main diagonal of $\textbf{M}_R$ are equal to $1$. Note that the elements oﬀ the main diagonal can be either $0$ or $1$.
* The relation $R$ is symmetric if $(a, b) ∈ R$ implies that $(b, a) ∈ R$. The relation $R$ is symmetric if and only if $m_{ji} = 1$ whenever $m_{ij} = 1$. This also means $m_{ji} = 0$ whenever $m_{ij} = 0$. Consequently, $R$ is symmetric if and only if $m_{ij} = m_{ji}$ , for all pairs of integers $i$ and $j$ with $i = 1, 2, … , n$ and $j = 1, 2, … , n$. Recalling the deﬁnition of the transpose of a matrix, we see that $R$ is symmetric if and only if $\textbf{M}_R = (\textbf{M}_R)^t$, that is, if $\textbf{M}_R$ is a symmetric matrix.
* The relation $R$ is antisymmetric if and only if $(a, b) ∈ R$ and $(b, a) ∈ R$ imply that $a = b$. Consequently, the matrix of an antisymmetric relation has the property that if $m_{ij} = 1$ with $i ≠ j$, then $m_{ji} = 0$. Or, in other words, either $m_{ij} = 0$ or $m_{ji} = 0$ when $i ≠ j$.
---
* The Boolean operations join and meet can be used to ﬁnd the matrices representing the union and the intersection of two relations. Suppose that $R_1$ and $R_2$ are relations on a set $A$ represented by the matrices $M_{R_1}$ and $M_{R_2}$, respectively. The matrix representing the union of these relations has a $1$ in the positions where either $M_{R_1}$ or $M_{R_2}$ has a $1$. The matrix representing the intersection of these relations has a $1$ in the positions where both $M_{R_1}$ and $M_{R_2}$ have a $1$. Thus, the matrices representing the union and intersection of these relations are
	* $\textbf{M}_{R_1 \cup R_2} = \textbf{M}_{R_1} ∨ \textbf{M}_{R_2}$ and $\textbf{M}_{R_1 \cap R_2} = \textbf{M}_{R_1} ∧ \textbf{M}_{R_2}$.
---
* We now turn our attention to determining the matrix for the composite of relations. This matrix can be found using the Boolean product of the matrices for these relations. In particular, suppose that $R$ is a relation from $A$ to $B$ and $S$ is a relation from $B$ to $C$. Suppose that $A$, $B$, and $C$ have $m$, $n$, and $p$ elements, respectively. Let the zero–one matrices for $S ◦ R$, $R$, and $S$ be $\textbf{M}_{S ◦ R} = [t_{ij}]$, $\textbf{M}_R = [r_{ij}]$, and $\textbf{M}_S = [s_{ij}]$, respectively (these matrices have sizes $m × p$, $m × n$, and $n × p$, respectively). The ordered pair $(a_i, c_j)$ belongs to $S ◦ R$ if and only if there is an element $b_k$ such that $(a_i, b_k)$ belongs to $R$ and $(b_k, c_j)$ belongs to $S$. It follows that $t_{ij} = 1$ if and only if $r_{ik} = s_{kj} = 1$ for some $k$. From the deﬁnition of the Boolean product, this means that
	* $\textbf{M}_{S ◦ R} = \textbf{M}_R ⊙ \textbf{M}_S$.
* The matrix representing the composite of two relations can be used to ﬁnd the matrix for $\textbf{M}_{R^n}$ . In particular, $\textbf{M}_{R^n} = \textbf{M}_R^{[n]}$, from the deﬁnition of Boolean powers.

> [!Error] 9.3.3 Representing Relations Using Digraphs

> [!Info] Definition: `digraph`
> A *directed graph*, or *digraph*, consists of a set $V$ of *vertices* (or *nodes*) together with a set $E$ of ordered pairs of elements of $V$ called *edges* (or *arcs*). The vertex $a$ is called the *initial vertex* of the edge $(a, b)$, and the vertex $b$ is called the *terminal vertex* of this edge.

* An edge of the form $(a, a)$ is represented using an arc from the vertex $a$ back to itself. Such an edge is called a **loop**.
* The relation $R$ on a set $A$ is represented by the directed graph that has the elements of $A$ as its vertices and the ordered pairs $(a, b)$, where $(a, b) ∈ R$, as edges. This assignment sets up a one-to-one correspondence between the relations on a set $A$ and the directed graphs with $A$ as their set of vertices. Thus, every statement about relations corresponds to a statement about directed graphs, and vice versa. Directed graphs give a visual display of information about relations. As such, they are often used to study relations and their properties. (Note that relations from a set $A$ to a set $B$ can be represented by a directed graph where there is a vertex for each element of $A$ and a vertex for each element of $B$. However, when $A = B$, such representation provides much less insight than the digraph representations described here.)
* The directed graph representing a relation can be used to determine whether the relation has various properties.
	* For instance, a relation is reﬂexive if and only if there is a loop at every vertex of the directed graph, so that every ordered pair of the form $(x, x)$ occurs in the relation.
	* A relation is symmetric if and only if for every edge between distinct vertices in its digraph there is an edge in the opposite direction, so that $(y, x)$ is in the relation whenever $(x, y)$ is in the relation.
		* **Remark**: Note that a symmetric relation can be represented by an undirected graph, which is a graph where edges do not have directions.
	* Similarly, a relation is antisymmetric if and only if there are never two edges in opposite directions between distinct vertices.
	* Finally, a relation is transitive if and only if whenever there is an edge from a vertex $x$ to a vertex $y$ and an edge from a vertex $y$ to a vertex $z$, there is an edge from $x$ to $z$ (completing a triangle where each side is a directed edge with the correct direction).

##### 9.4 Closures of Relations
> `pg: 9`
> `time req: 59"`
> `time done: 59"`
> `performance: 100%`
>
> `questions: 36`
> `practice time req: 35"`

> [!Error] 9.4.1 Introduction

* We can construct a *transitive relation* $S$ containing $R$ such that $S$ is a subset of every transitive relation containing $R$. Here, $S$ is the smallest transitive relation that contains $R$. This relation is called the **transitive closure** of $R$.

> [!Error] 9.4.2 Different Type of Closures

* If $R$ is a relation on a set $A$, it may or may not have some property $P$, such as reﬂexivity, symmetry, or transitivity. When $R$ does not enjoy property $P$, we would like to ﬁnd the smallest relation $S$ on $A$ with property $P$ that contains $R.$

> [!Info] Definition
> If $R$ is a relation on a set $A$, then the closure of $R$ with respect to $P$, if it exists, is the relation $S$ on $A$ with property $P$ that contains $R$ and is a subset of every subset of $A × A$ containing $R$ with property $P$.

* If there is a relation $S$ that is a subset of every relation containing $R$ with property $P$, it **must be unique**. To see this, suppose that relations $S$ and $T$ both have property $P$ and are subsets of every relation with property $P$ that contains $R$. Then, $S$ and $T$ are subsets of each other, and so are equal. Such a relation, if it exists, is the smallest relation with property $P$ that contains $R$ because it is a subset of every relation with property $P$ that contains $R$.
---
* Given a relation $R$ on a set $A$, the *reﬂexive closure* of $R$ can be formed by adding to $R$ all pairs of the form $(a, a)$ with $a ∈ A$, not already in $R$. The addition of these pairs produces a new relation that is reﬂexive, contains $R$, and is contained within any reﬂexive relation containing $R$. We see that the reﬂexive closure of $R$ equals $R ∪ Δ$, where $Δ = \{(a, a) ∣ a ∈ A\}$ is the **diagonal relation** on $A$.
* The symmetric closure of a relation $R$ can be constructed by adding all ordered pairs of the form $(b, a)$, where $(a, b)$ is in the relation, that are not already present in $R$. Adding these pairs produces a relation that is symmetric, that contains $R$, and that is contained in any symmetric relation that contains $R$. The symmetric closure of a relation can be constructed by taking the union of a relation with its inverse; that is, $R ∪ R^{−1}$ is the **symmetric closure** of $R$, where $R^{−1} = \{(b, a) ∣ (a, b) ∈ R\}$.
---
* Suppose that a relation $R$ is not transitive. How can we produce a transitive relation that contains $R$ such that this new relation is contained within any transitive relation that contains $R$? Can the transitive closure of a relation $R$ be produced by adding all the pairs of the form $(a, c)$, where $(a, b)$ and $(b, c)$ are already in the relation? Consider the relation $R = {(1, 3), (1, 4), (2, 1), (3, 2)}$ on the set ${1, 2, 3, 4}$. This relation is not transitive because it does not contain all pairs of the form $(a, c)$ where $(a, b)$ and $(b, c)$ are in $R$. The pairs of this form not in $R$ are $(1, 2)$, $(2, 3)$, $(2, 4)$, and $(3, 1)$. Adding these pairs does not produce a transitive relation, because the resulting relation contains $(3, 1)$ and $(1, 4)$ but does not contain $(3, 4)$. This shows that constructing the transitive closure of a relation is more complicated than constructing either the reﬂexive or symmetric closure. The rest of this section develops algorithms for constructing transitive closures. As will be shown later in this section, the transitive closure of a relation can be found by adding new ordered pairs that must be present and then repeating this process until no new ordered pairs are needed.

> [!Error] 9.4.3 Paths in Directed Graphs

* We will see that representing relations by directed graphs helps in the construction of transitive closures.

> [!Info] Definition: `path`
> A *path* from $a$ to $b$ in the directed graph $G$ is a sequence of edges $(x_0, x_1)$, $(x_1, x_2)$, $(x_2, x_3)$, $…$ , $(x_{n−1}, x_n)$ in $G$, where $n$ is a nonnegative integer, and $x_0 = a$ and $x_n = b$, that is, a sequence of edges where the terminal vertex of an edge is the same as the initial vertex in the next edge in the path. This path is denoted by $x_0, x_1, x_2, …, x_{n−1}, x_n$ and has length $n$. We view the empty set of edges as a path of length zero from $a$ to $a$. A path of length $n ≥ 1$ that begins and ends at the same vertex is called a **circuit** or **cycle**.

* A path in a directed graph can pass through a vertex more than once. Moreover, an edge in a directed graph can occur more than once in a path.
* The *term* path also applies to relations. Carrying over the deﬁnition from directed graphs to relations, there is a path from $a$ to $b$ in $R$ if there is a sequence of elements $a$, $x_1$, $x_2$, $…$, $x_{n−1}$, $b$ with $(a, x_1) ∈ R$, $(x_1, x_2) ∈ R$, $…$ , and $(x_{n−1}, b) ∈ R$.

> [!Info] Theorem 1
> Let $R$ be a relation on a set $A$. There is a path of length $n$, where $n$ is a positive integer, from $a$ to $b$ if and only if $(a, b) ∈ R^n$.

> [!Error] 9.4.4 Transitive Closures

> [!Info] Definition
> Let $R$ be a relation on a set $A$. The *connectivity relation* $R^∗$ consists of the pairs $(a, b)$ such that there is a path of length at least one from $a$ to $b$ in $R$.

* Because $R^n$ consists of the pairs $(a, b)$ such that there is a path of length $n$ from $a$ to $b$, it follows that $R^∗$ is the union of all the sets $R^n$. In other words,
	* $$\begin{flalign}R^∗ = \displaystyle\bigcup_{n=1}^{\infty} R^n&&\end{flalign}$$
* The connectivity relation is useful in many models.

> [!Info] Theorem 2
> The transitive closure of a relation $R$ equals the connectivity relation $R^∗$.

> [!Info] Lemma 1
> Let $A$ be a set with $n$ elements, and let $R$ be a relation on $A$. If there is a path of length at least one in $R$ from $a$ to $b$, then there is such a path with length not exceeding $n$. Moreover, when $a ≠ b$, if there is a path of length at least one in $R$ from $a$ to $b$, then there is such a path with length not exceeding $n − 1$.

* From Lemma 1, we see that the transitive closure of $R$ is the union of $R, R^2, R^3, …, and R^n$. This follows because there is a path in $R^∗$ between two vertices if and only if there is a path between these vertices in $R^i$, for some positive integer $i$ with $i ≤ n$. Because $R^∗ = R \cup R^2 \cup R^3 \cup ⋯ \cup R^n$ and the zero–one matrix representing a union of relations is the join of the zero–one matrices of these relations, the zero–one matrix for the transitive closure is the join of the zero–one matrices of the ﬁrst $n$ powers of the zero–one matrix of $R$.

> [!Info] Theorem 3
> Let $\textbf{M}_R$ be the zero–one matrix of the relation $R$ on a set with $n$ elements. Then the zero–one matrix of the transitive closure $R^∗$ is
>
> - $\textbf{M}_{R^∗} = \textbf{M}_R ∨ \textbf{M}_R^{[2]} ∨ \textbf{M}_R^{[3]} ∨ ⋯ ∨ \textbf{M}_R^{[n]}$.

* Theorem 3 can be used as a basis for an algorithm for computing the matrix of the relation $R^∗$ . To ﬁnd this matrix, the successive Boolean powers of $\textbf{M}_R$, up to the $n$th power, are computed. As each power is calculated, its join with the join of all smaller powers is formed. When this is done with the $n$th power, the matrix for $R^∗$ has been found.
* We can easily ﬁnd the number of bit operations used by Algorithm 1 to determine the transitive closure of a relation. Computing the Boolean powers $\textbf{M}_R$, $\textbf{M}_R^{[2]}$, …, $\textbf{M}_R^{[n]}$ requires that $n - 1$ Boolean products of $n × n$ zero–one matrices be found. Each of these Boolean products can be found using $n^2 (2n − 1)$ bit operations. Hence, these products can be computed using $n^2 (2n − 1)(n − 1)$ bit operations.
* To ﬁnd $\textbf{M}_{R^∗}$ from the $n$ Boolean powers of $\textbf{M}_R$, $n − 1$ joins of zero–one matrices need to be found. Computing each of these joins uses $n^2$ bit operations. Hence, $(n − 1)n^2$ bit operations are used in this part of the computation.
* Therefore, when Algorithm 1 is used, the matrix of the transitive closure of a relation on a set with $n$ elements can be found using $n^2 (2n − 1)(n − 1) + (n − 1)n^2 = 2n^3 (n − 1)$, which is $O(n^4)$ bit operations.

> [!Error] 9.4.5 Warshall's Algorithm

> [!Warning] I postponed reading this to when I'm reading graph algorithms in Algorithms Design Manual.

##### 9.5 Equivalence Relations
> `pg: 9`
> `time req: 59"`
> `time done: 48"`
> `performance: 122%`
>
> `questions: 69`
> `practice time req: 35"`

> [!Error] 9.5.2 Equivalence Relations

> [!Info] Definition
> A relation on a set $A$ is called an *equivalence relation* if it is *reﬂexive*, *symmetric*, and *transitive*.

* Equivalence relations are important throughout mathematics and computer science. One reason for this is that in an equivalence relation, when two elements are related it makes sense to say they are equivalent.

> [!Info] Definition
> Two elements $a$ and $b$ that are related by an equivalence relation are called *equivalent*. The notation $a ∼ b$ is often used to denote that $a$ and $b$ are equivalent elements with respect to a particular equivalence relation.

* For the notion of equivalent elements to make sense, every element should be equivalent to itself, as the reﬂexive property guarantees for an equivalence relation. It makes sense to say that $a$ and $b$ are related (not just that $a$ is related to $b$) by an equivalence relation, because when $a$ is related to $b$, by the symmetric property, $b$ is related to $a$. Furthermore, because an equivalence relation is transitive, if $a$ and $b$ are equivalent and $b$ and $c$ are equivalent, it follows that $a$ and $c$ are equivalent.
* One of the most widely used equivalence relations is congruence modulo $m$, where $m$ is an integer greater than $1$.

> [!Example] Example 3
> > **Congruence Modulo $m$**: Let $m$ be an integer with $m > 1$. Show that the relation $R = \{(a, b) ∣ a ≡ b\ (mod\ m)\}$ is an equivalence relation on the set of integers.
>
> $a ≡ b\ (mod\ m)$ if and only if $m$ divides $a − b$. Note that $a − a = 0$ is divisible by $m$, because $0 = 0 ⋅ m$. Hence, $a ≡ a\ (mod\ m)$, so congruence modulo $m$ is reﬂexive. Now suppose that $a ≡ b\ (mod\ m)$. Then $a − b$ is divisible by $m$, so $a − b = km$, where $k$ is an integer. It follows that $b − a = (−k)m$, so $b ≡ a\ (mod\ m)$. Hence, congruence modulo $m$ is symmetric. Next, suppose that $a ≡ b\ (mod\ m)$ and $b ≡ c\ (mod\ m)$. Then $m$ divides both $a − b$ and $b − c$. Therefore, there are integers $k$ and $l$ with $a − b = km$ and $b − c = lm$. Adding these two equations shows that $a − c = (a − b) + (b − c) = km + lm = (k + l)m$. Thus, $a ≡ c\ (mod\ m)$. Therefore, congruence modulo $m$ is transitive. It follows that congruence modulo $m$ is an equivalence relation.

> [!Error] 9.5.3 Equivalence Classes

> [!Info] Definition
> Let $R$ be an equivalence relation on a set $A$. The set of all elements that are related to an element $a$ of $A$ is called the equivalence class of $a$. The equivalence class of $a$ with respect to $R$ is denoted by $[a]_R$. When only one relation is under consideration, we can delete the subscript $R$ and write $[a]$ for this equivalence class.
>
> In other words, if $R$ is an equivalence relation on a set $A$, the equivalence class of the element $a$ is $[a]_R = \{s ∣ (a, s) ∈ R\}$.
>
> If $b ∈ [a]_R$ , then $b$ is called a representative of this equivalence class. Any element of a class can be used as a representative of this class. That is, there is nothing special about the particular element chosen as the representative of the class.

> [!Error] 9.5.4 Equivalence Classes and Partitions

> [!Info] Theorem 1
> Let $R$ be an equivalence relation on a set $A$. These statements for elements $a$ and $b$ of $A$ are equivalent:
> - $(i) aRb$
> - $(ii) [a] = [b]$
> - $(iii) [a] \cap [b] \ne \emptyset$
>
> This shows that the equivalence classes of two elements of $A$ are either identical or disjoint.

* We are now in a position to show how an equivalence relation partitions a set.
* Let $R$ be an equivalence relation on a set $A$. The union of the equivalence classes of $R$ is all of $A$, because an element $a$ of $A$ is in its own equivalence class, namely, $[a]_R$ . In other words, $\displaystyle\bigcup_{a \in A} [a]_R = A$.
* In addition, from Theorem 1, it follows that these equivalence classes are either equal or disjoint, so $[a]_R \cap [b]_R = \emptyset$, when $[a]_R ≠ [b]_R$.
* These two observations show that the equivalence classes form a partition of $A$, because they split $A$ into disjoint subsets. More precisely, a **partition** of a set $S$ is a collection of disjoint nonempty subsets of $S$ that have $S$ as their union. In other words, the collection of subsets $A_i, i ∈ I$ (where $I$ is an index set) forms a partition of $S$ if and only if $A_i ≠ \emptyset \text{ for } i ∈ I$, $A_i \cap A_j = \emptyset$ when $i ≠ j$, and $\displaystyle\bigcup_{i \in I} A_i = S$.
	* Here the notation $\bigcup_{i \in I} A_i$ represents the union of the sets $A_i$ for all $i ∈ I$.

> [!Info] Theorem 2
> Let $R$ be an equivalence relation on a set $S$. Then the equivalence classes of $R$ form a partition of $S$. Conversely, given a partition ${A_i ∣ i ∈ I}$ of the set $S$, there is an equivalence relation $R$ that has the sets $A_i, i ∈ I$, as its equivalence classes.

* The congruence classes modulo $m$ provide a useful illustration of Theorem 2. There are $m$ diﬀerent congruence classes modulo $m$, corresponding to the $m$ diﬀerent remainders possible when an integer is divided by $m$. These $m$ congruence classes are denoted by $[0]_m$, $[1]_m$, $…$, $[m − 1]_m$. They form a partition of the set of integers.

##### 9.6 Partial Orderings
> `pg: 12`
> `time req: 1' 20"`
> `time done: 45"`
> `performance: 177%`
>
> `questions: 67`
> `practice time req: 1' 6"`

> [!Info] Definition: `partial ordering`
> A relation $R$ on a set $S$ is called a *partial ordering* or *partial order* if it is reﬂexive, antisymmetric, and transitive. A set $S$ together with a partial ordering $R$ is called a *partially ordered set*, or *poset*, and is denoted by $(S, R)$. Members of $S$ are called elements of the poset.

> [!Example] Example 1
> > Show that the greater than or equal to relation ($≥$) is a partial ordering on the set of integers.
>
> Because $a ≥ a$ for every integer $a$, $≥$ is reﬂexive. If $a ≥ b$ and $b ≥ a$, then $a = b$. Hence, $≥$ is antisymmetric. Finally, $≥$ is transitive because $a ≥ b$ and $b ≥ c$ imply that $a ≥ c$. It follows that $≥$ is a partial ordering on the set of integers and $(Z, ≥)$ is a poset.

> [!Example] Example 2
> > Show that the inclusion relation $⊆$ is a partial ordering on the **power set** of a set $S$.
>
> Because $A ⊆ A$ whenever $A$ is a subset of $S$, $⊆$ is reﬂexive. It is antisymmetric because $A ⊆ B$ and $B ⊆ A$ imply that $A = B$. Finally, $⊆$ is transitive, because $A ⊆ B$ and $B ⊆ C$ imply that $A ⊆ C$. Hence, $⊆$ is a partial ordering on $P(S)$, and $(P(S), ⊆)$ is a poset.

* In diﬀerent posets diﬀerent symbols such as $≤$, $⊆$, and $|$, are used for a partial ordering. However, we need a symbol that we can use when we discuss the ordering relation in an arbitrary poset. Customarily, the notation $a \preceq b$ is used to denote that $(a, b) ∈ R$ in an arbitrary poset $(S, R)$. This notation is used because the less than or equal to relation on the set of real numbers is the most familiar example of a partial ordering and the symbol $\preceq$ is similar to the $≤$ symbol. (Note that the symbol $\preceq$ is used to denote the relation in any poset, not just the less than or equal to relation.) The notation $a \prec b$ denotes that $a \preceq b$, but $a ≠ b$. Also, we say “$a$ is less than $b$” or “$b$ is greater than $a$” if $a \prec b$.
* When $a$ and $b$ are elements of the poset $(S, \preceq)$, it is not necessary that either $a \preceq b$ or $b \preceq a$. For instance, in $(P(Z), ⊆)$, $\{1, 2\}$ is not related to $\{1, 3\}$, and vice versa, because neither set is contained within the other. Similarly, in $(Z^+ , ∣)$, $2$ is not related to $3$ and $3$ is not related to $2$, because $2 \centernot{|} 3$ and $3 \centernot{|} 2$. This leads to Deﬁnition 2.

> [!Info] Definition: `comparable`
> The elements $a$ and $b$ of a poset $(S, \preceq)$ are called comparable if either $a \preceq b$ or $b \preceq a$. When $a$ and $b$ are elements of $S$ such that neither $a \preceq b$ nor $b \preceq a$, $a$ and $b$ are called incomparable.

* The adjective “partial” is used to describe partial orderings because pairs of elements may be incomparable. When every two elements in the set are comparable, the relation is called a **total ordering**.

> [!Info] Definition: `poset`
> If $(S, \preceq)$ is a poset and every two elements of $S$ are comparable, $S$ is called a *totally ordered* or *linearly ordered* set, and $\preceq$ is called a total order or a linear order. A totally ordered set is also called a *chain*.

> [!Example] Example 6
> The poset $(Z, ≤)$ is totally ordered, because $a ≤ b$ or $b ≤ a$ whenever $a$ and $b$ are integers.

> [!Example] Example 7
> The poset $(Z+ , ∣)$ is not totally ordered because it contains elements that are incomparable, such as $5$ and $7$.

> [!Info] Definition: `well-ordered set`
> $(S, \preceq)$ is a *well-ordered* set if it is a poset such that $\preceq$ is a total ordering and every nonempty subset of $S$ has a least element.

> [!Example] Example 8
> The set of ordered pairs of positive integers, $Z^+ × Z^+$ , with $(a_1, a_2 ) \preceq (b_1, b_2)$ if $a_1 < b_1$, or if $a_1 = b_1$ and $a_2 ≤ b_2$ (the lexicographic ordering), is a well-ordered set.
> The set $Z$, with the usual $≤$ ordering, is not well-ordered because the set of negative integers, which is a subset of $Z$, has no least element.

> [!Info] Theorem 1: `The Principle of Well-Ordrered Induction`
> At the end of Section 5.3 we showed how to use the principle of well-ordered induction (there called generalized induction) to prove results about a well-ordered set. We now state and prove that this proof technique is valid.
>
> Suppose that $S$ is a well-ordered set. Then $P(x)$ is true for all $x ∈ S$, if
> 
> - **Inductive Step**: For every $y ∈ S$, if $P(x)$ is true for all $x ∈ S$ with $x ≺ y$, then $P(y)$ is true.
>
> **Remark**: We do not need a basis step in a proof using the principle of well-ordered induction because if $x_0$ is the least element of a well-ordered set, the inductive step tells us that $P(x_0)$ is true. This follows because there are no elements $x ∈ S$ with $x \prec x_0$ , so we know (using a vacuous proof) that $P(x)$ is true for all $x ∈ S$ with $x \prec x_0$. 

> [!Warning] I skipped from here on.

#### Chapter 10: Graphs
> [!Summary]
> `sum page: 76`
> `sum time req: 8' 22"`

##### 10.1 Graphs and Graph Models
> `pg: 10`
> `time req: 1' 6"`
> `time done: 28"`
> `performance: 235%`
>
> `questions: 38`
> `practice time req: 39"`

> [!Info] Definition: `graph`
> A graph $G = (V, E)$ consists of $V$, a nonempty set of vertices (or nodes) and $E$, a set of edges. Each edge has either one or two vertices associated with it, called its endpoints. An edge is said to connect its endpoints.

* A graph in which each edge connects two diﬀerent vertices and where no two edges connect the same pair of vertices is called a **simple graph**. Note that in a simple graph, each edge is associated to an unordered pair of vertices, and no other edge is associated to this same edge. Consequently, when there is an edge of a simple graph associated to $\{u, v\}$, we can also say, without possible confusion, that $\{u, v\}$ is an edge of the graph.
* Graphs that may have multiple edges connecting the same vertices are called **multigraphs**. When there are m diﬀerent edges associated to the same unordered pair of vertices $\{u, v\}$, we also say that $\{u, v\}$ is an edge of multiplicity $m$. That is, we can think of this set of edges as $m$ diﬀerent copies of an edge $\{u, v\}$.
* Graphs that may include **loops**, and possibly multiple edges connecting the same pair of vertices or a vertex to itself, are sometimes called **pseudographs**.

> [!Info] Definition: `directed graph`
> A *directed graph* (or *digraph*) $(V, E)$ consists of a nonempty set of vertices $V$ and a set of directed edges (or arcs) $E$. Each directed edge is associated with an ordered pair of vertices. The directed edge associated with the ordered pair $(u, v)$ is said to start at $u$ and end at $v$.

| type | edges | multiple edges allowed? | loops allowed? |
| :- | :- | :-: | :-: |
| simple graph | undirected | no | no |
| multigraph | undirected | yes | no |
| pseudograph | undirected | yes | yes |
| simple directed graph | directed | no | no |
| directed multigraph | directed | yes | yes |
| mixed graph | directed and undirected | yes | yes |

##### 10.2 Graph Terminology and Special types of Graphs
> `pg: 15`
> `time req: 1' 39"`
> `time done: 1' 19"`
> `performance: 125%`
>
> `questions: 38`
> `practice time req: 58"`

> [!Error] 10.2.2 Basic Terminology

> [!Info] Definition 1: `adjacent vertices`
> Two vertices $u$ and $v$ in an undirected graph $G$ are called *adjacent* (or *neighbours*) in $G$ if $u$ and $v$ are endpoints of an edge $e$ of $G$. Such an edge $e$ is called *incident with* the vertices $u$ and $v$ and $e$ is said to *connect* $u$ and $v$.

> [!Info] Definition 2: `vertix neighbourhood`
> The set of all neighbours of a vertex $v$ of $G = (V, E)$, denoted by $N(v)$, is called the *neighbourhood* of $v$. If $A$ is a subset of $V$, we denote by $N(A)$ the set of all vertices in $G$ that are adjacent to at least one vertex in $A$. So, $N(A) = \bigcup_{v \in A}N(v)$.

> [!Info] Definition 3: `degree of vertex`
> The *degree of a vertex* in an undirected graph is the number of edges incident with it, except that a loop at a vertex contributes twice to the degree of that vertex. The degree of the vertex $v$ is denoted by $deg(v)$.

* A vertex of degree zero is called **isolated**. It follows that an isolated vertex is not adjacent to any vertex.
* A vertex is **pendant** if and only if it has degree one. Consequently, a pendant vertex is adjacent to exactly one other vertex.

> [!Info] Theorem 1: `The Handshaking Theorem`
> Let $G = (V, E)$ be an undirected graph with $m$ edges. Then
>
> - $2m = \displaystyle\sum_{v \in V} deg(v)$
>
> (Note that this applies even if multiple edges and loops are present.)

* Theorem 1 shows that the sum of the degrees of the vertices of an undirected graph is even. This simple fact has many consequences.

> [!Info] Theorem 2
> An undirected graph has an even number of vertices of odd degree.

> [!Info] Definition 4
> When $(u, v)$ is an edge of the graph $G$ with directed edges, $u$ is said to be *adjacent to* $v$ and $v$ is said to be *adjacent from* $u$. The vertex $u$ is called the *initial vertex* of $(u, v)$, and $v$ is called the *terminal* or *end vertex* of $(u, v)$. The initial vertex and terminal vertex of a loop are the same.

* Because the edges in graphs with directed edges are ordered pairs, the deﬁnition of the degree of a vertex can be reﬁned to reﬂect the number of edges with this vertex as the initial vertex and as the terminal vertex.

> [!Info] Definition 5
> In a graph with directed edges the *in-degree of a vertex* $v$, denoted by $deg^−(v)$, is the number of edges with $v$ as their terminal vertex. The *out-degree of* $v$, denoted by $deg^+(v)$, is the number of edges with $v$ as their initial vertex. (Note that a loop at a vertex contributes $1$ to both the in-degree and the out-degree of this vertex.)

> [!Info] Theorem 3
> Let $G = (V, E)$ be a graph with directed edges. Then
>
> - $\displaystyle\sum_{v \in V} deg^−(v) = \displaystyle\sum_{v \in V} deg^+(v) = |E|$.

* There are many properties of a graph with directed edges that do not depend on the direction of its edges. Consequently, it is often useful to ignore these directions. The undirected graph that results from ignoring directions of edges is called the **underlying undirected graph**. A graph with directed edges and its underlying undirected graph have the same number of edges.

> [!Error] 10.2.3 Some Special Simple Graphs

* A **complete graph** on $n$ vertices, denoted by $K_n$ , is a simple graph that contains exactly one edge between each pair of distinct vertices.
* A simple graph for which there is at least one pair of distinct vertex not connected by an edge is called **noncomplete**.
* A cycle $C_n$, $n ≥ 3$, consists of $n$ vertices $v_1, v_2, …, v_n$ and edges ${v_1, v_2}$, ${v_2, v_3}$, …, ${v_{n−1}, v_n}$, and ${v_n, v_1}$.
* We obtain a **wheel** $W_n$ when we add an additional vertex to a cycle $C_n$, for $n ≥ 3$, and connect this new vertex to each of the $n$ vertices in $C_n$, by new edges.

> [!Error] 10.2.4 Bipartite Graphs

* Sometimes a graph has the property that its vertex set can be divided into two disjoint subsets such that each edge connects a vertex in one of these subsets to a vertex in the other subset.
	* For example, consider the graph representing marriages between men and women in a village, where each person is represented by a vertex and a marriage is represented by an edge. In this graph, each edge connects a vertex in the subset of vertices representing males and a vertex in the subset of vertices representing females.

> [!Info] Definition 5: `bipartite graph`
> A simple graph $G$ is called *bipartite* if its vertex set $V$ can be partitioned into two disjoint sets $V_1$ and $V_2$ such that every edge in the graph connects a vertex in $V_1$ and a vertex in $V_2$ (so that no edge in $G$ connects either two vertices in $V_1$ or two vertices in $V_2$). When this condition holds, we call the pair $(V_1, V_2)$ a *bipartition* of the vertex set $V$ of $G$.

* Theorem 4 provides a useful criterion for determining whether a graph is bipartite.

> [!Info] Theorem 4
> A simple graph is bipartite if and only if it is possible to assign one of two diﬀerent colors to each vertex of the graph so that no two adjacent vertices are assigned the same color.
>
> > [!Info] This is an example of a result in the part of graph theory known as graph colorings.

* A **complete bipartite graph** $K_{m,n}$ is a graph that has its vertex set partitioned into two subsets of $m$ and $n$ vertices, respectively with an edge between two vertices if and only if one vertex is in the ﬁrst subset and the other vertex is in the second subset.

> [!Error] 10.2.5 Bipartite Graphs and Matchings

* A **matching** $M$ in a simple graph $G = (V, E)$ is a subset of the set $E$ of edges of the graph such that no two edges are incident with the same vertex. In other words, a matching is a subset of edges such that if $\{s, t\}$ and $\{u, v\}$ are distinct edges of the matching, then $s$, $t$, $u$, and $v$ are distinct. A vertex that is the endpoint of an edge of a matching $M$ is said to be **matched** in $M$; otherwise it is said to be **unmatched**. A **maximum matching** is a matching with the largest number of edges. We say that a matching $M$ in a bipartite graph $G = (V, E)$ with bipartition $(V_1, V_2)$ is a **complete matching from** $V_1$ **to** $V_2$ if every vertex in $V_1$ is the endpoint of an edge in the matching, or equivalently, if $|M| = |V_1|$.

> [!Info] Theorem 5: `Hall's Marriage Theorem`
> The bipartite graph $G = (V, E)$ with bipartition $(V_1, V_2)$ has a complete matching from $V_1$ to $V_2$ if and only if $|N(A)| ≥ |A|$ for all subsets $A$ of $V_1$.

> [!Error] 10.2.7 New Graphs from Old

> [!Info] Definition
> A *subgraph* of a graph $G = (V, E)$ is a graph $H = (W, F)$, where $W ⊆ V$ and $F ⊆ E$. A subgraph $H$ of $G$ is a proper subgraph of $G$ if $H ≠ G$.

> [!Info] Definition
> Let $G = (V, E)$ be a simple graph. The subgraph induced by a subset $W$ of the vertex set $V$ is the graph $(W, F)$, where the edge set $F$ contains an edge in $E$ if and only if both endpoints of this edge are in $W$.
>
> > [!Warning] This is different from the other definition of subgraph. In the first one, the subgraph has custom picked edges, but in this new definition, the subgraph is induced from a set of vertices which is a subset of $V$, meaning the edges are induced.

> [!Info] Definition: `union of graphs`
> The *union* of two simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ is the simple graph with vertex set $V_1 \cup V_2$ and edge set $E_1 \cup E_2$. The union of $G_1$ and $G_2$ is denoted by $G_1 \cup G_2$.

##### 10.3 Representing Graphs and Graph Isomorphism
> `pg: 7`
> `time req: 46"`
> `time done: 46"`
> `performance: 100%`
>
> `questions: 78`
> `practice time req: 27"`

> [!Error] 10.3.2 Representing Graphs

* One way to represent a graph without multiple edges is to list all the edges of this graph.
* Another way to represent a graph with no multiple edges is to use adjacency lists, which specify the vertices that are adjacent to each vertex of the graph.

> [!Error] 10.3.3 Adjacency Matrices

* Suppose that $G = (V, E)$ is a simple graph where $|V| = n$. Suppose that the vertices of $G$ are listed arbitrarily as $v_1, v_2, …, v_n$ . The adjacency matrix $A$ (or $A_G$) of $G$, with respect to this listing of the vertices, is the $n\ x\ n$ zero–one matrix with $1$ as its $(i, j)$th entry when $v_i$ and $v_j$ are adjacent, and $0$ as its $(i, j)$th entry when they are not adjacent. In other words, if its adjacency matrix is $A = [a_{ij}]$, then
	* $a_{ij} = \begin{cases}1 & \quad \text{if } \{v_i, v_j\} \text{ is an edge of G,}\\ 0 & \quad \text{otherwise}\end{cases}$
	* Note that an adjacency matrix of a graph is based on the ordering chosen for the vertices. Hence, there may be as many as $n!$ diﬀerent adjacency matrices for a graph with $n$ vertices, because there are $n!$ diﬀerent orderings of $n$ vertices.
	* The adjacency matrix of a **simple** graph is symmetric, that is, $a_{ij} = a_{ji}$, because both of these entries are $1$ when $v_i$ and $v_j$ are adjacent, and both are $0$ otherwise. Furthermore, because a simple graph has no loops, each entry $a_{ii}$, $i = 1, 2, 3, … , n$, is $0$.
* Adjacency matrices can also be used to represent undirected graphs with loops and with multiple edges.
	* A loop at the vertex $v_i$ is represented by a $1$ at the $(i, i)$th position of the adjacency matrix.
	* When multiple edges connecting the same pair of vertices $v_i$ and $v_j$, or multiple loops at the same vertex, are present, the adjacency matrix is no longer a zero–one matrix, because the $(i, j)$th entry of this matrix equals the number of edges that are associated to $\{v_i, v_j\}$.
	* All undirected graphs, including multigraphs and pseudographs, have symmetric adjacency matrices.
* The matrix for a directed graph $G = (V, E)$ has a $1$ in its $(i, j)$th position if there is an edge from $v_i$ to $v_j$, where $v_1, v_2, …, v_n$ is an arbitrary listing of the vertices of the directed graph. In other words, if $A = [a_{ij}]$ is the adjacency matrix for the directed graph with respect to this listing of the vertices, then
	* $a_{ij} = \begin{cases}1 & \quad \text{if } (v_i, v_j) \text{ is an edge of G,}\\ 0 & \quad \text{otherwise} \end{cases}$
	* The adjacency matrix for a directed graph does not have to be symmetric, because there may not be an edge from $v_j$ to $v_i$ when there is an edge from $v_i$ to $v_j$.

> [!Error] 10.3.4 Incidence Matrices

* **Incidence matrices**: Let $G = (V, E)$ be an undirected graph. Suppose that $v_1, v_2, …, v_n$ are the vertices and $e_1, e_2, …, e_m$ are the edges of $G$. Then the incidence matrix with respect to this ordering of $V$ and $E$ is the $n × m$ matrix $M = [m_{ij}]$, where
	* $m_{ij} = \begin{cases}1 & \quad \text{when edge } e_j  \text{ is incident with } v_i,\\ 0 & \quad \text{otherwise.}\end{cases}$
* Incidence matrices can also be used to represent multiple edges and loops.
	* Multiple edges are represented in the incidence matrix using columns with identical entries, because these edges are incident with the same pair of vertices.
	* Loops are represented using a column with exactly one entry equal to $1$, corresponding to the vertex that is incident with this loop.

> [!Error] 10.3.5 Isomorphism of Graphs

> [!Info] Definition: `graph isomorphism`
> The simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are *isomorphic* if there exists a one-to-one and onto function $f$ from $V_1$ to $V_2$ with the property that $a$ and $b$ are adjacent in $G_1$ if and only if $f(a)$ and $f(b)$ are adjacent in $G_2$ , for all $a$ and $b$ in $V_1$. Such a function $f$ is called an *isomorphism*. Two simple graphs that are not isomorphic are called *nonisomorphic*.

> [!Error] 10.3.6 Determining whether Two Simple Graphs are Isomorphic

* It is often diﬃcult to determine whether two simple graphs are isomorphic. There are n! possible one-to-one correspondences between the vertex sets of two simple graphs with n vertices. Testing each such correspondence to see whether it preserves adjacency and nonadjacency is impractical if n is at all large.
* Sometimes it is not hard to show that two graphs are not isomorphic. In particular, we can show that two graphs are not isomorphic if we can ﬁnd a property only one of the two graphs has, but that is preserved by isomorphism. A property preserved by isomorphism of graphs is called a **graph invariant**. For instance, isomorphic simple graphs must have the same number of vertices, because there is a one-to-one correspondence between the sets of vertices of the graphs.
* Isomorphic simple graphs also must have the same number of edges, because the one-to-one correspondence between vertices establishes a one-to-one correspondence between edges. In addition, the degrees of the vertices in isomorphic simple graphs must be the same. That is, a vertex $v$ of degree $d$ in $G$ must correspond to a vertex $f(v)$ of degree $d$ in $H$, because a vertex $w$ in $G$ is adjacent to $v$ if and only if $f(v)$ and $f(w)$ are adjacent in $H$.
* To show that a function $f$ from the vertex set of a graph $G$ to the vertex set of a graph $H$ is an isomorphism, we need to show that $f$ preserves the presence and absence of edges. One helpful way to do this is to use adjacency matrices. In particular, to show that $f$ is an isomorphism, we can show that the adjacency matrix of $G$ is the same as the adjacency matrix of $H$, when rows and columns are labeled to correspond to the images under $f$ of the vertices in $G$ that are the labels of these rows and columns in the adjacency matrix of $G$.

##### 10.4 Connectivity
> `pg: 11`
> `time req: 1' 13"`
> `time done: 1' 22"`
> `performance: 89%`
>
> `questions: 66`
> `practice time req: 42"`

> [!Error] 10.4.2 Paths

> [!Info] Definition: `path`
> Let $n$ be a nonnegative integer and $G$ an undirected graph. A *path* of *length* $n$ from $u$ to $v$ in $G$ is a sequence of $n$ edges $e_1, …, e_n$ of $G$ for which there exists a sequence $x_0 = u$, $x_1$, $…$ , $x_{n−1}$, $x_n = v$ of vertices such that $e_i$ has, for $i = 1, … , n$, the endpoints $x_{i−1}$ and $x_i$. When the graph is simple, we denote this path by its vertex sequence $x_0, x_1, …, x_n$ (because listing these vertices uniquely determines the path). The path is a *circuit* if it begins and ends at the same vertex, that is, if $u = v$, and has length greater than zero. The path or circuit is said to *pass through* the vertices $x_1, x_2, …, x_{n−1}$ or *traverse* the edges $e_1, e_2, …, e_n$ . A path or circuit is *simple* if it does not contain the same edge more than once.

* Note that a path of length zero consists of a single vertex.

> [!Info] Definition
> Let $n$ be a nonnegative integer and $G$ a directed graph. A *path* of length $n$ from $u$ to $v$ in $G$ is a sequence of edges $e_1, e_2, …, e_n$ of $G$ such that $e_1$ is associated with $(x_0, x_1)$, $e_2$ is associated with $(x_1, x_2)$, and so on, with $e_n$ associated with $(x_{n−1}, x_n)$, where $x_0 = u$ and $x_n = v$. When there are no multiple edges in the directed graph, this path is denoted by its vertex sequence $x_0, x_1, x_2, …, x_n$ . A path of length greater than zero that begins and ends at the same vertex is called a *circuit* or *cycle*. A path or circuit is called $simple$ if it does not contain the same edge more than once.

> [!Error] 10.4.3 Connectedness\ in Undirected Graphs

> [!Info] Definition: `graph connectedness`
> An undirected graph is called $connected$ if there is a path between every pair of distinct vertices of the graph. An undirected graph that is not $connected$ is called $disconnected$. We say that we disconnect a graph when we remove vertices or edges, or both, to produce a disconnected subgraph.

> [!Info] Theorem 1
> There is a simple path between every pair of distinct vertices of a connected undirected graph.

* **Connected Components**: A connected component of a graph $G$ is a connected subgraph of $G$ that is not a proper subgraph of another connected subgraph of $G$.
	* That is, a connected component of a graph $G$ is a maximal connected subgraph of $G$.
	* A graph $G$ that is not connected has two or more connected components that are disjoint and have $G$ as their union.

> [!Error] 10.4.4 How Connected is a Graph?

* Sometimes the removal from a graph of a vertex and all incident edges produces a subgraph with more connected components. Such vertices are called **cut vertices** (or **articulation points**). The removal of a cut vertex from a connected graph produces a subgraph that is not connected. Analogously, an edge whose removal produces a graph with more connected components than in the original graph is called a **cut edge** or **bridge**. Note that in a graph representing a computer network, a cut vertex and a cut edge represent an essential router and an essential link that cannot fail for all computers to be able to communicate.
---
* **Vertex Connectivity**: Not all graphs have cut vertices. For example, the complete graph $K_n$, where $n ≥ 3$, has no cut vertices. When you remove a vertex from $K_n$ and all edges incident to it, the resulting subgraph is the complete graph $K_{n−1}$, a connected graph. Connected graphs without cut vertices are called **nonseparable graphs**, and can be thought of as more connected than those with a cut vertex.
* We can extend this notion by deﬁning a more granulated measure of graph connectivity based on the minimum number of vertices that can be removed to disconnect a graph.
* A subset $V^′$ of the vertex set $V$ of $G = (V, E)$ is a **vertex cut**, or **separating set**, if $G − V^′$ is disconnected. We deﬁne the **vertex connectivity** of a noncomplete graph $G$, denoted by $𝜅(G)$, as the minimum number of vertices in a vertex cut.
* When $G$ is a complete graph, it has no vertex cuts, because removing any subset of its vertices and all incident edges still leaves a complete graph. Consequently, we cannot deﬁne $𝜅(G)$ as the minimum number of vertices in a vertex cut when $G$ is complete. Instead, we set $𝜅(K_n) = n − 1$, the number of vertices needed to be removed to produce a graph with a single vertex.
* Consequently, for every graph $G$, $𝜅(G)$ is minimum number of vertices that can be removed from $G$ to either disconnect $G$ or produce a graph with a single vertex. We have $0 ≤ 𝜅(G) ≤ n − 1$ if $G$ has $n$ vertices, $𝜅(G) = 0$ if and only if $G$ is disconnected or $G = K_1$ , and $𝜅(G) = n − 1$ if and only if $G$ is complete.
* The larger $𝜅(G)$ is, the more connected we consider $G$ to be. Disconnected graphs and $K_1$ have $𝜅(G) = 0$, connected graphs with cut vertices and $K_2$ have $𝜅(G) = 1$, graphs without cut vertices that can be disconnected by removing two vertices and $K_3$ have $𝜅(G) = 2$, and so on. We say that a graph is $k$**-connected** (or $k$**-vertex-connected**), if $𝜅(G) ≥ k$. A graph $G$ is $1$-connected if it is connected and not a graph containing a single vertex; a graph is $2$-connected, or biconnected, if it is nonseparable and has at least three vertices. Note that if $G$ is a $k$-connected graph, then $G$ is a $j$-connected graph for all $j$ with $0 ≤ j ≤ k$.
---
* **Edge Connectivity**: We can also measure the connectivity of a connected graph $G = (V, E)$ in terms of the minimum number of edges that we can remove to disconnect it.
* If a graph has a cut edge, then we need only remove it to disconnect $G$. If $G$ does not have a cut edge, we look for the smallest set of edges that can be removed to disconnect it.
* A set of edges $E^′$ is called an **edge cut** of $G$ if the subgraph $G − E^′$ is disconnected. The **edge connectivity** of a graph $G$, denoted by $𝜆(G)$, is the minimum number of edges in an edge cut of $G$.
* This deﬁnes $𝜆(G)$ for all connected graphs with more than one vertex because it is always possible to disconnect such a graph by removing all edges incident to one of its vertices.
* Note that $𝜆(G) = 0$ if $G$ is not connected. We also specify that $𝜆(G) = 0$ if $G$ is a graph consisting of a single vertex.
* It follows that if $G$ is a graph with $n$ vertices, then $0 ≤ 𝜆(G) ≤ n − 1$.
* Note that $𝜆(G) = n − 1$ where $G$ is a graph with $n$ vertices if and only if $G = K_n$, which is equivalent to the statement that $𝜆(G) ≤ n − 2$ when $G$ is not a complete graph.
---
* **An Inequality for Vertex and Edge Connectivity**
* When $G = (V, E)$ is a noncomplete connected graph with at least three vertices, the minimum degree of a vertex of $G$ is an upper bound for both the vertex connectivity of $G$ and the edge connectivity of $G$.
* That is, $𝜅(G) ≤ min_{v∈V}\ deg(v)$ and $𝜆(G) ≤ min_{v∈V}\ deg(v)$.
* To see this, observe that deleting all the neighbours of a ﬁxed vertex of minimum degree disconnects $G$, and deleting all the edges that have a ﬁxed vertex of minimum degree as an endpoint disconnects $G$.
* Note that $𝜅(G) ≤ 𝜆(G)$ when $G$ is a connected non-complete graph.
* Note also that $𝜅(K_n) = 𝜆(K_n) = min_{v∈V}\ deg(v) = n − 1$ when $n$ is a positive integer and that $𝜅(G) = 𝜆(G) = 0$ when $G$ is a disconnected graph.
* Putting these facts together establishes that for all graphs $G$, $𝜅(G) ≤ 𝜆(G) ≤ min_{v∈V}\ deg(v)$.

> [!Error] 10.4.5 Connectedness in Directed Graphs

* There are two notions of connectedness in directed graphs, depending on whether the directions of the edges are considered.

> [!Info] Definition
> A directed graph is $strongly\ connected$ if there is a path from $a$ to $b$ and from $b$ to $a$ whenever $a$ and $b$ are vertices in the graph.

> [!Info] Definition
> A directed graph is $weakly\ connected$ if there is a path between every two vertices in the underlying undirected graph.

* * For a directed graph to be strongly connected there must be a sequence of directed edges from any vertex in the graph to any other vertex. A directed graph can fail to be strongly connected but still be in “one piece” (as cleared by definition 5).
* That is, a directed graph is weakly connected if and only if there is always a path between two vertices when the directions of the edges are disregarded. Clearly, any strongly connected directed graph is also weakly connected.
---
* **Strong Components of a Directed Graph**
* The subgraphs of a directed graph $G$ that are strongly connected but not contained in larger strongly connected subgraphs, that is, the maximal strongly connected subgraphs, are called the **strongly connected components** or **strong components** of $G$.
* Note that if $a$ and $b$ are two vertices in a directed graph, their strong components are either the same or disjoint.

> [!Error] 10.4.7 Counting Paths between Vertices

* The number of paths between two vertices in a graph can be determined using its adjacency matrix.

> [!Info] Theorem 2
> Let $G$ be a graph with adjacency matrix $A$ with respect to the ordering $v_1, v_2, …, v_n$ of the vertices of the graph (with directed or undirected edges, with multiple edges and loops allowed). The number of diﬀerent paths of length $r$ from $v_i$ to $v_j$, where $r$ is a positive integer, equals the $(i, j)$th entry of $A^r$.

* Theorem 2 can be used
	* to ﬁnd the length of the shortest path between two vertices of a graph,
	* and it can also be used to determine whether a graph is connected.

##### 10.5 Euler and Hamilton Paths
> `pg: 11`
> `time req: 1' 13"`
> `time done: 46"`
> `performance: 158%`
>
> `questions: 68`
> `practice time req: 42"`

> [!Error] 10.5.2 Euler Paths and Circuits

> [!Info] Definition: `euler circuit`
> An Euler circuit in a graph $G$ is a simple circuit containing every edge of $G$. An Euler path in $G$ is a simple path containing every edge of $G$.

---
* **Necessary and Sufficient Conditions for Euler Circuits and Paths**
* What we can show is that every vertex must have even degree.
	* To do this, ﬁrst note that an Euler circuit begins with a vertex $a$ and continues with an edge incident with $a$, say $\{a, b\}$.
	* The edge $\{a, b\}$ contributes one to $deg(a)$. Each time the circuit passes through a vertex it contributes two to the vertex’s degree, because the circuit enters via an edge incident with this vertex and leaves via another such edge.
	* Finally, the circuit terminates where it started, contributing one to $deg(a)$.
	* Therefore, $deg(a)$ must be even, because the circuit contributes one when it begins, one when it ends, and two every time it passes through $a$ (if it ever does).
	* A vertex other than $a$ has even degree because the circuit contributes two to its degree each time it passes through the vertex.
	* We conclude that if a connected graph has an Euler circuit, then every vertex must have even degree.
* Is this necessary condition for the existence of an Euler circuit also suﬃcient? That is, must an Euler circuit exist in a connected multigraph if all vertices have even degree? This question can be settled aﬃrmatively with a construction. \[The proof was hard, and I didn't get it. Refer to page 730.\]

> [!Info] Theorem 1
> A connected multigraph with at least two vertices has an Euler circuit if and only if each of its vertices has even degree.

> [!Info] Theorem 2
> A connected multigraph has an Euler path but not an Euler circuit if and only if it has exactly two vertices of odd degree.

> [!Error] 10.5.3 Hamilton Paths and Circuits

> [!Info] Definition
> A simple path in a graph $G$ that passes through every vertex exactly once is called a $Hamilton\ path$, and a simple circuit in a graph $G$ that passes through every vertex exactly once is called a $Hamilton\ circuit$.
> That is, the simple path $x_0, x_1, …, x_{n−1}, x_n$ in the graph $G = (V, E)$ is a Hamilton path if $V = \{x_0, x_1, …, x_{n−1}, x_n\}$ and $x_i ≠ x_j$ for $0 ≤ i < j ≤ n$, and the simple circuit $x_0, x_1, …, x_{n−1}, x_n, x_0$ (with $n > 0$) is a Hamilton circuit if $x_0, x_1, …, x_{n−1}, x_n$ is a Hamilton path.

---
* **Conditions for the Existence of Hamilton Circuits**
* Is there a simple way to determine whether a graph has a Hamilton circuit or path? At ﬁrst, it might seem that there should be an easy way to determine this, because there is a simple way to answer the similar question of whether a graph has an Euler circuit.
* Surprisingly, there are no known simple necessary and suﬃcient criteria for the existence of Hamilton circuits.
* However, many theorems are known that give suﬃcient conditions for the existence of Hamilton circuits. Also, certain properties can be used to show that a graph has no Hamilton circuit.
* For instance, a graph with a vertex of degree one cannot have a Hamilton circuit, because in a Hamilton circuit, each vertex is incident with two edges in the circuit.
* Moreover, if a vertex in the graph has degree two, then both edges that are incident with this vertex must be part of any Hamilton circuit.
* Also, note that when a Hamilton circuit is being constructed and this circuit has passed through a vertex, then all remaining edges incident with this vertex, other than the two used in the circuit, can be removed from consideration.
* Furthermore, a Hamilton circuit cannot contain a smaller circuit within it.
---
* Although no useful necessary and suﬃcient conditions for the existence of Hamilton circuits are known, quite a few suﬃcient conditions have been found.
* Note that the more edges a graph has, the more likely it is to have a Hamilton circuit.
* Furthermore, adding edges (but not vertices) to a graph with a Hamilton circuit produces a graph with the same Hamilton circuit. So as we add edges to a graph, especially when we make sure to add edges to each vertex, we make it increasingly likely that a Hamilton circuit exists in this graph. Consequently, we would expect there to be suﬃcient conditions for the existence of Hamilton circuits that depend on the degrees of vertices being suﬃciently large.
---
* We state two of the most important suﬃcient conditions here.

> [!Info] Theorem 3: `Dirac's Theorem`
> If $G$ is a simple graph with $n$ vertices with $n ≥ 3$ such that the degree of every vertex in $G$ is at least $n/2$, then $G$ has a Hamilton circuit. 

> [!Info] Theorem 4: `Ore's Theorem`
> If $G$ is a simple graph with $n$ vertices with $n ≥ 3$ such that $deg(u) + deg(v) ≥ n$ for every pair of nonadjacent vertices $u$ and $v$ in $G$, then $G$ has a Hamilton circuit.

* Both Ore’s theorem and Dirac’s theorem provide suﬃcient conditions for a connected simple graph to have a Hamilton circuit. However, these theorems do not provide necessary conditions for the existence of a Hamilton circuit. For example, the graph $C_5$ has a Hamilton circuit but does not satisfy the hypotheses of either Ore’s theorem or Dirac’s theorem.
* The best algorithms known for ﬁnding a Hamilton circuit in a graph or determining that no such circuit exists have **exponential** worst-case time complexity (in the number of vertices of the graph). Finding an algorithm that solves this problem with polynomial worst-case time complexity would be a major accomplishment because it has been shown that this problem is NP-complete.

##### 10.6 Shortest-Path Problems
> `pg: 8`
> `time req: 53"`
> `time done: 12"`
> `performance: 441%`
>
> `questions: 31`
> `practice time req: 31"`

> [!Info] Theorem 1
> Dijkstra’s algorithm ﬁnds the length of a shortest path between two vertices in a connected simple undirected weighted graph.

> [!Info] Theorem 2
> Dijkstra’s algorithm uses $O(n^2)$ operations (additions and comparisons) to ﬁnd the length of a shortest path between two vertices in a connected simple undirected weighted graph with $n$ vertices.

##### 10.7 Planar Graph
> `pg: 8`
> `time req: 53"`
> `time done: 29"`
> `performance: 182%`
>
> `questions: 37`
> `practice time req: 31"`

> [!Error] 10.7.1 Introduction

> [!Info] Definition: `planar graphs`
> A graph is called $planar$ if it can be drawn in the plane without any edges crossing (where a crossing of edges is the intersection of the lines or arcs representing them at a point other than their common endpoint). Such a drawing is called a $planar\ representation$ of the graph.

* A graph may be planar even if it is usually drawn with crossings, because it may be possible to draw it in a diﬀerent way without crossings.
* We can show that a graph is planar by displaying a planar representation. It is harder to show that a graph is nonplanar.
---
* **Applications of Planar Graphs**
* Planarity of graphs plays an important role in the design of electronic circuits. We can model a circuit with a graph by representing components of the circuit by vertices and connections between them by edges. We can print a circuit on a single board with no connections crossing if the graph representing the circuit is planar. When this graph is not planar, we must turn to more expensive options. For example, we can partition the vertices in the graph representing the circuit into planar subgraphs. We then construct the circuit using multiple layers. We can construct the circuit using insulated wires whenever connections cross. In this case, drawing the graph with the fewest possible crossings is important.
* The planarity of graphs is also useful in the design of road networks. Suppose we want to connect a group of cities by roads. We can model a road network connecting these cities using a simple graph with vertices representing the cities and edges representing the highways connecting them. We can built this road network without using underpasses or overpasses if the resulting graph is planar.

> [!Error] 10.7.2 Euler's Formula

* A planar representation of a graph splits the plane into **regions**, including an unbounded region.
* Euler showed that all planar representations of a graph split the plane into the same number of regions. He accomplished this by ﬁnding a relationship among the number of regions, the number of vertices, and the number of edges of a planar graph.

> [!Info] Theorem 1: `Euler's Formula`
> Let $G$ be a connected planar simple graph with $e$ edges and $v$ vertices. Let $r$ be the number of regions in a planar representation of $G$. Then $r = e − v + 2$.

> [!Info] Corollary 1
> If $G$ is a connected planar simple graph with $e$ edges and $v$ vertices, where $v ≥ 3$, then $e ≤ 3v − 6$.

> [!Info] Corollary 2
> If $G$ is a connected planar simple graph, then $G$ has a vertex of degree not exceeding ﬁve.

> [!Info] Corollary 3
> If a connected planar simple graph has $e$ edges and $v$ vertices with $v ≥ 3$ and no circuits of length three, then $e ≤ 2v − 4$.

> [!Error] 10.7.3 Kuratowski's Theorem

* If a graph is planar, so will be any graph obtained by removing an edge $\{u, v\}$ and adding a new vertex $w$ together with edges $\{u, w\}$ and $\{w, v\}$. Such an operation is called an **elementary subdivision**. The graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are called **homeomorphic** if they can be obtained from the same graph by a sequence of elementary subdivisions.

> [!Info] Theorem 2: `Kuratowski's Theorem`
> A graph is nonplanar if and only if it contains a subgraph homeomorphic to $K_{3,3}$ or $K_5$.

##### 10.8 Graph Coloring
> `pg: 6`
> `time req: 39"`
> `time done: 22"`
> `performance: 177%`
>
> `questions: 46`
> `practice time req: 23"`

> [!Error] 10.8.1 Introduction

* Each map in the plane can be represented by a graph. To set up this correspondence, each region of the map is represented by a vertex. Edges connect two vertices if the regions represented by these vertices have a common border. Two regions that touch at only one point are not considered adjacent. The resulting graph is called the **dual graph** of the map. By the way in which dual graphs of maps are constructed, it is clear that any map in the plane has a planar dual graph.
* The problem of coloring the regions of a map is equivalent to the problem of coloring the vertices of the dual graph so that no two adjacent vertices in this graph have the same color. We now deﬁne a graph coloring.

> [!Info] Definition
> A $coloring$ of a simple graph is the assignment of a color to each vertex of the graph so that no two adjacent vertices are assigned the same color.

> [!Info] Definition
> The $chromatic\ number$ of a graph is the least number of colors needed for a coloring of this graph. The chromatic number of a graph $G$ is denoted by $𝜒(G)$. (Here $𝜒$ is the Greek letter chi.)

> [!Info] Theorem 1: `The Four Color Theorem`
> The chromatic number of a planar graph is no greater than four.

#### Chapter 11: Trees
> [!Summary]
> `sum page: 53`
> `sum time req: 5' 50"`

##### 11.1 Introduction to Trees
> `pg: 12`
> `time req: 1' 19"`
> `time done: 38"`
> `performance: 207%`
>
> `questions: 48`
> `practice time req: 46"`

> [!Info] Definition: `tree`
> A $tree$ is a connected undirected graph with no simple circuits.

* Because a tree cannot have a simple circuit, a tree cannot contain multiple edges or loops. Therefore any tree must be a simple graph.
* Any connected graph that contains no simple circuits is a tree. What about graphs containing no simple circuits that are not necessarily connected? These graphs are called forests and have the property that each of their connected components is a tree.

> [!Info] Theorem 1
> An undirected graph is a tree if and only if there is a unique simple path between any two of its vertices.

> [!Error] 11.1.1 Rooted Trees

* In many applications of trees, a particular vertex of a tree is designated as the root. Once we specify a root, we can assign a direction to each edge as follows. Because there is a unique path from the root to each vertex of the graph (by Theorem 1), we direct each edge away from the root. Thus, a tree together with its root produces a directed graph called a rooted tree.

> [!Info] Definition
> A $rooted\ tree$ is a tree in which one vertex has been designated as the root and every edge is directed away from the root.

* The terminology for trees has botanical and genealogical origins. Suppose that $T$ is a rooted tree. If $v$ is a vertex in $T$ other than the root, the **parent** of $v$ is the unique vertex $u$ such that there is a directed edge from $u$ to $v$. When $u$ is the parent of $v$, $v$ is called a **child** of $u$. Vertices with the same parent are called **siblings**. The **ancestors** of a vertex other than the root are the vertices in the path from the root to this vertex, excluding the vertex itself and including the root (that is, its parent, its parent’s parent, and so on, until the root is reached). The **descendants** of a vertex $v$ are those vertices that have $v$ as an ancestor. A vertex of a rooted tree is called a **leaf** if it has no children. Vertices that have children are called **internal vertices**. The root is an internal vertex unless it is the only vertex in the graph, in which case it is a leaf.
* If $a$ is a vertex in a tree, the **subtree** with $a$ as its root is the subgraph of the tree consisting of $a$ and its descendants and all edges incident to these descendants.

> [!Info] Definition
> A rooted tree is called an $m-ary$ tree if every internal vertex has no more than $m$ children. The tree is called a full $m-ary$ tree if every internal vertex has exactly $m$ children. An $m-ary$ tree with $m = 2$ is called a $binary\ tree$.

---
* **Ordered Rooted Tree**
* An ordered rooted tree is a rooted tree where the children of each internal vertex are ordered. Ordered rooted trees are drawn so that the children of each internal vertex are shown in order from left to right. Note that a representation of a rooted tree in the conventional way determines an ordering for its edges. We will use such orderings of edges in drawings without explicitly mentioning that we are considering a rooted tree to be ordered.
* In an ordered binary tree (usually called just a binary tree), if an internal vertex has two children, the ﬁrst child is called the **left child** and the second child is called the **right child**. The tree rooted at the left child of a vertex is called the **left subtree** of this vertex, and the tree rooted at the right child of a vertex is called the **right subtree** of the vertex.

> [!Error] 11.1.3 Properties of Trees

> [!Info] Theorem 2
> A tree with $n$ vertices has $n − 1$ edges.

> [!Info] Theorem 3
> A full $m-ary$ tree with $i$ internal vertices contains $n = mi + 1$ vertices.

> [!Info] Theorem 4
> Suppose that $T$ is a full $m-ary$ tree. Let $i$ be the number of internal vertices and $l$ the number of leaves in this tree. Once one of $n$, $i$, and $l$ is known, the other two quantities are determined.
> A full $m-ary$ tree with
>
> - $(i)$ $n$ vertices has $i = (n − 1)/m$ internal vertices and $l = [(m − 1)n + 1]/m$ leaves,
> - $(ii)$ $i$ internal vertices has $n = mi + 1$ vertices and $l = (m − 1)i + 1$ leaves,
> - $(iii)$ $l$ leaves has $n = (ml − 1)/(m − 1)$ vertices and $i = (l − 1)/(m − 1)$ internal vertices.

---
* **Balanced $m$-ary Trees**: It is often desirable to use rooted trees that are “balanced” so that the subtrees at each vertex contain paths of approximately the same length. Some deﬁnitions will make this concept clear.
* The **level** of a vertex $v$ in a rooted tree is the length of the unique path from the root to this vertex. The level of the root is deﬁned to be zero.
* The **height** of a rooted tree is the maximum of the levels of vertices. In other words, the height of a rooted tree is the length of the longest path from the root to any vertex.
* A rooted $m-ary$ tree of height $h$ is **balanced** if all leaves are at levels $h$ or $h − 1$.
---
* **A Bound for the Number of Leaves in an $m$-ary Tree**
* It is often useful to have an upper bound for the number of leaves in an $m-ary$ tree.

> [!Info] Theorem 5
> There are at most $m^h$ leaves in an $m-ary$ tree of height $h$.

> [!Info] Corollary 1
> If an $m-ary$ tree of height $h$ has $l$ leaves, then $h ≥ ⌈log_m l⌉$. If the $m-ary$ tree is full and balanced, then $h = ⌈log_m l⌉$.

##### 11.2 Applications of Trees
> `pg: 13`
> `time req: 1' 26"`
> `time done: 13"`
> `performance: 661%`
>
> `questions: 44`
> `practice time req: 50"`

> [!Error] 11.2.3 Decision Trees

> [!Info] Theorem 1
> A sorting algorithm based on binary comparisons requires at least $⌈\log_2 n!⌉$ comparisons.

> [!Info] Corollary 1
> The number of comparisons used by a sorting algorithm to sort $n$ elements based on binary comparisons is $Ω(n \log n)$.

> [!Info] Theorem 2
> The average number of comparisons used by a sorting algorithm to sort $n$ elements based on binary comparisons is $Ω(n \log n)$.

> [!Error] 11.2.4 Game Trees

> [!Info] Definition
> The $value\ of\ a\ vertex$ in a game tree is deﬁned recursively as:
>
> - $(i)$ the value of a leaf is the payoﬀ to the ﬁrst player when the game terminates in the position represented by this leaf.
> - $(ii)$ the value of an internal vertex at an even level is the maximum of the values of its children, and the value of an internal vertex at an odd level is the minimum of the values of its children.

> [!Info] Theorem 3
> The value of a vertex of a game tree tells us the payoﬀ to the ﬁrst player if both players follow the minmax strategy and play starts from the position represented by this vertex.

##### 11.3 Tree Traversal
> `pg: 12`
> `time req: 1' 19"`
> `time done: 50"`
> `performance: 158%`
>
> `questions: 34`
> `practice time req: 46"`

> [!Error] 11.3.2 Universal Address System

* To produce this ordering, we must ﬁrst label all the vertices. We do this recursively:
	1. Label the root with the integer $0$. Then label its $k$ children (at level $1$) from left to right with $1, 2, 3, … , k$.
	2. For each vertex $v$ at level $n$ with label $A$, label its $k_v$ children, as they are drawn from left to right, with $A.1, A.2, … , A.k_v$.
* Following this procedure, a vertex $v$ at level $n$, for $n ≥ 1$, is labeled $x_1\ .x_2\ .\ …\ .x_n$, where the unique path from the root to $v$ goes through the $x_1 st$ vertex at level $1$, the $x_2 nd$ vertex at level $2$, and so on. This labelling is called the **universal address system** of the ordered rooted tree.
* We can totally order the vertices using the lexicographic ordering of their labels in the universal address system. The vertex labeled $x_1\ .x_2\ .\ …\ .x_n$ is less than the vertex labeled $y_1\ .y_2\ .\ …\ .y_m$ if
	* there is an $i$, $0 ≤ i ≤ n$, with $x_1 = y_1$, $x_2 = y_2$, …, $x_{i−1} = y_{i−1}$, and $x_i < y_i$;
	* or if $n < m$ and $x_i = y_i$ for $i = 1, 2, … , n$.
- ![[Computer Science/discrete-math-images/11.3-universal-address-system.png]]

> [!Error] 11.3.3 Traversal Algorithms

> [!Info] Definition: `preorder traversal`
> Let $T$ be an ordered rooted tree with root $r$. If $T$ consists only of $r$, then $r$ is the $preorder\ traversal$ of $T$. Otherwise, suppose that $T_1$, $T_2$, …, $T_n$ are the subtrees at $r$ from left to right in $T$. The preorder traversal begins by visiting $r$. It continues by traversing $T_1$ in preorder, then $T_2$ in preorder, and so on, until $T_n$ is traversed in preorder.

* The preorder traversal of an ordered rooted tree gives the same ordering of the vertices as the ordering obtained using a universal address system.

> [!Info] Definition: `inorder traversal`
> Let $T$ be an ordered rooted tree with root $r$. If $T$ consists only of $r$, then $r$ is the $inorder\ traversal$ of $T$. Otherwise, suppose that $T_1$, $T_2$, …, $T_n$ are the subtrees at $r$ from left to right. The inorder traversal begins by traversing $T_1$ in inorder, then visiting $r$. It continues by traversing $T_2$ in inorder, then $T_3$ in inorder, … , and ﬁnally $T_n$ in inorder.

> [!Info] Definition: `postorder traversal`
> Let $T$ be an ordered rooted tree with root $r$. If $T$ consists only of $r$, then $r$ is the $postorder\ traversal$ of $T$. Otherwise, suppose that $T_1$, $T_2$, …, $T_n$ are the subtrees at $r$ from left to right. The postorder traversal begins by traversing $T_1$ in postorder, then $T_2$ in postorder, … , then $T_n$ in postorder, and ends by visiting $r$.

---
> [!Question] ChatGPT
> > why is preorder traversal used in making copies, instead of inorder and postorder?
>
> - When making copies, **preorder traversal** is useful if you want to create a copy of the tree that maintains the same structural organization as the original tree. The order in which nodes are visited corresponds directly to the order in which nodes are created in the copied tree.
> - In the context of making copies, **inorder traversal** is often used when you want the copied tree to be a sorted version of the original tree. This is useful in scenarios where you want to maintain the sorted order of elements.
> - **Postorder traversal** is less commonly used for copying because it creates a copy that may not preserve the same structural organization as the original tree. However, it might be suitable for certain scenarios where you need to process child nodes before the parent node.

* Postorder traversal is the best choice for applications where leaves need to be explored before internal vertices. Postorder explores leaves before internal vertices, so it is the best choice for deleting a tree because the vertices below the root of a subtree can be removed before the root of the subtree.
* Topological sorting is an example of an algorithm that can be eﬃciently implemented using postorder traversal.

> [!Error] 11.3.4 Infix, Prefix, and Postfix Notation

* We obtain the **preﬁx form** of an expression when we traverse its rooted tree in preorder. An expression in preﬁx notation (where each operation has a speciﬁed number of operands), is unambiguous, so no parentheses are needed in such an expression.

> [!Example] Example 6
> > What is the preﬁx form for $((x + y) ↑ 2) + ((x − 4)/3)$?
>
> We obtain the preﬁx form for this expression by traversing the binary tree that represents it in preorder. This produces $+\ ↑\ +\ x\ y\ 2\ /\ −\ x\ 4\ 3$.

* We obtain the postﬁx form of an expression by traversing its binary tree in postorder. No parentheses are needed.
* Because preﬁx and postﬁx expressions are unambiguous and because they can be evaluated easily without scanning back and forth, they are used extensively in computer science. Such expressions are especially useful in the construction of compilers.

##### 11.4 Spanning Trees
> `pg: 11`
> `time req: 1' 13"`
> `time done: 55"`
> `performance: 132%`
>
> `questions: 61`
> `practice time req: 42"`

> [!Error] 11.4.1 Introduction

> [!Info] Definition: `spanning tree`
> Let $G$ be a simple graph. A $spanning\ tree$ of $G$ is a subgraph of $G$ that is a tree containing every vertex of $G$.

* A simple graph with a spanning tree must be connected, because there is a path in the spanning tree between any two vertices.
* The converse is also true; that is, every connected simple graph has a spanning tree.

> [!Info] Theorem 1
> A simple graph is connected if and only if it has a spanning tree.

> [!Error] 11.4.2 Depth-First Search

* We can build a spanning tree for a connected simple graph using depth-ﬁrst search. We will form a rooted tree, and the spanning tree will be the underlying undirected graph of this rooted tree. Arbitrarily choose a vertex of the graph as the root. Form a path starting at this vertex by successively adding vertices and edges, where each new edge is incident with the last vertex in the path and a vertex not already in the path. Continue adding vertices and edges to this path as long as possible. If the path goes through all vertices of the graph, the tree consisting of this path is a spanning tree. However, if the path does not go through all vertices, more vertices and edges must be added. Move back to the next to last vertex in the path, and, if possible, form a new path starting at this vertex passing through vertices that were not already visited. If this cannot be done, move back another vertex in the path, that is, two vertices back in the path, and try again.
* Repeat this procedure, beginning at the last vertex visited, moving back up the path one vertex at a time, forming new paths that are as long as possible until no more edges can be added. Because the graph has a ﬁnite number of edges and is connected, this process ends with the production of a spanning tree. Each vertex that ends a path at a stage of the algorithm will be a leaf in the rooted tree, and each vertex where a path is constructed starting at this vertex will be an internal vertex.
* Depth-ﬁrst search is also called **backtracking**, because the algorithm returns to vertices previously visited to add paths.
* The edges selected by depth-ﬁrst search of a graph are called **tree edges**. All other edges of the graph must connect a vertex to an ancestor or descendant of this vertex in the tree. These edges are called **back edges**.
---
* We have explained how to ﬁnd a spanning tree of a graph using depth-ﬁrst search. However, our discussion so far has not brought out the recursive nature of depth-ﬁrst search. To help make the recursive nature of the algorithm clear, we need a little terminology. We say that we explore from a vertex $v$ when we carry out the steps of depth-ﬁrst search beginning when $v$ is added to the tree and ending when we have backtracked back to $v$ for the last time. The key observation needed to understand the recursive nature of the algorithm is that when we add an edge connecting a vertex $v$ to a vertex $w$, we ﬁnish exploring from $w$ before we return to $v$ to complete exploring from $v$.
---
* The procedure DFS constructs a spanning tree using $O(e)$, or $O(n^2)$, steps where $e$ and $n$ are the number of edges and vertices, respectively.

> [!Error] 11.4.3 Breadth-First Search

* We can also produce a spanning tree of a simple graph by the use of breadth-ﬁrst search.
* Again, a rooted tree will be constructed, and the underlying undirected graph of this rooted tree forms the spanning tree. Arbitrarily choose a root from the vertices of the graph. Then add all edges incident to this vertex. The new vertices added at this stage become the vertices at level $1$ in the spanning tree. Arbitrarily order them. Next, for each vertex at level $1$, visited in order, add each edge incident to this vertex to the tree as long as it does not produce a simple circuit. Arbitrarily order the children of each vertex at level $1$. This produces the vertices at level $2$ in the tree. Follow the same procedure until all the vertices in the tree have been added. The procedure ends because there are only a ﬁnite number of edges in the graph. A spanning tree is produced because we have produced a tree containing every vertex of the graph.
* The breadth-ﬁrst search algorithm uses $O(e)$ or $O(n^2)$ steps.
---
* **Breadth-First Search vs Depth-First Search**
* We have introduced two widely used algorithms for constructing spanning trees of graphs, breadth-ﬁrst search (BFS) and depth-ﬁrst search (DFS).
* Although both BFS and DFS can be used to solve the same problems, there are theoretical and practical reasons for choosing between them.
* To solve a particular type of problem one of these search algorithms can be easier to apply, or can provide more insight, than the other.
* For some problems, BFS can be easier to use than DFS because BFS partitions the vertices of a graph into levels, which tell us how far away vertices are from the root.
* Also, edges connect vertices at the same level or at adjoining levels.
* Generally, DFS is a better choice when we need to explore a graph by exploring deeper rather than by exploring the graph systematically level by level.
* The structure obtained when using DFS can also be used when solving problems.
* Both BFS and DFS are extensively used in practice. The choice for which to use often depends on implementation details, such as the data structures used. Time and space considerations are paramount, especially when the problems being solved involved huge graphs.
* Also, keep in mind that we often solve problems using graph searching without completing the task of ﬁnding a spanning tree.
* When we use BFS on a graph that is dense, we spend a lot of time and use a lot of space to explore the graph level by level. In such situations, it can be preferable to use DFS to quickly reach vertices far away from the root.
* For a sparse graph, however, it may be more eﬃcient to explore a graph level by level.

> [!Error] 11.4.4 Backtracking Applications

* There are problems that can be solved only by performing an exhaustive search of all possible solutions.
* One way to search systematically for a solution is to use a decision tree, where each internal vertex represents a decision and each leaf a possible solution.
* To ﬁnd a solution via backtracking, ﬁrst make a sequence of decisions in an attempt to reach a solution as long as this is possible. The sequence of decisions can be represented by a path in the decision tree.
* Once it is known that no solution can result from any further sequence of decisions, backtrack to the parent of the current vertex and work toward a solution with another series of decisions, if this is possible.
* The procedure continues until a solution is found, or it is established that no solution exists.

> [!Error] 11.4.5 Depth-First Search in Directed Graphs

* We can easily modify both depth-ﬁrst search and breadth-ﬁrst search so that they can run given a directed graph as input.
* However, the output will not necessarily be a spanning tree, but rather a **spanning forest**.
* In both algorithms we can add an edge only when it is directed away from the vertex that is being visited and to a vertex not yet added. If at a stage of either algorithm we ﬁnd that no edge exists starting at a vertex already added to one not yet added, the next vertex added by the algorithm becomes the root of a new tree in the spanning forest.

##### 11.5 Minimum Spanning Trees
> `pg: 5`
> `time req: 33"`
> `time done: 8"`
> `performance: 412%`
>
> `questions: 35`
> `practice time req: 19"`

> [!Error] 11.5.2 Algorithms for Minimum Spanning Trees

> [!Info] Definition: `minimum spanning tree`
> A $minimum\ spanning\ tree$ in a connected *weighted* graph is a spanning tree that has the smallest possible sum of weights of its edges.

#### Chapter 12: Boolean Algebra
> [!Summary]
> `sum page: 30`
> `sum time req: 3' 17"`

##### 12.1 Boolean Functions
> `pg: 7`
> `time req: 46"`
> `questions: 43`
> `practice time req: 27"`

##### 12.2 Representing Boolean Functions
> `pg: 3`
> `time req: 19"`
> `questions: 20`
> `practice time req: 11"`

##### 12.3 Logic Gates
> `pg: 6`
> `time req: 39"`
> `questions: 20`
> `practice time req: 23"`

##### 12.4 Minimization of Circuits
> `pg: 14`
> `time req: 1' 33"`
> `questions: 33`
> `practice time req: 54"`

#### Chapter 13: Modeling Computation
> [!Summary]
> `sum page: 43`
> `sum time req: 4' 43"`

##### 13.1 Languages and Grammars
> `pg: 9`
> `time req: 59"`
> `questions: 42`
> `practice time req: 35"`

##### 13.2 Finite-State Machines with Output
> `pg: 5`
> `time req: 33"`
> `questions: 25`
> `practice time req: 19"`

##### 13.3 Finite-State Machines with No Output
> `pg: 10`
> `time req: 1' 6"`
> `questions: 62`
> `practice time req: 39"`

##### 13.4 Language Recognition
> `pg: 9`
> `time req: 59"`
> `questions: 31`
> `practice time req: 35"`

##### 13.5 Turing Machines
> `pg: 10`
> `time req: 1' 6"`
> `questions: 32`
> `practice time req: 39"`
