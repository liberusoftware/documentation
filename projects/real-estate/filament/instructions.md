# Real Estate: Instructions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#instructions). Observed identity: [`liberusoftware/real-estate-instructions-filament`](../../../modules/source/liberusoftware--real-estate-instructions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-instructions-filament`  
**Matching domain module:** `real-estate-instructions`  
**Application:** Real Estate  
**Source feature:** [Instructions](../features/instructions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-instructions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency agreements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disclosures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Withdrawal:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-instructions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `agency-agreements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disclosures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `withdrawal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-instructions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-instructions-filament`](https://github.com/liberusoftware/module-real-estate-instructions-filament) (`liberusoftware/real-estate-instructions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/instructions.md) · [API plan](../api/instructions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Agency agreements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agency agreements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disclosures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disclosures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Withdrawal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `withdrawal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [InstructionsFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/InstructionsFilamentPlugin.php) · [InstructionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/InstructionsFilamentServiceProvider.php) · [InstructionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/Resources/InstructionResource.php) · [CreateInstruction.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/Resources/InstructionResource/Pages/CreateInstruction.php) · [EditInstruction.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/Resources/InstructionResource/Pages/EditInstruction.php) · [ListInstructions.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-filament/src/Resources/InstructionResource/Pages/ListInstructions.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [InstructionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions/src/Policies/InstructionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Instruction $instruction): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Instruction $instruction): bool`<br>`public function delete(AuthUser $authUser, Instruction $instruction): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Instruction $instruction): bool`<br>`public function forceDelete(AuthUser $authUser, Instruction $instruction): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Instruction $instruction): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Instruction.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions/src/Models/Instruction.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
