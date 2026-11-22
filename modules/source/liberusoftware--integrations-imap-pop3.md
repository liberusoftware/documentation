# liberusoftware/integrations-imap-pop3: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

IMAP and POP3 email integration services.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-imap-pop3` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-imap-pop3` |
| Providers | `[]` |
| Capabilities | `integrations.imap.pop3` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\ImapPop3\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsImapPop3ServiceProvider.php` | `public function register(): void` |
| `src/Services/ImapService.php` | `public function getUnreadMessages(OAuthConfiguration $config): Collection`<br>`public function getMessage($messageId, OAuthConfiguration $config): ?array`<br>`public function sendReply(string $messageId, $content, OAuthConfiguration $config)`<br>`public function sendMessage($to, $subject, $content, OAuthConfiguration $config)` |
| `src/Services/Pop3Service.php` | `public function getUnreadMessages(OAuthConfiguration $config): Collection`<br>`public function getMessage($messageId, OAuthConfiguration $config)`<br>`public function sendReply($messageId, $content, OAuthConfiguration $config)`<br>`public function sendMessage($to, $subject, $content, OAuthConfiguration $config)` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
