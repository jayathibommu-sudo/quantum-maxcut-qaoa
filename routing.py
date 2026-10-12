from qiskit import transpile

BASIS_GATES = ["rz", "sx", "x", "cx"]

def transpile_unconstrained(circuit, seed=42):
    return transpile(circuit, basis_gates=BASIS_GATES,
                     optimization_level=1, seed_transpiler=seed)

def transpile_for_processor(circuit, coupling_map, seed=42):
    return transpile(circuit, basis_gates=BASIS_GATES, coupling_map=coupling_map,
                     optimization_level=1, seed_transpiler=seed)

def routing_overhead_proxy(baseline, routed):
    base_ops, routed_ops = baseline.count_ops(), routed.count_ops()
    return {
        "baseline_depth": baseline.depth(),
        "routed_depth": routed.depth(),
        "depth_delta": routed.depth() - baseline.depth(),
        "baseline_cx": int(base_ops.get("cx", 0)),
        "routed_cx": int(routed_ops.get("cx", 0)),
        "cx_delta": int(routed_ops.get("cx", 0) - base_ops.get("cx", 0)),
        "note": "CX/depth deltas are proxies, not exact SWAP counts."
    }
