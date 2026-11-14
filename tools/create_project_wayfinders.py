#!/usr/bin/env python3
"""Plan or publish resumable project technology wayfinders (never Filament issues)."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/liberusoftware/documentation/blob/main/'
LAYERS = {
    'laravel-inertia-react': ('react', 'Laravel Inertia React', 'Laravel routes, sessions and CSRF own mutations; use allowlisted Inertia props. HTTP API adapters are optional for this surface.'),
    'laravel-inertia-vue': ('vue', 'Laravel Inertia Vue', 'Laravel routes, sessions and CSRF own mutations; use allowlisted Inertia props. HTTP API adapters are optional for this surface.'),
    'nuxt-vue': ('nuxt', 'Nuxt Vue', 'Consume reviewed HTTP contracts; isolate authenticated SSR caches and hydration by actor and tenant.'),
    'next-react': ('nextjs', 'Next.js React', 'Consume reviewed HTTP contracts; specify server/client boundaries, private caching and mutation invalidation.'),
    'mobile-react': ('react-native', 'React Native Expo', 'Use typed API clients, secure token storage, native accessibility, deep-link validation and explicit online/offline behavior.'),
    'mobile-flutter': ('flutter', 'Flutter mobile', 'Use typed Dart API clients, secure token storage, native accessibility and lifecycle/reconnect handling.'),
    'dart-mobile': ('flutter', 'Dart mobile', 'Use the dedicated Dart mobile Flutter host, typed API contracts, secure storage, touch navigation and lifecycle/reconnect handling.'),
    'dart-desktop': ('flutter', 'Dart desktop', 'Use the dedicated desktop Flutter host, typed API contracts, desktop secure storage, keyboard/focus, resizing, printing/export and multi-window concurrency.'),
}
PROJECTS = {'accounting-erp': 'accounting', 'enterprise-sap': 'sap', 'liberu-official': 'liberu', 'music-daw': 'music'}


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()


def targets():
    names = sorted(set(re.findall(r'https://github.com/liberusoftware/(project-[a-z0-9-]+)', (ROOT/'projects/REPOSITORIES.md').read_text())))
    for name in names:
        if name.endswith(('-laravel-filament', '-laravel-api')):
            continue
        for suffix, (layer, label, boundary) in LAYERS.items():
            if name.endswith('-'+suffix):
                slug = name[len('project-'):-(len(suffix)+1)]
                project = PROJECTS.get(slug, slug)
                yield name, project, suffix, layer, label, boundary
                break
        else:
            raise ValueError(f'Unmapped technology: {name}')


def module_rows(project, layer):
    mapping = json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects'].get(project, {}).get('designs', {})
    groups = {}
    for page in sorted((ROOT/'projects'/project/'features').glob('*.md')):
        if page.name == 'README.md':
            continue
        observed = mapping.get(page.stem, {}).get('layers', {}).get('core', [])
        # Collapse only exact observed identity matches; never infer equivalent domains.
        key = '|'.join(sorted(x['identity'] for x in observed)) or page.stem
        groups.setdefault(key, []).append(page)
    rows = []
    for pages in groups.values():
        page = pages[0]
        title = page.read_text().splitlines()[0].removeprefix('# ').split(': ', 1)[-1]
        target = ROOT/'projects'/project/layer/page.name
        if not target.exists():
            target = page
        aliases = f'; aliases: {", ".join(p.stem for p in pages[1:])}' if len(pages)>1 else ''
        rows.append(f'- [ ] [{title}]({BASE}{target.relative_to(ROOT)})'+aliases)
    return '\n'.join(rows)


def body(project, suffix, layer, label, boundary):
    source_guide = 'SOURCE-MAPPING.md' if (ROOT/'projects'/project/'SOURCE-MAPPING.md').exists() else 'ARCHITECTURE.md'
    return f'''## User outcome

Deliver the {project} product through {label}, using independently owned domain capabilities and matching optional presentation adapters. This issue is a wayfinder and implementation backlog, not a claim that the skeleton already implements the catalogue.

## Read first

- [Product index]({BASE}projects/{project}/README.md) and [source/alias reconciliation]({BASE}projects/{project}/{source_guide}).
- [Technology repository map]({BASE}projects/REPOSITORIES.md), [module boundaries]({BASE}architecture/MODULES.md), [API ownership]({BASE}architecture/API.md), [themes]({BASE}standards/THEMES.md), [testing]({BASE}standards/TESTING.md).
- [Implementation and issue-splitting guide]({BASE}projects/IMPLEMENTATION-WAYFINDERS.md).

## Delivery boundary

{boundary}

Reuse Boilerplate identity, authorization, Team/Store or tenant context, localization and other foundation contracts. Do not fork domain rules into this client or recreate shared capabilities. Verify published manifests and public contracts before requiring packages. For Dart hosts the Flutter layer plans supply shared widget/client requirements; desktop/mobile host-specific acceptance remains mandatory.

Keep installed `/modules` and `/themes` committed in the host wherever those directories apply, including after promotion; source repository releases and host lockfiles/copies move together. Independent source repositories remain authoritative.

## Sequencing

1. Audit the skeleton and current source/aliases; mark existing evidence and unresolved boundaries before writing code.
2. Approve ownership/dependency decisions; reuse or deliver core and API contracts with independent tests before the consuming UI.
3. Implement one complete user journey at a time, including policy checks, revisions, errors, empty/loading states, accessibility and recovery.
4. Prove host composition, upgrade behavior, observability and release compatibility; link evidence per capability below.

## Capability checklist

Each checkbox links the matching presentation plan (or feature plan if none exists) and represents a capability delivery slice for this technology. Read the same filename under core/ and api/ for the domain and HTTP contract; consult SOURCE-MAPPING.md for aliases. Split a child issue when ownership, dependencies and acceptance are actionable; link it here and retain the domain/API/presentation references. Resolve exact source aliases once rather than creating duplicate packages. A checked box requires passing evidence, not merely generated files.

{module_rows(project, layer)}

## Acceptance criteria for every selected slice

- Domain owner and public contracts are explicit; no `App\\` dependency in reusable packages, cross-module table writes or presentation-owned business rules.
- Authorization and tenancy are rechecked server-side; audience-specific DTOs and private caches prevent data leakage across users/stores.
- Version/conflict handling, idempotent retries and offline behavior are documented; failed remote work is visible and recoverable.
- Responsive/native accessibility, localization, timezone/currency behavior and user-facing error recovery are verified.
- Independent domain/API/adapter tests and at least one host journey pass; use the applicable greenfield or approved extraction coverage floor.
- Provide operational signals, runbook, migration/upgrade notes and a clean locked installation with no unexpected generated diff.

## Tracking policy

This repository owns its technology composition work. Existing `-laravel-filament` programmes are intentionally excluded from issue creation. Avoid multiplying unapproved or duplicate module issues across every technology: promote checklist items to focused children as their contracts become implementable. Catering has focused children because its cross-layer boundary decisions and privacy/conversion acceptance need explicit tracking.
'''


def write_issue_index(entries):
    columns = list(LAYERS)
    grouped = {}
    for entry in entries:
        grouped.setdefault(entry['project'], {})[entry['technology']] = entry
    lines = ['# Project implementation issues', '',
             'Technology wayfinders for every non-Filament project host. Each issue contains a capability checklist and delivery requirements. Existing Filament programmes remain separate. See the [implementation guide](IMPLEMENTATION-WAYFINDERS.md) and [machine-readable register](implementation-wayfinders.json).', '',
             '| Product | '+ ' | '.join(LAYERS[key][1] for key in columns)+' |',
             '| --- | '+ ' | '.join('---' for _ in columns)+' |']
    for project, technologies in sorted(grouped.items()):
        cells = []
        for key in columns:
            entry = technologies.get(key, {})
            cells.append(f"[Wayfinder]({entry['url']})" if 'url' in entry else 'Planned')
        lines.append(f'| [{project}]({project}/README.md) | '+ ' | '.join(cells)+' |')
    lines += ['', '## Ecommerce Catering', '']
    for entry in entries:
        if 'cateringIssue' in entry:
            lines.append(f"- [{entry['technology']}]({entry['cateringIssue']})")
    if (ROOT/'projects/ecommerce/catering-filament-issues.json').exists():
        lines += ['', '- [Filament Catering epic and core/API/Filament/Livewire slices](ecommerce/catering-filament-issues.json) — the Catering-only extension to the existing Filament programme.']
    (ROOT/'projects/IMPLEMENTATION-ISSUES.md').write_text('\n'.join(lines)+'\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Create missing issues in GitHub; default is local planning only')
    parser.add_argument('--output', type=Path, help='Optional plan/register path; dry runs do not overwrite the published register')
    args = parser.parse_args()
    result = []
    output = args.output or (ROOT/'projects/implementation-wayfinders.json' if args.apply else None)
    for repo, project, suffix, layer, label, boundary in targets():
        assert not repo.endswith('-laravel-filament')
        title = f'Wayfinder: {project} implementation for {label}'
        entry = {'repository': f'liberusoftware/{repo}', 'project': project, 'technology': suffix, 'title': title}
        if args.apply:
            issues = json.loads(gh('issue', 'list', '-R', entry['repository'], '--state', 'all', '--limit', '1000', '--json', 'title,url'))
            matches = [i for i in issues if i['title'] == title]
            if len(matches)>1:
                raise ValueError(f'Duplicate wayfinders: {repo}')
            if matches:
                entry['url'] = matches[0]['url']
            else:
                completed = subprocess.run(['gh', 'issue', 'create', '-R', entry['repository'], '--title', title, '--body-file', '-'], input=body(project, suffix, layer, label, boundary), text=True, check=True, capture_output=True)
                entry['url'] = completed.stdout.strip()
            if project == 'ecommerce':
                child_title = f'Catering: implement {label} workflow after boundary approval'
                matches = [i for i in issues if i['title'] == child_title]
                child_body = f'''## User outcome

Deliver safe event/menu request, quote review/acceptance and confirmation status in {label}. Parent wayfinder: {entry['url']}.

## Specifications and dependencies

- [Catering delivery map]({BASE}projects/ecommerce/CATERING.md)
- [Core ownership, dependencies and unresolved decisions]({BASE}projects/ecommerce/core/catering.md)
- [API contract]({BASE}projects/ecommerce/api/catering.md)
- [Presentation plan]({BASE}projects/ecommerce/{suffix if suffix.startswith('dart-') else layer}/catering.md)
- Upstream boundary request: https://github.com/liberusoftware/documentation/issues/26

Planning may proceed; schema and implementation are blocked until the core ownership/dependency and quote/booking/order transition decisions are approved. Core and HTTP contracts belong to their existing authoritative owners. {boundary}

## Acceptance criteria

- Use approved domain/API contracts and immutable menu/quote revisions; reject stale or expired acceptance.
- Customer DTOs, storage, caches, exports and errors never expose recipes, preparation details or ingredient costs; staff capabilities enforce distinct policies and Team/Store scope.
- Display quote acceptance, availability, order creation, deposit and payment completion separately.
- Duplicate clicks, timeout-after-conversion and reconnect reconcile using the same durable key; never produce duplicate orders or replay stale acceptance offline.
- Test accessibility, validation, permissions, private fields, revisions, retries and one real host quote-to-order journey. Include pending-conversion telemetry and recovery guidance.
- Keep applicable `/modules` and `/themes` contents in host commits alongside lockfiles. No copied domain rules, payment SDKs or cross-module writes in presentation code.
'''
                if matches:
                    entry['cateringIssue'] = matches[0]['url']
                else:
                    entry['cateringIssue'] = subprocess.run(['gh', 'issue', 'create', '-R', entry['repository'], '--title', child_title, '--body-file', '-'], input=child_body, text=True, check=True, capture_output=True).stdout.strip()
            print(entry['url'], flush=True)
        result.append(entry)
        if output:
            output.write_text(json.dumps({'status': 'in_progress' if args.apply else 'planned', 'excludedSuffix': '-laravel-filament', 'wayfinders': result}, indent=2)+'\n')
    if args.apply:
        output.write_text(json.dumps({'status': 'published', 'excludedSuffix': '-laravel-filament', 'wayfinders': result}, indent=2)+'\n')
        write_issue_index(result)
    print(f'{len(result)} wayfinders; Filament repositories excluded.')


if __name__ == '__main__':
    main()
