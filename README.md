# Subnet Analyzer & Visualizer 🐳

This project reads a list of IP addresses and subnet masks from an Excel file (`ip_data.xlsx`), calculates subnet information including:

- CIDR Notation
- Network Address
- Broadcast Address
- Usable Hosts

It then groups the results by subnet and generates:

- 📄 A full analysis report: `subnet_report.csv`
- 📄 A grouped summary: `grouped_hosts.csv`
- 📊 A bar chart: `network_plot.png`

---

## 📦 Requirements

- Docker Desktop (for containerized use)
- Python 3 (for optional local use)

---

## 🐳 How to Run with Docker (Recommended)

### Step 1: Build the Docker Image

In your terminal, from the project folder:

```bash
docker build -t subnet-analyzer .
