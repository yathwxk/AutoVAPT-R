
import subprocess

def run_gobuster(url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    try:
        print(f"[+] Running Gobuster on {url}")
        result = subprocess.run([
            "gobuster", "dir",
            "-u", url,
            "-w", wordlist,
            "-q"
        ], capture_output=True, text=True)

        paths = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        formatted_paths = "\n".join(["    " + path for path in paths])

        return {
            "tool": "Gobuster",
            "url": url,
            "paths": paths,
            "output": f"[+] Found Paths:\n{formatted_paths}"
        }
    except Exception as e:
        return {
            "tool": "Gobuster",
            "url": url,
            "error": str(e)
        }