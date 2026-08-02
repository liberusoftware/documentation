# Liberu Documentation Standard

## Canonical Writing and Maintenance Specification

**Applies to:** Repository documentation, architecture and product scopes, developer guides, API documentation, runbooks, changelogs, migration guides, tutorials, and in-code documentation
**Related standards:** [REPOSITORIES.md](REPOSITORIES.md) · [MODULES.md](MODULES.md) · [THEMES.md](THEMES.md) · [API.md](API.md) · [TESTING.md](TESTING.md)

## 1. Purpose

Liberu documentation must help its intended reader complete a task, understand a decision, or operate a system safely without needing undocumented knowledge. It must be accurate, concise, professional, accessible, and easy to maintain.

Documentation is part of the product. A feature, public contract, release, or operational change is incomplete until its documentation and tested examples are current.

## 2. Core principles

1. **Write for a named reader:** identify whether the document serves users, adopters, developers, integrators, operators, security reviewers, or contributors.
2. **Lead with the outcome:** explain what the reader can achieve before implementation detail.
3. **Use one source of truth:** define a rule in its owning document and link to it elsewhere instead of copying it.
4. **Prefer plain language:** use familiar words, short sentences, and concrete examples; define necessary domain terms.
5. **Be precise:** distinguish requirements, recommendations, examples, current behavior, future scope, and known limitations.
6. **Make instructions executable:** state prerequisites, commands, expected results, failure recovery, and how to verify success.
7. **Keep claims provable:** link compatibility, security, performance, coverage, and release claims to maintained evidence.
8. **Design for change:** assign ownership, version public documentation, and update it in the same pull request as the behavior.
9. **Protect readers and data:** never publish secrets, private identifiers, unsafe production commands, or misleading security guarantees.
10. **Make content accessible:** use descriptive headings and links, meaningful alternative text, readable tables, and text alternatives for visual information.

## 3. Document ownership

Each subject has one authoritative home:

| Subject | Source of truth |
|---|---|
| Repository landing page and standard README content | [REPOSITORIES.md](REPOSITORIES.md) and the repository root `README.md` |
| Package boundaries, dependencies, installation, and lifecycle | [MODULES.md](MODULES.md) and module documentation |
| Theme resources, rendering, assets, and compatibility | [THEMES.md](THEMES.md) and theme documentation |
| API, connector, webhook, and marketplace contracts | [API.md](API.md) and generated API documentation |
| Shared Laravel foundation behavior | [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) |
| Product capabilities and implementation scope | The relevant product scope Markdown file |
| Test strategy, suites, tools, and coverage | [TESTING.md](TESTING.md) |
| Architectural decisions and trade-offs | Versioned ADRs in `/docs/adr` |
| Operational diagnosis and recovery | Versioned runbooks in `/docs/runbooks` |
| Released changes | `CHANGELOG.md`, release notes, and migration/upgrade guides |

Do not duplicate a feature catalogue, API schema, configuration reference, or architecture rule across repositories. Summarize only what is needed for context and link to the owning source.

## 4. Documentation structure

