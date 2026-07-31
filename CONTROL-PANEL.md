# Control Panel System Development Scope (Updated OS Support)
## Enterprise Open-Source Hosting, Infrastructure, Kubernetes & DevOps Control Panel

---

# 1. Vision & Positioning

This control panel combines three lineages into one platform:

- **Traditional hosting panels (cPanel / DirectAdmin / Plesk)** — account hierarchy, per-domain provisioning, email, DNS, databases, billing hooks.
- **Kubernetes-native hosting panels (KubePanel-style)** — container isolation per site, self-healing high availability, auto-scaling, flat/no per-account pricing model.
- **Kubernetes cluster dashboards (Kubernetes Dashboard, Headlamp, Devtron, Lens)** — cluster observability, workload management, RBAC exploration, Helm management, live logs/exec.

The panel must work equally well as: (a) a classic single-server LAMP-style hosting panel, (b) a multi-node Kubernetes-orchestrated hosting platform, and (c) a general-purpose Kubernetes cluster management UI — selectable per deployment.

---

# 2. Operating System Support Matrix

## Fully Supported Operating Systems

### Ubuntu LTS
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Ubuntu 26.04 LTS (forward compatibility target)

### Debian Stable
- Debian 11 (Bullseye)
- Debian 12 (Bookworm)
- Debian Stable future releases (forward-compatible design required)

### RedHat Enterprise Linux (RHEL)
- RHEL 8 / 9 / 10

### AlmaLinux
- AlmaLinux 8 / 9 / 10

### Rocky Linux
- Rocky Linux 8 / 9 / 10

### CloudLinux
- CloudLinux 8 / 9 / 10

## Container-Optimized / Kubernetes Host OS Support

- Ubuntu (kubeadm, k3s, MicroK8s)
- Flatcar Container Linux
- Talos Linux (for immutable, API-managed Kubernetes nodes)
- Bottlerocket (AWS-optimized container OS, optional)

---

# 3. OS Abstraction Layer Requirements

## Core Design Principles
- OS-agnostic application layer
- OS-aware provisioning layer
- Version-aware compatibility mapping
- Safe fallback execution strategies

## Unified System Interfaces

### Package Management Abstraction
- Debian-based systems: `apt`
- RHEL-based systems: `dnf` / `yum`

Unified API for: install, remove, update, repository management.

### Service Management
- Standardised use of `systemd`
- Unified lifecycle API: start, stop, restart, reload, enable, disable

### Firewall Abstraction
- Ubuntu / Debian: `ufw`
- RHEL family: `firewalld`
- Optional: CSF (CloudLinux), nftables abstraction layer, Kubernetes NetworkPolicy layer for containerized workloads

### Filesystem & Config Layer
- OS-specific configuration mapping layer
- Standardised service config registry
- Predictable path resolution abstraction

### OS Detection Engine
- Automatically detect OS and version
- Apply correct provisioning strategy
- Map compatible features dynamically
- Prevent unsupported configuration execution
- Detect whether host is bare-metal/VM (classic mode) or a Kubernetes node (orchestrated mode) and switch provisioning backend accordingly

---

# 4. Kubernetes & Container Orchestration Layer

A first-class deployment mode where every hosting account/domain runs as an isolated, orchestrated workload rather than a shared-OS process.

## 4.1 Cluster Distribution Support
- k3s (lightweight, default for small/edge deployments)
- MicroK8s (single-command bootstrap, snap-based)
- RKE2 (Rancher, hardened/enterprise)
- Full upstream Kubernetes (kubeadm)
- Managed cloud Kubernetes (EKS, GKE, AKS) as an optional backend
- Single-node "all-in-one" mode for small hosting boxes, with a path to multi-node scale-out without re-provisioning

## 4.2 Multi-Node Cluster Management
- Cluster bootstrap and node join/drain/cordon from the UI
- Node pool management (roles, taints, labels)
- Node health, capacity, and utilization overview (CPU, RAM, disk, network)
- Rolling node upgrades

## 4.3 Self-Healing & High Availability
- Automatic pod/container rescheduling on node failure
- Zero single-point-of-failure architecture across control plane and workloads
- Liveness/readiness probes managed per account/site
- Automatic recovery from crash-loop and OOM conditions with alerting

