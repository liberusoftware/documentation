# Implementing a product across technologies

The [repository map](REPOSITORIES.md) separates product ownership from delivery technology. Each of the 128 independent frontend/Inertia project hosts has a wayfinder issue with source links, a **technology-specific implementation method**, a **technical specification** summary, sequencing rules and a capability checklist. Durable per-technology specifications live under [wayfinders/](wayfinders/README.md). [The issue matrix](IMPLEMENTATION-ISSUES.md) provides direct links; [the machine-readable register](implementation-wayfinders.json) records the exact repository and issue URLs. The general publisher excludes existing `-laravel-filament` programmes. Ecommerce has a separate [Catering-only addition](ecommerce/catering-filament-issues.json), linked from its existing wayfinder; that addition does not revise unrelated programme decisions.

## Find the authoritative work

1. Open the product index and its `SOURCE-MAPPING.md`. Catalogue documents include historical spellings; counts of documents are not counts of independent packages or shipped features.
2. Find the domain owner and observed manifest identity before creating a package. If two spellings resolve to the same exact source identity, implement that boundary once. Similar names alone do not prove equivalence.
3. Read the core plan, then the API plan if the consumer uses HTTP, then the matching presentation plan. A missing source match is a research task, not permission to discard scope or invent a released contract.
4. Open this host's wayfinder issue and follow its **Implementation method** and **Technical specification** (or the matching [wayfinders/*.md](wayfinders/README.md) page) before writing code.
5. Select a complete user journey, settle dependencies, and implement it with its authorization, failure and recovery paths. Link tests and compatibility evidence before marking a checklist item complete.

The new `-laravel-api` product hosts provide the shared backend for independent clients; see [backend ownership and integration](../guides/LARAVEL-API-BACKENDS.md). The existing wayfinder publisher covers frontend/Inertia hosts and excludes these API backend repositories.

## Choose the delivery contract

| Host | Required boundary and acceptance | Specification |
| --- | --- | --- |
| Laravel Inertia React/Vue | Laravel routes, sessions and CSRF; typed allowlisted page props; server policies and revision conflict recovery. A separate HTTP API is optional for these pages. | [laravel-inertia-react](wayfinders/laravel-inertia-react.md) · [laravel-inertia-vue](wayfinders/laravel-inertia-vue.md) |
| Next.js React | Approved API/client contracts, server/client ownership, private rendering/cache boundaries and mutation invalidation. | [next-react](wayfinders/next-react.md) |
| Nuxt Vue | Approved API/client contracts, authenticated SSR/hydration isolation and private cache rules. | [nuxt-vue](wayfinders/nuxt-vue.md) |
| React Native Expo | Typed API, secure device credentials, validated deep links, touch/native accessibility, foreground refresh and explicit offline behavior. | [mobile-react](wayfinders/mobile-react.md) |
| Flutter mobile | Typed Dart API, secure device credentials, native widget semantics, account-isolated drafts and lifecycle/reconnect handling. | [mobile-flutter](wayfinders/mobile-flutter.md) |
| Dart mobile | A distinct mobile host/release using shared Flutter/API plans; verify touch navigation, platform lifecycle and secure local state independently. | [dart-mobile](wayfinders/dart-mobile.md) |
| Dart desktop | A distinct desktop host/release using shared Flutter/API plans; verify keyboard/focus, resizing, multi-window consistency, platform storage and safe printing/export. | [dart-desktop](wayfinders/dart-desktop.md) |

A client never becomes a second domain owner. Shared foundation capabilities remain in their authoritative modules. The host owns composition, routes, authentication context and cross-module workflows; themes own appearance and declared overrides. Keep installed `/modules` and `/themes` in host commits where applicable, including after promotion, with source releases and lockfiles updated together.

Each wayfinder issue body includes:

1. **Read first** — product, architecture and technology standard/runbook links, plus the durable [wayfinders](wayfinders/README.md) specification for that suffix.
2. **Implementation method** — ordered, technology-specific steps from skeleton audit through evidence.
3. **Technical specification** — host ownership, transport/session, package contracts, security/tenancy and verification/release rules for that surface.
4. **Capability checklist** — per-capability delivery slices with presentation-plan links.
5. **Acceptance criteria** — evidence required before checking a box.

## When to split a module issue

Create a focused child when a capability has an approved owner, specific dependencies, a bounded implementation outcome and testable acceptance. Include domain/API/presentation references, public contract changes, security/projection rules, migration impact, failure/retry behavior, operational evidence and exclusions. Link it from the technology wayfinder. Coordinate a shared core/API change in its owning repository rather than filing competing implementations in every client.

The initial wayfinders use per-capability checklists instead of generating thousands of speculative module tickets. Exact observed source aliases are grouped to avoid duplicate implementations. Catering has a focused issue in each non-Filament Ecommerce host because its privacy, revision and conversion requirements are concrete; those issues explicitly block implementation until its upstream boundary decisions are accepted. The existing Filament backlog is preserved, with a dedicated Catering epic and core/API/Filament/Livewire slices added separately.

## Delivery evidence

For each slice, show independent domain/contract/adapter tests, authorization and cross-tenant tests, audience-safe payloads/caches, accessible interaction, revision/conflict and retry evidence, a representative host journey, migration/upgrade behavior and operational recovery guidance. Follow the [coverage policy](../standards/TESTING.md#13-coverage-policy) and its documented extraction exception, plus [implementation evidence](../standards/IMPLEMENTATION-EVIDENCE.md). Verify a clean locked install and review tracked dependency diffs. Skeleton files and generated clients alone do not demonstrate product parity.

## Maintain the register

Regenerate technology specification pages and plan without writing to GitHub:

```bash
python tools/create_project_wayfinders.py --output /tmp/wayfinder-plan.json
```

Review the generated scope, then publish or refresh issues:

```bash
# Create any missing wayfinders (and Ecommerce Catering children); reuse existing titles
python tools/create_project_wayfinders.py --apply

# Also rewrite issue bodies to the current method + technical specification template
python tools/create_project_wayfinders.py --apply --sync
```

The publisher checks open and closed issues by exact stable title, excludes Filament and `-laravel-api` repositories, fails on duplicate wayfinders, writes [projects/wayfinders/](wayfinders/README.md), and saves progress after each repository. If interrupted, rerun to reuse created issues rather than duplicate them. Keep titles stable; inspect renamed issues manually before rerunning. Without `--sync`, existing issues are reused without overwriting bodies. The register records successful issue URLs; a final run must contain all 128 technology hosts before reporting completion.

For the Catering-only Filament extension, `python tools/add_catering_filament_issues.py` previews the scope and `--apply` creates missing issues and appends their links to existing wayfinder #925. It requires the non-Filament publication to be complete, reuses matching open or closed titles, and preserves the existing wayfinder body. See the [Catering issue register](ecommerce/catering-filament-issues.json).
