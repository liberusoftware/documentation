# Laravel Pint standard

Liberu uses [Laravel Pint](https://laravel.com/docs/13.x/pint) as the canonical PHP formatter. Pint must run at the repository’s maximum configured strictness level; formatting is a required quality gate, not an optional cleanup step.

## Policy

- Pin Pint in the repository’s Composer development dependencies and use the lock file as the version authority.
- Use the strictest supported preset/configuration for the repository, normally `laravel:pint` with all applicable risky rules enabled only when explicitly reviewed and safe.
- Format owned PHP source, tests, migrations, seeders, factories, configuration, commands, providers, and package code.
- Do not format vendor code, generated files, build artifacts, or third-party source. Exclusions must be narrow, documented, and reviewed.
- Run Pint before committing and in CI. A pull request fails when formatting changes are required.
- Keep formatting-only changes separate from behavioral changes when practical.

## Commands

Use the repository’s Composer script when available. The equivalent commands are:

```bash
vendor/bin/pint --test
vendor/bin/pint
```

`--test` verifies formatting without changing files. Run the write mode locally, inspect the diff, and rerun `--test` before committing. Package repositories run Pint from their own source repository and must not format the consuming application or sibling packages.

## Configuration and review

Keep `pint.json` or `php pint` configuration at the repository root and commit it with the lock file. Prefer the maximum strictness consistently across applications and packages; a lower rule level requires an explicit documented compatibility reason. Reviewers should treat unexplained formatter exclusions, inline ignores, disabled safety rules, and inconsistent package configurations as defects.

Pint does not replace static analysis, architecture checks, security review, tests, or PSR interoperability. Use it with [PHP.md](PHP.md), [PSR.md](PSR.md), [GUIDELINES.md](GUIDELINES.md), and [TESTING.md](TESTING.md).

## Official references

- [Laravel Pint documentation](https://laravel.com/docs/13.x/pint)
- [Laravel Pint GitHub repository](https://github.com/laravel/pint)
- [PHP-FIG PSR-12](https://www.php-fig.org/psr/psr-12/)
