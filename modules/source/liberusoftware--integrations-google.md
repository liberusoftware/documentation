# liberusoftware/integrations-google: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Google Ads, Google Calendar, Gmail, and YouTube integration services.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-google` |
| Version | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-google` |
| Providers | `[]` |
| Capabilities | `integrations.google` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Google\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Http/Controllers/GoogleCalendarController.php` | `public function redirectToGoogle(): Redirector|RedirectResponse`<br>`public function handleGoogleCallback(Request $request)` |
| `src/IntegrationsGoogleServiceProvider.php` | `public function register(): void` |
| `src/Services/GmailService.php` | `public function __construct()`<br>`public function getUnreadMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessage($messageId, ?OAuthConfiguration $config = null)`<br>`public function sendReply($messageId, $body, ?OAuthConfiguration $config = null)` |
| `src/Services/GoogleAdsService.php` | `public function __construct()`<br>`public function getCampaigns($accountId)`<br>`public function createCampaign($accountId, array $campaignData)`<br>`public function updateCampaign($accountId, $campaignId, array $campaignData)`<br>`public function deleteCampaign($accountId, $campaignId)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |
| `src/Services/GoogleCalendarService.php` | `public function __construct()`<br>`public function createEvent(Task $task): void`<br>`public function updateEvent(Task $task): void`<br>`public function deleteEvent(Task $task): void`<br>`public function fetchEvents(array $params = []): array`<br>`public function syncEvents(array $events): void` |
| `src/Services/YouTubeService.php` | `public function uploadVideo(ConnectedAccount $account, string $videoPath, string $title, string $description): array`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
