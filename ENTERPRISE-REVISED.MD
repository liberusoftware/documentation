Liberu Enterprise Platform

Composable Package and Application Architecture

Status: Proposed
Architecture: Composable Modular Laravel Platform
Stack: Laravel 13 · PHP 8.5 · Filament 5 · Livewire 4

---

1. Purpose

Liberu is implemented as a collection of independent, reusable Composer packages.

Each Liberu repository represents a product, application, or capability ecosystem. A repository must not automatically be treated as one Composer package or one runtime module.

Instead, repositories are composed of smaller packages with clear ownership and responsibilities.

For example:

cms-laravel
    ↓
CMS packages

ecommerce-laravel
    ↓
Ecommerce packages

billing-laravel
    ↓
Billing packages

accounting-laravel
    ↓
Accounting packages

Common capabilities are extracted into reusable packages and shared by multiple Liberu products.

For example:

payment-contracts
        ↑
        │
payment-core
        ↑
   ┌────┼────┐
   │    │    │
Stripe PayPal Adyen
   │    │    │
   └────┼────┘
        │
        ├── ecommerce-laravel
        ├── billing-laravel
        ├── subscriptions-laravel
        ├── bookings-laravel
        └── donations-laravel

The goal is:

«Build capabilities once, package them independently, and compose them into any Laravel application that requires them.»

---

2. Architectural Hierarchy

Liberu uses four distinct architectural levels.

Level 1 — Foundation
    Shared infrastructure and contracts

Level 2 — Capability Packages
    Reusable business capabilities

Level 3 — Product Packages
    Packages specific to a particular product domain

Level 4 — Applications / Distributions
    Laravel applications that compose packages

The relationship is:

Foundation
    ↓
Reusable Capabilities
    ↓
Product Domain Packages
    ↓
Application

An application must consume the lowest-level package that provides the capability it requires.

It must not depend on an entire product repository merely to access one feature.

---

3. Package Independence

Every package must be independently installable where technically meaningful.

A package must:

- have its own "composer.json";
- have its own PSR-4 namespace;
- have its own service provider;
- own its own configuration;
- own its own migrations;
- own its own tests;
- own its own documentation;
- declare its dependencies explicitly;
- avoid dependencies on application-specific "App\" classes;
- avoid dependencies on unrelated product packages.

A package may be consumed by:

- a Liberu application;
- another Liberu package;
- a third-party Laravel application;
- a custom Laravel application.

The package must not assume that it is running inside "cms-laravel", "ecommerce-laravel", or any other specific application.

---

4. Repository Structure

A Liberu repository is a development boundary.

It is not necessarily a Composer package boundary.

For example:

cms-laravel/
├── packages/
│   ├── cms-core/
│   ├── cms-content/
│   ├── cms-media/
│   ├── cms-pages/
│   ├── cms-navigation/
│   ├── cms-workflows/
│   └── cms-filament/
│
├── app/
├── config/
├── routes/
├── tests/
└── composer.json

The repository root application composes the packages.

The packages remain independently reusable.

Similarly:

ecommerce-laravel/
├── packages/
│   ├── ecommerce-core/
│   ├── ecommerce-catalog/
│   ├── ecommerce-cart/
│   ├── ecommerce-orders/
│   ├── ecommerce-checkout/
│   ├── ecommerce-payments/
│   ├── ecommerce-shipping/
│   └── ecommerce-filament/
│
├── app/
├── config/
├── routes/
├── tests/
└── composer.json

Shared functionality must be extracted from these repositories when it has legitimate reuse outside the owning product.

---

5. Product Repositories

The main Liberu repositories are treated as product ecosystems.

They may contain multiple Composer packages.

The initial mapping is:

Repository| Product| Package Family
"cms-laravel"| CMS| "liberu/cms-*"
"ecommerce-laravel"| Ecommerce| "liberu/ecommerce-*"
"crm-laravel"| CRM| "liberu/crm-*"
"billing-laravel"| Billing| "liberu/billing-*"
"accounting-laravel"| Accounting| "liberu/accounting-*"
"control-panel-laravel"| Control Panel| "liberu/control-panel-*"
"ai-gateway-laravel"| AI Gateway| "liberu/ai-*"
"omnichannel-laravel"| Omnichannel| "liberu/omnichannel-*"
"growth-laravel"| Growth| "liberu/growth-*"

The exact package decomposition is determined by domain ownership.

The rule is:

«A package represents one cohesive capability, not one repository.»

---

6. Package Categories

Every Liberu package belongs to one of these categories.

6.1 Foundation Packages

