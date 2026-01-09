"""
MCG Configuration Generator (simple)
-----------------------------------
Reads edge metrics and generates an adaptive YAML config list based on latency thresholds.
"""

from dataclasses import dataclass
import argparse
import pandas as pd
import yaml


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
            config = {"source": row["src"], "destination": row["dst"], "traffic_policy": {}}

            if float(row["response_time_ms"]) > self.policy.latency_threshold_ms:
                config["traffic_policy"]["retryPolicy"] = {
                    "attempts": 3,
                    "perTryTimeout": "2s",
                    "retryOn": "5xx,gateway-error,connect-failure"
                }
                config["traffic_policy"]["circuitBreaker"] = {"maxConnections": 50, "http1MaxPendingRequests": 20}
            else:
                config["traffic_policy"]["retryPolicy"] = {"attempts": 1}
                config["traffic_policy"]["circuitBreaker"] = {"maxConnections": 100}

            configs.append(config)
        return configs

    def export_to_yaml(self, output_file: str):
        configs = self.generate_config()
        with open(output_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(configs, f, sort_keys=False)
        print(f"✅ Configuration exported to {output_file}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--edge_csv", required=True, help="CSV with columns: src,dst,lambda,response_time_ms")
    p.add_argument("--out", default="adaptive_config.yaml")
    p.add_argument("--latency_threshold_ms", type=float, default=200.0)
    args = p.parse_args()

    policy = ThresholdPolicy(latency_threshold_ms=args.latency_threshold_ms)
    gen = MCGConfigGenerator(args.edge_csv, policy)
    gen.load_metrics()
    gen.export_to_yaml(args.out)


if __name__ == "__main__":
    main()