## 4.4 Per-Account Container Isolation
- Every domain/site/tenant runs in its own namespace and container(s)
- Dedicated CPU/RAM/storage resource requests & limits per tenant (ResourceQuota / LimitRange)
- Network isolation between tenants (NetworkPolicy per namespace)
- Prevents one compromised or runaway site from affecting others (equivalent goal to CloudLinux CageFS/LVE, achieved via Kubernetes primitives)

## 4.5 Auto-Scaling & Deployment
- Horizontal Pod Autoscaling based on CPU/RAM/custom metrics
- Vertical scaling recommendations
- Rolling, blue-green, and canary deployment strategies for site/app updates
- Scale-to-zero for idle low-traffic sites (cost optimization)

## 4.6 Workload & Resource Management (Dashboard-style)
- Visual management of Deployments, StatefulSets, DaemonSets, Jobs, CronJobs
- Pod/container list with live status, restarts, and resource consumption
- Live log streaming and log search per pod/container
- In-browser shell/exec into containers (audited)
- YAML editor with schema validation for direct manifest editing
- Manifest import from Git repositories (GitOps-style deploys)
- Events timeline per resource for troubleshooting

## 4.7 Networking & Ingress
- Ingress controller management (NGINX Ingress, Traefik)
- Automatic virtual host / Ingress rule creation per domain
- Service and Endpoint visibility
- Network Policy editor (visual + YAML)
- Load balancer / MetalLB integration for bare-metal clusters

## 4.8 Helm & Application Packaging
- Helm chart repository browser and one-click install/upgrade/rollback
- Curated hosting app catalog (WordPress, Ghost, Django, Node.js, static sites) as Helm charts or Operators
- Custom Docker image deployment per site
- Support for multiple runtime versions side-by-side (e.g., PHP 8.0 next to PHP 8.3, Python next to Node.js) with no host-level conflicts

## 4.9 Storage
- Persistent Volume / Storage Class management
- Per-domain LVM/CSI snapshot support for instant backup and restore
- Backup restore of a single tenant without affecting others

