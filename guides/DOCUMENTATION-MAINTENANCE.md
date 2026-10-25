# Keep the documentation synchronized with source

Use this guide when an application or module changes, when a dependency is adopted by another product, or when a new presentation package is planned. Source snapshots, design specifications and task guides answer different questions; maintain the links between them without turning a source directory count into a feature/release claim.

## Understand the documentation parts

| Part | What it establishes | What requires additional evidence |
| --- | --- | --- |
| Project scope and `features/` | Intended product capability and boundaries | Whether each requirement is implemented |
| `core/`, `api/` and presentation plans | Target package and adapter responsibilities | Actual package identity, routes and compatibility |
| `SOURCE-MODULES.md` | Commit-pinned module manifests, aliases and application source roots | Runtime behavior, enablement and registry publication |
| `modules/source/` | Exact metadata, callable signatures, migrations, route/schema paths and tests present | Correctness, complete public API, passing tests and safe adoption |
| `SOURCE-MAPPING.md` | Name-based connections between designs and sources | Semantic equivalence where names or ownership differ |
| Project walkthroughs | Reviewed behavior of a specific source workflow | Behavior outside the stated review scope |
| User guides | Tasks, outcomes and recovery for readers | Parity with current implementation unless reviewed |

Every source-backed claim should identify its repository/commit or an actual released contract. Mark proposals as proposals. Preserve source-specific differences instead of rewriting them to match a preferred architecture.

## Discover and clone applications

From the documentation repository:

```bash
python3 tools/clone_laravel_projects.py --projects /home/liberu/projects
```

The tool reads all GitHub organization repository pages until the final partial page, selects public names ending in `-laravel`, records the discovery list and clones missing repositories. It preserves existing checkouts and their branches. `--list-only` refreshes discovery without cloning. A failed API page stops discovery rather than replacing the snapshot with an incomplete list.

The discovery list lives in both `/home/liberu/projects/repositories.json` and [the repository snapshot](../architecture/source-repositories.json). Private repositories require separate authorized access and are outside a public listing's evidence. Existing clones must be reviewed/fetched separately when intentionally updating the source snapshot; the clone tool does not move their HEADs or discard local work.

## Reproduce a pinned snapshot while project work continues

If active project clones have uncommitted edits, preserve that work and prepare isolated views of the inventory commits:

```bash
python3 tools/prepare_source_snapshot.py --projects /home/liberu/projects --output /tmp/liberu-documentation-sources
```

The tool creates detached Git worktrees at the recorded commits and validates their HEADs/clean state. It does not reset active branches or overwrite active source files. An existing snapshot with another commit or local changes fails rather than being replaced; choose a fresh output directory in that case. Git worktree metadata is shared with the original repository.

Pass `--projects /tmp/liberu-documentation-sources` to the inventory, comparison, implementation-reference, project-guide, Next.js and API-evidence builders when reproducing that snapshot. The discovery list is copied into the snapshot root. Documentation-only reconciliation, enterprise builders, Inertia clarification and user-guide enrichment read repository inputs and need no source path flag. A snapshot is evidence for its recorded commits; it does not describe later uncommitted changes as published source.

## Rebuild source references in dependency order

Finish or preserve source edits before scanning. The tools reject dirty checkouts and require the pinned HEADs to match rather than linking uncommitted behavior to a public commit URL.

```bash
python3 tools/sync_source_inventory.py --projects /home/liberu/projects
python3 tools/compare_shared_modules.py --projects /home/liberu/projects
python3 tools/build_source_reference.py --projects /home/liberu/projects
python3 tools/reconcile_source_modules.py
python3 tools/build_project_guides.py
python3 tools/build_nextjs_plans.py
python3 tools/build_enterprise_api_plans.py
python3 tools/build_enterprise_layer_plans.py
python3 tools/improve_api_source_contracts.py
python3 tools/clarify_inertia_boundaries.py
python3 tools/enrich_user_module_guides.py
python3 tools/sync_documentation_indexes.py
python3 tools/build_shared_adoption_guides.py --projects /tmp/liberu-documentation-sources
```

Review all generated diffs. The inventory distinguishes physical package directories, compatibility symlink aliases and directories without direct package manifests. Application-owned source outside `modules/` is also recorded. The package reference groups identical reference inputs under one identity and preserves differing variants; the runtime comparison uses a narrower documented fingerprint.

The reconciliation tool updates marked source-reference blocks in existing module documents and preserves the rest of their content. Its matches are based on documented naming patterns, not a semantic PHP analysis. Review ambiguous or changed ownership manually. The 12 older foundation design spellings are retained aliases, not additional source packages.

