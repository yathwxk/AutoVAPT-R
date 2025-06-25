# scanners/nmap_scan.py

import subprocess
import re

def run_nmap(ip):
    print(f"[+] Running Nmap on {ip}...\n")

    try:
        result = subprocess.run(
            ["nmap", "-sV", "-T4", "--open", ip],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout

        # Parse and format
        open_ports, pretty = extract_ports_and_format(output)
        return {
            "open_ports": open_ports,  # For logic
            "display": pretty          # For output display
        }

    except subprocess.CalledProcessError as e:
        return {
            "open_ports": [],
            "display": f"[!] Nmap scan failed:\n{e.output}"
        }

def extract_ports_and_format(output):
    open_ports = []
    pretty_lines = []
    in_ports_section = False

    for line in output.splitlines():
        if line.strip().startswith("PORT"):
            in_ports_section = True
            pretty_lines.append(line)
            continue
        if in_ports_section:
            if line.strip() == "" or line.startswith("Nmap done"):
                break
            pretty_lines.append(line)

            # Extract port number using regex
            match = re.match(r"(\d+)/tcp\s+open", line)
            if match:
                open_ports.append(int(match.group(1)))

    return open_ports, "\n".join(pretty_lines) if pretty_lines else "[!] No open ports found."
