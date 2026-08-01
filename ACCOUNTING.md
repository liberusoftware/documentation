# Liberu Accounting

## Product Scope

**Purpose:** Composable cloud accounting and financial-management platform for sole traders, growing businesses, accountants, and multi-entity organizations.
**Architecture:** Packages and provider adapters follow [MODULES.md](MODULES.md); APIs, connectors, and webhooks follow [API.md](API.md); business, accountant, approval, and portal interfaces follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md). Identity, organizations/teams, authorization, localization, currency value types, files, audit infrastructure, analytics adapters, integrations, and queues are not reimplemented here.

## 1. Outcomes

- Maintain balanced, traceable books from source evidence through statutory and management reports.
- Make everyday invoicing, purchasing, expenses, banking, tax, projects, payroll accounting, and close understandable to non-accountants.
- Give accountants controlled collaboration, review, correction, compliance, and multi-client tooling.
- Match commonly expected QuickBooks Online, Sage Accounting, and Xero capability families through independently installable modules.
- Integrate operational products and marketplace add-ons without duplicating source records or leaking provider concepts into the ledger.

## 2. Domain ownership

- Accounting owns books, accounts, journals, postings, subledgers, reconciliations, financial dimensions, close, and financial reports.
- Billing/Ecommerce own operational invoices, orders, payments, subscriptions, and stock operations; Accounting consumes governed postings and keeps source references.
- Payroll providers own payroll calculations and filings unless a dedicated Liberu Payroll product is installed; Accounting owns imported journals, liabilities, cash, and reconciliation.
- Boilerplate owns identity, tenant/team context, base currency types, generic files/import/export/integration infrastructure, and app lifecycle.
- Provider-specific bank, payment, tax, payroll, capture, and marketplace behavior belongs in separate adapters.

## 3. Accounting foundation modules

| Module | Responsibilities |
|---|---|
| Accounting Core | Legal entities, books, accounting basis, fiscal calendars, currencies, numbering, defaults, policies, and domain events |
| Financial Master Data | Customers, suppliers, items/services, accounts, tax profiles, payment terms, addresses, bank details references, lifecycle, and deduplication |
| Chart of Accounts | Account types, codes, hierarchies, control accounts, normal balances, templates, restrictions, localization, and lifecycle |
| General Ledger | Journals, balanced postings, recurring journals, reversals, corrections, allocations, accruals, prepayments, and balances |
| Dimensions and Tracking | Classes/categories, locations, departments, cost/profit centers, projects, tags, validation, allocations, and dimensional balances |
| Opening Balances | Migration date, account/customer/supplier/bank/item balances, outstanding documents, validation, approval, and reconciliation |
| Recurring Transactions | Templates, schedules, date/amount rules, approval, draft/automatic generation, exceptions, expiry, and history |
| Accounting Periods | Open/soft-close/hard-close states, transaction-date controls, module dependencies, locks, reopen approval, and evidence |
| Accounting Policies | Effective-dated recognition, capitalization, depreciation, FX, tax, rounding, write-off, materiality, and approval rules |

## 4. Sales and receivables modules

| Module | Responsibilities |
|---|---|
| Estimates and Quotes | Branded estimates/quotes, items, terms, versions, delivery, acceptance/decline, expiry, conversion, and history |
| Sales Orders | Accepted demand, allocation/fulfillment references, deposits, partial invoicing, status, cancellation, and Billing/Ecommerce integration |
| Sales Invoicing | Draft/approved/final invoices, line items, tax, discounts, deposits, recurring sources, branding, PDFs, delivery, and immutability |
| Credit Notes and Adjustments | Full/partial credits, reasons, approval, invoice allocation, refund/store-credit references, tax correction, and audit |
| Customer Payments | Receipts, payment links, gateway/bank references, deposits, undeposited funds, allocations, partial/overpayments, refunds, and reconciliation |
| Accounts Receivable | Customer subledger, open items, statements, aging, balances, unapplied cash, disputes, credit limits/holds, and control-account reconciliation |
| Collections | Reminder schedules, statement runs, promise-to-pay, disputes, late fees/interest policy, collection stages, write-offs, and agency adapters |
| Customer Portal | Estimates, invoices, credits, statements, payment links, payment history, disputes, documents, and communication preferences |

## 5. Purchasing and payables modules

