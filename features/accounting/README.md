# Accounting Feature Specifications

**Source:** [ACCOUNTING.md](../../ACCOUNTING.md)  
**Architecture:** [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md) · [DOCUMENTATION.md](../../DOCUMENTATION.md)

Each file defines one independent module. Modules remain independently installable, testable, versioned, and presentation-neutral.

## Accounting foundation modules

- [Accounting Core](accounting-core.md) — `accounting-core`
- [Financial Master Data](financial-master-data.md) — `accounting-financial-master-data`
- [Chart of Accounts](chart-of-accounts.md) — `accounting-chart-of-accounts`
- [General Ledger](general-ledger.md) — `accounting-general-ledger`
- [Dimensions and Tracking](dimensions-and-tracking.md) — `accounting-dimensions-and-tracking`
- [Opening Balances](opening-balances.md) — `accounting-opening-balances`
- [Recurring Transactions](recurring-transactions.md) — `accounting-recurring-transactions`
- [Accounting Periods](accounting-periods.md) — `accounting-periods`
- [Accounting Policies](accounting-policies.md) — `accounting-policies`

## Sales and receivables modules

- [Estimates and Quotes](estimates-and-quotes.md) — `accounting-estimates-and-quotes`
- [Sales Orders](sales-orders.md) — `accounting-sales-orders`
- [Sales Invoicing](sales-invoicing.md) — `accounting-sales-invoicing`
- [Credit Notes and Adjustments](credit-notes-and-adjustments.md) — `accounting-credit-notes-and-adjustments`
- [Customer Payments](customer-payments.md) — `accounting-customer-payments`
- [Accounts Receivable](accounts-receivable.md) — `accounting-accounts-receivable`
- [Collections](collections.md) — `accounting-collections`
- [Customer Portal](customer-portal.md) — `accounting-customer-portal`

## Purchasing and payables modules

- [Purchase Requisitions](purchase-requisitions.md) — `accounting-purchase-requisitions`
- [Purchase Orders](purchase-orders.md) — `accounting-purchase-orders`
- [Goods and Service Receipts](goods-and-service-receipts.md) — `accounting-goods-and-service-receipts`
- [Supplier Bills](supplier-bills.md) — `accounting-supplier-bills`
- [Three-Way Matching](three-way-matching.md) — `accounting-three-way-matching`
- [Accounts Payable](accounts-payable.md) — `accounting-accounts-payable`
- [Bill Payments](bill-payments.md) — `accounting-bill-payments`
- [Supplier Portal](supplier-portal.md) — `accounting-supplier-portal`
- [Contractor Compliance](contractor-compliance.md) — `accounting-contractor-compliance`

## Capture, expenses, cards, time, and mileage modules

- [Document Capture](document-capture.md) — `accounting-document-capture`
- [Receipt Management](receipt-management.md) — `accounting-receipt-management`
- [Employee Expenses](employee-expenses.md) — `accounting-employee-expenses`
- [Corporate Cards](corporate-cards.md) — `accounting-corporate-cards`
- [Mileage](mileage.md) — `accounting-mileage`
- [Time Tracking](time-tracking.md) — `accounting-time-tracking`
- [Reimbursements](reimbursements.md) — `accounting-reimbursements`

## Banking, treasury, and cash modules

- [Bank Accounts](bank-accounts.md) — `accounting-bank-accounts`
- [Bank Feeds](bank-feeds.md) — `accounting-bank-feeds`
- [Bank Rules](bank-rules.md) — `accounting-bank-rules`
- [Cash Coding](cash-coding.md) — `accounting-cash-coding`
- [Bank Reconciliation](bank-reconciliation.md) — `accounting-bank-reconciliation`
- [Deposits and Clearing](deposits-and-clearing.md) — `accounting-deposits-and-clearing`
- [Transfers](transfers.md) — `accounting-transfers`
- [Payment Reconciliation](payment-reconciliation.md) — `accounting-payment-reconciliation`
- [Cash Position](cash-position.md) — `accounting-cash-position`
- [Cash-Flow Forecasting](cash-flow-forecasting.md) — `accounting-cash-flow-forecasting`
- [Debt and Loans](debt-and-loans.md) — `accounting-debt-and-loans`

## Tax and regulatory modules

- [Tax Core](tax-core.md) — `accounting-tax-core`
- [Sales Tax and GST](sales-tax-and-gst.md) — `accounting-sales-tax-and-gst`
- [VAT](vat.md) — `accounting-vat`
- [Tax Returns](tax-returns.md) — `accounting-tax-returns`
- [E-Invoicing](e-invoicing.md) — `accounting-e-invoicing`
- [Withholding Tax](withholding-tax.md) — `accounting-withholding-tax`
- [Construction Tax](construction-tax.md) — `accounting-construction-tax`
- [Contractor Reporting](contractor-reporting.md) — `accounting-contractor-reporting`
- [Carbon Accounting](carbon-accounting.md) — `accounting-carbon-accounting`
- [Regional Packs](regional-packs.md) — `accounting-regional-packs`

