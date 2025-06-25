# scanners/sqlmap_scan.py

import subprocess
from urllib.parse import urljoin
import re

# Predefined parameters to test
PARAMS = ["id=1", "user=admin", "page=1"]

def run_sqlmap(url, paths):
    results = []
    summary_lines = []
    vulnerable_count = 0
    total_scans = 0

    for path in paths:
        for param in PARAMS:
            total_scans += 1
            full_url = urljoin(url, path)
            target_url = f"{full_url}?{param}"

            try:
                cmd = [
                    "sqlmap", "-u", target_url, "--batch",
                    "--level", "1", "--risk", "1",
                    "--technique", "BEUSTQ", "--crawl=0"
                ]
                process = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = process.stdout

                # Remove ANSI escape sequences
                output_clean = re.sub(r'\x1B\[[0-9;]*[A-Za-z]', '', output)

                # Check vulnerability
                is_vulnerable = (
                    "is vulnerable" in output_clean.lower() or
                    ("parameter" in output_clean.lower() and "appears to be injectable" in output_clean.lower())
                )

                status = "VULNERABLE" if is_vulnerable else "Not Vulnerable"
                summary_lines.append(f"{path:<20} | {param:<15} | {status}")

                if is_vulnerable:
                    vulnerable_count += 1

                results.append({
                    "url": target_url,
                    "vulnerable": is_vulnerable
                })

            except subprocess.TimeoutExpired:
                summary_lines.append(f"{path:<20} | {param:<15} | Timed Out")
                results.append({
                    "url": target_url,
                    "vulnerable": False
                })
            except Exception as e:
                summary_lines.append(f"{path:<20} | {param:<15} | Error: {e}")
                results.append({
                    "url": target_url,
                    "vulnerable": False,
                    "error": str(e)
                })

    summary_text = (
        f"\n{'Directory':<20} | {'Parameter':<15} | Result\n"
        f"{'-'*55}\n" +
        "\n".join(summary_lines)
    )

    stats_summary = (
        f"\n\n=== SQLMap Scan Summary ===\n"
        f"Total Scans Run       : {total_scans}\n"
        f"Vulnerabilities Found : {vulnerable_count}\n"
        f"Safe Entries          : {total_scans - vulnerable_count}\n"
    )

    return {
        "tool": "SQLMap",
        "url": url,
        "output": summary_text + stats_summary,
        "results": results
    }
