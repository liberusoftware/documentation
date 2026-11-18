#!/usr/bin/env python3
"""Replace invented generic API payload examples with pinned route/schema evidence and structured feature-to-API operation plans."""
import argparse
import json
from pathlib import Path
import re

from build_source_reference import safe
from build_technology_module_plans import PROJECT_SLUGS, parse_source_evidence, scope_labels, title_for

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects', type=Path, default=Path('/tmp/liberu-documentation-sources'))
    parser.parse_args()

    snapshot = json.loads((ROOT / 'architecture/source-inventory.json').read_text())['repositories']
    mapping = json.loads((ROOT / 'architecture/source-design-mapping.json').read_text())['projects']
    nextjs_groups = json.loads((ROOT / 'architecture/nextjs-adapter-plans.json').read_text()).get('groups', {})
    records = {r['project']: r for r in snapshot}

    changed = 0
    route_scopes = 0
    schema_scopes = 0
    for project, project_info in mapping.items():
        if project in ('sap', 'music'):
            continue  # Authored enterprise and music API plans have their own builders.
        record = records.get(project)
        slug = PROJECT_SLUGS.get(project, project)
        for stem, info in project_info['designs'].items():
            if project == 'ecommerce' and stem == 'catering':
                continue
            page = ROOT / 'projects' / project / 'api' / f'{stem}.md'
            if not page.exists():
                continue
            original = page.read_text()
            if '<!-- documentation-kind: source-index -->' in original:
                continue

            core = info['layers']['core']
            cap_key = core[0]['identity'] if len(core) == 1 else f'planned:{project}:{stem}'
            canonical_home_rel = nextjs_groups.get(cap_key, {}).get('home')
            canonical_home = (ROOT / canonical_home_rel) if canonical_home_rel else None

            ev = parse_source_evidence(mapping, project, stem, canonical_home)
            routes_block = ev['routes_block']
            schemas = ev['schemas']
            controllers = ev['controllers']
            requests = ev['requests']
            queries = ev['queries']
            commands = ev['commands']
            models = ev['models']
            declared = ev['declared']

            references = []
            seen = set()
            for choice in info['layers']['api'] + info['layers']['core']:
                if choice['directory'] in seen:
                    continue
                seen.add(choice['directory'])
                references.append(choice)

            labels = scope_labels(project, stem) or list(dict.fromkeys(declared)) or [title_for(project, stem)]

            lines = [
                '## 3. Endpoint examples',
                '',
                '**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.',
                '',
                '### Product API backend and client integration',
                '',
                f'This module API adapter is composed into [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).',
                '',
                '| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |',
                '| --- | --- | --- | --- |',
                f'| Next.js React | [`project-{slug}-next-react`](https://github.com/liberusoftware/project-{slug}-next-react) | [Next.js plan](../nextjs/{stem}.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |',
                f'| Nuxt 4 Vue | [`project-{slug}-nuxt-vue`](https://github.com/liberusoftware/project-{slug}-nuxt-vue) | [Nuxt plan](../nuxt/{stem}.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |',
                f'| React Native Expo | [`project-{slug}-mobile-react`](https://github.com/liberusoftware/project-{slug}-mobile-react) | [React Native plan](../react-native/{stem}.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |',
                f'| Flutter mobile | [`project-{slug}-mobile-flutter`](https://github.com/liberusoftware/project-{slug}-mobile-flutter) | [Flutter plan](../flutter/{stem}.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |',
                f'| Dart mobile & desktop | [`project-{slug}-dart-mobile`](https://github.com/liberusoftware/project-{slug}-dart-mobile) · [`project-{slug}-dart-desktop`](https://github.com/liberusoftware/project-{slug}-dart-desktop) | [Flutter & Dart plan](../flutter/{stem}.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |',
                '',
                '### Feature-to-API capability and operation matrix',
                '',
                '| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |',
                '| --- | --- | --- |',
            ]
            for label in labels:
                lines.append(
                    f'| **{safe(label)}** | Expose authorized query/read projection and explicit domain transition command for `{safe(label.lower())}` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |'
                )
            lines += ['']

            if references:
                lines += ['| Boundary | Observed identity and implementation reference |', '| --- | --- |']
                for choice in references:
                    relative = Path('../../../') / choice['reference']
                    lines.append(f'| Source package | [{choice["identity"]}]({relative}) |')
                lines += ['']
            if routes_block:
                route_scopes += 1
                lines += [
                    '### Observed route declarations',
                    '',
                    'These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.',
                    '',
                    routes_block,
                    '',
                ]
            else:
                lines += [
                    'No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.',
                    '',
                ]
            if controllers:
                lines += [
                    '### Observed controller entry points',
                    '',
                    'The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.',
                    '',
                    '| Controller source | Public handler signatures |',
                    '| --- | --- |',
                ]
                for link_md, sigs_raw in controllers:
                    lines.append(f'| {link_md} | {sigs_raw} |')
                lines += ['']
            if requests:
                lines += ['Request validation sources: ' + ' · '.join(requests) + '.', '']
            if queries or commands or models:
                lines += [
                    '### Observed domain queries, actions, and storage models',
                    '',
                    'API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.',
                    '',
                ]
                if queries:
                    lines += ['| Core query source | Observed signatures |', '| --- | --- |']
                    for link_md, sigs_raw in queries:
                        lines.append(f'| {link_md} | {sigs_raw} |')
                    lines += ['']
                if commands:
                    lines += ['| Core action / service source | Observed signatures |', '| --- | --- |']
                    for link_md, sigs_raw in commands:
                        lines.append(f'| {link_md} | {sigs_raw} |')
                    lines += ['']
                if models:
                    lines += ['| Core storage model | Observed fillable fields (review for DTO allowlist) |', '| --- | --- |']
                    for link_md, fields_txt in models:
                        lines.append(f'| {link_md} | {fields_txt} |')
                    lines += ['']
            if project == 'ecommerce' and record:
                lines += [
                    'Ecommerce also implements capabilities in the [application tree](../SOURCE-APPLICATION.md). Its [current root route file](https://github.com/liberusoftware/'
                    + record['repository']
                    + '/blob/'
                    + record['commit']
                    + '/routes/api.php) and application controllers/GraphQL schema must be reviewed for the selected task. Preserve this module even when no independent package match exists.',
                    '',
                ]
                for row in (ROOT / 'projects/ecommerce/SOURCE-APPLICATION.md').read_text().splitlines():
                    if f'](features/{stem}.md)' in row:
                        lines += ['Capability-specific source entry points: ' + row.split('|')[-2].strip() + '.', '']
            lines += [
                'A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.',
                '',
                '## 4. OpenAPI schema',
                '',
            ]
            if schemas:
                schema_scopes += 1
                lines += [
                    'The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.',
                    '',
                    *[f'- {s}' for s in schemas],
                    '',
                ]
            else:
                lines += [
                    'No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.',
                    '',
                ]
            lines += [
                'For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.',
                '',
                'Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#'
                + stem
                + '), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.',
                '',
            ]
            block = '\n'.join(lines) + '\n'
            pattern = r'^## 3\. Endpoint examples\n.*?(?=^## 5\. Audience and operation matrix)'
            first_examples = re.search(r'^## 3\. Endpoint examples\n', original, re.M)
            marker_pos = original.find('<!-- observed-api-contract:start -->')
            if first_examples and not re.search(pattern, original, re.M | re.S) and (marker_pos < 0 or first_examples.start() < marker_pos):
                footer = '''## 5. Audience and operation matrix

Expose only explicitly selected operations. Anonymous access is disabled unless the owning capability requires it; customer/partner reads and commands use record/tenant scope, staff actions use the relevant policy, and integrations use a narrow service identity. UI visibility and authentication alone do not establish authorization.

## 6. Implementation strategy

Resolve trusted actor/tenant context, validate the reviewed request and delegate to the public owning action/query. Serialize explicit authorized DTOs; preserve documented operation identity, concurrency and error semantics. Reuse existing owner APIs instead of copying their records or private model access.

## 7. Security, resilience, and observability

Apply record/field policy to lists, relationships, commands, bulk work, jobs and downloads. Use bounded retries/timeouts, durable operation/source references and explicit partial-failure recovery. Redact credentials/protected data while retaining safe request/correlation diagnostics.

## 8. Verification strategy

Verify actual route/schema parity, required input, allowed/denied/wrong-tenant requests, stale/duplicate commands, uncertain outcomes, pagination/field policy and affected owner integrations. Check the declared package/host scripts and supported versions; source/test presence is not a passing-run claim.

## 9. Definition of done

Release only after the complete reviewed request/response/error contract, version compatibility, security and owner invariants, consumer integration, migrations where owned, and operational recovery are verified. Document the actual package identity and source/release evidence in its README and changelog.
'''
                updated = original[:first_examples.start()] + block + footer
            elif re.search(pattern, original, re.M | re.S):
                updated = re.sub(pattern, lambda _: block, original, flags=re.M | re.S)
            else:
                start = '<!-- observed-api-contract:start -->'
                end = '<!-- observed-api-contract:end -->'
                marked = start + '\n' + block + end
                if start in original:
                    updated = re.sub(re.escape(start) + r'.*?' + re.escape(end), lambda _: marked, original, flags=re.S)
                else:
                    updated = original + '\n' + marked + '\n'
            updated = re.sub(
                r'- Use `/api/[^`]+` as the default module route prefix[^\n]*',
                "- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.",
                updated,
            )
            updated = re.sub(r'\*\*API package:\*\* `([^`/]+)`', r'**Proposed API design identifier:** `\1`', updated)
            updated = re.sub(r'^(\*\*Proposed API design identifier:\*\* `[^`\n]+`)[ \t]+$', r'\1<br>', updated, flags=re.M)
            if updated != original:
                page.write_text(updated)
                changed += 1
    print(f'Updated {changed} non-enterprise API documents; indexed route evidence for {route_scopes} spellings and schema evidence for {schema_scopes}.')


if __name__ == '__main__':
    main()
