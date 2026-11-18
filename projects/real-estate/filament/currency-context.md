# Real Estate: Currency Context Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#currency-context). Observed identity: [`liberusoftware/currency-context-filament`](../../../modules/source/liberusoftware--currency-context-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-currency-context-filament`  
**Matching domain module:** `currency-context`  
**Application:** Real Estate  
**Source feature:** [Currency Context](../features/currency-context.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `currency-context` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Currency metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preferences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Precision:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Formatting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exchange-rate contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Context:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-currency-context-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `currency-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `precision`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `formatting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exchange-rate-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `context`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `currency-context` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-currency-context-filament`](https://github.com/liberusoftware/module-currency-context-filament) (`liberusoftware/currency-context-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/currency-context.md) · [API plan](../api/currency-context.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Currency metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `currency metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Precision** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `precision`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Formatting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `formatting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exchange-rate contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exchange-rate contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Context** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `context`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CurrencyContextFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-filament/src/CurrencyContextFilamentPlugin.php) · [CurrencyContextFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-filament/src/CurrencyContextFilamentServiceProvider.php) · [Overview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-filament/src/Pages/Overview.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExchangeRateProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Contracts/ExchangeRateProvider.php) | `public function rate(Currency $base, Currency $quote, DateTimeImmutable $effectiveAt): ?ExchangeRate` |
| [CurrencyContext.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyContext.php) | `public function __construct(private array $currencies)`<br>`public function for(CurrencyRole $role): Currency` |
| [CurrencyPreferenceResolver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyPreferenceResolver.php) | `public function resolve(array $scopes, string $fallback): string` |
| [CurrencyRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyRegistry.php) | `public function __construct(private array $definitions)`<br>`public function get(string $code): Currency` |
| [MoneyFormatter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/MoneyFormatter.php) | `public function __construct(private readonly ?Closure $formatterFactory = null)`<br>`public function format(Money $money, string $locale): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Currency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Models/Currency.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
