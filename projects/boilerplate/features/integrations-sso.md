# Boilerplate: Integrations SSO

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-sso`](../../../modules/source/liberusoftware--integrations-sso.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-integrations-sso` (`liberusoftware/integrations-sso`)  
**Application:** Boilerplate  
**Capability group:** Integrations SSO  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/integrations-sso.md](../core/integrations-sso.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

OIDC and SAML 2.0 SSO connections, metadata, ACS/SLO controllers, JIT user provisioning, enforcement middleware, SSRF guards, and Filament resources extending liberusoftware/integrations.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/integrations-sso` (v`1.1.0`).
- **Namespace:** `Liberu\Integrations\Sso\`.
- **Dependencies:** `illuminate/support, liberusoftware/integrations, liberusoftware/organizations-teams, liberusoftware/roles-permissions`.
- **Declared features:** SSO Integrations

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
