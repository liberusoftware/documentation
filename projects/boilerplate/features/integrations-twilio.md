# Boilerplate: Integrations Twilio

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-twilio`](../../../modules/source/liberusoftware--integrations-twilio.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-integrations-twilio` (`liberusoftware/integrations-twilio`)  
**Application:** Boilerplate  
**Capability group:** Integrations Twilio  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/integrations-twilio.md](../core/integrations-twilio.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

Twilio voice, SMS, OAuth provider, request signature verification middleware, call settings model, and Filament resource extending liberusoftware/integrations.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/integrations-twilio` (v`1.1.0`).
- **Namespace:** `Liberu\Integrations\Twilio\`.
- **Dependencies:** `illuminate/support, liberusoftware/integrations, liberusoftware/organizations-teams`.
- **Declared features:** Twilio Integrations

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
