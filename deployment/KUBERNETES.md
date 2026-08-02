# Kubernetes

Deploy Laravel to Kubernetes when you need declarative reconciliation, rolling releases, multiple nodes, or horizontal scaling. This guide applies to both standard Kubernetes (`k8s`) and K3s; manifests should remain portable unless a platform-specific feature is intentional.

## Choose k8s or K3s

- **Standard Kubernetes (`k8s`):** use a managed or self-operated distribution when you need broad ecosystem compatibility, cloud integrations, or an existing cluster platform.
- **K3s:** use the lightweight Kubernetes distribution for small clusters, edge locations, or a simpler self-managed footprint. Validate storage, ingress, load balancing, backup, and high-availability behavior for the selected K3s topology.
- Both platforms still require Kubernetes RBAC, TLS, namespaces, resource limits, probes, secret handling, backups, upgrades, and monitoring.

For a single-node K3s evaluation cluster:

```bash
curl -sfL https://get.k3s.io | sh -
sudo k3s kubectl get nodes
```

Use the K3s installation and high-availability documentation for production topology. Do not expose the kubeconfig or node token.

## Workload layout

- Run web, queue worker, scheduler, and realtime processes as separate Deployments or Jobs using an immutable application image.
- Use a Service and Ingress/Gateway for web traffic and TLS; keep databases and caches private.
- Store configuration in ConfigMaps and confidential values in Secrets or an external secret manager.
- Use PersistentVolumes only for data that cannot use managed external storage; test backup and restore.
- Set requests and limits, PodDisruptionBudgets, rolling-update strategy, and graceful termination.
- Add startup, readiness, and liveness probes with endpoints appropriate to each process. Readiness must fail when the pod should stop receiving traffic.
- Use a dedicated namespace, least-privilege ServiceAccounts/RBAC, NetworkPolicies, and a restricted Pod security context.

## Release flow

```bash
kubectl apply --server-side -f namespace.yaml
kubectl apply --server-side -f config/ -f secrets/ -f workloads/ -f services/
kubectl rollout status deployment/app-web --namespace=liberu
kubectl get pods,services,ingress --namespace=liberu
```

Run migrations as an approved, observable release Job before switching traffic when the migration is backward-compatible. Do not run migrations in every pod or store secrets in a manifest committed to Git.

## Operations

- Monitor pod restarts, probe failures, queue depth, request latency, errors, storage, and node capacity.
- Use `kubectl diff` and reviewed manifests before changes; record image digests and manifest versions.
- Drain nodes safely before maintenance and verify disruption budgets.
- Back up application data and cluster state according to the chosen k8s/K3s distribution; perform restore drills.
- Upgrade the control plane, nodes, ingress, storage, and application independently with a rollback plan.

## Verification

Test rollout, rollback, failed probes, pod rescheduling, node drain, secret rotation, wrong-namespace access, network isolation, queue recovery, storage recovery, and database restore on both the declared k8s and K3s targets.

## CI and release deployment

Every push to `main` runs [CI](../CI.md) and may update a staging namespace or GitOps revision after checks pass. Production manifests or image digests must not be changed automatically from `main`. A protected `vX.Y.Z` tag or GitHub Release may reconcile production only after all required checks, the 100% release-scope coverage gate, image and manifest scans, rollout/smoke checks, and production environment approval pass. The release must reference the exact tested commit and artifact.

## References

- [CI and release policy](../CI.md)
- [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)
- [Kubernetes security](https://kubernetes.io/docs/concepts/security/)
- [Kubernetes probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
- [K3s quick start](https://docs.k3s.io/quick-start)
- [Deployment index](README.md)
