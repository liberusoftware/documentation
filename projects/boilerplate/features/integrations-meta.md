# Boilerplate: Integrations Meta

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-meta`](../../../modules/source/liberusoftware--integrations-meta.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-integrations-meta` (`liberusoftware/integrations-meta`)  
**Application:** Boilerplate  
**Capability group:** Integrations Meta  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/integrations-meta.md](../core/integrations-meta.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

Facebook, Facebook Ads, Facebook Messenger, Instagram, and WhatsApp Business integration services, model, and Filament resource extending liberusoftware/integrations.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/integrations-meta` (v`1.1.0`).
- **Namespace:** `Liberu\Integrations\Meta\`.
- **Dependencies:** `illuminate/support, liberusoftware/integrations, liberusoftware/organizations-teams`.
- **Declared features:** Meta Integrations

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