The Next.js builder uses one plan home per observed core identity where matched, retains the authored SAP Next.js plans, and preserves all other spellings as consumer/alias links. Source identity collisions leave package naming unassigned rather than silently merging incompatible PHP identities. The enterprise builders read the detailed domain briefs and authored command examples; edit those inputs when changing the proposed contract. The API evidence pass replaces invented payload keys with source routes/handlers/schemas, and the Inertia pass clarifies its page transport.

Generated files are indexes/reference material. Edit reviewed behavior guides and domain designs directly; update the relevant generator when its extraction method is wrong. A package disappearing from a refreshed input needs a documented compatibility/retirement review, not automatic deletion of a product capability or its documentation.

## Preserve Ecommerce capabilities

Ecommerce implements substantial behavior in `app/`, routes, views and application services. Its immediate package-folder count is not its module catalogue. Preserve all documented Ecommerce modules and extend the [application capability map](../projects/ecommerce/SOURCE-APPLICATION.md) when reviewing extraction or new source locations. The source project's historical research and ADRs must be checked for current status before applying them.

The repository checker verifies that previously tracked Ecommerce documentation files remain present. That is a file-preservation check; review module scope and task content as well so a capability is not accidentally removed inside a retained file.

## Review a changed module

Read the actual manifest, provider/registration, exported contracts, actions, queries, policies, schemas and migrations. Trace at least the changed user journey from UI/API entry through authoritative behavior and back to the response. Record actor/tenant resolution, input validation, legal transitions, outputs/events, concurrency/retry behavior, and recovery. List concrete differences from the target design instead of presenting planned invariants as implemented guarantees.

For a shared capability, compare all affected consumers and variants. Choose one accountable owner, document supported extension points and data transitions, and link other products to that owner. A tracked installed copy or directory alias is not automatically an independent module. See the [reuse/consolidation guide](../architecture/SHARED-MODULES.md).

Update core/API and every affected presentation document together. React/Inertia and Next.js may share framework-independent React primitives; keep their navigation, session, request protocol and cache boundaries explicit. For asynchronous work, include observable pending/failure state and the user/operator's recovery action.

## Validate navigation and examples

```bash
python3 tools/repair_standard_links.py --check
python3 tools/check_documentation.py --report /tmp/documentation-links.json
python3 tools/audit_documentation_coverage.py --projects /tmp/liberu-documentation-sources --report /tmp/documentation-coverage.json
```

The first check finds a specific class of misleading standard links: a filename label pointing to a different local filename. The second checks inline local Markdown file targets outside fenced examples and preservation of tracked Ecommerce files. The coverage audit additionally checks every mapped spelling/layer/task index, package reference coverage, exact shared-plan links, source snapshot HEADs, domain metadata and module fences. These checks still do not prove semantic completeness, external availability, runtime parity or package stability.

For the rendered-structure and heading-fragment check, create isolated tooling outside the repository:

```bash
python3 -m venv /tmp/liberu-docs-checks
/tmp/liberu-docs-checks/bin/pip install -r tools/requirements-docs.txt
npm install --prefix /tmp/liberu-docs-checks/node --no-audit --no-fund github-slugger@2.0.0
/tmp/liberu-docs-checks/bin/python tools/check_rendered_documentation.py --slugger-module /tmp/liberu-docs-checks/node/node_modules/github-slugger/index.js --report /tmp/rendered-documentation.json --preview-dir /tmp/liberu-docs-previews
```

Run `/tmp/liberu-docs-checks/bin/python tools/check_enterprise_api_examples.py` to validate the 16 proposed enterprise request schemas/examples and route alignment. This validates documentation specimens, not implemented business rules.

The rendered check parses GFM-like Markdown and checks heading/explicit-anchor destinations with GitHub-style slugs, and writes representative HTML previews. It checks structure/navigation, not browser visual behavior or semantic implementation completeness. The preview CSS is a review aid, not a deployed documentation site.

Review the remaining concerns separately. Render representative long tables, package references, command examples, domain designs and user tasks using the intended Markdown renderer. Check headings/fragments, table cell boundaries, code fences, meaningful link labels and a clear path from getting started to module detail. Verify commands against declared scripts/runner versions and use a disposable compatible host when an execution result is needed. Record whether an example was source-inspected, syntax-checked or actually executed.

## Publish documentation changes

Review the diff for source correctness, retained capabilities, generated/reference consistency and actionable user guidance. Run the checks appropriate to the changed content, record remaining limitations and follow the repository's Git/review workflow. Documentation updates do not themselves publish Composer/npm packages or establish their stability. Package publishing follows the [Composer](COMPOSER.md) or [npm](NPM.md) lifecycle guide in the owning package repository.

The [objective audit](../architecture/DOCUMENTATION-AUDIT.md) records requirement-by-requirement evidence and the limits of automated checks.
