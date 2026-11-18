# Accounting: Accounting Policies Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-policies). Observed identity: [`liberusoftware/module-accounting-policies-filament`](../../../modules/source/liberusoftware--module-accounting-policies-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-policies-filament`  
**Matching domain module:** `accounting-policies`  
**Application:** Accounting  
**Source feature:** [Accounting Policies](../features/accounting-policies.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-policies` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Effective-dated recognition:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capitalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Depreciation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **FX:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rounding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Write-off:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Materiality:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval rules:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-policies-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `effective-dated-recognition`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capitalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `depreciation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fx`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rounding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `write-off`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `materiality`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-policies` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-policies-filament`](https://github.com/liberusoftware/module-accounting-policies-filament) (`liberusoftware/accounting-policies-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-policies.md) · [API plan](../api/accounting-policies.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Effective-dated recognition** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `effective-dated recognition`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capitalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capitalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Depreciation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `depreciation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **FX** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fx`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rounding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rounding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Write-off** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `write-off`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Materiality** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `materiality`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountingPoliciesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-filament/src/AccountingPoliciesFilamentPlugin.php) · [AccountingPoliciesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-filament/src/AccountingPoliciesFilamentServiceProvider.php) · [PolicyRuleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-filament/src/Resources/PolicyRuleResource.php) · [ListPolicyRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-filament/src/Resources/PolicyRuleResource/Pages/ListPolicyRules.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PolicyRuleForDate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Queries/PolicyRuleForDate.php) | `public function handle(int\|string $bookId, PolicyCategory\|string $category, string $key, \DateTimeInterface\|string $date): ?PolicyRule` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SavePolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Actions/SavePolicyRule.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?PolicyRule $rule, array $attributes): PolicyRule` |
| [AccountingPoliciesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/src/Policies/AccountingPoliciesPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function delete(?Authenticatable $u, PolicyRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Models/PolicyRule.php) | `book_id`, `category`, `key`, `value`, `effective_from`, `effective_until`, `is_active`, `approved_by`, `approved_at`, `metadata` |
<!-- layer-implementation-plan:end -->
