# Genealogy: Relationships Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#relationships). Observed identity: [`liberusoftware/module-genealogy-relationships-filament`](../../../modules/source/liberusoftware--module-genealogy-relationships-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-relationships-filament`  
**Matching domain module:** `genealogy-relationships`  
**Application:** Genealogy  
**Source feature:** [Relationships](../features/relationships.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-relationships` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Parent:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partner:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Household:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adoption:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guardianship:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Uncertain links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Graph validation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-relationships-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `parent`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partner`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `household`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adoption`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guardianship`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `uncertain-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `graph-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-relationships` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-relationships-filament`](https://github.com/liberusoftware/module-genealogy-relationships-filament) (`liberusoftware/genealogy-relationships-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/relationships.md) · [API plan](../api/relationships.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Parent** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parent`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partner** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Household** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `household`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adoption** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adoption`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Guardianship** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guardianship`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Uncertain links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `uncertain links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Graph validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `graph validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RelationshipCalculator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/Pages/RelationshipCalculator.php) · [RelationshipsFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/RelationshipsFilamentServiceProvider.php) · [RelationshipResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/Resources/RelationshipResource.php) · [CreateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/Resources/RelationshipResource/Pages/CreateRelationship.php) · [EditRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/Resources/RelationshipResource/Pages/EditRelationship.php) · [ListRelationships.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships-filament/src/Resources/RelationshipResource/Pages/ListRelationships.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GraphValidator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/GraphValidator.php) | `public function validate(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): array`<br>`public function assertValid(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): void` |
| [ParentGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/ParentGraph.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [RelationshipCalculator.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/RelationshipCalculator.php) | `public function between(string $firstPersonId, string $secondPersonId, ?string $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/CreateRelationship.php) | `public function execute(array $attributes): Relationship` |
| [DeleteRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/DeleteRelationship.php) | `public function execute(Relationship $relationship): void` |
| [RecordRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/RecordRelationship.php) | `public function execute(array $attributes): Relationship` |
| [UpdateRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/UpdateRelationship.php) | `public function __construct(private readonly GraphValidator $validator)`<br>`public function execute(Relationship $relationship, array $attributes): Relationship` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Relationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Models/Relationship.php) | `team_id`, `person_id`, `related_person_id`, `type`, `confidence`, `metadata` |
<!-- layer-implementation-plan:end -->
