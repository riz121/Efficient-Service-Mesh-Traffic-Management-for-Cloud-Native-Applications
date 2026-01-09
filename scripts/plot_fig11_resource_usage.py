import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/resource_efficiency_scalability.csv")

plt.figure()
plt.bar(df["approach"], df["cpu_usage_millicores"])
plt.ylabel("CPU usage (millicores)")
plt.title("Fig. 11(a) – CPU usage comparison")
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(df["approach"], df["memory_usage_gb"])
plt.ylabel("Memory usage (GB)")
plt.title("Fig. 11(b) – Memory usage comparison")
plt.tight_layout()
plt.show()
