# Boilerplate: Users and Roles

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/users-roles`](../../../modules/source/liberusoftware--users-roles.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-users-roles` (`liberusoftware/users-roles`)  
**Application:** Boilerplate  
**Capability group:** Users and Roles  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/users-roles.md](../core/users-roles.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

Shared user authenticatable base model, role lookup service, user policies, migrations, and user factories.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/users-roles` (v`1.0.3`).
- **Namespace:** `Liberu\Foundation\UsersRoles\`.
- **Dependencies:** `illuminate/auth, illuminate/database, illuminate/support, spatie/laravel-permission, illuminate/contracts`.
- **Declared features:** Shared user model, Team-independent role lookup, User authorization policies

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
