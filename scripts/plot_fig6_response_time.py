import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/bookinfo_response_time.csv")

for service in df["service_name"].unique():
    s = df[df["service_name"] == service].sort_values("network_latency_ms")
    x = s["network_latency_ms"].tolist()
    plt.figure()
    plt.plot(x, s["istio_avg_response_ms"], marker="o", label="Istio")
    plt.plot(x, s["mcg_avg_response_ms"], marker="o", label="MCG")
    plt.xlabel("Network latency (ms)")
    plt.ylabel("Average response time (ms)")
    plt.title(f"Fig. 6 – Average response time: {service}")
    plt.legend()
    plt.tight_layout()
    plt.show()
