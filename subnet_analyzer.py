import pandas as pd
import ipaddress

# Load the Excel file
df = pd.read_excel("ip_data.xlsx")

# Prepare empty lists to store calculated data
cidr_list = []
network_address_list = []
broadcast_address_list = []
usable_hosts_list = []

# Process each row
for i, row in df.iterrows():
    ip = row["IP Address"]
    mask = row["Subnet Mask"]
    
    # Create a network object using ipaddress
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    
    # Extract values
    cidr_list.append(network.with_prefixlen)
    network_address_list.append(str(network.network_address))
    broadcast_address_list.append(str(network.broadcast_address))
    usable_hosts_list.append(network.num_addresses - 2)

# Add results as new columns to the DataFrame
df["CIDR Notation"] = cidr_list
df["Network Address"] = network_address_list
df["Broadcast Address"] = broadcast_address_list
df["Usable Hosts"] = usable_hosts_list

# Save the results to a CSV file
df.to_csv("output/subnet_report.csv", index=False)
print("✅ subnet_report.csv created successfully.")

# Create a grouped summary for charting
grouped = df.groupby("CIDR Notation")["Usable Hosts"].sum().reset_index()
grouped.to_csv("output/grouped_hosts.csv", index=False)
print("✅ grouped_hosts.csv saved for visualization.")

