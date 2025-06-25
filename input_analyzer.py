# input_analyzer.py

import re

def analyze_input(target):
    if target.startswith("http"):
        return "url"
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    if re.match(ip_pattern, target):
        return "ip"
    return "invalid"
