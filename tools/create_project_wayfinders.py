#!/usr/bin/env python3
"""Plan, publish or sync resumable project technology wayfinders (never Filament issues)."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from wayfinder_technologies import BASE, LAYERS, link, write_wayfinder_docs  # noqa: E402

PROJECTS = {'accounting-erp': 'accounting', 'enterprise-sap': 'sap', 'liberu-official': 'liberu', 'music-daw': 'music'}
MAPPING = json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
SKELETON_LOOKUP = {
    (r['capabilityKey'], r['presentation']): r
    for r in json.loads((ROOT/'architecture/module-skeleton-repositories.json').read_text())['repositories']
}


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()


def targets():
    names = sorted(set(re.findall(r'https://github.com/liberusoftware/(project-[a-z0-9-]+)', (ROOT/'projects/REPOSITORIES.md').read_text())))
    for name in names:
        if name.endswith(('-laravel-filament', '-laravel-api')):
            continue
        for suffix, (layer, label, profile) in LAYERS.items():
            if name.endswith('-'+suffix):
                slug = name[len('project-'):-(len(suffix)+1)]
                project = PROJECTS.get(slug, slug)
                yield name, project, slug, suffix, layer, label, profile
                break
        else:
            raise ValueError(f'Unmapped technology: {name}')


def module_rows(project, layer, suffix):
    mapping = MAPPING.get(project, {}).get('designs', {})
    groups = {}
    for page in sorted((ROOT/'projects'/project/'features').glob('*.md')):
        if page.name == 'README.md' or '<!-- documentation-kind: source-index -->' in page.read_text():
            continue
        observed = mapping.get(page.stem, {}).get('layers', {}).get('core', [])
        # Collapse only exact observed identity matches; never infer equivalent domains.
        key = '|'.join(sorted(x['identity'] for x in observed)) or page.stem
        groups.setdefault(key, []).append(page)
    rows = []
    for pages in groups.values():
        page = pages[0]
        title = page.read_text().splitlines()[0].removeprefix('# ').split(': ', 1)[-1].removesuffix(' — Domain specifications')
        target = ROOT/'projects'/project/layer/page.name
        if not target.exists():
            target = page
        observed = mapping.get(page.stem, {}).get('layers', {}).get('core', [])
        cap_key = observed[0]['identity'] if len(observed) == 1 else (f'liberusoftware/music-{page.stem}' if project == 'music' else f'planned:{project}:{page.stem}')
        skel = SKELETON_LOOKUP.get((cap_key, suffix))
        skel_note = f' · `{skel["repository"]}`' if skel else ''
        aliases = f'; aliases: {", ".join(p.stem for p in pages[1:])}' if len(pages)>1 else ''
        rows.append(f'- [ ] [{title}]({BASE}{target.relative_to(ROOT)}){skel_note}'+aliases)
    return '\n'.join(rows)


def body(project, slug, suffix, layer, label, profile):
    source_guide = 'SOURCE-MAPPING.md' if (ROOT/'projects'/project/'SOURCE-MAPPING.md').exists() else 'ARCHITECTURE.md'
    api_repo = f'https://github.com/liberusoftware/project-{slug}-laravel-api'

    standards = '\n'.join(f'- [{title}]({link(path)})' for title, path in profile['standards'])
    guides = '\n'.join(f'- [{title}]({link(path)})' for title, path in profile['guides'])
    method = '\n'.join(f'{i}. {step}' for i, step in enumerate(profile['method'], 1))
    spec = profile['spec'].replace('{adapter}', profile['adapter_pattern'])
    api_block = ''
    if profile['api_client']:
        api_block = f'''
## Product API backend

Independent clients use [{api_repo}]({api_repo}) as the composition root for authorized HTTP access. Configure this application's API base URL to that deployment; the frontend repository URL is not an API endpoint. See [Laravel API backends]({link('guides/LARAVEL-API-BACKENDS.md')}).
'''

    return f'''## User outcome

Deliver the {project} product through {label}, using independently owned domain capabilities and matching optional presentation adapters. This issue is a wayfinder and implementation backlog, not a claim that the skeleton already implements the catalogue.

## Read first

- [Product index]({link(f'projects/{project}/README.md')}) and [source/alias reconciliation]({link(f'projects/{project}/{source_guide}')}).
- [Technology repository map]({link('projects/REPOSITORIES.md')}), [module boundaries]({link('architecture/MODULES.md')}), [API ownership]({link('architecture/API.md')}), [testing]({link('standards/TESTING.md')}), [implementation evidence]({link('standards/IMPLEMENTATION-EVIDENCE.md')}).
- [Implementation and issue-splitting guide]({link('projects/IMPLEMENTATION-WAYFINDERS.md')}).
- **Full technical specification for this technology:** [wayfinders/{suffix}.md]({link(f'projects/wayfinders/{suffix}.md')}).
- **Capability skeleton catalog for this layer:** [{profile['skeleton_catalog']}]({link(profile['skeleton_catalog'])}).
- Application Boilerplate template: {profile['boilerplate']}
- Reusable module foundation template: {profile['module_foundation']}

### Technology standards
{standards}

### Implementation runbooks
{guides}
- [Module index for this layer]({link(profile['module_index'])})
{api_block}
## Delivery boundary

{profile['boundary']}

Reuse Boilerplate identity, authorization, Team/Store or tenant context, localization and other foundation contracts. Do not fork domain rules into this client or recreate shared capabilities. Verify published manifests and public contracts before requiring packages. Adapter identity pattern: `{profile['adapter_pattern']}`.

Keep installed `/modules` and `/themes` committed in the host wherever those directories apply, including after promotion; source repository releases and host lockfiles/copies move together. Independent source repositories remain authoritative.

## Implementation method

Follow this technology-specific method for every capability slice. Details and examples live in the [full specification]({link(f'projects/wayfinders/{suffix}.md')}) and linked runbooks.

{method}

## Technical specification

{spec}

## Phased implementation plan

1. **Phase 1 — Skeleton & Source Audit:** Audit this host skeleton, the matching capability module skeletons (`{profile['adapter_pattern']}`), and `SOURCE-MAPPING.md`; record existing source evidence and unresolved boundary decisions before writing code.
2. **Phase 2 — Backend, Auth & Tenant Wiring:** Approve ownership/dependency decisions; wire session/authentication, workspace/tenant resolution, and core/API contracts (`project-{slug}-laravel-api` or Laravel Inertia routes) with independent contract tests.
3. **Phase 3 — Capability Vertical Slices:** Execute the implementation method above capability-by-capability using the structured feature/aspect matrix in each linked presentation plan (`{layer}/*.md`), implementing all features/aspects inside the capability module skeleton and composing it in this host.
4. **Phase 4 — UX States, Accessibility & Recovery:** Verify loading, empty, denied (403), validation (422), stale/conflict (409/412), rate-limit (429), pending operation (202), accessibility, localization, and offline/retry reconciliation.
5. **Phase 5 — Verification & Release Gates:** Prove host composition, clean locked installs, coverage floors, upgrade/rollback safety, and release compatibility; link evidence per capability below.

## Capability checklist

Each checkbox links the matching presentation plan (which includes the structured feature/aspect matrix, skeleton repository link, API backend integration, and observed source evidence) and names the capability module skeleton repository (`module-...`). Read the same filename under `features/`, `core/`, and `api/` for the domain and HTTP contract; consult `SOURCE-MAPPING.md` for aliases. Split a child issue when ownership, dependencies and acceptance are actionable; link it here and retain the domain/API/presentation references. Resolve exact source aliases once rather than creating duplicate packages. A checked box requires passing evidence, not merely generated files.

{module_rows(project, layer, suffix)}

## Acceptance criteria for every selected slice

- Domain owner and public contracts are explicit; no `App\\` dependency in reusable packages, cross-module table writes or presentation-owned business rules.
- Authorization and tenancy are rechecked server-side; audience-specific DTOs and private caches prevent data leakage across users/stores.
- Version/conflict handling, idempotent retries and offline behavior are documented; failed remote work is visible and recoverable.
- Responsive/native accessibility, localization, timezone/currency behavior and user-facing error recovery are verified.
- Independent domain/API/adapter tests and at least one host journey pass; use the applicable greenfield or approved extraction coverage floor.
- Provide operational signals, runbook, migration/upgrade notes and a clean locked installation with no unexpected generated diff.
- Work followed the technology method and specification linked above (transport, session, package layout and security rules for {label}).

## Tracking policy

This repository owns its technology composition work. Existing `-laravel-filament` programmes are intentionally excluded from issue creation. Avoid multiplying unapproved or duplicate module issues across every technology: promote checklist items to focused children as their contracts become implementable. Catering has focused children because its cross-layer boundary decisions and privacy/conversion acceptance need explicit tracking.
'''


def write_issue_index(entries):
    columns = list(LAYERS)
    grouped = {}
    for entry in entries:
        grouped.setdefault(entry['project'], {})[entry['technology']] = entry
    lines = ['# Project implementation issues', '',
             'Technology wayfinders for every non-Filament project host. Each issue contains a capability checklist, a technology-specific implementation method and a technical specification summary. Existing Filament programmes remain separate. See the [implementation guide](IMPLEMENTATION-WAYFINDERS.md), [technology specifications](wayfinders/README.md) and [machine-readable register](implementation-wayfinders.json).', '',
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


def find_issue(repository, title):
    issues = json.loads(gh('issue', 'list', '-R', repository, '--state', 'all', '--limit', '1000', '--json', 'number,title,url'))
    matches = [i for i in issues if i['title'] == title]
    if len(matches) > 1:
        raise ValueError(f'Duplicate wayfinders: {repository}')
    return matches[0] if matches else None, issues


def edit_issue_body(repository, number, content):
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', delete=False) as handle:
        handle.write(content)
        path = handle.name
    try:
        subprocess.run(['gh', 'issue', 'edit', str(number), '-R', repository, '--body-file', path], check=True, capture_output=True, text=True)
    finally:
        Path(path).unlink(missing_ok=True)


def create_issue(repository, title, content):
    completed = subprocess.run(
        ['gh', 'issue', 'create', '-R', repository, '--title', title, '--body-file', '-'],
        input=content, text=True, check=True, capture_output=True,
    )
    return completed.stdout.strip()


def catering_body(label, boundary, parent_url, suffix, layer):
    presentation = suffix if suffix.startswith('dart-') else layer
    return f'''## User outcome

Deliver safe event/menu request, quote review/acceptance and confirmation status in {label}. Parent wayfinder: {parent_url}.

## Specifications and dependencies

- [Catering delivery map]({link('projects/ecommerce/CATERING.md')})
- [Core ownership, dependencies and unresolved decisions]({link('projects/ecommerce/core/catering.md')})
- [API contract]({link('projects/ecommerce/api/catering.md')})
- [Presentation plan]({link(f'projects/ecommerce/{presentation}/catering.md')})
- [Technology wayfinder specification]({link(f'projects/wayfinders/{suffix}.md')})
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


def process_target(item, apply=False, sync=False):
    repo, project, slug, suffix, layer, label, profile = item
    assert not repo.endswith('-laravel-filament')
    title = f'Wayfinder: {project} implementation for {label}'
    entry = {'repository': f'liberusoftware/{repo}', 'project': project, 'technology': suffix, 'title': title}
    content = body(project, slug, suffix, layer, label, profile)
    if apply:
        match, issues = find_issue(entry['repository'], title)
        if match:
            entry['url'] = match['url']
            entry['number'] = match['number']
            if sync:
                edit_issue_body(entry['repository'], match['number'], content)
                print(f"synced {entry['url']}", flush=True)
            else:
                print(f"reuse {entry['url']}", flush=True)
        else:
            entry['url'] = create_issue(entry['repository'], title, content)
            print(f"created {entry['url']}", flush=True)
        if project == 'ecommerce':
            child_title = f'Catering: implement {label} workflow after boundary approval'
            child_matches = [i for i in issues if i['title'] == child_title]
            if len(child_matches) > 1:
                raise ValueError(f'Duplicate Catering issues: {repo}')
            child_content = catering_body(label, profile['boundary'], entry['url'], suffix, layer)
            if child_matches:
                entry['cateringIssue'] = child_matches[0]['url']
                if sync:
                    edit_issue_body(entry['repository'], child_matches[0]['number'], child_content)
            else:
                entry['cateringIssue'] = create_issue(entry['repository'], child_title, child_content)
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Create missing issues in GitHub; default is local planning only')
    parser.add_argument('--sync', action='store_true', help='Update bodies of existing wayfinder (and Catering) issues to the current template')
    parser.add_argument('--workers', type=int, default=8, help='Parallel workers for GitHub issue sync')
    parser.add_argument('--output', type=Path, help='Optional plan/register path; dry runs do not overwrite the published register')
    args = parser.parse_args()
    if args.sync and not args.apply:
        parser.error('--sync requires --apply')

    write_wayfinder_docs(ROOT)
    output = args.output or (ROOT/'projects/implementation-wayfinders.json' if args.apply else None)
    all_targets = list(targets())
    if args.apply and args.workers > 1:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            result = list(pool.map(lambda t: process_target(t, args.apply, args.sync), all_targets))
    else:
        result = []
        for t in all_targets:
            result.append(process_target(t, args.apply, args.sync))
            if output:
                serializable = [{k: v for k, v in item.items() if k != 'number'} for item in result]
                output.write_text(json.dumps({'status': 'in_progress' if args.apply else 'planned', 'excludedSuffix': '-laravel-filament', 'wayfinders': serializable}, indent=2)+'\n')
    if output:
        serializable = [{k: v for k, v in item.items() if k != 'number'} for item in result]
        output.write_text(json.dumps({'status': 'published' if args.apply else 'planned', 'excludedSuffix': '-laravel-filament', 'wayfinders': serializable}, indent=2)+'\n')
    if args.apply:
        write_issue_index(result)
    print(f'{len(result)} wayfinders; Filament repositories excluded.')


if __name__ == '__main__':
    main()
