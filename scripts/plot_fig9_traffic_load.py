import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/traffic_load_results.csv")

plt.figure()
plt.plot(df["timestamp"], df["successful_rps_80pct"], marker="o", label="Successful (80%)")
plt.plot(df["timestamp"], df["blocked_rps_80pct"], marker="o", label="Blocked (80%)")
plt.plot(df["timestamp"], df["successful_rps_120pct"], marker="o", label="Successful (120%)")
plt.plot(df["timestamp"], df["blocked_rps_120pct"], marker="o", label="Blocked (120%)")
plt.xlabel("Time stamp")
plt.ylabel("Requests per second (RPS)")
plt.title("Fig. 9 – Impact of varying inbound traffic load")
plt.legend()
plt.tight_layout()
plt.show()
