from fastapi import APIRouter
from app.services.threat_intel.email_analyzer import analyze_email

router = APIRouter(prefix="/threat", tags=["Threat Intelligence"])


@router.post("/scan-email")
def scan_email(payload: dict):
    result = analyze_email(payload)
    return result
