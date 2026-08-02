# Docker

Use Docker to package the Laravel application as an immutable image. Keep the web process, queue worker, scheduler, and realtime process as separate services or commands using the same release image where practical.

## Build requirements

- Use a supported PHP 8.5 base image and pin the base image tag or digest through a reviewed update process.
- Use a multi-stage build: install Composer dependencies and compile frontend assets in builder stages; copy only production output into the runtime stage.
- Run `composer install --no-dev --prefer-dist --optimize-autoloader` from the committed lock file.
- Run `npm ci` and `npm run build` in the asset stage when the application has frontend assets.
- Add a `.dockerignore` that excludes `.git`, `.env*`, `node_modules`, `vendor`, test output, local databases, logs, and secrets.
- Run as a non-root user and make only required writable paths writable, normally `storage/` and `bootstrap/cache/`.
- Do not place credentials, `.env` files, private keys, or runtime-generated data in the image.

## Minimal build flow

```bash
docker build --pull --tag registry.example.test/liberu/app:COMMIT_SHA .
docker run --rm --read-only \
  --env-file .env.production \
  --tmpfs /tmp \
  --publish 8080:8080 \
  registry.example.test/liberu/app:COMMIT_SHA
```

Use a deployment-specific process command and port. Do not use `latest` for releases. Scan the image and dependencies before pushing it to a registry.

## Runtime rules

- Inject configuration and secrets at runtime through the deployment platform.
- Keep containers stateless; persist uploads and other durable data in managed storage.
- Send logs to standard output/error and include correlation IDs without secrets or personal data.
- Add a health endpoint that does not expose credentials or sensitive internals.
- Set CPU, memory, filesystem, and restart limits at the runtime platform.
- Run migrations as a controlled release step, never on every web-container start.
- Run queue workers with graceful shutdown and a documented retry/failure policy.

## Verification

Test a clean image build, container boot, health endpoint, read-only filesystem behavior, storage mounts, queue/scheduler commands, migrations, graceful termination, and vulnerability scan. Rebuild regularly to receive base-image security updates.

## CI and release deployment

Every push to `main` runs [CI](../architecture/CI.md) and may build, scan, and publish an immutable staging image. Do not deploy that push directly to production. A protected `vX.Y.Z` tag or GitHub Release can promote the exact tested image digest only after all required checks, the 100% release-scope coverage gate, image scanning, smoke tests, and production environment approval pass.

## References

- [CI and release policy](../architecture/CI.md)
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
- [Dockerfile overview](https://docs.docker.com/build/concepts/dockerfile/)
- [Deployment index](README.md)
