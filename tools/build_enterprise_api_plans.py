#!/usr/bin/env python3
"""Build proposed enterprise API plans from domain briefs and authored command examples."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]


def section(text,title):
    match=re.search(r'^## '+re.escape(title)+r'\n(.*?)(?=^## |\Z)',text,re.M|re.S)
    if not match:raise ValueError('Missing enterprise design section: '+title)
    return match.group(1).strip()


def schema(value):
    if isinstance(value,bool):return {'type':'boolean'}
    if isinstance(value,int):return {'type':'integer'}
    if isinstance(value,str):return {'type':'string','minLength':1}
    if isinstance(value,list):
        if not value:raise ValueError('An example array needs an explicit item type')
        return {'type':'array','minItems':1,'items':schema(value[0])}
    if isinstance(value,dict):return {'type':'object','additionalProperties':False,'required':list(value),'properties':{k:schema(v) for k,v in value.items()}}
    raise ValueError(type(value))


def main():
    root=ROOT/'projects/sap'
    examples=json.loads((root/'design/api-command-examples.json').read_text())
    contracts=root/'api/contracts';contracts.mkdir(exist_ok=True)
    for slug,example in examples.items():
        design=(root/'design'/f'{slug}.md').read_text()
        title=design.splitlines()[0].removeprefix('# ').removesuffix(': detailed enterprise design')
        routes=re.findall(r'^\| (GET|POST) \| `([^`]+)` \| ([^\n]+) \|$',section(design,'Proposed API operations'),re.M)
        base=next(path for method,path,_ in routes if method=='GET' and '{id}' not in path)
        target=base+'/{id}/'+example['action']
        assert any(method=='POST' and path==target for method,path,_ in routes),(slug,example['action'])
        record_name=re.search(r'primary workflow record is \*\*([^*]+)\*\*',design).group(1)
        fields=re.findall(r'^\| `([^`]+)` \|',section(design,'Records and required context'),re.M)
        record_id=example['record_id'];path=target.replace('{id}',record_id)
        operation_id=f'enterprise.{slug}.{example["action"]}'
        body=example['body'];request_schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':f'urn:liberu:proposed:enterprise:{slug}:{example["action"]}:request:v1',
                    'title':f'{title}: proposed {example["action"]} request','description':'Draft enterprise request contract, not an implemented or released API guarantee.',**schema(body)}
        schema_file=contracts/f'{slug}.request.schema.json'
        example_file=contracts/f'{slug}.request.example.json'
        schema_file.write_text(json.dumps(request_schema,indent=2)+'\n')
        example_file.write_text(json.dumps(body,indent=2)+'\n')
        existing=(root/'api'/f'{slug}.md').read_text()
        source=re.search(r'<!-- source-reconciliation:start -->.*?<!-- source-reconciliation:end -->',existing,re.S)
        owned=section(design,'Boundary and reuse').split('\n\n')[0]
        permissions=section(design,'Permissions and integrations').split('\n\n')
        failed=section(design,'Failure and recovery').split('\n\n')[0]
        tests=section(design,'Acceptance scenarios').split('\n\n')[0]
        lines=[f'# {title}: enterprise API design','',
               '**Status:** proposed composition contract. The [observed SAP source](../SOURCE-APPLICATION.md) establishes a foundation host, not these enterprise business endpoints. The paths, schemas and examples below require implementation/adoption review before any client uses them.','']
        if source:lines += [source.group(),'']
        lines+=['## 1. Purpose and ownership','',owned,'',
                'The primary enterprise workflow record is a **'+record_name+'**. A façade can coordinate owning product APIs and an enterprise read model, while the original product retains write authority for its records. `module-sap-'+slug+'-api` is a design identifier; it does not establish a published Composer package or another authoritative business implementation.','',
                'Read the [detailed domain design](../design/'+slug+'.md), [composition guide](../COMPOSITION.md), and [API architecture](../../../architecture/API.md) for the surrounding boundaries.','',
                '## 2. Contract design','',
                'The resource DTO exposes a stable identifier/type, workflow state, record version, authorized source/evidence references and permitted actions. Its domain fields are **'+', '.join('`'+field+'`' for field in fields)+'**. The [domain field table](../design/'+slug+'.md#records-and-required-context) defines their responsibilities; complete types, limits, sensitivity and required/nullable behavior must be reviewed with the actual owners.','',
                'Separate input from output schemas. Resolve actor/service, tenant membership and permitted legal entities from trusted authentication; submitted IDs select records but grant no authority. Resource state, audit fields, source results and permitted actions are server-owned. Paginated reads allowlist filters/sorts/includes and apply field/entity policy before serialization.','',
                'The proposed command protocol uses an actor/tenant-scoped `Idempotency-Key` and a documented record-version precondition such as `If-Match`. Scope a stored command result by operation and subject as well as identity; reusing a key with a different request is a conflict. Implement this storage/checking explicitly: passing a header alone does not make a downstream API idempotent.','',
                '## 3. Endpoint examples','',
                'These routes come from the detailed enterprise design. They are not a discovered runtime route list. Record creation/ingestion follows the owning workflow contract; there is no invented generic create/delete operation for an entire business group.','',
                '| Method | Proposed path | Responsibility |','| --- | --- | --- |']
        for method,route,purpose in routes:lines.append(f'| {method} | `{route}` | {purpose.strip()} |')
        lines+=['','### '+example['action']+' command','',
                f'Proposed operation ID: `{operation_id}`. Scenario: `{example["before"]}` → `{example["after"]}` after the business action is confirmed. The example IDs are illustrative; obtain actual identifiers from authorized records.','',
                '```http',f'POST {path} HTTP/1.1','Accept: application/json','Content-Type: application/json','Authorization: Bearer YOUR_AUTHORIZED_TOKEN','If-Match: "record-v12"',f'Idempotency-Key: {slug}-example-command-001','```','',
                '```json',json.dumps(body,indent=2),'```','',example['validation'],'',example['outcome'],'']
        if example['status']==202:
            response={'data':{'id':'operation-example-001','type':'operation','attributes':{'status':'queued','operation_id':operation_id,'subject_reference':record_id},'links':{'self':'/api/v1/operations/operation-example-001'}},'meta':{'request_id':'request-example-001'}}
            lines+=['Proposed acceptance response: `202 Accepted`, with `Location: /api/v1/operations/operation-example-001`. Authorization applies when polling the operation and retrieving its result. The returned queue state is not the final business state.','']
        else:
            response={'data':{'id':record_id,'type':base.rsplit('/',1)[-1],'attributes':{'state':example['after'],'version':'record-v13'}},'meta':{'request_id':'request-example-001'}}
            lines+=['Proposed synchronous response: `200 OK` only after the local authorized decision is recorded, with the new record version. Any resulting downstream handoffs remain separately observable; local success is not proof of their completion.','']
        lines+=['```json',json.dumps(response,indent=2),'```','',
                '## 4. OpenAPI schema','',
                'The reviewed fragment should define the resource and collection schemas, separate command bodies, operation/result schemas, scopes, version preconditions, idempotency semantics, errors and pagination. Use stable operation IDs for each explicit action and include the owning product/enterprise boundary. Validate/bundle the specification and compare it against supported contracts before generating clients.','',
                f'This document includes a machine-readable **draft schema for the illustrated `{example["action"]}` request only**: [request schema](contracts/{schema_file.name}) and [matching example](contracts/{example_file.name}). Other command bodies and the complete response/OpenAPI bundle still require their own reviewed schemas. The specimen is not a full implemented service contract.','',
                'The specimen makes the illustrated business fields required and rejects unknown properties. Required fields, units, effective-date constraints, value ranges, enum sets and cross-record rules must be confirmed against the selected owner before a release; JSON type validation cannot establish authorization or business validity.','',
                'Reference: [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) and [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0).','',
                '## 5. Audience and operation matrix','',permissions[0],'',
                '| Audience | Exposure decision |','| --- | --- |',
                '| Anonymous/public | Disabled for these workflow commands |',
                '| Employee or approved external delegate | Only explicitly granted records, fields and actions; enforce source/evidence policy independently |',
                '| Approver/operator | Domain authority and segregation/delegation policy apply to each action and bulk record |',
                '| Service integration | Narrow service identity, permitted entities/operations, correlation and durable command identity |','',
                'An authenticated role name alone is insufficient where a record, value threshold, legal entity, time window or independent approval constrains the operation. Recheck permissions in jobs and evidence downloads.','',
                '## 6. Implementation strategy','',permissions[1],'',
                'Persist only enterprise-owned workflow/operation state and source references. Use local transactions for its invariants, then durable outbox/inbox or an equivalent owner-supported handoff. Confirm an existing source operation before retrying a timeout; do not repeat a side effect under a fresh identity. Product adapters translate schemas/errors without accessing another owner\'s private tables.','',
                'Presentations use explicit domain commands rather than a generic state patch. Filament/Livewire can invoke the reviewed public application boundary, while React/Inertia, Next.js, Vue/Nuxt and mobile use their appropriate authorized transport. Preserve one domain invariant and recovery contract across all surfaces.','',
                '## 7. Security, resilience, and observability','',failed,'',
                '| Response condition | Proposed handling |','| --- | --- |',
                '| 401 / 403 / scoped 404 | Authenticate or deny/conceal consistently; never retry under a broader identity |',
                '| 409 conflict | Invalid transition, duplicate identity with another payload, or owner uniqueness conflict; expose an actionable current outcome |',
                '| 412 precondition failed | Reload/review the changed record version; preserve safe draft inputs |',
                '| 422 validation failed | Return field/domain errors without leaking hidden source records |',
                '| 429 / 503 | Apply documented retry/backoff and preserve operation identity; reconcile uncertain outcomes before reissuing writes |','',
                'Use the shared Problem Details envelope, request/correlation IDs and scoped operator diagnostics. Redact protected data and credentials. Record source acknowledgements, last error, attempt count and recovery owner; an unavailable dependency must not silently advance the final state.','',
                '## 8. Verification strategy','',tests,'',
                'Also verify the illustrated command body against its draft request schema, allowed/denied/wrong-entity requests, stale versions, changed-payload key reuse, uncertain outcomes, job authorization changes and result/evidence downloads. Test real owner adapters and the selected presentations against the same accepted/rejected transitions. Document which checks ran; the presence of a schema or test file is not a passing-run claim.','',
                '## 9. Definition of done','',
                'Implementation/adoption is complete only after the selected owner contracts, full request/response/OpenAPI schemas, API/security/version tests, affected data transitions, UI parity and operational recovery are verified. Publish actual identities/compatibility and migration guidance through the owning package process. This document supplies a concrete proposed workflow contract; it does not certify that release gate.','']
        (root/'api'/f'{slug}.md').write_text('\n'.join(lines))
    print(f'Rebuilt {len(examples)} enterprise API plans with concrete command examples and {len(examples)} draft request schemas.')


if __name__=='__main__':main()
