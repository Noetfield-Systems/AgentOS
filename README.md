# Noetfield AgentOS

**Noetfield's owned Paperclip-derived AI workforce operating system.**

This repository is the **dedicated canonical destination** for the complete customized fork. The existing full-source fork is currently maintained on [`Noetfield-Systems/sina_founder_os` branch `noetfield-agentos/full-history-premium-v1`](https://github.com/Noetfield-Systems/sina_founder_os/tree/noetfield-agentos/full-history-premium-v1). The existing live canary uses that branch. **Do not confuse this destination's current documentation/bootstrap state with a completed full-source migration or production cutover.**

## Current verified inventory (2026-11-13)

| Layer | Canonical existing owner | What exists |
| --- | --- | --- |
| Forked agent organization | `sina_founder_os:noetfield-agentos/full-history-premium-v1` | Paperclip v2026.1106.0 full-source derivative, Noetfield overlays and history attestation |
| Customized AgentOS canary | Railway `noetfield-agent-workforce/staging/noetfield-agentos-canary` | Successful deployment; `/api/health`; persistent `/paperclip` volume |
| Original Paperclip container | Railway `noetfield-agent-workforce/staging/paperclip-agent-workforce` | Upstream `ghcr.io/paperclipai/paperclip:2026.1023.0`; distinct persistent volume |
| Human/agent workforce customer product | `Noetfield-Systems/WorkforceOS` | Separately deployed `workforce-os/production/workforce-web` |
| Founder goals & strategy | `Noetfield-Systems/sina_founder_os` | Founder intent, portfolio directives and bridge |
| Business operations | `Noetfield-Systems/noetfeld-os` | Company OS / NOOS, including staging deployments and production loop runner |
| Execution | `sina_founder_os` Agent Fabric and `NOETFIELD-RUNWAY` | Existing workers, permissions, event and run tracking |
| Independent verification | `Noetfield-Systems/Verification_Layer` | Existing production verification-layer-api |
| Read-only operational floor | `sina_founder_os` | Existing Railway `sina-company-floor` |

**No duplicate Railway project, database, server, or agent runtime is authorized by this consolidation.** Preserve source ownership and volumes. Keep customer-facing WorkforceOS distinct from internal AgentOS. Separate ventures retain separate legal/tenant boundaries.

## Import provenance

- Source: [Paperclip](https://github.com/paperclipai/paperclip), release `v2026.1106.0` (upstream MIT).
- Customized fork provenance and contract: [`noetfield/source-attestation.json`](https://github.com/Noetfield-Systems/sina_founder_os/blob/noetfield-agentos/full-history-premium-v1/noetfield/source-attestation.json) and [`noetfield/FOUNDER-EXECUTION-CONTRACT.md`](https://github.com/Noetfield-Systems/sina_founder_os/blob/noetfield-agentos/full-history-premium-v1/noetfield/FOUNDER-EXECUTION-CONTRACT.md).
- The source currently resides on a branch of another repository, **not** a native GitHub fork. Mirror the *full* upstream-derived tree and preserved rewritten-history chain into this dedicated repository before switching the Railway canary's source.
- Retain the upstream MIT LICENSE and copyright notices when importing any Paperclip source; never copy environment secrets, instance databases, runtime volumes, private user records, or external credentials.

## Execution contract

`Founder goal → Company OS governed workpacket → AgentOS agent/task ownership → Agent Fabric/Runway execution → independent verification → Company Floor readback`.

Keep task statuses separate: `SOURCE_IMPORTED`, `OVERLAY_TESTED`, `CANARY_DEPLOYED`, `WORKFORCE_COMMISSIONED`, `REAL_TASK_EXECUTED`, `INDEPENDENT_OUTCOME_VERIFIED`, `CANONICAL_CUTOVER`. Deployment does not establish autonomous execution, sales, or verified outcomes.

## Deployment policy

**Keep the current Railway service and persistent volume.** Existing AgentOS canary: https://noetfield-agentos-canary-staging.up.railway.app . Only switch its GitHub source to this repository after a complete source import, lockfile/build/test checks, and successful healthcheck on the candidate commit. Never point that running service at this currently incomplete repository.

The mapping, verification contracts, and cutover runbook are in `docs/`. These declarations are operational references; the live configuration reported by Railway remains authoritative.
