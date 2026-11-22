# liberusoftware/integrations-zernio: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Zernio publishing, advertising, webhook, and tenant provisioning integration.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-zernio` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-zernio` |
| Providers | `[]` |
| Capabilities | `integrations.zernio` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Zernio\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Http/Controllers/ZernioWebhookController.php` | `public function __invoke(Request $request, Team $team, SyncExternalConversation $sync): JsonResponse` |
| `src/IntegrationsZernioServiceProvider.php` | `public function register(): void` |
| `src/Listeners/ProvisionZernioProfile.php` | `public function __construct(private readonly ZernioTenantService $zernio)`<br>`public function handle(TeamCreated $event): void` |
| `src/Services/Zernio/ZernioAdvertisingService.php` | `public function __construct(private readonly ZernioClient $client)`<br>`public function listAds(Model $team, array $filters = []): array`<br>`public function campaignAnalytics(Model $team, string $campaignId, array $filters = []): array`<br>`public function adAnalytics(Model $team, string $adId, array $filters = []): array`<br>`public function createCampaign(Model $team, array $payload): array`<br>`public function updateCampaign(Model $team, string $campaignId, array $payload): array` |
| `src/Services/Zernio/ZernioClient.php` | `public function request(): PendingRequest`<br>`public function createPost(array $payload): array`<br>`public function createProfile(string $name, ?string $description = null): array`<br>`public function getPost(string $postId): array`<br>`public function listPosts(array $query = []): array`<br>`public function updatePost(string $postId, array $payload): array`<br>`public function validatePost(array $payload): array`<br>`public function listAccounts(?string $profileId = null): array` |
| `src/Services/Zernio/ZernioPublisher.php` | `public function __construct(
        private readonly ZernioClient $client,
        private readonly ZernioTenantService $tenants,
    )`<br>`public function publish(SocialMediaPost $post, array $platforms): array`<br>`public function canPublishForPost(SocialMediaPost $post): bool`<br>`public function canPublish(array $platforms): bool` |
| `src/Services/Zernio/ZernioTenantService.php` | `public function __construct(private readonly ZernioClient $client)`<br>`public function ensureProfile(Model $team): string`<br>`public function connectUrl(Model $team, string $platform, ?string $redirectUrl = null): array`<br>`public function accounts(Model $team): array`<br>`public function analytics(Model $team, array $query = []): array`<br>`public function inbox(Model $team, array $query = []): array`<br>`public function comments(Model $team, array $query = []): array`<br>`public function reviews(Model $team, array $query = []): array` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
