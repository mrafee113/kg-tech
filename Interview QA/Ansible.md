1. What is Ansible, and how does it differ from other configuration management tools?
	Ansible is an open-source automation tool used for configuration management, application deployment, and task automation. It operates over SSH and does not require any agents to be installed on target systems. Unlike some other tools, Ansible follows a declarative approach, describing the desired state of systems rather than specifying explicit commands.
2. What are Ansible playbooks?
	Ansible playbooks are YAML files that define a set of tasks to be executed on remote systems. Playbooks describe how Ansible should configure, manage, and orchestrate tasks across multiple systems in a structured and easily readable format.
3. How does Ansible handle idempotence?
	Ansible is idempotent, meaning that running the same playbook multiple times should result in the same consistent state. If a task has already been executed and the system is in the desired state, Ansible will not perform unnecessary changes, reducing the risk of unintended changes.
4. Explain the difference between Ansible ad-hoc commands and playbooks.
	Ad-hoc commands are one-liners executed from the command line, while playbooks are more structured, reusable, and organized scripts that allow for complex orchestration of tasks. Playbooks are better suited for managing larger configurations and workflows.
5. What is an Ansible role, and how does it promote reusability?
	An Ansible role is a predefined way of organizing playbooks and related files to perform specific automation tasks. Roles promote code reusability by encapsulating configuration, tasks, variables, and templates into modular units that can be easily reused across projects.
6. How does Ansible ensure secure communication with remote hosts?
	Ansible communicates with remote hosts over SSH by default. It uses SSH keys and provides options to securely manage credentials and vault encrypted files to protect sensitive information.
7. What is Ansible Tower (AWX), and how does it enhance Ansible's capabilities?
	Ansible Tower (or AWX, the open-source version) is a web-based UI and automation tool that adds enhanced capabilities to Ansible. It provides centralized control, scheduling, inventory management, role-based access control, and visual insights into playbook runs.
8. How can you dynamically manage inventory in Ansible?
	Ansible supports dynamic inventory by allowing inventory sources to be scripts, databases, or external systems. You can write custom inventory scripts or use tools like dynamic inventory plugins to fetch real-time data about your infrastructure.
9. How do you handle sensitive data, such as passwords, in Ansible?
	Ansible provides the concept of "Vault" to encrypt sensitive data. You can use `ansible-vault` to create and manage encrypted files containing variables or secrets. Playbooks can reference these vault-encrypted files for secure configuration.
