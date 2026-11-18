# Genealogy: Genealogy People Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-people). Observed identity: [`liberusoftware/module-genealogy-people-filament`](../../../modules/source/liberusoftware--module-genealogy-people-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-people-filament`  
**Matching domain module:** `genealogy-people`  
**Application:** Genealogy  
**Source feature:** [Genealogy People](../features/genealogy-people.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-people` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Names:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attributes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Life events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Living/deceased status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Merge candidates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-people-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `names`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attributes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `life-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `living-deceased-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `merge-candidates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-people` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-people-filament`](https://github.com/liberusoftware/module-genealogy-people-filament) (`liberusoftware/genealogy-people-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-people.md) · [API plan](../api/genealogy-people.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Names** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `names`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attributes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attributes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Life events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `life events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Living/deceased status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `living/deceased status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Merge candidates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `merge candidates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PeopleFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/PeopleFilamentServiceProvider.php) · [PersonResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource.php) · [CreatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/Pages/CreatePerson.php) · [EditPerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/Pages/EditPerson.php) · [ListPeople.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/Pages/ListPeople.php) · [AssociationsRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/AssociationsRelationManager.php) · [IdentitiesRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/IdentitiesRelationManager.php) · [LifeEventsRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/LifeEventsRelationManager.php) · [MergeCandidatesRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/MergeCandidatesRelationManager.php) · [NamesRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/NamesRelationManager.php) · [PersonSupportingRelationManager.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people-filament/src/Resources/PersonResource/RelationManagers/PersonSupportingRelationManager.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreateMergeCandidate.php) | `public function execute(array $attributes): MergeCandidate` |
| [CreatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePerson.php) | `public function execute(array $attributes): Person` |
| [CreatePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonAssociation.php) | `public function execute(array $attributes): PersonAssociation` |
| [CreatePersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonIdentity.php) | `public function execute(array $attributes): PersonIdentity` |
| [CreatePersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonLifeEvent.php) | `public function execute(array $attributes): PersonLifeEvent` |
| [CreatePersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonName.php) | `public function execute(array $attributes): PersonName` |
| [DeletePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePerson.php) | `public function execute(Person $person): void` |
| [DeletePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonAssociation.php) | `public function execute(PersonAssociation $association): void` |
| [DeletePersonSupportingRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonSupportingRecord.php) | `public function execute(Model $record): void` |
| [MergePersons.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/MergePersons.php) | `public function execute(Person $primary, Person $duplicate): Person` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/MergeCandidate.php) | `team_id`, `person_id`, `candidate_person_id`, `status`, `score`, `reason`, `metadata`, `reviewed_at` |
| [Person.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/Person.php) | `team_id`, `given_name`, `family_name`, `display_name`, `sex`, `aliases`, `attributes`, `birth_date`, `death_date`, `birth_place`, `death_place`, `is_public`, `metadata` |
| [PersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonAssociation.php) | `team_id`, `person_id`, `associated_person_id`, `associated_external_id`, `relationship`, `description`, `metadata` |
| [PersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonIdentity.php) | `team_id`, `person_id`, `type`, `value`, `label`, `is_verified`, `metadata` |
| [PersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonLifeEvent.php) | `team_id`, `person_id`, `type`, `date`, `place`, `description`, `metadata` |
| [PersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonName.php) | `team_id`, `person_id`, `type`, `given_name`, `family_name`, `prefix`, `suffix`, `is_preferred`, `metadata` |
<!-- layer-implementation-plan:end -->
