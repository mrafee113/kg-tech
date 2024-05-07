1. What is Docker, and why is it used in DevOps?
	Docker is a containerization platform that allows you to package, distribute, and run applications and their dependencies as isolated containers. Containers provide consistent environments across development, testing, and production, making it easier to manage and deploy applications in various environments.
2. What are containers, and how do they differ from virtual machines?
	Containers are lightweight, portable, and isolated environments for running applications. They package an application and its dependencies, including libraries and settings, into a single unit. Containers share the host OS kernel, making them more efficient and faster than virtual machines, which require separate guest OS instances.
3. Explain the difference between an image and a container in Docker.
	An image is a read-only template containing instructions for creating a Docker container. It includes the application code, runtime, libraries, and dependencies. A container is an instance of an image that can be executed, modified, and stopped.
4. What is a Dockerfile?
	A Dockerfile is a text-based script that contains a set of instructions to build a Docker image. It defines the base image, adds files, installs packages, and configures the environment for the application.
5. How do you share Docker images between environments?
	Docker images can be shared using Docker Hub, a public or private container registry, or by exporting and importing image files. Docker Hub is a popular cloud-based registry that hosts public images, while private registries provide secure storage for images within an organization.
6. What is a Docker Compose file, and how is it used?
	A Docker Compose file is a YAML file that defines a multi-container application. It describes services, networks, and volumes, allowing you to manage and run multi-container applications using a single command.
7. How do you manage persistent data in Docker containers?
	You can use Docker volumes to manage persistent data. Volumes are directories outside the container's file system that Docker manages. They allow data to be shared and preserved across container lifecycles.
8. Explain the concept of orchestration in Docker.
	Orchestration in Docker refers to managing the deployment, scaling, and operation of multiple containers that work together as a single application. Tools like Docker Swarm and Kubernetes provide orchestration capabilities to automate container deployment, scaling, load balancing, and failure recovery.
9. What is Docker Swarm, and how does it work?
	Docker Swarm is Docker's built-in orchestration tool for creating and managing a cluster of Docker nodes. It enables you to deploy and manage containers across multiple hosts, providing load balancing, high availability, and scaling capabilities.
10. How does Docker help achieve Continuous Integration and Continuous Deployment (CI/CD)?
	Docker's containerization ensures that the application environment is consistent across different stages of the CI/CD pipeline, from development to production. This reduces the "it works on my machine" problem and streamlines the deployment process. 
11. How do you ensure security in Docker containers?
	- Use official images from trusted sources.
	- Minimize the attack surface by only installing necessary packages.
	- Keep images and software updated regularly.
	- Use Docker Content Trust to verify image authenticity.
	- Apply proper user permissions and use non-root users in containers.
12. Explain the difference between a Docker image and a Docker container.
	A Docker image is a template used to create Docker containers. It contains the application code, runtime, and dependencies. A Docker container is a running instance of an image, isolated from the host system and other containers.
13. What are Docker volumes, and why are they used?
	Docker volumes are a mechanism for persistently storing data outside a container's file system. They are used to share data between containers, store configuration files, and manage data that needs to be preserved across container restarts.
14. What is a Docker registry, and how is it used?
	A Docker registry is a repository for Docker images. It stores images for distribution and sharing among teams. Docker Hub is a popular public registry, while organizations often set up private registries for security and control.
15. How do you build a Docker image from a Dockerfile?
	1. Navigate to the directory containing the Dockerfile. 
	2. Run the command: `docker build -t image-name .`
16. How do you remove a Docker container?
	To remove a Docker container: ```sh docker rm container-id ```
17. What is the purpose of a Dockerfile's `CMD` instruction?
	The `CMD` instruction in a Dockerfile specifies the default command that should be executed when a container is started from the image. It can be overridden by providing a command when running the container.
18. How can you inspect the logs of a Docker container?
	To inspect the logs of a Docker container: ```sh docker logs container-id ```
19. Can you tell something about docker namespace?
	A namespace is basically a Linux feature that ensures OS resources partition in a mutually exclusive manner. This forms the core concept behind containerization as namespaces introduce a layer of isolation amongst the containers. In docker, the namespaces ensure that the containers are portable and they don't affect the underlying host. Examples for namespace types that are currently being supported by Docker – PID, Mount, User, Network, IPC.
20. On what circumstances will you lose data stored in a container?
	The data of a container remains in it until and unless you delete the container.
21. How many Docker components are there?
	- Docker Client: This component performs “build” and “run” operations for the purpose of opening communication with the docker host.
	- Docker Host: This component has the main docker daemon and hosts containers and their associated images. The daemon establishes a connection with the docker registry.
	- Docker Registry: This component stores the docker images. There can be a public registry or a private one. The most famous public registries are Docker Hub and Docker Cloud.
22. What is Docker's layer-based architecture? How does it contribute to efficiency? 
	Docker uses a layered file system to create images. Each layer represents a set of file system changes. Layers are cached and shared between images, reducing storage requirements and improving build times. When an image is updated, only the changed layers need to be rebuilt.
23. Explain the concept of Docker image tagging and how it relates to versioning.
	Docker image tagging involves assigning labels to images, often representing versions or other identifiers. Tags help identify specific versions of images and allow for easier management and reference. It's essential to follow proper versioning practices to ensure consistency and traceability.
24. What are multi-stage builds in Docker, and why are they useful?
	Multi-stage builds allow you to create smaller and more efficient Docker images by building multiple stages in a single Dockerfile. Intermediate images are discarded, leaving only the final image with the necessary artifacts. This reduces image size and improves security by excluding build-related tools.
25. What is Docker's "build context," and why is it important?
	The build context is the set of files and directories sent to the Docker daemon for building an image. It's defined in the `docker build` command. The build context includes files referenced in the Dockerfile. Keeping the build context minimal is crucial for efficient image building.
26. Explain the differences between Docker containers and Kubernetes pods.
	Docker containers are the smallest deploy-able units in Docker, representing a single application and its dependencies. Kubernetes pods can contain one or more containers sharing the same network namespace and storage. Containers within a pod are co-located and can communicate via localhost.
27. How does Docker handle networking between containers in the same network?
	Docker provides a default bridge network for containers on the same host. Containers can communicate using IP addresses. However, Docker also supports user-defined networks that allow for better isolation, DNS-based service discovery, and container communication via container name.