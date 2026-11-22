# Boilerplate: Integrations MailChimp Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-mailchimp`](../../../modules/source/liberusoftware--integrations-mailchimp.md).
<!-- source-reconciliation:end -->

**Package identifier:** `liberusoftware/integrations-mailchimp` (`module-integrations-mailchimp`)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** MailChimp marketing list, member, and campaign integration service extending liberusoftware/integrations.

## Ownership and boundaries

This package is the authoritative, independently installable implementation of **Integrations MailChimp**.

- Owns its domain services, models, actions, middleware, controllers, and provider-specific configuration.
- Exposes explicit public contracts and never depends on host `App\` domain logic.
- Integrates with `liberusoftware/integrations` contracts (`IntegrationAdapter`, `CalendarService`, `SsrfGuard`, etc.) and shared foundation modules (`organizations-teams`, `roles-permissions`, `tenancy`) through public boundaries.
- Keeps credentials encrypted/config-backed and redacts sensitive tokens from logs and responses.

## Key entry points and persistence

| Source file | Public API |
| --- | --- |
| `src/IntegrationsMailchimpServiceProvider.php` | `public function register(): void` |
| `src/Services/MailChimpService.php` | `public function __construct()`<br>`public function setClient(ApiClient $client): void`<br>`public function getLists()`<br>`public function isConfigured(): bool`<br>`public function createList($name, $company, $permission_reminder, $from_name, $from_email)`<br>`public function addMember($list_id, $email, $status = 'subscribed', $merge_fields = [])`<br>`public function createCampaign($list_id, $subject, $from_name, $reply_to, $html_content)`<br>`public function createABTestCampaign($list_id, $subject_a, $subject_b, $from_name, $reply_to, $html_content_a, $html_content_b, $test_size = 50, $winner_criteria = 'opens')` |

**Migrations:**
- None (stateless adapter or reuses parent module persistence).

## Verification and consumer contract

- Verified with Pest 5 targeting 100% line coverage across `src/`.
- Consumers install `liberusoftware/integrations-mailchimp` via Composer and enable `integrations-mailchimp` via Module Manager without copying source.
- See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [API standards](../../../architecture/API.md), and [testing standards](../../../standards/TESTING.md).
