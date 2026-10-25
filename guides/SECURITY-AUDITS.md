# Audit dependencies, source and released module copies

This guide defines a repeatable audit workflow for module maintainers and consuming applications. Combine it with [security issue handling](SECURITY-ISSUES.md), the [security policy](../architecture/SECURITY.md), [testing](../standards/TESTING.md), and [CI policy](../standards/CI.md). It documents checks to run in the owning code repository; it is not a vulnerability assessment of all Liberu packages.

## Choose scope and timing

Audit new dependencies and significant upgrades before adoption, changed security-sensitive code during review, and the exact artifact before release. Run scheduled dependency checks too, because new advisories can affect an unchanged lockfile. The owner should set a cadence and response deadlines based on deployment risk, and rerun relevant checks after a security report or publisher incident.

Record the repositories, commits, package versions, application lockfiles, runtime/tool versions, registries, environments and exclusions. Include development/build dependencies in release-system risk review. Check both the canonical module and the application: their resolved dependency graphs and exposure can differ.

For tracked installed modules, include a source/artifact comparison to detect local drift. For application-owned capabilities, inspect their actual paths even without package manifests. The [local-copy guide](MODULE-REPOSITORIES.md) explains ownership and clean comparison; Ecommerce's directory listing is not its full capability scope.

## Audit PHP dependencies

From the appropriate package or application root, inspect available commands/options for its installed Composer version:

```bash
composer --version
composer validate --strict
composer audit --help
composer audit --locked --format=json
```

A locked audit reviews the recorded graph; inspect installed dependencies separately when they may differ. Save the JSON result as restricted CI evidence and preserve the command's exit status. For a library that intentionally does not commit a lockfile, resolve a supported dependency set in a disposable environment and audit that set; do not claim a lockfile audit ran where no lockfile exists. Test the supported version matrix according to package policy.

Composer's audit consults configured advisory sources. Registry/network errors are incomplete scans, not clean results. Advisory and abandoned-package handling varies with the Composer version/configuration; inspect the report and the [official audit reference](https://getcomposer.org/doc/03-cli.md#audit). Do not weaken policy or suppress failures globally to make installation pass.

For each finding, use `composer why vendor/affected-package` and `composer prohibits vendor/affected-package <fixed-version>` with real values to find the dependency path and upgrade constraints. Review a targeted upgrade and its related changes, then run the consumer's compatibility, migration and security regression checks.

## Audit JavaScript dependencies

For an npm project with a valid committed lockfile, install in an isolated trusted environment using its declared runtime and then run:

```bash
npm --version
npm ci
npm audit --json
npm audit --omit=dev --json
npm audit signatures
```

Use the repository's actual package manager when it is not npm. The complete dependency scan and production-only scan answer different questions; retain both scopes. A browser build can incorporate development-time tooling, so excluding development dependencies alone does not cover release integrity.

