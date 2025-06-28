# AutoVAPT-R 🔍

AutoVAPT-R is an *automated Web Vulnerability Assessment and Penetration Testing (VAPT) toolkit* built using Python. It integrates powerful reconnaissance and scanning tools like *Nmap, WhatWeb, Nikto, Gobuster, and SQLMap* to streamline the VAPT process from start to finish.

---

## 🚀 Features

- 🔍 IP or URL input analysis
- 🌐 Nmap scan to identify open ports and services
- 🕸 WhatWeb for fingerprinting web technologies
- 🛡 Nikto for server misconfigurations and vulnerabilities
- 📂 Gobuster for brute-forcing hidden directories
- 🧠 SQLMap for intelligent SQL injection detection
- 📊 Clear, structured results with summaries

---

## 🛠 Tech Stack

- Python 3
- Linux CLI tools: nmap, nikto, gobuster, whatweb, sqlmap
- Standard Python libraries: subprocess, re, os, sys

---

## ⚙ Installation & Usage

1. **Clone the repository and navigate into it**
   ```bash
   git clone https://github.com/yathwxk/AutoVAPT-R.git
   cd AutoVAPT-R
   ```
2. **Install Python requirements**

```bash
pip install -r requirements.txt
```
3. **Run the scanner**
```bash
# For an IP target:
python app.py <target_ip_address>

# For a URL target:
python app.py http://example.com
```
## 📝 Project Highlights

✅ **Built with multiprocessing** to parallelize SQL injection checks for faster execution.

✅ **Combines directory brute-forcing** with hard-coded vulnerable endpoints.

✅ **Filters discovered paths** based on HTTP status codes for accuracy.

✅ **Displays detailed scan summaries** including total scans, vulnerabilities found, and safe entries.

---

## ⚠️ Disclaimer

🚨 **This toolkit is for educational and authorized security testing purposes only.**  
Never scan systems you do not own or have explicit permission to test. Unauthorized scanning may be illegal.

