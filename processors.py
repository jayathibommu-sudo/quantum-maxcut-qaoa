import json
from pathlib import Path
from qiskit.transpiler import CouplingMap

def load_processor(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def coupling_map_from_json(path):
    config = load_processor(path)
    edges = config["coupling_edges_undirected"]
    return CouplingMap(couplinglist=edges + [[v, u] for u, v in edges])