These provide infrastructure shared across many products.

Examples:

liberu/platform-contracts
liberu/platform-core
liberu/identity
liberu/tenancy
liberu/audit
liberu/settings
liberu/permissions
liberu/localisation
liberu/files

Foundation packages must contain only genuinely shared functionality.

They must not become a dumping ground for unrelated business logic.

---

6.2 Domain Contract Packages

These define stable interfaces for capabilities that may have multiple implementations.

Examples:

liberu/payment-contracts
liberu/customer-contracts
liberu/tax-contracts
liberu/shipping-contracts
liberu/search-contracts
liberu/notification-contracts
liberu/ai-contracts

Contracts are deliberately lightweight.

They define interfaces, DTOs, value objects, enums, and shared exceptions.

They do not contain provider-specific implementations.

---

6.3 Capability Packages

These provide reusable business capabilities.

Examples:

liberu/payment-core
liberu/customer-core
liberu/address
liberu/cart
liberu/order
liberu/invoice
liberu/subscription
liberu/media
liberu/content

A capability package may be consumed by multiple product repositories.

---

6.4 Integration Packages

Integration packages connect a capability to an external provider.

Examples:

liberu/payment-stripe
liberu/payment-paypal
liberu/payment-adyen
liberu/payment-mollie
liberu/storage-s3
liberu/storage-azure
liberu/ai-openai
liberu/ai-anthropic

An integration package implements a contract.

It must not be embedded inside Ecommerce, Billing, or another consuming product.

---

6.5 Product Packages

Product packages contain functionality that is genuinely specific to one domain.

Examples:

liberu/ecommerce-catalog
liberu/ecommerce-cart
liberu/ecommerce-checkout
liberu/ecommerce-orders

liberu/crm-leads
liberu/crm-opportunities

liberu/cms-pages
liberu/cms-content
liberu/cms-publishing

Product packages may consume shared capability packages.

They must not duplicate shared functionality.

---

6.6 Presentation Packages

Filament and other UI integrations are separate packages from core domain logic.

For example:

liberu/cms-filament
liberu/ecommerce-filament
liberu/crm-filament
liberu/billing-filament

A Filament package depends on the domain packages it represents.

The domain package does not depend on Filament.

This allows the same business logic to be used by:

- Filament;
- APIs;
- console commands;
- Livewire applications;
- background jobs;
- third-party applications.

---

7. The Payment Example

Payments are the primary example of this architecture.

Payment functionality must not belong exclusively to Ecommerce.

The package hierarchy is:

liberu/payment-contracts
        │
        ├── PaymentGateway
        ├── PaymentMethod
        ├── PaymentIntent
        ├── PaymentResult
        ├── Refund
        └── PaymentException
                │
                ▼
liberu/payment-core
                │
                ├── PaymentManager
                ├── GatewayRegistry
                ├── PaymentMethodRegistry
                └── Payment orchestration
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
payment-    payment-   payment-
stripe       paypal     adyen
        │       │        │
        └───────┼────────┘
                ▼
        Any consuming application

Ecommerce then consumes the contracts and core:

ecommerce-checkout
        ↓
payment-core
        ↓
payment-contracts

Stripe is added independently:

payment-stripe
        ↓
implements PaymentGateway
        ↓
registered with payment-core

Billing can use exactly the same integration:

billing
    ↓
payment-core
    ↓
payment-stripe

Subscriptions can use it:

subscriptions
    ↓
payment-core
    ↓
payment-stripe

Bookings can use it:

bookings
    ↓
payment-core
    ↓
payment-stripe

No product owns Stripe.

No product duplicates Stripe's API implementation.

The integration is implemented once and reused everywhere.

---

8. Payment Contracts

The payment contract package defines the stable API.

Conceptually:

interface PaymentGateway
{
    public function authorize(
        PaymentRequest $request
    ): PaymentResult;

    public function capture(
        PaymentReference $payment
    ): PaymentResult;

    public function refund(
        RefundRequest $request
    ): RefundResult;
}

The interface must contain only provider-neutral concepts.

It must not contain:

StripePaymentIntent
StripeCheckoutSession
StripeWebhookEvent

Those belong to:

liberu/payment-stripe

The contract is the stable boundary.

Providers implement the contract.

Applications consume the contract.

---

9. Payment Methods

Payment methods are also shared capabilities.

Examples:

card
bank_transfer
paypal
apple_pay
google_pay
klarna

A payment method is not inherently an Ecommerce feature.

The payment system provides a standard method registry.

PaymentMethodRegistry::register(
    CardPaymentMethod::class
);

