"""HACCP Automated Compliance and Critical Control Point Logging Engine."""

from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CriticalControlPoint:
    ccp_id: str
    process_step: str
    hazard_description: str
    critical_limit: str
    monitoring_procedure: str
    corrective_action: str


class HACCPEngine:
    """Provides regulatory HACCP hazard analysis and critical control point verification."""

    @staticmethod
    def analyze_process_hazard(
        process_type: str,
        target_temperature_c: float,
        holding_time_minutes: float
    ) -> Dict[str, Any]:
        p_type = process_type.lower().strip()
        
        # Hazard evaluation
        if "sous_vide" in p_type or "cook" in p_type:
            ccp_name = "CCP-1: Thermal Microbial Reduction"
            safe_temp_min = 55.0
            safe_time_min = 30.0 if target_temperature_c >= 60.0 else 120.0
            hazard = "Survival of vegetative pathogens (Salmonella, Listeria monocytogenes, E. coli)"
            ref = "FDA Food Code 3-401.11 / USDA FSIS 6D Salmonella Guidelines"
        elif "cooling" in p_type or "chill" in p_type:
            ccp_name = "CCP-2: Rapid Blast Chilling"
            safe_temp_min = 5.0
            safe_time_min = 360.0  # 6 hours total cooling
            hazard = "Germination of spore-forming pathogens (Clostridium perfringens, Bacillus cereus)"
            ref = "FDA Food Code 3-501.14"
        else:
            ccp_name = "CCP-3: Cold Holding Maintenance"
            safe_temp_min = 4.1
            safe_time_min = 0.0
            hazard = "Listeria monocytogenes proliferation during cold storage"
            ref = "FDA Food Code 3-501.16"

        is_compliant = target_temperature_c >= safe_temp_min and holding_time_minutes >= safe_time_min

        status = "COMPLIANT" if is_compliant else "CRITICAL_DEVIATION_DETECTED"
        corrective_action = (
            "Continue standard process monitoring." if is_compliant
            else f"CRITICAL ACTION REQUIRED: Immediately adjust temperature to >={safe_temp_min}°C or extend time to {safe_time_min} mins. Do not serve product until verified."
        )

        return {
            "ccp_id": ccp_name,
            "status": status,
            "hazard_analyzed": hazard,
            "monitored_temperature_c": target_temperature_c,
            "monitored_holding_time_mins": holding_time_minutes,
            "required_safe_temp_c": safe_temp_min,
            "regulatory_reference": ref,
            "corrective_action_workflow": corrective_action
        }
