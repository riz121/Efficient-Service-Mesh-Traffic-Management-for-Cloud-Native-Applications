import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ubbench_fault_injection.csv")

plt.figure()
plt.plot(df["timestamp"], df["response_time_ms"], marker="o")
plt.xlabel("Time stamp (10s intervals)")
plt.ylabel("End-to-end response time (ms)")
plt.title("Fig. 7(a) – End-to-end latency (no traffic management)")
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df["timestamp"], df["request_rate_rps"], marker="o")
plt.xlabel("Time stamp (10s intervals)")
plt.ylabel("Request rate (RPS)")
plt.title("Fig. 7(b) – Request rate (no traffic management)")
plt.tight_layout()
plt.show()
