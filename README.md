# Pharmacy Intelligence Skill

> Global drug reference and regulatory intelligence for AI agents — OpenFDA, DailyMed, RxNorm, PubChem, Health Canada, EMA, MHRA, and ClinicalTrials.gov. All free, no API keys.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--pharmacy-green)](https://github.com/zavora-ai/mcp-pharmacy)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | What It Achieves |
|----------|-------|------------------|
| Drug Lookup | 2-3 | Normalize + label + safety |
| Safety Check | 2 | Adverse events + recalls |
| Global Registration | 2 | Approved in which countries |
| Clinical Trials | 2 | Active studies for condition |
| Compound Research | 1-2 | Molecular properties |

### Global Coverage

| Source | Region | Data |
|--------|--------|------|
| OpenFDA | US | Labels, adverse events, recalls, NDC |
| DailyMed | US | Full prescribing information |
| RxNorm | US | Drug name normalization |
| PubChem | Global | Compound properties |
| Health Canada | Canada | Product approvals |
| EMA | EU | Medicine authorizations |
| MHRA | UK | Safety updates |
| ClinicalTrials.gov | Global | Active/completed trials |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-pharmacy-intelligence.git ~/.skills/skills/pharmacy-intelligence
```

## Requirements

**Required:** `mcp-pharmacy` (19 tools — all free public databases, no API keys)
**Cross-MCP:** `mcp-medical` (PubMed evidence), `mcp-legal` (recall compliance)

## Success Criteria

| Metric | Target |
|--------|--------|
| Safety first | Always check adverse events + recalls |
| Global coverage | US, Canada, EU, UK registration status |
| Name normalization | RxNorm before searching |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
