# liberusoftware/integrations-linkedin: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

LinkedIn organic and LinkedIn Ads integration services.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-linkedin` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-linkedin` |
| Providers | `[]` |
| Capabilities | `integrations.linkedin` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\LinkedIn\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsLinkedinServiceProvider.php` | `public function register(): void` |
| `src/Services/LinkedInAdsService.php` | `public function __construct(protected AdvertisingAccount $account)`<br>`public function getCampaigns()`<br>`public function createAndSchedulePost($organizationId, array $postData)` |
| `src/Services/LinkedInService.php` | `public function getProfile(ConnectedAccount $account)`<br>`public function sharePost(ConnectedAccount $account, $content)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