| Module | Responsibilities |
|---|---|
| Purchase Requisitions | Requests, coding, budgets, attachments, approvals, sourcing handoff, conversion, and status |
| Purchase Orders | Supplier items, prices, quantities, delivery, approval, issue, receipts, partials, changes, closure, and commitments |
| Goods and Service Receipts | Receipts, service confirmation, quantities, variance, returns, attachments, inventory/project references, and accrual events |
| Supplier Bills | Draft/approved/posted bills, capture sources, line coding, tax, due dates, duplicate detection, matching, credits, and documents |
| Three-Way Matching | PO/receipt/bill matching, quantity/price/tax tolerances, exceptions, approval, partial matching, and evidence |
| Accounts Payable | Supplier subledger, open items, aging, balances, credits, disputes, holds, payment terms, and control-account reconciliation |
| Bill Payments | Payment proposals, due-date/discount optimization, bank details validation, maker-checker approval, files/APIs, remittances, and status |
| Supplier Portal | Profile/bank-change requests, purchase orders, invoices, statements, disputes, payment status, and secure documents |
| Contractor Compliance | Contractor records, status/evidence, withholding schemes, CIS/1099-style classifications, deductions, statements, and regional exports |

## 6. Capture, expenses, cards, time, and mileage modules

| Module | Responsibilities |
|---|---|
| Document Capture | Mobile/web/email upload, OCR/extraction adapters, supplier matching, line/tax capture, confidence, duplicate checks, review, and source retention |
| Receipt Management | Receipt inbox, matching to bank/card/expense/bill, missing-receipt requests, annotations, retention, and audit |
| Employee Expenses | Claims, categories, policy checks, per diem, attendees, projects/dimensions, approval, reimbursement, rejection, and posting |
| Corporate Cards | Card accounts, holders, feeds, controls references, transaction assignment, receipt collection, coding, approval, and reconciliation |
| Mileage | Vehicles/rates, trip capture/import, distance, business purpose, projects, policy, approval, reimbursement, and regional reporting |
| Time Tracking | Timesheets, timers, employees/contractors, customers/projects/tasks, billable/cost rates, approval, payroll/invoice export, and corrections |
| Reimbursements | Approved expense/mileage liabilities, payment batches, bank export/provider status, remittance, failure, and reconciliation |

## 7. Banking, treasury, and cash modules

| Module | Responsibilities |
|---|---|
| Bank Accounts | Bank/current/savings/credit/loan/cash accounts, ownership, currency, opening data, feeds, lifecycle, and restricted details |
| Bank Feeds | Consent/connections, institutions, account mapping, cursors, imports, duplicates, pending/posted state, health, and provider adapters |
| Bank Rules | Payee/text/amount/account conditions, split/category/tax/dimension actions, priority, suggestions/automation, testing, and history |
| Cash Coding | High-volume statement coding, bulk rules, tax/dimensions, payee creation policy, review, posting, and undo constraints |
| Bank Reconciliation | Suggested/exact matches, transfers, grouped receipts, fees/interest, adjustments, statement balance, exceptions, and sign-off |
| Deposits and Clearing | Undeposited funds, grouped deposits, payment-provider clearing, fees, payouts, timing differences, and reconciliation |
| Transfers | Inter-account/entity transfers, currency conversion, fees, in-transit state, paired posting, and reconciliation |
| Payment Reconciliation | Gateway/merchant settlement imports, gross-to-net fees/refunds/disputes, matching, missing items, and provider drift |
| Cash Position | Available/ledger balances, outstanding receipts/payments, committed cash, entity/currency views, and freshness |
| Cash-Flow Forecasting | Direct forecast, opening cash, receivable/payable timing, recurring items, scenarios, manual assumptions, variance, and confidence |
| Debt and Loans | Facilities, drawdowns, repayments, interest/fees, schedules, covenants, current/non-current split, and reconciliation |

## 8. Tax and regulatory modules

