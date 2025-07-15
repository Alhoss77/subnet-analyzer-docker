# Subnet Analysis Report

## 1. Which subnet has the most hosts?
The subnets with the most usable hosts are the ones using a /22 mask, which gives **1022 usable IPs**. These subnets in the dataset are:

- 192.168.100.0/22
- 10.2.0.0/22
- 172.16.48.0/22
- 10.20.4.0/22
- 192.168.20.0/22
- 10.3.0.0/22
- 172.16.60.0/22
- 10.15.4.0/22

Each of these subnets has **1022 usable IP addresses**.

---

## 2. Are there any overlapping subnets? If yes, which ones?
There are **no overlapping subnets** in this dataset. All subnets have **unique, non-overlapping address ranges**. Their network boundaries are distinct and do not intersect with one another.

---

## 3. What is the smallest and largest subnet in terms of address space?
- **Smallest subnets**:  
  All subnets with a **/24 mask**, each having **254 usable IPs**.  
  Examples:
  - 192.168.1.0/24
  - 192.168.2.0/24
  - 192.168.3.0/24
  - 10.0.3.0/24
  - 10.4.3.0/24
  - 10.50.2.0/24
  - 192.168.10.0/24
  - 172.16.20.0/24
  - 172.16.40.0/24
  - 192.168.4.0/24

- **Largest subnets**:  
  All subnets with a **/22 mask**, each having **1022 usable IPs**.  
  Examples:
  - 192.168.100.0/22
  - 10.2.0.0/22
  - 10.3.0.0/22
  - 10.15.4.0/22
  - 10.20.4.0/22
  - 172.16.48.0/22
  - 172.16.60.0/22
  - 192.168.20.0/22

---

## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network.
Many subnets in this network use large address blocks like `/22`, which provide **1022 usable IPs**. This is often unnecessary, especially for small device groups (e.g., printers, sensors, cameras).

To reduce wasted IPs:
- Use **/30 (2 usable IPs)** for point-to-point connections.
- Use **/29 (6 usable IPs)** or **/28 (14 usable IPs)** for small LANs or device clusters.
- Use **/27 or /26** when medium-sized groups are needed (30–62 IPs).

This approach would significantly reduce IP address waste and improve network efficiency.
