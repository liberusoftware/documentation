# CRM: CRM Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-core). Observed identity: [`liberusoftware/module-crm-core-filament`](../../../modules/source/liberusoftware--module-crm-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-core-filament`  
**Matching domain module:** `crm-core`  
**Application:** CRM  
**Source feature:** [CRM Core](../features/crm-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Organizations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Households:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Owners:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Teams:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tags:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Favorites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Record lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unified timeline:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `organizations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `households`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `owners`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `teams`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tags`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `favorites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `record-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unified-timeline`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-core-filament`](https://github.com/liberusoftware/module-crm-core-filament) (`liberusoftware/crm-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-core.md) · [API plan](../api/crm-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Organizations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `organizations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Households** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `households`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relationships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relationships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Owners** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `owners`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Teams** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `teams`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tags** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tags`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Notes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `notes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attachments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attachments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Favorites** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `favorites`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Record lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `record lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unified timeline** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unified timeline`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CRMCoreFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/CRMCoreFilamentPlugin.php) · [CRMCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/CRMCoreFilamentServiceProvider.php) · [RecordResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/Resources/RecordResource.php) · [CreateRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/Resources/RecordResource/Pages/CreateRecord.php) · [EditRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/Resources/RecordResource/Pages/EditRecord.php) · [ListRecords.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core-filament/src/Resources/RecordResource/Pages/ListRecords.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddNote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/AddNote.php) | `public function execute(Record $record, string $body, ?int $authorId = null): Note` |
| [ArchiveRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ArchiveRecord.php) | `public function execute(Record $record): Record` |
| [CreateRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRecord.php) | `public function execute(string $type, int $teamId, string $name, array $data = [], ?int $ownerId = null): Record` |
| [CreateRelationship.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateRelationship.php) | `public function execute(Record $from, Record $to, string $type, array $metadata = []): Relationship` |
| [CreateTag.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/CreateTag.php) | `public function execute(int $teamId, string $name): Tag` |
| [TagRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/TagRecord.php) | `public function execute(Record $record, Tag $tag): void` |
| [ToggleFavorite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/ToggleFavorite.php) | `public function execute(Model $record, int $teamId, int $userId): bool` |
| [UpdateRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Actions/UpdateRecord.php) | `public function execute(Record $record, array $attributes): Record` |
| [RecordRepository.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Contracts/RecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |
| [EloquentRecordRepository.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Services/EloquentRecordRepository.php) | `public function find(string $type, int\|string $id): ?Record`<br>`public function paginate(string $type, int $perPage = 25): LengthAwarePaginator` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Attachment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Attachment.php) | `team_id`, `uploaded_by`, `disk`, `path`, `name`, `mime_type`, `size`, `metadata` |
| [Contact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [Favorite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Favorite.php) | `team_id`, `user_id` |
| [Household.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Household.php) | No literal fillable array detected; inspect the model and API schema. |
| [Note.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Note.php) | `team_id`, `author_id`, `body` |
| [Organization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Organization.php) | No literal fillable array detected; inspect the model and API schema. |
| [Record.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Record.php) | `record_type`, `team_id`, `owner_id`, `name`, `status`, `data`, `archived_at` |
| [Relationship.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-core/src/Models/Relationship.php) | `team_id`, `relationship_type`, `metadata` |
<!-- layer-implementation-plan:end -->
