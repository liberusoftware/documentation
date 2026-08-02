# Docker Compose

Use Docker Compose when the application stack runs on one host, in development, staging, CI, or a small controlled production environment. Compose is not a replacement for a multi-node orchestrator.

## Services

Define separate services for the web process, queue worker, scheduler, and any realtime process. Add database, cache, mail, and storage services only when the environment owns them; managed services are preferred for production data.

Use the Compose Specification and keep configuration in version control:

```bash
docker compose config
docker compose -f compose.yaml -f compose.production.yaml up -d
docker compose ps
docker compose logs --tail=100 web worker scheduler
```

## Production rules

- Keep application code inside the image; do not bind-mount the source tree in production.
- Pin image versions or digests and rebuild from the reviewed commit.
- Put production differences in `compose.production.yaml` instead of duplicating the base file.
- Pass secrets through a secret manager or protected environment mechanism, never committed YAML.
- Define health checks, restart policies, resource limits, explicit networks, and named volumes for durable data.
- Publish only the required web/TLS port. Do not publish database, cache, or internal worker ports.
- Use an external reverse proxy or TLS terminator and restrict its network access.
- Back up named volumes and managed services; test restoration independently.

## Release flow

```bash
docker compose -f compose.yaml -f compose.production.yaml pull
docker compose -f compose.yaml -f compose.production.yaml run --rm app php artisan migrate --force
docker compose -f compose.yaml -f compose.production.yaml up -d --remove-orphans
docker compose -f compose.yaml -f compose.production.yaml ps
```

Build and recreate the affected service after an application change. Verify health, queues, scheduler, storage, mail, and logs before declaring the release complete.

## Recovery

Keep the previous image tag available, record the deployed Compose files and environment version, and roll back the application image when safe. Treat irreversible database migrations as a separate compatibility decision with a tested recovery plan.

## CI and release deployment

Every push to `main` runs [CI](../standards/CI.md) and may update a staging Compose deployment with a pinned image digest. Production must not follow `main` automatically. A protected `vX.Y.Z` tag or GitHub Release promotes the exact tested digest only after the required checks, 100% release-scope coverage gate, scans, smoke tests, and production environment approval pass.

## References

- [CI and release policy](../standards/CI.md)
- [Docker Compose](https://docs.docker.com/compose/)
- [Compose in production](https://docs.docker.com/compose/how-tos/production/)
- [Deployment index](README.md)