| Module | Responsibilities |
|---|---|
| Tax Core | Tax types/codes/rates, inclusive/exclusive treatment, jurisdictions, effective dates, exemptions, rounding, evidence, and control accounts |
| Sales Tax and GST | Registrations/nexus, destination/origin rules, taxable bases, liabilities, adjustments, return periods, and calculation adapters |
| VAT | Input/output VAT, reverse charge, partial exemption hooks, import/export, schemes, boxes, adjustments, digital records, and audit trail |
| Tax Returns | Return preparation, source reconciliation, diagnostics, review, approval, submission adapter, receipt/status, payment, and amendments |
| E-Invoicing | Structured invoice/credit formats, tax-ID validation, network/provider routing, signatures, delivery/receipt status, archival, and reconciliation |
| Withholding Tax | Rules, certificates, supplier/customer deductions, liabilities, remittance, statements, and regional filing adapters |
| Construction Tax | CIS-style subcontractor verification, deduction rates, statements, monthly returns, corrections, and filing adapters |
| Contractor Reporting | 1099-style thresholds, classifications, payee validation, forms, electronic filing adapters, corrections, and evidence |
| Carbon Accounting | Activity-data imports, factors, scopes/categories, calculations, evidence, estimates, dashboards, and export (optional) |
| Regional Packs | Country-specific tax, reports, document formats, filing calendars, account templates, terminology, and compliance tests |

## 9. Inventory, assets, and specialized accounting modules

| Module | Responsibilities |
|---|---|
| Inventory Accounting | Perpetual/periodic methods, valuation, cost layers, cost of sales, landed cost, adjustments, write-downs, and subledger reconciliation |
| Product and Service Items | Items/services, codes, purchase/sales descriptions, accounts, tax defaults, units, costs/prices, and Ecommerce references |
| Fixed Assets | Asset register, categories, acquisition, capitalization, components, locations/custodians, books, and supporting documents |
| Depreciation | Methods, conventions, useful life, residual value, schedules, runs, journals, tax books, and forecast |
| Asset Events | Transfer, improvement, revaluation, impairment, disposal, sale, write-off, gain/loss, and complete history |
| Leases | Lease records, payment schedules, right-of-use assets, liabilities, interest/depreciation, modifications, and disclosures (optional) |
| Revenue Recognition | Obligations/schedules, allocation references, deferred/accrued revenue, recognition runs, modifications, and reconciliation (optional) |

## 10. Projects, jobs, and profitability modules

| Module | Responsibilities |
|---|---|
| Projects and Jobs | Customers, project/job hierarchy, status, dates, managers, budgets, dimensions, source links, and lifecycle |
| Project Costing | Labor, expense, bill, inventory, subcontractor, overhead, commitments, WIP, cost-to-complete, and variance |
| Project Billing | Fixed fee, time/material, milestone, progress, retainer, billable time/expense, write-up/down, and invoice handoff |
| Project Profitability | Revenue, cost, margin, estimates, committed/actual, unbilled WIP, realization, dashboards, and drill-through |
| Job Estimates | Cost/revenue estimates, quantities/rates, versions, approvals, actual comparison, and estimate-at-completion |

## 11. Payroll accounting modules

| Module | Responsibilities |
|---|---|
| Payroll Integration | Provider/period/run identity, employee/contractor references, import validation, dimensions/projects, and provider adapters |
| Payroll Journals | Gross pay, taxes, deductions, benefits, employer costs, net pay, liabilities, allocation, posting, reversal, and corrections |
| Payroll Liabilities | Agency/payee balances, due dates, payments, allocations, exceptions, and reconciliation |
| Payroll Payments | Net-pay and liability batch references, approvals, bank/provider status, failures, and bank reconciliation |
| Workforce Costing | Time/payroll cost allocation to project, department, class/location, capitalization rules, and profitability reporting |

## 12. Planning, reporting, and advisory modules

| Module | Responsibilities |
|---|---|
| Financial Statements | Profit and loss, balance sheet, cash flow, changes in equity, comparative periods, dimensions, and drill-through |
| Operational Reports | Receivables/payables, sales/purchases, tax, bank, inventory, assets, expenses, projects, payroll, and exception reports |
| Custom Report Builder | Governed measures/dimensions, filters, grouping, formulas, comparisons, layouts, permissions, saved variants, and exports |
| Dashboards | Role-specific KPIs, widgets, periods, dimensions, targets, drill-through, refresh status, and sharing |
| Budgets | Annual/rolling budgets, accounts/dimensions/projects, imports, versions, approvals, phasing, actual comparison, and revisions |
| Forecasts | Driver/manual forecasts, scenarios, rolling periods, actual replacement, assumptions, approvals, and variance |
| Management Reporting | Report packs, narratives, charts, schedules, review, approval, PDF/spreadsheet delivery, and archive |
| Business Insights | Trends, ratios, working capital, profitability, cash runway, anomalies, benchmarks adapters, and explanations |
| KPI and Goals | Governed metrics, targets, owners, thresholds, periods, alerts, commentary, and history |

## 13. Multi-entity and international modules

