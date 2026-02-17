def interpret_probabilities(probs):
    p_trend = probs.get("001", 0)
    p_transition = probs.get("110", 0)

    if p_trend > 0.55:
        return "STABLE RISK-ON / TREND REGIME"
    elif p_transition > 0.55:
        return "ROTATIONAL / TRANSITIONAL REGIME"
    else:
        return "MIXED / UNCERTAIN"
