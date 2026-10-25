#!/usr/bin/env python3
"""Replace invented generic API payload examples with pinned route/schema evidence."""
import argparse
import json
from pathlib import Path
import re
import subprocess

from build_source_reference import methods,safe,source_url

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--projects',type=Path,default=Path('/home/liberu/projects'))
    args=parser.parse_args()
    snapshot=json.loads((ROOT/'architecture/source-inventory.json').read_text())['repositories']
    mapping=json.loads((ROOT/'architecture/source-design-mapping.json').read_text())['projects']
    records={r['project']:r for r in snapshot};tracked={}
    for record in snapshot:
        repo=args.projects/record['repository']
        assert subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()==record['commit']
        if subprocess.check_output(['git','-C',str(repo),'status','--porcelain'],text=True).strip():
            raise SystemExit(f'{repo}: source worktree changed; use a clean pinned snapshot')
        tracked[record['project']]=subprocess.check_output(['git','-C',str(repo),'ls-files'],text=True).splitlines()
    changed=0;route_scopes=0;schema_scopes=0
    for project,project_info in mapping.items():
        if project=='sap':continue # Authored enterprise command contracts have their own generator.
        record=records.get(project)
        for stem,info in project_info['designs'].items():
            page=ROOT/'projects'/project/'api'/(stem+'.md')
            if not page.exists():continue
            routes=[];schemas=[];controllers=[];requests=[];references=[]
            seen=set()
            if record:
                for choice in info['layers']['api']+info['layers']['core']:
                    if choice['directory'] in seen:continue
                    seen.add(choice['directory']);references.append(choice)
                    prefix=f'modules/{choice["directory"]}/'
                    for file in tracked[project]:
                        if not file.startswith(prefix):continue
                        local=file.removeprefix(prefix);path=args.projects/record['repository']/file
                        if local.startswith('routes/') and file.endswith('.php') and path.is_file():
                            declarations=[line.strip() for line in path.read_text().splitlines() if re.search(r'Route::(?:get|post|put|patch|delete|apiResource|resource|middleware|prefix)\(',line)]
                            routes.append((file,declarations))
                        elif local.startswith(('openapi/','schemas/')) and path.is_file():schemas.append(file)
                        elif local.startswith('src/Http/Controllers/') and file.endswith('.php') and path.is_file():
                            signatures=[signature for signature,_ in methods(path.read_text()) if 'function __construct(' not in signature]
                            controllers.append((file,signatures))
                        elif local.startswith('src/Http/Requests/') and file.endswith('.php') and path.is_file():requests.append(file)
            lines=['## 3. Endpoint examples','',
                   '**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.','']
            if references:
                lines+=['| Boundary | Observed identity and implementation reference |','| --- | --- |']
                for choice in references:
                    relative=Path('../../../')/choice['reference']
                    lines.append(f'| Source package | [{choice["identity"]}]({relative}) |')
                lines+=['']
            if routes:
                route_scopes+=1
                lines+=['### Observed route declarations','',
                        'These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.','']
                for file,declarations in routes:
                    lines += [f'[{file}]({source_url(record,file)})','']
                    if declarations:lines+=['```php',*declarations,'```','']
            else:
                lines+=['No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.','']
            if controllers:
                lines+=['### Observed controller entry points','',
                        'The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.','',
                        '| Controller source | Public handler signatures |','| --- | --- |']
                for file,signatures in controllers:
                    lines.append(f'| [{Path(file).name}]({source_url(record,file)}) | '+('<br>'.join(f'`{safe(s)}`' for s in signatures) or 'Inspect the source for dynamically supplied handlers.')+' |')
                lines+=['']
            if requests:
                lines+=['Request validation sources: '+ ' · '.join(f'[{Path(file).name}]({source_url(record,file)})' for file in requests)+'.','']
            if project=='ecommerce':
                lines+=['Ecommerce also implements capabilities in the [application tree](../SOURCE-APPLICATION.md). Its [current root route file](https://github.com/liberusoftware/'+record['repository']+'/blob/'+record['commit']+'/routes/api.php) and application controllers/GraphQL schema must be reviewed for the selected task. Preserve this module even when no independent package match exists.','']
                for row in (ROOT/'projects/ecommerce/SOURCE-APPLICATION.md').read_text().splitlines():
                    if f'](features/{stem}.md)' in row:lines+=['Capability-specific source entry points: '+row.split('|')[-2].strip()+'.','']
            lines+=['A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.','',
                    '## 4. OpenAPI schema','']
            if schemas:
                schema_scopes+=1
                lines+=['The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.','',
                        *[f'- [{file}]({source_url(record,file)})' for file in schemas],'']
            else:
                lines+=['No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.','']
            lines+=['For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.','',
                    'Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#'+stem+'), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.','']
            block='\n'.join(lines)+'\n'
            original=page.read_text()
            pattern=r'^## 3\. Endpoint examples\n.*?(?=^## 5\. Audience and operation matrix)'
            first_examples=re.search(r'^## 3\. Endpoint examples\n',original,re.M)
            marker_pos=original.find('<!-- observed-api-contract:start -->')
            if first_examples and not re.search(pattern,original,re.M|re.S) and (marker_pos<0 or first_examples.start()<marker_pos):
                # Some original API files contain truncated schema fences or pasted frontend sections.
                # Retain their valid scope/header and replace the damaged API tail with the actual evidence.
                footer='''## 5. Audience and operation matrix

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
                updated=original[:first_examples.start()]+block+footer
            elif re.search(pattern,original,re.M|re.S):
                updated=re.sub(pattern,lambda _:block,original,flags=re.M|re.S)
            else:
                start='<!-- observed-api-contract:start -->';end='<!-- observed-api-contract:end -->'
                marked=start+'\n'+block+end
                if start in original:updated=re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:marked,original,flags=re.S)
                else:updated=original+'\n'+marked+'\n'
            updated=re.sub(r'- Use `/api/[^`]+` as the default module route prefix[^\n]*', '- Choose the route namespace through the host\'s reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.',updated)
            updated=re.sub(r'\*\*API package:\*\* `([^`/]+)`',r'**Proposed API design identifier:** `\1`',updated)
            updated=re.sub(r'^(\*\*Proposed API design identifier:\*\* `[^`\n]+`)[ \t]+$',r'\1<br>',updated,flags=re.M)
            if updated!=original:page.write_text(updated);changed+=1
    print(f'Updated {changed} non-enterprise API documents; indexed route evidence for {route_scopes} spellings and schema evidence for {schema_scopes}.')


if __name__=='__main__':main()
