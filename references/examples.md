# Pharmacy Examples

## Example 1: "Tell me about metformin"
```
rxnorm_normalize(name: "metformin") → {rxcui: "6809", name: "metformin hydrochloride"}
openfda_search_labels(drug: "metformin") → {indications: "Type 2 diabetes", dosage: "500-2000mg/day"}
openfda_get_adverse_events(drug: "metformin", limit: 5) → {top: ["nausea", "diarrhea", "lactic acidosis (rare)"]}
```
Response: "Metformin (RxCUI: 6809): Type 2 diabetes. Dose: 500-2000mg/day. Common AEs: nausea, diarrhea. Rare: lactic acidosis."

## Example 2: "Is this drug approved in the EU?"
```
get_registration_status(drug: "semaglutide") → {US: "approved", EU: "approved", Canada: "approved", UK: "approved"}
ema_search_medicines(name: "semaglutide") → {brand: "Ozempic", status: "authorised", date: "2018"}
```
Response: "Semaglutide (Ozempic): Approved in US, EU (2018), Canada, UK. EMA authorised."
