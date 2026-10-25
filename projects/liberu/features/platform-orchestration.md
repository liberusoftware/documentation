# Liberu: Platform Orchestration

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#platform-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent feature specification

**Domain module:** `module-liberu-platform-orchestration`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; does not replace Module Manager or any product module
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Platform Orchestration coordinates application manifests, enabled/installed/entitled states, cross-product capability declarations, workflow ownership, release gates, and safe composition. It does not own product records, package internals, authorization policy, or business workflows already owned by another project.

## New capabilities

- **Composition manifest:** declare applications, selected modules, adapters, themes, compatibility ranges, and deliberate exclusions.
- **Capability graph:** resolve required/optional capabilities and report missing, conflicting, or unsupported combinations before activation.
- **Lifecycle coordination:** distinguish install, enable, entitlement, activation, migration, disable, upgrade, and uninstall states.
- **Release gates:** collect compatibility, migration, security, test, and operator sign-off evidence for a composed release.
- **Ownership registry:** identify the authoritative module and escalation owner for cross-product workflows without copying its data.

## Boundaries and verification

The module stores only platform composition metadata and evidence. It consumes package manifests and public contracts, never private tables. Test collision detection, dependency cycles, capability resolution, authorization, tenant isolation, migration rehearsal, rollback, and safe failure when an optional module is unavailable.

## Canonical independent feature specification

**Domain module:** `module-liberu-platform-orchestration`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; does not replace Module Manager or any product module
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Platform Orchestration coordinates application manifests, enabled/installed/entitled states, cross-product capability declarations, workflow ownership, release gates, and safe composition. It does not own product records, package internals, authorization policy, or business workflows already owned by another project.

## New capabilities

- **Composition manifest:** declare applications, selected modules, adapters, themes, compatibility ranges, and deliberate exclusions.
- **Capability graph:** resolve required/optional capabilities and report missing, conflicting, or unsupported combinations before activation.
- **Lifecycle coordination:** distinguish install, enable, entitlement, activation, migration, disable, upgrade, and uninstall states.
- **Release gates:** collect compatibility, migration, security, test, and operator sign-off evidence for a composed release.
- **Ownership registry:** identify the authoritative module and escalation owner for cross-product workflows without copying its data.

## Boundaries and verification

The module stores only platform composition metadata and evidence. It consumes package manifests and public contracts, never private tables. Test collision detection, dependency cycles, capability resolution, authorization, tenant isolation, migration rehearsal, rollback, and safe failure when an optional module is unavailable.

## Canonical independent feature specification

**Domain module:** `module-liberu-platform-orchestration`
**Application:** Liberu Business Platform  
**Status:** New cross-product capability; does not replace Module Manager or any product module  
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Platform Orchestration coordinates application manifests, enabled/installed/entitled states, cross-product capability declarations, workflow ownership, release gates, and safe composition. It does not own product records, package internals, authorization policy, or business workflows already owned by another project.

## New capabilities

- **Composition manifest:** declare applications, selected modules, adapters, themes, compatibility ranges, and deliberate exclusions.
- **Capability graph:** resolve required/optional capabilities and report missing, conflicting, or unsupported combinations before activation.
- **Lifecycle coordination:** distinguish install, enable, entitlement, activation, migration, disable, upgrade, and uninstall states.
- **Release gates:** collect compatibility, migration, security, test, and operator sign-off evidence for a composed release.
- **Ownership registry:** identify the authoritative module and escalation owner for cross-product workflows without copying its data.

## Boundaries and verification

The module stores only platform composition metadata and evidence. It consumes package manifests and public contracts, never private tables. Test collision detection, dependency cycles, capability resolution, authorization, tenant isolation, migration rehearsal, rollback, and safe failure when an optional module is unavailable.
