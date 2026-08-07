# Authoring a module

**Reader:** a developer creating a new `liberu-module` package, or bringing an existing one onto the current conventions.

[MODULES.md](../../architecture/MODULES.md) states the rules. This directory states the **sequence** — what to create, in what order, with the commands that prove each step. Nothing here overrides the specification; where the two differ, MODULES.md wins and this guide is the defect.

## Documents

| Document | Answers |
| --- | --- |
| [WALKTHROUGH.md](WALKTHROUGH.md) | Create a domain package from nothing to a tagged release. |
| [TEST-BOOTSTRAP.md](TEST-BOOTSTRAP.md) | What `package-testbench` boots for you, what it deliberately does not, and the six failures that follow from getting that wrong. |
| [PRESENTATION.md](PRESENTATION.md) | Add the `-filament` companion, and test a panel from inside a package. |
| [RELEASING.md](RELEASING.md) | Version coupling, the three workflows, and the zero-diff gate. |

## The shortest possible summary

A module is a Composer package that a host **installs** without **booting**. Installation and enablement are separate decisions, and the manifest — not the application's configuration — is what carries the default:

```text
Installed   composer require put the code in /modules
Enabled     the manifest said default_enabled, or the deployment overrode it
Booted      the module resolver returned this provider, in dependency order
```

That separation is the reason a package declares **no** `extra.laravel.providers`. Laravel's auto-discovery must find nothing, so that adding a package to a composition is exactly one act — installing it — with no second list to remember. Everything in this guide follows from that one constraint.

## Evidence

This guide is derived from bringing 44 packages and 4 themes onto these conventions in [liberusoftware/boilerplate-laravel](https://github.com/liberusoftware/boilerplate-laravel), and from five packages subsequently developed repository-first. Each trap recorded here failed at least once in that work. Where a claim is a measurement rather than a rule, it says so.

## A known inconsistency

The Composer vendor is **`liberusoftware/`** throughout. MODULES.md and four sibling standards once wrote `liberu/*`, which does not resolve — `PROMPT.md` had always said `liberusoftware/`, so the specification disagreed with itself. Corrected in [#16](https://github.com/liberusoftware/documentation/pull/16). If you meet a `liberu/*` name anywhere, it is stale: copy the name from an existing package's `composer.json` rather than from prose.
