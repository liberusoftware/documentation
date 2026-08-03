# Accounting Flutter + Dart implementations

**Scope:** [Accounting](../ACCOUNTING.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Accounting project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-flutter`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [Flutter + Dart module standard](../../../modules/flutter/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 105 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                              | Package                                                  | Core                                              | API                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| [Account Reconciliations](account-reconciliations.md)               | module-accounting-account-reconciliations-flutter        | [Core](../core/account-reconciliations.md)        | [API](../api/account-reconciliations.md)        |
| [Accountant Workspace](accountant-workspace.md)                     | module-accounting-accountant-workspace-flutter           | [Core](../core/accountant-workspace.md)           | [API](../api/accountant-workspace.md)           |
| [Accounting Automation Pack](accounting-automation-pack.md)         | module-accounting-accounting-automation-pack-flutter     | [Core](../core/accounting-automation-pack.md)     | [API](../api/accounting-automation-pack.md)     |
| [Accounting Copilot](accounting-copilot.md)                         | module-accounting-accounting-copilot-flutter             | [Core](../core/accounting-copilot.md)             | [API](../api/accounting-copilot.md)             |
| [Accounting Core](accounting-core.md)                               | module-accounting-accounting-core-flutter                | [Core](../core/accounting-core.md)                | [API](../api/accounting-core.md)                |
| [Accounting Periods](accounting-periods.md)                         | module-accounting-accounting-periods-flutter             | [Core](../core/accounting-periods.md)             | [API](../api/accounting-periods.md)             |
| [Accounting Policies](accounting-policies.md)                       | module-accounting-accounting-policies-flutter            | [Core](../core/accounting-policies.md)            | [API](../api/accounting-policies.md)            |
| [Accounting Review](accounting-review.md)                           | module-accounting-accounting-review-flutter              | [Core](../core/accounting-review.md)              | [API](../api/accounting-review.md)              |
| [Accounts Payable](accounts-payable.md)                             | module-accounting-accounts-payable-flutter               | [Core](../core/accounts-payable.md)               | [API](../api/accounts-payable.md)               |
| [Accounts Receivable](accounts-receivable.md)                       | module-accounting-accounts-receivable-flutter            | [Core](../core/accounts-receivable.md)            | [API](../api/accounts-receivable.md)            |
| [Anomaly Detection](anomaly-detection.md)                           | module-accounting-anomaly-detection-flutter              | [Core](../core/anomaly-detection.md)              | [API](../api/anomaly-detection.md)              |
| [Asset Events](asset-events.md)                                     | module-accounting-asset-events-flutter                   | [Core](../core/asset-events.md)                   | [API](../api/asset-events.md)                   |
| [Audit Support](audit-support.md)                                   | module-accounting-audit-support-flutter                  | [Core](../core/audit-support.md)                  | [API](../api/audit-support.md)                  |
| [Bank Accounts](bank-accounts.md)                                   | module-accounting-bank-accounts-flutter                  | [Core](../core/bank-accounts.md)                  | [API](../api/bank-accounts.md)                  |
| [Bank Feeds](bank-feeds.md)                                         | module-accounting-bank-feeds-flutter                     | [Core](../core/bank-feeds.md)                     | [API](../api/bank-feeds.md)                     |
| [Bank Reconciliation](bank-reconciliation.md)                       | module-accounting-bank-reconciliation-flutter            | [Core](../core/bank-reconciliation.md)            | [API](../api/bank-reconciliation.md)            |
| [Bank Rules](bank-rules.md)                                         | module-accounting-bank-rules-flutter                     | [Core](../core/bank-rules.md)                     | [API](../api/bank-rules.md)                     |
| [Bill Payments](bill-payments.md)                                   | module-accounting-bill-payments-flutter                  | [Core](../core/bill-payments.md)                  | [API](../api/bill-payments.md)                  |
| [Branch And Location Accounting](branch-and-location-accounting.md) | module-accounting-branch-and-location-accounting-flutter | [Core](../core/branch-and-location-accounting.md) | [API](../api/branch-and-location-accounting.md) |
| [Budgets](budgets.md)                                               | module-accounting-budgets-flutter                        | [Core](../core/budgets.md)                        | [API](../api/budgets.md)                        |
| [Business Insights](business-insights.md)                           | module-accounting-business-insights-flutter              | [Core](../core/business-insights.md)              | [API](../api/business-insights.md)              |
| [Carbon Accounting](carbon-accounting.md)                           | module-accounting-carbon-accounting-flutter              | [Core](../core/carbon-accounting.md)              | [API](../api/carbon-accounting.md)              |
| [Cash Coding](cash-coding.md)                                       | module-accounting-cash-coding-flutter                    | [Core](../core/cash-coding.md)                    | [API](../api/cash-coding.md)                    |
| [Cash Collection Assistant](cash-collection-assistant.md)           | module-accounting-cash-collection-assistant-flutter      | [Core](../core/cash-collection-assistant.md)      | [API](../api/cash-collection-assistant.md)      |
| [Cash Flow Forecasting](cash-flow-forecasting.md)                   | module-accounting-cash-flow-forecasting-flutter          | [Core](../core/cash-flow-forecasting.md)          | [API](../api/cash-flow-forecasting.md)          |
| [Cash Position](cash-position.md)                                   | module-accounting-cash-position-flutter                  | [Core](../core/cash-position.md)                  | [API](../api/cash-position.md)                  |
| [Chart Of Accounts](chart-of-accounts.md)                           | module-accounting-chart-of-accounts-flutter              | [Core](../core/chart-of-accounts.md)              | [API](../api/chart-of-accounts.md)              |
| [Client Collaboration](client-collaboration.md)                     | module-accounting-client-collaboration-flutter           | [Core](../core/client-collaboration.md)           | [API](../api/client-collaboration.md)           |
| [Close Management](close-management.md)                             | module-accounting-close-management-flutter               | [Core](../core/close-management.md)               | [API](../api/close-management.md)               |
| [Coding Suggestions](coding-suggestions.md)                         | module-accounting-coding-suggestions-flutter             | [Core](../core/coding-suggestions.md)             | [API](../api/coding-suggestions.md)             |
| [Collections](collections.md)                                       | module-accounting-collections-flutter                    | [Core](../core/collections.md)                    | [API](../api/collections.md)                    |
| [Consolidation](consolidation.md)                                   | module-accounting-consolidation-flutter                  | [Core](../core/consolidation.md)                  | [API](../api/consolidation.md)                  |
| [Construction Tax](construction-tax.md)                             | module-accounting-construction-tax-flutter               | [Core](../core/construction-tax.md)               | [API](../api/construction-tax.md)               |
| [Contractor Compliance](contractor-compliance.md)                   | module-accounting-contractor-compliance-flutter          | [Core](../core/contractor-compliance.md)          | [API](../api/contractor-compliance.md)          |
| [Contractor Reporting](contractor-reporting.md)                     | module-accounting-contractor-reporting-flutter           | [Core](../core/contractor-reporting.md)           | [API](../api/contractor-reporting.md)           |
| [Corporate Cards](corporate-cards.md)                               | module-accounting-corporate-cards-flutter                | [Core](../core/corporate-cards.md)                | [API](../api/corporate-cards.md)                |
| [Credit Notes And Adjustments](credit-notes-and-adjustments.md)     | module-accounting-credit-notes-and-adjustments-flutter   | [Core](../core/credit-notes-and-adjustments.md)   | [API](../api/credit-notes-and-adjustments.md)   |
| [Custom Report Builder](custom-report-builder.md)                   | module-accounting-custom-report-builder-flutter          | [Core](../core/custom-report-builder.md)          | [API](../api/custom-report-builder.md)          |
| [Customer Payments](customer-payments.md)                           | module-accounting-customer-payments-flutter              | [Core](../core/customer-payments.md)              | [API](../api/customer-payments.md)              |
| [Customer Portal](customer-portal.md)                               | module-accounting-customer-portal-flutter                | [Core](../core/customer-portal.md)                | [API](../api/customer-portal.md)                |
| [Dashboards](dashboards.md)                                         | module-accounting-dashboards-flutter                     | [Core](../core/dashboards.md)                     | [API](../api/dashboards.md)                     |
| [Debt And Loans](debt-and-loans.md)                                 | module-accounting-debt-and-loans-flutter                 | [Core](../core/debt-and-loans.md)                 | [API](../api/debt-and-loans.md)                 |
| [Deposits And Clearing](deposits-and-clearing.md)                   | module-accounting-deposits-and-clearing-flutter          | [Core](../core/deposits-and-clearing.md)          | [API](../api/deposits-and-clearing.md)          |
| [Depreciation](depreciation.md)                                     | module-accounting-depreciation-flutter                   | [Core](../core/depreciation.md)                   | [API](../api/depreciation.md)                   |
| [Dimensions And Tracking](dimensions-and-tracking.md)               | module-accounting-dimensions-and-tracking-flutter        | [Core](../core/dimensions-and-tracking.md)        | [API](../api/dimensions-and-tracking.md)        |
| [Document Capture](document-capture.md)                             | module-accounting-document-capture-flutter               | [Core](../core/document-capture.md)               | [API](../api/document-capture.md)               |
| [E Invoicing](e-invoicing.md)                                       | module-accounting-e-invoicing-flutter                    | [Core](../core/e-invoicing.md)                    | [API](../api/e-invoicing.md)                    |
| [Employee Expenses](employee-expenses.md)                           | module-accounting-employee-expenses-flutter              | [Core](../core/employee-expenses.md)              | [API](../api/employee-expenses.md)              |
| [Estimates And Quotes](estimates-and-quotes.md)                     | module-accounting-estimates-and-quotes-flutter           | [Core](../core/estimates-and-quotes.md)           | [API](../api/estimates-and-quotes.md)           |
| [Financial Master Data](financial-master-data.md)                   | module-accounting-financial-master-data-flutter          | [Core](../core/financial-master-data.md)          | [API](../api/financial-master-data.md)          |
| [Financial Statements](financial-statements.md)                     | module-accounting-financial-statements-flutter           | [Core](../core/financial-statements.md)           | [API](../api/financial-statements.md)           |
| [Fixed Assets](fixed-assets.md)                                     | module-accounting-fixed-assets-flutter                   | [Core](../core/fixed-assets.md)                   | [API](../api/fixed-assets.md)                   |
| [Forecasts](forecasts.md)                                           | module-accounting-forecasts-flutter                      | [Core](../core/forecasts.md)                      | [API](../api/forecasts.md)                      |
| [General Ledger](general-ledger.md)                                 | module-accounting-general-ledger-flutter                 | [Core](../core/general-ledger.md)                 | [API](../api/general-ledger.md)                 |
| [Goods And Service Receipts](goods-and-service-receipts.md)         | module-accounting-goods-and-service-receipts-flutter     | [Core](../core/goods-and-service-receipts.md)     | [API](../api/goods-and-service-receipts.md)     |
| [Intercompany](intercompany.md)                                     | module-accounting-intercompany-flutter                   | [Core](../core/intercompany.md)                   | [API](../api/intercompany.md)                   |
| [Inventory Accounting](inventory-accounting.md)                     | module-accounting-inventory-accounting-flutter           | [Core](../core/inventory-accounting.md)           | [API](../api/inventory-accounting.md)           |
| [Job Estimates](job-estimates.md)                                   | module-accounting-job-estimates-flutter                  | [Core](../core/job-estimates.md)                  | [API](../api/job-estimates.md)                  |
| [Journal Approvals](journal-approvals.md)                           | module-accounting-journal-approvals-flutter              | [Core](../core/journal-approvals.md)              | [API](../api/journal-approvals.md)              |
| [Kpi And Goals](kpi-and-goals.md)                                   | module-accounting-kpi-and-goals-flutter                  | [Core](../core/kpi-and-goals.md)                  | [API](../api/kpi-and-goals.md)                  |
| [Leases](leases.md)                                                 | module-accounting-leases-flutter                         | [Core](../core/leases.md)                         | [API](../api/leases.md)                         |
| [Management Reporting](management-reporting.md)                     | module-accounting-management-reporting-flutter           | [Core](../core/management-reporting.md)           | [API](../api/management-reporting.md)           |
| [Matching Intelligence](matching-intelligence.md)                   | module-accounting-matching-intelligence-flutter          | [Core](../core/matching-intelligence.md)          | [API](../api/matching-intelligence.md)          |
| [Migration Framework](migration-framework.md)                       | module-accounting-migration-framework-flutter            | [Core](../core/migration-framework.md)            | [API](../api/migration-framework.md)            |
| [Mileage](mileage.md)                                               | module-accounting-mileage-flutter                        | [Core](../core/mileage.md)                        | [API](../api/mileage.md)                        |
| [Multi Currency](multi-currency.md)                                 | module-accounting-multi-currency-flutter                 | [Core](../core/multi-currency.md)                 | [API](../api/multi-currency.md)                 |
| [Multi Entity](multi-entity.md)                                     | module-accounting-multi-entity-flutter                   | [Core](../core/multi-entity.md)                   | [API](../api/multi-entity.md)                   |
| [Opening Balances](opening-balances.md)                             | module-accounting-opening-balances-flutter               | [Core](../core/opening-balances.md)               | [API](../api/opening-balances.md)               |
| [Operational Reports](operational-reports.md)                       | module-accounting-operational-reports-flutter            | [Core](../core/operational-reports.md)            | [API](../api/operational-reports.md)            |
| [Payment Reconciliation](payment-reconciliation.md)                 | module-accounting-payment-reconciliation-flutter         | [Core](../core/payment-reconciliation.md)         | [API](../api/payment-reconciliation.md)         |
| [Payroll Integration](payroll-integration.md)                       | module-accounting-payroll-integration-flutter            | [Core](../core/payroll-integration.md)            | [API](../api/payroll-integration.md)            |
| [Payroll Journals](payroll-journals.md)                             | module-accounting-payroll-journals-flutter               | [Core](../core/payroll-journals.md)               | [API](../api/payroll-journals.md)               |
| [Payroll Liabilities](payroll-liabilities.md)                       | module-accounting-payroll-liabilities-flutter            | [Core](../core/payroll-liabilities.md)            | [API](../api/payroll-liabilities.md)            |
| [Payroll Payments](payroll-payments.md)                             | module-accounting-payroll-payments-flutter               | [Core](../core/payroll-payments.md)               | [API](../api/payroll-payments.md)               |
| [Product And Service Items](product-and-service-items.md)           | module-accounting-product-and-service-items-flutter      | [Core](../core/product-and-service-items.md)      | [API](../api/product-and-service-items.md)      |
| [Project Billing](project-billing.md)                               | module-accounting-project-billing-flutter                | [Core](../core/project-billing.md)                | [API](../api/project-billing.md)                |
| [Project Costing](project-costing.md)                               | module-accounting-project-costing-flutter                | [Core](../core/project-costing.md)                | [API](../api/project-costing.md)                |
| [Project Profitability](project-profitability.md)                   | module-accounting-project-profitability-flutter          | [Core](../core/project-profitability.md)          | [API](../api/project-profitability.md)          |
| [Projects And Jobs](projects-and-jobs.md)                           | module-accounting-projects-and-jobs-flutter              | [Core](../core/projects-and-jobs.md)              | [API](../api/projects-and-jobs.md)              |
| [Purchase Orders](purchase-orders.md)                               | module-accounting-purchase-orders-flutter                | [Core](../core/purchase-orders.md)                | [API](../api/purchase-orders.md)                |
| [Purchase Requisitions](purchase-requisitions.md)                   | module-accounting-purchase-requisitions-flutter          | [Core](../core/purchase-requisitions.md)          | [API](../api/purchase-requisitions.md)          |
| [Quickbooks Online Migration](quickbooks-online-migration.md)       | module-accounting-quickbooks-online-migration-flutter    | [Core](../core/quickbooks-online-migration.md)    | [API](../api/quickbooks-online-migration.md)    |
| [Receipt Management](receipt-management.md)                         | module-accounting-receipt-management-flutter             | [Core](../core/receipt-management.md)             | [API](../api/receipt-management.md)             |
| [Recurring Transactions](recurring-transactions.md)                 | module-accounting-recurring-transactions-flutter         | [Core](../core/recurring-transactions.md)         | [API](../api/recurring-transactions.md)         |
| [Regional Packs](regional-packs.md)                                 | module-accounting-regional-packs-flutter                 | [Core](../core/regional-packs.md)                 | [API](../api/regional-packs.md)                 |
| [Reimbursements](reimbursements.md)                                 | module-accounting-reimbursements-flutter                 | [Core](../core/reimbursements.md)                 | [API](../api/reimbursements.md)                 |
| [Revenue Recognition](revenue-recognition.md)                       | module-accounting-revenue-recognition-flutter            | [Core](../core/revenue-recognition.md)            | [API](../api/revenue-recognition.md)            |
| [Sage Accounting Migration](sage-accounting-migration.md)           | module-accounting-sage-accounting-migration-flutter      | [Core](../core/sage-accounting-migration.md)      | [API](../api/sage-accounting-migration.md)      |
| [Sales Invoicing](sales-invoicing.md)                               | module-accounting-sales-invoicing-flutter                | [Core](../core/sales-invoicing.md)                | [API](../api/sales-invoicing.md)                |
| [Sales Orders](sales-orders.md)                                     | module-accounting-sales-orders-flutter                   | [Core](../core/sales-orders.md)                   | [API](../api/sales-orders.md)                   |
| [Sales Tax And Gst](sales-tax-and-gst.md)                           | module-accounting-sales-tax-and-gst-flutter              | [Core](../core/sales-tax-and-gst.md)              | [API](../api/sales-tax-and-gst.md)              |
| [Spreadsheet Migration](spreadsheet-migration.md)                   | module-accounting-spreadsheet-migration-flutter          | [Core](../core/spreadsheet-migration.md)          | [API](../api/spreadsheet-migration.md)          |
| [Supplier Bills](supplier-bills.md)                                 | module-accounting-supplier-bills-flutter                 | [Core](../core/supplier-bills.md)                 | [API](../api/supplier-bills.md)                 |
| [Supplier Portal](supplier-portal.md)                               | module-accounting-supplier-portal-flutter                | [Core](../core/supplier-portal.md)                | [API](../api/supplier-portal.md)                |
| [Tax Core](tax-core.md)                                             | module-accounting-tax-core-flutter                       | [Core](../core/tax-core.md)                       | [API](../api/tax-core.md)                       |
| [Tax Returns](tax-returns.md)                                       | module-accounting-tax-returns-flutter                    | [Core](../core/tax-returns.md)                    | [API](../api/tax-returns.md)                    |
| [Three Way Matching](three-way-matching.md)                         | module-accounting-three-way-matching-flutter             | [Core](../core/three-way-matching.md)             | [API](../api/three-way-matching.md)             |
| [Time Tracking](time-tracking.md)                                   | module-accounting-time-tracking-flutter                  | [Core](../core/time-tracking.md)                  | [API](../api/time-tracking.md)                  |
| [Transfers](transfers.md)                                           | module-accounting-transfers-flutter                      | [Core](../core/transfers.md)                      | [API](../api/transfers.md)                      |
| [Vat](vat.md)                                                       | module-accounting-vat-flutter                            | [Core](../core/vat.md)                            | [API](../api/vat.md)                            |
| [Withholding Tax](withholding-tax.md)                               | module-accounting-withholding-tax-flutter                | [Core](../core/withholding-tax.md)                | [API](../api/withholding-tax.md)                |
| [Workforce Costing](workforce-costing.md)                           | module-accounting-workforce-costing-flutter              | [Core](../core/workforce-costing.md)              | [API](../api/workforce-costing.md)              |
| [Workpapers](workpapers.md)                                         | module-accounting-workpapers-flutter                     | [Core](../core/workpapers.md)                     | [API](../api/workpapers.md)                     |
| [Xero Migration](xero-migration.md)                                 | module-accounting-xero-migration-flutter                 | [Core](../core/xero-migration.md)                 | [API](../api/xero-migration.md)                 |
| [Year End](year-end.md)                                             | module-accounting-year-end-flutter                       | [Core](../core/year-end.md)                       | [API](../api/year-end.md)                       |
