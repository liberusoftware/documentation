#!/usr/bin/env python3
"""Create only Catering issues and append their links to Ecommerce Filament #925."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = 'liberusoftware/project-ecommerce-laravel-filament'
DOCS = 'https://github.com/liberusoftware/documentation/blob/main/projects/ecommerce/'


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()


def create(title, body, known):
    matches = [i for i in known if i['title'] == title]
    if len(matches)>1:
        raise ValueError('Duplicate Catering title: '+title)
    if matches:
        return matches[0]['url']
    return subprocess.run(['gh', 'issue', 'create', '-R', REPO, '--title', title, '--body-file', '-'], input=body, text=True, check=True, capture_output=True).stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    plans = json.loads((ROOT/'projects/implementation-wayfinders.json').read_text())
    if plans['status'] != 'published' or len(plans['wayfinders']) != 128 or sum('cateringIssue' in e for e in plans['wayfinders']) != 8:
        raise ValueError('Finish the 128 non-Filament wayfinders and eight Catering children first.')
    title = 'Architecture: Ecommerce — Catering'
    common = f'''## Approved scope and dependencies

Upstream boundary request: https://github.com/liberusoftware/documentation/issues/26.
[Core ownership, public boundaries and open decisions]({DOCS}core/catering.md), [delivery map]({DOCS}CATERING.md).

This is planning work until the upstream ownership, required-versus-optional Quotes/Bookings dependencies, quote/menu snapshot ownership and authoritative order-conversion transition are accepted. Schema and implementation remain blocked until those decisions are recorded. Proposed domain source is `module-ecommerce-catering`, Composer `liberusoftware/ecommerce-catering`, namespace `Liberu\\Ecommerce\\Catering\\`. Do not create host-only catering rules or duplicate Catalog, Cart, Pricing, generic quote negotiation, scheduling, Orders or Payments. Verify actual published public contracts and directional, version-constrained, cycle-free dependencies before implementation.

Catering owns meals, ingredient/recipe composition and yields, staff packages, event menu revisions and event/service requirements. Catalog owns products/publication; Cart can optionally seed a request; Pricing integration is conditional; Negotiated Quotes owns generic version/expiry/acceptance behavior; Bookings owns availability/capacity; Orders owns order state; Payments owns authorization/capture/reconciliation. No upstream capability depends on Catering. No payment SDK or cross-module table writes.

Team/Store policies and explicit audience DTOs protect all entry points. Recipes, preparation and ingredient costs are staff-only. Quote acceptance, availability confirmation, order creation, deposit and payment completion are distinct transitions. Menu/quote snapshots are immutable; concurrency, retries and timeout reconciliation must create at most one order.

Use independent source modules with tracked host `/modules` and `/themes` copies where applicable; lockfiles and installed copies change together. Catering remains reusable and free of host `App\\` dependencies.
'''
    epic_body = f'''## User outcome

A catering operator maintains meals/packages, prepares a reproducible event menu and quotation, and converts an accepted, availability-confirmed event to one order. Customers see approved event/menu/price information without private preparation data.

{common}
## Delivery slices

- Core: domain invariants, contracts, snapshots, approved integrations and recovery.
- API: reviewed operation/projection schemas and authorization/concurrency behavior.
- Filament: authorized staff resources, event review, quotation context and conversion recovery.
- Livewire: customer event request, quote review/acceptance and distinct confirmation/order/payment status.

Each slice needs independent tests, applicable coverage evidence, one host journey, privacy/tenancy checks, migration/upgrade notes and operational recovery guidance. This epic adds the Catering capability to the existing programme; link the focused slice issues in the Catering issue register.
'''
    slices = {
        'core': ('Catering core: domain, snapshots and approved commerce integrations', '''Implement meals/recipes with explicit units/yields, package composition, event date/timezone/venue/guest/service validation, menu revisions and catering-specific snapshot references. Reuse approved Catalog/Quotes/Bookings/Orders contracts, with optional integrations disabled cleanly when not used. Agree confirmation ordering before implementation; use a durable conversion idempotency key and outbox/reconciliation where transactions cross boundaries. Test stale/expired acceptance, changed menus/guest counts, invalid yields, unavailable capacity, concurrent workers, duplicate delivery and timeout-after-order-create. Provide private-field projections, retention/export/redaction boundaries and a pending-conversion runbook.'''),
        'api': ('Catering API: contracts, audience projections and safe confirmation', '''Propose `module-ecommerce-catering-api` / `liberusoftware/ecommerce-catering-api` after boundary approval. Publish a reviewed OpenAPI fragment for meal/package staff operations, event requirements/menu revision, quote submission/review/acceptance and approved confirmation/status operations. Explicitly allowlist customer fields; omit recipes/preparation/costs from list/detail/export/error payloads. Define trusted scope, operation authorization, expected revision, expiry/conflict errors, idempotency payload matching/replay and pending reconciliation. Test schemas/examples, cross-store/ownership denial, private-field absence and concurrent/retried conversion against approved domain contracts.'''),
        'filament': ('Catering Filament: staff meals, event menus and quotation operations', '''Propose the matching one-to-one Catering Filament adapter; register reusable resources/pages/actions in host-owned panels. Staff manages meals, private recipes/yields and packages, reviews event/service requirements and frozen menu/quote context, and investigates pending conversion. Enforce policies on every resource/action and restrict preparation/cost fields separately. Show quote acceptance, availability, order creation and payment distinctly. Confirm high-impact actions, reject stale revisions, prevent duplicate conversion and provide retry/reconciliation status. Test policies/tenancy, private-field restrictions, accessible tables/forms, conflict recovery and a host staff journey. Ship namespaced default presentation views where renderable and verify theme resolution.'''),
        'livewire': ('Catering Livewire: customer event requests and quote acceptance', '''Propose the matching one-to-one Catering Livewire adapter for customer event requirements, menu/quote review, acceptance and confirmation status. Treat hydrated IDs as untrusted; reauthorize ownership and Team/Store scope on each action. Customer views, payloads and notifications never expose recipes, preparation data or ingredient costs. Display currency, timezone, quote revision/expiry, menu changes and actionable validation. Require online authoritative acceptance, reject stale quotes and reconcile duplicate/interrupted conversion using the same durable key. Test hostile hydrated IDs, private-field leakage, stale acceptance, expiry, network interruption, accessibility and one customer journey. Ship default namespaced views and test child/parent overrides and host fallback.'''),
    }
    if not args.apply:
        print(json.dumps({'repository': REPO, 'epic': title, 'slices': {k: v[0] for k, v in slices.items()}, 'appendToWayfinder': 925}, indent=2))
        return
    known = json.loads(gh('issue', 'list', '-R', REPO, '--state', 'all', '--limit', '2000', '--json', 'title,url'))
    epic = create(title, epic_body, known)
    result = {'repository': REPO, 'epic': epic, 'slices': {}, 'wayfinder': f'https://github.com/{REPO}/issues/925'}
    for layer, (slice_title, detail) in slices.items():
        result['slices'][layer] = create(slice_title, f'Parent Catering epic: {epic}\n\n{common}\n## Layer specification\n\n{DOCS}{layer}/catering.md\n\n## Implementation outcome and acceptance\n\n{detail}\n\nKeep changes bounded to Catering and the explicitly approved integrations described above. Follow the shared module/API/theme/testing standards and capture independent and host-composition evidence.\n', known)
        (ROOT/'projects/ecommerce/catering-filament-issues.json').write_text(json.dumps(result, indent=2)+'\n')
    epic_current = json.loads(gh('issue', 'view', epic, '--json', 'body'))['body']
    epic_marker = '<!-- catering-slices:start -->'
    if epic_marker not in epic_current:
        slice_links = '\n\n'+epic_marker+'\n## Focused implementation issues\n\n'+ '\n'.join(f'- [{layer}]({url})' for layer, url in result['slices'].items())+'\n<!-- catering-slices:end -->\n'
        subprocess.run(['gh', 'issue', 'edit', epic, '--body-file', '-'], input=epic_current+slice_links, text=True, check=True, capture_output=True)
    current = json.loads(gh('issue', 'view', '925', '-R', REPO, '--json', 'body'))['body']
    marker = '<!-- catering-addition:start -->'
    if marker not in current:
        addition = f'''\n\n{marker}
## Catering addition

Track the new Catering capability in {epic}, based on documentation issue https://github.com/liberusoftware/documentation/issues/26 and the [Catering delivery map]({DOCS}CATERING.md).

'''+ '\n'.join(f'- {layer}: {url}' for layer, url in result['slices'].items())+'''

Catering owns meals/recipes/yields, staff packages, event menus and service requirements. Reuse Catalog, Negotiated Quotes, Bookings and Orders only through their approved contracts; Payments remains separate. Resolve upstream dependency/snapshot/confirmation decisions before schema or implementation. Keep recipes/preparation/costs staff-only and preserve immutable accepted snapshots, Team/Store ownership and idempotent order conversion. Applicable installed `/modules` and `/themes` copies stay committed in the host.
<!-- catering-addition:end -->
'''
        subprocess.run(['gh', 'issue', 'edit', '925', '-R', REPO, '--body-file', '-'], input=current+addition, text=True, check=True, capture_output=True)
    (ROOT/'projects/ecommerce/catering-filament-issues.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
