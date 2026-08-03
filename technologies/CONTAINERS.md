# Containers and local services technology reference

Containers are an optional delivery and development tool for consistent PHP, Node.js, database, queue, and browser-test environments. A small personal deployment may use native services; enterprise deployments should document image provenance, patching, secrets, backups, and resource limits.

## Practical baseline

- Pin image digests or controlled tags and rebuild for security updates.
- Run as a non-root user where supported, minimize packages, and do not bake secrets into images.
- Separate application, worker, scheduler, database, cache, and reverse-proxy responsibilities.
- Add health checks, graceful shutdown, persistent volumes, network boundaries, log limits, and backup/restore tests.
- Keep local compose configuration representative without treating it as production orchestration.

Official references: [Docker Get Started](https://docs.docker.com/get-started/), [Dockerfile reference](https://docs.docker.com/reference/dockerfile/), [Compose specification](https://compose-spec.io/), and [OCI image specification](https://github.com/opencontainers/image-spec). Related local guides: [installation](../INSTALL.md), [CI](../standards/CI.md), [security architecture](../architecture/SECURITY.md), and [Control Panel](../projects/control-panel/CONTROL-PANEL.md).
