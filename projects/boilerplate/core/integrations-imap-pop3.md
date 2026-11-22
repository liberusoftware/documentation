# Boilerplate: Integrations IMAP/POP3 Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-imap-pop3`](../../../modules/source/liberusoftware--integrations-imap-pop3.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-imap-pop3` (`module-integrations-imap-pop3`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** IMAP and POP3 inbound email integration services extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations IMAP/POP3**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/IntegrationsImapPop3ServiceProvider.php` | `public function register(): void` |
| `src/Services/ImapService.php` | `public function getUnreadMessages(OAuthConfiguration $config): Collection`<br>`public function getMessage($messageId, OAuthConfiguration $config): ?array`<br>`public function sendReply(string $messageId, $content, OAuthConfiguration $config)`<br>`public function sendMessage($to, $subject, $content, OAuthConfiguration $config)` |
| `src/Services/Pop3Service.php` | `public function getUnreadMessages(OAuthConfiguration $config): Collection`<br>`public function getMessage($messageId, OAuthConfiguration $config)`<br>`public function sendReply($messageId, $content, OAuthConfiguration $config)`<br>`public function sendMessage($to, $subject, $content, OAuthConfiguration $config)` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-imap-pop3` via Composer and enable `integrations-imap-pop3` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
