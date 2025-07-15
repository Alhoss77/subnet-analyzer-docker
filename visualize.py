import pandas as pd
import matplotlib.pyplot as plt

# Load the grouped data from the CSV file
df = pd.read_csv("output/grouped_hosts.csv")

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(df["CIDR Notation"], df["Usable Hosts"], color="steelblue")
plt.xlabel("Subnet (CIDR Notation)")
plt.ylabel("Total Usable Hosts")
plt.title("Number of Usable Hosts per Subnet")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/network_plot.png")
print("✅ Bar chart saved to output/network_plot.png")
