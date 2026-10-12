def summarize_counts(counts, graph, score_bitstring, classical_optimum):
    shots = sum(counts.values())
    if shots <= 0:
        raise ValueError("No measurement shots found.")
    cut_sum = sum(score_bitstring(key, graph) * frequency for key, frequency in counts.items())
    best = max(score_bitstring(key, graph) for key in counts)
    average = cut_sum / shots
    return {
        "shots": shots,
        "average_cut": average,
        "best_observed_cut": best,
        "approximation_ratio": average / classical_optimum if classical_optimum else 0.0
    }
