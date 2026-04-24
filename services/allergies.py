ALLERGY_MAP = {
    "penicillin": ["amoxicillin", "ampicillin"],
}

def check_allergies(meds, allergies):
    alerts = []

    meds = [m.lower() for m in meds]
    allergies = [a.lower() for a in allergies]

    for allergy in allergies:
        if allergy in ALLERGY_MAP:
            for med in meds:
                if med in ALLERGY_MAP[allergy]:
                    alerts.append({
                        "medicine": med,
                        "reason": f"{allergy} class",
                        "severity": "critical"
                    })

    return alerts