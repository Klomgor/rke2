# Changelog

## [Unreleased]

### Added
- Initial release with the following features and components:
  - Automated deployment of RKE2 Kubernetes cluster
  - Helm repository management and chart deployments
  - Kubernetes resource and configuration management
  - SSH configuration and key distribution
  - Common tasks for setting up nodes
  - Security enhancements and RBAC configurations
  - Monitoring stack with Prometheus and Grafana
  - Storage solution with Longhorn
  - Service mesh with Istio
  - Backup and restore with Velero
  - GitOps with ArgoCD
  - Secrets management with Vault

### Changed
- Merged `site.yaml` and `site.yml` into one `site.yaml` file, including all roles and tasks, maintaining the order, and removing duplicates.
- Renamed all `.yml` files to `.yaml` for consistency.

### Deprecated
- N/A

### Removed
- Deprecated roles or tasks

### Fixed
- N/A

### Security
- N/A
