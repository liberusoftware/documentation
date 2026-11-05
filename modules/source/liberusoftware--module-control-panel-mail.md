# liberusoftware/module-control-panel-mail: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Control Panel mail domains, accounts, routing and delivery state.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-mail](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-mail`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-mail` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-mail` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\Mail\\MailServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/module.json).

**Declared capabilities:** control-panel.mail

**Declared features:** Mail domains, Mail accounts, Mailboxes, Routing, Quotas, Spam and virus controls, DKIM/SPF/DMARC generation, Delivery diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\Mail\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ConfigureMailAuthentication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailAuthentication.php) | `public function __construct(private readonly RotateDkimKey $rotateDkimKey)`<br>`public function execute(MailDomain $domain, array $attributes = []): MailDomain` |
| [src/Actions/ConfigureMailControls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailControls.php) | `public function execute(array $a): MailControl` |
| [src/Actions/CreateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAccount.php) | `public function execute(array $attributes): MailAccount` |
| [src/Actions/CreateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAlias.php) | `public function execute(array $a): MailAlias` |
| [src/Actions/CreateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailRoute.php) | `public function execute(array $attributes): MailRoute` |
| [src/Actions/DeleteMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAccount.php) | `public function execute(MailAccount $account): void` |
| [src/Actions/DeleteMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAlias.php) | `public function execute(MailAlias $alias): void` |
| [src/Actions/DeleteMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailRoute.php) | `public function execute(MailRoute $route): void` |
| [src/Actions/RecordDeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordDeliveryDiagnostic.php) | `public function execute(array $a): DeliveryDiagnostic` |
| [src/Actions/RecordMailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordMailOperation.php) | `public function execute(array $a): MailOperation` |
| [src/Actions/RegisterMailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RegisterMailDomain.php) | `public function execute(array $attributes): MailDomain` |
| [src/Actions/RotateDkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RotateDkimKey.php) | `public function execute(string $teamId, string $domain, string $selector = 'default'): DkimKey` |
| [src/Actions/UpdateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailAccount.php) | `public function execute(MailAccount $account, array $attributes): MailAccount` |
| [src/Actions/UpdateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailAlias.php) | `public function execute(MailAlias $alias, array $attributes): MailAlias` |
| [src/Actions/UpdateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailRoute.php) | `public function execute(MailRoute $route, array $attributes): MailRoute` |
| [src/Queries/ListMailAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Queries/ListMailAccounts.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/MailServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/MailServiceProvider.php) · [src/Models/DeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DeliveryDiagnostic.php) · [src/Models/DkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DkimKey.php) · [src/Models/MailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAccount.php) · [src/Models/MailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAlias.php) · [src/Models/MailControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailControl.php) · [src/Models/MailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailDomain.php) · [src/Models/MailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailOperation.php) · [src/Models/MailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailRoute.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_110001_create_control_panel_mail_accounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/database/migrations/2026_08_24_110001_create_control_panel_mail_accounts.php)
- [database/migrations/2026_08_24_120003_create_control_panel_mail_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/database/migrations/2026_08_24_120003_create_control_panel_mail_operations.php)
- [database/migrations/2026_08_24_130002_create_control_panel_mail_features.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/database/migrations/2026_08_24_130002_create_control_panel_mail_features.php)
- [database/migrations/2026_08_25_120002_add_mail_domain_uniqueness.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/database/migrations/2026_08_25_120002_add_mail_domain_uniqueness.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