## 4.10 Security & RBAC (cluster-level)
- Kubernetes RBAC viewer and editor, with reverse lookup ("what can this user/service account do?")
- Pod Security Standards / policy audit
- Certificate tracker for cluster and ingress TLS certs (cert-manager integration, Let's Encrypt automation)
- Container image registry manager and vulnerability scanning hooks
- Audit logging of all cluster-admin actions taken through the panel

## 4.11 Multi-Cluster Support
- Manage multiple clusters (on-prem, cloud, hybrid) from a single control plane
- Per-cluster credential isolation (no cross-cluster credential storage without explicit operator opt-in)
- Cluster selector / tab-based switching in the UI

## 4.12 AI-Assisted Operations (optional module)
- Natural-language cluster query assistant ("why is this pod crashing?")
- Automated root-cause suggestions from events/logs

---

# 5. Account & Reseller Hierarchy (cPanel / DirectAdmin-Style)

## 5.1 Multi-Tier Roles
- **Root/Server Admin** — full server and cluster control, plugin management, global settings
- **Reseller** — manages a pool of end-user accounts within assigned resource limits, white-label branding
- **Account Owner (User)** — manages their own domains, email, databases, files
- **Sub-user / Team member** — scoped permissions within a single account (e.g., developer with SSH-only access)

## 5.2 Package & Plan Management
- Hosting package templates (disk, bandwidth, CPU/RAM quota, number of domains/databases/mailboxes)
- Per-package feature toggles (SSH access, cron jobs, Node.js apps, backups)
- Assign/change/upgrade/downgrade packages per account
- Reseller-defined custom packages within their allotted resources

## 5.3 Branding & White-Labeling
- Custom logo, color scheme, and domain for reseller-facing panel instances
- Custom nameserver branding (vanity nameservers)

## 5.4 Provisioning Automation
- Instant account creation with automatic: container/namespace (or system user), database, SFTP/SSH access, SSL certificate, DNS zone
- Bulk account import/export
- Migration tools: import from cPanel, DirectAdmin, Plesk, and CloudLinux accounts

---

# 6. Web Hosting Features (Per-Domain)

- Primary domains, subdomains, addon domains, parked/alias domains
- Multi-PHP support (side-by-side versions, per-domain selection) plus Python, Node.js, Ruby/Rails runtimes
- One-click application installer (WordPress, Ghost, Django, static sites, custom images) — Softaculous-equivalent catalog
- Git-based deployment (push-to-deploy, deploy keys, webhook triggers)
- File Manager (browser-based, with archive extraction, permissions editor, code editor)
- FTP/SFTP account management, scoped to a directory
- SSH access management, including per-account key management
- Cron job scheduler (UI-based, with logging)
- Redirect manager (301/302, per-path rules)
- Custom error pages, .htaccess/NGINX config equivalents through the abstraction layer
- Hotlink protection and directory-level password protection (leech protection)
- Staging environments / one-click clone to staging

---

# 7. Email Hosting

- Mailbox creation, quotas, and per-domain mail plans
- Aliases, forwarders, autoresponders, mailing lists
- Webmail interface (Roundcube/Rainloop-equivalent)
- IMAP/POP3/SMTP with modern auth (OAuth2 optional)
- Anti-spam and anti-virus (Rspamd/SpamAssassin) with per-mailbox spam scoring
- DKIM, SPF, and DMARC automatic configuration and monitoring
- Mail queue management and delivery/bounce log viewer
- Outbound rate limiting to protect IP/domain reputation

---

# 8. Database Management

- MariaDB/MySQL and PostgreSQL provisioning per account
- Redis provisioning for caching/session storage
- Web-based query/admin tool (phpMyAdmin/Adminer-equivalent)
- Per-database user management with granular privilege control
- Remote access control (allow-listed hosts/IPs)
- Automated and on-demand database backups, point-in-time restore where supported
- Database resource quotas tied to account package

---

# 9. DNS Management

- Built-in authoritative DNS (BIND9 or PowerDNS backend)
- Visual DNS zone editor (A, AAAA, CNAME, MX, TXT, SRV, CAA, etc.)
- DNS clustering/replication across multiple nameservers
- DNSSEC support
- DNS templates applied automatically on account/domain creation
- API-driven DNS record management for automation/CI pipelines

---

# 10. Backup, Restore & Disaster Recovery

- Per-account/per-domain instant backup and restore (independent of other tenants)
- Full-account backup (files + databases + email + config) in a portable, downloadable archive
- Incremental and scheduled backups
- Offsite/remote backup targets (S3-compatible storage, SFTP, other nodes)
- Snapshot-based restore for Kubernetes-orchestrated tenants (CSI/LVM snapshots) completing in under a minute
- Disaster recovery runbook: cluster/node loss recovery, automatic workload rescheduling validation
- One-click migration import from cPanel, DirectAdmin, Plesk backup formats

---

# 11. Security

- Fail2ban (all OS) and equivalent brute-force protection for orchestrated workloads
- Web Application Firewall (ModSecurity or equivalent WAF, plus Kubernetes-native ingress WAF rules)
- SELinux compatibility layer (RHEL family) / AppArmor support (Ubuntu/Debian)
- CSF firewall (CloudLinux optional integration)
- IP allow/block lists, geo-blocking
- Two-factor authentication for all panel roles
- Malware scanning for hosted files
- Account-level audit logging (who changed what, when) across both classic and Kubernetes modes
- Automatic SSL/TLS via Let's Encrypt (classic) and cert-manager (Kubernetes), including wildcard support
- Login/IP anomaly detection and alerting

## CloudLinux Enhancements (Classic Mode)
When CloudLinux is detected:
- LVE Manager integration
- CPU / RAM / IO resource limits per user
- CageFS isolation support
- Shared hosting hardening features
- Account-level resource enforcement

*(In Kubernetes mode, equivalent isolation is achieved via namespaces, ResourceQuotas, and NetworkPolicies — see Section 4.4.)*

---

# 12. Monitoring, Analytics & Alerting

- Real-time resource usage graphs (CPU, RAM, disk, bandwidth) per account and per node/cluster
- Traffic and visitor statistics (AWStats/Webalizer-equivalent) per domain
- Uptime monitoring with configurable alert channels (email, Slack, webhook)
- Centralized log aggregation across classic and containerized workloads
- Cluster health dashboard: node status, pod counts, restarts, pending/failed workloads
- Resource efficiency recommendations (over/under-provisioned tenants)
- Certificate expiry tracking and renewal alerts

---

# 13. Billing, API & Automation

- REST API covering account, domain, email, database, DNS, backup, and Kubernetes workload operations
- CLI tool mirroring the API for scripting and CI/CD integration
- Webhook events for provisioning/lifecycle actions
- Billing system integration hooks (WHMCS-equivalent) for automated account suspension/termination on non-payment
- Plugin/extension marketplace for third-party integrations
- Terraform provider (optional) for infrastructure-as-code management of accounts and clusters

---

# 14. Hosting Stack Compatibility Per OS

## Web Servers
- NGINX (all supported OS)
- Apache HTTP Server (all supported OS)
- LiteSpeed / OpenLiteSpeed (where supported)

## DNS Systems
- BIND9 (all OS)
- PowerDNS (recommended for enterprise and RHEL-based systems)

## Email Stack
- Postfix (all OS)
- Dovecot (all OS)
- Rspamd / SpamAssassin (all OS)

## Database Systems
- MariaDB / MySQL (all OS)
- PostgreSQL (all OS)
- Redis (all OS)

## Security Systems
- Fail2ban (all OS)
- SELinux compatibility layer (RHEL / AlmaLinux / Rocky / CloudLinux)
- AppArmor support (Ubuntu / Debian)
- CSF firewall (CloudLinux optional integration)

---

# 15. Enterprise Infrastructure Support Targets

The control panel must operate across:
- Shared hosting environments (classic mode)
- Dedicated server environments
- VPS infrastructure
- Hybrid cloud deployments
- Kubernetes clusters (k3s, MicroK8s, RKE2, kubeadm, managed cloud K8s)
- Docker-based infrastructure (standalone, non-orchestrated fallback)
- Enterprise bare-metal data centers
- Small hosting companies migrating off cPanel/Plesk (50–500 accounts) seeking flat pricing
- Web design studios needing multi-runtime hosting (WordPress, Python, Node.js) without juggling servers

---

# 16. Testing Requirements

## System-Level Validation Tests
- Installation tests across all supported OS versions
- Package manager compatibility verification
- Service lifecycle validation
- Network stack validation per OS

## Provisioning Tests
- Virtual host provisioning across OS types
- Email provisioning consistency tests
- DNS provisioning consistency tests
- Database provisioning validation across distributions
- Kubernetes namespace/workload provisioning consistency across k3s/MicroK8s/RKE2/kubeadm

## Security & Hardening Tests
- Firewall compatibility validation (ufw/firewalld)
- SELinux enforcement validation (RHEL family)
- AppArmor policy validation (Ubuntu/Debian)
- SSH hardening validation
- Privilege escalation prevention tests
- Kubernetes RBAC and NetworkPolicy enforcement tests
- Cross-tenant isolation tests (verify one compromised container/namespace cannot access another's data or resources)

## High Availability & Resilience Tests
- Node failure / automatic workload rescheduling validation (time-to-recovery benchmarks)
- Rolling upgrade validation with zero downtime
- Backup/restore time benchmarks per tenant (target: under 60 seconds for single-domain restore)
- Chaos-engineering style fault injection (kill nodes, kill pods, simulate network partition)

## Kubernetes Conformance
- CNCF Kubernetes conformance test suite pass on all supported distributions
- Helm chart install/upgrade/rollback validation for the curated app catalog

---

# 17. Strategic Compatibility Vision

The control panel is designed to be:
- Fully OS-agnostic at the application layer
- Dynamically adaptive at the provisioning layer (classic OS or Kubernetes-orchestrated)
- Enterprise-grade across all major Linux hosting distributions and Kubernetes distributions
- Competitive with cPanel, DirectAdmin, and Plesk on features, while matching or exceeding KubePanel-style platforms on resilience and cost model (no per-account licensing fees)

This ensures seamless deployment across:
- Modern cloud environments
- Traditional hosting providers
- Enterprise IT infrastructures
- Kubernetes-native systems
- Hybrid multi-OS, multi-cluster fleets

---

# 18. Long-Term Platform Guarantee

This system is designed with forward compatibility for:
- Ubuntu LTS future releases
- RHEL enterprise lifecycle updates
- AlmaLinux/Rocky Linux ecosystem continuity
- CloudLinux hosting ecosystem evolution
- Kubernetes upstream release cadence (N-2 supported versions minimum) across k3s, MicroK8s, RKE2, and kubeadm

ensuring long-term stability for enterprise-grade infrastructure deployments, whether run on a single classic Linux box or a multi-node, self-healing Kubernetes cluster.
