# Liberu: Revenue and Care Orchestration API

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-api`
**Core:** [Revenue and Care Orchestration](../core/revenue-and-care-orchestration.md)
**Feature:** [Revenue and Care Orchestration](../features/revenue-and-care-orchestration.md)

## Contract

Base path: `/api/v1/liberu/revenue-and-care-orchestration`. Use versioned OpenAPI 3.1 resources, explicit DTOs, Sanctum/service scopes, tenant/brand policy, RFC 9457 errors, bounded pagination, and `Idempotency-Key` for mutations.

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/health?customer_id={id}` | Read authorized health constellation and evidence links |
| `GET` | `/care-queue` | List prioritized sales/support/on-call work with safe reason codes |
| `GET` | `/outreach-eligibility?contact_id={id}&channel=voice` | Explain whether contact is eligible and return `next_contact_at` |
| `POST` | `/recovery-requests` | Request an owning CRM case from an incident/provisioning signal |
| `POST` | `/ai-recommendations/{id}/accept` | Accept an approved recommendation as a typed action |

The API never accepts a caller-supplied bypass or tenant context as authority. Response fields include source references, freshness, policy version, and non-sensitive reason codes; protected consent, infrastructure, and financial details are field-authorized. Slow projection rebuilds and provider-dependent actions return an operation resource with retry/reconciliation status.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#revenue-and-care-orchestration), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

<!-- observed-api-contract:end -->
