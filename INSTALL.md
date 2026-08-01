# Installation

## Supported baseline

The current Liberu Laravel baseline is PHP 8.5, Laravel 13, Filament 5, Livewire 4, and Composer 2. Use the application repository's lock file and CI matrix as the final compatibility authority.

Required services depend on the selected modules, but commonly include a supported database, cache/queue backend, mail transport, Node.js/npm for frontend assets, and a process supervisor for workers.

## Local installation

From the application repository:

```bash
git clone REPOSITORY_URL application
cd application
cp .env.example .env
composer install
php artisan key:generate
php artisan migrate
npm install
npm run build
php artisan test
```

Set database, cache, queue, mail, OAuth, and filesystem values in `.env` before using the application. Never commit `.env` or credentials. If the application uses Jetstream teams, install the feature during application scaffolding and follow [JETSTREAM.md](JETSTREAM.md) and [TEAMS.md](TEAMS.md).

## Dependency-specific setup

- Install [Jetstream](JETSTREAM.md) in a new application and choose Livewire or Inertia once.
- Install [Socialstream](SOCIALSTREAM.md) from `bursteri/socialstream`; configure OAuth credentials through a secret store.
- Configure [Spatie Permission and Filament Shield](POLICY.md) for application/panel permissions only.
- Follow [TESTING.md](TESTING.md) for formatting, static analysis, architecture, security, and test commands.

## Verification and failure recovery

Confirm migrations, queues, mail, storage, OAuth callbacks, health checks, and authorization in a disposable environment before production. If installation fails, preserve the error and environment versions, remove only the failed application's generated state, correct the dependency/configuration issue, and rerun from a clean working tree; do not delete shared or production data.

## Next steps

- [Deployment guide](deployment/README.md)
- [Repository standards](REPOSITORIES.md)
- [Contributing](CONTRIBUTING.md)
