# Boilerplate: Integrations Meta Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-meta`](../../../modules/source/liberusoftware--integrations-meta.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-meta` (`module-integrations-meta`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Facebook, Facebook Ads, Facebook Messenger, Instagram, and WhatsApp Business integration services, model, and Filament resource extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Meta**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/Filament/App/Resources/WhatsAppNumberResource.php` | `public function permissionResource(): string`<br>`public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getRelations(): array`<br>`public function getPages(): array` |
| `src/IntegrationsMetaServiceProvider.php` | `public function register(): void` |
| `src/Services/FacebookAdsService.php` | `public function __construct(protected AdvertisingAccount $account)`<br>`public function getCampaigns()`<br>`public function createAndSchedulePost($pageId, array $postData)` |
| `src/Services/FacebookMessengerService.php` | `public function __construct()`<br>`public function getUnreadMessages(?ConnectedAccount $account = null): array`<br>`public function getMessage(string $messageId, ?ConnectedAccount $account = null): array`<br>`public function sendReply(string $recipientId, string $message, ?ConnectedAccount $account = null)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount(): ?ConnectedAccount` |
| `src/Services/FacebookService.php` | `public function __construct()`<br>`public function publishPost($content)`<br>`public function getPostInsights($postId)` |
| `src/Services/InstagramService.php` | `public function getRecentMedia(ConnectedAccount $account)`<br>`public function postMedia(ConnectedAccount $account, $imageUrl, $caption)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |
| `src/Services/WhatsAppBusinessService.php` | `public function __construct()`<br>`public function getUnreadMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessage(string $messageId, ?OAuthConfiguration $config = null)`<br>`public function sendReply($to, $body, ?OAuthConfiguration $config = null)`<br>`public function sendMessage($to, $body, ?OAuthConfiguration $config = null)` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-meta` via Composer and enable `integrations-meta` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
