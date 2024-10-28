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

3. Update the inventory file (`inventory/hosts.yaml`) with the target nodes' information.

4. Update the group variables file (`inventory/group_vars/all.yaml`) with the necessary configuration values.

5. Encrypt sensitive data in the group variables file using Ansible Vault:

   ```bash
   ansible-vault encrypt inventory/group_vars/all.yaml
   ```

6. Run the playbook to set up the Kubernetes cluster:

   ```bash
   ansible-playbook site.yaml
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

## Key Components of the Kubernetes Cluster Setup

The key components of the Kubernetes cluster setup in this repository are:

* `inventory/group_vars/all.yaml`: Contains configuration variables for Kubernetes, including versions, network settings, load balancer settings, storage settings, monitoring settings, security settings, backup settings, service mesh settings, Vault configuration, ArgoCD configuration, Istio configuration, TLS configuration, and MetalLB configuration.
* `inventory/hosts.yaml`: Defines the inventory of hosts, including master nodes, worker nodes, storage nodes, and an admin node.
* `roles/common/tasks/main.yaml`: Installs required packages, sets up kernel modules, configures sysctl parameters, and installs RKE2.
* `roles/admin/tasks/main.yaml`: Installs required packages, kubectl, Helm, Rancher CLI, and other tools on the admin node. It also sets up kubeconfig and bash completion for kubectl and Helm.
* `roles/components/tasks/main.yaml`: Adds required Helm repositories and deploys various components such as Cert-Manager, MetalLB, Longhorn, ArgoCD, Vault, Velero, and Istio.
* `roles/install-rancher/tasks/main.yaml`: Installs Rancher on the admin node.
* `roles/kube-vip/tasks/main.yaml`: Deploys Kube VIP configuration for load balancing.
* `roles/kubernetes/tasks/main.yaml`: Manages Kubernetes resources and configurations, including applying manifests, deploying network policies, and deploying security configurations.
* `roles/monitoring/tasks/main.yaml`: Adds Prometheus and Grafana Helm repositories, creates a monitoring namespace, and deploys kube-prometheus-stack and Loki stack for monitoring.
* `roles/prepare-admin/tasks/main.yaml`: Prepares the admin node by ensuring SSH configuration, installing kubectl, and setting up SSH keys.
* `roles/prepare-nodes/tasks/main.yaml`: Prepares the nodes by enabling IPv4 and IPv6 forwarding.
* `roles/rke2-download/tasks/main.yaml`: Downloads the RKE2 binary.
* `roles/rke2-prepare/tasks/main.yaml`: Prepares RKE2 on servers and agents, including creating directories, deploying configurations, and setting up systemd services.
* `roles/rke2/tasks/main.yaml`: Deploys RKE2 agent and server configurations, ensures services are running, and applies Kube VIP configuration.
* `roles/security/tasks/main.yaml`: Creates a security namespace, deploys network policies, pod security policies, Falco, and RBAC configurations.
* `roles/storage/tasks/main.yaml`: Installs storage prerequisites, configures RKE2 agent for storage nodes, and starts the RKE2 agent service.
* `roles/worker/tasks/main.yaml`: Configures RKE2 agent on worker nodes and starts the RKE2 agent service.
* `site.yaml`: Defines the playbooks for setting up the RKE2 cluster, including preparing nodes, downloading RKE2, deploying Kube VIP, preparing RKE2 on servers and agents, adding additional servers and agents, applying manifests, installing Rancher, installing Longhorn, and deploying monitoring stack.

## Best Practices

### Idempotency

To ensure the playbooks are idempotent, consider the following suggestions:

* Use the `creates` attribute in tasks that download or install files, such as in `roles/admin/tasks/main.yaml` and `roles/common/tasks/main.yaml`, to prevent re-execution if the file already exists.
* Use the `changed_when` attribute to explicitly specify when a task should be considered changed, as seen in `roles/install-rancher/tasks/main.yaml`.
* Use the `when` attribute to conditionally execute tasks based on the current state of the system, as demonstrated in `roles/rke2-prepare/tasks/main.yaml`.
* Use the `stat` module to check the state of files or directories before performing actions, as seen in `roles/rke2-prepare/tasks/main.yaml`.
* Use the `lineinfile` and `blockinfile` modules to ensure specific lines or blocks of text are present in configuration files, as shown in `roles/admin/tasks/main.yaml`.
* Use the `ansible.builtin.wait_for` module to wait for specific conditions to be met before proceeding with the next task, as seen in `roles/rke2-prepare/tasks/main.yaml`.
* Use the `ansible.builtin.fetch` and `ansible.builtin.copy` modules to transfer files between nodes, ensuring they are only copied if they do not already exist, as demonstrated in `roles/admin/tasks/main.yaml`.
* Use the `ansible.builtin.template` module to deploy configuration files, ensuring they are only updated if the content has changed, as seen in `roles/rke2-prepare/tasks/main.yaml`.
* Use the `ansible.builtin.systemd` module to manage services, ensuring they are only restarted or enabled if their state has changed, as shown in `roles/rke2/tasks/main.yaml`.
* Use the `ansible.builtin.replace` module to update specific lines in configuration files, ensuring they are only modified if the content has changed, as demonstrated in `roles/rke2-prepare/tasks/main.yaml`.

### Organizing Ansible Roles

Here are some best practices for organizing Ansible roles:

* Use a consistent directory structure for roles, including `tasks`, `handlers`, `templates`, `files`, `vars`, and `defaults` directories. For example, the role `roles/admin` follows this structure.
* Group related tasks into separate roles to improve modularity and reusability. For instance, the repository has roles like `roles/common` for common tasks, `roles/kubernetes` for Kubernetes resources, and `roles/monitoring` for monitoring setup.
* Use descriptive names for roles and tasks to make it clear what each role and task does. For example, `roles/install-rancher` clearly indicates that it installs Rancher.
* Use variables to make roles configurable and reusable. Store variables in `vars` or `defaults` directories within the role or in group variables files like `inventory/group_vars/all.yaml`.
* Use templates for configuration files to allow customization based on variables. For example, `roles/kube-vip/templates/kube-vip-config.j2` is a template for Kube VIP configuration.
* Use handlers to manage service restarts and other actions that should only occur when certain tasks change. For example, `roles/add-agent/handlers/main.yaml` contains handlers for the `add-agent` role.
* Ensure idempotency by using appropriate Ansible modules and attributes like `creates`, `changed_when`, and `when`. For example, `roles/admin/tasks/main.yaml` uses the `creates` attribute to prevent re-execution of tasks.
* Use tags to allow selective execution of tasks or roles. For example, `roles/prepare-nodes/tasks/main.yaml` uses the `sysctl` tag for tasks related to sysctl configuration.
* Document roles and tasks with comments to improve readability and maintainability. For example, `roles/components/tasks/main.yaml` includes comments to describe each section of tasks.
* Organize roles logically within the playbooks. For example, `site.yaml` defines the sequence of roles to set up the RKE2 cluster.

### Managing Helm Charts

Here are some best practices for managing Helm charts:

* Use a consistent directory structure for Helm charts, including `charts`, `templates`, `values.yaml`, and `Chart.yaml` files. For example, the repository uses templates for Helm values in `roles/components/templates/`.
* Store Helm chart values in separate files to allow customization and reuse. For instance, the repository uses files like `roles/components/templates/cert-manager-values.yaml.j2` and `roles/components/templates/longhorn-values.yaml.j2`.
* Use descriptive names for Helm releases and namespaces to make it clear what each release and namespace is for. For example, the repository uses names like `cert-manager` and `longhorn-system` in `roles/components/tasks/main.yaml`.
* Use variables to make Helm charts configurable and reusable. Store variables in `values.yaml` files or in Ansible variables files like `inventory/group_vars/all.yaml`.
* Use the `kubernetes.core.helm` module to manage Helm releases in Ansible playbooks. For example, the repository uses this module in `roles/components/tasks/main.yaml` and `roles/monitoring/tasks/main.yaml`.
* Ensure idempotency by using appropriate Ansible modules and attributes like `creates`, `changed_when`, and `when`. For example, `roles/admin/tasks/main.yaml` uses the `creates` attribute to prevent re-execution of tasks.
* Use templates for Helm values files to allow customization based on variables. For example, the repository uses templates like `roles/components/templates/argocd-values.yaml.j2` and `roles/components/templates/istio-values.yaml.j2`.
* Document Helm charts and values files with comments to improve readability and maintainability. For example, `roles/components/templates/cert-manager-values.yaml.j2` includes comments to describe each section of values.
* Regularly update Helm repositories and charts to ensure the latest features and security patches are applied. For example, the repository adds Helm repositories in `roles/components/tasks/main.yaml` and `roles/monitoring/tasks/main.yaml`.

### Testing Ansible Roles

To ensure the Ansible playbooks and roles work as expected, the following tests should be added:

* Verify syntax and linting of all Ansible playbooks and roles using tools like `ansible-lint`.
* Test the installation of required packages on all nodes, as defined in `roles/common/tasks/main.yaml` and `roles/admin/tasks/main.yaml`.
* Validate the configuration of kernel modules and sysctl parameters in `roles/common/tasks/main.yaml`.
* Check the successful installation and configuration of RKE2 on servers and agents, as specified in `roles/rke2-prepare/tasks/main.yaml` and `roles/rke2/tasks/main.yaml`.
* Ensure the correct deployment of Kube VIP configuration in `roles/kube-vip/tasks/main.yaml`.
* Verify the installation and configuration of Helm repositories and charts in `roles/components/tasks/main.yaml`.
* Test the deployment of Kubernetes resources and configurations, including network policies and security configurations, as defined in `roles/kubernetes/tasks/main.yaml` and `roles/security/tasks/main.yaml`.
* Validate the setup and configuration of monitoring tools like Prometheus and Grafana in `roles/monitoring/tasks/main.yaml`.
* Check the preparation of the admin node, including SSH configuration and key distribution, as specified in `roles/prepare-admin/tasks/main.yaml`.
* Ensure the correct configuration of storage nodes and the installation of storage prerequisites in `roles/storage/tasks/main.yaml`.
* Test the setup and configuration of worker nodes, as defined in `roles/worker/tasks/main.yaml`.
* Verify the successful execution of the main playbook `site.yaml` to ensure the entire cluster setup process works as expected.

### Using Molecule for Testing Ansible Roles

To learn how to use Molecule for testing Ansible roles, consider the following steps:

* Install Molecule and its dependencies by running `pip install molecule[docker]` in your development environment.
* Create a `molecule` directory within each role you want to test. For example, create `roles/admin/molecule`.
* Inside the `molecule` directory, create a `default` scenario directory. For example, create `roles/admin/molecule/default`.
* In the `default` scenario directory, create a `molecule.yaml` file to define the testing configuration. For example, create `roles/admin/molecule/default/molecule.yaml`.
* In the `default` scenario directory, create a `playbook.yaml` file to define the playbook for testing the role. For example, create `roles/admin/molecule/default/playbook.yaml`.
* In the `default` scenario directory, create a `verify.yaml` file to define the verification steps for the role. For example, create `roles/admin/molecule/default/verify.yaml`.
* Run `molecule test` in the role directory to execute the tests and verify the role's functionality.

### Using Testinfra for Testing Ansible Roles

To learn how to use Testinfra for testing Ansible roles, consider the following steps:

* Install Testinfra and its dependencies by running `pip install testinfra` in your development environment.
* Create a `tests` directory within each role you want to test. For example, create `roles/admin/tests`.
* Inside the `tests` directory, create a `test_default.py` file to define the tests for the role. For example, create `roles/admin/tests/test_default.py`.
* In the `test_default.py` file, write test cases to verify the functionality of the role. For example, you can test if required packages are installed, if files are created, and if services are running.
* Run the tests using the `pytest` command in the role directory to execute the tests and verify the role's functionality.

### Using Jenkins for CI/CD

To learn how to use Jenkins for CI/CD, consider the following steps:

* Install Jenkins on a server or use a Jenkins service provider.
* Configure Jenkins by setting up the necessary plugins, such as the Ansible plugin and the Git plugin.
* Create a new Jenkins job or pipeline for the project.
* Configure the job to pull the repository from the version control system (e.g., GitHub).
* Set up build triggers to automatically run the job on code changes or at scheduled intervals.
* Add build steps to execute the Ansible playbooks, such as running `ansible-playbook site.yaml` to set up the Kubernetes cluster.
* Use Jenkins environment variables to pass sensitive data, such as Ansible Vault passwords, to the playbooks.
* Configure post-build actions to notify stakeholders of the build status, such as sending emails or integrating with communication platforms like Slack.

### Optimizing the Repository Structure

To optimize the repository structure, consider the following suggestions:

* Add a `.gitignore` file to exclude unnecessary files from being tracked by Git.
* Add a `CONTRIBUTING.md` file to provide guidelines for contributing to the project.
* Add a `LICENSE` file to clearly state the licensing terms of the project.
* Add a `CHANGELOG.md` file to document changes and updates to the project.
* Add comments and documentation to the Ansible playbooks and roles to improve readability and maintainability.
* Ensure that sensitive data, such as passwords and tokens, are encrypted using Ansible Vault.
* Implement role-based access control using Ansible Tower or AWX to manage and execute playbooks securely.
* Regularly update dependencies and packages to ensure the latest security patches are applied.
* Optimize the structure of the repository by organizing files and directories logically.
* Add tests for the Ansible playbooks and roles to ensure they work as expected.

### Enhancing Security and Compliance

To enhance security and compliance, consider the following suggestions:

* Add a role for auditing and compliance checks to ensure the cluster meets security and compliance standards.
* Add a role for automated security scanning of container images using tools like Trivy or Clair.
* Add a task to regularly update and patch the Kubernetes cluster and its components to ensure the latest security patches are applied.
* Ensure that sensitive data, such as passwords and tokens, are encrypted using Ansible Vault.
* Implement role-based access control using Ansible Tower or AWX to manage and execute playbooks securely.

### Improving Monitoring and Alerting

To improve monitoring and alerting, consider the following suggestions:

* Add a role for setting up alerting mechanisms using tools like Alertmanager and integrating with communication platforms like Slack or email.
* Add a role for setting up logging and log aggregation using tools like ELK stack (Elasticsearch, Logstash, Kibana) or Fluentd.
* Add a task to configure and deploy custom Grafana dashboards for better visualization of cluster metrics.
* Ensure that the CI/CD pipeline includes steps to monitor the health and performance of the Kubernetes cluster and its components.

### Enhancing Automation and CI/CD

To enhance automation and CI/CD, consider the following suggestions:

* Add a role for setting up a CI/CD pipeline using tools like Jenkins, GitLab CI, or GitHub Actions to automate the deployment and management of the Kubernetes cluster.
* Add a role for integrating with GitOps tools like Flux or ArgoCD to enable continuous deployment and management of Kubernetes resources.
* Add a task to automate the backup and restore process of the Kubernetes cluster and its components using tools like Velero.
* Add automated tests for the Ansible playbooks and roles to ensure they work as expected. This can be done using tools like Molecule and Testinfra.
* Set up a CI/CD pipeline using tools like Jenkins, GitLab CI, or GitHub Actions to run the tests automatically on every commit or pull request.
* Integrate linting tools like `ansible-lint` to check for syntax errors and best practices in the Ansible playbooks and roles.
* Ensure that the CI/CD pipeline includes steps to verify the successful creation of backups and the ability to restore them.

### Optimizing the Performance of the Kubernetes Cluster

To optimize the performance of the Kubernetes cluster, consider the following suggestions:

* Ensure that resource requests and limits are set for all pods to prevent resource contention and overcommitment. This can be done by defining resource requests and limits in the Kubernetes manifests.
* Use node selectors, taints, and tolerations to control pod placement and ensure that critical workloads are scheduled on appropriate nodes.
* Implement horizontal pod autoscaling to automatically adjust the number of pod replicas based on CPU or memory usage.
* Use vertical pod autoscaling to automatically adjust the resource requests and limits of pods based on their actual usage.
* Use a high-performance CNI (Container Network Interface) plugin, such as Calico or Cilium, to improve network performance and security.
* Enable and configure network policies to control traffic flow between pods and reduce unnecessary network traffic.
* Optimize the configuration of the load balancer, such as Kube-VIP and MetalLB, to ensure efficient load distribution and minimize latency.
* Use a high-performance storage solution, such as Longhorn, and ensure that it is properly configured with the appropriate replica count and storage class settings.
* Enable and configure storage policies to ensure that storage resources are allocated efficiently and meet the performance requirements of the workloads.
* Regularly monitor and optimize the performance of the storage solution to ensure that it meets the needs of the Kubernetes cluster.

### Ensuring the Scalability of the Kubernetes Cluster

To ensure the scalability of the Kubernetes cluster, consider the following suggestions:

* Ensure that resource requests and limits are set for all pods to prevent resource contention and overcommitment. This can be done by defining resource requests and limits in the Kubernetes manifests.
* Use node selectors, taints, and tolerations to control pod placement and ensure that critical workloads are scheduled on appropriate nodes.
* Implement horizontal pod autoscaling to automatically adjust the number of pod replicas based on CPU or memory usage.
* Use vertical pod autoscaling to automatically adjust the resource requests and limits of pods based on their actual usage.
* Use a high-performance CNI (Container Network Interface) plugin, such as Calico or Cilium, to improve network performance and security.
* Enable and configure network policies to control traffic flow between pods and reduce unnecessary network traffic.
* Optimize the configuration of the load balancer, such as Kube-VIP and MetalLB, to ensure efficient load distribution and minimize latency.
* Use a high-performance storage solution, such as Longhorn, and ensure that it is properly configured with the appropriate replica count and storage class settings.
* Enable and configure storage policies to ensure that storage resources are allocated efficiently and meet the performance requirements of the workloads.
* Regularly monitor and optimize the performance of the storage solution to ensure that it meets the needs of the Kubernetes cluster.
