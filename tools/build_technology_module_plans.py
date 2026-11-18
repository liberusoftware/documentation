#!/usr/bin/env python3
"""Enrich every project/module document across all technologies with structured feature matrices, skeleton repository links, API backend integration, and observed source evidence."""
import argparse
import json
from pathlib import Path
import re

from build_source_reference import safe

ROOT = Path(__file__).resolve().parents[1]
PROJECT_SLUGS = {'accounting': 'accounting-erp', 'sap': 'enterprise-sap', 'liberu': 'liberu-official', 'music': 'music-daw'}

FEAT_START = '<!-- feature-technology-matrix:start -->'
FEAT_END = '<!-- feature-technology-matrix:end -->'
CORE_START = '<!-- core-implementation-plan:start -->'
CORE_END = '<!-- core-implementation-plan:end -->'
LAYER_START = '<!-- layer-implementation-plan:start -->'
LAYER_END = '<!-- layer-implementation-plan:end -->'


def scope_file(project: str, stem: str) -> Path:
    for layer in ('features', 'core'):
        path = ROOT / 'projects' / project / layer / f'{stem}.md'
        if path.exists():
            return path
    raise ValueError(f'{project}/{stem}: missing scope document')


def title_for(project: str, stem: str) -> str:
    title = scope_file(project, stem).read_text().splitlines()[0].removeprefix('# ')
    return title.split(': ', 1)[-1].removesuffix(' domain packages').removesuffix(' — Domain specifications')


def scope_labels(project: str, stem: str) -> list[str]:
    content = scope_file(project, stem).read_text()
    section = re.search(r'## (?:2\. Full feature scope|New capabilities|Business capabilities)\n(.*?)(?=\n## |\Z)', content, re.S)
    if section:
        labels = re.findall(r'^- \*\*([^*]+):\*\*', section.group(1), re.M)
        if labels:
            return labels
    cap = re.search(r'\*\*Capability:\*\*\s*(.+)', content)
    if cap:
        raw = re.sub(r'\s+and\s+', ', ', cap.group(1).strip().rstrip('.'))
        return [p.strip().removeprefix('and ').strip().capitalize() for p in raw.split(',') if p.strip()]
    return []


