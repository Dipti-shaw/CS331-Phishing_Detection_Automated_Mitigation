import re
from typing import List, Dict


class RiskEngine:

    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        Extract URLs using regex
        """
        url_pattern = r'https?://[^\s]+'
        return re.findall(url_pattern, text)

    @staticmethod
    def calculate_risk(subject: str, body: str) -> Dict:

        score = 0
        reasons = []

        full_text = f"{subject} {body}".lower()

        ###################################################
        # 1. PHISHING KEYWORD DETECTION
        ###################################################

        phishing_keywords = [
            "urgent",
            "immediately",
            "verify",
            "suspended",
            "click below",
            "reset",
            "password",
            "login",
            "confirm",
            "bank",
            "security alert",
            "unauthorized",
            "limited time"
        ]

        keyword_hits = [word for word in phishing_keywords if word in full_text]

        if keyword_hits:
            score += len(keyword_hits) * 8
            reasons.append(f"Phishing keywords detected: {keyword_hits}")

        ###################################################
        # 2. URL DETECTION
        ###################################################

        urls = RiskEngine.extract_urls(full_text)

        if urls:
            score += 15
            reasons.append("Email contains URLs")

        ###################################################
        # 3. SUSPICIOUS DOMAIN PATTERNS
        ###################################################

        suspicious_domain_words = [
            "login",
            "secure",
            "verify",
            "account",
            "update",
            "banking",
            "security"
        ]

        for url in urls:
            for pattern in suspicious_domain_words:
                if pattern in url:
                    score += 12
                    reasons.append(f"Suspicious domain pattern '{pattern}' in {url}")
                    break

        ###################################################
        # 4. FAKE / RARE TLD DETECTION
        ###################################################

        suspicious_tlds = [
            ".ru", ".tk", ".xyz", ".cn", ".top", ".gq"
        ]

        for url in urls:
            if any(tld in url for tld in suspicious_tlds):
                score += 20
                reasons.append(f"Suspicious TLD detected in {url}")

        ###################################################
        # 5. TOO MANY LINKS (Classic phishing trick)
        ###################################################

        if len(urls) > 3:
            score += 25
            reasons.append("Email contains multiple links")

        ###################################################
        # 6. URGENCY DETECTION
        ###################################################

        urgency_words = [
            "act now",
            "urgent",
            "immediate",
            "expires today",
            "final warning"
        ]

        if any(word in full_text for word in urgency_words):
            score += 10
            reasons.append("Urgency language detected")

        ###################################################
        # 7. MESSAGE LENGTH TRICK
        ###################################################

        if len(body) < 40:
            score += 10
            reasons.append("Very short email body (common phishing pattern)")

        ###################################################
        # FINAL VERDICT ENGINE
        ###################################################

        if score >= 70:
            verdict = "PHISHING"
            severity = "HIGH"

        elif score >= 40:
            verdict = "SUSPICIOUS"
            severity = "MEDIUM"

        else:
            verdict = "SAFE"
            severity = "LOW"

        return {
            "risk_score": score,
            "verdict": verdict,
            "severity": severity,
            "urls_detected": urls,
            "analysis": reasons
        }
