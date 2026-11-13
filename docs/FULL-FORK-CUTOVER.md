# AgentOS — Full Fork Migration and Live Cutover

**Objective:** relocate the already-owned full-source Paperclip derivative from the `sina_founder_os` topic branch to `Noetfield-Systems/AgentOS`, preserving rewritten history and Paperclip premium functionality, then switch the **existing** Railway canary's GitHub source without changing its service ID, database, volumes or public hostname.

## Source to move

`Noetfield-Systems/sina_founder_os` branch `noetfield-agentos/full-history-premium-v1` (tip during audit `dff29e5ebed9cd762e5099adb5b645ac0ca14fba`). This is **not** a folder-only extraction from main: the topic branch root is an entire Paperclip-derived repository. The upstream license and 5,534 rewritten-history ancestors must remain. Additional changes on the source branch after that tip must be incorporated, not overwritten.

## Authenticated Git transfer (run with an owner-approved Git credential with source read and AgentOS write)

```bash
set -euo pipefail
mkdir -p /tmp/agentos-consolidation
cd /tmp/agentos-consolidation
# Clone ONLY the full-source fork branch (keeps complete reachable history).
git clone --single-branch --branch noetfield-agentos/full-history-premium-v1 \\
  git@github.com:Noetfield-Systems/sina_founder_os.git agentos-full
cd agentos-full
git rev-list --count HEAD
test -f LICENSE && test -d server && test -d ui && test -d packages && test -d cli
git remote add canonical git@github.com:Noetfield-Systems/AgentOS.git
# Non-destructive: push a new import branch; do NOT overwrite main yet.
git push canonical HEAD:refs/heads/import/full-history-premium-v1
```

Verify `import/full-history-premium-v1` contains `pnpm-lock.yaml`, full code, upstream MIT `LICENSE`, `noetfield/source-attestation.json`, source contracts, and `.github/workflows` limited to reviewed Noetfield workflows. Compare tip and number of reachable commits. Merge or cherry-pick this repository's bootstrap docs/bridge/tests into the full-source branch, run `pnpm install --frozen-lockfile`, TypeScript builds, native UI tests, server tests, Python bridge tests and healthcheck smoke. Do not use force push on the destination `main` without a reviewed lease and preserved bootstrap commit.

## Canary cutover

1. Confirm source import CI is green and production secrets are not in Git.
2. Confirm native first-owner setup, company/team IDs, agent permission scopes, and the provider/runner are **actually** commissioned; no default public admin bypass.
3. Snapshot/backup the existing canary's attached `/paperclip` volume and database; do not copy into source.
4. On existing Railway project `noetfield-agent-workforce`, environment `staging`, service `noetfield-agentos-canary`, switch source to AgentOS **only after** its full app branch is deployable; retain existing domain, vars and volume.
5. Verify Railway status, `/api/health`, authenticated login, company isolation, Issue creation/readback, live agent heartbeat, exact WorkPacket trace, bounded worker action, and independently checked receipt.
6. Roll back to pinned prior source commit if health/readback fails. **Do not decommission upstream container** until cutover evidence is written.

## Why this is not complete yet

The connected GitHub action supports file and Git object writes **within** a repository, not `git push --mirror` or direct sharing of blobs across unrelated repositories: GitHub rejected a cross-repository blob reference with HTTP 422. This initial repository therefore holds the source-backed operational contracts and bridge, **not yet the full application**, and must not be deployed as a replacement for the working canary.
