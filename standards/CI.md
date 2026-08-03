# Continuous integration and delivery

CI must enforce the shared quality baseline for every package and application. Personal and SME deployments may use a smaller execution topology, but they still need locked dependencies, formatting, static/architecture/security checks, migrations, tests, and a verified release path. Enterprise profiles add matrix, provenance, environment protection, DR, and compliance evidence; see [progressive delivery](ADOPTION.md).

This document defines the GitHub Actions workflow policy for Liberu repositories. It complements [Testing](TESTING.md), [Repository standards](../architecture/REPOSITORIES.md), [Security](../architecture/SECURITY.md), and [Deployment](../deployment/README.md).

## Release policy

Every pull request and every push to `main` runs the required validation suite. A successful `main` build may publish an immutable artifact and deploy a non-production environment. It must not deploy production automatically.

Production deployment is release-based. A protected version tag such as `v1.2.3`, or the corresponding GitHub Release, may deploy only after the tagged commit has passed all required checks, including the 100% coverage gate for the configured release scope, artifact and dependency security checks, deployment verification, and production environment approval. Tags must not be moved or force-updated.

## Workflow responsibilities

The exact workflow filenames may vary by application, but responsibilities remain consistent:

| Workflow             | Responsibility                                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `install.yml`        | Verify supported PHP and Node versions, lock files, package installation, and application bootstrap.                             |
| `tests.yml`          | Run formatting, static analysis, architecture checks, unit and feature tests, API/OpenAPI checks, security checks, and coverage. |
| `docker.yml`         | Build, scan, and publish immutable container artifacts where applicable.                                                         |
| `deploy-staging.yml` | Optionally deploy the successful `main` artifact to staging and run smoke checks.                                                |
| `release.yml`        | Validate a protected version tag or release, obtain production approval, deploy, and verify or roll back.                        |

Keep workflows small and composable. A reusable workflow should own repeated setup and gate logic; application repositories remain responsible for their deployment manifests and environment-specific commands.

## Required gates

The required checks must cover, as applicable:

- `composer validate`, locked dependency installation, formatting, static analysis, and architecture rules.
- Unit, feature, integration, API contract, and browser tests defined by [TESTING.md](TESTING.md).
- OpenAPI validation, generated-contract drift, and breaking-change checks.
- Frontend installation from the lock file, linting, type checking, tests, and production build.
- Dependency, secret, container, and supported security scans.
- Coverage reports with no unreviewed regression.

The production release gate requires 100% line coverage for owned executable code in the configured release scope, plus the required branch/path coverage for critical code where supported. Vendor code, generated artifacts, static assets, and explicitly documented configuration-only paths are outside that scope. A failed gate blocks the release. Any exception requires protected maintainer approval and a recorded architecture decision; it must never be hidden by changing the threshold in the workflow.

The release workflow must test the exact commit and artifact that it deploys. Do not rebuild from a different commit after approval.

## Triggers and environments

Use these triggers as the default:

- `pull_request` to `main`: required validation only; never expose production secrets to untrusted fork code.
- `push` to `main`: repeat required validation, publish an immutable non-production artifact, and optionally deploy staging.
- `push` for protected `v*.*.*` tags or a GitHub Release: run release gates and request production approval.
- `workflow_dispatch`: support controlled operations, but do not allow it to bypass required checks or environment protection.

Configure GitHub environments as follows:

- `staging` may deploy automatically after the successful `main` workflow.
- `production` is restricted to protected release tags, uses environment-scoped secrets, requires reviewers where appropriate, and has a concurrency group so releases cannot overlap.
- Deployment jobs should stop on failed health checks and retain the artifact digest, logs, migration result, and rollback information.

## Workflow security

Use least-privilege job permissions, normally starting with:

```yaml
permissions:
  contents: read
```

Grant `id-token: write` only to a job that needs trusted OIDC deployment. Pin third-party actions to full-length commit SHAs, use lock files, avoid shell interpolation of untrusted values, and keep secrets in protected environments rather than repository files. Never print credentials, tokens, connection strings, or decrypted settings in logs.

## Minimal trigger and release shape

```yaml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
    tags: ["v*.*.*"]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<full-length-commit-sha>
      - run: ./vendor/bin/pest --coverage

  production:
    if: startsWith(github.ref, 'refs/tags/v')
    needs: checks
    runs-on: ubuntu-latest
    environment: production
    concurrency:
      group: production
      cancel-in-progress: false
    steps:
      - run: ./scripts/deploy-production "${GITHUB_REF_NAME}"
```

The example is intentionally incomplete: each application must add its supported runtime matrix, complete checks, artifact provenance, migration strategy, smoke tests, and rollback procedure. Replace placeholder action references with pinned SHAs.

## Deployment hand-off

Each deployment guide documents the same policy for its target: `main` validates and may update staging; production is updated only by a successful protected release. See [Docker](../deployment/DOCKER.md), [Docker Compose](../deployment/DOCKER-COMPOSE.md), [Kubernetes](../deployment/KUBERNETES.md), [NGINX](../deployment/NGINX.md), [Apache](../deployment/APACHE.md), [Queues](../deployment/QUEUES.md), [Supervisor](../deployment/SUPERVISORD.md), [Reverb](../deployment/REVERB.md), [Horizon](../deployment/HORIZON.md), and [Telescope](../deployment/TELESCOPE.md).

## References

- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [Control deployments and environment protection](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
- [Secure use of GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use)