## Inventory, assets, and specialized accounting modules

- [Inventory Accounting](inventory-accounting.md) — `accounting-inventory-accounting`
- [Product and Service Items](product-and-service-items.md) — `accounting-product-and-service-items`
- [Fixed Assets](fixed-assets.md) — `accounting-fixed-assets`
- [Depreciation](depreciation.md) — `accounting-depreciation`
- [Asset Events](asset-events.md) — `accounting-asset-events`
- [Leases](leases.md) — `accounting-leases`
- [Revenue Recognition](revenue-recognition.md) — `accounting-revenue-recognition`

## Projects, jobs, and profitability modules

- [Projects and Jobs](projects-and-jobs.md) — `accounting-projects-and-jobs`
- [Project Costing](project-costing.md) — `accounting-project-costing`
- [Project Billing](project-billing.md) — `accounting-project-billing`
- [Project Profitability](project-profitability.md) — `accounting-project-profitability`
- [Job Estimates](job-estimates.md) — `accounting-job-estimates`

## Payroll accounting modules

- [Payroll Integration](payroll-integration.md) — `accounting-payroll-integration`
- [Payroll Journals](payroll-journals.md) — `accounting-payroll-journals`
- [Payroll Liabilities](payroll-liabilities.md) — `accounting-payroll-liabilities`
- [Payroll Payments](payroll-payments.md) — `accounting-payroll-payments`
- [Workforce Costing](workforce-costing.md) — `accounting-workforce-costing`

## Planning, reporting, and advisory modules

- [Financial Statements](financial-statements.md) — `accounting-financial-statements`
- [Operational Reports](operational-reports.md) — `accounting-operational-reports`
- [Custom Report Builder](custom-report-builder.md) — `accounting-custom-report-builder`
- [Dashboards](dashboards.md) — `accounting-dashboards`
- [Budgets](budgets.md) — `accounting-budgets`
- [Forecasts](forecasts.md) — `accounting-forecasts`
- [Management Reporting](management-reporting.md) — `accounting-management-reporting`
- [Business Insights](business-insights.md) — `accounting-business-insights`
- [KPI and Goals](kpi-and-goals.md) — `accounting-kpi-and-goals`

## Multi-entity and international modules

- [Multi-Currency](multi-currency.md) — `accounting-multi-currency`
- [Multi-Entity](multi-entity.md) — `accounting-multi-entity`
- [Intercompany](intercompany.md) — `accounting-intercompany`
- [Consolidation](consolidation.md) — `accounting-consolidation`
- [Branch and Location Accounting](branch-and-location-accounting.md) — `accounting-branch-and-location-accounting`

## Close, controls, and accountant-practice modules

- [Close Management](close-management.md) — `accounting-close-management`
- [Account Reconciliations](account-reconciliations.md) — `accounting-account-reconciliations`
- [Journal Approvals](journal-approvals.md) — `accounting-journal-approvals`
- [Accounting Review](accounting-review.md) — `accounting-review`
- [Accountant Workspace](accountant-workspace.md) — `accounting-accountant-workspace`
- [Client Collaboration](client-collaboration.md) — `accounting-client-collaboration`
- [Workpapers](workpapers.md) — `accounting-workpapers`
- [Year End](year-end.md) — `accounting-year-end`
- [Audit Support](audit-support.md) — `accounting-audit-support`

## Automation and intelligence modules

- [Accounting Automation Pack](accounting-automation-pack.md) — `accounting-automation-pack`
- [Coding Suggestions](coding-suggestions.md) — `accounting-coding-suggestions`
- [Matching Intelligence](matching-intelligence.md) — `accounting-matching-intelligence`
- [Anomaly Detection](anomaly-detection.md) — `accounting-anomaly-detection`
- [Cash Collection Assistant](cash-collection-assistant.md) — `accounting-cash-collection-assistant`
- [Accounting Copilot](accounting-copilot.md) — `accounting-copilot`

## Migration modules

- [Migration Framework](migration-framework.md) — `accounting-migration-framework`
- [QuickBooks Online Migration](quickbooks-online-migration.md) — `accounting-quickbooks-online-migration`
- [Sage Accounting Migration](sage-accounting-migration.md) — `accounting-sage-accounting-migration`
- [Xero Migration](xero-migration.md) — `accounting-xero-migration`
- [Spreadsheet Migration](spreadsheet-migration.md) — `accounting-spreadsheet-migration`

