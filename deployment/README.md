# Deployment

This guide indexes the supported deployment shapes. The application repository's manifests, lock file, health checks, migration policy, and release notes remain authoritative for a specific application.

## Choose a target

| Target | Use when | Required operational controls |
|---|---|---|
| Standalone host | You need a conventional PHP deployment on a managed VM or bare-metal host | PHP-FPM/web server, queue and scheduler supervision, TLS, backups, health checks, and rollback |
| Docker Compose | You need reproducible application, worker, database, cache, and frontend services on one host or development environment | Pinned images, non-root containers, persistent volumes, secrets, health checks, resource limits, backups, and migration ordering |
| Kubernetes (k3s or k8s) | You need declarative reconciliation, rolling releases, horizontal scaling, or multi-node operation | Namespaces, RBAC, NetworkPolicies, Secrets, probes, resource requests/limits, persistent storage, ingress/TLS, PodDisruptionBudgets, observability, and restore-tested backups |

## Deployment guides

- [Docker](DOCKER.md) — build a small, reproducible, production-ready application image.
- [Docker Compose](DOCKER-COMPOSE.md) — run the application stack on one host or in CI.
- [Kubernetes](KUBERNETES.md) — deploy to either a standard Kubernetes cluster (`k8s`) or lightweight K3s cluster.
- [NGINX](NGINX.md) — serve Laravel through NGINX and PHP-FPM.
- [Apache](APACHE.md) — serve Laravel through Apache HTTP Server and PHP-FPM.
- [Queues](QUEUES.md) — design, operate, retry, and observe asynchronous jobs.
- [Supervisor](SUPERVISORD.md) — supervise workers, schedulers, Reverb, and SSR on standalone hosts.
- [Reverb](REVERB.md) — operate Laravel WebSockets behind a trusted TLS proxy.
- [Horizon](HORIZON.md) — manage Redis queue supervisors and metrics.
- [Telescope](TELESCOPE.md) — use application diagnostics safely with retention and access controls.

## Common release sequence

1. Build and scan an immutable artifact from the reviewed commit.
2. Back up and verify the database and uploaded media.
3. Apply compatible migrations through a controlled release job.
4. Deploy web, queue, scheduler, and realtime processes with health/readiness checks.
5. Confirm authorization, queues, scheduled tasks, storage, mail, OAuth callbacks, and application health.
6. Monitor errors and latency; roll back the application artifact or follow the migration rollback plan if verification fails.

Do not run destructive migrations, expose databases publicly, bake credentials into images, or use an unreviewed `latest` image tag.

## Control Panel provisioning

When Liberu Control Panel provisions the environment, use its documented desired-state and reconciliation workflows rather than ad-hoc remote commands. Relevant modules are:

- [Control Panel scope](../CONTROL-PANEL.md)
- [Web Hosting](../features/control-panel/web-hosting.md) and [Web Hosting API](../api/control-panel/web-hosting.md)
- [Containers](../features/control-panel/containers.md) and [Containers API](../api/control-panel/containers.md)
- [Kubernetes](../features/control-panel/kubernetes.md) and [Kubernetes API](../api/control-panel/kubernetes.md)
- [Certificates](../features/control-panel/certificates.md) for TLS
- [Databases](../features/control-panel/databases.md) and [Backups](../features/control-panel/backups.md)
- [Control Panel API and Automation](../features/control-panel/api-and-automation.md)
- [Billing provisioning](../features/billing/provisioning.md) for service lifecycle integration

Provisioning must be authenticated, least-privilege, idempotent, observable, and recoverable. Keep application secrets in the control plane's secret mechanism and inject them at runtime.

## References

- [Laravel deployment](https://laravel.com/docs/13.x/deployment)
- [Docker Compose](https://docs.docker.com/compose/)
- [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)
- [Docker](DOCKER.md)
- [Docker Compose](DOCKER-COMPOSE.md)
- [Kubernetes](KUBERNETES.md)
- [NGINX](NGINX.md)
- [Apache](APACHE.md)
- [Queues](QUEUES.md)
- [Supervisor](SUPERVISORD.md)
- [Reverb](REVERB.md)
- [Horizon](HORIZON.md)
- [Telescope](TELESCOPE.md)
- [Installation](../INSTALL.md)
- [Security policy](../SECURITY.md)
