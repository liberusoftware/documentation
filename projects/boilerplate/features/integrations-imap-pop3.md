# Boilerplate: Integrations IMAP/POP3

<!-- source-reconciliation:start -->
**Source reconciliation:** [observed source modules](../SOURCE-MODULES.md). Observed identity: [`liberusoftware/integrations-imap-pop3`](../../../modules/source/liberusoftware--integrations-imap-pop3.md).
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-integrations-imap-pop3` (`liberusoftware/integrations-imap-pop3`)  
**Application:** Boilerplate  
**Capability group:** Integrations IMAP/POP3  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md)  
**Core technical spec:** [core/integrations-imap-pop3.md](../core/integrations-imap-pop3.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md)

## 1. Purpose

IMAP and POP3 inbound email integration services extending liberusoftware/integrations.

## 2. Scope and capabilities

- **Package identity:** `liberusoftware/integrations-imap-pop3` (v`1.0.0`).
- **Namespace:** `Liberu\Integrations\ImapPop3\`.
- **Dependencies:** `illuminate/support, liberusoftware/integrations`.
- **Declared features:** IMAP and POP3 Integrations

## 3. Security, privacy, and operations

- Enforce tenant/team isolation and server-side policy checks on all resources, controllers, and webhooks.
- Validate external URLs against SSRF and verify provider webhook signatures before processing payloads.
- Redact API keys, OAuth tokens, and secrets from logs, exceptions, and diagnostics.

## 4. Verification strategy

- Unit and feature tests verify allowed, denied, invalid, timeout/error, and tenant-isolation paths.
- Target 100% line coverage across `src/` with no `Legacy` namespaces or duplicated host code.
