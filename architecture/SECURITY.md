# Security policy

## Scope

This repository contains architecture and operational documentation for Liberu applications. Report vulnerabilities in documented implementations, dependency guidance, deployment examples, authentication/authorization design, secret handling, or repository automation privately.

## Report a vulnerability

Do not open a public issue, pull request, or discussion for a suspected vulnerability. Use the repository's [GitHub Security Advisories](https://github.com/liberusoftware/documentation/security/advisories/new) form. If that form is unavailable, contact the maintainers through the private security channel listed in the repository's GitHub security settings.

Include:

- affected repository, document, version/commit, and deployment target;
- concise impact and threat model;
- reproducible steps or a minimal proof of concept;
- affected configuration, permissions, data, or users;
- logs/screenshots with secrets and personal data removed;
- a safe contact method and any proposed mitigation.

Encrypt sensitive attachments when practical. Do not test against systems or data you do not own or have permission to assess.

## Response process

Maintainers will acknowledge a report when received, validate scope and severity, coordinate a fix or mitigation, and publish disclosure details only after affected users can update. Reporter credit is provided unless anonymity is requested. Timelines depend on severity, exploitability, affected data, and release coordination.

## Secure contribution rules

Never commit credentials, tokens, private keys, personal data, unredacted OAuth payloads, database dumps, or production identifiers. Follow [CONTRIBUTING.md](../standards/CONTRIBUTING.md), use least privilege, pin or lock dependencies, review generated changes, and run the security checks in [TESTING.md](../standards/TESTING.md).

## Related guidance

- [Laravel security](https://laravel.com/docs/13.x/security)
- [Policies and permissions](POLICY.md)
- [Deployment](../deployment/README.md)
- [Contributing](../standards/CONTRIBUTING.md)
