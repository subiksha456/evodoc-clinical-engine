CONDITION_RULES = {
    "kidney disease": ["ibuprofen", "diclofenac"],
    "hypertension": ["pseudoephedrine"],
}

def check_conditions(meds, conditions):
    alerts = []

    meds = [m.lower() for m in meds]
    conditions = [c.lower() for c in conditions]

    for condition in conditions:
        if condition in CONDITION_RULES:
            risky_drugs = CONDITION_RULES[condition]

            for med in meds:
                if med in risky_drugs:
                    alerts.append({
                        "condition": condition,
                        "medicine": med,
                        "reason": f"contraindicated for {condition}",
                        "severity": "high"
                    })

    return alerts