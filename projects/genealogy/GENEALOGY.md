# Liberu Genealogy

## Product Scope

**Purpose:** Evidence-based family history, relationship, DNA, research, and collaboration platform.
**Architecture:** Functional modules follow [MODULES.md](../../architecture/MODULES.md); data exchange, integration APIs, and webhooks follow [API.md](../../architecture/API.md); tree, research, and portal experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines genealogy behavior only.

## Outcomes

- Model people, events, relationships, places, sources, citations, and competing conclusions without losing provenance.
- Import, analyze, visualize, collaborate on, and export large family-history datasets safely.
- Protect living-person and genetic data with granular consent and visibility controls.

## Module plan

| Module         | Responsibilities                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------- |
| Genealogy Core | Trees, ownership, identifiers, privacy defaults, terminology, and shared events                |
| People         | Names, identities, attributes, life events, living/deceased status, and merge candidates       |
| Relationships  | Parent, partner, household, adoption, guardianship, uncertain links, and graph validation      |
| Evidence       | Sources, repositories, citations, extracts, assertions, confidence, and proof conclusions      |
| Research       | Questions, plans, tasks, logs, correspondence, negative searches, and findings                 |
| Places         | Historical/current place hierarchy, names over time, coordinates, jurisdictions, and maps      |
| Timeline       | Personal/family timelines, historical context, conflicts, and chronological navigation         |
| Tree Viewer    | Pedigree, descendants, fan/chart views, navigation, filters, and large-tree rendering          |
| Import Export  | GEDCOM and GRAMPS mapping, validation, dry run, duplicate detection, reports, and round trip   |
| DNA            | Kits, providers, consent, match segments, relationships, groups, notes, and revocation         |
| Media          | Documents, photographs, audio/video, transcription, rights, links, and preservation metadata   |
| Collaboration  | Invitations, roles, branch/change proposals, review, discussions, watch lists, and attribution |
| Discovery      | Person/place/source search, hints, duplicates, relationship paths, and privacy-aware indexes   |
| Reports        | Family groups, pedigrees, descendants, timelines, research, sources, and exportable charts     |

## Required workflows

1. **Research conclusion:** question → plan/search log → source/citation → assertion → evidence comparison → reasoned conclusion.
2. **Import:** upload → parse/validate → map → detect duplicates → preview changes → import atomically → report and undo window.
3. **Merge:** select candidates → compare facts/relationships/evidence → resolve conflicts → approve → redirect identifiers and audit.
4. **Collaborate:** invite → grant tree/subtree permission → propose change → review → accept/reject → notify and attribute.
5. **DNA match:** register consent → import kit/matches → analyze segment/relationship → contact controls → revoke/export/delete.

## Product requirements

- Represent uncertain dates, places, relationships, conflicting facts, privacy status, and evidence quality explicitly.
- Prevent impossible graph cycles while allowing culturally and legally varied family structures.
- Preserve original import data, external identifiers, source citations, and change attribution.
- Provide responsive interactive maps/trees plus accessible tabular or narrative alternatives.
- Support multilingual names, calendars, locales, place histories, and GEDCOM character encodings.
- Offer APIs/webhooks with living-person, tree, source, and genetic-data authorization.

## Integrations

Record archives, mapping/geocoding, OCR/transcription, storage, DNA-provider imports, email, search, and optional AI research assistance use replaceable drivers. Automated hints remain suggestions and disclose their evidence.

## Quality and privacy gates

- Apply explicit consent, encryption, access logging, retention, export, and deletion to genetic and living-person data.
- Test kinship calculations, graph integrity, date uncertainty, merges, imports, round trips, tenant/tree isolation, and revoked access.
- Benchmark trees, graph queries, search indexes, charts, and imports at representative large sizes.
- Clearly distinguish sourced facts, user conclusions, inferred hints, and generated content.

## Delivery phases

1. Core, People, Relationships, privacy, Evidence, and basic tree views.
2. Research, Places, Timeline, Media, GEDCOM import/export, and reports.
3. Collaboration, discovery/hints, merge workflow, and advanced visualization.
4. DNA, GRAMPS support, archive integrations, and governed AI assistance.

## Definition of done

Users can build, evidence, import, review, share, visualize, and export trees without losing provenance or exposing protected data. Each module maps cleanly to a GitHub epic with privacy and graph-integrity acceptance criteria.

