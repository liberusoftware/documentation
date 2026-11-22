# liberusoftware/integrations-microsoft: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

Outlook Mail and Outlook Calendar integration services.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-microsoft` |
| Version | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-microsoft` |
| Providers | `[]` |
| Capabilities | `integrations.microsoft` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\Microsoft\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsMicrosoftServiceProvider.php` | `public function register(): void` |
| `src/Services/OutlookCalendarService.php` | `public function __construct()`<br>`public function createEvent(Task $task): void`<br>`public function updateEvent(Task $task): void`<br>`public function deleteEvent(Task $task): void`<br>`public function fetchEvents(array $params = []): array`<br>`public function syncEvents(array $events): void` |
| `src/Services/OutlookService.php` | `public function __construct()`<br>`public function getUnreadMessages(OAuthConfiguration $config): Collection`<br>`public function getMessage($messageId, OAuthConfiguration $config)`<br>`public function sendReply($messageId, $content, OAuthConfiguration $config)`<br>`public function sendMessage($to, $subject, $content, OAuthConfiguration $config)` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
