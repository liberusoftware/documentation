# liberusoftware/integrations-twilio: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Twilio voice, SMS, OAuth provider, and call settings integration.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-twilio` |
| Version | `1.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-twilio` |
| Providers | `[]` |
| Capabilities | `integrations.twilio` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Twilio\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/Filament/App/Resources/CallSettingResource.php` | `public function form(Schema $schema): Schema`<br>`public function table(Table $table): Table`<br>`public function getRelations(): array`<br>`public function getPages(): array` |
| `src/Http/Controllers/TwilioController.php` | `public function __construct(protected TwilioService $twilioService)`<br>`public function initiateCall(Request $request)`<br>`public function handleOutboundCall(Request $request)`<br>`public function handleInboundCall(Request $request)`<br>`public function handleRecordingCallback(Request $request): ResponseFactory|Response`<br>`public function startRecording(Request $request)`<br>`public function stopRecording(Request $request)` |
| `src/Http/Middleware/VerifyTwilioRequest.php` | `public function handle(Request $request, Closure $next): Response` |
| `src/IntegrationsTwilioServiceProvider.php` | `public function register(): void` |
| `src/Services/TwilioService.php` | `public function __construct()`<br>`public function setClient($client): void`<br>`public function sendSMS(string $to, string $message): bool`<br>`public function makeCall(string $to, string $url): bool`<br>`public function getCallLogs(array $filters = []): array`<br>`public function getCallDetails(string $callSid)`<br>`public function initiateCall(string $to)`<br>`public function startCallRecording(string $callSid)` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
