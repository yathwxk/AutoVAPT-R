# banner.py

try:
    from pyfiglet import Figlet
except ImportError:
    print("pyfiglet is not installed. Run: pip install pyfiglet")
    exit(1)

def print_banner():
    figlet = Figlet(font='slant')  # Try also: 'standard', 'block', 'banner3-D'
    print(figlet.renderText('AutoVAPT-R'))
    print("=" * 70)
    print("     Automated Vulnerability Assessment & Penetration Testing Tool")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    print_banner()
