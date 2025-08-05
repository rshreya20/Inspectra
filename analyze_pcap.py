import subprocess
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

pcap_file = "suspicious_traffic.pcapng"

# Use tshark to extract HTTP request timestamps
cmd = [
    "tshark",
    "-r", pcap_file,
    "-Y", "http.request",
    "-T", "fields",
    "-e", "frame.time_epoch"
]

print("[*] Extracting timestamps...")
result = subprocess.run(cmd, capture_output=True, text=True)
lines = result.stdout.strip().split("\n")

# Convert timestamps to second-level buckets
traffic_per_second = defaultdict(int)

for line in lines:
    if not line.strip():
        continue
    timestamp = float(line.strip())
    second = int(timestamp)
    traffic_per_second[second] += 1

# Sort by time
sorted_times = sorted(traffic_per_second.keys())
counts = [traffic_per_second[t] for t in sorted_times]
labels = [datetime.fromtimestamp(t).strftime("%H:%M:%S") for t in sorted_times]

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(labels, counts, marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Time")
plt.ylabel("Number of HTTP Requests")
plt.title("HTTP Request Burst Pattern Over Time")
plt.tight_layout()
plt.grid(True)

# Save and show
plt.savefig("http_traffic_graph.png")
plt.show()

print("[+] Graph saved as http_traffic_graph.png")
