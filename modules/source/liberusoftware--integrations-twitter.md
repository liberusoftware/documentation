# liberusoftware/integrations-twitter: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Twitter / X integration service.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-twitter` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-twitter` |
| Providers | `[]` |
| Capabilities | `integrations.twitter` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Twitter\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsTwitterServiceProvider.php` | `public function register(): void` |
| `src/Services/TwitterService.php` | `public function __construct()`<br>`public function getTimeline(ConnectedAccount $account)`<br>`public function postTweet(ConnectedAccount $account, $message)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
