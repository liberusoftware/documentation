# Accounting Feature Specifications

**Source:** [ACCOUNTING.md](../ACCOUNTING.md)  
**Architecture:** [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md) · [DOCUMENTATION.md](../ACCOUNTING.md)

Each file defines one independent module. Modules remain independently installable, testable, versioned, and presentation-neutral.

## Accounting foundation modules

- [Accounting Core](accounting-core.md) — `module-accounting-core`
- [Financial Master Data](financial-master-data.md) — `module-accounting-financial-master-data`
- [Chart of Accounts](chart-of-accounts.md) — `module-accounting-chart-of-accounts`
- [General Ledger](general-ledger.md) — `module-accounting-general-ledger`
- [Dimensions and Tracking](dimensions-and-tracking.md) — `module-accounting-dimensions-and-tracking`
- [Opening Balances](opening-balances.md) — `module-accounting-opening-balances`
- [Recurring Transactions](recurring-transactions.md) — `module-accounting-recurring-transactions`
- [Accounting Periods](accounting-periods.md) — `module-accounting-periods`
- [Accounting Policies](accounting-policies.md) — `module-accounting-policies`

## Sales and receivables modules

- [Estimates and Quotes](estimates-and-quotes.md) — `module-accounting-estimates-and-quotes`
- [Sales Orders](sales-orders.md) — `module-accounting-sales-orders`
- [Sales Invoicing](sales-invoicing.md) — `module-accounting-sales-invoicing`
- [Credit Notes and Adjustments](credit-notes-and-adjustments.md) — `module-accounting-credit-notes-and-adjustments`
- [Customer Payments](customer-payments.md) — `module-accounting-customer-payments`
- [Accounts Receivable](accounts-receivable.md) — `module-accounting-accounts-receivable`
- [Collections](collections.md) — `module-accounting-collections`
- [Customer Portal](customer-portal.md) — `module-accounting-customer-portal`

## Purchasing and payables modules

- [Purchase Requisitions](purchase-requisitions.md) — `module-accounting-purchase-requisitions`
- [Purchase Orders](purchase-orders.md) — `module-accounting-purchase-orders`
- [Goods and Service Receipts](goods-and-service-receipts.md) — `module-accounting-goods-and-service-receipts`
- [Supplier Bills](supplier-bills.md) — `module-accounting-supplier-bills`
- [Three-Way Matching](three-way-matching.md) — `module-accounting-three-way-matching`
- [Accounts Payable](accounts-payable.md) — `module-accounting-accounts-payable`
- [Bill Payments](bill-payments.md) — `module-accounting-bill-payments`
- [Supplier Portal](supplier-portal.md) — `module-accounting-supplier-portal`
- [Contractor Compliance](contractor-compliance.md) — `module-accounting-contractor-compliance`

## Capture, expenses, cards, time, and mileage modules

- [Document Capture](document-capture.md) — `module-accounting-document-capture`
- [Receipt Management](receipt-management.md) — `module-accounting-receipt-management`
- [Employee Expenses](employee-expenses.md) — `module-accounting-employee-expenses`
- [Corporate Cards](corporate-cards.md) — `module-accounting-corporate-cards`
- [Mileage](mileage.md) — `module-accounting-mileage`
- [Time Tracking](time-tracking.md) — `module-accounting-time-tracking`
- [Reimbursements](reimbursements.md) — `module-accounting-reimbursements`

## Banking, treasury, and cash modules

- [Bank Accounts](bank-accounts.md) — `module-accounting-bank-accounts`
- [Bank Feeds](bank-feeds.md) — `module-accounting-bank-feeds`
- [Bank Rules](bank-rules.md) — `module-accounting-bank-rules`
- [Cash Coding](cash-coding.md) — `module-accounting-cash-coding`
- [Bank Reconciliation](bank-reconciliation.md) — `module-accounting-bank-reconciliation`
- [Deposits and Clearing](deposits-and-clearing.md) — `module-accounting-deposits-and-clearing`
- [Transfers](transfers.md) — `module-accounting-transfers`
- [Payment Reconciliation](payment-reconciliation.md) — `module-accounting-payment-reconciliation`
- [Cash Position](cash-position.md) — `module-accounting-cash-position`
- [Cash-Flow Forecasting](cash-flow-forecasting.md) — `module-accounting-cash-flow-forecasting`
- [Debt and Loans](debt-and-loans.md) — `module-accounting-debt-and-loans`

## Tax and regulatory modules

- [Tax Core](tax-core.md) — `module-accounting-tax-core`
- [Sales Tax and GST](sales-tax-and-gst.md) — `module-accounting-sales-tax-and-gst`
- [VAT](vat.md) — `module-accounting-vat`
- [Tax Returns](tax-returns.md) — `module-accounting-tax-returns`
- [E-Invoicing](e-invoicing.md) — `module-accounting-e-invoicing`
- [Withholding Tax](withholding-tax.md) — `module-accounting-withholding-tax`
- [Construction Tax](construction-tax.md) — `module-accounting-construction-tax`
- [Contractor Reporting](contractor-reporting.md) — `module-accounting-contractor-reporting`
- [Carbon Accounting](carbon-accounting.md) — `module-accounting-carbon-accounting`
- [Regional Packs](regional-packs.md) — `module-accounting-regional-packs`

