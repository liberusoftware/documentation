# Boilerplate: Tenancy

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/tenancy`](../../../modules/source/liberusoftware--tenancy.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-tenancy` (`liberusoftware/tenancy`)  
**Application:** Boilerplate  
**Capability group:** Tenancy  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/tenancy.md](../core/tenancy.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

Shared Filament and Jetstream team tenancy with scoped runtime context, Eloquent isolation, queue context propagation, and Spatie permission team synchronization.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/tenancy` (v`1.2.3`).
- **Namespace:** `Liberu\Foundation\Tenancy\`.
- **Dependencies:** `illuminate/support, illuminate/database, filament/filament, laravel/jetstream, spatie/laravel-permission`.
- **Declared features:** Team context, Tenant model scopes, Request context, Permission team switching

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
