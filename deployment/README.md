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

## Automated deployment policy

See [CI](../architecture/CI.md) for the workflow contract. Every push to `main` runs required checks and may publish an immutable staging artifact or deploy staging. Production is never deployed directly from `main`; it is deployed only from a protected version tag or GitHub Release after all checks, the 100% release-scope coverage gate, artifact scanning, smoke tests, and production environment approval pass.

## Control Panel provisioning

When Liberu Control Panel provisions the environment, use its documented desired-state and reconciliation workflows rather than ad-hoc remote commands. Relevant modules are:

- [Control Panel scope](../projects/control-panel/CONTROL-PANEL.md)
- [Web Hosting](../projects/control-panel/features/web-hosting.md) and [Web Hosting API](../projects/control-panel/api/web-hosting.md)
- [Containers](../projects/control-panel/features/containers.md) and [Containers API](../projects/control-panel/api/containers.md)
- [Kubernetes](../projects/control-panel/features/kubernetes.md) and [Kubernetes API](../projects/control-panel/api/kubernetes.md)
- [Certificates](../projects/control-panel/features/certificates.md) for TLS
- [Databases](../projects/control-panel/features/databases.md) and [Backups](../projects/control-panel/features/backups.md)
- [Control Panel API and Automation](../projects/control-panel/features/api-and-automation.md)
- [Billing provisioning](../projects/billing/features/provisioning.md) for service lifecycle integration

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
- [CI](../architecture/CI.md)
- [Installation](../architecture/INSTALL.md)
- [Security policy](../architecture/SECURITY.md)
