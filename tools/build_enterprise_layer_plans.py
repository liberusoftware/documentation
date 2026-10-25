#!/usr/bin/env python3
"""Align enterprise core, presentation and task guides with the detailed domain contracts."""
import json
from pathlib import Path
import re

from build_enterprise_api_plans import section

ROOT=Path(__file__).resolve().parents[1]
LAYERS=('core','filament','livewire','react','vue','nuxt','react-native','flutter')


def main():
    root=ROOT/'projects/sap';examples=json.loads((root/'design/api-command-examples.json').read_text())
    written=0
    for slug,example in examples.items():
        design=(root/'design'/f'{slug}.md').read_text()
        title=design.splitlines()[0].removeprefix('# ').removesuffix(': detailed enterprise design')
        owner=section(design,'Boundary and reuse').split('\n\n')[0]
        lifecycle=section(design,'Lifecycle and invariants').split('\n\n')
        permissions=section(design,'Permissions and integrations').split('\n\n')
        failure=section(design,'Failure and recovery').split('\n\n')[0]
        acceptance=section(design,'Acceptance scenarios').split('\n\n')[0]
        surfaces=re.search(r'The workspace surfaces are \*\*([^*]+)\*\*',design).group(1)
        fields=re.findall(r'^\| `([^`]+)` \|',section(design,'Records and required context'),re.M)
        route=next(path for method,path in re.findall(r'^\| (GET|POST) \| `([^`]+)`',section(design,'Proposed API operations'),re.M) if method=='POST' and path.endswith('/'+example['action']))
        prefix=route.rsplit('/{id}/',1)[0]
        body_fields=', '.join('`'+key+'`' for key in example['body'])
        for layer in LAYERS:
            path=root/layer/f'{slug}.md'
            original=path.read_text()
            annotation=re.search(r'<!-- source-reconciliation:start -->.*?<!-- source-reconciliation:end -->',original,re.S)
            layer_title={'core':'core composition','filament':'Filament','livewire':'Livewire','react':'React + Inertia','vue':'Vue + Inertia','nuxt':'Nuxt','react-native':'React Native','flutter':'Flutter'}[layer]
            lines=[f'# {title}: {layer_title} design','',
                   '**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/'+slug+'.md) and [API plan](../api/'+slug+'.md) as the review target.','']
            if annotation:lines += [annotation.group(),'']
            lines+=['## Ownership and delivery scope','',owner,'',
                    'Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.','',
                    '## Workflow and command contract','',
                    '**Workspace surfaces:** '+surfaces+'.','',
                    '**Business lifecycle:** '+lifecycle[0], '',lifecycle[1],'',
                    f'The illustrated `{example["action"]}` command takes {body_fields}, with a documented record-version precondition and scoped operation identity. It starts from `{example["before"]}` and reaches `{example["after"]}` only after its defined business outcome. The [API example](../api/{slug}.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/{slug}.request.schema.json).','',
                    example['validation'],'',example['outcome'],'',
                    '## Layer implementation','']
            if layer=='core':
                lines += ['Use an explicit application use case for each reviewed transition. Inputs are authenticated actor/service context, authorized tenant/entity/subject references, expected subject version, scoped operation identity and a typed command DTO. Browser/request fields do not replace this trusted context.','',
                          'The public result distinguishes validation/permission/stale-state rejection, a committed local decision and an accepted asynchronous operation. Publish only permitted DTO fields and evidence references; Eloquent models and upstream private tables are not the cross-module contract.','',
                          '**Domain context fields:** '+', '.join('`'+field+'`' for field in fields)+'. These are design inputs/references, not a mandate to duplicate complete upstream records. Preserve owner identifiers and immutable decision/source snapshots where needed.','',
                          'Store enterprise-owned orchestration changes transactionally and record outbox work with them. The shared operation journal owns delivery state; the business owner owns the actual transition. Use the owner concurrency contract for upstream writes and reconcile its acknowledgement before advancing a final outcome.','',
                          permissions[1],'',
                          'Migrations apply only to newly owned operation/projection state. Plan backfills, indexes, constraints, retention/holds and recovery without renaming or deleting another owner\'s records. Financial corrections use the owner reversal workflow; identity/access changes retain their revocation acknowledgements.','']
            elif layer=='filament':
                lines += ['Compose a scoped work queue and detail/evidence page for the workspace above. Recommended queue columns are subject/source reference, active legal entity, business state, operation state, responsible owner and last transition/attempt time. Filter authorized records before counts, search, exports and relationships.','',
                          f'Implement `{example["action"]}` as an explicit authorized action/form using {body_fields}. Load permitted options from owning queries; keep protected IDs and final state fields outside editable form state. Validate at the form boundary for feedback and again in the public core/API command.','',
                          'A generic resource save or a status dropdown must not bypass the transition use case. Resolve the current record/version and policy again when handling the action. Display a review summary/evidence when the domain approval policy requires it; do not infer approval from a hidden button or navigation permission.','',
                          'Bulk operations preview eligible/skipped rows and retain each record\'s version and command identity. Show per-record completion/conflict/failure rather than a blanket success toast. Queue large exports/actions and preserve authorized result/evidence links.','']
            elif layer=='livewire':
                lines += ['Compose a workspace list, selected-subject detail, command form and operation-status component. Public component state contains only authorized filter values, opaque selection/version, safe command draft and operation reference; hydrated IDs are untrusted input.','',
                          f'The `{example["action"]}` handler resolves the authenticated actor and current scope afresh, loads the authorized subject, validates {body_fields}, and calls the public application/API command. Protected lifecycle/audit/owner-result fields are not mass-assigned from component state.','',
                          'Keep field validation messages with the draft and announce them accessibly. Disable repeat interaction while a request is pending for usability, while relying on server command identity/concurrency rules for correctness. After a confirmed write, reload authorized state rather than applying an assumed client-side final state.','',
                          'Poll only an authorized operation reference at a bounded interval; stop/recover cleanly after expiry, revocation or navigation. Avoid persisting request-specific tenant/actor data in long-lived singleton/static state. File uploads need size/type checks and authorized evidence registration before use.','']
            elif layer in ('react','vue'):
                framework='React' if layer=='react' else 'Vue'
                components='typed React components/hooks' if layer=='react' else 'typed Vue components/composables'
                lines += [f'The Laravel host owns Inertia routes/controllers and passes authorized serializable page props to {components}. Compose a queue, subject/evidence detail and `{example["action"]}` form for the domain workspace. Props include the record/version, permitted actions, safe draft defaults and operation reference, not an unrestricted model snapshot.','',
                          'An Inertia visit expects an Inertia page/redirect lifecycle. Use the Laravel controller\'s reviewed public application boundary or a deliberate API adapter and then return the appropriate Inertia response. Do not point an Inertia page visit at a bare REST JSON endpoint and assume it is an Inertia page.','',
                          f'Keep {body_fields} in a typed command draft and map actual server field errors to the form. Preserve navigation/filter state where safe, focus the actionable error summary, and reload/review a stale record before resubmission. Laravel reauthorizes every command independently of client visibility.','',
                          ('Share framework-independent cards, tables, labels, formatting and field primitives with the [Next.js adapter](../nextjs/'+slug+'.md). Keep Inertia `Link`, visits, page props, form transport and redirects in its wrapper; Next.js retains its own routing, server/client and cache boundaries.' if layer=='react' else 'Share framework-independent Vue primitives with Nuxt where the contracts fit. Keep Inertia navigation/forms/page props in its wrapper and Nuxt server/browser transport, routing and runtime configuration in its adapter.'),'',
                          f'The {framework} UI displays business and operation states separately. A queued response preserves a pending status and authorized progress link; it does not manufacture the eventual domain outcome in local state.','']
            elif layer=='nuxt':
                lines += ['The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.','',
                          f'The proposed API family is `{prefix}`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `{example["action"]}` rather than a generic status update.','',
                          'Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.','',
                          f'The command form preserves {body_fields}, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.','']
            else:
                framework='React Native' if layer=='react-native' else 'Flutter'
                types='TypeScript DTOs and typed navigation' if layer=='react-native' else 'Dart DTOs and explicit widget/navigation state'
                lines += [f'Use {types} for a focused mobile queue/detail/evidence and `{example["action"]}` review workflow. The host {framework} application owns identity/session storage, platform permissions, signing and release. Keep the full enterprise admin surface on the appropriate web workspace when it is unsuitable for a phone.','',
                          f'Resolve the selected entity and permitted subject through the reviewed API. The command body uses {body_fields}; the server validates authority, references and version independently. Secure storage protects credentials; logs, notifications and device caches omit sensitive fields.','',
                          'Offline mode may preserve an explicitly permitted draft or bounded evidence capture with a visible stale indicator. Approval, posting, custody, access and other consequential transitions require fresh server validation. A queued local command is not a confirmed business decision; revalidate scope/version before transmitting after reconnection.','',
                          'For evidence uploads, retain a resumable upload/operation identity where supported, protect temporary local files and show partial-upload recovery. Recheck access when opening or downloading artifacts. Revocation/logout clears protected local state according to policy.','',
                          'Provide accessible labels, focus/error announcements, explicit loading/empty/denied/conflict states and localized dates/units. Test iOS/Android behavior separately where storage, backgrounding, uploads or permissions differ.','']
            lines+=['## Authorization, recovery and operations','',permissions[0],'',failure,'',
                    'Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.','',
                    '## Module-specific acceptance','',acceptance,'',
                    f'- Exercise the `{example["action"]}` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `{example["after"]}` only from its authoritative outcome.',
                    '- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.',
                    '- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.','',
                    'Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.','']
            path.write_text('\n'.join(lines));written+=1
        user=ROOT/'user-guides/projects/sap/modules'/f'{slug}.md'
        if not user.exists():raise ValueError(str(user))
        user.write_text(f'''# {title}: workflow guide

**Availability:** target enterprise workflow. The current source host supplies shared foundation modules; confirm an enabled implementation and your permissions with the application operator before using these steps. This guide does not claim the proposed business UI is deployed.

## Understand the workspace

Use **{surfaces}** for the intended business tasks. {owner}

Business lifecycle: {lifecycle[0]}

## Complete the illustrated task

1. Sign in with the correct account and select the authorized legal entity/workspace. Confirm the displayed source and subject reference before acting.
2. Open the relevant record and review its current `{example['before']}` state, version and evidence. The displayed action must be permitted for your role and this record.
3. Prepare the `{example['action']}` action using {body_fields}. These are design field names; the actual UI should provide clear labels and authorized choices rather than expect users to invent identifiers.
4. Review the domain requirements: {example['validation']}
5. Submit once and retain the displayed operation/result reference. {example['outcome']}
6. Confirm the authoritative outcome and any remaining obligations. `{example['after']}` is a business result, while queued/running describe operation delivery; they are not interchangeable.

## Permission and recovery

{permissions[0]}

{failure}

For validation errors, correct the indicated fields while preserving the safe draft. If another user changed the record, reload/review its current version before submitting again. After a timeout, inspect the existing operation/current record before retrying; repeatedly clicking or creating a new operation identity can duplicate an external effect.

On a permission or entity mismatch, stop the task and use an authorized account/scope; a hidden action or expired session is not a reason to work around the server policy. For unresolved operations, provide the subject/source reference, operation ID and safe error/correlation details to the responsible operator rather than sending protected payloads or credentials.

## Presentation choices and technical detail

Filament and Livewire support administrative/server-owned workflows. React/Inertia and Vue/Inertia use Laravel navigation, while Next.js/Nuxt and mobile use their reviewed API/session integration. Each enabled surface must preserve the same permissions, state and recovery behavior. Mobile draft capture does not approve a stale/offline business decision.

See the [detailed domain design](../../../../projects/sap/design/{slug}.md), [API example](../../../../projects/sap/api/{slug}.md), and [shared operation semantics](../../../../projects/sap/design/OPERATIONS.md) for implementation detail. The [current source guide](../../../../projects/sap/SOURCE-APPLICATION.md) distinguishes foundation behavior from the proposed enterprise business scope.
''')
    print(f'Aligned {written} enterprise core/presentation plans and {len(examples)} user workflow guides.')


if __name__=='__main__':main()
