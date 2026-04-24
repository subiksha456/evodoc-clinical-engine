import time
from services.interactions import check_interactions
from services.allergies import check_allergies
from services.risk import calculate_risk
from services.conditions import check_conditions
from services.cache import get_cache, set_cache, generate_cache_key
from data.fallback_interactions import FALLBACK_INTERACTIONS

def analyze_case(data):
    start = time.time()

    cache_key = generate_cache_key(data)
    cached = get_cache(cache_key)

    if cached:
        cached["cache_hit"] = True
        return cached

    all_drugs = data.medications + data.patient_history.current_medications

    interactions, source = check_interactions(all_drugs)

    allergies = check_allergies(
        data.medications,
        data.patient_history.allergies
    )

    condition_alerts = check_conditions(
        data.medications,
        data.patient_history.conditions
    )

    # fallback if empty
    if not interactions:
        interactions = FALLBACK_INTERACTIONS
        source = "fallback"

    # risk scoring
    risk_score, risk_level, breakdown = calculate_risk(
        interactions,
        allergies + condition_alerts
    )

    # doctor review logic
    requires_review = False

    if source == "fallback":
        requires_review = True

    if risk_score >= 70:
        requires_review = True

    safe = risk_score < 40

    result = {
        "interactions": interactions,
        "allergy_alerts": allergies,
        "condition_alerts": condition_alerts,
        "safe_to_prescribe": safe,
        "overall_risk_level": risk_level,
        "risk_score": risk_score,
        "risk_breakdown": breakdown,
        "requires_doctor_review": requires_review,
        "source": source,
        "cache_hit": False,
        "processing_time_ms": int((time.time() - start) * 1000)
    }

    set_cache(cache_key, result)

    return result