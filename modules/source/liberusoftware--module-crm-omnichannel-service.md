# liberusoftware/module-crm-omnichannel-service: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-omnichannel-service](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-omnichannel-service`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-omnichannel-service` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-omnichannel-service` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\OmnichannelService\\OmnichannelServiceServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\OmnichannelService\\OmnichannelServiceServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/module.json).

**Declared capabilities:** crm.omnichannel-service

**Declared features:** Multichannel conversation intake and interaction history, Routing, workspace, macros, suggestions, swarming and collision control

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\OmnichannelService\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AssignConversation.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/AssignConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Conversation` |
| [src/Actions/RecordInteraction.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordInteraction.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Interaction` |
| [src/Actions/RecordWorkspaceEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordWorkspaceEvent.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): WorkspaceEvent` |
| [src/Actions/StartConversation.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/StartConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Conversation` |
| [src/Queries/ConversationQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Queries/ConversationQuery.php) | `public function forTeam(int $teamId)` |
| [src/Services/OmnichannelPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Services/OmnichannelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Models/Conversation.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Conversation.php) · [src/Models/Interaction.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Interaction.php) · [src/Models/Macro.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Macro.php) · [src/Models/WorkspaceEvent.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/WorkspaceEvent.php) · [src/OmnichannelServiceServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/OmnichannelServiceServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_110000_create_crm_omnichannel_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/database/migrations/2026_08_26_110000_create_crm_omnichannel_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/OmnichannelService/OmnichannelServiceModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/tests/Feature/OmnichannelService/OmnichannelServiceModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
