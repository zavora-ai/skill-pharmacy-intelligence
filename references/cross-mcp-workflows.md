# Pharmacy Cross-MCP Workflows

## Pharmacy + Medical: Drug + Evidence
```
PHARMACY: rxnorm_normalize(name: "ozempic") → semaglutide
PHARMACY: openfda_get_adverse_events(drug: "semaglutide")
MEDICAL: pubmed_search(query: "semaglutide efficacy weight loss 2024")
```

## Pharmacy + Legal: Recall → Compliance
```
PHARMACY: openfda_search_recalls(drug: "contaminated_batch") → active recall
LEGAL: search_federal_register(query: "FDA recall notice")
NOTIFICATIONS: send_notification(recipient: compliance_team, title: "⚠️ Drug recall alert")
```
