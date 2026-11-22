# Boilerplate: Integrations Google Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-google`](../../../modules/source/liberusoftware--integrations-google.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-google` (`module-integrations-google`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Google Ads, Google Calendar, Gmail, and YouTube integration services and controller adapter extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Google**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/Http/Controllers/GoogleCalendarController.php` | `public function redirectToGoogle(): Redirector|RedirectResponse`<br>`public function handleGoogleCallback(Request $request)` |
| `src/IntegrationsGoogleServiceProvider.php` | `public function register(): void` |
| `src/Services/GmailService.php` | `public function __construct()`<br>`public function getUnreadMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessage($messageId, ?OAuthConfiguration $config = null)`<br>`public function sendReply($messageId, $body, ?OAuthConfiguration $config = null)` |
| `src/Services/GoogleAdsService.php` | `public function __construct()`<br>`public function getCampaigns($accountId)`<br>`public function createCampaign($accountId, array $campaignData)`<br>`public function updateCampaign($accountId, $campaignId, array $campaignData)`<br>`public function deleteCampaign($accountId, $campaignId)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |
| `src/Services/GoogleCalendarService.php` | `public function __construct()`<br>`public function createEvent(Task $task): void`<br>`public function updateEvent(Task $task): void`<br>`public function deleteEvent(Task $task): void`<br>`public function fetchEvents(array $params = []): array`<br>`public function syncEvents(array $events): void` |
| `src/Services/YouTubeService.php` | `public function uploadVideo(ConnectedAccount $account, string $videoPath, string $title, string $description): array`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-google` via Composer and enable `integrations-google` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
