# liberusoftware/module-crm-proposals-and-quotes-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-proposals-and-quotes-api](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-proposals-and-quotes-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-proposals-and-quotes-api` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-proposals-and-quotes-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\CRM\\ProposalsAndQuotesApi\\Providers\\ProposalsAndQuotesApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\ProposalsAndQuotesApi\\Providers\\ProposalsAndQuotesApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/module.json).

**Declared capabilities:** crm.proposals-and-quotes.api

**Declared features:** Templates, proposals, versions, approvals, delivery and acceptance API

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-crm-proposals-and-quotes` | `*` |

PSR-4 mappings: `{"Liberu\\CRM\\ProposalsAndQuotesApi\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-crm-proposals-and-quotes": "*"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/ProposalsAndQuotesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/src/Http/Controllers/ProposalsAndQuotesController.php) | `public function templates(Request $r, ProposalQuery $q)`<br>`public function template(Request $r, CreateProposalTemplate $a)`<br>`public function proposals(Request $r, ProposalQuery $q)`<br>`public function proposal(Request $r, CreateProposal $a)`<br>`public function version(Request $r, CreateProposalVersion $a)`<br>`public function status(Request $r, int $proposal, string $status, ChangeProposalStatus $a)`<br>`public function comment(Request $r, AddProposalComment $a)` |

Other non-legacy PHP sources: [src/Providers/ProposalsAndQuotesApiServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/src/Providers/ProposalsAndQuotesApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/proposals-and-quotes.yaml](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/openapi/v1/proposals-and-quotes.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
