"""
Phishing Email Identifier
Version: 2.0
Purpose: Educational, rule-based email risk assessment.

This program analyzes user-provided email text locally.
It does not open URLs or guarantee that an email is safe.
"""

import re
from urllib.parse import urlparse


APP_NAME = "PHISHING EMAIL IDENTIFIER"
VERSION = "2.0"

# Each matching rule contributes to a heuristic score.
# The score is an indicator, not a probability of phishing.
DETECTION_RULES = [
    {
        "name": "Urgent language",
        "phrases": [
            "act now",
            "immediate action",
            "account suspended",
            "account will be closed",
            "verify your account",
            "urgent action required",
            "within 24 hours",
        ],
        "points": 15,
    },
    {
        "name": "Sensitive-information request",
        "phrases": [
            "password",
            "one-time password",
            "otp",
            "bank details",
            "credit card",
            "login credentials",
            "security code",
        ],
        "points": 15,
    },
    {
        "name": "Unexpected reward",
        "phrases": [
            "you have won",
            "claim your prize",
            "free gift",
            "lottery winner",
            "you are the winner",
        ],
        "points": 10,
    },
]

SHORTENED_DOMAINS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "ow.ly",
}

URL_PATTERN = re.compile(
    r"https?://[^\s<>\"']+|www\.[^\s<>\"']+",
    re.IGNORECASE,
)

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def extract_urls(text):
    """Extract URL-like strings from text."""
    return [
        match.rstrip(".,!?;:)]}")
        for match in URL_PATTERN.findall(text)
    ]


def analyze_url(url):
    """Identify selected warning signs in a URL."""
    findings = []
    candidate = url.strip().rstrip(".,!?;:)]}")

    if candidate.lower().startswith("www."):
        candidate = "http://" + candidate

    try:
        parsed = urlparse(candidate)
        hostname = parsed.hostname

        if parsed.scheme not in {"http", "https"}:
            findings.append("Unexpected or missing URL scheme")

        if not hostname:
            return ["URL has an invalid or missing hostname"]

        hostname = hostname.lower().rstrip(".")

        if parsed.scheme == "http":
            findings.append("URL uses unencrypted HTTP")

        if hostname in SHORTENED_DOMAINS:
            findings.append("URL uses a link-shortening service")

        if "@" in parsed.netloc:
            findings.append("URL contains an @ symbol in its address")

        if hostname.startswith("xn--") or ".xn--" in hostname:
            findings.append(
                "URL contains an internationalized domain pattern"
            )

        # Check IPv4-style addresses without making network requests.
        ip_pattern = r"\d{1,3}(?:\.\d{1,3}){3}"
        if re.fullmatch(ip_pattern, hostname):
            findings.append(
                "URL uses an IP address instead of a domain name"
            )

    except (ValueError, UnicodeError):
        findings.append("URL could not be parsed")

    return findings


def analyze_email(sender, subject, body):
    """
    Analyze an email and return a structured risk assessment.

    Risk levels:
        LOW:    score below 30
        MEDIUM: score from 30 through 59
        HIGH:   score 60 or higher
    """
    findings = []
    score = 0

    sender = sender.strip()
    subject = subject.strip()
    body = body.strip()
    combined_text = f"{subject}\n{body}".casefold()

    # Validate basic sender-address format.
    if not EMAIL_PATTERN.fullmatch(sender):
        findings.append({
            "category": "Sender",
            "message": "Sender address has an unusual or invalid format",
            "points": 10,
        })
        score += 10

    # Check each configured phrase once per rule.
    for rule in DETECTION_RULES:
        matched_phrases = [
            phrase
            for phrase in rule["phrases"]
            if phrase in combined_text
        ]

        if matched_phrases:
            findings.append({
                "category": rule["name"],
                "message": (
                    "Matched phrase(s): "
                    + ", ".join(f"'{phrase}'" for phrase in matched_phrases)
                ),
                "points": rule["points"],
            })
            score += rule["points"]

    # Inspect each distinct URL only once.
    urls = list(dict.fromkeys(extract_urls(body)))

    for url in urls:
        for warning in analyze_url(url):
            findings.append({
                "category": "URL",
                "message": f"{url} — {warning}",
                "points": 15,
            })
            score += 15

    score = min(score, 100)

    if score >= 60:
        risk = "HIGH"
        recommendation = (
            "Treat this email as suspicious. Do not click its links "
            "or provide sensitive information. Verify the request "
            "through an independently obtained trusted contact method."
        )
    elif score >= 30:
        risk = "MEDIUM"
        recommendation = (
            "Review the warning signs carefully. Verify the sender "
            "and request through a trusted, independent channel."
        )
    else:
        risk = "LOW"
        recommendation = (
            "Few configured warning signs were detected. This does "
            "not establish that the email is safe. Stay cautious with "
            "unexpected links, attachments, and requests."
        )

    if not findings:
        findings.append({
            "category": "General",
            "message": "No configured warning signs were detected",
            "points": 0,
        })

    return {
        "score": score,
        "risk": risk,
        "findings": findings,
        "recommendation": recommendation,
        "urls_found": urls,
    }


def print_report(result):
    """Display a readable analysis report."""
    line = "=" * 60

    print(f"\n{line}")
    print(f"{APP_NAME}  |  v{VERSION}")
    print(line)
    print(f"Risk level       : {result['risk']}")
    print(f"Heuristic score  : {result['score']}/100")

    print("\nDETECTED INDICATORS")
    print("-" * 60)

    for number, finding in enumerate(result["findings"], start=1):
        print(f"{number}. [{finding['category']}] {finding['message']}")

    if result["urls_found"]:
        print("\nURLS FOUND")
        print("-" * 60)
        for url in result["urls_found"]:
            print(f"- {url}")

    print("\nRECOMMENDATION")
    print("-" * 60)
    print(result["recommendation"])

    print("\nLIMITATION")
    print("-" * 60)
    print(
        "This educational tool uses simple rules. Results can contain "
        "false positives or miss phishing attempts."
    )
    print(line)


def main():
    """Collect sample email details and run the analysis."""
    print("=" * 60)
    print(f"{APP_NAME}  |  v{VERSION}")
    print("Local, rule-based email analysis")
    print("=" * 60)
    print("Use fictional examples. Do not enter private email content.\n")

    try:
        sender = input("Sender email address: ").strip()
        subject = input("Email subject: ").strip()

        print(
            "\nEnter the email body one line at a time. "
            "Press Enter on an empty line to finish."
        )

        body_lines = []

        while True:
            line = input()
            if not line:
                break
            body_lines.append(line)

        result = analyze_email(sender, subject, "\n".join(body_lines))
        print_report(result)

    except (KeyboardInterrupt, EOFError):
        print("\nAnalysis cancelled.")


if __name__ == "__main__":
    main()