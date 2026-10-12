import matplotlib.pyplot as plt
import networkx as nx

def draw_weighted_graph(graph, output_path):
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(graph, pos, with_labels=True, node_size=900)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "weight"))
    plt.title("Six-node weighted Max-Cut graph")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=160)
    plt.close()
