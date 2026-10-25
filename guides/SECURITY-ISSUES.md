# Handle module and application security issues

Use this guide to report, investigate, fix and disclose security defects across independent packages and their project-local copies. The [security policy](../architecture/SECURITY.md) defines reporting expectations; the [audit guide](SECURITY-AUDITS.md) defines repeatable checks and evidence. This is an operating procedure, not a claim that any particular package has passed an audit.

## Files each owning repository should maintain

| File or record | Required content |
| --- | --- |
| `SECURITY.md` at the repository root | Supported releases, a verified private reporting channel, response process and disclosure expectations |
| Package README and release notes | Canonical ownership, supported runtime/dependency versions, upgrade instructions and security contact link |
| Private issue/advisory record | Reproduction, impact, affected versions, owner, remediation and disclosure decisions |
| Audit evidence | Exact source/artifact/lockfile identities, tools, results, triage and retest evidence |
| Public advisory after coordination | Accurate affected/fixed ranges, mitigation, upgrade actions and safe technical explanation |

For this documentation repository use [its security policy](../architecture/SECURITY.md). For an application or package, use its own verified reporting channel, not the documentation repository's advisory form by default. If GitHub private reporting is unavailable, obtain the maintainer's established private contact. Do not invent an address, publish exploit details in a public issue, or place credentials in a report.

## Intake and triage

Collect the package/repository identity, exact version/commit, consuming application, relevant configuration, attacker prerequisites, affected users/tenants/data, reproducible steps and redacted evidence. Reproduce only in an authorized isolated environment with synthetic data. Describe expected versus observed behavior and distinguish a known advisory match from a confirmed exploitable application path.

Assign a maintainer and record severity, confidence, exploitability, exposure and remediation priority. Consider authorization boundaries, public access, data sensitivity and blast radius alongside a dependency advisory's score. A developer tool that executes in CI can affect release integrity even when absent from production runtime. If a finding is false positive or accepted risk, keep the reason, approver, review date and conditions that would reopen it.

## Contain exposure

For active compromise or exposed credentials, involve the owning incident responders immediately. Revoke/rotate affected credentials, invalidate sessions or signing material when appropriate, restrict the vulnerable endpoint/integration, and preserve useful logs and immutable artifacts. Coordinate dependent services when changing keys. Deleting a secret from the latest commit does not revoke copies in history, caches, artifacts or registry tarballs.

Use the application's tested recovery plan. Record whether a mitigation reduces exposure or fully removes the vulnerable path. Avoid disabling an entire shared control, such as tenant checks or signature verification, to bypass a failing workflow.

## Trace all package copies

Use [repository ownership records](MODULE-REPOSITORIES.md) and the [source inventory](../architecture/SOURCE-INVENTORY.md) to find independent releases, tracked application copies, local patches and divergent variants. Search application-owned services, routes, controllers and build assets too. For Ecommerce, preserve and inspect its [outside-module capabilities](../projects/ecommerce/SOURCE-APPLICATION.md).

Build a private impact matrix:

| Consumer | Installed/source identity | Reachable vulnerable path | Mitigation | Fixed release/deployment | Owner |
| --- | --- | --- | --- | --- | --- |
| `<application/environment>` | `<package version + commit + lockfile>` | `<confirmed / unconfirmed + evidence>` | `<control and verification>` | `<pending or verified version>` | `<team>` |

A fixed canonical package does not fix a tracked copy that was never upgraded. A lockfile can identify a nominal version while local source edits change its behavior. Include artifact comparison where tracked trees can drift. Check frontend bundles and long-lived workers, not only the PHP process that serves a request.

## Design and verify the fix

Fix shared behavior in the canonical owner and product integration in its application. Add a regression case that demonstrates the boundary, such as one tenant being unable to read another's resource, a replayed command being rejected, or an unsigned webhook being denied. Verify the permitted user journey still succeeds.

Review adjacent endpoints, alternate adapters, queues, imports, scheduled tasks and cached responses for the same weakness. Test server-side enforcement; hidden controls and disabled UI buttons are not authorization. Keep migrations and repair jobs repeatable and auditable. If exposure requires data correction, specify a separately reviewed recovery procedure and its validation.

Build and test the actual release artifact, rerun the relevant dependency/static/secret checks, and verify in affected consumers. For forks or older supported lines, track backports separately. Do not mark the issue resolved solely because a scanner stopped reporting it.

## Release and disclose

Coordinate a reviewed package release and application rollout through the [publishing runbook](PACKAGE-PUBLISHING.md). Keep sensitive remediation details private until the agreed release/disclosure point, while following the host's normal trusted review and release controls. Record affected/fixed ranges precisely, including variant packages with different names or histories.

After a verified fix is available, provide upgrade and mitigation instructions, relevant advisory identifiers, compatibility or migration effects, and any operator action such as token rotation. If no fix exists for an unsupported version, say so and provide a supported upgrade path. Avoid publishing personal data or weaponized payloads as proof.

Close each consumer only after deployment is verified, module copies and lockfiles agree, workers/assets are refreshed as required, and monitoring confirms expected behavior. Keep unresolved consumers visible. Conduct an incident review when warranted: record the cause, detection gap, preventive changes and accountable follow-up without storing sensitive incident material in public documentation.

## Security review areas for Liberu modules

| Boundary | Review and regression cases |
| --- | --- |
| Authentication and sessions | Login/refresh/logout, revoked sessions, expired credentials, cookie flags, CSRF and token audience |
| Authorization and tenancy | Cross-tenant IDs, bulk operations, exports, background jobs and administrative overrides |
| Inputs and output | Mass assignment, query construction, validation, rich text rendering and safe error responses |
| Integrations | Webhook signatures/replay, OAuth scopes/state, SSRF controls, outbound credentials and rate limits |
| Files and imports | Type/size limits, path traversal, archive extraction, malware scanning where needed and private storage access |
| Financial and enterprise actions | Approval separation, duplicate execution, legal transitions, ledger invariants and audit trail integrity |
| UI and caching | Server/client secret boundaries, authenticated SSR caches, unsafe HTML and browser storage exposure |
| Release pipeline | Registry identity, package contents, install hooks, protected credentials and immutable artifact/source mapping |

These are review prompts; the owning product defines its actual threat model, controls and test cases. Link results to the [audit evidence](SECURITY-AUDITS.md), rather than claiming these controls exist because they appear in a plan.
