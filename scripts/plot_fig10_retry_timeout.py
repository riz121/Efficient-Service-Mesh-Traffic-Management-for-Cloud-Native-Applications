import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/workload_spike_results.csv")

plt.figure()
plt.plot(df["timestamp"], df["successful_rps"], marker="o", label="Successful")
plt.plot(df["timestamp"], df["failed_rps"], marker="o", label="Failed")
plt.xlabel("Time stamp")
plt.ylabel("Requests per second (RPS)")
plt.title("Fig. 10(a) – Successful and failed requests (workload spike)")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(df["timestamp"], df["blocked_retries_rps"], marker="o")
plt.xlabel("Time stamp")
plt.ylabel("Blocked retries (RPS)")
plt.title("Fig. 10(b) – Blocked requests due to retries/circuit breaker")
plt.tight_layout()
plt.show()
