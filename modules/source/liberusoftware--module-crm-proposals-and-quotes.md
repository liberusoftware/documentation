# liberusoftware/module-crm-proposals-and-quotes: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-proposals-and-quotes](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-proposals-and-quotes`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-proposals-and-quotes` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-proposals-and-quotes` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\ProposalsAndQuotes\\ProposalsAndQuotesServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\ProposalsAndQuotes\\ProposalsAndQuotesServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/module.json).

**Declared capabilities:** crm.proposals-and-quotes

**Declared features:** Branded templates, sections, scope and line items, Optional choices, versions, comments and approvals, Delivery, engagement, acceptance and expiry

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\ProposalsAndQuotes\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddProposalComment.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [src/Actions/ChangeProposalStatus.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [src/Actions/CreateProposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Proposal` |
| [src/Actions/CreateProposalTemplate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [src/Actions/CreateProposalVersion.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [src/Actions/UpdateProposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [src/Queries/ProposalQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |
| [src/Services/ProposalPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/ProposalStatusChanged.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Events/ProposalStatusChanged.php) · [src/Models/Proposal.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) · [src/Models/ProposalEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) · [src/Models/ProposalTemplate.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) · [src/Models/ProposalVersion.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) · [src/ProposalsAndQuotesServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/ProposalsAndQuotesServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_040000_create_crm_proposals_and_quotes_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/database/migrations/2026_08_26_040000_create_crm_proposals_and_quotes_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/ProposalsAndQuotes/ProposalsAndQuotesModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/tests/Feature/ProposalsAndQuotes/ProposalsAndQuotesModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