def parse_source_evidence(mapping: dict, project: str, stem: str, canonical_nextjs_path: Path | None = None) -> dict:
    design = mapping.get(project, {}).get('designs', {}).get(stem, {})
    layers = design.get('layers', {})
    queries, commands, controllers = [], [], []
    models, migrations, schemas, filament_links, livewire_links, requests, declared = [], [], [], [], [], [], []
    seen_refs = set()
    for lkey in ('core', 'api', 'filament', 'livewire'):
        for choice in layers.get(lkey, []):
            ref_rel = choice['reference']
            if ref_rel in seen_refs:
                continue
            seen_refs.add(ref_rel)
            ref_path = ROOT / ref_rel
            if not ref_path.is_file():
                continue
            text = ref_path.read_text()
            v1 = text.split('## Variant 2')[0]
            for d in re.findall(r'\*\*Declared features:\*\* (.*)', v1):
                for item in d.split(','):
                    clean = item.strip()
                    if clean and '.' not in clean:
                        declared.append(clean)
            for m in re.finditer(r'^\| (\[([^\]]+)\]\(([^)]+)\)) \| ([^\n]+) \|$', v1, re.M):
                rel_path, url, sigs_raw = m.group(2), m.group(3), m.group(4)
                short_link = f'[{Path(rel_path).name}]({url})'
                if rel_path.startswith('src/Queries/'):
                    queries.append((short_link, sigs_raw))
                elif rel_path.startswith(('src/Actions/', 'src/Services/', 'src/Policies/', 'src/Contracts/')):
                    commands.append((short_link, sigs_raw))
                elif rel_path.startswith('src/Http/Controllers/'):
                    controllers.append((short_link, sigs_raw))
                elif rel_path.startswith(('src/Filament/', 'src/Resources/')):
                    filament_links.append(short_link)
                elif rel_path.startswith('src/Livewire/'):
                    livewire_links.append(short_link)
            for m_other in re.finditer(r'Other non-legacy PHP sources: ([^\n]+)', v1):
                for m_link in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', m_other.group(1)):
                    rel_path, url = m_link.group(1), m_link.group(2)
                    short_link = f'[{Path(rel_path).name}]({url})'
                    if rel_path.startswith('src/Models/'):
                        models.append((short_link, 'No literal fillable array detected; inspect the model and API schema.'))
                    elif rel_path.startswith(('src/Resources/', 'src/Filament/', 'src/Pages/', 'src/Widgets/')) or 'Filament' in rel_path:
                        filament_links.append(short_link)
                    elif rel_path.startswith(('src/Livewire/', 'src/Components/')) or 'Livewire' in rel_path:
                        livewire_links.append(short_link)
                    elif rel_path.startswith('src/Http/Requests/'):
                        requests.append(short_link)
            for m_mig in re.finditer(r'^- (\[(database/migrations/[^\]]+)\]\(([^)]+)\))', v1, re.M):
                migrations.append(f'[{Path(m_mig.group(2)).name}]({m_mig.group(3)})')
            for m_sch in re.finditer(r'^- (\[((?:openapi|schemas)/[^\]]+)\]\(([^)]+)\))', v1, re.M):
                schemas.append(m_sch.group(1))

    routes_block = ''
    api_page = ROOT / 'projects' / project / 'api' / f'{stem}.md'
    if api_page.is_file():
        api_text = api_page.read_text()
        m_rt = re.search(
            r'### Observed route declarations\n\nThese are literal excerpts[^\n]*\n\n(.*?)(?=\n### |\nRequest validation sources:|\nEcommerce also implements|\nA client example is valid)',
            api_text,
            re.S,
        )
        if m_rt:
            routes_block = m_rt.group(1).strip()

    for candidate in filter(None, [ROOT / 'projects' / project / 'nextjs' / f'{stem}.md', canonical_nextjs_path]):
        if not candidate.is_file():
            continue
        ntext = candidate.read_text()
        if not routes_block:
            m_rt = re.search(
                r'### Route source evidence\n\nThe following are literal declaration excerpts[^\n]*\n\n(.*?)(?=\n## )',
                ntext,
                re.S,
            )
            if m_rt:
                routes_block = m_rt.group(1).strip()
        m_mod = re.search(r'\| Source model \| Observed fillable fields \|\n\| --- \| --- \|\n((?:\| [^\n]+\n)+)', ntext)
        if m_mod:
            parsed_models = []
            for row in m_mod.group(1).strip().splitlines():
                parts = [c.strip() for c in row.strip('|').split('|')]
                if len(parts) == 2:
                    parsed_models.append((parts[0], parts[1]))
            if parsed_models:
                models = parsed_models

    return {
        'queries': queries,
        'commands': commands,
        'controllers': controllers,
        'models': models,
        'migrations': migrations,
        'schemas': schemas,
        'filament_links': filament_links,
        'livewire_links': livewire_links,
        'requests': requests,
        'routes_block': routes_block,
        'declared': list(dict.fromkeys(declared)),
    }


def upsert_block(text: str, start_marker: str, end_marker: str, block_body: str) -> str:
    marked = f'{start_marker}\n{block_body.rstrip()}\n{end_marker}'
    if start_marker in text and end_marker in text:
        return re.sub(
            re.escape(start_marker) + r'.*?' + re.escape(end_marker),
            lambda _: marked,
            text,
            flags=re.S,
        )
    walkthrough_match = re.search(r'\nRead the \[source-backed [^\n]+\n*$', text)
    if walkthrough_match:
        idx = walkthrough_match.start()
        return text[:idx].rstrip() + '\n\n' + marked + '\n' + text[idx:]
    return text.rstrip() + '\n\n' + marked + '\n'


