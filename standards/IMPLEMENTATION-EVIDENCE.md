# Implementation and evidence across technologies

Use this standard when documenting or reviewing a capability that crosses a domain module, an API, and one or more user interfaces. It applies to both new work and changes to existing implementations. The technology-specific standards remain authoritative for framework conventions; this page defines the evidence needed to connect them.

## Establish the implementation baseline

Record the owning repository and commit or release, the consuming application, and the relevant runtime and dependency versions from its manifests and lockfiles. Identify the supported database, browser or device range only when the owner has established it. A target in a standard is not evidence that an existing application supports that version. Link to the source inventory or a commit-pinned source reference and name any local changes that are outside that evidence.

Classify each claim as **observed** (with source and verification), **proposed**, or **unknown**. Source inspection establishes that code exists; it does not establish that the code works in every deployment. Record separately whether an example was inspected, syntax-checked, executed, or tested end to end, including the environment and relevant versions. Do not describe an unexecuted example as tested.

## Trace a complete operation

Choose a representative user outcome and follow it through each applicable boundary. Link the actual files or versioned contracts; use the table as a review aid, not as a claim that every application has every layer.

| Boundary | Document and verify |
| --- | --- |
| Entry point | Route, command, event or screen; prerequisites; identity and tenant context; required permission. |
| Validation and authorization | Accepted inputs and limits, where they are checked, denial behavior, and whether authorization is repeated for asynchronous work. |
| Domain operation | Public action or contract, owner of the data, state transitions, transaction boundary, and effects on other modules. |
| Persistence and concurrency | Constraints and migrations, conflict handling, duplicate requests, retry safety, and any ordering assumptions. Describe guarantees only when supported by evidence. |
| Response and side effects | Returned fields or page props, error mapping, events and jobs, delivery guarantees, and how pending or failed work becomes visible. |
| Presentation | Transport and session boundary, loading/empty/error states, accessible interaction, stale data and draft recovery. Inertia page visits and independent JSON API clients have different contracts. |
| Operations | Configuration, observability without sensitive data, failure diagnosis, recovery, deployment and rollback constraints. |

For each boundary, identify the authoritative implementation and the tests that exercise it. If a contract or test is absent, record the gap and its owner rather than inventing an endpoint, field, guarantee, or command. Link the detailed [API](../architecture/API.md), [testing](TESTING.md), [security](../architecture/SECURITY.md), and [presentation](../guides/presentation/README.md) guidance where applicable.

## Review by technology

Apply the relevant row in addition to the trace above. A project may use only a subset of these technologies.

| Technology or surface | Implementation evidence to seek | Standard or guide |
| --- | --- | --- |
| PHP, Composer, Laravel | Manifest and lock, public interfaces, container registration, policies, migrations, jobs and feature tests. | [PHP](PHP.md), [Laravel](LARAVEL.md), [Composer](../guides/COMPOSER.md) |
| Filament, Livewire, Blade | Server-side authorization and validation, component lifecycle, rendered states and interaction tests. | [Filament](FILAMENT.md), [Livewire](LIVEWIRE.md), [Blade](BLADE.md) |
| React or Vue with Inertia | Laravel route and page props, form/redirect behavior, client state and server authorization. | [React](REACT.md), [Vue](VUE.md), [Inertia](INERTIA.md) |
| Next.js or Nuxt | Server/client execution boundary, API authentication, caching and invalidation, configuration and deployment. | [Next.js](NEXTJS.md), [Nuxt](NUXT.md) |
| JavaScript, TypeScript and npm packages | Runtime and compiler configuration, exported contracts, dependency compatibility, lockfile and consumer build. | [JavaScript](../technologies/JAVASCRIPT.md), [TypeScript](../technologies/TYPESCRIPT.md), [npm](../guides/NPM.md) |
| React Native, Flutter and Dart | Platform support, secure session storage, lifecycle and connectivity behavior, native build and device verification. | [React Native](REACT-NATIVE.md), [Flutter](FLUTTER.md), [Dart guide](../guides/presentation/DART.md) |
| Database and asynchronous processing | Schema constraints, migration and rollback behavior, queue configuration, retry and failure handling. | [Database](DATABASE.md), [Jobs](JOBS.md), [Queues](QUEUES.md) |

## Record verification and gaps

For each changed journey, record the commands actually run, their result and environment, plus manual checks that cannot be automated. Include at least a successful operation and relevant denied or invalid input; add tenant isolation, concurrency, retries, or recovery checks when the behavior requires them. Use the owning repository's documented commands instead of assuming a universal test runner. If a dependency or environment is unavailable, state what remains unverified and how to reproduce the check.

For example, a review might say: “Proposed: submitting a record twice should not create duplicates. No idempotency contract or concurrent-request test was found in the inspected revision.” This identifies a requirement and a gap without claiming the current application provides the guarantee. Once implemented, replace the gap with links to the reviewed contract, implementation and test result.

Update the owning guide and affected adapter documentation in the same change. Review [documentation maintenance](../guides/DOCUMENTATION-MAINTENANCE.md) for generated files, source snapshots, and repository checks.
