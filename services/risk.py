def calculate_risk(interactions, allergies):
    score = 0
    breakdown = []

    # interaction scoring
    for i in interactions:
        severity = i["severity"]

        if severity == "high":
            score += 40
            breakdown.append("high interaction +40")
        elif severity == "medium":
            score += 25
            breakdown.append("medium interaction +25")
        elif severity == "low":
            score += 10
            breakdown.append("low interaction +10")

    # allergy scoring (very critical)
    for a in allergies:
        score += 50
        breakdown.append("allergy +50")

    # cap score at 100
    score = min(score, 100)

    # determine level
    if score >= 70:
        level = "high"
    elif score >= 40:
        level = "medium"
    else:
        level = "low"

    return score, level, breakdown