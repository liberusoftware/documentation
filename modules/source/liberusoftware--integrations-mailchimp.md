# liberusoftware/integrations-mailchimp: observed package reference

**Evidence status:** extracted from tracked source in `liberusoftware/project-boilerplate-laravel-filament`.

MailChimp marketing integration service.

## Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations-mailchimp` |
| Version | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `integrations-mailchimp` |
| Providers | `[]` |
| Capabilities | `integrations.mailchimp` |

## Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.38.0` |
| `liberusoftware/integrations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Integrations\\MailChimp\\": "src/"}`.

## Source entry points

| Source file | Public method signatures observed |
| --- | --- |
| `src/IntegrationsMailchimpServiceProvider.php` | `public function register(): void` |
| `src/Services/MailChimpService.php` | `public function __construct()`<br>`public function setClient(ApiClient $client): void`<br>`public function getLists()`<br>`public function isConfigured(): bool`<br>`public function createList($name, $company, $permission_reminder, $from_name, $from_email)`<br>`public function addMember($list_id, $email, $status = 'subscribed', $merge_fields = [])`<br>`public function createCampaign($list_id, $subject, $from_name, $reply_to, $html_content)`<br>`public function createABTestCampaign($list_id, $subject_a, $subject_b, $from_name, $reply_to, $html_content_a, $html_content_b, $test_size = 50, $winner_criteria = 'opens')` |

## Persistence and lifecycle

- None (stateless adapter or reuses parent module persistence).

## Verification

Tracked files under `tests/`: **1**.

- `tests/Unit/ServiceProviderTest.php`
