# Socialstream

## Purpose

Socialstream provides OAuth login and account linking for Jetstream and Filament. Liberu applications must use the Laravel 13-compatible fork declared by `liberusoftware/genealogy-laravel`:

```json
"bursteri/socialstream": "^7.0"
```

Do not substitute the archived upstream package or change the namespace without an explicit compatibility decision. The package retains the `JoelButcher\Socialstream` namespace for compatibility.

## Installation

Install in a new application, then publish the package integration:

```bash
composer require bursteri/socialstream
php artisan socialstream:install
php artisan migrate
```

Configure enabled providers in `config/socialstream.php` and provider credentials in `config/services.php`. Store credentials only in environment or a secret manager. Use HTTPS callback URLs outside local development.

## Provider and account rules

- Enable only providers that have an owner, privacy review, callback registration, and documented recovery path.
- Treat provider profile data, email addresses, avatars, refresh tokens, and state parameters as untrusted or sensitive input.
- Validate OAuth `state`, callback errors, provider identity, verified-email policy, and account-linking authorization.
- Never silently merge accounts. Require an authenticated session and recent authentication before linking or unlinking a provider.
- Prevent account enumeration and define what happens when a provider returns no email or an email already belongs to an account.
- Encrypt or otherwise protect refresh tokens; never log access tokens, authorization codes, or complete provider payloads.
- Record provider, subject identifier, actor, result, and correlation ID in audit data without storing unnecessary profile data.

## UI and architecture

Socialstream may adapt Jetstream Livewire/Inertia or Filament forms, but it does not own users, teams, roles, permissions, or product-domain authorization. Keep provider-specific UI in the presentation layer and keep business decisions in actions/policies.

## Verification

Test successful and failed callbacks, replayed state, denied consent, missing email, duplicate identity, linking/unlinking, revoked credentials, provider outage, rate limits, session fixation, and team/resource authorization after login.

## References

- [Required fork on GitHub](https://github.com/bursteri/socialstream)
- [Package information](https://packagist.org/packages/bursteri/socialstream)
- [Socialstream documentation](https://docs.socialstream.dev/)
- [Laravel Socialite](https://github.com/laravel/socialite)
- [Jetstream](JETSTREAM.md)