def update_bullet_sections(text: str, labels: list[str], layer: str) -> str:
    if len(labels) <= 1:
        return text
    if layer == 'filament':
        surf_lines = [
            f'- **{label}:** resource/table/form/action or page behavior for this module\'s authorized workflow.'
            for label in labels
        ]
        cap_lines = [
            f'- `{re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")}`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.'
            for label in labels
        ]
        text = re.sub(
            r'(## 2\. Module-specific surfaces\n\n)(?:- \*\*[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(surf_lines) + '\n',
            text,
        )
        text = re.sub(
            r'(### Capability mapping\n\n)(?:- `[^`]+`:[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(cap_lines) + '\n',
            text,
        )
    elif layer == 'livewire':
        surf_lines = [
            f'- **{label}:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.'
            for label in labels
        ]
        cap_lines = [
            f'- `{re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")}`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.'
            for label in labels
        ]
        text = re.sub(
            r'(## 2\. Module-specific interactions\n\n)(?:- \*\*[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(surf_lines) + '\n',
            text,
        )
        text = re.sub(
            r'(### Capability mapping\n\n)(?:- `[^`]+`:[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(cap_lines) + '\n',
            text,
        )
    elif layer in ('react', 'vue'):
        fw = 'React' if layer == 'react' else 'Vue'
        surf_lines = [
            f'- **{label}:** page, component, hook, form, and failure-state behavior for this module\'s authorized workflow.'
            for label in labels
        ]
        cap_lines = [
            f'- `{re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")}`: map the matching API query/action to a focused {fw} page, component, hook, or Inertia form.'
            for label in labels
        ]
        text = re.sub(
            r'(## 2\. Module-specific surfaces\n\n)(?:- \*\*[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(surf_lines) + '\n',
            text,
        )
        text = re.sub(
            r'(### Capability mapping\n\n)(?:- `[^`]+`:[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(cap_lines) + '\n',
            text,
        )
    elif layer == 'nuxt':
        surf_lines = [
            f'- **{label}:** page/component/composable/API-action behavior for this module\'s authorized workflow.'
            for label in labels
        ]
        cap_lines = [
            f'- `{re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")}`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.'
            for label in labels
        ]
        text = re.sub(
            r'(## 2\. Module-specific surfaces\n\n)(?:- \*\*[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(surf_lines) + '\n',
            text,
        )
        text = re.sub(
            r'(### Capability mapping\n\n)(?:- `[^`]+`:[^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(cap_lines) + '\n',
            text,
        )
    elif layer == 'api':
        api_lines = [f'- {label}' for label in labels]
        text = re.sub(
            r'(The domain capability includes:\n\n)(?:- [^\n]+\n)+',
            lambda m: m.group(1) + '\n'.join(api_lines) + '\n',
            text,
        )
    return text


def format_skel(skel: dict | None, fallback_name: str) -> str:
    if skel and skel.get('state') in ('published', 'verified-existing'):
        return f'[`{skel["repository"]}`](https://github.com/liberusoftware/{skel["repository"]}) (`{skel["intendedPackageIdentity"]}`)'
    if skel:
        return f'`{skel["repository"]}` (`{skel["intendedPackageIdentity"]}`)'
    return f'`{fallback_name}`'


