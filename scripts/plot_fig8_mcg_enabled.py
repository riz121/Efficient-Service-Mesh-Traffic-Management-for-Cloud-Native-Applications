import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/circuit_breaker_results.csv")

plt.figure()
plt.plot(df["timestamp"], df["p95_response_time_ms"], marker="o")
plt.xlabel("Time stamp (10s intervals)")
plt.ylabel("95th percentile response time (ms)")
plt.title("Fig. 8(a) – Response time under MCG + circuit breaking")
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df["timestamp"], df["request_rate_rps"], marker="o")
plt.xlabel("Time stamp (10s intervals)")
plt.ylabel("Request rate (RPS)")
plt.title("Fig. 8(b) – Request rate under MCG + circuit breaking")
plt.tight_layout()
plt.show()
