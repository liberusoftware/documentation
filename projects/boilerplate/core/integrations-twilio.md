# Boilerplate: Integrations Twilio Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-twilio`](../../../modules/source/liberusoftware--integrations-twilio.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-twilio` (`module-integrations-twilio`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Twilio voice, SMS, OAuth provider, request signature verification middleware, call settings model, and Filament resource extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations Twilio**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/Filament/App/Resources/CallSettingResource.php` | `public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getRelations(): array`<br>`public function getPages(): array` |
| `src/Http/Controllers/TwilioController.php` | `public function __construct(protected TwilioService $twilioService)`<br>`public function initiateCall(Request $request)`<br>`public function handleOutboundCall(Request $request)`<br>`public function handleInboundCall(Request $request)`<br>`public function handleRecordingCallback(Request $request): ResponseFactory|Response`<br>`public function startRecording(Request $request)`<br>`public function stopRecording(Request $request)` |
| `src/Http/Middleware/VerifyTwilioRequest.php` | `public function handle(Request $request, Closure $next): Response` |
| `src/IntegrationsTwilioServiceProvider.php` | `public function register(): void` |
| `src/Services/TwilioService.php` | `public function __construct()`<br>`public function setClient($client): void`<br>`public function sendSMS(string $to, string $message): bool`<br>`public function makeCall(string $to, string $url): bool`<br>`public function getCallLogs(array $filters = []): array`<br>`public function getCallDetails(string $callSid)`<br>`public function initiateCall(string $to)`<br>`public function startCallRecording(string $callSid)` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-twilio` via Composer and enable `integrations-twilio` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
