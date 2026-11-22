# Boilerplate: Integrations Zernio Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-zernio`](../../../modules/source/liberusoftware--integrations-zernio.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-zernio` (`module-integrations-zernio`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Zernio multi-channel social publishing, advertising, webhook controller, and tenant profile provisioning extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Zernio**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
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

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-zernio` via Composer and enable `integrations-zernio` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
