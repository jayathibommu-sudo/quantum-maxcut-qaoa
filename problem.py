import random
import networkx as nx

def create_weighted_graph(n=6, p=0.5, seed=42):
    graph = nx.erdos_renyi_graph(n=n, p=p, seed=seed)
    rng = random.Random(seed)
    for u, v in graph.edges():
        graph[u][v]["weight"] = rng.randint(1, 5)
    return graph

def cut_value(graph, bits):
    if len(bits) != graph.number_of_nodes():
        raise ValueError("Bit assignment length must equal graph node count.")
    return sum(data["weight"] for u, v, data in graph.edges(data=True)
               if bits[u] != bits[v])

def score_qiskit_bitstring(graph, bitstring):
    return cut_value(graph, bitstring.replace(" ", "")[::-1])
