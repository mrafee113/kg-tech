### Ansible Vault
> [source](https://docs.ansible.com/ansible/latest/vault_guide/vault.html)
* Ansible Vault encrypts variables and files so you can protect sensitive content such as passwords or keys rather than leaving it visible as plaintext in playbooks or roles.
* To use Ansible Vault you need one or more passwords to encrypt and decrypt content.
* If you store your vault passwords in a third-party tool such as a secret manager, you need a script to access them. Use the passwords with the [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html#ansible-vault) command-line tool to create and view encrypted variables, create encrypted files, encrypt existing files, or edit, re-key, or decrypt files. You can then place encrypted content under source control and share it more safely.

> [!Warning]
> Encryption with Ansible Vault ONLY protects ‘data at rest’. Once the content is decrypted (‘data in use’), play and plugin authors are responsible for avoiding any secret disclosure, see [no_log](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#keep-secret-data) for details on hiding output and [Steps to secure your editor](https://docs.ansible.com/ansible/latest/vault_guide/vault_encrypting_content.html#vault-securing-editor) for security considerations on editors you use with Ansible Vault.

* You can use encrypted variables and files in ad hoc commands and playbooks by supplying the passwords you used to encrypt them. You can modify your `ansible.cfg` file to specify the location of a password file or to always prompt for the password.

### Managing vault passwords
> [source](https://docs.ansible.com/ansible/latest/vault_guide/vault_managing_passwords.html)
* Managing your encrypted content is easier if you develop a strategy for managing your vault passwords. A vault password can be any string you choose. There is no special command to create a vault password. However, you need to keep track of your vault passwords. Each time you encrypt a variable or file with Ansible Vault, you must provide a password. When you use an encrypted variable or file in a command or playbook, you must provide the same password that was used to encrypt it.
* To develop a strategy for managing vault passwords, start with two questions:
	* Do you want to encrypt all your content with the same password, or use different passwords for different needs?
	* Where do you want to store your password or passwords?

#### Choosing between a single password and multiple passwords
* If you have a small team or few sensitive values, you can use a single password for everything you encrypt with Ansible Vault. Store your vault password securely in a file or a secret manager as described below.
* If you have a larger team or many sensitive values, you can use multiple passwords. For example, you can use different passwords for different users or different levels of access. Depending on your needs, you might want a different password for each encrypted file, for each directory, or for each environment. For example, you might have a playbook that includes two vars files, one for the dev environment and one for the production environment, encrypted with two different passwords. When you run the playbook, select the correct vault password for the environment you are targeting, using a vault ID.

#### Managing multiple passwords with vault IDs
* If you use multiple vault passwords, you can differentiate one password from another with vault IDs. You use the vault ID in three ways:
	* Pass it with [`--vault-id`](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#cmdoption-ansible-playbook-vault-id) to the [ansible-vault](https://docs.ansible.com/ansible/latest/cli/ansible-vault.html#ansible-vault) command when you create encrypted content
	* Include it wherever you store the password for that vault ID (see [Storing and accessing vault passwords](https://docs.ansible.com/ansible/latest/vault_guide/vault_managing_passwords.html#storing-vault-passwords))
	* Pass it with [`--vault-id`](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#cmdoption-ansible-playbook-vault-id) to the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#ansible-playbook) command when you run a playbook that uses content you encrypted with that vault ID