| Module | Responsibilities |
|---|---|
| Multi-Currency | Transaction/functional/reporting currencies, rates, revaluation, realized/unrealized gains, historical rates, and reconciliation |
| Multi-Entity | Entity books, shared master-data policy, access, entity switching, separate periods/tax, standardized mappings, and reporting |
| Intercompany | Counterparties, trading rules, paired transactions, confirmations, settlement, differences, transfer-pricing evidence, and reconciliation |
| Consolidation | Group hierarchy, mappings, currency translation, intercompany eliminations, ownership/minority interests, adjustments, and group close |
| Branch and Location Accounting | Branch/location dimensions or books, local sequences/tax, allocations, performance, and statutory requirements |

## 14. Close, controls, and accountant-practice modules

| Module | Responsibilities |
|---|---|
| Close Management | Checklist, owners, dependencies, due dates, evidence, reconciliations, adjustments, review, certification, lock, and reopen |
| Account Reconciliations | GL account templates, source balances, supporting items, preparer/reviewer, aging, certification, and carry-forward |
| Journal Approvals | Journal sources/types, thresholds, preparer/reviewer, evidence, rejection, posting, and emergency controls |
| Accounting Review | Uncategorized/unreconciled items, exceptions, unusual balances, changes, overdue transactions, queries, resolution, and sign-off |
| Accountant Workspace | Client/entity portfolio, status, deadlines, alerts, access, notes, requests, recent changes, and drill-through |
| Client Collaboration | Secure document requests, questions, tasks, discussions, approvals, status, reminders, and evidence |
| Workpapers | Lead schedules, references, attachments, procedures, conclusions, preparer/reviewer, rollover, and export |
| Year End | Final adjustments, retained earnings/roll-forward, opening balances, statutory/tax handoff, lock, archive, and evidence |
| Audit Support | Read-only auditor access, samples, evidence requests, immutable exports, source drill-through, and access logs |

## 15. Automation and intelligence modules

| Module | Responsibilities |
|---|---|
| Accounting Automation Pack | Financial triggers/actions/recipes, approvals, schedules, simulation, idempotency, and generic Automation integration |
| Coding Suggestions | Account/tax/dimension/payee suggestions, confidence, explanations, user feedback, policy thresholds, and review |
| Matching Intelligence | Bank/document/payment/settlement matching suggestions, confidence, evidence, feedback, and safe automation thresholds |
| Anomaly Detection | Duplicates, unusual amounts/accounts/timing, control breaches, missing sequences, fraud indicators, and review queues |
| Cash Collection Assistant | Invoice-risk prioritization, reminder drafts/timing, promise tracking, policy, approval, and outcome feedback |
| Accounting Copilot | Permission-bounded search, explanations, summaries, report narratives, draft transactions, and explicit action confirmation |

AI output remains advisory unless an approved low-risk policy permits automation. Models cannot post journals, release payments, file returns, change bank details, close periods, or override controls without required authorization and approval.

## 16. Extension marketplace and integration packs

### 16.1 Accounting app marketplace

- Manage first/third-party apps, publishers, listings, categories, compatibility, scopes, data accessed, regions, pricing references, support, and uninstall behavior.
- Require signed/versioned releases, permission and financial-data review, webhook verification, credential rotation, audit, health, reconciliation, and vulnerability response.
- Support administrator allowlists, elevated-scope approval, trials/entitlements, installed-app inventory, activity logs, revocation, and data export/deletion.
- Apps cannot post directly to private tables; they use authorized contracts and preserve source identifiers, idempotency, balancing, and audit.

### 16.2 Common integration packs

| Pack | Common capabilities represented |
|---|---|
| Bank and Open Banking | Account consent, feeds, balances, transactions, payments, renewals, institution status, and reconciliation |
| Payments and Merchant Services | Payment links, receipts, fees, payouts, refunds, disputes, settlement imports, and clearing reconciliation |
| Capture and AP Automation | Dext/Hubdoc/AutoEntry/Bill-style receipt/bill capture, approval, supplier validation, payment, and document retention |
| Expense and Corporate Cards | Employee spend, cards, controls, receipts, mileage, reimbursement, and accounting synchronization |
| Payroll and HR | Employees/contractors, payroll summaries, journals, liabilities, payments, time, leave/cost allocations, and reconciliation |
| Ecommerce and POS | Customers, items, orders, tax, payments, fees, payouts, refunds, inventory/COGS, and daily-summary or transaction sync |
| Inventory and Order Management | Items, purchase/sales/stock operations, costs, valuation, landed cost, and subledger reconciliation |
| CRM and Professional Services | Customers, quotes, projects, time, expenses, milestones, invoices, payments, and profitability |
| Tax and Compliance | Calculation, filing, e-invoicing, tax-ID validation, digital records, receipts, and status reconciliation |
| Reporting and Planning | Governed data export, report packs, forecasts, scenarios, KPI dashboards, and write-back controls |
| Debt Collection | Accounts/invoices, communications, promises, disputes, collection status, fees, and payment results |
| Productivity | Spreadsheet import/export, email/document storage, calendar time capture, notifications, and approvals |

