# scanners/whatweb_scan.py

import subprocess

def run_whatweb(url):
    try:
        print(f"[+] Running WhatWeb on {url}")
        result = subprocess.run(["whatweb", url], capture_output=True, text=True)
        return {
            "tool": "WhatWeb",
            "url": url,
            "output": result.stdout.strip()
        }
    except Exception as e:
        return {
            "tool": "WhatWeb",
            "error": str(e)
        }
