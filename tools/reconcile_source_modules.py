#!/usr/bin/env python3
"""Connect existing designs to observed identities, keeping unmatched scopes intact."""
import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LAYERS = ('features', 'core', 'api', 'filament', 'livewire', 'react', 'vue', 'nuxt', 'react-native', 'flutter', 'nextjs')
FOUNDATION_ALIASES = {
    'activity-and-comments': 'activity-comments', 'application-core': 'application',
    'files-and-media': 'files-media', 'google-analytics': 'analytics-google',
    'identity': 'identity-core', 'import-and-export': 'import-export',
    'localization': 'localization-core', 'meta-server-side-tracking': 'analytics-meta',
    'organizations-and-teams': 'organizations-teams', 'roles-and-permissions': 'roles-permissions',
    'scheduler-and-queues': 'scheduler-queues', 'sessions-and-devices': 'sessions-devices',
}
START = '<!-- source-reconciliation:start -->'
END = '<!-- source-reconciliation:end -->'


def normalized(value, project):
    previous = None
    while previous != value:
        previous = value
        value = value.removeprefix('module-').removeprefix(project + '-')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-annotate', action='store_true', help='Rebuild maps without updating existing module documents')
    args = parser.parse_args()
    snapshot = json.loads((ROOT / 'architecture/source-inventory.json').read_text())
    references = json.loads((ROOT / 'architecture/source-reference-index.json').read_text())['packages']
    source_projects = {r['project']: r for r in snapshot['repositories']}
    result = {}
    annotations = 0
    for project in sorted((ROOT / 'projects').iterdir()):
        if not (project / 'features').is_dir():
            continue
        record = source_projects.get(project.name)
        available = []
        if record:
            for m in record['modules']:
                if m.get('alias_of'):
                    continue
                identity = m['manifests'].get('composer.json', {}).get('name') or m['manifests'].get('package.json', {}).get('name')
                if identity:
                    available.append((m['directory'], identity))
        slugs = sorted({p.stem for layer in LAYERS for p in (project/layer).glob('*.md') if p.name != 'README.md'})
        matches = {}
        mapped = set()
        for feature in slugs:
            base = FOUNDATION_ALIASES.get(feature, feature) if project.name == 'boilerplate' else feature
            group = {}
            for layer in ('core', 'api', 'filament', 'livewire', 'react', 'vue', 'nuxt', 'react-native', 'flutter', 'nextjs'):
                suffix = '' if layer == 'core' else {'react': '-react-inertia', 'vue': '-vue-inertia'}.get(layer, '-' + layer)
                target = base + suffix
                scored = []
                for directory, identity in available:
                    score = 100 if directory == target else 95 if directory == 'module-' + target else 90 if directory == project.name + '-' + target else 85 if directory == 'module-' + project.name + '-' + target else 60 if normalized(directory, project.name) == normalized(target, project.name) else 0
                    if score:
                        scored.append((score, directory, identity))
                best = max((s for s, _, _ in scored), default=0)
                choices = [{'directory': directory, 'identity': identity, 'reference': references[identity]['reference']} for score, directory, identity in scored if score == best]
                group[layer] = choices
                mapped.update(c['directory'] for c in choices)
            matches[feature] = {'design_alias': base if base != feature else None, 'layers': group}
        unmapped = [{'directory': directory, 'identity': identity, 'reference': references[identity]['reference']} for directory, identity in available if directory not in mapped]
        result[project.name] = {'repository': record['repository'] if record else None, 'designs': matches, 'unmapped_observed_packages': unmapped}
        lines = [f'# {project.name.replace("-", " ").title()}: design and source reconciliation', '',
                 'This map connects existing design filenames to observed package identities. Matching is based on exact/local naming patterns plus the documented foundation aliases below; it is navigation evidence, not proof of equivalent behavior or complete implementation. Read the source reference before using a proposed field, endpoint, permission or installation example.', '',
                 '**Preservation rule:** all existing product scopes and module documents remain in place. A blank package match means only that this scan did not find a dedicated manifest under the expected naming pattern; implementation can exist elsewhere or use another identity.', '']
        if project.name == 'ecommerce':
            lines += ['Ecommerce has application-owned implementations outside the immediate package folder. Use the [application capability map](SOURCE-APPLICATION.md) and retain the [full catalogue](ECOMMERCE.md). Every blank row below preserves the existing module design; it is not a recommendation to remove that module.', '']
        elif not record:
            lines += ['No corresponding application repository was included in the requested `liberusoftware/*-laravel` discovery set. Use the enterprise/platform composition documents and owning product sources rather than inventing a source package.', '']
        else:
            lines += ['See the [project inventory](SOURCE-MODULES.md) for source commits, compatibility aliases and application-owned source roots.', '']
        if project.name == 'liberu':
            lines += ['Existing platform code is present in other application trees. The [cross-project reuse guide](REUSE.md) records the two identity families, namespaces and tables; a missing direct application match here must not be interpreted as no implementation or a need for a third owner.', '']
        lines += ['## Read the mapping', '',
                  'Core/API/Filament/Livewire columns show dedicated observed identities where names match. JavaScript/mobile source matches are recorded in the JSON index and individual annotations when present. An adapter can also be application-owned or ship assets through a PHP package; absence of a dedicated npm manifest does not establish absence of UI.', '',
                  'Multiple matches are left visible for review. Repeated design spellings may point to the same package; they must not become independent competing owners. Installation uses the observed manifest name, not a generated design slug.', '',
                  '| Design scope | Core source reference | API source reference | Filament source reference | Livewire source reference |',
                  '| --- | --- | --- | --- | --- |']
        for feature, info in matches.items():
            feature_path = next((project/layer/f'{feature}.md' for layer in ('features', 'core') if (project/layer/f'{feature}.md').exists()), None)
            label = f'[{feature}]({feature_path.relative_to(project)})' if feature_path else feature
            label = f'<a id="{feature}"></a>{label}'
            cells = []
            for layer in ('core', 'api', 'filament', 'livewire'):
                choices = info['layers'][layer]
                cells.append(' · '.join(f'[{c["identity"]}]({os.path.relpath(ROOT/c["reference"], project)})' for c in choices) or 'No dedicated name match')
            lines.append('| ' + ' | '.join([label] + cells) + ' |')
        if project.name == 'boilerplate':
            lines += ['', '## Retained foundation design aliases', '',
                      'These 12 older core/adapter spellings map to the current foundation names below. Their documents are retained as compatibility navigation, not new independent capabilities. Current source identities and requirements are in the reference links.', '',
                      '| Retained spelling | Current design spelling |', '| --- | --- |']
            for alias, canonical in FOUNDATION_ALIASES.items():
                lines.append(f'| `{alias}` | [{canonical}](features/{canonical}.md) |')
        lines += ['', '## Observed packages without a design-name match', '',
                  'These package references document observed modules even when an existing feature filename did not match. Review their capabilities, call sites and ownership before deciding whether to extend an existing feature or add a distinct product capability. They are not silently omitted or merged by this tool.', '',
                  '| Actual directory | Manifest identity and implementation reference |', '| --- | --- |']
        if project.name == 'sap' and unmapped:
            lines[-2:-2] = ['The current SAP host installs shared foundation packages. Their presence here is a reuse relationship, not a requirement to create another SAP-owned feature for each foundation module. Use the [foundation source map](../boilerplate/SOURCE-MAPPING.md), [shared implementation references](../../modules/source/README.md), and [current SAP foundation guide](SOURCE-APPLICATION.md).', '']
        if unmapped:
            for item in unmapped:
                lines.append(f'| `{item["directory"]}` | [{item["identity"]}]({os.path.relpath(ROOT/item["reference"], project)}) |')
        else:
            lines.append('| — | No unmatched dedicated package identities in this scan |')
        lines += ['', 'Reproduce with `python3 tools/reconcile_source_modules.py` after rebuilding the inventory and package references. The [machine-readable mapping](../../architecture/source-design-mapping.json) includes every layer match. Follow the [reuse guide](../../architecture/SHARED-MODULES.md), [Composer lifecycle](../../guides/COMPOSER.md) and [npm lifecycle](../../guides/NPM.md) when implementing or adopting a module.', '']
        (project/'SOURCE-MAPPING.md').write_text('\n'.join(lines))
        if not args.no_annotate:
            for layer in LAYERS:
                for path in sorted((project/layer).glob('*.md')):
                    if path.name == 'README.md' or path.stem not in matches:
                        continue
                    info = matches[path.stem]
                    choices = info['layers']['core' if layer == 'features' else layer]
                    map_link = f'../SOURCE-MAPPING.md#{path.stem}'
                    note = f'**Source reconciliation:** [design-to-source map]({map_link}). '
                    if choices:
                        note += 'Observed identity: ' + ' · '.join(f'[`{c["identity"]}`]({os.path.relpath(ROOT/c["reference"], path.parent)})' for c in choices) + '. '
                        if len(choices)>1:
                            note += 'Multiple source candidates require ownership review. '
                    elif project.name == 'ecommerce':
                        note += 'Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. '
                    else:
                        note += 'No dedicated package name match was found for this layer in the scanned module manifests. '
                    if info['design_alias']:
                        note += f'This retained spelling maps to `{info["design_alias"]}`; it is not another independent module. '
                    note += 'Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.'
                    block = START + '\n' + note + '\n' + END
                    original = path.read_text()
                    if START in original:
                        updated = re.sub(re.escape(START)+r'.*?'+re.escape(END), lambda _: block, original, flags=re.S)
                    else:
                        title, rest = original.split('\n',1)
                        updated = title + '\n\n' + block + '\n' + rest
                    updated = re.sub(r'\*\*Composer package:\*\* `([^`/]+)`', r'**Design package identifier:** `\1`', updated)
                    if updated != original:
                        path.write_text(updated)
                        annotations += 1
        readme = project/'README.md'
        if readme.exists() and '(SOURCE-MAPPING.md)' not in readme.read_text():
            readme.write_text(readme.read_text()+'\n- [Design-to-source reconciliation](SOURCE-MAPPING.md) — exact package identities, retained aliases, unmatched observed modules, and source implementation references.\n')
    (ROOT/'architecture/source-design-mapping.json').write_text(json.dumps({'projects': result},indent=2)+'\n')
    print(f'Reconciled {sum(len(r["designs"]) for r in result.values())} design spellings across {len(result)} projects; updated {annotations} source annotations.')
    print(f'Observed physical package locations without a design-name match: {sum(len(r["unmapped_observed_packages"]) for r in result.values())}')


if __name__ == '__main__':
    main()
