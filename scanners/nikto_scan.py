# scanners/nikto_scan.py

import subprocess

def run_nikto(url):
    try:
        print(f"[+] Running Nikto on {url}")
        result = subprocess.run(["nikto", "-h", url], capture_output=True, text=True)
        return {
            "tool": "Nikto",
            "url": url,
            "output": result.stdout.strip()
        }
    except Exception as e:
        return {
            "tool": "Nikto",
            "error": str(e)
        }