## Inventory, assets, and specialized accounting modules

- [Inventory Accounting](inventory-accounting.md) — `module-accounting-inventory-accounting`
- [Product and Service Items](product-and-service-items.md) — `module-accounting-product-and-service-items`
- [Fixed Assets](fixed-assets.md) — `module-accounting-fixed-assets`
- [Depreciation](depreciation.md) — `module-accounting-depreciation`
- [Asset Events](asset-events.md) — `module-accounting-asset-events`
- [Leases](leases.md) — `module-accounting-leases`
- [Revenue Recognition](revenue-recognition.md) — `module-accounting-revenue-recognition`

## Projects, jobs, and profitability modules

- [Projects and Jobs](projects-and-jobs.md) — `module-accounting-projects-and-jobs`
- [Project Costing](project-costing.md) — `module-accounting-project-costing`
- [Project Billing](project-billing.md) — `module-accounting-project-billing`
- [Project Profitability](project-profitability.md) — `module-accounting-project-profitability`
- [Job Estimates](job-estimates.md) — `module-accounting-job-estimates`

## Payroll accounting modules

- [Payroll Integration](payroll-integration.md) — `module-accounting-payroll-integration`
- [Payroll Journals](payroll-journals.md) — `module-accounting-payroll-journals`
- [Payroll Liabilities](payroll-liabilities.md) — `module-accounting-payroll-liabilities`
- [Payroll Payments](payroll-payments.md) — `module-accounting-payroll-payments`
- [Workforce Costing](workforce-costing.md) — `module-accounting-workforce-costing`

## Planning, reporting, and advisory modules

- [Financial Statements](financial-statements.md) — `module-accounting-financial-statements`
- [Operational Reports](operational-reports.md) — `module-accounting-operational-reports`
- [Custom Report Builder](custom-report-builder.md) — `module-accounting-custom-report-builder`
- [Dashboards](dashboards.md) — `module-accounting-dashboards`
- [Budgets](budgets.md) — `module-accounting-budgets`
- [Forecasts](forecasts.md) — `module-accounting-forecasts`
- [Management Reporting](management-reporting.md) — `module-accounting-management-reporting`
- [Business Insights](business-insights.md) — `module-accounting-business-insights`
- [KPI and Goals](kpi-and-goals.md) — `module-accounting-kpi-and-goals`

## Multi-entity and international modules

- [Multi-Currency](multi-currency.md) — `module-accounting-multi-currency`
- [Multi-Entity](multi-entity.md) — `module-accounting-multi-entity`
- [Intercompany](intercompany.md) — `module-accounting-intercompany`
- [Consolidation](consolidation.md) — `module-accounting-consolidation`
- [Branch and Location Accounting](branch-and-location-accounting.md) — `module-accounting-branch-and-location-accounting`

## Close, controls, and accountant-practice modules

- [Close Management](close-management.md) — `module-accounting-close-management`
- [Account Reconciliations](account-reconciliations.md) — `module-accounting-account-reconciliations`
- [Journal Approvals](journal-approvals.md) — `module-accounting-journal-approvals`
- [Accounting Review](accounting-review.md) — `module-accounting-review`
- [Accountant Workspace](accountant-workspace.md) — `module-accounting-accountant-workspace`
- [Client Collaboration](client-collaboration.md) — `module-accounting-client-collaboration`
- [Workpapers](workpapers.md) — `module-accounting-workpapers`
- [Year End](year-end.md) — `module-accounting-year-end`
- [Audit Support](audit-support.md) — `module-accounting-audit-support`

## Automation and intelligence modules

- [Accounting Automation Pack](accounting-automation-pack.md) — `module-accounting-automation-pack`
- [Coding Suggestions](coding-suggestions.md) — `module-accounting-coding-suggestions`
- [Matching Intelligence](matching-intelligence.md) — `module-accounting-matching-intelligence`
- [Anomaly Detection](anomaly-detection.md) — `module-accounting-anomaly-detection`
- [Cash Collection Assistant](cash-collection-assistant.md) — `module-accounting-cash-collection-assistant`
- [Accounting Copilot](accounting-copilot.md) — `module-accounting-copilot`

## Migration modules

- [Migration Framework](migration-framework.md) — `module-accounting-migration-framework`
- [QuickBooks Online Migration](quickbooks-online-migration.md) — `module-accounting-quickbooks-online-migration`
- [Sage Accounting Migration](sage-accounting-migration.md) — `module-accounting-sage-accounting-migration`
- [Xero Migration](xero-migration.md) — `module-accounting-xero-migration`
- [Spreadsheet Migration](spreadsheet-migration.md) — `module-accounting-spreadsheet-migration`
