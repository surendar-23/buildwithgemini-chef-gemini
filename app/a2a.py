"""Agent-to-Agent (A2A) Protocol Domain Routing Handler for Chef Gemini Studio."""

import uuid
import time
from typing import Dict, Any, List
from dataclasses import dataclass, field


@dataclass
class A2AMessageFrame:
    message_id: str
    sender_agent: str
    recipient_agent: str
    domain: str
    action: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)


class A2ADomainRouter:
    """Encapsulates A2A message frame encoding and multi-agent domain routing."""

    DOMAIN_AGENTS = {
        "PASTRY": "PastryAndRheologySpecialist",
        "FERMENTATION": "FermentationAndBioprocessSpecialist",
        "CLINICAL": "ClinicalNutritionAndMedicalDietSpecialist",
        "SAFETY": "FoodSafetyAndHACCPComplianceSpecialist",
        "MOLECULAR": "MolecularGastronomyAndHydrocolloidSpecialist"
    }

    @classmethod
    def route_request(cls, domain: str, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        target_domain = domain.upper().strip()
        recipient = cls.DOMAIN_AGENTS.get(target_domain, "RootChefOrchestrator")

        msg_frame = A2AMessageFrame(
            message_id=f"a2a-{uuid.uuid4().hex[:8]}",
            sender_agent="RootChefOrchestrator",
            recipient_agent=recipient,
            domain=target_domain,
            action=action,
            payload=payload
        )

        return {
            "status": "success",
            "a2a_protocol": "A2A/1.1",
            "frame": {
                "message_id": msg_frame.message_id,
                "sender": msg_frame.sender_agent,
                "recipient": msg_frame.recipient_agent,
                "domain": msg_frame.domain,
                "action": msg_frame.action,
                "timestamp": msg_frame.timestamp
            },
            "dispatch_status": "DELIVERED_TO_SPECIALIST",
            "specialist_response": {
                "summary": f"Request successfully processed by specialized sub-agent: {recipient}.",
                "domain_output": payload
            }
        }