Stripe provides the provider implementation.

Ecommerce decides which methods are available during checkout.

Billing decides which methods are available for invoices.

Subscriptions decides which methods are available for recurring payments.

The same provider can therefore support multiple products without duplication.

---

10. Provider and Application Separation

The architecture must always separate:

Business Capability
        ↓
Contract
        ↓
Core Orchestration
        ↓
Provider Adapter
        ↓
External Service

Example:

Ecommerce Checkout
        ↓
Payment Contract
        ↓
Payment Core
        ↓
Stripe Adapter
        ↓
Stripe API

The Ecommerce package must never call the Stripe SDK directly.

The Billing package must never call the Stripe SDK directly.

The Subscription package must never call the Stripe SDK directly.

Only "payment-stripe" communicates with Stripe.

This makes provider replacement possible without modifying consuming products.

---

11. Product Composition

An application declares the packages it needs.

For example:

Ecommerce Application
├── platform-core
├── identity
├── ecommerce-core
├── ecommerce-catalog
├── ecommerce-cart
├── ecommerce-orders
├── ecommerce-checkout
├── payment-core
├── payment-stripe
└── ecommerce-filament

A different application may use:

Subscription Application
├── platform-core
├── identity
├── subscription-core
├── payment-core
├── payment-stripe
└── subscription-filament

A custom Laravel application may use:

Custom Application
├── platform-core
├── payment-core
├── payment-stripe
└── custom-checkout

None of these applications needs "ecommerce-laravel".

This is the required outcome.

---

12. Application Distribution Packages

Product repositories may provide a convenient distribution package.

For example:

liberu/ecommerce

may depend on:

liberu/ecommerce-core
liberu/ecommerce-catalog
liberu/ecommerce-cart
liberu/ecommerce-orders
liberu/ecommerce-checkout
liberu/payment-core

This is an aggregate package.

It provides convenience without removing package independence.

Therefore:

Install everything:
    liberu/ecommerce

Install only catalog:
    liberu/ecommerce-catalog

Install checkout:
    liberu/ecommerce-checkout
    liberu/payment-core

The aggregate package must never contain the actual implementation.

It only composes packages.

---

13. Repository Applications

The root "*-laravel" repositories provide reference implementations and complete applications.

For example:

ecommerce-laravel
    ↓
Composer dependencies
    ↓
ecommerce packages
    ↓
shared Liberu packages

The root application contains:

- Laravel bootstrapping;
- environment configuration;
- application routes;
- authentication;
- panel configuration;
- application-level policies;
- package composition;
- deployment configuration.

It does not own reusable domain logic.

This ensures that the package can be extracted and consumed elsewhere without taking the entire Laravel application with it.

---

14. Filament Architecture

Filament is always an integration layer.

The architecture is:

Domain Package
        ↑
        │
Filament Package

Never:

Domain Package
        ↓
    Filament

The domain must not require Filament.

For example:

liberu/payment-core
        │
        ├── API consumer
        ├── Console consumer
        ├── Ecommerce
        ├── Billing
        └── payment-filament

The Filament implementation may be:

liberu/payment-filament

It provides:

- resources;
- pages;
- widgets;
- actions;
- forms;
- tables;
- navigation;
- permissions integration.

The payment domain remains completely independent.

The same rule applies to every product.

For example:

cms-core
    ↓
cms-filament

ecommerce-core
    ↓
ecommerce-filament

crm-core
    ↓
crm-filament

billing-core
    ↓
billing-filament

Filament packages may depend on multiple domain packages.

Domain packages must never depend on Filament.

---

15. Filament Application Composition

The root Laravel application defines the Filament panels.

Packages contribute functionality through explicit plugins.

For example:

Staff Panel
├── CMS Filament Plugin
├── Ecommerce Filament Plugin
├── CRM Filament Plugin
├── Billing Filament Plugin
├── Accounting Filament Plugin
└── Payment Filament Plugin

The application decides which plugins are installed and enabled.

A package may therefore be used without its Filament integration.

A Filament package may also be installed independently where required.

---

16. Runtime Enablement

Runtime enablement applies to application capabilities, not Composer package loading.

Composer determines:

What code is installed?

The application's module registry determines:

What installed capability is enabled?

Entitlements determine:

Who can use it?

The three states are:

Installed
    ↓
Composer/package deployment

Enabled
    ↓
Application capability activation

Entitled
    ↓
Site/brand/user availability

A package must not assume that installation means activation.

For example:

payment-stripe installed
        ↓
Stripe integration available
        ↓
Ecommerce payment capability enabled
        ↓