`npm audit` reports dependency advisory matches. Its exit threshold can be configured, but a threshold does not hide findings from the report. Preserve nonzero exit statuses and triage them. `npm audit fix` changes the installation and can run installer behavior; review any proposed fix as a dependency change. Avoid an unattended `--force` upgrade that can cross compatibility boundaries. See the [npm audit command](https://docs.npmjs.com/cli/v11/commands/npm-audit/).

`npm audit signatures` checks available registry signatures and provenance for installed packages. Run it where the selected registry supports the required verification; document unsupported coverage and investigate failures. It is distinct from an advisory scan and does not establish that source code is safe. See [npm provenance verification](https://docs.npmjs.com/viewing-package-provenance/).

Use `npm explain <actual-package>` and `npm ls <actual-package>` to understand a transitive dependency before changing the direct owner. Rebuild and test the consumer after an upgrade; confirm peer compatibility and the exact locked versions deployed.

## Inspect source and the supply chain

| Check | Evidence and limitations |
| --- | --- |
| Static analysis and security review | Run declared tools and review relevant data/control flow; record rules and exclusions. Tool names in a plan are not executed results. |
| Authorization and isolation tests | Test denied and permitted operations across tenants/roles, API adapters, queues, imports and exports. |
| Secret scanning | Inspect working changes, history where relevant, release archives and build output with approved tooling; rotate exposed credentials. |
| Artifact inspection | Compare release commit to distributed files; check exports/autoloading, generated assets, install hooks and unintended data. |
| Workflow/registry review | Check maintainers, permissions, trusted publishers, action pinning, protected tags and secret exposure. |
| Container/runtime checks | Where deployed, scan base/runtime images and system packages; Composer/npm scans do not cover them. |
| Dynamic/manual review | Exercise the authorized staging threat scenarios and record actual results; dependency scanners do not test business rules. |

Install scripts, Composer plugins and CI actions can execute code. Review them before running untrusted checkouts; use isolated runners without production credentials. Diagnostic installs with scripts disabled may help inspection but do not verify a working application. A normal trusted installation and application test is still needed before release.

Audit requests can disclose dependency names and versions to configured services. Review registry and advisory service settings for private projects, and protect generated reports because paths, dependency names and vulnerabilities can reveal internal information.

## Keep evidence without hiding failures

Store reports in the organization's restricted CI/artifact system under its retention policy, not automatically in this public documentation repository. Record scan time, source/lockfile/artifact hashes, commands, tool/config versions, report location, exit status and reviewer decision. If a shell step redirects JSON to a file, preserve and propagate its original status after artifact upload. Do not append `|| true` and label the job successful without a separate enforced gate.

A suggested private audit record is:

```yaml
audit_id: <internal-reference>
reviewed_at: <UTC-timestamp>
owner: <maintaining-team>
repository: <canonical-url>
commit: <full-commit-sha>
package_version: <exact-release-or-candidate>
consumer: <application-and-environment>
lockfile_sha256: <hash-or-not-applicable-with-reason>
artifact_sha256: <hash-or-not-built>
checks:
  - command: <exact-command>
    tool_version: <version>
    exit_status: <actual-number>
    result: <passed-failed-incomplete>
    evidence: <restricted-report-reference>
findings:
  - id: <advisory-or-internal-id>
    dependency_path: <direct-owner-to-affected-package>
    affected_range: <verified-range>
    exposure: <evidence-based-assessment>
    disposition: <fix-mitigate-false-positive-accepted-risk>
    remediation_owner: <team>
    due_at: <date>
    exception_expires_at: <date-or-none>
retest: <evidence-reference-or-pending>
release_decision: <blocked-approved-with-recorded-conditions-approved>
```

This is a specimen, not an automatically enforced schema. No field should imply an assessment was performed when it was not. Separate confirmed vulnerabilities, potential exposure, unsupported scan coverage and operational errors.

## Triage, exceptions and remediation

For each finding, confirm identity/range, dependency path and affected execution path. Prioritize active exploitation, exposed credentials, public remote execution, tenant/data access and release-chain compromise promptly. Assign an owner and due date according to the owning security policy. A low advisory score does not override a high-impact product context.

Prefer a supported fixed release. If blocked, document the blocker and a verified mitigation. An exception needs the exact package/advisory/version scope, rationale, residual risk, compensating control, approver, expiry and retest trigger. Do not permanently blanket-ignore a package or hide all low-severity findings. Abandoned dependencies need an ownership/replacement decision even without a matching exploit advisory.

Apply a shared fix at the canonical owner, publish it, and update each consumer and tracked copy. Rerun the original failing scenario, advisory scan and affected integration checks. See [security response](SECURITY-ISSUES.md) for disclosure and [package publishing](PACKAGE-PUBLISHING.md) for artifact verification.

## CI gates and audit completion

Use the repository's required checks; this guide does not silently replace stricter existing gates. Block a release for failed required checks, unresolved release-blocking findings, invalid evidence or an incomplete required scan. Scheduled scans should create an owned triage item through the organization's approved automation, rather than merely emitting logs nobody reviews. Avoid exposing secrets to untrusted pull requests.

An audit is complete when scope is explicit, required checks actually ran, findings have reviewed dispositions, fixed paths were retested, exceptions are current and the release decision has evidence. Keep the audit date visible. A clean dependency report means no matching advisories were reported by those sources at that time; it does not certify the entire product or replace continued monitoring.
