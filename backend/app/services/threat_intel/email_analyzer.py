from app.services.threat_intel.risk_engine import RiskEngine


def analyze_email(payload: dict):
    """
    This acts as the orchestrator.

    Later this is where we will plug:

    ✅ VirusTotal
    ✅ Google Safe Browsing
    ✅ Attachment scanning
    ✅ SPF/DKIM checks
    ✅ ML model

    RiskEngine remains the core scorer.
    """

    subject = payload.get("subject", "")
    body = payload.get("body", "")

    result = RiskEngine.calculate_risk(subject, body)

    return result
