# Boilerplate: Integrations Zernio

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-zernio`](../../../modules/source/liberusoftware--integrations-zernio.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-integrations-zernio` (`liberusoftware/integrations-zernio`)  
**Application:** Boilerplate  
**Capability group:** Integrations Zernio  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/integrations-zernio.md](../core/integrations-zernio.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

Zernio multi-channel social publishing, advertising, webhook controller, and tenant profile provisioning extending liberusoftware/integrations.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/integrations-zernio` (v`1.0.0`).
- **Namespace:** `Liberu\Integrations\Zernio\`.
- **Dependencies:** `illuminate/support, liberusoftware/integrations, liberusoftware/organizations-teams`.
- **Declared features:** Zernio Integrations

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
