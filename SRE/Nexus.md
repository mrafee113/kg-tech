d> [source](https://help.sonatype.com/repomanager3)

## Repository Manager Concepts
> [source](https://help.sonatype.com/repomanager3/using-nexus-repository/repository-manager-concepts)

* Using Nexus Repository as well as the tools for software supply chain automation using the Nexus IQ Server and associated tools of the Nexus platform requires an understanding of a few concepts and terms like component, repository and repository format. This section provides you with all the necessary background and knowledge as well as an idea of a progression in your usage of the tools from the Nexus platform.

### Components, Repositories, and Repository Formats
> [source](https://help.sonatype.com/repomanager3/using-nexus-repository/repository-manager-concepts/components%2C-repositories%2C-and-repository-formats)

* The Nexus platform, with Nexus Repository Pro, Nexus Repository OSS, and Nexus IQ Server is all about working with components and repositories.

#### Components
* A component is a package of resources that your software application uses (e.g., a library or a framework). Some examples of components include the following:
	* Java byte code in class files
	* C object files
	* text files (e.g., properties files, XML files, JavaScript code, HTML, CSS
	* binary files such as images, PDF files, sound files
* Components can come in numerous formats, including the following:
	* Java JAR, WAR, EAR formats
	* plain ZIP or .tar.gz files
	* other package formats such as NuGet packages, Ruby gems, NPM packages
	* executable formats, Android APK files, various installer formats
* Components can be as complex as an entire application or as simple as a static resource; they can even comprise multiple nested components themselves along with assets. For example, a Java web application may be packaged as a WAR component containing multiple JAR components and a number of JavaScript libraries. These JARs and libraries are also standalone components in other contexts while also being included as part of the WAR component.
* While we use the generic term "component" in Nexus Repository, components are also called artifacts, packages, bundles, archives, and other terms.
* Each component is identified by a unique set of coordinates. For example, you may have heard of GAV (group, artifact, and version) coordinates for Maven; however, coordinate names and usage strategies vary between formats.

#### Assets
* An asset is a single file associated with a component. Many formats have a one-to-one mapping for component to asset; however, more complex formats have numerous assets associated with a component. For example, a typical JAR component in a Maven repository is defined at least by the POM and the JAR files; each file as well as additional files (e.g., Javadoc, Sources JAR) is a separate asset belonging to the same component.
* In the Docker format, assets have unique identifiers called Docker layers. You can reuse these assets can for different components (i.e., Docker images). As Docker can be complex, we cover it in depth in Components and Assets in Docker.

#### Components in Repositories
* The open source community as well as proprietary vendors are continually creating new components. For example, there are libraries and frameworks written in various languages on different platforms that developers use for application development every day.
* Developers typically build applications for a specific domain by combining multiple components' features with their own custom components containing their application code.
* To make consumption and usage easier, components are aggregated into collections called a repository; these are typically available on the internet as a service. Different platforms may use terms such as "registry" and others to refer to repositories.
* Examples of repositories available on the internet as a service include the following:
	* Central Repository, also known as Maven Central
	* NuGet Gallery
	* [RubyGems.org](http://rubygems.org/)
	* [npmjs.org](http://npmjs.org/)
	* [Docker](https://hub.docker.com/search?q=)
* Numerous tools like the following access components in these repositories:
	* package managers like npm, nuget, gem
	* build tools such as Maven, Gradle, rake, grunt
	* IDE’s such as Eclipse, IntelliJ, Visual Studio

#### Repository Formats
* Different repositories use different technologies to store and expose the components in them to client tools. These technologies define a repository format that is closely related to the tools interacting with the repository.
* For example, the Maven repository format relies on a specific directory structure defined by the components' identifiers and a number of XML-formatted files for metadata. Component interaction is performed via plain HTTP commands and some additional custom interaction with the XML files.
* Other repository formats use databases for storage and REST API interactions or different directory structures with format-specific files for the metadata.

### Managing Repositories
> [source](https://help.sonatype.com/repomanager3/using-nexus-repository/repository-manager-concepts/managing-repositories)

* The proliferation of different repository formats and tools accessing them as well as the emergence of more publicly available repositories has triggered the need to manage access and usage of these repositories and the components they contain.
* In addition, hosting your own private repositories for internal components has proven to be a very efficient methodology to exchange components during all phases of the software development life cycle. It is considered a best practice at this stage.
* The task of managing all the repositories your development teams interact with can be supported by the use of a dedicated server application - a repository manager.
* Put simply, a repository manager provides two core features:
	* the ability to proxy a remote repository and cache components saving both bandwidth and time required to retrieve a software component from a remote repository repeatedly
	* the ability the host a repository providing an organization with a deployment target for internal software components
* Just as Source Code Management (SCM) tools are designed to manage source code, repository managers have been designed to manage and track external dependencies and components generated by your build.
* Repository managers are an essential part of any enterprise or open-source software development effort, and they enable greater collaboration between developers and wider distribution of software, by facilitating the exchange and usage of binary components.
* Once you start to rely on repositories, you realize how easy it is to add a dependency on an open source software library available in a public repository, and you might start to wonder how you can provide a similar level of convenience for your own developers. When you install a repository manager, you are bringing the power of a repository like the Central Repository into your organization. You can use it to proxy the Central Repositories and other repositories, and host your own repositories for internal and external use.

#### Capabilities of a Repository manager
* In addition to these two core features, a repository manager can support the following use cases:
	* allows you to manage binary software components through the software development life-cycle
	* search and catalogue software components
	* control component releases with rules and add automated notifications
	* integrate with external security systems, such as LDAP or Atlassian Crowd
	* manage component metadata
	* host components, not available in external repositories
	* control access to components and repositories
	* display component dependencies
	* browse component archive contents

#### Advantages of using a Repository manager
* Using a repository manager provides a number of benefits including:
	* improved software build performance due to faster component download off the local repository manager
	* reduced bandwidth usage due to component caching
	* higher predictability and scalability due to limited dependency on external repositories
	* increased understanding of component usage due to centralized storage of all used components
	* simplified developer configuration due to central access configuration to remote repositories and components on the repository manager
	* unified method to provide components to consumers reducing complexity overheads
	* improved collaboration due the simplified exchange of binary components

### Proxy Repository Concepts
> [source](https://help.sonatype.com/repomanager3/using-nexus-repository/repository-manager-concepts/proxy-repository-concepts)

* Explain the value of proxy repositories
* Discuss audit guidelines for proxy repositories 
* Share best practices when using proxies at scale

#### What is a Proxy Repository?
* Dependency managers use components from public open-source repositories such as Central, npm, and PyPI to build applications. They will often use the local cache first to see if the component already exists in order to reduce the number of requests and the bandwidth used to download all the components from the remote repository. This speeds up build times and keeps the final output consistent, however it can introduce risk as the local cache is not centrally managed or consistent everywhere the application is built. In a modern DevOps pipeline, organizations have multiple build servers and development teams so trying to manage multiple component caches is not efficient or cost-effective. Redirecting traffic through proxy repositories is a primary use case when using a universal artifact repository like Repository Manager.
* A proxy repository is a substitute access point and managed cache for remote repositories. These could be the public repositories for open source components or private repositories such as another Nexus Repository for instance. They respond in exactly the same way as the public repository would however they allow your organization to centrally manage to cache, ensure your dependencies are always available, and greatly reduce traffic to external servers. Here is a simple example of the proxy in action.
	1. Your build makes a request for a component from the proxy repository.
	2. If the component is not cached, the request is forwarded to the remote repository, downloaded, and cached to the local storage.
	3. The component is then forwarded to your build.
* Future requests for the same component skip the external request and immediately deliver the component.
* As part of a Nexus Repository Manager [Health check workshop](https://www.sonatype.com/learn-training-workshops), we review the server configuration and provide detailed recommendations on how to better optimize your repository instance. There are a number of recommendations regarding proxy repositories that are fairly universal to any production instance. We will go through the most common ones here.

#### Routing Rules
* Routing rules are incredibly useful tools that are often overlooked. Administrators use routing rules to limit requests to external repositories to only the artifacts needed from the proxy. Routing rules can help with dependency confusion like attacks against an organization’s internal namespace. Routing rules will speed up access times for group repositories by limiting requests to only the proxies where the components should be fetched.
* **Recommendations**
	* It is a best practice to use routing rules on all proxy repositories.
	* For public repositories, BLOCK access to internal namespaces to prevent dependency confusion attacks.
	* For other repositories, only ALLOW access to the namespaces that are required from that repository.