"""
MCG Configuration Generator
---------------------------
This script reads an MCG (Microservice Communication Graph) and
generates adaptive YAML configurations (e.g., retries, circuit breakers)
based on performance metrics.
"""

import yaml
import pandas as pd
from dataclasses import dataclass


@dataclass
class ThresholdPolicy:
    latency_threshold_ms: float = 200.0
    error_rate_threshold: float = 0.05
    cpu_threshold: float = 0.8


class MCGConfigGenerator:
    def __init__(self, edge_metrics_csv: str, policy: ThresholdPolicy):
        self.edge_metrics_csv = edge_metrics_csv
        self.policy = policy

    def load_metrics(self):
        self.metrics = pd.read_csv(self.edge_metrics_csv)

    def generate_config(self):
        configs = []

        for _, row in self.metrics.iterrows():
            config = {
                "source": row["src"],
                "destination": row["dst"],
                "traffic_policy": {}
            }

            # Latency-based adaptation
            if row["response_time_ms"] > self.policy.latency_threshold_ms:
                config["traffic_policy"]["retryPolicy"] = {
                    "attempts": 3,
                    "perTryTimeout": "2s",
                    "retryOn": "5xx,gateway-error,connect-failure"
                }
                config["traffic_policy"]["circuitBreaker"] = {
                    "maxConnections": 50,
                    "http1MaxPendingRequests": 20
                }
            else:
                config["traffic_policy"]["retryPolicy"] = {"attempts": 1}
                config["traffic_policy"]["circuitBreaker"] = {"maxConnections": 100}

            configs.append(config)

        return configs

    def export_to_yaml(self, output_file="adaptive_config.yaml"):
        configs = self.generate_config()
        with open(output_file, "w") as f:
            yaml.dump(configs, f, sort_keys=False)
        print(f"✅ Configuration exported to {output_file}")


if __name__ == "__main__":
    policy = ThresholdPolicy(latency_threshold_ms=200.0, error_rate_threshold=0.05, cpu_threshold=0.8)
    generator = MCGConfigGenerator("../data/sample_metrics/edge_metrics.csv", policy)
    generator.load_metrics()
    generator.export_to_yaml("adaptive_config.yaml")
