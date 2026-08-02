# Liberu Control Panel\n\n## Product Scope\n\n**Purpose:** Secure management of hosting, servers, containers, Kubernetes, DNS, mail, databases, backups, and customer/reseller services.\n**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); management APIs, agents, automation, and provider connectors follow [API.md](../../architecture/API.md); operational and customer interfaces follow [THEMES.md](../../standards/THEMES.md).\n\n**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines infrastructure behavior only.\n\n## Outcomes\n\n- Provision and operate infrastructure consistently across supported operating systems and providers.\n- Give administrators, resellers, and customers least-privilege self-service with complete auditability.\n- Detect configuration drift and recover safely from failed, interrupted, or destructive operations.\n\n## Module plan\n\n| Module | Responsibilities |\n|---|---|\n| Control Core | Nodes, capabilities, credentials, task engine, inventory, desired state, locks, and audit |\n| OS Adapters | Detection, packages, services, firewall, users, filesystems, repositories, and support matrix |\n| Accounts | Admin/reseller/customer hierarchy, packages, quotas, delegation, branding, and suspension |\n| Web Hosting | Domains, virtual hosts, PHP/runtime versions, web servers, SSL, logs, redirects, and applications |\n| Mail | Domains, mailboxes, aliases, routing, quotas, spam/virus controls, DKIM, and delivery diagnostics |\n| Databases | Engines, databases, users, privileges, backups, upgrades, health, and remote access |\n| DNS | Zones, records, templates, DNSSEC, validation, providers, and propagation checks |\n| Files | Home directories, permissions, SFTP, file operations, quotas, scanning, and retention |\n| Certificates | ACME accounts, issuance, deployment, renewal, revocation, and expiry monitoring |\n| Backups | Policies, snapshots, application-consistent backup, encryption, off-site storage, restore, and verification |\n| Security | Hardening, patching, MFA/RBAC, secrets, malware, intrusion controls, vulnerability and compliance status |\n| Monitoring | Metrics, logs, uptime, capacity, alerts, incidents, maintenance windows, and status |\n| Containers | Images, registries, workloads, networks, volumes, secrets, limits, and lifecycle |\n| Kubernetes | Clusters, nodes, namespaces, RBAC, workloads, ingress, Helm, storage, autoscaling, upgrades, and multi-cluster views |\n| API and Automation | Scoped API, webhooks, CLI, templates, schedules, orchestration, and billing/provisioning events |\n\n## Supported platforms\n\nMaintain a versioned support matrix for Ubuntu LTS, Debian Stable, RHEL, AlmaLinux, Rocky Linux, and CloudLinux. Each release states lifecycle status, architectures, package/service/firewall adapters, validated hosting stacks, upgrade paths, and known limitations. Container-optimized systems are supported only through declared Kubernetes/container capabilities.\n\n## Required workflows\n\n1. **Enroll node:** authenticate → detect OS/capabilities → assess prerequisites → install agent/config → baseline inventory and health.\n2. **Provision service:** validate plan/quota → calculate desired state → acquire locks → execute idempotent steps → verify → report external identifier.\n3. **Change or suspend:** preview impact/dependencies → authorize/approve → execute → verify → notify and reconcile Billing state.\n4. **Patch/upgrade:** assess → snapshot/backup → stage/canary → apply → health check → continue or roll back/escalate.\n5. **Restore:** select verified recovery point → authorize target/overwrite → restore in dependency order → validate application/data → record evidence.\n\n## Product requirements\n\n- Use an authenticated agent or constrained transport; never build commands from untrusted strings.\n- Express operations as resumable, idempotent tasks with step logs, timeouts, retries, locks, cancellation, and compensation.\n- Separate desired state, observed state, and last successful state; surface drift and reconciliation.\n- Enforce account/package quota at API, UI, task, and remote execution boundaries.\n- Require step-up authentication and approval for destructive bulk, cluster, backup deletion, firewall, credential, and root-level actions.\n- Support high availability, maintenance/drain workflows, capacity planning, and safe rolling changes.\n\n## Integrations\n\nBilling/provisioning, DNS, registries, ACME, object storage, cloud providers, monitoring, alerting, Git repositories/CI, identity, support, and security scanners use scoped replaceable drivers.\n\n## Quality and operations gates\n\n- Test every supported OS/stack in disposable environments, including fresh install, upgrade, rollback, drift, partial failure, and uninstall.\n- Run Kubernetes conformance and workload recovery tests for declared distributions/features.\n- Verify backup restoration, secret rotation, quota isolation, privilege boundaries, firewall safety, and concurrent task locks.\n- Provide break-glass access, tamper-evident audit, redacted logs, health checks, SLOs, alerts, and operator runbooks.\n\n## Delivery phases\n\n1. Core, secure agent, OS adapters, Accounts, task engine, API, inventory, and monitoring basics.\n2. Web, certificates, DNS, databases, mail, files, quotas, Billing integration, and customer portal.\n3. Backups/restores, security/hardening, HA, reseller functions, and provider reconciliation.\n4. Containers, Kubernetes, multi-cluster, autoscaling, advanced observability, and AI-assisted diagnosis with approval controls.\n\n## Definition of done\n\nDeclared platforms pass install/upgrade/recovery matrices; operations are least-privilege, idempotent, observable, and recoverable; backups restore; state reconciles with Billing; destructive actions are controlled. Each module maps to a GitHub epic.

## Product Scope

**Purpose:** Secure management of hosting, servers, containers, Kubernetes, DNS, mail, databases, backups, and customer/reseller services.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); management APIs, agents, automation, and provider connectors follow [API.md](../../architecture/API.md); operational and customer interfaces follow [THEMES.md](../../standards/THEMES.md).

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
