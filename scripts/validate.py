#!/usr/bin/env python3
"""Check for known drug interaction severity between two medications."""
import json, sys

# Simplified interaction database (real system would call RxNorm/OpenFDA)
KNOWN_INTERACTIONS = {
    ("warfarin", "aspirin"): {"severity": "major", "effect": "Increased bleeding risk"},
    ("metformin", "alcohol"): {"severity": "major", "effect": "Lactic acidosis risk"},
    ("ssri", "maoi"): {"severity": "contraindicated", "effect": "Serotonin syndrome"},
    ("ace_inhibitor", "potassium"): {"severity": "moderate", "effect": "Hyperkalemia risk"},
    ("statin", "grapefruit"): {"severity": "moderate", "effect": "Increased statin levels"},
}

def check_interaction(data):
    drug_a = data.get("drug_a", "").lower()
    drug_b = data.get("drug_b", "").lower()
    pair = tuple(sorted([drug_a, drug_b]))

    interaction = KNOWN_INTERACTIONS.get(pair)
    if interaction:
        return {"drugs": [drug_a, drug_b], "interaction": True, **interaction}
    return {
        "drugs": [drug_a, drug_b],
        "interaction": False,
        "note": "No known interaction in local DB — verify with openfda_get_adverse_events"
    }

if __name__ == "__main__":
    print(json.dumps(check_interaction(json.loads(sys.argv[1])), indent=2))
