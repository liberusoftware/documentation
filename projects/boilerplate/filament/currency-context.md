# Boilerplate: Currency Context Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#currency-context). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-currency-context-filament`
**Matching core package:** [`module-currency-context`](../core/currency-context.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Currency metadata, preferences, precision, formatting, exchange-rate contracts, and context.

## Adapter implementation plan

This package presents the Currency Context core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Currency Context core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
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
