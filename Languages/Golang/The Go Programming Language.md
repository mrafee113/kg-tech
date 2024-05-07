> [The Go Programming Language - Alan A. A. Donavan](https://www.oreilly.com/library/view/the-go-programming/9780134190570/)

> [!Example] Planning
> H = `total hours`
> hpd = `hours/day`
> mpd = `minutes/day`
> hpp = `hours/page`
> mpp = `minutes/page`
> wpp = `words/page`
> wpm = `words/minute`
> np = `number of pages`
> tnp = `total number of pages`
>
> Total number of pages (`tnp`): 366
> wpp = 500
> wpm = 150
> mpp = wpp / wpm = 500 / 150 = 3.33333
> H = tnp * mpp / 60 = 366 \* 3.33333 / 60 = 20.33333
> 
> > [!Info] Formula
> > hpp = 0.0555555
> > mpp = 3.33333
>
> 20.33333 hours, 1 hpd -> 21 days
> 15 Farvardin -> 5 Ordibehesht
>
> > [!Exmaple] Example
> > `Tutorial`
> > 	section page = 26
> > 	section time = 1' 26"

#### Preface
* The goals of the language and its accompanying tools were to be expressive, efficient in both compilation and execution, and effective in writing reliable and robust programs.
* Go bears a surface similarity to C and, like C, is a tool for professional programmers, achieving maximum effect with minimum means. But it is much more than an updated version of C. It borrows and adapts good ideas from many other languages, while avoiding features that have led to complexity and unreliable code. Its facilities for concurrency are new and efficient, and its approach to data abstraction and object-oriented programming is unusually flexible. It has automatic memory management or garbage collection.
* Go is especially well suited for building infrastructure like networked servers, and tools and systems for programmers, but it is truly a general-purpose language and finds use in domains as diverse as graphics, mobile applications, and machine learning. It has become popular as a replacement for untyped scripting languages because it balances expressiveness with safety: Go programs typically run faster than programs written in dynamic languages and suffer far fewer crashes due to unexpected type errors.
* Go is an open-source project, so source code for its compiler, libraries, and tools is freely available to anyone. Contributions to the project come from an active worldwide community.

#### The Origins of Go
* Like biological species, successful languages beget offspring that incorporate the advantages of their ancestors; interbreeding sometimes leads to surprising strengths; and, very occasionally, a radical new feature arises without precedent. We can learn a lot about why a language is the way it is and what environment it has been adapted for by looking at these influences.
* Go is sometimes described as a ‘‘C-like language,’’ or as ‘‘C for the 21st century.’’ From C, Go inherited its expression syntax, control-flow statements, basic data types, call by-value parameter passing, pointers, and above all, C’s emphasis on programs that compile to efficient machine code and cooperate naturally with the abstractions of current operating systems.

#### The Go Project
* All programming languages reflect the programming philosophy of their creators, which often includes a significant component of reaction to the perceived shortcomings of earlier languages. The Go project was borne of frustration with several software systems at Google that were suffering from an explosion of complexity. (This problem is by no means unique to Google.)
* As Rob Pike put it, ‘‘complexity is multiplicative’’: fixing a problem by making one part of the system more complex slowly but surely adds complexity to other parts. With constant pressure to add features and options and configurations, and to ship code quickly, it’s easy to neglect simplicity, even though in the long run simplicity is the key to good software.
* Simplicity requires more work at the beginning of a project to reduce an idea to its essence and more discipline over the lifetime of a project to distinguish good changes from bad or pernicious ones. With sufficient effort, a good change can be accommodated without compromising what Fred Brooks called the ‘‘conceptual integrity’’ of the design but a bad change cannot, and a pernicious change trades simplicity for its shallow cousin, convenience. Only through simplicity of design can a system remain stable, secure, and coherent as it grows.
* The Go project includes the language itself, its tools and standard libraries, and last but not least, a cultural agenda of radical simplicity. As a recent high-level language, Go has the benefit of hindsight, and the basics are done well: it has garbage collection, a package system, first-class functions, lexical scope, a system call interface, and immutable strings in which text is generally encoded in UTF-8. But it has comparatively few features and is unlikely to add more. For instance, it has no implicit numeric conversions, no constructors or destructors, no operator overloading, no default parameter values, no inheritance, no generics, no exceptions, no macros, no function annotations, and no thread-local storage. The language is mature and stable, and guarantees backwards compatibility: older Go programs can be compiled and run with newer versions of compilers and standard libraries.
* Go has enough of a type system to avoid most of the careless mistakes that plague programmers in dynamic languages, but it has a simpler type system than comparable typed languages. This approach can sometimes lead to isolated pockets of ‘‘untyped’’ programming within a broader framework of types, and Go programmers do not go to the lengths that C++ or Haskell programmers do to express safety properties as type-based proofs. But in practice Go gives programmers much of the safety and run-time performance benefits of a relatively strong type system without the burden of a complex one.
* Go encourages an awareness of contemporary computer system design, particularly the importance of locality. Its built-in data types and most library data structures are crafted to work naturally without explicit initialization or implicit constructors, so relatively few memory allocations and memory writes are hidden in the code. Go’s aggregate types (structs and arrays) hold their elements directly, requiring less storage and fewer allocations and pointer indirections than languages that use indirect fields. And since the modern computer is a parallel machine, Go has concurrency features based on CSP, as mentioned earlier. The variable-size stacks of Go’s lightweight threads or goroutines are initially small enough that creating one goroutine is cheap and creating a million is practical.

### 1. Tutorial
> `pg: 26`

* Go is a compiled language. The Go toolchain converts a source program and the things it depends on into instructions in the native machine language of a computer. These tools are accessed through a single command called go that has a number of subcommands. The simplest of these subcommands is run, which compiles the source code from one or more source files whose names end in .go, links it with libraries, then runs the resulting executable file.
* Go natively handles Unicode, so it can process text in all the world’s languages.
* `go run program.go`
* `go build program.go` saves the executable
* Let’s now talk about the program itself. Go code is organized into packages, which are similar to libraries or modules in other languages. A package consists of one or more `.go` source files in a single directory that define what the package does. *Each source file begins with a package declaration*, here package main, that states which package the file belongs to, followed by a list of other packages that it imports, and then the declarations of the program that are stored in that file.
* The Go standard library has over 100 packages for common tasks like input and output, sorting, and text manipulation. For instance, the `fmt` package contains functions for printing formatted output and scanning input. `Println` is one of the basic output functions in `fmt`; it prints one or more values, separated by spaces, with a newline character at the end so that the values appear as a single line of output.
* Package *main* is special. It defines a standalone executable program, not a library. Within package main the function *main* is also special—it’s where execution of the program begins. Whatever main does is what the program does. Of course, main will normally call upon functions in other packages to do much of the work, such as the function `fmt.Println`.
* We must tell the compiler what packages are needed by this source file; that’s the role of the *import* declaration that follows the package declaration.
* You must import exactly the packages you need. A program will not compile if there are missing imports or if there are unnecessary ones. This strict requirement prevents references to unused packages from accumulating as programs evolve.
* The import declarations must follow the package declaration. After that, a program consists of the declarations of functions, variables, constants, and types; for the most part, the order of declarations does not matter.
* Go does not require semicolons at the ends of statements or declarations, except where two or more appear on the same line. In effect, newlines following certain tokens are converted into semicolons, so where newlines are placed matters to proper parsing of Go code. For instance, the opening brace { of the function must be on the same line as the end of the func declaration, not on a line by itself, and in the expression x + y, a newline is permitted after but not before the + operator.
* Go takes a strong stance on code formatting. The `gofmt` tool rewrites code into the standard format, and the `go` tool’s `fmt` subcommand applies `gofmt` to all the files in the specified package, or the ones in the current directory by default. All Go source files in the book have been run through `gofmt`, and you should get into the habit of doing the same for your own code. Declaring a standard format by fiat eliminates a lot of pointless debate about trivia and, more importantly, enables a variety of automated source code transformations that would be infeasible if arbitrary formatting were allowed.

> [!Error] 1.2 Command-Line Arguments

* The `os` package provides functions and other values for dealing with the operating system in a platform-independent fashion. Command-line arguments are available to a program in a variable named `Args` that is part of the `os` package; thus its name anywhere outside the `os` package is `os.Args`.
* The variable `os.Args` is a slice of strings.
* The first element of `os.Args`, `os.Args[0]`, is the name of the command itself.
* Comments begin with `//`. All text from a `//` to the end of the line is commentary for programmers and is ignored by the compiler.
	* By convention, we describe each package in a comment immediately preceding its package declaration;
	* for a main package, this comment is one or more complete sentences that describe the program as a whole.
* The for loop is the only loop statement in Go. It has a number of forms, one of which is illustrated here:
	```go
	for initialization; condition; post {
		// zero or more statements
	}
	```
* The optional initialization statement is executed before the loop starts. If it is present, it must be a simple statement, that is, a short variable declaration, an increment or assignment statement, or a function call. The condition is a boolean expression that is evaluated at the beginning of each iteration of the loop; if it evaluates to true, the statements controlled by the loop are executed. The post statement is executed after the body of the loop, then the condition is evaluated again. The loop ends when the condition becomes false.
* Any of these parts may be omitted. If there is no initialization and no post, the semicolons may also be omitted.
* If the condition is omitted entirely in any of these forms, the loop is infinite, though loops of this form may be terminated in some other way, like a break or return statement.
	```go
	// a traditional while loop
	for condition {
		// ...
	}
	
	// a traditional infinite loop
	for {
		// ...
	}
	```
* Another form of the for loop iterates over a range of values from a data type like a string or a slice.
	```go
	for _, arg := range os.Args[2:] {
		s += arg
	}
	```
* In each iteration of the loop, range produces a pair of values: the index and the value of the element at that index. In this example, we don’t need the index, but the syntax of a range loop requires that if we deal with the element, we must deal with the index too. One idea would be to assign the index to an obviously temporary variable like temp and ignore its value, but Go does not permit unused local variables, so this would result in a compilation error.
* The solution is to use the blank identifier, whose name is _ (that is, an underscore). The blank identifier may be used whenever syntax requires a variable name but program logic does not.
* There are several ways to declare a string variable; these are all equivalent:
	```go
	s := ""
	var s string
	var s = ""
	var s string = ""
	```
* Why should you prefer one form to another?
	* The first form, a short variable declaration, is the most compact, but it may be used only within a function, not for package-level variables.
	* The second form relies on default initialization to the zero value for strings, which is `""`.
	* The third form is rarely used except when declaring multiple variables.
	* The fourth form is explicit about the variable’s type, which is redundant when it is the same as that of the initial value but necessary in other cases where they are not of the same type.
	* In practice, you should generally use one of the first two forms, with explicit initialization to say that the initial value is important and implicit initialization to say that the initial value doesn’t matter.
* The `+=` statement makes a new string by concatenating the old string and the next argument, then assigns the new string to s. The old contents of s are no longer in use, so they will be garbage-collected in due course. If the amount of data involved is large, this could be costly. A simpler and more efficient solution would be to use the `Join` function from the strings package.
	```go
	fmt.Println(strings.Join(os.Args[1:]))
	```

> [!Error] 1.3 Finding Duplicate Lines

* The order of map iteration is not specified, but in practice it is random, varying from one run to another. This design is intentional, since it prevents programs from relying on any particular ordering where none is guaranteed.
* The program uses a short variable declaration to create a new variable input that refers to a `bufio.Scanner`: `input := bufio.NewScanner(os.Stdin)`
* The scanner reads from the program’s standard input. Each call to `input.Scan()` reads the next line and removes the newline character from the end; the result can be retrieved by calling `input.Text()`. The Scan function returns true if there is a line and false when there is no more input.
* The function `os.Open` returns two values. The first is an open file (`*os.File`) that is used in subsequent reads by the Scanner.
* Notice that the call to `countLines` precedes its declaration. Functions and other package-level entities may be declared in any order.
* `io/ioutil.ReadFile` returns a byte slice that must be converted into a string so it can be split by `strings.Split`.
* Under the covers, `bufio.Scanner`, `ioutil.ReadFile`, and `ioutil.WriteFile` use the Read and Write methods of `*os.File`, but it’s rare that most programmers need to access those lower-level routines directly. The higher-level functions like those from `bufio` and `io/ioutil` are easier to use.

### 2. Program Structure
> `pg: 24`
> `time req: 1' 20"`

> [!Error] 2.1 Names

* The names of Go functions, variables, constants, types, statement labels, and packages follow a simple rule: a name begins with a letter (that is, anything that Unicode deems a letter) or an underscore and may have any number of additional letters, digits, and underscores. It's also CaseSensitive
* syntax:
	* keywords
		* `break`,       `default`,        `func`,    `interface`, `select`,
		* `case`,         `defer`,            `go`,        `map`,            `struct`,
		* `chan`,         `else`,              `goto`,    `package`,     `switch`,
		* `const`,       `fallthrough`, `if`,        `range`,         `type`,
		* `continue`, `for`,                `import`, `return`,       `var`
	* constants: `true`, `false`, `iota`, `nil`
	* types:
		* `int`,         `int8`,      `int16`,           `int32`,       `int64`
		* `uint`,       `uint8`,    `uint16`,         `uint32`,      `uint64`, `uintptr`,
		* `float32`, `float64`, `complex128`, `complex64`,
		* `bool`,       `byte`,      `rune`,             `string`,      `error`
	* functions:
		* `make`, `len`, `cap`, `new`, `append`, `copy`, `close`, `delete`,
		* `complex`, `real`, `imag`,
		* `panic`, `recover`
	* These names - constants, types, and functions - are not reserved, so you may use them in declarations.
* If an entity is declared within a function, it is local to that function. If declared outside of a function, however, it is visible in all files of the package to which it belongs. The case of the first letter of a name determines its visibility across package boundaries. If the name begins with an upper-case letter, it is exported, which means that it is visible and accessible outside of its own package and may be referred to by other parts of the program, as with `Printf` in the `fmt` package. Package names themselves are always in lower case.
* There is no limit on name length, but convention and style in Go programs lean toward short names, especially for local variables with small scopes; you are much more likely to see variables named `i` than `theLoopIndex`. **Generally, the larger the scope of a name, the longer and more meaningful it should be.**
* Stylistically, Go programmers use ‘‘camel case’’ when forming names by combining words; that is, interior capital letters are preferred over interior underscores. The letters of acronyms and initialisms like `ASCII` and `HTML` are always rendered in the same case, so a function might be called `htmlEscape`, `HTMLEscape`, or `escapeHTML`, but not `escapeHtml`.

> [!Error] 2.2 Declarations

* A *declaration* names a program entity and specifies some or all of its properties. There are four major kinds of declarations: `var`, `const`, `type`, and `func`.
* A Go program is stored in one or more files whose names end in `.go`. Each file begins with a package declaration that says what package the file is part of. The package declaration is followed by any import declarations, and then a sequence of package-level declarations of types, variables, constants, and functions, in any order.
* The name of each package-level entity is visible not only throughout the source file that contains its declaration, but throughout all the files of the package. By contrast, local declarations are visible only within the function in which they are declared and perhaps only within a small part of it.

> [!Error] 2.3 Variables

* A var declaration creates a variable of a particular type, attaches a name to it, and sets its initial value.
* `var name type = expression`
* Either the type or the = expression part may be omitted, but not both.
	* If the type is omitted, it is determined by the initializer expression.
	* If the expression is omitted, the initial value is the zero value for the type, which is
		* `0` for numbers,
		* `false` for booleans,
		* `""` for strings,
		* and `nil` for interfaces and reference types (slice, pointer, map, channel, function).
	* The zero value of an aggregate type like an array or a struct has the zero value of all of its elements or fields.
* The zero-value mechanism ensures that a variable always holds a well-defined value of its type; in Go there is no such thing as an uninitialized variable. This simplifies code and often ensures sensible behavior of boundary conditions without extra work.
* Go programmers often go to some effort to make the zero value of a more complicated type meaningful, so that variables begin life in a useful state.
* It is possible to declare and optionally initialize a set of variables in a single declaration, with a matching list of expressions. Omitting the type allows declaration of multiple variables of different types. Initializers may be literal values or arbitrary expressions. Package-level variables are initialized before main begins, and local variables are initialized as their declarations are encountered during function execution. A set of variables can also be initialized by calling a function that returns multiple values

> [!subsubsection] 2.3.1 Short Variable Declarations

* Within a function, an alternate form called a short variable declaration may be used to declare and initialize **local** variables.
* It takes the form `name := expression`, and the type of name is determined by the type of expression.
* Because of their brevity and flexibility, short variable declarations are used to declare and initialize the majority of local variables.
* A var declaration tends to be reserved for local variables that need an explicit type that differs from that of the initializer expression, **or** for when the variable will be assigned a value later and its initial value is unimportant.
* As with var declarations, multiple variables may be declared and initialized in the same short variable declaration, **but** declarations with multiple initializer expressions should be used only when they help readability, such as for short and natural groupings like the initialization part of a for loop.
* Keep in mind that `:=` is a declaration, whereas `=` is an assignment. A multi-variable declaration should not be confused with a tuple assignment, in which each variable on the left-hand side is assigned the corresponding value from the right-hand side.
* One subtle but important point: a short variable declaration does not necessarily declare all the variables on its left-hand side. If some of them were already declared in the same lexical block, then the short variable declaration acts like an assignment to those variables.
	* **A short variable declaration must declare at least one new variable, however!**
	* The fix is to use an ordinary assignment for the second statement.

> [!subsubsection] 2.3.2 Pointers

* A pointer value is the address of a variable. A pointer is thus the location at which a value is stored. Not every value has an address, but every variable does. With a pointer, we can read or update the value of a variable indirectly, without using or even knowing the name of the variable, if indeed it has a name.
* If a variable is declared `var x int`, the expression `&x` (‘‘address of x’’) yields a pointer to an integer variable, that is, a value of type `*int`, which is pronounced ‘‘pointer to int.’’ If this value is called `p`, we say ‘‘p points to x,’’ or equivalently ‘‘p contains the address of x.’’
* The variable to which `p` points is written `*p`. The expression `*p` yields the value of that variable, an int, but since `*p` denotes a variable, it may also appear on the left-hand side of an assignment, in which case the assignment updates the variable.
* Each component of a variable of aggregate type—a field of a struct or an element of an array—is also a variable and thus has an address too.
* Variables are sometimes described as addressable values. Expressions that denote variables are the only expressions to which the *address-of* operator `&` may be applied.
* The zero value for a pointer of any type is `nil`. The test `p != nil` is true if `p` points to a variable. Pointers are comparable; two pointers are equal if and only if they point to the same variable or both are `nil`.
* It is perfectly safe for a function to return the address of a local variable.
* Because a pointer contains the address of a variable, passing a pointer argument to a function makes it possible for the function to update the variable that was indirectly passed.
* Each time we take the address of a variable or copy a pointer, we create new aliases or ways to identify the same variable. Pointer aliasing is useful because it allows us to access a variable without using its name, but this is a double-edged sword: to find all the statements that access a variable, we have to know all its aliases. It’s not just pointers that create aliases; aliasing also occurs when we copy values of other reference types like slices, maps, and channels, and even structs, arrays, and interfaces that contain these types.

> [!subsubsection] 2.3.3 The new Function

* Another way to create a variable is to use the built-in function new. The expression `new(T)` creates an unnamed variable of type `T`, initializes it to the zero value of `T`, and returns its address, which is a value of type `*T`.
* Each call to new returns a distinct variable with a unique address. There is one exception to this rule: two variables whose type carries no information and is therefore of size zero, such as `struct{}` or `[0]int`, **may**, depending on the implementation, have the same address.

> [!subsubsection] 2.3.4 Lifetime of Variables

* The lifetime of a variable is the interval of time during which it exists as the program executes.
* The lifetime of a package-level variable is the entire execution of the program.
* By contrast, local variables have dynamic lifetimes: a new instance is created each time the declaration statement is executed, and the variable lives on until it becomes unreachable, at which point its storage may be recycled.
* Function parameters and results are local variables too; they are created each time their enclosing function is called.
* How does the garbage collector know that a variable’s storage can be reclaimed? The full story is much more detailed than we need here, but the basic idea is that every package-level variable, and every local variable of each currently active function, can potentially be the start or root of a path to the variable in question, following pointers and other kinds of references that ultimately lead to the variable. If no such path exists, the variable has become unreachable, so it can no longer affect the rest of the computation.
* Because the lifetime of a variable is determined only by whether or not it is reachable, a local variable may outlive a single iteration of the enclosing loop. It may continue to exist even after its enclosing function has returned.
* Garbage collection is a tremendous help in writing correct programs, but it does not relieve you of the burden of thinking about memory. You don’t need to explicitly allocate and free memory, but to write efficient programs you still need to be aware of the lifetime of variables.

> [!Error] 2.4 Assignments

* The value held by a variable is updated by an assignment statement, which in its simplest form has a variable on the left of the `=` sign and an expression on the right.
* Each of the arithmetic and bitwise binary operators has a corresponding *assignment operator*.

> [!subsubsection] 2.4.1 Tuple Assignments

* Another form of assignment, known as *tuple assignment*, allows several variables to be assigned at once.
	* All of the right-hand side expressions are evaluated before any of the variables are updated, making this form most useful when some of the variables appear on both sides of the assignment,
	* as happens, for example, when swapping the values of two variables.
* As a matter of style, avoid the tuple form if the expressions are complex; a sequence of separate statements is easier to read.

> [!subsubsection] 2.4.2 Assignability

* There are many places in a program where an assignment occurs implicitly:
	* a function call implicitly assigns the argument values to the corresponding parameter variables;
	* a return statement implicitly assigns the return operands to the corresponding result variables;
	* and a literal expression for a composite type such as this slice `medals := []string{"gold", "silver", "bronze"}` implicitly assigns each element.
* The elements of maps and channels, though not ordinary variables, are also subject to similar implicit assignments.
* An assignment, explicit or implicit, is always legal if the left-hand side (the variable) and the right-hand side (the value) have the same type. More generally, the assignment is legal only if the value is *assignable* to the type of the variable.
* Whether two values may be compared with `==` and `!=` is related to assignability: in any comparison, the first operand must be assignable to the type of the second operand, or vice versa. As with assignability, we’ll explain the relevant cases for comparability when we present each new type.

> [!error] 2.5 Type Declarations

* The type of a variable or expression defines the characteristics of the values it may take on, such as their size (number of bits or number of elements, perhaps), how they are represented internally, the intrinsic operations that can be performed on them, and the methods associated with them.
* A type declaration defines a new named type that has the same underlying type as an existing type. The named type provides a way to separate different and perhaps incompatible uses of the underlying type so that they can’t be mixed unintentionally.
	* `type name underlying-type`
* Type declarations most often appear at package level, where the named type is visible throughout the package, and if the name is exported, it’s accessible from other packages as well.
```go
type Celsius float64
type Fahrenheit float64
func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }
```
* This package defines two types, Celsius and Fahrenheit, for the two units of temperature. Even though both have the same underlying type, `float64`, they are not the same type, so they cannot be compared or combined in arithmetic expressions.
* An explicit type conversion like `Celsius(t)` or `Fahrenheit(t)` is required to convert from a `float64`. `Celsius(t)` and `Fahrenheit(t)` are conversions, not function calls. They don’t change the value or representation in any way, but they make the change of meaning explicit.
* For every type `T`, there is a corresponding conversion operation `T(x)` that converts the value `x` to type `T`. A conversion from one type to another is allowed if both have the same underlying type, or if both are unnamed pointer types that point to variables of the same underlying type; these conversions change the type but not the representation of the value.
* Conversions are also allowed between numeric types, and between string and some slice types, as we will see in the next chapter. These conversions may change the representation of the value. For instance, converting a floating-point number to an integer discards any fractional part, and converting a string to a `[]byte` slice allocates a copy of the string data. In any case, a conversion never fails at run time.
* The underlying type of a named type determines its structure and representation, and also the set of intrinsic operations it supports, which are the same as if the underlying type had been used directly.
* Comparison operators like `==` and `<` can also be used to compare a value of a named type to another of the same type, or to a value of the underlying type. But two values of different named types cannot be compared directly.

> [!Error] 2.6 Packages and Files

* Packages in Go serve the same purposes as libraries or modules in other languages, supporting modularity, encapsulation, separate compilation, and reuse. The source code for a package resides in one or more .go files, usually in a directory whose name ends with the import path.
* Each package serves as a separate *name space* for its declarations. Within the image package, for example, the identifier `Decode` refers to a different function than does the same identifier in the `unicode/utf16` package. To refer to a function from outside its package, we must *qualify* the identifier to make explicit whether we mean `image.Decode` or `utf16.Decode`.
* The doc comment immediately preceding the package declaration documents the package as a whole. Conventionally, it should start with a summary sentence in the style illustrated. Only one file in each package should have a package doc comment. Extensive doc comments are often placed in a file of their own, conventionally called `doc.go`.

> [!subsubsection] 2.6.1 Imports

* Within a Go program, every package is identified by a unique string called its import path.
* These are the strings that appear in an import declaration.
* The language specification doesn’t define where these strings come from or what they mean; it’s up to the tools to interpret them.
* When using the go tool, an import path denotes a directory containing one or more Go source files that together make up the package.
* In addition to its import path, each package has a package name, which is the short (and not necessarily unique) name that appears in its package declaration.
* By convention, a package’s name matches the last segment of its import path.
* The import declaration binds a short name to the imported package that may be used to refer to its contents throughout the file. By default, the short name is the package name but an import declaration may specify an alternative name to avoid a conflict.

> [!subsubsection] 2.6.2 Package Initialization

* Package initialization begins by initializing package-level variables in the order in which they are declared, except that dependencies are resolved first:
	```go
	var a = b + c // a initialized third, to 3
	var b = f()   // b initialized second, to 2, by calling f
	var c = 1     // c initialized first, to 1
	func f() int { return c + 1 }
	```
* If the package has multiple `.go` files, they are initialized in the order in which the files are given to the compiler; the go tool sorts `.go` files by name before invoking the compiler.
* Each variable declared at package level starts life with the value of its initializer expression, if any, but for some variables, like tables of data, an initializer expression may not be the simplest way to set its initial value. In that case, the init function mechanism may be simpler. Any file may contain any number of functions whose declaration is just func `init() { /* ... */ }`. Such init functions can’t be called or referenced, but otherwise they are normal functions. Within each file, init functions are automatically executed when the program starts, in the order in which they are declared.
* One package is initialized at a time, in the order of imports in the program, dependencies first, so a package p importing q can be sure that q is fully initialized before p’s initialization begins. Initialization proceeds from the bottom up; the main package is the last to be initialized. In this manner, all packages are fully initialized before the application’s main function begins.

> [!Error] 2.7 Scope

* A declaration associates a name with a program entity, such as a function or a variable. The scope of a declaration is the part of the source code where a use of the declared name refers to that declaration.
* Don’t confuse scope with lifetime. The scope of a declaration is a region of the program text; it is a compile-time property. The lifetime of a variable is the range of time during execution when the variable can be referred to by other parts of the program; it is a run time property.
* A **syntactic block** is a sequence of statements enclosed in braces like those that surround the body of a function or loop.
	* A name declared inside a syntactic block is not visible outside that block.
	* The block encloses its declarations and determines their scope.
	* We can generalize this notion of blocks to include other groupings of declarations that are not explicitly surrounded by braces in the source code; we’ll call them all **lexical blocks**.
	* There is a lexical block for the entire source code, called the **universe block**; for each *package*; for each *file*; for each *for*, *if*, and *switch* statement; for each *case* in a switch or select statement; and, of course, for each explicit *syntactic block*.
* A declaration’s *lexical block* determines its scope, which may be large or small.
	* The declarations of *built-in types*, *functions*, and *constants* like `int`, `len`, and `true` are in the *universe block* and can be referred to throughout the entire program.
	* Declarations outside any function, that is, at package level, can be referred to from any file in the same package.
	* Imported packages, such as `fmt`, are declared at the file level, so they can be referred to from the same file, but not from another file in the same package without another import.
	* Many declarations, are local, so they can be referred to only from within the same function or perhaps just a part of it.
* The scope of a control-flow label, as used by `break`, `continue`, and `goto` statements, is the entire enclosing function.
* A program may contain multiple declarations of the same name so long as each declaration is in a different lexical block. Don’t overdo it, though; the larger the scope of the redeclaration, the more likely you are to surprise the reader.
* When the compiler encounters a reference to a name, it looks for a declaration, starting with the innermost enclosing lexical block and working up to the universe block. If the compiler finds no declaration, it reports an ‘‘undeclared name’’ error. If a name is declared in both an outer block and an inner block, the inner declaration will be found first. In that case, the inner declaration is said to shadow or hide the outer one, making it inaccessible.

> [!Warning] Read about implicit Blocks.

> [!Important] Scopes are actually tricky and important!

### 3. Basic Data Types
> `pg: 30`
> `time req: 1' 40"`

> [!Error] 3.1 Integers

* The type `rune` is an synonym for `int32` and conventionally indicates that a value is a *Unicode code point*. The two names may be used interchangeably.
* Similarly, the type `byte` is an synonym for `uint8`, and emphasizes that the value is a piece of raw data rather than a small numeric quantity.
* Finally, there is an unsigned integer type `uintptr`, whose width is not specified but is sufficient to hold all the bits of a pointer value. The `uintptr` type is used only for low-level programming, such as at the boundary of a Go program with a C library or an operating system.
* Regardless of their size, `int`, `uint`, and `uintptr` are different types from their explicitly sized siblings. Thus int is not the same type as `int32`, even if the natural size of integers is 32 bits, and an explicit conversion is required to use an `int` value where an `int32` is needed, and vice versa.
* Go’s binary operators for arithmetic, logic, and comparison are listed here in order of decreasing precedence:
	```go
	*  /  % << >> &  &^
	+  -  | ^
	== != < <= >  >=
	&&
	||
	```
* Each operator in the first two lines of the table above, for instance `+`, has a corresponding assignment operator like `+=` that may be used to abbreviate an assignment statement.
* The remainder operator `%` applies only to integers. The behavior of `%` for negative numbers varies across programming languages. In Go, the sign of the remainder is always the same as the sign of the dividend, so `-5%3` and `-5%-3` are both `-2`.
* The behavior of `/` depends on whether its operands are integers, so `5.0/4.0` is `1.25`, but `5/4` is `1` because integer division truncates the result toward zero.
* If the result of an arithmetic operation, whether signed or unsigned, has more bits than can be represented in the result type, it is said to overflow. The high-order bits that do not fit are silently discarded. If the original number is a signed type, the result could be negative.
* All values of basic type—booleans, numbers, and strings—are comparable, meaning that two values of the same type may be compared using the `==` and `!=` operators. Furthermore, integers, floating-point numbers, and strings are ordered by the comparison operators.
	* The values of many other types are not comparable, and no other types are ordered.
* For integers, `+x` is a shorthand for `0+x` and `-x` is a shorthand for `0-x`; for floating-point and complex numbers, `+x` is just `x` and `-x` is the negation of `x`.
* Go also provides the following bitwise binary operators:
	```go
	&   AND
	|   OR
	^   XOR
	&^  AND NOT (bit clear)
	<<  left shift
    >>  right shift
	```
	* The operator `^` is bitwise exclusive OR (XOR) when used as a binary operator, but when used as a unary prefix operator it is bitwise negation or complement; that is, it returns a value with each bit in its operand inverted.
	* The `&^` operator is bit clear (AND NOT): in the expression `z = x &^ y`, each bit of `z` is `0` if the corresponding bit of `y` is `1`; other wise it equals the corresponding bit of `x`.
* Rune literals are written as a character within single quotes. The simplest example is an ASCII character like `'a'`, but it’s possible to write any Unicode code point either directly or with numeric escapes, as we will see shortly. Runes are printed with `%c`, or with `%q` if quoting is desired:
	```go
	ascii := 'a'
	unicode := 'D'
	newline := '\n'
	fmt.Printf("%d %[1]c %[1]q\n", ascii)   // "97 a 'a'"
	fmt.Printf("%d %[1]c %[1]q\n", unicode) // "22269 D 'D'"
	fmt.Printf("%d %[1]q\n", newline)       // "10 '\n'"
	```

> [!Error] 3.2 Floating-Point Numbers

* Go provides two sizes of floating-point numbers, `float32` and `float64`. Their arithmetic properties are governed by the `IEEE 754` standard implemented by all modern CPUs.
* Values of these numeric types range from tiny to huge. The limits of floating-point values can be found in the `math` package. The constant `math.MaxFloat32`, the largest `float32`, is about `3.4e38`, and `math.MaxFloat64` is about `1.8e308`. The smallest positive values are near `1.4e-45` and `4.9e-324`, respectively.
* A `float32` provides approximately six decimal digits of precision, whereas a `float64` provides about `15` digits; `float64` should be preferred for most purposes because `float32` computations accumulate error rapidly unless one is quite careful, and the smallest positive integer that cannot be exactly represented as a `float32` is not large:
	```go
	var f float32 = 16777216 // 1 << 24
	fmt.Println(f == f+1)    // "true"!
	```
* Floating-point numbers can be written literally using decimals, like this:
	```go
	const e = 2.71828 // (approximately)
	f := .707         // 0.707
	f := 1.           // 1.0
	```
* Very small or very large numbers are better written in scientific notation, with the letter `e` or `E` preceding the decimal exponent:
	```go
	const Avogadro = 6.02214129e23
	const Planck   = 6.62606957e-34
	```
* In addition to a large collection of the usual mathematical functions, the `math` package has functions for creating and detecting the special values defined by `IEEE 754`: the positive and negative infinities, which represent numbers of excessive magnitude and the result of division by zero; and `NaN` (‘‘not a number’’), the result of such mathematically dubious operations as `0/0` or `Sqrt(-1)`.
	```go
	var z float64
	fmt.Println(z, -z, 1/z, -1/z, z/z) // "0 -0 +Inf -Inf NaN"
	```
* The function `math.IsNaN` tests whether its argument is a not-a-number value, and `math.NaN` returns such a value.
* It’s tempting to use `NaN` as a sentinel value in a numeric computation, but testing whether a specific computational result is equal to `NaN` is fraught with peril because any comparison with `NaN` always yields false:
	```go
	nan := math.NaN()
	fmt.Println(nan == nan, nan < nan, nan > nan)
	// "false false false"
	```

> [!Error] 3.4 Booleans

* A value of type `bool`, or *boolean*, has only two possible values, `true` and `false`.
* The unary operator `!` is logical negation, so `!true` is `false`, although as a matter of style, we always simplify redundant boolean expressions like `x==true` to `x`.
* There is no implicit conversion from a boolean value to a numeric value like `0` or `1`, or vice versa. Only in the `if` and such clauses is a numeric value evaluated as a boolean.

> [!Error] 3.5 Strings

* A string is an immutable sequence of `bytes`.
* Strings may contain arbitrary data, including `bytes` with value `0`, but usually they contain human-readable text.
* Text strings are conventionally interpreted as `UTF-8`-encoded sequences of Unicode code points (`runes`).
* The built-in `len` function returns the number of `bytes` (not `runes`) in a string, and the `index` operation `s[i]` retrieves the `i`-th byte of string `s`, where `0 ≤ i < len(s)`.
```go
s := "hello, world"
fmt.Println(len(s))     // "12"
fmt.Println(s[0], s[7]) // "104 119" ('h' and 'w')
```
* Strings may be compared with comparison operators like `==` and `<`; the comparison is done `byte` by `byte`, so the result is the *natural lexicographic ordering*.
* String values are immutable: the byte sequence contained in a string value can never be changed. Thereby constructions that try to modify a string’s data in place are not allowed: `s[0] = 'L' // compile error: cannot assign to s[0]`
* Immutability means that it is safe for two copies of a string to share the same underlying memory, making it cheap to copy strings of any length. Similarly, a string `s` and a substring like `s[7:]` may safely share the same data, so the substring operation is also cheap. No new memory is allocated in either case.

> [!subsubsection] 3.5.1 String Literals

* Within a double-quoted string literal, escape sequences that begin with a backslash `\` can be used to insert arbitrary byte values into the string:
	* `\a` "alert" or bell
	* `\b` backspace
	* `\f` form feed
	* `\n` newline
	* `\r` carriage return
	* `\t` tab
	* `\v` vertical tab
	* `\'` single quote (only in the rune literal `'\''`)
	* `\"` double quote (only within `"..."` literals)
	* `\\` backslash
* A raw string literal is written \`...\`, using backquotes instead of double quotes. Within a raw string literal, no escape sequences are processed; the contents are taken literally, including backslashes and newlines, so a raw string literal may spread over several lines in the program source. The only processing is that carriage returns are deleted so that the value of the string is the same on all platforms, including those that conventionally put carriage returns in text files.
* Raw string literals are a convenient way to write regular expressions, which tend to have lots of backslashes. They are also useful for `HTML` templates, `JSON` literals, command usage messages, and the like, which often extend over multiple lines.
```go
const GoUsage = `Go is a tool for managing Go source code.
Usage:
	go command [arguments]
...`
```

> [!subsubsection] 3.5.3 UTF-8

* Go source files are always encoded in `UTF-8`, and `UTF-8` is the preferred encoding for text strings manipulated by Go programs.
* The `unicode` package provides functions for working with individual runes (such as distinguishing letters from numbers, or converting an upper-case letter to a lower-case one), and the `unicode/utf8` package provides functions for encoding and decoding `runes` as `bytes` using `UTF-8`.
* Unicode escapes in Go string literals allow us to specify them by their numeric code point value. There are two forms, `\uhhhh` for a `16`-bit value and `\Uhhhhhhhh` for a `32`-bit value, where each `h` is a hexadecimal digit. Each denotes the `UTF-8` encoding of the specified code point.
* If we really care about the individual Unicode characters, we have to use other mechanisms. Consider the string from our very first example, which includes two East Asian characters. 
	```go
	import "unicode/utf8"
	s := "Hello, BF"
	fmt.Println(len(s))                    // "13"
	fmt.Println(utf8.RuneCountInString(s)) // "9"
	```
* To process those characters, we need a `UTF-8` decoder. The `unicode/utf8` package provides one that we can use like this:
	```go
	for i := 0; i < len(s); {
		r, size := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%d\t%c\n", i, r)
		i += size
	}
	```
* Each call to `DecodeRuneInString` returns `r`, the rune itself, and size, the number of bytes occupied by the `UTF-8` encoding of `r`. The size is used to update the byte index `i` of the next rune in the string. But this is clumsy, and we need loops of this kind all the time. Fortunately, Go’s range loop, when applied to a string, performs `UTF-8` decoding implicitly. Notice how the index jumps by more than `1` for each non-`ASCII` rune.
	```go
	for i, r := range "Hello, BF" {
		fmt.Printf("%d\t%q\t%d\n", i, r, r)
	}
	```
* We could use a simple range loop to count the number of runes in a string, like this, or we can just call `utf8.RuneCountInString(s)`:
	```go
	n := 0
	for range s {
		n++
	}
	```
* `UTF-8` is exceptionally convenient as an interchange format but within a program runes may be more convenient because they are of uniform size and are thus easily indexed in arrays and slices.
* A `[]rune` conversion applied to a `UTF-8`-encoded string returns the sequence of Unicode code points that the string encodes:
	```go
	// "program" in Japanese katakana
	s := ">+=@?" // this was japanese in the book :P
	fmt.Printf("% x\n", s) // "e3 83 97 e3 83 ad e3 82 b0 e3 83 a9 e3 83 a0"
	r := []rune(s)
	fmt.Printf("%x\n", r) // "[30d7 30ed 30b0 30e9 30e0]"
	```
* Converting an integer value to a string interprets the integer as a rune value, and yields the `UTF-8` representation of that rune (If the rune is invalid, the replacement character is substituted):
```go
fmt.Println(string(65))     // "A", not "65"
fmt.Println(string(0x4eac)) // "C"
fmt.Println(string(1234567)) // "?"
```

> [!subsubsection] 3.5.4 Strings and Byte Slices

* Four standard packages are particularly important for manipulating `strings`: `bytes`, `strings`, `strconv`, and `unicode`.
* The strings package provides many functions for searching, replacing, comparing, trimming, splitting, and joining strings. The strings package has functions `ToUpper` and `ToLower`, that return a new string with the specified transformation applied to each character of the original string.
* The `bytes` package has similar functions for manipulating slices of bytes, of type `[]byte`, which share some properties with `strings`. Because strings are immutable, building up strings incrementally can involve a lot of allocation and copying. In such cases, it’s more efficient to use the `bytes.Buffer` type.
* The `strconv` package provides functions for converting `boolean`, `integer`, and `floating-point` values to and from their `string` representations, and functions for quoting and unquoting strings.
* The `unicode` package provides functions like `IsDigit`, `IsLetter`, `IsUpper`, and `IsLower` for classifying runes. Each function takes a single rune argument and returns a boolean. Conversion functions like `ToUpper` and `ToLower` convert a rune into the given case if it is a letter. All these functions use the Unicode standard categories for letters, digits, and so on.
* The `path` and `path/filepath` packages provide a more general set of functions for manipulating hierarchical names. The `path` package works with slash-delimited paths on any platform. It shouldn’t be used for file names, but it is appropriate for other domains, like the path component of a `URL`. By contrast, `path/filepath` manipulates file names using the rules for the host platform.
* A string contains an array of bytes that, once created, is immutable. By contrast, the elements of a byte slice can be freely modified.
* Strings can be converted to byte slices and back again:
	```go
	s := "abc"
	b := []byte(s)
	s2 := string(b)
	```
* Conceptually, the `[]byte(s)` conversion allocates a new byte array holding a copy of the bytes of `s`, and yields a slice that references the entirety of that array. An optimizing compiler may be able to avoid the allocation and copying in some cases, but in general copying is required to ensure that the bytes of `s` remain unchanged even if those of `b` are subsequently modified. The conversion from byte slice back to string with `string(b)` also makes a copy, to ensure immutability of the resulting string `s2`.
* To avoid conversions and unnecessary memory allocation, many of the utility functions in the bytes package directly parallel their counterparts in the strings package:
	* `func Contains(s, substr string) bool`
	* `func Contains(b, subslice []byte) bool`
	* `func Count(s, sep string) int`
	* `func Count(s, sep []byte) int`
	* `func Fields(s string) []string`
	* `func Fields(s []byte) [][]byte`
	* `func HasPrefix(s, prefix string) bool`
	* `func HasPrefix(s, prefix []byte) bool`
	* `func Index(s, sep string) int`
	* `func Index(s, sep []byte) int`
	* `func Join(a []string, sep string) string`
	* `func Join(s [][]byte, sep []byte) []byte`

> [!subsubsection] 3.5.5 Conversions between Strings and Numbers

* To convert an integer to a string, one option is to use `fmt.Sprintf`; another is to use the function `strconv.Itoa` (‘‘integer to ASCII’’):
	```go
	x := 123
	y := fmt.Sprintf("%d", x)
	fmt.Println(y, strconv.Itoa(x)) // "123 123"
	```
* `FormatInt` and `FormatUint` can be used to format numbers in a different base:
	```go
	fmt.Println(strconv.FormatInt(int64(x), 2)) // "1111011"
	```
* The `fmt.Printf` verbs `%b`, `%d`, `%u`, and `%x` are often more convenient than Format functions, especially if we want to include additional information besides the number:
	```go
	s := fmt.Sprintf("x=%b", x) // "x=1111011"
	```
* To parse a string representing an integer, use the `strconv` functions `Atoi` or `ParseInt`, or `ParseUint` for unsigned integers:
	```go
	x, err := strconv.Atoi("123")             // x is an int
	y, err := strconv.ParseInt("123", 10, 64) // base 10, up to 64 bits
	```
* The third argument of `ParseInt` gives the size of the integer type that the result must fit into; for example, 16 implies `int16`, and the special value of 0 implies `int`. In any case, the type of the result `y` is always `int64`, which you can then convert to a smaller type.
* Sometimes `fmt.Scanf` is useful for parsing input that consists of orderly mixtures of strings and numbers all on a single line, but it can be inflexible, especially when handling incomplete or irregular input.

> [!Error] 3.6 Constants

* Constants are expressions whose value is known to the compiler and whose evaluation is guaranteed to occur at compile time, not at run time. The underlying type of every constant is a basic type: boolean, string, or number.
* As with variables, a sequence of constants can appear in one declaration; this would be appropriate for a group of related values:
	```go
	const (
		e = 2.7182818284590452353602874713526624977572470936999595749
		pi = 3.141592653589793238462643383279502884197169399375105820
	)
	```
* Many computations on constants can be completely evaluated at compile time, reducing the work necessary at run time and enabling other compiler optimizations. Errors ordinarily detected at run time can be reported at compile time when their operands are constants, such as integer division by zero, string indexing out of bounds, and any floating-point operation that would result in a non-finite value.
* The results of all arithmetic, logical, and comparison operations applied to constant operands are themselves constants, as are the results of conversions and calls to certain built-in functions such as `len`, `cap`, `real`, `imag`, `complex`, and `unsafe.Sizeof`.

> [!subsubsection] 3.6.1 The Constant Generator iota

* A const declaration may use the *constant generator* `iota`, which is used to create a sequence of related values without spelling out each one explicitly. In a const declaration, the value of `iota` begins at *zero* and increments by one for each item in the sequence.
* Here’s an example from the `time` package, which defines named constants of type Weekday for the days of the week, starting with zero for Sunday. Types of this kind are often called *enumerations*, or *enums* for short.
	```go
	type Weekday int
	const (
		Sunday Weekday = iota
		Monday
		Tuesday
		Wednesday
		Thursday
		Friday
		Saturday
	)
	```
	```go
	type Flags uint
	const (
		FlagUp Flags = 1 << iota // is up
		FlagBroadcast    // supports broadcast access capability
		FlagLoopback     // is a loopback interface
		FlagPointToPoint // belongs to a point-to-point link
		FlagMulticast    // supports multicast access capability
	)
	```
	```go
	const (
		_ = 1 << (10 * iota)
		KiB // 1024
		MiB // 1048576
		GiB // 1073741824
		TiB // 1099511627776                (exceeds 1 << 32)
		PiB // 1125899906842624
		EiB // 1152921504606846976
		ZiB // 1180591620717411303424       (exceeds 1 << 64)
		YiB // 1208925819614629174706176
	)
	```
* The `iota` mechanism has its limits. For example, it’s not possible to generate the more familiar powers of `1000` (KB, MB, and so on) because there is no exponentiation operator.

> [!subsubsection] 3.6.2 Untyped Constants

* Constants in Go are a bit unusual. Although a constant can have any of the basic data types like `int` or `float64`, including named basic types like `time.Duration`, many constants are not committed to a particular type. The compiler represents these uncommitted constants with much greater numeric precision than values of basic types, and arithmetic on them is more precise than machine arithmetic; you may assume at least `256` bits of precision. There are six flavors of these uncommitted constants, called `untyped boolean`, `untyped integer`, `untyped rune`, `untyped floating-point`, `untyped complex`, and `untyped string`.
* By deferring this commitment, untyped constants not only retain their higher precision until later, but they can participate in many more expressions than committed constants without requiring conversions. For example, the values `ZiB` and `YiB` in the example above are too big to store in any integer variable, but they are legitimate constants.
* For literals, syntax determines flavor. The literals `0`, `0.0`, `0i`, and `'\u0000'` all denote constants of the same value but different flavors: `untyped integer`, `untyped floating-point`, `untyped complex`, and `untyped rune`, respectively. Similarly, `true` and `false` are untyped `booleans` and `string` literals are untyped strings.
* Recall that `/` may represent integer or floating-point division depending on its operands. Consequently, the choice of literal may affect the result of a constant division expression:
	```go
	var f float64 = 212
	fmt.Println((f - 32) * 5 / 9)     // "100"; (f - 32) * 5 is a float64
	fmt.Println(5 / 9 * (f - 32))     // "0"; 5/9 is an untyped integer, 0
	fmt.Println(5.0 / 9.0 * (f - 32)) // "100"; 5.0/9.0 is an untyped float
	```
* Only constants can be untyped. When an untyped constant is assigned to a variable, or appears on the right-hand side of a variable declaration with an explicit type, the constant is implicitly converted to the type of that variable if possible.
```go
var f float64 = 3 + 0i // untyped complex -> float64
// var f float64 = float64(3 + 0i)
f = 2      // untyped integer -> float64
// f = float64(2)
f = 1e123  // untyped floating-point -> float64
// f = float64(1e123)
f = 'a'    // untyped rune -> float64
// f = float64('a')
```
* Whether implicit or explicit, converting a constant from one type to another requires that the target type can represent the original value. Rounding is allowed for real and complex floating-point numbers:
	```go
	const (
		deadbeef = 0xdeadbeef // untyped int with value 3735928559
		a = uint32(deadbeef)  // uint32 with value 3735928559
		b = float32(deadbeef) // float32 with value 3735928576 (rounded up)
		c = float64(deadbeef) // float64 with value 3735928559 (exact)
		d = int32(deadbeef)   // compile error: constant overflows int32
		e = float64(1e309)    // compile error: constant overflows float64
		f = uint(-1)          // compile error: constant underflows uint
	)
	```
* In a variable declaration without an explicit type (including short variable declarations), the flavor of the untyped constant implicitly determines the default type of the variable, as in these examples:
	```go
	i := 0      // untyped integer;        implicit int(0)
	r := '\000' // untyped rune;           implicit rune('\000')
	f := 0.0    // untyped floating-point; implicit float64(0.0)
	c := 0i     // untyped complex;        implicit complex128(0i)
	```
* These defaults are particularly important when converting an untyped constant to an interface value since they determine its dynamic type.
	```go
	fmt.Printf("%T\n", 0)      // "int"
	fmt.Printf("%T\n", 0.0)    // "float64"
	fmt.Printf("%T\n", 0i)     // "complex128"
	fmt.Printf("%T\n", '\000') // "int32" (rune)
	```

### 4. Composite Types
> `pg: 38`
> `time req: 2' 7"`

* Arrays and structs are aggregate types; their values are concatenations of other values in memory. Arrays are homogeneous—their elements all have the same type—whereas structs are heterogeneous. Both arrays and structs are fixed size. In contrast, slices and maps are dynamic data structures that grow as values are added.

> [!Error] 4.1 Arrays

* An array is a fixed-length sequence of zero or more elements of a particular type. Because of their fixed length, arrays are rarely used directly in Go. Slices, which can grow and shrink, are much more versatile.
* The built-in function `len` returns the number of elements in the array.
* By default, the elements of a new array variable are initially set to the zero value for the element type. We can use an array literal to initialize an array with a list of values:
	```go
	var q [3]int = [3]int{1, 2, 3}
	var r [3]int = [3]int{1, 2}
	fmt.Println(r[2]) // "0"
	```
* In an array literal, if an ellipsis ‘‘`...`’’ appears in place of the length, the array length is determined by the number of initializers.
	```go
	q := [...]int{1, 2, 3}
	fmt.Printf("%T\n", q) // "[3]int"
	```
* The size of an array is part of its type, so `[3]int` and `[4]int` are different types. The size must be a constant expression, that is, an expression whose value can be computed as the program is being compiled.
* It is also possible to specify a list of index and value pairs, like this:
	```go
	type Currency int
	const (
		USD Currency = iota
		EUR
		GBP
		RMB
	)
	symbol := [...]string{USD: "$", EUR: "9", GBP: "!", RMB: """}
	fmt.Println(RMB, symbol[RMB]) // "3 ""
	```
* In this form, indices can appear in any order and some may be omitted.
	```go
	r := [...]int{99: -1}
	```
	* defines an array r with 100 elements, all zero except for the last, which has value −1.
* If an array’s element type is comparable then the array type is comparable too, so we may directly compare two arrays of that type using the `==` operator, which reports whether all corresponding elements are equal.
	```go
	a := [2]int{1, 2}
	b := [...]int{1, 2}
	c := [2]int{1, 3}
	fmt.Println(a == b, a == c, b == c) // "true false false"
	d := [3]int{1, 2}
	fmt.Println(a == d) // compile error: cannot compare [2]int == [3]int
	```
* When a function is called, a copy of each argument value is assigned to the corresponding parameter variable, so the function receives a copy, not the original. Passing large arrays in this way can be inefficient, and any changes that the function makes to array elements affect only the copy, not the original. In this regard, Go treats arrays like any other type, but this behavior is different from languages that implicitly pass arrays by reference.
* Of course, we can explicitly pass a pointer to an array so that any modifications the function makes to array elements will be visible to the caller. The array literal `[32]byte{}` yields an array of 32 bytes. Each element of the array has the zero value for byte, which is zero.
* Using a pointer to an array is efficient and allows the called function to mutate the caller’s variable, but arrays are still inherently inflexible because of their fixed size. The zero function will not accept a pointer to a `[16]byte` variable, for example, nor is there any way to add or remove array elements. For these reasons, arrays are seldom used as function parameters; instead, we use slices.

> [!Error] 4.2 Slices

* Slices represent variable-length sequences whose elements all have the same type. A slice type is written `[]T`, where the elements have type `T`; it looks like an array type without a size.
* Arrays and slices are intimately connected. A slice is a lightweight data structure that gives access to a subsequence (or perhaps all) of the elements of an array, which is known as the slice’s *underlying array*.
* A slice has three components: a pointer, a length, and a capacity.
	* The pointer points to the first element of the array that is reachable through the slice, which is not necessarily the array’s first element.
	* The length is the number of slice elements; it can’t exceed the capacity.
	* The capacity is usually the number of elements between the start of the slice and the end of the underlying array.
	* The built-in functions `len` and `cap` return those values.
* The slice operator `s[i:j]`, where `0 ≤ i ≤ j ≤ cap(s)`, creates a new slice that refers to elements `i` through `j-1` of the sequence `s`, which may be an array variable, a pointer to an array, or another slice. The resulting slice has `j-i` elements. If `i` is omitted, it’s `0`, and if `j` is omitted, it’s `len(s)`.
* Slicing beyond `cap(s)` causes a panic, but slicing beyond `len(s)` extends the slice, so the result may be longer than the original.
* As an aside, note the similarity of the substring operation on strings to the slice operator on `[]byte` slices. Both are written `x[m:n]`, and both return a subsequence of the original bytes, sharing the underlying representation so that both operations take constant time. The expression `x[m:n]` yields a string if `x` is a string, or a `[]byte` if `x` is a `[]byte`.
* Since a slice contains a pointer to an element of an array, passing a slice to a function permits the function to modify the underlying array elements. In other words, copying a slice creates an alias for the underlying array.
* Unlike arrays, slices are not comparable, so we cannot use `==` to test whether two slices contain the same elements. The standard library provides the highly optimized `bytes.Equal` function for comparing two slices of bytes (`[]byte`), but for other types of slice, we must do the comparison ourselves:
	```go
	func equal(x, y []string) bool {
		if len(x) != len(y) {
			return false
		}
		for i := range x {
			if x[i] != y[i] {
				return false
			}
		}
		return true
	}
	```
	* Given how natural this ‘‘deep’’ equality test is, and that it is no more costly at run time than the `==` operator for arrays of strings, it may be puzzling that slice comparisons do not also work this way. There are two reasons why deep equivalence is problematic.
	* First, unlike array elements, the elements of a slice are indirect, making it possible for a slice to contain itself. Although there are ways to deal with such cases, none is simple, efficient, and most importantly, obvious. **This is probably related to interfaces and can only be understood later.**
	* Second, because slice elements are indirect, a fixed slice value may contain different elements at different times as the contents of the underlying array are modified. Because a hash table such as Go’s map type makes only shallow copies of its keys, it requires that equality for each key remain the same throughout the lifetime of the hash table. Deep equivalence would thus make slices unsuitable for use as map keys. For reference types like pointers and channels, the `==` operator tests reference identity, that is, whether the two entities refer to the same thing. An analogous ‘‘shallow’’ equality test for slices could be useful, and it would solve the problem with maps, but the inconsistent treatment of slices and arrays by the `==` operator would be confusing. The safest choice is to disallow slice comparisons altogether.
* The only legal slice comparison is against `nil`, as in `if summer == nil { /* ... */ }`.
* The zero value of a slice type is `nil`. A `nil` slice has no underlying array. The `nil` slice has length and capacity zero, but there are also non-`nil` slices of length and capacity zero, such as `[]int{}` or `make([]int, 3)[3:]`. As with any type that can have `nil` values, the `nil` value of a particular slice type can be written using a conversion expression such as `[]int(nil)`.
	```go
	var s []int    // len(s) == 0, s == nil
	s = nil        // len(s) == 0, s == nil
	s = []int(nil) // len(s) == 0, s == nil
	s = []int{}    // len(s) == 0, s != nil
	```
	* So, if you need to test whether a slice is empty, use `len(s) == 0`, not `s == nil`. Other than comparing equal to `nil`, a `nil` slice behaves like any other zero-length slice. Unless clearly documented to the contrary, Go functions should treat all zero-length slices the same way, whether `nil` or `non-nil`.
* The built-in function make creates a slice of a specified element type, length, and capacity. The capacity argument may be omitted, in which case the capacity equals the length.
	```go
		make([]T, len)
		make([]T, len, cap) // same as make([]T, cap)[:len]
	```
	* Under the hood, `make` creates an unnamed array variable and returns a slice of it; the array is accessible only through the returned slice. In the first form, the slice is a view of the entire array. In the second, the slice is a view of only the array’s first `len` elements, but its capacity includes the entire array. The additional elements are set aside for future growth.

> [!subsubsection] 4.2.1 The append Function

* The built-in append function appends items to slices.
* The append function is crucial to understanding how slices work, so let’s take a look at what is going on. Here’s a version called `appendInt` that is specialized for `[]int` slices.
```go
func appendInt(x []int, y int) []int {
	var z []int
	zlen := len(x) + 1
	if zlen <= cap(x) {
		// There is room to grow. Extend the slice.
		z = x[:zlen]
	} else {
		// There is insufficient space. Allocate a new array.
		// Grow by doubling, for amortized linear complexity.
		zcap := zlen
		if zcap < 2*len(x) {
			zcap = 2 * len(x)
		}
		z = make([]int, zlen, zcap)
		copy(z, x) // a built-in function; see text
	}
	z[len(x)] = y
	return z
}
```
* If the the slice `x` has sufficient capacity to hold the new value, the resulting `z` slice will have the same underlying array as `x`. But if `x` does not posses sufficient capacity, the resulting `z` slice will not share the same underlying array as `x` as it did before.
* The built-in function `copy`, which copies elements from one slice to another of the same type. Its first argument is the destination and its second is the source, resembling the order of operands in an assignment like `dst = src`. The slices may refer to the same underlying array; they may even overlap. `copy` returns the number of elements actually copied, which is the smaller of the two slice lengths, so there is no danger of running off the end or overwriting something out of range.
* The built-in `append` function may use a more sophisticated growth strategy. Usually we don’t know whether a given call to append will cause a reallocation, so we can’t assume that the original slice refers to the same array as the resulting slice, nor that it refers to a different one. Similarly, we must not assume that operations on elements of the old slice will (or will not) be reflected in the new slice. As a result, it’s usual to assign the result of a call to append to the same slice variable whose value we passed to `append`: `runes = append(runes, r)`
* Updating the slice variable is required not just when calling `append`, but for any function that may change the length or capacity of a slice or make it refer to a different underlying array. To use slices correctly, it’s important to bear in mind that although the elements of the underlying array are indirect, the slice’s pointer, length, and capacity are not. To update them requires an assignment like the one above. In this respect, slices are not ‘‘pure’’ reference types but resemble an aggregate type such as this struct:
	```go
	type IntSlice struct {
		ptr *int
		len, cap int
	}
	```

> [!Error] 4.3 Maps

* In Go, a map is a reference to a hash table, and a map type is written `map[K]V`, where `K` and `V` are the types of its keys and values. All of the keys in a given map are of the same type, and all of the values are of the same type, but the keys need not be of the same type as the values. The key type `K` must be comparable using `==`, so that the map can test whether a given key is equal to one already within it. Though floating-point numbers are comparable, it’s a bad idea to compare floats for equality and especially bad if `NaN` is a possible value. There are no restrictions on the value type `V`.
* The built-in function `make` can be used to create a `map`: `ages := make(map[string]int) // mapping from strings to ints`
* We can also use a `map` literal to create a new `map` populated with some initial key/value pairs:
	```go
	ages := map[string]int{
		"alice": 31,
		"charlie": 34,
	}
	// which is equivalent to:
	ages := make(map[string]int)
	ages["alice"] = 31
	ages["charlie"] = 34
	```
* so an alternative expression for a new empty `map` is `map[string]int{}`.
* `Map` elements are accessed through the usual subscript notation.
* and removed with the built-in function `delete`: `delete(ages, "alice") // remove element ages["alice"]`
* All of these operations are safe even if the element isn’t in the `map`; a `map` lookup using a key that isn’t present returns the zero value for its type.
* But a `map` element is not a variable, and we cannot take its address.
* One reason that we can’t take the address of a `map` element is that growing a `map` might cause rehashing of existing elements into new storage locations, thus potentially invalidating the address.
* To enumerate all the key/value pairs in the `map`, we use a range-based for loop similar to those we saw for slices: `for key, val := range dict {}`
* The order of `map` iteration is unspecified, and different implementations might use a different hash function, leading to a different ordering. In practice, the order is random, varying from one execution to the next. This is intentional; making the sequence vary helps force programs to be robust across implementations. To enumerate the key/value pairs in order, we must sort the keys explicitly.
* The zero value for a `map` type is `nil`, that is, a reference to no hash table at all.
	```go
	var ages map[string]int
	fmt.Println(ages == nil)    // "true"
	fmt.Println(len(ages) == 0) // "true"
	```
* Most operations on `maps`, including lookup, `delete`, `len`, and `range` loops, are safe to perform on a `nil` `map` reference, since it behaves like an empty `map`. But storing to a `nil` `map` causes a panic.
* You must allocate the `map` before you can store into it.
* Accessing a `map` element by subscripting always yields a value. If the key is present in the `map`, you get the corresponding value; if not, you get the zero value for the element type. For many purposes that’s fine, but sometimes you need to know whether the element was really there or not. For example, if the element type is numeric, you might have to distinguish between a nonexistent element and an element that happens to have the value zero, using a test like this:
	```go
	age, ok := ages["bob"]
	if !ok { /* "bob" is not a key in this map; age == 0. */ }
	```
* You’ll often see these two statements combined, like this:
	```go
	if age, ok := ages["bob"]; !ok { /* ... */ }
	```
* As with slices, `maps` cannot be compared to each other; the only legal comparison is with `nil`. To test whether two `maps` contain the same keys and the same associated values, we must write a loop:
	```go
	func equal(x, y map[string]int) bool {
		if len(x) != len(y) {
			return false
		}
		for k, xv := range x {
			if yv, ok := y[k]; !ok || yv != xv {
				return false
			}
		}
		return true
	}
	```
* Go does not provide a `set` type, but since the keys of a `map` are distinct, a `map` can serve this purpose.

> [!Error] 4.4 Structs

* A `struct` is an aggregate data type that groups together zero or more named values of arbitrary types as a single entity. Each value is called a *field*. All of these fields are collected into a single entity that can be copied as a unit, passed to functions and returned by them, stored in arrays, and so on.
* The dot notation also works with a pointer to a `struct`.
* Fields are usually written one per line, with the field’s name preceding its type, but consecutive fields of the same type may be combined.
* Field order is significant to type identity. Had we also combined the declaration of the Position field (also a string), or interchanged Name and Address, we would be defining a different `struct` type. Typically we only combine the declarations of related fields.
* The name of a `struct` field is exported if it begins with a capital letter; this is Go’s main access control mechanism. A `struct` type may contain a mixture of exported and unexported fields.
* A named `struct` type S can’t declare a field of the same type S: an aggregate value cannot contain itself. (An analogous restriction applies to arrays.) But S may declare a field of the pointer type \*S, which lets us create recursive data structures like linked lists and trees.
* The zero value for a `struct` is composed of the zero values of each of its fields. It is usually desirable that the zero value be a natural or sensible default. For example, in `bytes.Buffer`, the initial value of the `struct` is a ready-to-use empty buffer, and the zero value of `sync.Mutex` is a ready-to-use unlocked mutex. Sometimes this sensible initial behavior happens for free, but sometimes the type designer has to work at it.
* The `struct` type with no fields is called the empty `struct`, written `struct{}`. It has size zero and carries no information but may be useful nonetheless. Some Go programmers use it instead of bool as the value type of a map that represents a set, to emphasize that only the keys are significant, but the space saving is marginal and the syntax more cumbersome, so we generally avoid it.

> [!subsubsection] 4.4.1 Struct Literals

* A value of a `struct` type can be written using a *struct literal* that specifies values for its fields.
* There are two forms of `struct` literal.
	* The first form requires that a value be specified for every field, in the right order. It burdens the writer (and reader) with remembering exactly what the fields are, and it makes the code fragile should the set of fields later grow or be reordered. Accordingly, this form tends to be used only within the package that defines the `struct` type, or with smaller `struct` types for which there is an obvious field ordering convention, like `image.Point{x, y}` or `color.RGBA{red, green, blue, alpha}`.
	* More often, the second form is used, in which a struct value is initialized by listing some or all of the field names and their corresponding values. If a field is omitted in this kind of literal, it is set to the zero value for its type. Because names are provided, the order of fields doesn’t matter.
* The two forms cannot be mixed in the same literal. Nor can you use the (order-based) first form of literal to sneak around the rule that unexported identifiers may not be referred to from another package.

> [!subsubsection] 4.4.2 Comparing Structs

* If all the fields of a `struct` are comparable, the `struct` itself is comparable, so two expressions of that type may be compared using `==` or `!=`. The `==` operation compares the corresponding fields of the two structs in order.
* Comparable `struct` types, like other comparable types, may be used as the key type of a map.

> [!subsubsection] 4.4.3 Struct Embedding and Anonymous Fields

* Go lets us declare a field with a type but no name; such fields are called ***anonymous fields***. The type of the field must be a named type or a pointer to a named type.
* Below, Circle and Wheel have one anonymous field each. We say that a Point is embedded within Circle, and a Circle is embedded within Wheel.
	```go
	type Point struct {
		X, Y int
	}
	type Circle struct {
		Point
		Radius int
	}
	type Wheel struct {
		Circle
		Spokes int
	}
	```
* Thanks to embedding, we can refer to the names at the leaves of the implicit tree without giving the intervening names:
```go
var w Wheel
w.X = 8        // equivalent to w.Circle.Point.X = 8
w.Y = 8        // equivalent to w.Circle.Point.Y = 8
w.Radius = 5   // equivalent to w.Circle.Radius = 5
w.Spokes = 20
```
* The explicit forms shown in the comments above are still valid, however, showing that ‘‘anonymous field’’ is something of a misnomer. The fields Circle and Point do have names—that of the named type—but those names are optional in dot expressions. We may omit any or all of the anonymous fields when selecting their subfields.
* Unfortunately, there’s no corresponding shorthand for the `struct` literal syntax, so neither of these will compile:
	```go
	w = Wheel{8, 8, 5, 20}
	// compile error: unknown fields
	w = Wheel{X: 8, Y: 8, Radius: 5, Spokes: 20}
	// compile error: unknown fields
	```
* The `struct` literal must follow the shape of the type declaration, so we must use one of the two forms below, which are equivalent to each other:
	```go
	w = Wheel{Circle{Point{8, 8}, 5}, 20}
	w = Wheel{
		Circle: Circle{
			Point: Point{X: 8, Y: 8},
			Radius: 5,
		},
		Spokes: 20, // NOTE: trailing comma necessary here (and at Radius)
	}
	fmt.Printf("%#v\n", w)
	// Output:
	// Wheel{Circle:Circle{Point:Point{X:8, Y:8}, Radius:5}, Spokes:20}
	w.X = 42
	fmt.Printf("%#v\n", w)
	// Output:
	// Wheel{Circle:Circle{Point:Point{X:42, Y:8}, Radius:5}, Spokes:20}
	```
* Because ‘‘anonymous’’ fields do have implicit names, you can’t have two anonymous fields of the same type since their names would conflict. And because the name of the field is implicitly determined by its type, so too is the visibility of the field. In the examples above, the Point and Circle anonymous fields are exported. Had they been unexported (point and circle), we could still use the shorthand form `w.X = 8 // equivalent to w.circle.point.X = 8` but the explicit long form shown in the comment would be forbidden outside the declaring package because circle and point would be inaccessible.

> [!Error] 4.5 JSON

* JavaScript Object Notation (JSON) is a standard notation for sending and receiving structured information. JSON is not the only such notation. XML, ASN.1, and Google’s Protocol Buffers serve similar purposes and each has its niche, but because of its simplicity, readability, and universal support, JSON is the most widely used.
* Go has excellent support for encoding and decoding these formats, provided by the standard library packages `encoding/json`, `encoding/gob`, `encoding/xml`, `encoding/asn1`, and so on, and these packages all have similar APIs. This section gives a brief overview of the most important parts of the `encoding/json` package.
* Converting a Go data structure to JSON is called marshaling. Marshaling is done by `json.Marshal`. Marshal produces a byte slice containing a very long string with no extraneous white space. This will contain all the information but it’s hard to read; For human consumption, a variant called `json.MarshalIndent` produces neatly indented output. Two additional arguments define a prefix for each line of output and a string for each level of indentation.
* Marshaling uses the Go struct field names as the field names for the JSON objects (through reflection). Only exported fields are marshaled.
* A *field tag* is a string of metadata associated at compile time with the field of a struct. A field tag may be any literal string, but it is conventionally interpreted as a space-separated list of `key:"value"` pairs; since they contain double quotation marks, field tags are usually written with raw string literals. The json key controls the behavior of the `encoding/json` package, and other `encoding/...` packages follow this convention. The first part of the json field tag specifies an alternative JSON name for the Go field. Field tags are often used to specify an idiomatic JSON name like `total_count` for a Go field named `TotalCount`. The tag in the example has an additional option, `omitempty`, which indicates that no JSON output should be produced if the field has the zero value for its type or is otherwise empty.
* The inverse operation to marshaling, decoding JSON and populating a Go data structure, is called unmarshaling, and it is done by `json.Unmarshal`. By defining suitable Go data structures in this way, we can select which parts of the JSON input to decode and which to discard. When `Unmarshal` returns, it has filled in the slice with the defined information; other names in the JSON are ignored.

### 5. Functions
> `pg: 36`
> `time req: 2'`

> [!Error] 5.1 Function Declarations

* A function declaration has a name, a list of parameters, an optional list of results, and a body:
	```go
	func name(parameter-list) (result-list) {
		body
	}
	```
* The parameter list specifies the names and types of the function’s parameters, which are the local variables whose values or arguments are supplied by the caller.
* The result list specifies the types of the values that the function returns. If the function returns one unnamed result or no results at all, parentheses are optional and usually omitted. Leaving off the result list entirely declares a function that does not return any value and is called only for its effects.
* Like parameters, results may be named. In that case, each name declares a local variable initialized to the zero value for its type.
* A function that has a result list must end with a return statement unless execution clearly cannot reach the end of the function, perhaps because the function ends with a call to panic or an infinite for loop with no break.
* The type of a function is sometimes called its signature. Two functions have the same type or signature if they have the same sequence of parameter types and the same sequence of result types. The names of parameters and results don’t affect the type, nor does whether or not they were declared using the factored form.
* The type of a function is sometimes called its signature. Two functions have the same type or signature if they have the same sequence of parameter types and the same sequence of result types. The names of parameters and results don’t affect the type, nor does whether or not they were declared using the factored form.
* Every function call must provide an argument for each parameter, in the order in which the parameters were declared. Go has no concept of default parameter values, nor any way to specify arguments by name, so the names of parameters and results don’t matter to the caller except as documentation.
* Parameters are local variables within the body of the function, with their initial values set to the arguments supplied by the caller. Function parameters and named results are variables in the same lexical block as the function’s outermost local variables.
* Arguments are passed by value, so the function receives a copy of each argument.
* You may occasionally encounter a function declaration without a body, indicating that the function is implemented in a language other than Go. Such a declaration defines the function signature.
	```go
	package math
	func Sin(x float64) float64 // implemented in assembly language
	```

> [!Error] 5.2 Recursion

* Many programming language implementations use a fixed-size function call stack; sizes from 64KB to 2MB are typical. Fixed-size stacks impose a limit on the depth of recursion, so one must be careful to avoid a stack overflow when traversing large data structures recursively; fixed-size stacks may even pose a security risk. In contrast, typical Go implementations use variable-size stacks that start small and grow as needed up to a limit on the order of a gigabyte. This lets us use recursion safely and without worrying about overflow.

> [!Error] 5.3 Multiple Return values

* Go’s garbage collector recycles unused memory, but do not assume it will release unused operating system resources like open files and network connections. They should be closed explicitly.
* A multi-valued call may appear as the sole argument when calling a function of multiple parameters. Although rarely used in production code, this feature is sometimes convenient during debugging since it lets us print all the results of a call using a single statement. The two print statements below have the same effect.
	```go
	log.Println(findLinks(url))
	links, err := findLinks(url)
	log.Println(links, err)
	```
* A bare return is a shorthand way to return each of the named result variables in order.

> [!Error] 5.4 Errors

* A function for which failure is an expected behavior returns an additional result, conventionally the last one. If the failure has only one possible cause, the result is a boolean, usually called ok.
* More often, and especially for I/O, the failure may have a variety of causes for which the caller will need an explanation. In such cases, the type of the additional result is error.
* The built-in type error is an interface type. An error may be nil or non-nil, that nil implies success and non-nil implies failure, and that a non-nil error has an error message string which we can obtain by calling its Error method or print it.
* Usually when a function returns a non-nil error, its other results are undefined and should be ignored. However, a few functions may return partial results in error cases. For example, if an error occurs while reading from a file, a call to Read returns the number of bytes it was able to read and an error value describing the problem. For correct behavior, some callers may need to process the incomplete data before handling the error, so it is important that such functions clearly document their results.
* Go’s approach sets it apart from many other languages in which failures are reported using exceptions, not ordinary values. Although Go does have an exception mechanism of sorts, it is used only for reporting truly unexpected errors that indicate a bug, not the routine errors that a robust program should be built to expect.
* The reason for this design is that exceptions tend to entangle the description of an error with the control flow required to handle it, often leading to an undesirable outcome: routine errors are reported to the end user in the form of an incomprehensible stack trace, full of information about the structure of the program but lacking intelligible context about what went wrong.
* By contrast, Go programs use ordinary control-flow mechanisms like if and return to respond to errors. This style undeniably demands that more attention be paid to error-handling logic, but that is precisely the point.

> [!subsubsection] 5.4.1 Error-Handling Strategies

* **First**, and most common, is to propagate the error, so that a failure in a subroutine becomes a failure of the calling routine.
* The `fmt.Errorf` function formats an error message using `fmt.Sprintf` and returns a new error value. We use it to build descriptive errors by successively prefixing additional context information to the original error message. When the error is ultimately handled by the program’s main function, it should provide a clear causal chain from the root problem to the overall failure, reminiscent of a NASA accident investigation:
	* `genesis: crashed: no parachute: G-switch failed: bad relay orientation`
* Because error messages are frequently chained together, message strings should not be capitalized and newlines should be avoided. The resulting errors may be long, but they will be self-contained when found by tools like `grep`.
* When designing error messages, be deliberate, so that each one is a meaningful description of the problem with sufficient and relevant detail, and be consistent, so that errors returned by the same function or by a group of functions in the same package are similar in form and can be dealt with in the same way.
* For example, the `os` package guarantees that every error returned by a file operation, such as `os.Open` or the `Read`, `Write`, or Close methods of an open file, describes not just the nature of the failure (permission denied, no such directory, and so on) but also the name of the file, so the caller needn’t include this information in the error message it constructs.
* In general, the call `f(x)` is responsible for reporting the attempted operation `f` and the argument value `x` as they relate to the context of the error. The caller is responsible for adding further information that it has but the call `f(x)` does not.
* The **second** strategy for handling errors. For errors that represent transient or unpredictable problems, it may make sense to retry the failed operation, possibly with a delay between tries, and perhaps with a limit on the number of attempts or the time spent trying before giving up entirely.
* **Third**, if progress is impossible, the caller can print the error and stop the program gracefully, but this course of action should generally be reserved for the main package of a program. Library functions should usually propagate errors to the caller, unless the error is a sign of an internal inconsistency—that is, a bug.
* **Fourth**, in some cases, it’s sufficient just to log the error and then continue, perhaps with reduced functionality.
* And **fifth** and finally, in rare cases we can safely ignore an error entirely.
* Error handling in Go has a particular rhythm. After checking an error, failure is usually dealt with before success. If failure causes the function to return, the logic for success is not indented within an else block but follows at the outer level. Functions tend to exhibit a common structure, with a series of initial checks to reject errors, followed by the substance of the function at the end, minimally indented.

> [!Error] 5.5 Function Values

* Functions are *first-class* values in Go: like other values, function values have types, and they may be assigned to variables or passed to or returned from functions. A function value may be called like any other function. For example:
	```go
	func square(n int) int { return n * n }
	func negative(n int) int { return -n }
	func product(m, n int) int { return m * n }
	f := square
	fmt.Println(f(3)) // "9"
	f = negative
	fmt.Println(f(3))
	// "-3"
	fmt.Printf("%T\n", f) // "func(int) int"
	f = product
	// compile error: can't assign f(int, int) int to f(int) int
	```
* The zero value of a function type is nil. Calling a nil function value causes a panic.
* Function values may be compared with nil:
	```go
	var f func(int) int
	if f != nil {
		f(3)
	}
	```
* but they are not comparable, so they may not be compared against each other or used as keys in a map.
* Function values let us parameterize our functions over not just data, but behavior too. The standard libraries contain many examples.

> [!Error] 5.6 Anonymous Functions

* Named functions can be declared only at the package level, but we can use a function literal to denote a function value within any expression. A function literal is written like a function declaration, but without a name following the func keyword. It is an expression, and its value is called an *anonymous function*.
* More importantly, functions defined in this way have access to the entire lexical environment, so the inner function can refer to variables from the enclosing function
* Function values are not just code but can have state.
* The anonymous inner function returned by a function can access and update the local variables of the enclosing function. These hidden variable references are why we classify functions as reference types and why function values are not comparable. Function values like these are implemented using a technique called *closures*, and Go programmers often use this term for function values.
	* The variables of the enclosing function that are used in the body of the anonymous function, will live on after the enclosing function is done running; as long as the anonymous function that was returned, lives on.

> [!subsubsection] 5.6.1 Caveat: Capturing Iteration Variables

* In this section, we’ll look at a pitfall of Go’s lexical scope rules that can cause surprising results. We urge you to understand the problem before proceeding, because the trap can ensnare even experienced programmers.
* Consider a program that must create a set of directories and later remove them. We can use a slice of function values to hold the clean-up operations. (For brevity, we have omitted all error handling in this example.)
```go
var rmdirs []func()
for _, d := range tempDirs() {
	dir := d // NOTE: necessary!
	os.MkdirAll(dir, 0755) // creates parent directories too
	rmdirs = append(rmdirs, func() {
	os.RemoveAll(dir)
	})
}
// ...do some work...
for _, rmdir := range rmdirs {
	rmdir() // clean up
}
```
* You may be wondering why we assigned the loop variable d to a new local variable dir within the loop body, instead of just naming the loop variable dir as in this subtly incorrect variant:
```go
var rmdirs []func()
for _, dir := range tempDirs() {
	os.MkdirAll(dir, 0755)
	rmdirs = append(rmdirs, func() {
		os.RemoveAll(dir) // NOTE: incorrect!
	})
}
```
* The reason is a consequence of the scope rules for loop variables. In the program immediately above, the for loop introduces a new lexical block in which the variable dir is declared. All function values created by this loop ‘‘capture’’ and share the same variable—an addressable storage location, not its value at that particular moment. The value of dir is updated in successive iterations, so by the time the cleanup functions are called, the dir variable has been updated several times by the now-completed for loop. Thus dir holds the value from the final iteration, and consequently all calls to os.RemoveAll will attempt to remove the same directory.
* Frequently, the inner variable introduced to work around this problem—dir in our example—is given the exact same name as the outer variable of which it is a copy, leading to odd-looking but crucial variable declarations like this:
```go
for _, dir := range tempDirs() {
	dir := dir // declares inner dir, initialized to outer dir
	// ...
}
```
* The risk is not unique to range-based for loops. The problem of iteration variable capture is most often encountered when using the `go` statement or with defer since both may delay the execution of a function value until after the loop has finished. But the problem is not inherent to `go` or `defer`.

> [!Error] 5.7 Variadic Functions

* A *variadic function* is one that can be called with varying numbers of arguments. The most familiar examples are `fmt.Printf` and its variants. `Printf` requires one fixed argument at the beginning, then accepts any number of subsequent arguments.
* To declare a variadic function, the type of the final parameter is preceded by an ellipsis, ‘‘`...`’’, which indicates that the function may be called with any number of arguments of this type.
* Within the body of the function, the type of the parameter will be a slice of the type specified.
* Implicitly, the caller allocates an array, copies the arguments into it, and passes a slice of the entire array to the function.
* Although the `...int` parameter behaves like a slice within the function body, the type of a variadic function is distinct from the type of a function with an ordinary slice parameter.

> [!Error] 5.8 Deferred Function Calls

* Syntactically, a defer statement is an ordinary function or method call prefixed by the keyword `defer`. The function and argument expressions are evaluated when the statement is executed, but the actual call is deferred until the function that contains the defer statement has finished, whether normally, by executing a return statement or falling off the end, or abnormally, by panicking. Any number of calls may be deferred; they are executed in the reverse of the order in which they were deferred.
* A defer statement is often used with paired operations like open and close, connect and disconnect, or lock and unlock to ensure that resources are released in all cases, no matter how complex the control flow. The right place for a defer statement that releases a resource is immediately after the resource has been successfully acquired.
* Deferred functions run *after* return statements have updated the function’s result variables. Because an anonymous function can access its enclosing function’s variables, including named results, a deferred anonymous function can observe the function’s results. This trick may be useful in functions with many return statements.

> [!Error] 5.9 Panic

* Go’s type system catches many mistakes at compile time, but others, like an out-of-bounds array access or nil pointer dereference, require checks at run time. When the Go runtime detects these mistakes, it *panics*.
* During a typical panic, normal execution stops, all deferred function calls in that goroutine are executed, and the program crashes with a log message. This log message includes the panic value, which is usually an error message of some sort, and, for each goroutine, a stack trace showing the stack of function calls that were active at the time of the panic. This log message often has enough information to diagnose the root cause of the problem without running the program again, so it should always be included in a bug report about a panicking program.
* Not all panics come from the runtime. The built-in `panic` function may be called directly ; it accepts any value as an argument. A panic is often the best thing to do when some ‘‘impossible’’ situation happens, for instance, execution reaches a case that logically can’t happen.
* Although Go’s panic mechanism resembles exceptions in other languages, the situations in which panic is used are quite different. Since a panic causes the program to crash, it is generally used for grave errors, such as a logical inconsistency in the program; diligent programmers consider any crash to be proof of a bug in their code. In a robust program, ‘‘expected’’ errors, the kind that arise from incorrect input, misconfiguration, or failing I/O, should be handled gracefully; they are best dealt with using error values.
* Consider a function that returns an error if called with parameters that cause error, but checking this error is unnecessary and burdensome if the caller knows that a particular call cannot fail. In such cases, it’s reasonable for the caller to handle an error by panicking, since it is believed to be impossible.

> [!Error] 5.10 Recover

* Giving up is usually the right response to a panic, but not always. It might be possible to recover in some way, or at least clean up the mess before quitting. For example, a web server that encounters an unexpected problem could close the connection rather than leave the client hanging, and during development, it might report the error to the client too.
* If the built-in recover function is called within a deferred function and the function containing the defer statement is panicking, recover ends the current state of panic and returns the panic value. The function that was panicking does not continue where it left off but returns normally. If recover is called at any other time, it has no effect and returns nil.
* Recovering indiscriminately from panics is a dubious practice because the state of a package’s variables after a panic is rarely well defined or documented. Perhaps a critical update to a data structure was incomplete, a file or network connection was opened but not closed, or a lock was acquired but not released. Furthermore, by replacing a crash with, say, a line in a log file, indiscriminate recovery may cause bugs to go unnoticed.
* Recovering from a panic within the same package can help simplify the handling of complex or unexpected errors, but as a general rule, you should not attempt to recover from another package’s panic. Public APIs should report failures as errors. Similarly, you should not recover from a panic that may pass through a function you do not maintain, such as a caller-provided callback, since you cannot reason about its safety.
* For all the above reasons, it’s safest to recover selectively if at all. In other words, recover only from panics that were intended to be recovered from, which should be rare. This intention can be encoded by using a distinct, unexported type for the panic value and testing whether the value returned by recover has that type. If so, we report the panic as an ordinary error; if not, we call panic with the same value to resume the state of panic.
* From some conditions there is no recovery. Running out of memory, for example, causes the Go runtime to terminate the program with a fatal error.

### 6. Methods
> `pg: 16`
> `time req: 54"`

> [!Error] 6.1 Method Declaration

* A method is declared with a variant of the ordinary function declaration in which an extra parameter appears before the function name. The parameter attaches the function to the type of that parameter.
```go
package geometry
import "math"
type Point struct{ X, Y float64 }
// traditional function
func Distance(p, q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}
// same thing, but as a method of the Point type
func (p Point) Distance(q Point) float64 {
	return math.Hypot(q.X-p.X, q.Y-p.Y)
}
```
* The extra parameter `p` is called the method’s *receiver*, a legacy from early object-oriented languages that described calling a method as ‘‘sending a message to an object.’’
* In Go, we don’t use a special name like `this` or `self` for the receiver; we choose receiver names just as we would for any other parameter. Since the receiver name will be frequently used, it’s a good idea to choose something short and to be consistent across methods. A common choice is the first letter of the type name.
* The expression `p.Distance` is called a selector, because it selects the appropriate Distance method for the receiver `p` of type Point. Selectors are also used to select fields of struct types, as in `p.X`. Since methods and fields inhabit the same name space, declaring a method X on the struct type Point would be ambiguous and the compiler will reject it.
* Since each type has its own name space for methods, we can use the name Distance for other methods so long as they belong to different types.
```go
// A Path is a journey connecting the points with straight lines.
type Path []Point
// Distance returns the distance traveled along the path.
func (path Path) Distance() float64 {
	sum := 0.0
	for i := range path {
		if i > 0 {
			sum += path[i-1].Distance(path[i])
		}
	}
	return sum
}
```
* Path is a named slice type, not a struct type like Point, yet we can still define methods for it. In allowing methods to be associated with any type, Go is unlike many other object-oriented languages. It is often convenient to define additional behaviors for simple types such as numbers, strings, slices, maps, and sometimes even functions. Methods may be declared on any named type defined in the same package, so long as its underlying type is neither a *pointer* nor an *interface*.
* Here we see the first benefit to using methods over ordinary functions: method names can be shorter. The benefit is magnified for calls originating outside the package, since they can use the shorter name and omit the package name.

> [!Error] 6.2 Methods with a Pointer Receiver

* Because calling a function makes a copy of each argument value, if a function needs to update a variable, or if an argument is so large that we wish to avoid copying it, we must pass the address of the variable using a pointer. The same goes for methods that need to update the receiver variable: we attach them to the pointer type.
```go
func (p *Point) ScaleBy(factor float64) {
	p.X *= factor
	p.Y *= factor
}
```
* In a realistic program, convention dictates that if any method of a type has a pointer receiver, then all methods of that type should have a pointer receiver, even ones that don’t strictly need it.
* The `(*Point).ScaleBy` method can be called by providing a `*Point` receiver, like this:
```go
r := &Point{1, 2}
r.ScaleBy(2)
fmt.Println(*r) // "{2, 4}"
```
* or this:
```go
p := Point{1, 2}
pptr := &p
pptr.ScaleBy(2)
fmt.Println(p) // "{2, 4}"
```
* or this:
```go
p := Point{1, 2}
(&p).ScaleBy(2)
fmt.Println(p) // "{2, 4}"
```
* But the last two cases are *ungainly*. Fortunately, the language helps us here. If the receiver `p` is a *variable* of type `Point` but the method requires a `*Point` receiver, we can use this shorthand:
```go
p.ScaleBy(2)
```
* and the compiler will perform an implicit `&p` on the variable. This works only for *variables*, including struct fields like `p.X` and array or slice elements like `perim[0]`.
* We cannot call a `*Point` method on a non-addressable Point receiver, because there’s no way to obtain the address of a temporary value.
```go
Point{1, 2}.ScaleBy(2)
// compile error: can't take address of Point literal
```
* But we can call a Point method like Point.Distance with a `*Point` receiver, because there is a way to obtain the value from the address: just load the value pointed to by the receiver. The compiler inserts an implicit `*` operation for us. These two function calls are equivalent:
```go
pptr.Distance(q)
(*pptr).Distance(q)
```
---
* In every valid method call expression, exactly one of these three statements is true.
	* Either the receiver argument has the same type as the receiver parameter, for example both have type `T` or both have type `*T`:
		```go
		Point{1, 2}.Distance(q) // Point
		pptr.ScaleBy(2)         // *Point
		```
	* Or the receiver argument is a variable of type `T` and the receiver parameter has type `*T`. The compiler implicitly takes the address of the variable:
		```go
		p.ScaleBy(2) // implicit (&p)
		```
	* Or the receiver argument has type `*T` and the receiver parameter has type `T`. The compiler implicitly dereferences the receiver, in other words, loads the value:
		```go
		pptr.Distance(q) // implicit (*pptr)
		```
---
* If all the methods of a named type `T` have a receiver type of `T` itself (not `*T`), it is safe to copy instances of that type; calling any of its methods necessarily makes a copy. For example, `time.Duration` values are liberally copied, including as arguments to functions. But if any method has a pointer receiver, you should avoid copying instances of `T` because doing so may violate internal invariants. For example, copying an instance of `bytes.Buffer` would cause the original and the copy to alias the same underlying array of bytes. Subsequent method calls would have unpredictable effects.

> [!subsubsection] 6.2.1 Nil is Valid Receiver Value

* Just as some functions allow `nil` pointers as arguments, so do some methods for their receiver, especially if nil is a meaningful zero value of the type, as with maps and slices.
```go
// An IntList is a linked list of integers.
// A nil *IntList represents the empty list.
type IntList struct {
	Value int
	Tail *IntList
}
// Sum returns the sum of the list elements.
func (list *IntList) Sum() int {
	if list == nil {
		return 0
	}
	return list.Value + list.Tail.Sum()
}
```

> [!subsubsection] 6.3 Composing Types by Struct Embedding

* A similar mechanism to embedding fields applies to the *methods* of `Point`. We can call methods of the embedded Point field using a receiver of type `ColoredPoint`, even though `ColoredPoint` has no declared methods:
	```go
	type Point struct{ X, Y float64 }
	type ColoredPoint struct {
		Point
		Color color.RGBA
	}
	var p = ColoredPoint{Point{1, 1}, red}
	var q = ColoredPoint{Point{5, 4}, blue}
	fmt.Println(p.Distance(q.Point)) // "5"
	p.ScaleBy(2)
	q.ScaleBy(2)
	fmt.Println(p.Distance(q.Point)) // "10"
	```
* The methods of `Point` have been promoted to `ColoredPoint`. In this way, embedding allows complex types with many methods to be built up by the *composition* of several fields, each providing a few methods.
---
* Readers familiar with class-based object-oriented languages may be tempted to view Point as a base class and `ColoredPoint` as a subclass or derived class, or to interpret the relationship between these types as if a `ColoredPoint` ‘‘is a’’ `Point`. But that would be a mistake. Notice the calls to `Distance` above. `Distance` has a parameter of type `Point`, and `q` is not a `Point`, so although `q` does have an embedded field of that type, we must explicitly select it. Attempting to pass `q` would be an error:
	```go
	p.Distance(q)
	// compile error: cannot use q (ColoredPoint) as Point
	```
* A `ColoredPoint` is not a `Point`, but it ‘‘has a’’ `Point`, and it has two additional methods `Distance` and `ScaleBy` promoted from `Point`.
* If you prefer to think in terms of implementation, the embedded field instructs the compiler to generate additional wrapper methods that delegate to the declared methods.
---
* The type of an *anonymous* field may be a pointer to a named type, in which case fields and methods are promoted indirectly from the pointed-to object. Adding another level of indirection lets us share common structures and vary the relationships between objects dynamically.
* A struct type may have more than one anonymous field. When the compiler resolves a selector to a method, it first looks for a directly declared method, then for methods promoted once from the type's embedded fields, then for methods promoted twice from embedded fields within the types of the embedded fields on the type, and so on. The compiler reports an error if the selector was ambiguous because two methods were promoted from the same rank.
---
* Methods can be declared only on named types and pointers to them, but thanks to embedding, it’s possible and sometimes useful for unnamed struct types to have methods too.
* Here’s a nice trick to illustrate. This example shows part of a simple cache implemented using two package-level variables, a mutex and the map that it guards:
	```go
	var (
		mu sync.Mutex // guards mapping
		mapping = make(map[string]string)
	)
	func Lookup(key string) string {
		mu.Lock()
		v := mapping[key]
		mu.Unlock()
		return v
	}
	```
* The version below is functionally equivalent but groups together the two related variables in a single package-level variable, cache:
	```go
	var cache = struct {
		sync.Mutex
		mapping map[string]string
	} {
		mapping: make(map[string]string),
	}
	func Lookup(key string) string {
		cache.Lock()
		v := cache.mapping[key]
		cache.Unlock()
		return v
	}
	```
* The new variable gives more expressive names to the variables related to the cache, and because the `sync.Mutex` field is embedded within it, its `Lock` and `Unlock` methods are promoted to the unnamed struct type, allowing us to lock the cache with a self-explanatory syntax.

> [!Error] 6.4 Method Values and Expressions

* Method Value:
	```go
	type Rocket struct { /* ... */ }
	func (r *Rocket) Launch() { /* ... */ }
	r := new(Rocket)
	time.AfterFunc(10 * time.Second, func() { r.Launch() })
	// the method value syntax is shorter:
	time.AfterFunc(10 * time.Second, r.Launch)
	```
* Method Expressions:
	```go
	p := Point{1, 2}
	q := Point{4, 6}
	distance := Point.Distance
	// method expression
	fmt.Println(distance(p, q)) // "5"
	fmt.Printf("%T\n", distance) // "func(Point, Point) float64"
	scale := (*Point).ScaleBy
	scale(&p, 2)
	fmt.Println(p)
	// "{2 4}"
	fmt.Printf("%T\n", scale) // "func(*Point, float64)"
	```

> [!Error] 6.6 Encapsulation

* A variable or method of an object is said to be encapsulated if it is inaccessible to clients of the object. Encapsulation, sometimes called *information hiding*, is a key aspect of object-oriented programming.
* Go has only one mechanism to control the visibility of names: capitalized identifiers are exported from the package in which they are defined, and uncapitalized names are not. The same mechanism that limits access to members of a package also limits access to the fields of a struct or the methods of a type. As a consequence, to encapsulate an object, we must make it a struct.
* That’s the reason the `IntSet` type from the previous section was declared as a struct type even though it has only a single field:
	```go
	type IntSet struct {
		words []uint64
	}
	```
* We could instead define `IntSet` as a slice type as follows, though of course we’d have to replace each occurrence of `s.words` by `*s` in its methods:
	```go
	type IntSet []uint64
	```
* Although this version of `IntSet` would be essentially equivalent, it would allow clients from other packages to read and modify the slice directly. Put another way, whereas the expression `*s` could be used in any package, `s.words` may appear only in the package that defines `IntSet`.
* Another consequence of this name-based mechanism is that the unit of encapsulation is the package, not the type as in many other languages. The fields of a struct type are visible to all code within the same package. Whether the code appears in a function or a method makes no difference.
---
* Encapsulation provides three benefits.
* First, because clients cannot directly modify the object’s variables, one need inspect fewer statements to understand the possible values of those variables.
* Second, hiding implementation details prevents clients from depending on things that might change, which gives the designer greater freedom to evolve the implementation without breaking API compatibility.
* The third benefit of encapsulation, and in many cases the most important, is that it prevents clients from setting an object’s variables arbitrarily. Because the object’s variables can be set only by functions in the same package, the author of that package can ensure that all those functions maintain the object’s internal invariants.
---
* Functions that merely access or modify internal values of a type are called *getters* and *setters*.
* However, when naming a *getter* method, we usually omit the Get prefix. This preference for brevity extends to all methods, not just field accessors, and to other redundant prefixes as well, such as Fetch, Find, and Lookup.
* Go style does not forbid exported fields. Of course, once exported, a field cannot be unexported without an incompatible change to the API, so the initial choice should be deliberate and should consider the complexity of the invariants that must be maintained, the likelihood of future changes, and the quantity of client code that would be affected by a change.

### 7. Interfaces
> `pg: 46`
> `time req: 2' 34"`

> [!Error] 7.1 Interfaces as Contracts

* All the types we’ve looked at so far have been concrete types. A concrete type specifies the exact representation of its values and exposes the intrinsic operations of that representation, such as arithmetic for numbers, or indexing, append, and range for slices. A concrete type may also provide additional behaviors through its methods. When you have a value of a concrete type, you know exactly what it is and what you can do with it.
* There is another kind of type in Go called an interface type. An interface is an *abstract* type. It doesn’t expose the representation or internal structure of its values, or the set of basic operations they support; it reveals only some of their methods. When you have a value of an interface type, you know nothing about what it is; you know only what it can do, or more precisely, what behaviors are provided by its methods.
* This freedom to substitute one type for another that satisfies the same interface is called *substitutability*, and is a hallmark of object-oriented programming.
```go
package io
// Writer is the interface that wraps the basic Write method.
type Writer interface {
	// Write writes len(p) bytes from p to the underlying data stream.
	// It returns the number of bytes written from p (0 <= n <= len(p))
	// and any error encountered that caused the write to stop early.
	// Write must return a non-nil error if it returns n < len(p).
	// Write must not modify the slice data, even temporarily.
	//
	// Implementations must not retain p.
	Write(p []byte) (n int, err error)
}
```
* Declaring a String method makes a type satisfy one of the most widely used interfaces of all, `fmt.Stringer`:
```go
package fmt
// The String method is used to print values passed
// as an operand to any format that accepts a string
// or to an unformatted printer such as Print.
type Stringer interface {
	String() string
}
```

> [!Error] 7.2 Interface Types

* An interface type specifies a set of methods that a concrete type must possess to be considered an instance of that interface.
```go
package io
type Reader interface {
	Read(p []byte) (n int, err error)
}
type Closer interface {
	Close() error
}
```
* Interface Embedding:
```go
type ReadWriter interface {
	Reader
	Writer
}
type ReadWriteCloser interface {
	Reader
	Writer
	Closer
}
```

> [!Error] 7.3 Interface Satisfaction

* A type *satisfies* an interface if it possesses all the methods the interface requires. For example, an `*os.File` satisfies `io.Reader`, `Writer`, `Closer`, and `ReadWriter`. A `*bytes.Buffer` satisfies `Reader`, `Writer`, and `ReadWriter`, but does not satisfy `Closer` because it does not have a `Close` method.
* As a shorthand, Go programmers often say that a concrete type ‘‘is a’’ particular interface type, meaning that it satisfies the interface. For example, a `*bytes.Buffer` is an `io.Writer`; an `*os.File` is an `io.ReadWriter`.
* The *assignability* rule for interfaces is very simple: an expression may be assigned to an interface only if its type satisfies the interface. (side note: this is similar to polymorphism in c++)
```go
var w io.Writer
w = os.Stdout         // OK: *os.File has Write method
w = new(bytes.Buffer) // OK: *bytes.Buffer has Write method
w = time.Second // compile error: time.Duration lacks Write method

var rwc io.ReadWriteCloser
rwc = os.Stdout // OK: *os.File has Read, Write, Close methods
rwc = new(bytes.Buffer)
// compile error: *bytes.Buffer lacks Close method

// This rule applies even when the right-hand side is itself an interface:
w = rwc // OK: io.ReadWriteCloser has Write method
rwc = w // compile error: io.Writer lacks Close method
```
---
* Before we go further, we should explain one subtlety in what it means for a type to have a method. For each named concrete type `T`, some of its methods have a receiver of type `T` itself whereas others require a `*T` pointer. Recall also that it is legal to call a `*T` method on an argument of type `T` so long as the argument is a variable; the compiler implicitly takes its address. But this is mere syntactic sugar: a value of type `T` does not possess all the methods that a `*T` pointer does, and as a result it might satisfy fewer interfaces.
* The `String` method of the `IntSet` type requires a pointer receiver, so we cannot call that method on a non addressable `IntSet` value:
```go
type IntSet struct { /* ... */ }
func (*IntSet) String() string
var _ = IntSet{}.String()
// compile error: String requires *IntSet receiver

// but we can call it on an IntSet variable:
var s IntSet
var _ = s.String()
// OK: s is a variable and &s has a String method

// However, since only *IntSet has a String method, only *IntSet satisfies the fmt.Stringer interface:
var _ fmt.Stringer = &s // OK
var _ fmt.Stringer = s // compile error: IntSet lacks String method
```
* Like an envelope that wraps and conceals the letter it holds, an interface wraps and conceals the concrete type and value that it holds. Only the methods revealed by the interface type may be called, even if the concrete type has others:
```go
os.Stdout.Write([]byte("hello"))  // OK: *os.File has Write method
os.Stdout.Close()  // OK: *os.File has Close method

var w io.Writer
w = os.Stdout
w.Write([]byte("hello"))  // OK: io.Writer has Write method
w.Close()  // compile error: io.Writer lacks Close method
```
---
* An interface with more methods, such as `io.ReadWriter`, tells us more about the values it contains, and places greater demands on the types that implement it, than does an interface with fewer methods such as `io.Reader`. So what does the type interface{}, which has no methods at all, tell us about the concrete types that satisfy it?
* That’s right: nothing. This may seem useless, but in fact the type `interface{}`, which is called the empty interface type, is indispensable. Because the empty interface type places no demands on the types that satisfy it, we can assign any value to the empty interface.
```go
var any interface{}
any = true
any = 12.34
any = "hello"
any = map[string]int{"one": 1}
any = new(bytes.Buffer)
```
* Of course, having created an interface{} value containing a boolean, float, string, map, pointer, or any other type, we can do nothing directly to the value it holds since the interface has no methods. We need a way to get the value back out again. *spoiler alert:* this is type assertion.
---
* Non-empty interface types such as io.Writer are most often satisfied by a pointer type, particularly when one or more of the interface methods implies some kind of mutation to the receiver, as the Write method does. A pointer to a struct is an especially common method-bearing type.
* But pointer types are by no means the only types that satisfy interfaces, and even interfaces with mutator methods may be satisfied by one of Go’s other reference types.
---
* Each grouping of concrete types based on their shared behaviors can be expressed as an interface type. Unlike class-based languages, in which the set of interfaces satisfied by a class is explicit, in Go we can define new abstractions or groupings of interest when we need them, without modifying the declaration of the concrete type. This is particularly useful when the concrete type comes from a package written by a different author. Of course, there do need to be underlying commonalities in the concrete types.

> [!Error] 7.5 Interface Values

* Conceptually, a value of an interface type, or *interface value*, has two components, a concrete type and a value of that type. These are called the interface’s *dynamic type* and *dynamic value*.
* For a statically typed language like Go, types are a compile-time concept, so a type is not a value. In our conceptual model, a set of values called *type descriptors* provide information about each type, such as its name and methods. In an interface value, the type component is represented by the appropriate type descriptor.
* In the four statements below, the variable w takes on three different values. (The initial and final values are the same.)
	```go
	var w io.Writer
	w = os.Stdout
	w = new(bytes.Buffer)
	w = nil
	```
* Let’s take a closer look at the value and dynamic behavior of `w` after each statement. The first statement declares `w`:
	```go
	var w io.Writer
	```
* In Go, variables are always initialized to a well-defined value, and interfaces are no exception. The zero value for an interface has both its type and value components set to `nil`.
	![[Languages/Golang/go-aad-images/fig7.1.png]]
* An interface value is described as nil or non-nil based on its dynamic type, so this is a nil interface value. You can test whether an interface value is nil using `w == nil` or `w != nil`.
* Calling any method of a nil interface value causes a panic:
	```go
	w.Write([]byte("hello")) // panic: nil pointer dereference
	```
* The second statement assigns a value of type `*os.File` to `w`:
	```go
	w = os.Stdout
	```
* This assignment involves an implicit conversion from a concrete type to an interface type, and is equivalent to the explicit conversion `io.Writer(os.Stdout)`. A conversion of this kind, whether explicit or implicit, captures the type and the value of its operand. The interface value’s dynamic type is set to the type descriptor for the pointer type `*os.File`, and its dynamic value holds a copy of `os.Stdout`, which is a pointer to the `os.File` variable representing the standard output of the process.
	![[Languages/Golang/go-aad-images/fig7.2.png]]
* Calling the `Write` method on an interface value containing an `*os.File` pointer causes the `(*os.File).Write` method to be called. The call prints `"hello"`.
	```go
	w.Write([]byte("hello")) // "hello"
	```
* In general, we cannot know at compile time what the dynamic type of an interface value will be, so a call through an interface must use dynamic dispatch. Instead of a direct call, the compiler must generate code to obtain the address of the method named `Write` from the type descriptor, then make an indirect call to that address. The receiver argument for the call is a copy of the interface’s dynamic value, `os.Stdout`. The effect is as if we had made this call directly:
	```go
	os.Stdout.Write([]byte("hello")) // "hello"
	```
* The third statement assigns a value of type `*bytes.Buffer` to the interface value:
	```go
	w = new(bytes.Buffer)
	```
* The dynamic type is now `*bytes.Buffer` and the dynamic value is a pointer to the newly allocated buffer.
	![[Languages/Golang/go-aad-images/fig7.3.png]]
* A call to the `Write` method uses the same mechanism as before:
	```go
	w.Write([]byte("hello")) // writes "hello" to the bytes.Buffer
	```
* This time, the type descriptor is `*bytes.Buffer`, so the `(*bytes.Buffer).Write` method is called, with the address of the buffer as the value of the receiver parameter. The call appends `"hello"` to the buffer.
* Finally, the fourth statement assigns nil to the interface value:
	```go
	w = nil
	```
* This resets both its components to nil, restoring w to the same state as when it was declared.
---
---
* An interface value can hold arbitrarily large dynamic values. For example, the `time.Time` type, which represents an instant in time, is a struct type with several unexported fields. If we create an interface value from it,
	```go
	var x interface{} = time.Now()
	```
* the result will look like this:
	![[Languages/Golang/go-aad-images/fig7.4.png]]
* Conceptually, the dynamic value always fits inside the interface value, no matter how large its type. (This is only a conceptual model; a realistic implementation is quite different.)
* Interface values may be compared using `==` and `!=`. Two interface values are equal if both are nil, or if their dynamic types are identical and their dynamic values are equal according to the usual behavior of == for that type.
* Because interface values are comparable, they may be used as the keys of a map or as the operand of a switch statement.
* However, if two interface values are compared and have the same dynamic type, but that type is not comparable (a slice, for instance), then the comparison fails with a panic:
	```go
	var x interface{} = []int{1, 2, 3}
	fmt.Println(x == x) // panic: comparing uncomparable type []int
	```
* In this respect, interface types are unusual. Other types are either safely comparable (like basic types and pointers) or not comparable at all (like slices, maps, and functions), but when comparing interface values or aggregate types that contain interface values, we must be aware of the potential for a panic. A similar risk exists when using interfaces as map keys or switch operands. Only compare interface values if you are certain that they contain dynamic values of comparable types.

> [!subsubsection] 7.5.1 Caveat: An Interface Containing a Nil Pointer is Non-Nil

* A nil interface value, which contains no value at all, is not the same as an interface value containing a pointer that happens to be nil. This subtle distinction creates a trap into which every Go programmer has stumbled.
* Consider the program below. With `debug` set to `true`, the main function collects the output of the function `f` in a `bytes.Buffer`.
```go
const debug = true
func main() {
	var buf *bytes.Buffer
	if debug {
		buf = new(bytes.Buffer) // enable collection of output
	}
	f(buf) // NOTE: subtly incorrect!
	if debug {
		// ...use buf...
	}
}
// If out is non-nil, output will be written to it.
func f(out io.Writer) {
	// ...do something...
	if out != nil {
		out.Write([]byte("done!\n"))
	}
}

// We might expect that changing debug to false would disable the collection of the output, but in fact it causes the program to panic during the out.Write call:
	if out != nil {
		out.Write([]byte("done!\n"))
		// panic: nil pointer dereference
	}
```
* When main calls `f`, it assigns a nil pointer of type `*bytes.Buffer` to the out parameter, so the dynamic value of out is nil. However, its dynamic type is `*bytes.Buffer`, meaning that out is a non-nil interface containing a nil pointer value, so the defensive check `out != nil` is still true.
	![[Languages/Golang/go-aad-images/fig7.5.png]]
* As before, the dynamic dispatch mechanism determines that `(*bytes.Buffer).Write` must be called but this time with a receiver value that is nil. For some types, such as `*os.File`, nil is a valid receiver, but `*bytes.Buffer` is not among them. The method is called, but it panics as it tries to access the buffer.
* The problem is that although a nil `*bytes.Buffer` pointer has the methods needed to satisfy the interface, it doesn’t satisfy the *behavioral requirements* of the interface. In particular, the call violates the implicit precondition of `(*bytes.Buffer).Write` that its receiver is not nil, so assigning the nil pointer to the interface was a mistake.
* The solution is to change the type of `buf` in main to `io.Writer`, thereby avoiding the assignment of the dysfunctional value to the interface in the first place:
	```go
		var buf io.Writer
		if debug {
			buf = new(bytes.Buffer) // enable collection of output
		}
		f(buf) // OK
	```

> [!Error] 7.8 The `error` Interface

```go
type error interface {
	Error() string
}
```

* The simplest way to create an `error` is by calling `errors.New`, which returns a new error for a given error message.
* The entire `errors` package is only four lines long:
	```go
	package errors
	func New(text string) error { return &errorString{text} }
	type errorString struct { text string }
	func (e *errorString) Error() string { return e.text }
	```
* The underlying type of `errorString` is a struct, not a string, to protect its representation from inadvertent (or premeditated) updates. And the reason that the pointer type `*errorString`, not `errorString` alone, satisfies the error interface is so that every call to New allocates a distinct error instance that is equal to no other. We would not want a distinguished error such as `io.EOF` to compare equal to one that merely happened to have the same message.
	```go
	fmt.Println(errors.New("EOF") == errors.New("EOF")) // "false"
	```
* Calls to `errors.New` are relatively infrequent because there’s a convenient wrapper function, `fmt.Errorf`, that does string formatting too.

> [!Error] 7.10 Type Assertions

* A type assertion is an operation applied to an interface value. Syntactically, it looks like `x.(T)`, where `x` is an expression of an interface type and `T` is a type, called the ‘‘asserted’’ type.
* A type assertion checks that the dynamic type of its operand matches the asserted type.
* There are two possibilities. First, if the asserted type `T` is a concrete type, then the type assertion checks whether `x`’s dynamic type is identical to `T`. If this check succeeds, the result of the type assertion is `x`’s dynamic value, whose type is of course `T`. In other words, a type assertion to a concrete type extracts the concrete value from its operand. If the check fails, then the operation panics. For example:
	```go
	var w io.Writer
	w = os.Stdout
	f := w.(*os.File)
	// success: f == os.Stdout
	c := w.(*bytes.Buffer)
	// panic: interface holds *os.File, not *bytes.Buffer
	```
* Second, if instead the asserted type `T` is an interface type, then the type assertion checks whether x’s dynamic type satisfies `T`. If this check succeeds, the dynamic value is not extracted; the result is still an interface value with the same type and value components, but the result has the interface type `T`. In other words, a type assertion to an interface type changes the type of the expression, making a different (and usually larger) set of methods accessible, but it preserves the dynamic type and value components inside the interface value.
* After the first type assertion below, both `w` and `rw` hold `os.Stdout` so each has a dynamic type of `*os.File`, but `w`, an `io.Writer`, exposes only the file’s Write method, whereas `rw` exposes its Read method too.
	```go
	var w io.Writer
	w = os.Stdout
	rw := w.(io.ReadWriter) // success: *os.File has both Read and Write
	w = new(ByteCounter)
	rw = w.(io.ReadWriter) // panic: *ByteCounter has no Read method
	```
* No matter what type was asserted, if the operand is a `nil` interface value, the type assertion fails. A type assertion to a less restrictive interface type (one with fewer methods) is rarely needed, as it behaves just like an assignment, except in the `nil` case.
	```go
	w = rw // io.ReadWriter is assignable to io.Writer
	w = rw.(io.Writer) // fails only if rw == nil
	```
* Often we’re not sure of the dynamic type of an interface value, and we’d like to test whether it is some particular type. If the type assertion appears in an assignment in which two results are expected, such as the following declarations, the operation does not panic on failure but instead returns an additional second result, a boolean indicating success:
	```go
	var w io.Writer = os.Stdout
	f, ok := w.(*os.File)      // success: ok, f == os.Stdout
	b, ok := w.(*bytes.Buffer) // failure: !ok, b == nil
	```
* The second result is conventionally assigned to a variable named `ok`. If the operation failed, `ok` is false, and the first result is equal to the zero value of the asserted type, which in this example is a `nil` `*bytes.Buffer`.
* The `ok` result is often immediately used to decide what to do next. The extended form of the if statement makes this quite compact:
	```go
	if f, ok := w.(*os.File); ok {
		// ...use f...
	}
	```
* When the operand of a type assertion is a variable, rather than invent another name for the new local variable, you’ll sometimes see the original name reused, shadowing the original, like this:
	```go
	if w, ok := w.(*os.File); ok {
		// ...use w...
	}
	```

> [!Error] 7.11 Discriminating Errors with type Assertions

* Consider the set of errors returned by file operations in the `os` package. I/O can fail for any number of reasons, but three kinds of failure often must be handled differently: file already exists (for create operations), file not found (for read operations), and permission denied.
* The `os` package provides these three helper functions to classify the failure indicated by a given error value:
	```go
	package os
	func IsExist(err error) bool
	func IsNotExist(err error) bool
	func IsPermission(err error) bool
	```
* Of course, error structure is lost if the error message is combined into a larger string, for instance by a call to `fmt.Errorf`. Error discrimination must usually be done immediately after the failing operation, before an error is propagated to the caller.

> [!Error] 7.13 Type Switches

* Interfaces are used in two distinct styles. In the first style, exemplified by `io.Reader`, `io.Writer`, `fmt.Stringer`, `sort.Interface`, `http.Handler`, and `error`, an interface’s methods express the similarities of the concrete types that satisfy the interface but hide the representation details and intrinsic operations of those concrete types. The emphasis is on the methods, not on the concrete types.
* The second style exploits the ability of an interface value to hold values of a variety of concrete types and considers the interface to be the union of those types. Type assertions are used to discriminate among these types dynamically and treat each case differently. In this style, the emphasis is on the concrete types that satisfy the interface, not on the interface’s methods (if indeed it has any), and there is no hiding of information. We’ll describe interfaces used this way as *discriminated unions*.
* A switch statement simplifies an if-else chain that performs a series of value equality tests. An analogous type switch statement simplifies an if-else chain of type assertions.
* In its simplest form, a type switch looks like an ordinary switch statement in which the operand is `x.(type)`—that’s literally the keyword type—and each case has one or more types. A type switch enables a multi-way branch based on the interface value’s dynamic type. The `nil` case matches if `x == nil`, and the default case matches if no other case does. For example:
	```go
	switch x.(type) {
	case nil:
	case int, uint:
	case bool:
	case string:
	default:
	}
	```
* As with an ordinary switch statement, cases are considered in order and, when a match is found, the case’s body is executed. Case order becomes significant when one or more case types are interfaces, since then there is a possibility of two cases matching. The position of the default case relative to the others is immaterial. No fallthrough is allowed.
* Notice that in the original function, the logic for the bool and string cases needs access to the value extracted by the type assertion. Since this is typical, the type switch statement has an extended form that binds the extracted value to a new variable within each case:
	```go
	switch x := x.(type) { /* ... */ }
	```
* In type switches, within the block of each single-type case, the variable `x` has the same type as the case. In all other cases, `x` has the (interface) type of the switch operand (the original type). When the same action is required for multiple cases, like `case int, uint:`, the type switch makes it easy to combine them.

> [!Error] 7.15 A Few Words of Advice

* When designing a new package, novice Go programmers often start by creating a set of interfaces and only later define the concrete types that satisfy them. This approach results in many interfaces, each of which has only a single implementation. Don’t do that. Such interfaces are unnecessary abstractions; they also have a run-time cost. You can restrict which methods of a type or fields of a struct are visible outside a package using the export mechanism. Interfaces are only needed when there are two or more concrete types that must be dealt with in a uniform way.
* We make an exception to this rule when an interface is satisfied by a single concrete type but that type cannot live in the same package as the interface because of its dependencies. In that case, an interface is a good way to decouple two packages.
* Because interfaces are used in Go only when they are satisfied by two or more types, they necessarily abstract away from the details of any particular implementation. The result is smaller interfaces with fewer, simpler methods, often just one as with `io.Writer` or `fmt.Stringer`. Small interfaces are easier to satisfy when new types come along. A good rule of thumb for interface design is ***ask only for what you need***.

### 8. Goroutines and Channels
> `pg: 40`
> `time req: 2' 14"`



### 9. Concurrency with Shared Variables
> `pg: 26`
> `time req: 1' 27"`

### 10. Packages and the Go Tool
> `pg: 18`
> `time req: 1'`

### 11. Testing
> `pg: 28`
> `time req: 1' 34"`

### 12. Reflection
> `pg: 24`
> `time req: 1' 20"`

### 13. Low-Level Programming
> `pg: 14`
> `time req: 47"`