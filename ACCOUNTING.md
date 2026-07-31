# Liberu Accounting

## Product Scope

**Purpose:** Auditable multi-entity financial accounting and reporting for Liberu products and independent organizations.
**Architecture:** Implement as modules under [MODULES.md](MODULES.md); financial interfaces follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines accounting behavior only.

## Outcomes

- Maintain balanced, traceable books from source transaction through financial statement.
- Support multi-entity, multi-currency, tax, period close, reconciliation, and controlled corrections.
- Integrate operational products without duplicating their source records.

## Module plan

| Module | Responsibilities |
|---|---|
| Accounting Core | Legal entities, books, fiscal calendars, currencies, dimensions, numbering, and policies |
| General Ledger | Chart of accounts, journals, postings, allocations, recurring journals, and balances |
| Receivables | Customers, invoices/credit notes, receipts, allocation, aging, collections, and write-offs |
| Payables | Suppliers, bills/credits, approvals, payment proposals, aging, and remittances |
| Banking | Accounts, statement imports/feeds, matching rules, reconciliation, transfers, and cash position |
| Tax | Codes, rates, jurisdictions, evidence, returns, adjustments, and tax-engine adapters |
| Assets | Asset register, capitalization, depreciation books, impairment, transfer, and disposal |
| Expenses | Claims, receipts, mileage, policy checks, approval, reimbursement, and posting |
| Inventory Accounting | Valuation, cost layers, landed cost, adjustments, and stock-to-ledger reconciliation |
| Project Accounting | Projects, budgets, time/cost capture, work in progress, revenue, and profitability |
| Payroll Accounting | Payroll imports, liabilities, journals, payments, reconciliation, and corrections |
| Consolidation | Intercompany rules, eliminations, currency translation, group close, and consolidation |
| Reporting | Trial balance, statements, ledgers, tax, cash flow, budgets, variance, and scheduled packs |
| Close | Period checklist, dependencies, approvals, locks, adjustments, evidence, and reopen controls |

## Required workflows

1. **Posting:** receive approved source transaction → validate period/currency/dimensions → create balanced journal → post atomically → update projections.
2. **Receivables:** invoice → receipt/import → allocate → reconcile → collect/write off/refund → report aging.
3. **Payables:** bill capture → duplicate/policy checks → approval → payment proposal → dual approval → execution/export → reconciliation.
4. **Bank reconciliation:** import statement → suggest matches → review exceptions → confirm → post fees/FX/adjustments.
5. **Period close:** complete subledgers → reconcile → adjustments → review statements → lock → consolidate; reopening requires privileged approval.

## Product requirements

- Use decimal monetary types, explicit currencies, configurable rounding, and immutable posted journals.
- Correct posted errors through reversals and replacement entries, never destructive edits.
- Support accrual/cash reporting, cost/profit centers, projects, departments, branches, and configurable dimensions.
- Track source module/type/identifier and provide drill-through without direct schema coupling.
- Support exchange rates, realized/unrealized gains, revaluation, translation, and historical rate policies.
- Provide imports/exports with dry run, mapping, balancing controls, idempotency, and exception reports.
- Enforce maker-checker approvals and segregation of duties for payments, journals, close, and configuration.

## Integrations

Billing, Ecommerce, CRM, Maintenance, payroll, banks/open banking, payment gateways, tax engines, expense capture, and document storage integrate through versioned events/adapters. Reconciliation detects missing, duplicate, and changed source transactions.

## Quality and control gates

- Property-test debit/credit balance, currency conversion, tax rounding, allocations, depreciation, consolidation, and reversals.
- Test concurrent numbering, duplicate imports, closed periods, backdated entries, approval bypass, and tenant/entity isolation.
- Provide immutable audit trails, configurable retention, encrypted bank/tax identifiers, and restricted financial exports.
- Reconcile every subledger to control accounts and expose unexplained differences operationally.

## Delivery phases

1. Core, General Ledger, Receivables, Payables, Banking, base reports, and close controls.
2. Tax, expenses, assets, budgets/dimensions, and operational integrations.
3. Inventory, project and payroll accounting, advanced cash/revenue workflows.
4. Multi-entity consolidation, advanced reporting, regional packs, and optimization.

## Definition of done

Books remain balanced and traceable under normal, correction, concurrency, import, close, and provider-failure scenarios; subledgers reconcile; permissions and approvals are enforced; reports reproduce their source balances. Each module becomes a GitHub epic.