def render_source_evidence_block(
    ev: dict,
    include_routes: bool = True,
    extra_title: str = '',
    extra_links: list[str] | None = None,
) -> list[str]:
    lines = ['### Observed domain and transport source evidence', '']
    queries = ev['queries']
    commands = ev['commands']
    models = ev['models']
    controllers = ev['controllers']
    routes_block = ev['routes_block'] if include_routes else ''
    if not (queries or commands or models or controllers or routes_block or extra_links):
        lines += [
            'No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.',
            '',
        ]
        return lines
    if extra_links:
        lines += [
            f'**Observed {extra_title} files:** ' + ' · '.join(extra_links[:14]) + '.',
            '',
        ]
    if queries:
        lines += ['| Observed core query | Public method signatures |', '| --- | --- |']
        for link_md, sigs_raw in queries[:8]:
            lines.append(f'| {link_md} | {sigs_raw} |')
        lines.append('')
    if commands:
        lines += ['| Observed core action / service / policy | Public method signatures |', '| --- | --- |']
        for link_md, sigs_raw in commands[:10]:
            lines.append(f'| {link_md} | {sigs_raw} |')
        lines.append('')
    if models:
        lines += ['| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |', '| --- | --- |']
        for link_md, fields_txt in models[:8]:
            lines.append(f'| {link_md} | {fields_txt} |')
        lines.append('')
    if controllers and include_routes:
        lines += ['| Observed API controller | Handler signatures |', '| --- | --- |']
        for link_md, sigs_raw in controllers[:8]:
            lines.append(f'| {link_md} | {sigs_raw} |')
        lines.append('')
    if routes_block:
        lines += ['**Observed route declarations:**', '', routes_block, '']
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects', type=Path, default=Path('/tmp/liberu-documentation-sources'))
    parser.parse_args()

    mapping = json.loads((ROOT / 'architecture/source-design-mapping.json').read_text())['projects']
    skeletons_raw = json.loads((ROOT / 'architecture/module-skeleton-repositories.json').read_text())['repositories']
    skeleton_lookup = {(r['capabilityKey'], r['presentation']): r for r in skeletons_raw}
    nextjs_groups = json.loads((ROOT / 'architecture/nextjs-adapter-plans.json').read_text()).get('groups', {})

    files_updated = 0

    for project, project_info in sorted(mapping.items()):
        slug = PROJECT_SLUGS.get(project, project)
        for stem, design in sorted(project_info['designs'].items()):
            title = title_for(project, stem)
            domain_mod = design.get('design_alias') or stem
            core = design['layers']['core']
            cap_key = core[0]['identity'] if len(core) == 1 else (f'liberusoftware/music-{stem}' if project == 'music' else f'planned:{project}:{stem}')
            base_mod = (core[0]['identity'].split('/')[-1].removeprefix('module-') if len(core) == 1 else f'{project}-{stem}')
            canonical_home_rel = nextjs_groups.get(cap_key, {}).get('home')
            canonical_home = (ROOT / canonical_home_rel) if canonical_home_rel else None

            ev = parse_source_evidence(mapping, project, stem, canonical_home)
            labels = scope_labels(project, stem) or ev['declared'] or [title]

            sk_fil = format_skel(skeleton_lookup.get((cap_key, 'laravel-filament')), f'module-{base_mod}-filament')
            sk_react = format_skel(skeleton_lookup.get((cap_key, 'laravel-inertia-react')), f'module-{base_mod}-react-inertia')
            sk_vue = format_skel(skeleton_lookup.get((cap_key, 'laravel-inertia-vue')), f'module-{base_mod}-vue-inertia')
            sk_nuxt = format_skel(skeleton_lookup.get((cap_key, 'nuxt-vue')), f'module-{base_mod}-nuxt')
            sk_next = format_skel(skeleton_lookup.get((cap_key, 'next-react')), f'module-{base_mod}-nextjs')
            sk_rn = format_skel(skeleton_lookup.get((cap_key, 'mobile-react')), f'module-{base_mod}-react-native')
            sk_fl = format_skel(skeleton_lookup.get((cap_key, 'mobile-flutter')), f'module-{base_mod}-flutter')
            sk_dm = format_skel(skeleton_lookup.get((cap_key, 'dart-mobile')), f'module-{base_mod}-dart-mobile')
            sk_dd = format_skel(skeleton_lookup.get((cap_key, 'dart-desktop')), f'module-{base_mod}-dart-desktop')

            # 1. features/<stem>.md
            feat_path = ROOT / 'projects' / project / 'features' / f'{stem}.md'
            if feat_path.exists() and '<!-- documentation-kind: source-index -->' not in feat_path.read_text():
                feat_lines = [
                    '## Cross-technology implementation plan and feature matrix',
                    '',
                    'Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module\'s persistence.',
                    '',
                    '### Feature and domain aspect breakdown',
                    '',
                    '| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    feat_lines.append(
                        f'| **{safe(lbl)}** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `{safe(lbl.lower())}`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |'
                    )
                feat_lines += [
                    '',
                    '### Technology delivery matrix',
                    '',
                    '| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |',
                    '| --- | --- | --- | --- |',
                    f'| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/{stem}.md) | [Source map](../SOURCE-MAPPING.md#{stem}) | Authoritative domain model, actions, queries, policies, migrations, and events |',
                    f'| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/{stem}.md) | [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |',
                    f'| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/{stem}.md) | [`project-{slug}-laravel-filament`](https://github.com/liberusoftware/project-{slug}-laravel-filament) · {sk_fil} | Resources, schemas, tables, infolists, widgets, and panel actions |',
                    f'| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/{stem}.md) | [`project-{slug}-laravel-filament`](https://github.com/liberusoftware/project-{slug}-laravel-filament) | Server-driven reactive components and namespaced default Blade views |',
                    f'| React 19.2 + Inertia 3 | [React Inertia plan](../react/{stem}.md) | [`project-{slug}-laravel-inertia-react`](https://github.com/liberusoftware/project-{slug}-laravel-inertia-react) · {sk_react} | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |',
                    f'| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/{stem}.md) | [`project-{slug}-laravel-inertia-vue`](https://github.com/liberusoftware/project-{slug}-laravel-inertia-vue) · {sk_vue} | Laravel session/CSRF routes with Vue SFC pages and shared composables |',
                    f'| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/{stem}.md) | [`project-{slug}-nuxt-vue`](https://github.com/liberusoftware/project-{slug}-nuxt-vue) · {sk_nuxt} | Standalone Vue SSR client consuming `project-{slug}-laravel-api` with isolated caches |',
                    f'| Next.js + React 19.2 | [Next.js plan](../nextjs/{stem}.md) | [`project-{slug}-next-react`](https://github.com/liberusoftware/project-{slug}-next-react) · {sk_next} | App Router Server/Client components consuming `project-{slug}-laravel-api` |',
                    f'| React Native + Expo | [React Native plan](../react-native/{stem}.md) | [`project-{slug}-mobile-react`](https://github.com/liberusoftware/project-{slug}-mobile-react) · {sk_rn} | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |',
                    f'| Flutter mobile | [Flutter plan](../flutter/{stem}.md) | [`project-{slug}-mobile-flutter`](https://github.com/liberusoftware/project-{slug}-mobile-flutter) · {sk_fl} | Native iOS/Android Dart/Flutter widgets and typed repository client |',
                    f'| Dart mobile & desktop | [Flutter & Dart plan](../flutter/{stem}.md) | [`project-{slug}-dart-mobile`](https://github.com/liberusoftware/project-{slug}-dart-mobile) · {sk_dm}<br>[`project-{slug}-dart-desktop`](https://github.com/liberusoftware/project-{slug}-dart-desktop) · {sk_dd} | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |',
                ]
                orig = feat_path.read_text()
                updated = upsert_block(orig, FEAT_START, FEAT_END, '\n'.join(feat_lines))
                if updated != orig:
                    feat_path.write_text(updated)
                    files_updated += 1

            # 2. core/<stem>.md
            core_path = ROOT / 'projects' / project / 'core' / f'{stem}.md'
            if core_path.exists() and '<!-- documentation-kind: source-index -->' not in core_path.read_text():
                core_lines = [
                    '## Module features, domain aspects, and source architecture',
                    '',
                    '### Feature and domain aspect implementation matrix',
                    '',
                    '| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    core_lines.append(
                        f'| **{safe(lbl)}** | Model `{safe(lbl.lower())}` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |'
                    )
                core_lines += ['']
                core_lines += render_source_evidence_block(
                    ev, include_routes=False, extra_title='migration', extra_links=ev['migrations']
                )
                core_lines += [
                    '### Consuming adapter specifications',
                    '',
                    f'- [HTTP API contract](../api/{stem}.md) · [Filament 5](../filament/{stem}.md) · [Livewire 4](../livewire/{stem}.md) · [React + Inertia](../react/{stem}.md) · [Vue + Inertia](../vue/{stem}.md) · [Nuxt 4](../nuxt/{stem}.md) · [Next.js](../nextjs/{stem}.md) · [React Native](../react-native/{stem}.md) · [Flutter & Dart](../flutter/{stem}.md)',
                ]
                orig = core_path.read_text()
                updated = upsert_block(orig, CORE_START, CORE_END, '\n'.join(core_lines))
                if updated != orig:
                    core_path.write_text(updated)
                    files_updated += 1

            # 3. api/<stem>.md (update bullets + add block for music/catering where improve_api_source_contracts is custom)
            api_path = ROOT / 'projects' / project / 'api' / f'{stem}.md'
            if api_path.exists() and '<!-- documentation-kind: source-index -->' not in api_path.read_text():
                orig = api_path.read_text()
                updated = update_bullet_sections(orig, labels, 'api')
                if project == 'music' or (project == 'ecommerce' and stem == 'catering'):
                    api_extra = [
                        '## Product API backend and feature-to-operation plan',
                        '',
                        f'This API contract is composed into [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) ([Laravel API backends](../../../guides/LARAVEL-API-BACKENDS.md)) to serve [`project-{slug}-next-react`](https://github.com/liberusoftware/project-{slug}-next-react), [`project-{slug}-nuxt-vue`](https://github.com/liberusoftware/project-{slug}-nuxt-vue), [`project-{slug}-mobile-react`](https://github.com/liberusoftware/project-{slug}-mobile-react), [`project-{slug}-mobile-flutter`](https://github.com/liberusoftware/project-{slug}-mobile-flutter), [`project-{slug}-dart-mobile`](https://github.com/liberusoftware/project-{slug}-dart-mobile), and [`project-{slug}-dart-desktop`](https://github.com/liberusoftware/project-{slug}-dart-desktop).',
                        '',
                        '| Feature / aspect | HTTP query and command contract | DTO projection, concurrency & error semantics |',
                        '| --- | --- | --- |',
                    ]
                    for lbl in labels:
                        api_extra.append(
                            f'| **{safe(lbl)}** | Expose workspace-scoped read query and explicit command endpoint for `{safe(lbl.lower())}` delegating to the core domain owner. | Audience-safe `snake_case` DTO allowlist; `Idempotency-Key` and revision preconditions (`If-Match`) for mutations; RFC 9457 Problem Details errors. |'
                        )
                    updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(api_extra))
                if updated != orig:
                    api_path.write_text(updated)
                    files_updated += 1

            # 4. filament/<stem>.md
            fil_path = ROOT / 'projects' / project / 'filament' / f'{stem}.md'
            if fil_path.exists() and '<!-- documentation-kind: source-index -->' not in fil_path.read_text():
                orig = fil_path.read_text()
                updated = update_bullet_sections(orig, labels, 'filament')
                fil_lines = [
                    '## Structured feature plan, repository skeleton, and source evidence',
                    '',
                    '| Delivery boundary | Repository / specification | Responsibility |',
                    '| --- | --- | --- |',
                    f'| Product Filament host | [`project-{slug}-laravel-filament`](https://github.com/liberusoftware/project-{slug}-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |',
                    f'| Capability Filament package | {sk_fil} | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |',
                    f'| Authoritative domain owner | [Core plan](../core/{stem}.md) · [API plan](../api/{stem}.md) | Domain actions, queries, policies, and persistence |',
                    '',
                    '### Filament 5 feature and surface matrix',
                    '',
                    '| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    fil_lines.append(
                        f'| **{safe(lbl)}** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `{safe(lbl.lower())}`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |'
                    )
                fil_lines += ['']
                fil_lines += render_source_evidence_block(
                    ev, include_routes=False, extra_title='Filament class', extra_links=ev['filament_links']
                )
                updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(fil_lines))
                if updated != orig:
                    fil_path.write_text(updated)
                    files_updated += 1

            # 5. livewire/<stem>.md
            lw_path = ROOT / 'projects' / project / 'livewire' / f'{stem}.md'
            if lw_path.exists() and '<!-- documentation-kind: source-index -->' not in lw_path.read_text():
                orig = lw_path.read_text()
                updated = update_bullet_sections(orig, labels, 'livewire')
                lw_lines = [
                    '## Structured feature plan, view resolution contract, and source evidence',
                    '',
                    '| Delivery boundary | Repository / specification | Responsibility |',
                    '| --- | --- | --- |',
                    f'| Product Laravel host | [`project-{slug}-laravel-filament`](https://github.com/liberusoftware/project-{slug}-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |',
                    f'| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |',
                    f'| Authoritative domain owner | [Core plan](../core/{stem}.md) · [API plan](../api/{stem}.md) | Domain actions, queries, policies, and persistence |',
                    '',
                    '### Livewire 4 feature and component matrix',
                    '',
                    '| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    lw_lines.append(
                        f'| **{safe(lbl)}** | Expose a focused Livewire 4 component and namespaced Blade default view for `{safe(lbl.lower())}` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |'
                    )
                lw_lines += ['']
                lw_lines += render_source_evidence_block(
                    ev, include_routes=False, extra_title='Livewire / view', extra_links=ev['livewire_links']
                )
                updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(lw_lines))
                if updated != orig:
                    lw_path.write_text(updated)
                    files_updated += 1

            # 6. react/<stem>.md (Laravel + Inertia + React)
            react_path = ROOT / 'projects' / project / 'react' / f'{stem}.md'
            if react_path.exists() and '<!-- documentation-kind: source-index -->' not in react_path.read_text():
                orig = react_path.read_text()
                updated = update_bullet_sections(orig, labels, 'react')
                react_lines = [
                    '## Structured feature plan, skeleton repository, and source evidence',
                    '',
                    '| Delivery boundary | Repository / specification | Role in implementation |',
                    '| --- | --- | --- |',
                    f'| Product Inertia React host skeleton | [`project-{slug}-laravel-inertia-react`](https://github.com/liberusoftware/project-{slug}-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |',
                    f'| Capability React Inertia module skeleton | {sk_react} | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |',
                    f'| Shared React reuse | [Next.js plan](../nextjs/{stem}.md) · [Core plan](../core/{stem}.md) · [API plan](../api/{stem}.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |',
                    '',
                    '### React 19.2 + Inertia 3 feature and component matrix',
                    '',
                    '| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    react_lines.append(
                        f'| **{safe(lbl)}** | Render `{safe(lbl.lower())}` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |'
                    )
                react_lines += ['']
                react_lines += render_source_evidence_block(ev, include_routes=True)
                updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(react_lines))
                if updated != orig:
                    react_path.write_text(updated)
                    files_updated += 1

            # 7. vue/<stem>.md (Laravel + Inertia + Vue)
            vue_path = ROOT / 'projects' / project / 'vue' / f'{stem}.md'
            if vue_path.exists() and '<!-- documentation-kind: source-index -->' not in vue_path.read_text():
                orig = vue_path.read_text()
                updated = update_bullet_sections(orig, labels, 'vue')
                vue_lines = [
                    '## Structured feature plan, skeleton repository, and source evidence',
                    '',
                    '| Delivery boundary | Repository / specification | Role in implementation |',
                    '| --- | --- | --- |',
                    f'| Product Inertia Vue host skeleton | [`project-{slug}-laravel-inertia-vue`](https://github.com/liberusoftware/project-{slug}-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |',
                    f'| Capability Vue Inertia module skeleton | {sk_vue} | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |',
                    f'| Shared Vue reuse | [Nuxt plan](../nuxt/{stem}.md) · [Core plan](../core/{stem}.md) · [API plan](../api/{stem}.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |',
                    '',
                    '### Vue 3 + Inertia 3 feature and component matrix',
                    '',
                    '| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    vue_lines.append(
                        f'| **{safe(lbl)}** | Render `{safe(lbl.lower())}` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |'
                    )
                vue_lines += ['']
                vue_lines += render_source_evidence_block(ev, include_routes=True)
                updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(vue_lines))
                if updated != orig:
                    vue_path.write_text(updated)
                    files_updated += 1

            # 8. nuxt/<stem>.md (Nuxt 4 + Vue 3)
            nuxt_path = ROOT / 'projects' / project / 'nuxt' / f'{stem}.md'
            if nuxt_path.exists() and '<!-- documentation-kind: source-index -->' not in nuxt_path.read_text():
                orig = nuxt_path.read_text()
                updated = update_bullet_sections(orig, labels, 'nuxt')
                nuxt_lines = [
                    '## Structured feature plan, skeleton repository, and source evidence',
                    '',
                    '| Delivery boundary | Repository / specification | Role in implementation |',
                    '| --- | --- | --- |',
                    f'| Product Nuxt 4 host skeleton | [`project-{slug}-nuxt-vue`](https://github.com/liberusoftware/project-{slug}-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |',
                    f'| Shared product API backend | [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/{stem}.md)) |',
                    f'| Capability Nuxt module skeleton | {sk_nuxt} | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |',
                    '',
                    '### Nuxt 4 feature, SSR, and API integration matrix',
                    '',
                    '| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    nuxt_lines.append(
                        f'| **{safe(lbl)}** | Expose composable and Vue 3 component for `{safe(lbl.lower())}` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/{stem}.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-{slug}-laravel-api`. |'
                    )
                nuxt_lines += ['']
                nuxt_lines += render_source_evidence_block(ev, include_routes=True)
                updated = upsert_block(updated, LAYER_START, LAYER_END, '\n'.join(nuxt_lines))
                if updated != orig:
                    nuxt_path.write_text(updated)
                    files_updated += 1

            # 9. Authored nextjs/<stem>.md (when not generated by build_nextjs_plans.py)
            next_path = ROOT / 'projects' / project / 'nextjs' / f'{stem}.md'
            if next_path.exists():
                orig = next_path.read_text()
                if '<!-- nextjs-plan:generated -->' not in orig and '<!-- documentation-kind: source-index -->' not in orig:
                    next_lines = [
                        '## Structured feature plan, skeleton repository, and backend integration',
                        '',
                        f'**Matching domain module:** `{domain_mod}`',
                        '',
                        '| Delivery boundary | Repository / specification | Role in implementation |',
                        '| --- | --- | --- |',
                        f'| Product Next.js host skeleton | [`project-{slug}-next-react`](https://github.com/liberusoftware/project-{slug}-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |',
                        f'| Shared product API backend | [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/{stem}.md)) |',
                        f'| Capability Next.js module skeleton | {sk_next} | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |',
                        '',
                        '### Next.js feature and component matrix',
                        '',
                        '| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |',
                        '| --- | --- | --- |',
                    ]
                    for lbl in labels:
                        next_lines.append(
                            f'| **{safe(lbl)}** | Server Component fetches authorized `{safe(lbl.lower())}` DTOs; Client Component (`\'use client\'`) handles interaction, focus, and form state. | Call `project-{slug}-laravel-api` with `cache: \'no-store\'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |'
                        )
                    updated = upsert_block(orig, LAYER_START, LAYER_END, '\n'.join(next_lines))
                    if updated != orig:
                        next_path.write_text(updated)
                        files_updated += 1

            # 10. react-native/<stem>.md (React Native + Expo)
            rn_path = ROOT / 'projects' / project / 'react-native' / f'{stem}.md'
            if rn_path.exists() and '<!-- documentation-kind: source-index -->' not in rn_path.read_text():
                orig = rn_path.read_text()
                rn_lines = [
                    '## Structured mobile feature plan, skeleton repository, and source evidence',
                    '',
                    f'**Matching domain module:** `{domain_mod}`',
                    '',
                    '| Delivery boundary | Repository / specification | Role in implementation |',
                    '| --- | --- | --- |',
                    f'| Product React Native Expo host skeleton | [`project-{slug}-mobile-react`](https://github.com/liberusoftware/project-{slug}-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |',
                    f'| Shared product API backend | [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/{stem}.md)) |',
                    f'| Capability React Native module skeleton | {sk_rn} | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |',
                    '',
                    '### React Native + Expo feature and mobile screen matrix',
                    '',
                    '| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |',
                    '| --- | --- | --- |',
                ]
                for lbl in labels:
                    rn_lines.append(
                        f'| **{safe(lbl)}** | Progressive mobile list/detail/sheet flow for `{safe(lbl.lower())}` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-{slug}-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |'
                    )
                rn_lines += ['']
                rn_lines += render_source_evidence_block(ev, include_routes=True)
                updated = upsert_block(orig, LAYER_START, LAYER_END, '\n'.join(rn_lines))
                if updated != orig:
                    rn_path.write_text(updated)
                    files_updated += 1

            # 11. flutter/<stem>.md (Flutter mobile, Dart mobile, and Dart desktop)
            fl_path = ROOT / 'projects' / project / 'flutter' / f'{stem}.md'
            if fl_path.exists() and '<!-- documentation-kind: source-index -->' not in fl_path.read_text():
                orig = fl_path.read_text()
                fl_lines = [
                    '## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan',
                    '',
                    f'**Matching domain module:** `{domain_mod}`',
                    '',
                    'This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-' + slug + '-laravel-api`](https://github.com/liberusoftware/project-' + slug + '-laravel-api).',
                    '',
                    '| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |',
                    '| --- | --- | --- | --- |',
                    f'| Flutter mobile (`iOS` / `Android`) | [`project-{slug}-mobile-flutter`](https://github.com/liberusoftware/project-{slug}-mobile-flutter) | {sk_fl} | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |',
                    f'| Dart mobile (`iOS` / `Android`) | [`project-{slug}-dart-mobile`](https://github.com/liberusoftware/project-{slug}-dart-mobile) | {sk_dm} | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |',
                    f'| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-{slug}-dart-desktop`](https://github.com/liberusoftware/project-{slug}-dart-desktop) | {sk_dd} | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |',
                    f'| Shared product API backend | [`project-{slug}-laravel-api`](https://github.com/liberusoftware/project-{slug}-laravel-api) | [API plan](../api/{stem}.md) · [Core plan](../core/{stem}.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |',
                    '',
                    '### Feature and aspect matrix across mobile and desktop hosts',
                    '',
                    '| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |',
                    '| --- | --- | --- | --- |',
                ]
                for lbl in labels:
                    fl_lines.append(
                        f'| **{safe(lbl)}** | Adaptive mobile cards/sheets for `{safe(lbl.lower())}` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `{safe(lbl.lower())}` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-{slug}-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |'
                    )
                fl_lines += ['']
                fl_lines += render_source_evidence_block(ev, include_routes=True)
                updated = upsert_block(orig, LAYER_START, LAYER_END, '\n'.join(fl_lines))
                if updated != orig:
                    fl_path.write_text(updated)
                    files_updated += 1

    print(f'Enriched {files_updated} module documents across all technologies and projects.')


if __name__ == '__main__':
    main()
