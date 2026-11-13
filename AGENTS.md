# AgentOS — Repository Engineering Contract

Read this before editing, migrating or deploying Noetfield AgentOS.

## Mission
Build the **actual full-source Noetfield-owned Paperclip derivative**, not a mock dashboard, proxy shell, isolated agent registry or fresh substitute. Restore all upstream UI/server/CLI/DB/adapters and premium features while preserving Noetfield native roles, first-party authentication, Persian/English UX and Paperclip MIT attribution. Source is the **full-history topic branch** `Noetfield-Systems/sina_founder_os:noetfield-agentos/full-history-premium-v1`. See `docs/SERVICE-INVENTORY.md` and `docs/FULL-FORK-CUTOVER.md`.

## Mandatory owned-fork rule — no Paperclip Cloud
- There is **no wait for Paperclip Cloud, vendor SaaS, third-party Board key, or a replacement upstream image**. The actual app and native company-scoped APIs are self-hosted in the existing `noetfield-agentos-canary` service. First-party owner login/permissions are still required for real mutations.
- **Authoritative current 8-team source:** `Noetfield-Systems/sina_founder_os` / `noetfield-agentos/full-history-premium-v1`, `ui/src/noetfield/venture-team-presets.ts`. Its native People Office uses authenticated same-instance APIs, with heartbeats off until worker commissioning.
- **Latest runtime charter:** `doc/plans/2026-11-13-sina-autonomous-venture-runtime-contract.md` in the source branch. This is the operating policy for Hassan, Farid, seven proposed venture GMs, five feedback loops and 14 acceptance checks. It must not be displaced by historical upstream documents or by a duplicate agent registry.
- Report real source status as `DEFINED`, `NATIVE_REGISTERED`, `RUN_EXECUTED`, `INDEPENDENTLY_VERIFIED`, `REAL_USER_ACTIVE`, `CASH_COLLECTED` separately. Kian, Arash, Raha, Nima, Navid, Dara, Sam are proposed until source-native identity and runtime readback exists; Farid remains `gm-buildrelay-farid`; Hassan is a single portfolio executive and Asad is unmapped.
- Do not treat the earlier `paperclip-agent-workforce` image as the product to upgrade; maintain it only as a legacy rollback footprint until existing owned service cutover is proven.

## Correct authority and execution topology
1. Sina Founder OS holds the original Founder goal, strategy and portfolio authority.
2. Company OS/NOOS holds workstreams, real company operations and current approved plan.
3. AgentOS holds native companies, people, goals, teams, agents, issues, approvals, budgets, heartbeats, skills, tasks and history.
4. Existing Governor/NAC issues or verifies the bounded authorization; neither a Paperclip task nor any agent prompt constitutes an execution permit.
5. Existing Agent Fabric / Runway / remote model runners perform authorized work; do not duplicate their orchestration or infer a runner from a scheduler.
6. Existing Independent Verifier validates artifacts and outcomes. Company Floor displays traceable readback; not another source of truth.

## Required operating loop
`Founder intent → source-backed WorkPacket → original manager/agent assignment → governed runner → concrete artifact or effect → independent QA/verifier → exact source-linked receipt → Company Floor`.

For any blocker, assign an owner, deadline and next concrete action; retry reversible operations with idempotency; explain a real access/permission constraint without introducing arbitrary commercial gates. Prevent `FOUNDER_INTENT_DRIFT`. Do not lose the objectives of independent BuildRelay, Cairn, Earnloop, TrustField or WorkforceOS through cross-product edits.

## Proof ladder
`SOURCE_IMPORTED` is not `TESTED`; `TESTED` is not `DEPLOYED`; `DEPLOYED` is not `WORKFORCE_COMMISSIONED`; `ISSUE_CREATED` is not `REAL_TASK_EXECUTED`; a worker result is not `INDEPENDENT_OUTCOME_VERIFIED`; internal credits are not `CASH_COLLECTED`.

Never manufacture successful task logs, user accounts, tokens, transactions, signatures, payment receipts or production URLs.

## Scope boundaries
- Reuse Railway service `noetfield-agentos-canary` in existing `noetfield-agent-workforce` staging environment, existing PostgreSQL and persistent `/paperclip` volume. Keep original Paperclip image as separate legacy footprint until cutover is tested; no duplicate project or extra DB.
- Do **not** repoint canary to this repository before a complete source import and build.
- Do not copy secrets, PostgreSQL data, agent prompts containing private user material or volume backups into Git.
- Protect company/venture tenant boundaries, role scopes, credential isolation and legitimate payment/settlement controls.
- The AgentOS repository is public; review new commits for confidential information.
- No destructive source changes, default admin bypass or irreversible external financial actions without an actual authorized task.

## Acceptance tests
- Full source tree and preserved MIT license/attribution, with history integrity recorded.
- `pnpm install --frozen-lockfile`, UI/server builds, adapter regression, tenant isolation and native owner login tests.
- Authenticated company and Issue create/readback, model/runner heartbeat, one bounded **real** WorkPacket, receipt linked to exactly one issue.
- GitHub CI and Railway live status verified after deployment, with rollback checkpoint.
- Clear `CURRENT`/ `MISSING` register on all platform claims; integrate one piece at a time rather than displacing other repo owners.

## Permanent instruction
When asked to **build/ship/deploy**, prefer executable code changes, tests, and evidence-backed deployment over more planning. The bootstrapped repository is not the full fork yet: migrate its real code instead of re-implementing it.