## Product Scope

**Purpose:** Evidence-based family history, relationship, DNA, research, and collaboration platform.
**Architecture:** Functional modules follow [MODULES.md](../../architecture/MODULES.md); data exchange, integration APIs, and webhooks follow [API.md](../../architecture/API.md); tree, research, and portal experiences follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines genealogy behavior only.

## Outcomes

- Model people, events, relationships, places, sources, citations, and competing conclusions without losing provenance.
- Import, analyze, visualize, collaborate on, and export large family-history datasets safely.
- Protect living-person and genetic data with granular consent and visibility controls.

## Module plan

| Module         | Responsibilities                                                                               |
| -------------- | ---------------------------------------------------------------------------------------------- |
| Genealogy Core | Trees, ownership, identifiers, privacy defaults, terminology, and shared events                |
| People         | Names, identities, attributes, life events, living/deceased status, and merge candidates       |
| Relationships  | Parent, partner, household, adoption, guardianship, uncertain links, and graph validation      |
| Evidence       | Sources, repositories, citations, extracts, assertions, confidence, and proof conclusions      |
| Research       | Questions, plans, tasks, logs, correspondence, negative searches, and findings                 |
| Places         | Historical/current place hierarchy, names over time, coordinates, jurisdictions, and maps      |
| Timeline       | Personal/family timelines, historical context, conflicts, and chronological navigation         |
| Tree Viewer    | Pedigree, descendants, fan/chart views, navigation, filters, and large-tree rendering          |
| Import Export  | GEDCOM and GRAMPS mapping, validation, dry run, duplicate detection, reports, and round trip   |
| DNA            | Kits, providers, consent, match segments, relationships, groups, notes, and revocation         |
| Media          | Documents, photographs, audio/video, transcription, rights, links, and preservation metadata   |
| Collaboration  | Invitations, roles, branch/change proposals, review, discussions, watch lists, and attribution |
| Discovery      | Person/place/source search, hints, duplicates, relationship paths, and privacy-aware indexes   |
| Reports        | Family groups, pedigrees, descendants, timelines, research, sources, and exportable charts     |

## Required workflows

1. **Research conclusion:** question → plan/search log → source/citation → assertion → evidence comparison → reasoned conclusion.
2. **Import:** upload → parse/validate → map → detect duplicates → preview changes → import atomically → report and undo window.
3. **Merge:** select candidates → compare facts/relationships/evidence → resolve conflicts → approve → redirect identifiers and audit.
4. **Collaborate:** invite → grant tree/subtree permission → propose change → review → accept/reject → notify and attribute.
5. **DNA match:** register consent → import kit/matches → analyze segment/relationship → contact controls → revoke/export/delete.

## Product requirements

- Represent uncertain dates, places, relationships, conflicting facts, privacy status, and evidence quality explicitly.
- Prevent impossible graph cycles while allowing culturally and legally varied family structures.
- Preserve original import data, external identifiers, source citations, and change attribution.
- Provide responsive interactive maps/trees plus accessible tabular or narrative alternatives.
- Support multilingual names, calendars, locales, place histories, and GEDCOM character encodings.
- Offer APIs/webhooks with living-person, tree, source, and genetic-data authorization.

## Integrations

Record archives, mapping/geocoding, OCR/transcription, storage, DNA-provider imports, email, search, and optional AI research assistance use replaceable drivers. Automated hints remain suggestions and disclose their evidence.

## Quality and privacy gates

- Apply explicit consent, encryption, access logging, retention, export, and deletion to genetic and living-person data.
- Test kinship calculations, graph integrity, date uncertainty, merges, imports, round trips, tenant/tree isolation, and revoked access.
- Benchmark trees, graph queries, search indexes, charts, and imports at representative large sizes.
- Clearly distinguish sourced facts, user conclusions, inferred hints, and generated content.

## Delivery phases

1. Core, People, Relationships, privacy, Evidence, and basic tree views.
2. Research, Places, Timeline, Media, GEDCOM import/export, and reports.
3. Collaboration, discovery/hints, merge workflow, and advanced visualization.
4. DNA, GRAMPS support, archive integrations, and governed AI assistance.

## Definition of done

Users can build, evidence, import, review, share, visualize, and export trees without losing provenance or exposing protected data. Each module maps cleanly to a GitHub epic with privacy and graph-integrity acceptance criteria.