Vendor names illustrate expected interoperability; each provider remains a separate adapter and is not guaranteed merely by defining the contract.

## 17. Migration modules

| Module | Responsibilities |
|---|---|
| Migration Framework | Source inventory, mapping, dry run, transforms, validation, batches, resume, attachments, errors, counts, and reconciliation |
| QuickBooks Online Migration | Chart, classes/locations, contacts, items, invoices/bills/credits/payments, journals, bank data, projects, tax, attachments, and source IDs |
| Sage Accounting Migration | Chart/analysis types, contacts, products, sales/purchases, payments, bank, VAT/CIS evidence, currencies, budgets, attachments, and source IDs |
| Xero Migration | Chart/tracking categories, contacts, items, invoices/bills/credits/payments, bank, tax, assets, projects, expense claims, attachments, and source IDs |
| Spreadsheet Migration | Templates, guided mapping, opening/outstanding/detail modes, balancing, duplicate controls, validation, and reconciliation |

Migration never silently converts unbalanced or unsupported data. The cutover records source totals, outstanding subledgers, bank balances, tax balances, retained earnings, migration adjustments, and formal sign-off.

## 18. Required end-to-end workflows

1. **Quote to cash:** estimate → acceptance/sales order → invoice → online/bank receipt → allocation → bank/merchant reconciliation → collections or closure.
2. **Procure to pay:** requisition → approval → purchase order → receipt → captured bill → match/exception → payment proposal/approval → bank reconciliation.
3. **Expense to reimbursement:** capture receipt/mileage/time → code/project/tax → policy check → approval → liability/payment → bank/payroll reconciliation.
4. **Bank to books:** feed/import → deduplicate → rule/suggest match → review/cash code → reconcile statement → certify account.
5. **Tax to filing:** accumulate tax transactions → reconcile control accounts → diagnostics/adjustments → review/approve → submit → pay/refund → retain receipt.
6. **Project to profit:** estimate/budget → time/expense/bill/inventory cost → progress billing → WIP/revenue policy → cash → profitability.
7. **Payroll to ledger:** import run → validate totals/dimensions → post journal/liabilities → execute/reference payments → reconcile bank and agencies.
8. **Period close:** complete subledgers → reconcile bank/control/GL accounts → accruals/depreciation/FX/tax → review statements → certify/lock → reopen only by approval.
9. **Migration:** inventory/map → dry run → transform/import → balance subledgers/GL/bank/tax → validate reports → approve cutover → archive evidence.

Every workflow defines authoritative records, posting rules, states, actor/entity/book/period/currency context, approvals, segregation of duties, idempotency, source evidence, audit, exceptions, reconciliation, metrics, and recovery.

## 19. Shared product requirements

- Use precise decimal/minor-unit values with explicit currency and effective exchange rates; never binary floating point.
- Enforce double-entry balance atomically and immutable posted journals; correct through reversal and replacement rather than destructive edit.
- Preserve source module/provider/type/identifier, document evidence, posting derivation, approval, exchange rate, and tax calculation for drill-through.
- Reconcile receivable, payable, tax, bank, inventory, assets, payroll, projects/WIP, merchant clearing, gift/store credit, and intercompany subledgers to control accounts.
- Support cash/accrual views where legally meaningful, configurable dimensions, multiple currencies/entities, and regional terminology/packs.
- Make numbering, imports, feeds, captures, matching, posting, recurring generation, payments, filings, and provider webhooks idempotent and concurrency-safe.
- Offer versioned APIs/events, Filament plugins, theme-ready portals, bulk operations with preview, and permission-aware mobile capture.
- Require maker-checker/separation of duties for supplier bank changes, payments, journals, returns, write-offs, close/reopen, migration, app scopes, and configuration.

