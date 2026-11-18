# Genealogy: Genealogy Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-core). Observed identity: [`liberusoftware/module-genealogy-core-filament`](../../../modules/source/liberusoftware--module-genealogy-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-core-filament`  
**Matching domain module:** `genealogy-core`  
**Application:** Genealogy  
**Source feature:** [Genealogy Core](../features/genealogy-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Trees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identifiers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy defaults:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terminology:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `trees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identifiers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy-defaults`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terminology`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-core-filament`](https://github.com/liberusoftware/module-genealogy-core-filament) (`liberusoftware/genealogy-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-core.md) · [API plan](../api/genealogy-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Trees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identifiers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identifiers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy defaults** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy defaults`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terminology** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terminology`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [GenealogyCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-filament/src/GenealogyCoreFilamentServiceProvider.php) · [TreeResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-filament/src/Resources/TreeResource.php) · [CreateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-filament/src/Resources/TreeResource/Pages/CreateTree.php) · [EditTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-filament/src/Resources/TreeResource/Pages/EditTree.php) · [ListTrees.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-filament/src/Resources/TreeResource/Pages/ListTrees.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TreeStatistics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Queries/TreeStatistics.php) | `public function __construct(private readonly ?ParentGraphReader $graph = null)`<br>`public function for(Tree $tree): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/CreateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): Tree` |
| [DeleteTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/DeleteTree.php) | `public function execute(Tree $tree): void` |
| [SetTreeOwner.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeOwner.php) | `public function execute(Tree $tree, string\|int\|null $userId): Tree` |
| [SetTreeVisibility.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeVisibility.php) | `public function execute(Tree $tree, bool $isPublic): Tree` |
| [UpdateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/UpdateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(Tree $tree, array $attributes): Tree` |
| [ParentGraphReader.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/ParentGraphReader.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [PersonReferenceResolver.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/PersonReferenceResolver.php) | `public function existsForTeam(mixed $personId, string $teamId): bool` |
| [TeamOwnedPolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TeamOwnedPolicy.php) | `public function viewAny(?object $actor): bool`<br>`public function view(?object $actor, object $record): bool`<br>`public function create(?object $actor): bool`<br>`public function update(?object $actor, object $record): bool`<br>`public function delete(?object $actor, object $record): bool` |
| [TreePolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TreePolicy.php) | `public function view(?object $actor, Tree $tree): bool`<br>`public function manage(?object $actor, Tree $tree): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Tree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Models/Tree.php) | `team_id`, `name`, `status`, `description`, `root_person_id`, `is_public`, `metadata`, `user_id`, `identifier`, `terminology` |
<!-- layer-implementation-plan:end -->
