# Billing: Module Billing Domains Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-domains). Observed identity: [`liberusoftware/module-billing-domains-filament`](../../../modules/source/liberusoftware--module-billing-domains-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-domains-filament`  
**Matching domain module:** `module-billing-domains`  
**Application:** Billing  
**Source feature:** [Module Billing Domains](../features/module-billing-domains.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-domains` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Registration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redemption:** resource/table/form/action or page behavior for this module's authorized workflow.
- **EPP:** resource/table/form/action or page behavior for this module's authorized workflow.
- **DNS:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Registrar adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-domains-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `registration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redemption`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `epp`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `registrar-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-domains` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-domains-filament`](https://github.com/liberusoftware/module-billing-domains-filament) (`liberusoftware/billing-domains-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-domains.md) · [API plan](../api/module-billing-domains.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redemption** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redemption`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **EPP** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `epp`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **DNS** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registrar adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registrar adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DomainsFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/DomainsFilamentPlugin.php) · [DomainsFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/DomainsFilamentServiceProvider.php) · [DnsRecordResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DnsRecordResource.php) · [DomainContactResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainContactResource.php) · [DomainResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainResource.php) · [CreateDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainResource/Pages/CreateDomain.php) · [ListDomains.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainResource/Pages/ListDomains.php) · [DomainTldResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainTldResource.php) · [CreateDomainTld.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainTldResource/Pages/CreateDomainTld.php) · [ListDomainTlds.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/DomainTldResource/Pages/ListDomainTlds.php) · [EppOperationResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-filament/src/Resources/EppOperationResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListDomainsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/ListDomainsRecords.php) | `public function handle(int $teamId): Collection` |
| [SearchDomains.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/SearchDomains.php) | `public function __construct(private RegistrarManager $registrars)`<br>`public function execute(string $domain, string $registrar, array $suggestionTlds = ['com', 'net', 'org']): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/CreateDomain.php) | `public function handle(int $teamId, array $attributes): Domain` |
| [CreateDomainContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/CreateDomainContact.php) | `public function execute(int $teamId, array $attributes): DomainContact` |
| [DeleteDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/DeleteDomain.php) | `public function execute(Domain $domain): void` |
| [RecordEppOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RecordEppOperation.php) | `public function execute(Domain $domain, string $operation, string $status, array $payload = [], ?string $eppCode = null): EppOperation` |
| [RedeemDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RedeemDomain.php) | `public function execute(Domain $domain): Domain` |
| [RegisterDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RegisterDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, mixed $customerId): Domain` |
| [RenewDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RenewDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, int $period = 1): Domain` |
| [TransferDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/TransferDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, string $authCode, mixed $customerId, ?string $registrar = null): Domain` |
| [UpdateDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/UpdateDomain.php) | `public function handle(Domain $domain, array $attributes): Domain` |
| [UpsertDnsRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/UpsertDnsRecord.php) | `public function execute(int $teamId, array $attributes): DnsRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnsRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DnsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Domain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/Domain.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainTld.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainTld.php) | No literal fillable array detected; inspect the model and API schema. |
| [EppOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/EppOperation.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
