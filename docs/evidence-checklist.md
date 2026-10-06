# HIPAA Security Rule — CSW Evidence Checklist

A printable worklist for the evidence owner. For each item: **what** to export, **where** from in CSW, and the **cadence**. Tick as you collect; file exports to immutable storage (not screenshots taken during audit week).

> Legend — 🟢 Direct · 🟠 Supporting · ⚪ Evidence Required *(supplied outside CSW)*. CSW evidence is an input to compliance, not an attestation.

---

## Phase 1 — Coverage (Days 1–10)

- [ ] In-scope host list reconciled to **CSW Inventory** (100% or documented exceptions)
- [ ] Labels applied: `compliance:hipaa`, `data:<class>`, `env:<tier>`, `app:*`, `owner:*`
- [ ] CSW scope tree created matching the compliance boundary
- [ ] **Export:** inventory CSV + agent-status screenshot → `evidence/01-coverage/`

## Phase 2 — Baseline (Days 11–28)

- [ ] ADM running on the compliance scope for ≥ 2 weeks (full business cycle)
- [ ] Unexpected flows documented (shadow IT, vendor egress, scope creep)
- [ ] App owners signed the cluster-to-application mapping
- [ ] **Export:** ADM diagram + flow samples with process context → `evidence/02-baseline/`

## Phase 3 — Policy (Days 29–45)

- [ ] Default-deny posture defined for the sensitive scope
- [ ] ADM-imported rules refined; **Simulation** run ≥ 1 week
- [ ] Change tickets raised for false positives; exception register updated
- [ ] **Export:** policy export + simulation report → `evidence/03-policy/`

## Phase 4 — Operate (ongoing)

- [ ] Enforcement enabled; negative test recorded in **Denied Connections**
- [ ] SIEM integration verified with sample events
- [ ] Quarterly binder assembled
- [ ] **Export:** enforcement screenshot + quarterly binder → `evidence/04-operate/`

---

## Recurring evidence pack

| # | Evidence item | CSW location | Cadence | Collected |
|---|---|---|---|:--:|
| 1 | Network policy export | Defend → Policy Workspaces | Per assessment | ☐ |
| 2 | Inbound/outbound flow log | Investigate → Flow Search | Continuous | ☐ |
| 3 | Policy-violation report | Alerts → Triggered Events | Monthly | ☐ |
| 4 | Vulnerability + reachability report | Investigate → Vulnerability | Weekly | ☐ |
| 5 | Scope-membership snapshot | Inventory → Export | Monthly | ☐ |
| 6 | Anomaly / baseline-deviation log | Alerts → Dashboard | Monthly | ☐ |
| 7 | ADM dependency map | Investigate → ADM | Quarterly | ☐ |
| 8 | Process audit log | Investigate → Process Search | On-demand | ☐ |

The framework-specific control-to-evidence mapping is in the [Reference Design](../CSW-HIPAA-Reference-Design.md).

```
evidence/
├── 01-coverage/   inventory.csv, agent-status.png
├── 02-baseline/   adm-map.pdf, flow-samples.csv
├── 03-policy/     policy-export.json, simulation-report.pdf, exceptions.xlsx
└── 04-operate/    QYYYY-Qn/  (quarterly binder: items 1–8)
```

*Validate sufficiency of every item with your assessor. CSW does not replace crypto/key-management, physical, or HR evidence.*