A repository should use only the documents relevant to its type:

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
LICENSE.md
docs/
├── index.md
├── getting-started.md
├── configuration.md
├── architecture.md
├── concepts/
├── guides/
├── reference/
├── adr/
├── runbooks/
├── upgrades/
└── troubleshooting.md
```

- **README:** concise project identity, status, features, tested quick start, and links.
- **Tutorial:** a guided learning path that produces a working result.
- **How-to guide:** steps for one practical outcome; assume basic context.
- **Concept:** explains why the system behaves as it does and how ideas relate.
- **Reference:** complete, structured facts such as configuration, commands, permissions, events, and compatibility.
- **ADR:** immutable context, decision, alternatives, consequences, and status; supersede rather than silently rewrite decisions.
- **Runbook:** symptoms, impact, safe diagnosis, mitigation, verification, rollback, escalation, and follow-up.

Do not combine tutorials, conceptual explanation, reference tables, and incident procedures into one long page when readers need them at different times.

## 5. Standard page template

Use this order when applicable:

1. Clear title using the reader's terminology.
2. One-sentence purpose and intended audience.
3. Outcome or capability provided.
4. Prerequisites, permissions, versions, and safety warnings.
5. Numbered procedure or structured explanation.
6. Minimal, realistic examples with expected results.
7. Verification and common failure recovery.
8. Limitations, security/privacy implications, and compatibility.
9. Related documentation and next steps.
10. Owner or last-reviewed metadata when the publishing system supports it.

Short documents should remain short; omit empty or irrelevant sections.

## 6. Clear and professional writing

- Use active voice: “The worker retries the job,” not “The job will be retried by the worker.”
- Address the reader as “you” in task instructions; use “Liberu” or the component name for system behavior.
- Put one main idea in each paragraph and one action in each numbered step.
- Prefer specific verbs such as “install,” “validate,” “publish,” and “revoke” over vague terms such as “handle” or “manage.”
- Expand uncommon abbreviations on first use and use domain terminology consistently thereafter.
- Use sentence case for headings. Avoid marketing language, unexplained jargon, jokes, blame, and unnecessary exclamation marks.
- State exact file names, package names, supported versions, defaults, units, time zones, and state transitions where they matter.
- Use **must** for requirements, **should** for recommended defaults, and **may** for optional behavior. Do not use these interchangeably.
- Describe current released behavior in the present tense. Mark proposals and planned features explicitly.

Prefer a paragraph for explanation, a numbered list for ordered actions, bullets for independent items, and a table only for data readers genuinely need to compare.

## 7. Links, code, and examples

- Use descriptive link text that makes sense out of context; avoid “click here.”
- Prefer relative links between files in the same repository and stable canonical URLs for external documentation.
- Link to a specific owned page, not a search result or an unstable branch line when a permanent reference exists.
- Label fenced code blocks with the language and keep commands copy-and-pasteable.
- Separate commands from output. Never include prompts such as `$` when they obstruct copying.
- Use placeholders such as `YOUR_TOKEN` and explain each one. Never use authentic secrets or production personal data.
- Show the smallest complete example that demonstrates the contract, including important error or denial behavior where relevant.
- Test code samples, installation commands, API examples, internal links, and referenced files automatically where practical.
- Provide text and alt text for diagrams, screenshots, and video. Crop imagery appropriately and avoid embedding essential instructions only in an image.

## 8. Architecture and module documentation

Module documentation must describe purpose, ownership, boundaries, dependencies, installation under `/modules`, configuration, data ownership, public contracts, permissions, events, jobs, extension points, failure recovery, compatibility, testing, upgrade, and uninstall behavior as required by [MODULES.md](MODULES.md).

Explain decisions through dependencies and observable behavior. Do not expose private tables or classes as public extension points merely because they exist. Use a small dependency diagram only when it clarifies three or more relationships, and provide an accompanying textual explanation.

Theme documentation must cover installation under `/themes`, optimized and tested hosts, supported module surfaces, resources, Blade/Livewire components, JavaScript and CSS entry points, assets and rights, accessibility, fallbacks, performance, tests, and known limitations as required by [THEMES.md](THEMES.md).

## 9. API and connector documentation

API documentation follows [API.md](API.md) and must be generated from or checked against the versioned contract. Document:

- base URL, versions, authentication, scopes, permissions, tenancy, and rate limits;
- resources, operations, fields, validation, pagination, filtering, errors, idempotency, and concurrency behavior;
- complete request/response examples with safe sample values;
- webhook verification, delivery identifiers, retries, ordering, replay, and deduplication;
- connector credentials, provider capability differences, mappings, sandbox mode, limits, outages, and reconciliation;
- compatibility, deprecation, migration periods, changelog, SDK generation, and support status.

OpenAPI schemas, generated references, implementation, examples, and tests must agree. Human-written guides explain intent and workflows; generated reference material supplies exhaustive contract facts.

## 10. Operations, security, and troubleshooting

- Put warnings immediately before the risky action and explain the consequence, backup, rollback, and required authority.
- Mark destructive, irreversible, billable, privacy-sensitive, or production-only steps clearly.
- Redact tokens, credentials, session values, personal data, provider payloads, and internal infrastructure identifiers from examples and logs.
- Troubleshooting starts with observable symptoms, then safe checks, likely causes, resolution, and verification.
- Runbooks distinguish customer impact, temporary mitigation, durable repair, rollback, escalation, and post-incident work.
- Link vulnerability reporting to `SECURITY.md`; never direct security reports to a public issue.

## 11. Releases, migrations, and deprecations

Every material release documents user-visible changes, compatibility, configuration or migration work, rollback constraints, and known issues. Breaking changes require a migration guide with before/after examples and a supported transition path.

Deprecation documentation states what is deprecated, the replacement, the first deprecated version, planned removal version or policy, detection method, migration steps, and behavior during the overlap period. Do not remove a public contract merely by deleting its documentation.

## 12. Review and automated quality

Documentation review is part of code review. Reviewers verify:

- technical accuracy against the implementation and tests;
- correct audience, outcome, ownership, prerequisites, and terminology;
- concise structure without duplicated sources of truth;
- runnable examples and a clear verification step;
- accurate links, anchors, diagrams, screenshots, versions, and badges;
- accessibility, inclusive language, spelling, grammar, and safe handling of data;
- upgrade, failure, rollback, security, and operational implications where relevant.

CI should lint Markdown, check internal and external links appropriately, validate headings and code fences, detect spelling/terminology issues, build the documentation site, and execute or contract-test examples where practical. Generated output should normally be published as an artifact or documentation site rather than committed.

## 13. Documentation workflow

1. Identify the reader, intended outcome, and authoritative owner.
2. Choose the correct document type and location.
3. Outline only the information needed to achieve the outcome safely.
4. Write and test the smallest complete example or procedure.
5. Link canonical architecture, API, testing, security, and product scope documents.
6. Review for accuracy, readability, accessibility, privacy, and duplication.
7. Run documentation checks and have a technically informed reviewer approve it.
8. Publish documentation with the corresponding feature or release.
9. Track ownership and review after changes, incidents, deprecations, and support trends.

## 14. Definition of done

Documentation is ready when:

- its audience can identify the purpose and complete the documented outcome;
- current behavior, requirements, limitations, and planned work are clearly distinguished;
- examples and commands are safe, minimal, accurate, and tested where practical;
- public contracts, configuration, permissions, failures, and compatibility are documented by their owner;
- links resolve and duplicated or superseded guidance has been removed;
- security, privacy, accessibility, migration, rollback, and operational needs are addressed proportionately;
- CI documentation checks pass and an appropriate reviewer has approved the change.
