# Liberu: Executive Insights

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#executive-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent feature specification

**Domain module:** `module-liberu-executive-insights`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Accounting, CRM, SAP Data and Intelligence, or product analytics modules
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Executive Insights provides governed cross-product metrics and read models for leadership and operations. Source systems remain authoritative; this module owns metric definitions, lineage, freshness, access, snapshots, and drill-through evidence.

## New capabilities

- **Metric registry:** define owner, formula, source contracts, dimensions, currency/timezone, freshness, and version.
- **Cross-product projections:** combine authorized events/read models for revenue, margin, cash, pipeline, service health, utilization, risk, and provider spend.
- **Evidence drill-through:** link each value to authorized source records, reconciliation status, and calculation version.
- **Decision snapshots:** capture period-closed metric packs with immutable lineage and approval status.
- **Data-quality operations:** surface freshness, missing dimensions, reconciliation failures, stale providers, and permission-filtered gaps.

## Boundaries and verification

The module never becomes the owner of invoices, customers, tickets, jobs, assets, or ledger records. Test formula/version changes, tenant and role filtering, stale data, missing sources, currency/timezone conversions, reconciliation, export redaction, and reproducible snapshots.

## Canonical independent feature specification

**Domain module:** `module-liberu-executive-insights`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Accounting, CRM, SAP Data and Intelligence, or product analytics modules
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Executive Insights provides governed cross-product metrics and read models for leadership and operations. Source systems remain authoritative; this module owns metric definitions, lineage, freshness, access, snapshots, and drill-through evidence.

## New capabilities

- **Metric registry:** define owner, formula, source contracts, dimensions, currency/timezone, freshness, and version.
- **Cross-product projections:** combine authorized events/read models for revenue, margin, cash, pipeline, service health, utilization, risk, and provider spend.
- **Evidence drill-through:** link each value to authorized source records, reconciliation status, and calculation version.
- **Decision snapshots:** capture period-closed metric packs with immutable lineage and approval status.
- **Data-quality operations:** surface freshness, missing dimensions, reconciliation failures, stale providers, and permission-filtered gaps.

## Boundaries and verification

The module never becomes the owner of invoices, customers, tickets, jobs, assets, or ledger records. Test formula/version changes, tenant and role filtering, stale data, missing sources, currency/timezone conversions, reconciliation, export redaction, and reproducible snapshots.

## Canonical independent feature specification

**Domain module:** `module-liberu-executive-insights`
**Application:** Liberu Business Platform  
**Status:** New cross-product capability; it does not replace Accounting, CRM, SAP Data and Intelligence, or product analytics modules  
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Executive Insights provides governed cross-product metrics and read models for leadership and operations. Source systems remain authoritative; this module owns metric definitions, lineage, freshness, access, snapshots, and drill-through evidence.

## New capabilities

- **Metric registry:** define owner, formula, source contracts, dimensions, currency/timezone, freshness, and version.
- **Cross-product projections:** combine authorized events/read models for revenue, margin, cash, pipeline, service health, utilization, risk, and provider spend.
- **Evidence drill-through:** link each value to authorized source records, reconciliation status, and calculation version.
- **Decision snapshots:** capture period-closed metric packs with immutable lineage and approval status.
- **Data-quality operations:** surface freshness, missing dimensions, reconciliation failures, stale providers, and permission-filtered gaps.

## Boundaries and verification

The module never becomes the owner of invoices, customers, tickets, jobs, assets, or ledger records. Test formula/version changes, tenant and role filtering, stale data, missing sources, currency/timezone conversions, reconciliation, export redaction, and reproducible snapshots.
