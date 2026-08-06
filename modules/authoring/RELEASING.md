# Releasing a module

**Reader:** a developer cutting a release, or diagnosing why a consuming application stopped booting after one.

---

## 1. What a version bump obliges

Three files carry the version, and a mismatch between any two is a failure rather than a warning:

| Where | Checked by |
| --- | --- |
| `composer.json` `version` | the boundary suite, against `module.json` |
| `module.json` `version` | the module resolver at boot, against `Composer\InstalledVersions` |
| the Git tag | Packagist, which publishes what the tag contains |

The consequence is worth stating plainly, because it looks like a broken application rather than an unfinished release:

> Bumping a manifest in a monorepo that also **installs** the package makes the host unbootable until the package is published and `composer update`d. The resolver compares the manifest against what Composer says is installed, and they disagree until then.

The same shape catches renames. A monorepo can change what a class *does* and stay green, because the autoload map in `vendor/composer/installed.json` is written from each package's *published* metadata. It cannot change what a class is *called*, or which package owns it, without a publish — the map is frozen until a reinstall, and a reinstall fetches from the remote.

**Practical rule for a coordinated change across packages: the gate is each package's own suite, not the host's.** A package suite boots against the files on disk and never consults `installed.json`. A package whose dependency was renamed in the same wave cannot install standalone at all; that is expected, and it clears when the wave lands.

---

## 2. The sequence

```bash
# 1. green, standalone, from a real resolve
composer update --no-interaction --prefer-dist
vendor/bin/pest

# 2. bump composer.json and module.json together, write the changelog entry

# 3. publish
git add -A && git commit -m "…"
git push origin main
git tag -a 1.1.0 -m 1.1.0 && git push origin 1.1.0

# 4. in the consuming application
composer update liberusoftware/payment-core
php artisan test
git status --porcelain      # must be empty
```

**Step 1 must be a real resolve.** A suite made green against a hand-patched `vendor/` reverts the moment anyone runs `composer update`, and the failure surfaces in someone else's repository. If you patched a dependency locally to get a suite passing, publish that dependency first and re-run against the resolved tree before believing the result.

The same caution applies to a pre-release sweep across many packages: it runs against the working tree, not against the tarball. In the reference fleet a sweep passed while 34 packages were publishing without a `tests/` directory, because the directory existed locally. **A sweep proves the source; only an install proves the release.**

---

## 3. The zero-diff gate

[§6.2](../../architecture/MODULES.md#62-tracked-modules-policy) requires that a clean locked install reproduces the tracked `/modules` tree byte-for-byte. Step 4's `git status --porcelain` is that check, and the host's `install.yml` runs it in CI.

A non-empty diff means the published package and the tracked tree disagree. **The published side is authoritative** — that is what "the module repository is source of truth" means in practice. Resolve it by publishing the missing change, not by committing the diff.

---

## 4. Why the triggers differ

`tests.yml` runs on every push. `install.yml` and `compatibility.yml` run on tags only.

Resolving the package from nothing, and resolving it `--prefer-lowest`, are questions about the **declared constraints**. Those change when `composer.json` changes, which is a release event — not when a line of code does.

The arithmetic matters at fleet scale. As one workflow calling three reusables, each package ran four jobs per push. A publish sweep pushes every repository within seconds of the others, so one sweep queued **176 jobs**; split as three workflows with only `tests` on push, the same sweep queues **44**.

Add a concurrency group so a re-publish supersedes its own unfinished sweep rather than stacking on it:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

> **Do not read a queue stall as your own amplification.** The observation that prompted the split in the reference fleet — hundreds queued, none running, then pushes creating no runs at all — turned out to coincide with a GitHub Actions incident that throttled webhook triggers. The arithmetic above stands on its own; the incident is a caution about diagnosing infrastructure from symptoms.

---

## 5. `composer validate`, and why not `--strict`

CI validates metadata, but without `--strict`. `--strict` promotes every warning to an error, and one of those warnings is that a published package should omit the `version` field.

This fleet cannot omit it: the resolver compares each manifest against `Composer\InstalledVersions`, and the boundary suite asserts `composer.json` and `module.json` agree on it. `--strict` fails every package for carrying a field they are required to carry.

If you hit that failure, the fix is the validate flag — not the field.

---

## 6. First publication

Registering a package on Packagist is a one-time manual submission at <https://packagist.org/packages/submit>. Subsequent tags update through the repository webhook.

Automating it needs a Packagist API token. Keep that token in `~/.config/composer/auth.json` or a GitHub Actions secret — never on a command line, in a script, or pasted into any transcript.
