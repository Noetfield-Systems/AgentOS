# AgentOS — Verified Source and Service Register

As of 2026-11-13, inspected via authenticated GitHub and Railway connectors.

**Canonical target:** `Noetfield-Systems/AgentOS` (public; initialized 2026-11-13). This is a *partially assembled consolidation repository*. The full Paperclip-derived application has **not** yet been transferred here. Its live deployment remains sourced from the existing verified fork branch.

## Code provenance

- Full customized source: `Noetfield-Systems/sina_founder_os`, branch `noetfield-agentos/full-history-premium-v1`, tip `dff29e5ebed9cd762e5099adb5b645ac0ca14fba` at audit.
- Upstream: `paperclipai/paperclip` release `v2026.1106.0`, original SHA `d69631b01b9c658f80bf8bed389863dce82643e1`, MIT license; source attestation describes 5,534 ancestors preserved with workflow-path rewrite.
- This repository retains reviewed Noetfield contract, attestation, architecture and bridge/test code under source-owned paths; do not infer that all `server/`, `ui/`, `packages/` and `cli/` are present until the full history transfer is proven.

## Deployed footprint (Railway)

| Railway project / environment | Service | Source | Status at audit | Purpose |
|---|---|---|---|---|
| noetfield-agent-workforce / staging | noetfield-agentos-canary | `sina_founder_os:noetfield-agentos/full-history-premium-v1` | SUCCESS / online 1 of 1 | Customized full-source Paperclip derivative; its own persistent `/paperclip` volume |
| noetfield-agent-workforce / staging | paperclip-agent-workforce | `ghcr.io/paperclipai/paperclip:2026.1023.0` | SUCCESS | Earlier uncustomized Paperclip image, independent volume |
| noetfield-agent-workforce / staging | noetfield-agent-fabric-staging | `sina_founder_os:feat/sina-first-self-build-20261109` | SUCCESS | Existing run/agent workers and bridge |
| noetfield-agent-workforce / staging | sina-founder-os-staging | `sina_founder_os:main` | SUCCESS | Founder authority and portfolio management |
| noetfield-agent-workforce / staging | sina-selfbuild-verifier-staging | `sina_founder_os:feat/sina-first-self-build-20261109` | SUCCESS | Verifier service |
| company-os-hardening-staging / staging | company-os-staging | `noetfeld-os:feat/nexus-company-os-growth-bridge-20261109` | SUCCESS | Existing Company OS workstreams |
| noetfield-platform / production | noos-loop-runner | `noetfeld-os:deploy/noos-loop-runner-entrypoint` | SUCCESS | Existing loop runner |
| sina-company-floor / production | sina-company-floor | `sina_founder_os:main` | SUCCESS | Source-linked operational floor |
| noetfield-platform / production | verification-layer-api | `Verification_Layer:main` | SUCCESS | Independent receipts API |
| workforce-os / production | workforce-web | `WorkforceOS:main` | SUCCESS | Separately scoped customer-facing WorkforceOS |
| noetfield-runway-staging / production | runway-heavy-executor | `NOETFIELD-RUNWAY:main` | No deployment recorded; staged changes exist | Do not mark execution ready |

Live service domain: https://noetfield-agentos-canary-staging.up.railway.app ; `/api/health` is its configured healthcheck. The Railway deployment state is verified, but no authenticated workpacket → runner → signed receipt end-to-end acceptance test has been performed by this consolidation.

## Consolidation categories

- **IN REPO:** Noetfield source contract, architecture, provenance, and reusable permitted-issue bridge with source tests.
- **EXISTING FULL SOURCE:** React UI, Paperclip Node API, packages/db, CLI, adapters, managed agents/skills, copied upstream workflows (not copied into this destination yet).
- **LIVE BUT EXTERNAL:** Agent Fabric, Company OS, Runway, independent verifier, Company Floor, WorkforceOS; keep their own source and databases.
- **NOT VERIFIED:** First owner fully commissioned, native workforce operating without intervention, actual worker execution, independent signed delivery receipts attached to native Issue, canonical source cutover, production SLA, monetized activity.

A `SUCCESS` Railway build is not evidence of a successful task. Existing service data, volumes and secrets must not be copied into source control.
