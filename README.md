# 🔎 Inspectra

 **A Wireshark-based tool for detecting suspicious network traffic patterns using packet analysis and Python visualization.**

Inspectra is a cybersecurity analysis project that captures, identifies, and visualizes suspicious traffic patterns using Wireshark and Python. It simulates both **normal** and **malicious** traffic to demonstrate anomaly detection techniques such as:

- Packet burst patterns
- Unusual URL parameters (e.g., `cmd=rm`)
- Repeated login attempts
- ICMP floods and HTTP request floods




## 🧪 Features

✅ Captures both **baseline traffic** (normal browsing, ping, curl) and **attack-like patterns**  
✅ Visualizes packet bursts using `matplotlib`  
✅ Filters traffic by protocol (HTTP, ICMP, TCP, etc.) using Wireshark  
✅ Detects:
- Login brute-force attempts
- Command injection via URL
- HTTP flooding (50+ GETs in 5s)
- Packet size anomalies



🔍 Tools Used
Wireshark – for capturing and filtering packets

TShark – for CLI-based packet parsing

Python – for scripting and plotting

Matplotlib – for traffic visualization




🧠 Learnings
Real-world usage of Wireshark filters

Recognizing anomaly patterns in network traffic

Visualizing raw .pcapng data using Python

Network behavior of ping floods, curl bursts, and injections

