"""
MCG Builder Algorithm
---------------------
This script constructs a Microservice Communication Graph (MCG)
based on observed communication between microservices.
"""

from dataclasses import dataclass
import pandas as pd
import networkx as nx


@dataclass
class ServiceNode:
    name: str
    cpu_usage: float
    memory_mb: float


@dataclass
class EdgeMetric:
    src: str
    dst: str
    lambda_val: float
    response_time_ms: float


class MCGBuilder:
    def __init__(self, cpu_memory_csv: str, edge_metrics_csv: str):
        self.cpu_memory_csv = cpu_memory_csv
        self.edge_metrics_csv = edge_metrics_csv
        self.graph = nx.DiGraph()

    def load_data(self):
        self.cpu_data = pd.read_csv(self.cpu_memory_csv)
        self.edge_data = pd.read_csv(self.edge_metrics_csv)

    def build_graph(self):
        # Add nodes
        for _, row in self.cpu_data.iterrows():
            node = ServiceNode(row["service_name"], row["cpu_usage"], row["memory_mb"])
            self.graph.add_node(node.name, cpu=node.cpu_usage, memory=node.memory_mb)

        # Add edges
        for _, row in self.edge_data.iterrows():
            edge = EdgeMetric(row["src"], row["dst"], row["lambda"], row["response_time_ms"])
            self.graph.add_edge(edge.src, edge.dst, weight=edge.lambda_val, latency=edge.response_time_ms)

    def get_summary(self):
        summary = {
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges),
            "avg_latency_ms": sum(nx.get_edge_attributes(self.graph, "latency").values()) / len(self.graph.edges)
        }
        return summary

    def visualize(self, output_path="mcg_graph.png"):
        import matplotlib.pyplot as plt

        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=2000, node_color="lightblue", arrows=True)
        edge_labels = nx.get_edge_attributes(self.graph, 'latency')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Microservice Communication Graph (MCG)")
        plt.savefig(output_path)
        plt.close()


if __name__ == "__main__":
    builder = MCGBuilder(
        cpu_memory_csv="../data/sample_metrics/cpu_memory_metrics.csv",
        edge_metrics_csv="../data/sample_metrics/edge_metrics.csv"
    )
    builder.load_data()
    builder.build_graph()
    print("Graph Summary:", builder.get_summary())
