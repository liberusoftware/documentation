# liberusoftware/integrations-meta: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Facebook, Facebook Ads, Facebook Messenger, Instagram, and WhatsApp Business integration services.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-meta` |
| Version | `1.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-meta` |
| Providers | `[]` |
| Capabilities | `integrations.meta` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Meta\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Filament/App/Resources/WhatsAppNumberResource.php` | `public function permissionResource(): string`<br>`public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getRelations(): array`<br>`public function getPages(): array` |
| `src/IntegrationsMetaServiceProvider.php` | `public function register(): void` |
| `src/Services/FacebookAdsService.php` | `public function __construct(protected AdvertisingAccount $account)`<br>`public function getCampaigns()`<br>`public function createAndSchedulePost($pageId, array $postData)` |
| `src/Services/FacebookMessengerService.php` | `public function __construct()`<br>`public function getUnreadMessages(?ConnectedAccount $account = null): array`<br>`public function getMessage(string $messageId, ?ConnectedAccount $account = null): array`<br>`public function sendReply(string $recipientId, string $message, ?ConnectedAccount $account = null)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount(): ?ConnectedAccount` |
| `src/Services/FacebookService.php` | `public function __construct()`<br>`public function publishPost($content)`<br>`public function getPostInsights($postId)` |
| `src/Services/InstagramService.php` | `public function getRecentMedia(ConnectedAccount $account)`<br>`public function postMedia(ConnectedAccount $account, $imageUrl, $caption)`<br>`public function getAllConnectedAccounts()`<br>`public function getPrimaryAccount()` |
| `src/Services/WhatsAppBusinessService.php` | `public function __construct()`<br>`public function getUnreadMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessages(?OAuthConfiguration $config = null): Collection`<br>`public function getMessage(string $messageId, ?OAuthConfiguration $config = null)`<br>`public function sendReply($to, $body, ?OAuthConfiguration $config = null)`<br>`public function sendMessage($to, $body, ?OAuthConfiguration $config = null)` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