Stripe enabled for Site A

The same Stripe package can be installed once while different applications or sites enable different payment providers.

---

17. Capability Registry

Reusable capabilities should expose registries where multiple implementations are expected.

Examples:

PaymentGatewayRegistry
PaymentMethodRegistry
TaxProviderRegistry
ShippingProviderRegistry
StorageDriverRegistry
SearchDriverRegistry
NotificationChannelRegistry
AIProviderRegistry

The registry pattern is:

Contract
    ↓
Registry
    ↓
Implementations

For example:

PaymentGateway
    ↓
PaymentGatewayRegistry
    ├── Stripe
    ├── PayPal
    ├── Adyen
    └── Mollie

The consuming application selects the implementation.

The core capability remains provider-neutral.

---

18. Shared Data and Identity

Shared packages must not create hidden dependencies on product databases.

If multiple products need a common concept, that concept must be explicitly owned.

For example:

platform-identity
    ├── people
    ├── organisations
    └── identities

Then:

CRM
Ecommerce
Billing
Subscriptions

may reference the identity package.

They do not duplicate their own incompatible customer identity systems unless the domain genuinely requires a separate concept.

A shared concept must have one authoritative owner.

---

19. Database Ownership

Each package owns its own tables.

For example:

payment-core
    payments
    payment_transactions

payment-stripe
    stripe_payment_intents
    stripe_webhook_events

ecommerce-orders
    orders
    order_items

billing-invoices
    invoices
    invoice_items

A package must not create foreign keys directly into another product package unless the dependency is explicitly part of the package contract.

Shared identifiers should normally use ULIDs.

Cross-package references must use stable contracts and identifiers.

Provider-specific data belongs to the provider package.

For example:

payment-stripe
    stripe_customer_id
    stripe_payment_intent_id

must not be added to:

ecommerce-orders

The Ecommerce package stores the platform payment reference.

The Stripe package stores the Stripe-specific reference.

This preserves provider independence.

---

20. Package Dependency Rules

Dependencies must always point toward more reusable abstractions.

Preferred:

ecommerce-checkout
        ↓
payment-core
        ↓
payment-contracts

Incorrect:

payment-core
        ↓
ecommerce-checkout

Incorrect:

payment-core
        ↓
payment-stripe

Incorrect:

ecommerce-checkout
        ↓
Stripe SDK

Correct:

payment-stripe
        ↓
payment-contracts
        ↓
Stripe SDK

A lower-level reusable package must never depend on a higher-level product package.

---

21. Package Naming

Use the following naming convention:

liberu/{domain}-{capability}

Examples:

liberu/cms-core
liberu/cms-content
liberu/cms-media
liberu/cms-filament

liberu/ecommerce-core
liberu/ecommerce-cart
liberu/ecommerce-orders
liberu/ecommerce-filament

liberu/payment-contracts
liberu/payment-core
liberu/payment-stripe

liberu/customer-contracts
liberu/customer-core

liberu/ai-contracts
liberu/ai-core
liberu/ai-openai

The naming must communicate:

1. the domain;
2. the capability;
3. whether the package is core, contract, integration, or presentation.

---

22. Package Implementation Standard

Every new package must follow this process.

Step 1 — Identify the capability

Define exactly one primary responsibility.

Step 2 — Identify ownership

Determine which package owns the business concept.

Step 3 — Extract contracts

Create provider-neutral interfaces where implementations may vary.

Step 4 — Implement the core capability

Implement business logic without application-specific dependencies.

Step 5 — Extract integrations

Create one package per external provider where appropriate.

Step 6 — Implement presentation separately

Create Filament integrations without coupling the domain to Filament.

Step 7 — Add application composition

The "*-laravel" repository composes the packages.

Step 8 — Add runtime activation

Register the package capability with the application module/capability registry.

Step 9 — Test independent installation

Install the package in a clean Laravel application.

Step 10 — Test product integration

Verify that the package works within its primary Liberu product.

---

23. Example: CMS

"cms-laravel" should not become one monolithic package.

Instead:

cms-laravel
│
├── cms-core
├── cms-content
├── cms-pages
├── cms-media
├── cms-navigation
├── cms-publishing
├── cms-workflows
└── cms-filament

A custom Laravel application can use:

cms-core
cms-content
cms-pages

without installing the complete CMS distribution.

A different application can use:

cms-core
cms-content
cms-media

without Pages or Publishing.

The complete CMS application composes all packages.

---

24. Example: Ecommerce

"ecommerce-laravel" should similarly be composed:

