from dataclasses import asdict
import json

def event_record(event, signal: str, risk_reason: str) -> str:
    payload = {"event": asdict(event), "signal": signal, "risk_reason": risk_reason}
    return json.dumps(payload, sort_keys=True, default=str)
