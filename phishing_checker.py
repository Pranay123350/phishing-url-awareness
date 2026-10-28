import re
import ipaddress
from urllib.parse import urlparse

def is_phishing_url(url):
    reasons = []
    try:
        parsed = urlparse(url)
        host = parsed.netloc
        if host:
            ipaddress.ip_address(host.split(':')[0])
            reasons.append("URL contains IP address")
    except:
        pass
    if "@" in url:
        reasons.append("URL contains @ symbol")
    if url.count('.') > 5:
        reasons.append("Too many dots in URL")
    if len(url) > 75:
        reasons.append("URL is too long")
    if not url.startswith("https://"):
        reasons.append("Not using HTTPS")
    if reasons:
        return True, reasons
    return False, ["URL looks safe"]

if __name__ == "__main__":
    print("=== Phishing URL Awareness Checker ===")
    test_url = input("Enter URL to check: ")
    is_phish, reason_list = is_phishing_url(test_url)
    print("\nResult:")
    if is_phish:
        print(f"⚠️ SUSPICIOUS URL Detected!")
        for r in reason_list:
            print(f"- {r}")
    else:
        print(f"✅ Looks Safe: {reason_list[0]}")
