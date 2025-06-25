# app.py

from input_analyzer import analyze_input
from scanners.nmap_scan import run_nmap
from scanners.whatweb_scan import run_whatweb
from scanners.nikto_scan import run_nikto
from scanners.gobuster_scan import run_gobuster
from scanners.sqlmap_scan import run_sqlmap
from utils.banner import print_banner

import sys
from multiprocessing import Pool

def generate_web_urls(ip, open_ports):
    urls = []
    for port in open_ports:
        if port in [80, 8080]:
            urls.append(f"http://{ip}:{port}")
        elif port == 443:
            urls.append(f"https://{ip}")
    return urls

def sqlmap_wrapper(args):
    url, paths = args
    return run_sqlmap(url, paths)

def main():
    print_banner()
    if len(sys.argv) != 2:
        print("Usage: python app.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    input_type = analyze_input(target)
    print(f"[DEBUG] Target input type detected as: {input_type}")

    results = []

    if input_type == "ip":
        nmap_result = run_nmap(target)
        results.append({
            "tool": "nmap",
            "url": target,
            "output": nmap_result["display"]
        })

        print(f"[DEBUG] Open ports found: {nmap_result['open_ports']}")
        web_urls = generate_web_urls(target, nmap_result["open_ports"])
        print(f"[DEBUG] Web URLs to scan: {web_urls}")

    elif input_type == "url":
        web_urls = [target]
        print(f"[+] Detected target as URL")

    else:
        print("[-] Invalid target format.")
        sys.exit(1)

    gobuster_paths = ["/index", "/index.php", "/login", "/phpMyAdmin", "/test"]

    for url in web_urls:
        results.append(run_whatweb(url))
        results.append(run_nikto(url))
        gobuster_result = run_gobuster(url)
        results.append(gobuster_result)

        print("[+] Running SQLMap scan on discovered web paths")
        with Pool() as pool:
            sqlmap_results = pool.map(sqlmap_wrapper, [(url, gobuster_paths)])
        results.extend(sqlmap_results)

    print("\n\n=== Final VAPT Summary ===")
    for result in results:
        print(f"\n[+] {result['tool']} Result for {result.get('url', target)}:")
        if "error" in result:
            print(f"[-] Error: {result['error']}")
        elif "output" in result:
            print(result["output"])

if __name__ == "__main__":
    main()
