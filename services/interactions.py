from services.llm import call_llm
from data.fallback_interactions import FALLBACK_INTERACTIONS
import json

def check_interactions(drugs):
    results = []
    source = "fallback"

    drugs = [d.lower() for d in drugs]

    for i in range(len(drugs)):
        for j in range(i + 1, len(drugs)):
            a, b = drugs[i], drugs[j]

            prompt = f"Check interaction between {a} and {b}. Return JSON."

            llm_output = call_llm(prompt)

            # 👉 THIS IS THE PART YOU ASKED ABOUT
            if llm_output:
                try:
                    parsed = json.loads(llm_output)

                    results.append({
                        "drug_a": a,
                        "drug_b": b,
                        "severity": parsed.get("severity", "medium"),
                        "mechanism": parsed.get("mechanism", ""),
                        "clinical_recommendation": parsed.get("clinical_recommendation", ""),
                        "source_confidence": parsed.get("confidence", "medium")
                    })

                    source = "llm"

                except:
                    pass

    # 👉 fallback if nothing from LLM
    if not results:
        results = FALLBACK_INTERACTIONS
        source = "fallback"

    return results, source