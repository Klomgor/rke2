# Project Overview

This repository contains Ansible playbooks and roles for setting up and managing a Kubernetes cluster using RKE2. The purpose of this project is to provide a streamlined and automated way to deploy and configure a Kubernetes cluster with various components and services.

## Features

- Automated deployment of RKE2 Kubernetes cluster
- Helm repository management and chart deployments
- Kubernetes resource and configuration management
- SSH configuration and key distribution
- Common tasks for setting up nodes
- Security enhancements and RBAC configurations

## Setup and Usage

### Prerequisites

- Ansible 2.9 or later
- Python 3.6 or later
- Access to the target nodes with SSH

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-org/your-repo.git
   cd your-repo
   ```

2. Install required Ansible collections:

   ```bash
   ansible-galaxy collection install -r collections/requirements.yaml
   ```

3. Update the inventory file (`inventory/hosts.yml`) with the target nodes' information.

4. Update the group variables file (`inventory/group_vars/all.yml`) with the necessary configuration values.

5. Encrypt sensitive data in the group variables file using Ansible Vault:

   ```bash
   ansible-vault encrypt inventory/group_vars/all.yml
   ```

6. Run the playbook to set up the Kubernetes cluster:

   ```bash
   ansible-playbook site.yml
   ```

## Troubleshooting

### Common Issues

1. **Connection Timeout**

   If you encounter connection timeouts, try increasing the `timeout` value in the `ansible.cfg` file.

2. **Host Key Checking**

   If you face host key checking issues, set `host_key_checking` to `False` in the `ansible.cfg` file.

3. **Retry Files**

   If you want to control the creation of retry files, set the `retry_files_enabled` option in the `ansible.cfg` file.

4. **Sensitive Data**

   Ensure that sensitive data is encrypted using Ansible Vault to prevent unauthorized access.

5. **Role-Based Access Control**

   Implement role-based access control using Ansible Tower or AWX to manage and execute playbooks securely.

6. **Updating Dependencies**

   Regularly update dependencies and packages to ensure the latest security patches are applied.

## Contributing

We welcome contributions to improve this project. Please follow the guidelines in the `CONTRIBUTING.md` file for submitting pull requests and reporting issues.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
