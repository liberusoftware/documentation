# Jetstream

## Purpose

Liberu applications use Laravel Jetstream 5 with Laravel 13 and PHP 8.5 for authentication and account security. Jetstream is the application shell; domain modules consume its contracts and must not reimplement authentication, sessions, teams, or two-factor flows.

## Installation boundary

Install Jetstream only in a new Laravel application and choose the frontend stack once:

```bash
composer require laravel/jetstream
php artisan jetstream:install livewire --teams
# Or: php artisan jetstream:install inertia --teams
npm install
npm run build
php artisan migrate
```

Enable only the features the application needs in `config/jetstream.php`. Teams are the supported workspace model; see [TEAMS.md](TEAMS.md) and [POLICY.md](POLICY.md).

## Design rules

- Keep Jetstream actions in `app/Actions/Jetstream`; one action should represent one use case.
- Keep domain rules in modules and application services. Jetstream actions may orchestrate them but must not become a second domain layer.
- Use Laravel policies and gates for server-side authorization. UI visibility is never an authorization control.
- Resolve and validate the current team before querying team-owned data. A team switch changes context; it does not grant access.
- Require recent authentication for password, two-factor, token, ownership, billing, deletion, and other high-impact changes.
- Rotate sessions after authentication and privilege changes; support revocation and audit for security-sensitive events.
- Keep secrets out of source control, logs, URLs, browser storage, and exception messages.
- Follow PSR-12 formatting and PSR-4 autoloading. Prefer typed properties, return types, immutable value objects, constructor injection, and explicit service contracts compatible with PHP 8.5.

## API and tokens

When API access is enabled, use Laravel Sanctum through Jetstream. Every request must pass both token ability and application/team policy checks where both apply. Token abilities are not a replacement for team membership or resource authorization.

## Verification

Test registration, verification, password reset, two-factor enrollment/recovery, session revocation, account deletion, team switching, invitations, policy denial, API ability checks, and rate limits. Run the repository checks defined in [TESTING.md](TESTING.md).

## References

- [Jetstream introduction](https://jetstream.laravel.com/introduction.html)
- [Jetstream installation](https://jetstream.laravel.com/installation.html)
- [Jetstream teams](https://jetstream.laravel.com/features/teams.html)
- [Boilerplate foundation](BOILERPLATE.md)
- [Installation](INSTALL.md)
