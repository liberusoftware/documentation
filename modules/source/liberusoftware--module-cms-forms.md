# liberusoftware/module-cms-forms: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Forms module for Liberu CMS: public form definitions and spam-protected submissions that emit a FormSubmitted event.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-forms](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-forms`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-forms` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-forms` |
| Module version field | `0.1.0` |
| Category / layers | `["core", "api", "filament"]` |
| Manifest provider(s) | `["Liberu\\Cms\\Forms\\CmsFormsServiceProvider"]` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Forms\\CmsFormsServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `illuminate/contracts` | `^13.0` |
| `illuminate/database` | `^13.0` |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-cms-content` | `^0.1` |
| `liberusoftware/module-cms-contracts` | `^0.1` |
| `liberusoftware/module-cms-core` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Forms\\": "src/", "Liberu\\Cms\\Forms\\Database\\Factories\\": "database/factories/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Filament/FormResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/FormResource.php) | `public static function form(Schema $schema): Schema`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/FormSubmissionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/FormSubmissionResource.php) | `public static function canCreate(): bool`<br>`public static function table(Table $table): Table`<br>`public static function getPages(): array` |
| [src/Filament/Pages/ListFormSubmissions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/Pages/ListFormSubmissions.php) | No named public method detected by the static index. |
| [src/Filament/Pages/ListForms.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Filament/Pages/ListForms.php) | No named public method detected by the static index. |
| [src/Http/Controllers/FormSubmissionController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Http/Controllers/FormSubmissionController.php) | `public function __construct( private EventBusInterface $events, private SubmissionValidator $validator, )`<br>`public function __invoke(Request $request, string $slug): JsonResponse` |
| [src/Support/SubmissionValidator.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Support/SubmissionValidator.php) | `public function validate(Form $form, array $input): array` |

Other non-legacy PHP sources: [src/CmsFormsModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/CmsFormsModule.php) · [src/CmsFormsServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/CmsFormsServiceProvider.php) · [src/Fields/FormField.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Fields/FormField.php) · [src/Fields/FormFieldType.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Fields/FormFieldType.php) · [src/Models/Form.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/Form.php) · [src/Models/FormSubmission.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/FormSubmission.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [routes/web.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/routes/web.php)

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_02_01_000000_create_cms_forms_table.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/database/migrations/2026_02_01_000000_create_cms_forms_table.php)
- [database/migrations/2026_02_01_000001_create_cms_form_submissions_table.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/database/migrations/2026_02_01_000001_create_cms_form_submissions_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
