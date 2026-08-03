# Git technology reference

Git is the change-management layer for documentation, modules, applications, and releases. Keep commits reviewable, preserve history, and make the branch state reproducible.

## Practical workflow

```bash
git status
git diff --check
git add path/to/changed-files
git commit -m "Describe the focused change"
git push origin main
```

Never commit secrets, generated dependency directories, environment files, or unreviewed lockfile churn. Before a documentation change, run Markdown formatting, link checks, and repository-specific tests. Before a release, review the diff, changelog, migration notes, compatibility matrix, and rollback/runbook updates.

Official references: [Pro Git](https://git-scm.com/book/en/v2), [Git reference](https://git-scm.com/docs), [GitHub documentation](https://docs.github.com/en), and [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow). Related local guides: [contributing](../standards/CONTRIBUTING.md), [CI](../standards/CI.md), and [repository architecture](../architecture/REPOSITORIES.md).
