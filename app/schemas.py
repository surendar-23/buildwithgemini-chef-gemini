"""Standardized Tool Result & Safety Contracts for Chef Gemini Studio."""

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional
import datetime


@dataclass
class SafetyWarning:
    category: str  # "food_safety", "clinical_nutrition", "equipment_hazard", "allergen"
    level: str  # "info", "warning", "critical"
    message: str
    regulatory_reference: Optional[str] = None


@dataclass
class ConfidenceInfo:
    level: str  # "high", "medium", "low"
    reason: str


@dataclass
class ProvenanceInfo:
    formula_id: Optional[str] = None
    data_source: Optional[str] = None
    calculated_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())


@dataclass
class ToolResult:
    status: str  # "success" or "error"
    tool: str
    result: Dict[str, Any]
    units: Dict[str, str] = field(default_factory=dict)
    assumptions: List[str] = field(default_factory=list)
    warnings: List[SafetyWarning] = field(default_factory=list)
    confidence: Optional[ConfidenceInfo] = None
    provenance: Optional[ProvenanceInfo] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def format_output(self) -> str:
        """Formats the result as a rich, human-friendly Markdown string while maintaining structured data."""
        lines = []
        if self.status == "error":
            lines.append(f"❌ **Error in {self.tool}**:")
            err_msg = self.result.get("message", "An unexpected error occurred.")
            lines.append(f"> {err_msg}")
        else:
            lines.append(f"🟢 **{self.tool.replace('_', ' ').title()} Analysis**:")
            for k, v in self.result.items():
                unit = f" {self.units.get(k, '')}".rstrip()
                lines.append(f"- **{k.replace('_', ' ').title()}**: **{v}**{unit}")
        
        if self.assumptions:
            lines.append("\n📌 **Assumptions**:")
            for a in self.assumptions:
                lines.append(f"- {a}")
                
        if self.warnings:
            lines.append("\n⚠️ **Safety & Health Notes**:")
            for w in self.warnings:
                icon = "🚨" if w.level == "critical" else "⚠️"
                ref = f" *(Ref: {w.regulatory_reference})*" if w.regulatory_reference else ""
                lines.append(f"- {icon} **[{w.category.upper()}]**: {w.message}{ref}")
                
        if self.provenance and self.provenance.formula_id:
            lines.append(f"\n🔬 *Formula Reference: {self.provenance.formula_id}*")
            
        return "\n".join(lines)