## 20. Security, compliance, and quality gates

- Enforce entity/book/period/account/dimension/record/field/action permissions across UI, API, reports, exports, search, automation, jobs, and apps.
- Encrypt bank, tax, payroll, identity, and provider credentials; redact sensitive documents and payment data from logs and analytics.
- Audit privileged reads, bank-detail changes, posting/correction, approvals, payment files/API calls, tax filings, exports, app access, and break-glass actions.
- Property-test balancing, allocations, tax/FX rounding, depreciation, inventory valuation, matching, consolidation, and reversals.
- Test sequence races, duplicate imports/feeds/webhooks, closed/backdated periods, partial payments, overpayments, multi-currency allocations, approval bypass, and tenant/entity isolation.
- Verify all reports reproduce ledger/subledger balances and retain metric/query version, parameters, period, currency, basis, and refresh time.
- Provide backup/restore drills, close/migration rollback guidance, provider outage behavior, health checks, failed-job replay, alerts, and finance runbooks.

## 21. Delivery phases

1. Core, Master Data, Chart, General Ledger, Dimensions, periods, Sales Invoicing, Receivables, Supplier Bills, Payables, Bank Accounts/Feeds/Reconciliation, base tax, and statements.
2. Estimates/Sales Orders, POs/receipts/matching, bill payments, customer/supplier portals, capture/receipts, expenses/cards/mileage/time, recurring transactions, and cash forecasting.
3. VAT/sales-tax returns, e-invoicing/regional packs, inventory/assets/projects/payroll accounting, budgets/forecasts, custom reports, and accountant workspace/close.
4. Multi-currency/entity, intercompany/consolidation, advanced planning/advisory, loans/leases/revenue recognition, workpapers/audit support, and marketplace.
5. Integration packs, QuickBooks/Sage/Xero migrations, intelligence modules, expanded regional compliance, and continuous reconciliation optimization.

## 22. Benchmark coverage and sources

- **QuickBooks Online:** estimates/invoices/payment links, expenses/bills/bill pay, receipt capture, bank feeds/rules/reconciliation, recurring transactions, inventory, projects/time/profitability, classes/locations, sales tax, payroll links, budgets/custom reports, accountant access, workflows, and batch operations.
- **Sage Accounting:** sales/purchase workflows, quotes, bank reconciliation, VAT/MTD and CIS-style compliance, receipt/invoice capture, inventory/reorder, multi-currency, budgets, cash-flow forecasting, customizable dimensional reports, payroll links, and accountant collaboration.
- **Xero:** invoicing/quotes, bills/purchase orders, bank feeds/rules/reconciliation, expenses/receipts, projects/time, inventory items, fixed assets, multi-currency, tax, payroll integrations, contacts, dashboards/reports, advisor collaboration, and app ecosystem.
- **Common marketplace add-ons:** AP automation, payment collection, payroll, time/expenses, ecommerce/POS, inventory, forecasting/reporting, tax/e-invoicing, debt collection, CRM/projects, cards, consolidation, and migration have explicit module or adapter homes.

Official reference starting points:

- [QuickBooks Online feature overview](https://quickbooks.intuit.com/global/features/)
- [QuickBooks Online product capabilities](https://quickbooks.intuit.com/online/)
- [QuickBooks Online reports](https://quickbooks.intuit.com/learn-support/en-us/help-article/purchase-orders/reports-included-quickbooks-online-subscription/L0s4KrGgr_US_en_US)
- [Sage Accounting](https://www.sage.com/en-gb/sage-business-cloud/sage-accounting/)
- [Sage Accounting reporting](https://www.sage.com/en-gb/sage-business-cloud/sage-accounting/features/reporting/)
- [Sage invoicing capabilities](https://www.sage.com/en-gb/accounting-software/invoicing/)
- [Xero accounting features](https://www.xero.com/us/accounting-software/all-features/)
- [Xero bank reconciliation](https://www.xero.com/us/accounting-software/reconcile-bank-transactions/)

These references establish expected capability coverage only. Liberu retains its own package boundaries, controls, terminology, and provider-neutral implementation.

## 23. Definition of done

Selected Accounting packages keep books balanced, immutable, permission-safe, and traceable through everyday entry, automation, corrections, close, migration, and provider failure. Subledgers reconcile to controls, reports reproduce ledger truth, payments and filings retain approvals/evidence, marketplace extensions remain governed, and each module row is suitable for a focused GitHub epic.