ecommerce-core
ecommerce-catalog
ecommerce-pricing
ecommerce-cart
ecommerce-orders
ecommerce-checkout
ecommerce-payments
ecommerce-shipping
ecommerce-filament

The Ecommerce application may then consume:

payment-core
payment-stripe

but those packages remain completely independent.

The same payment packages can be consumed by:

ecommerce-laravel
billing-laravel
subscriptions-laravel
bookings-laravel
donations-laravel

This is the central principle of the Liberu architecture.

---

25. Example: Billing

Billing may be composed as:

billing-core
billing-invoices
billing-subscriptions
billing-recurring
billing-filament

Billing consumes:

payment-contracts
payment-core

and optionally:

payment-stripe
payment-paypal
payment-adyen

Billing therefore owns billing concepts.

Payment owns payment concepts.

Stripe owns Stripe concepts.

No package crosses these ownership boundaries.

---

26. Complete Example

A full Liberu Ecommerce deployment might be:

Application
│
├── platform-core
├── identity
├── permissions
│
├── cms-core
├── cms-content
├── cms-media
│
├── ecommerce-core
├── ecommerce-catalog
├── ecommerce-cart
├── ecommerce-orders
├── ecommerce-checkout
│
├── customer-core
│
├── payment-core
├── payment-stripe
│
├── shipping-core
├── shipping-dhl
│
├── tax-core
├── tax-uk
│
├── ecommerce-filament
├── cms-filament
└── payment-filament

Another application might be:

Application
│
├── platform-core
├── identity
├── billing-core
├── billing-invoices
├── payment-core
├── payment-stripe
└── billing-filament

Both applications reuse:

payment-core
payment-stripe

Neither needs the other application.

---

27. Repository and Package Lifecycle

The lifecycle is:

Repository
    ↓
Contains one or more packages
    ↓
Packages are independently versioned
    ↓
Applications compose packages
    ↓
Applications may provide aggregate packages

A package may later be moved to its own repository without changing its public architecture.

For example:

ecommerce-laravel/packages/payment-stripe

may initially be developed alongside Ecommerce.

When reuse increases:

payment-stripe

can move to:

liberu/payment-stripe

without changing the package API.

This makes repository boundaries an implementation and governance decision rather than an architectural limitation.

---

28. Required Architecture Rules

The following rules are mandatory.

Rule 1

A repository is not automatically a package.

Rule 2

A product is not automatically a capability.

Rule 3

Reusable capabilities must be extracted into independent packages.

Rule 4

External integrations must be independent provider packages.

Rule 5

Contracts must be provider-neutral.

Rule 6

Domain packages must not depend on Filament.

Rule 7

Filament integrations must be separate packages.

Rule 8

Applications compose packages; packages must not depend on applications.

Rule 9

Provider-specific implementation must never leak into consuming domains.

Rule 10

Shared functionality must have one authoritative implementation.

Rule 11

Cross-package communication must use explicit contracts, events, registries, or stable identifiers.

Rule 12

A package must be usable without installing an unrelated product repository.

---

29. Final Architecture

The final Liberu architecture is:

                         LIBERU PLATFORM
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
       Foundation Packages                 Domain Contracts
             │                                   │
             └─────────────────┬─────────────────┘
                               │
                    Reusable Capabilities
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
         Payments          Customers         Content
             │                 │                 │
       Provider Adapters   Domain Packages   CMS Packages
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                       Product Packages
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             CMS          Ecommerce           Billing
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                     Filament Integrations
                               │
                               ▼
                     Laravel Applications

The governing principle is:

«Liberu repositories are product ecosystems. Liberu Composer packages are reusable capabilities. Applications are compositions of those packages.»

Therefore, "cms-laravel" is not the CMS itself as one indivisible module. It is the reference application and package ecosystem that composes independent CMS packages.

Likewise, "ecommerce-laravel" is not the owner of payment processing. Ecommerce consumes the shared payment capability.

The payment architecture is:

payment-contracts
        ↓
payment-core
        ↓
payment-stripe
        ↓
Stripe

payment-core
        ↑
        ├── Ecommerce
        ├── Billing
        ├── Subscriptions
        ├── Bookings
        └── Any Laravel Application

This is the architecture Liberu should standardise on for all future development.

It gives Liberu three levels of reuse:

1. Package reuse
   Any Laravel application can consume a package.

2. Product reuse
   A product can compose multiple packages.

3. Platform reuse
   Multiple products can share the same underlying capabilities.

The result is a true composable Laravel ecosystem, rather than a collection of monolithic Laravel applications with duplicated implementations.
