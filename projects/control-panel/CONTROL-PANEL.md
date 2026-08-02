# Liberu Control Panel

## Product Scope

**Purpose:** Secure management of hosting, servers, containers, Kubernetes, DNS, mail, databases, backups, and customer/reseller services.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); management APIs, agents, automation, and provider connectors follow [API.md](../../architecture/API.md); operational and customer interfaces follow [THEMES.md](../../architecture/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines infrastructure behavior only.

## Outcomes

- Provision and operate infrastructure consistently across supported operating systems and providers.
- Give administrators, resellers, and customers least-privilege self-service with complete auditability.
- Detect configuration drift and recover safely from failed, interrupted, or destructive operations.

## Module plan

| Module | Responsibilities |
|---|---|
| Control Core | Nodes, capabilities, credentials, task engine, inventory, desired state, locks, and audit |
| OS Adapters | Detection, packages, services, firewall, users, filesystems, repositories, and support matrix |
| Accounts | Admin/reseller/customer hierarchy, packages, quotas, delegation, branding, and suspension |
| Web Hosting | Domains, virtual hosts, PHP/runtime versions, web servers, SSL, logs, redirects, and applications |
| Mail | Domains, mailboxes, aliases, routing, quotas, spam/virus controls, DKIM, and delivery diagnostics |
| Databases | Engines, databases, users, privileges, backups, upgrades, health, and remote access |
| DNS | Zones, records, templates, DNSSEC, validation, providers, and propagation checks |
| Files | Home directories, permissions, SFTP, file operations, quotas, scanning, and retention |
| Certificates | ACME accounts, issuance, deployment, renewal, revocation, and expiry monitoring |
| Backups | Policies, snapshots, application-consistent backup, encryption, off-site storage, restore, and verification |
| Security | Hardening, patching, MFA/RBAC, secrets, malware, intrusion controls, vulnerability and compliance status |
| Monitoring | Metrics, logs, uptime, capacity, alerts, incidents, maintenance windows, and status |
| Containers | Images, registries, workloads, networks, volumes, secrets, limits, and lifecycle |
| Kubernetes | Clusters, nodes, namespaces, RBAC, workloads, ingress, Helm, storage, autoscaling, upgrades, and multi-cluster views |
| API and Automation | Scoped API, webhooks, CLI, templates, schedules, orchestration, and billing/provisioning events |

## Supported platforms

Maintain a versioned support matrix for Ubuntu LTS, Debian Stable, RHEL, AlmaLinux, Rocky Linux, and CloudLinux. Each release states lifecycle status, architectures, package/service/firewall adapters, validated hosting stacks, upgrade paths, and known limitations. Container-optimized systems are supported only through declared Kubernetes/container capabilities.

## Required workflows

1. **Enroll node:** authenticate → detect OS/capabilities → assess prerequisites → install agent/config → baseline inventory and health.
2. **Provision service:** validate plan/quota → calculate desired state → acquire locks → execute idempotent steps → verify → report external identifier.
3. **Change or suspend:** preview impact/dependencies → authorize/approve → execute → verify → notify and reconcile Billing state.
4. **Patch/upgrade:** assess → snapshot/backup → stage/canary → apply → health check → continue or roll back/escalate.
5. **Restore:** select verified recovery point → authorize target/overwrite → restore in dependency order → validate application/data → record evidence.

## Product requirements

- Use an authenticated agent or constrained transport; never build commands from untrusted strings.
- Express operations as resumable, idempotent tasks with step logs, timeouts, retries, locks, cancellation, and compensation.
- Separate desired state, observed state, and last successful state; surface drift and reconciliation.
- Enforce account/package quota at API, UI, task, and remote execution boundaries.
- Require step-up authentication and approval for destructive bulk, cluster, backup deletion, firewall, credential, and root-level actions.
- Support high availability, maintenance/drain workflows, capacity planning, and safe rolling changes.

## Integrations

Billing/provisioning, DNS, registries, ACME, object storage, cloud providers, monitoring, alerting, Git repositories/CI, identity, support, and security scanners use scoped replaceable drivers.

## Quality and operations gates

- Test every supported OS/stack in disposable environments, including fresh install, upgrade, rollback, drift, partial failure, and uninstall.
- Run Kubernetes conformance and workload recovery tests for declared distributions/features.
- Verify backup restoration, secret rotation, quota isolation, privilege boundaries, firewall safety, and concurrent task locks.
- Provide break-glass access, tamper-evident audit, redacted logs, health checks, SLOs, alerts, and operator runbooks.

## Delivery phases

1. Core, secure agent, OS adapters, Accounts, task engine, API, inventory, and monitoring basics.
2. Web, certificates, DNS, databases, mail, files, quotas, Billing integration, and customer portal.
3. Backups/restores, security/hardening, HA, reseller functions, and provider reconciliation.
4. Containers, Kubernetes, multi-cluster, autoscaling, advanced observability, and AI-assisted diagnosis with approval controls.

## Definition of done

Declared platforms pass install/upgrade/recovery matrices; operations are least-privilege, idempotent, observable, and recoverable; backups restore; state reconciles with Billing; destructive actions are controlled. Each module maps to a GitHub epic.
