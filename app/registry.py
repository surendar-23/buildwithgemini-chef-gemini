"""Hierarchical Domain Registry and Tool Routing System for Chef Gemini Studio."""

import inspect
from typing import Dict, List, Set, Any
from dataclasses import dataclass, field


@dataclass
class ToolMetadata:
    name: str
    domain: str
    subdomain: str
    risk_level: str  # "low", "medium", "high", "critical"
    is_deterministic: bool = True
    requires_external_service: bool = False
    is_state_mutating: bool = False
    description: str = ""


class ToolRegistry:
    """Central registry categorizing tools across 10 specialized culinary domains."""

    DOMAINS = {
        "CORE_PANTRY_GROCERY_MULTIMODAL": "Core recipes, pantry management, grocery maps, and media generation.",
        "PRESERVATION_FERMENTATION": "Koji, garum, lacto-fermentation, black garlic, and vinegar science.",
        "HYDROCOLLOIDS_CRYO_PHYSICS": "Spherification, transglutaminase, LN2 shatter, and rotovap distillation.",
        "ENOLOGY_SPIRITS_BEVERAGES": "Wine terroir, Champagne tirage, beer IBU, bourbon char, and carbonation.",
        "CONFECTIONERY_PASTRY": "Chocolate tempering, macaronage, croissant lamination, and sourdough kinetics.",
        "REGIONAL_HERITAGE": "Nixtamalization, tadka spice blooming, injera ersho, and ramen tare/dashi.",
        "CLINICAL_NUTRITION": "Ketogenic macros, FODMAP scanning, renal leaching, mTOR leucine, and IDDSI diets.",
        "SUSTAINABLE_BUTCHERY": "Ikejime harvesting, dry-aged beef, nose-to-tail, and spent grain flour.",
        "THERMAL_RHEOLOGY": "Thermal diffusivity, emulsion droplet size, Maillard kinetics, and fluid yield.",
        "FUTURE_FOOD_SCIENCE": "3D food printing, acoustic levitation, mycelium scaffolds, PEF, and HPP pasteurization.",
    }

    _registry: Dict[str, ToolMetadata] = {}
    _discovered: bool = False

    @classmethod
    def register_tool(cls, metadata: ToolMetadata):
        cls._registry[metadata.name] = metadata

    @classmethod
    def auto_discover(cls):
        """Auto-populates registry by discovering all functions defined in app.tools."""
        if cls._discovered:
            return
        try:
            import app.tools as tools_mod
            for name, func in inspect.getmembers(tools_mod, inspect.isfunction):
                if name not in cls._registry and not name.startswith("_"):
                    cls._registry[name] = ToolMetadata(
                        name=name,
                        domain="CORE_PANTRY_GROCERY_MULTIMODAL",
                        subdomain="general",
                        risk_level="low",
                        description=getattr(func, "__doc__", "") or ""
                    )
            cls._discovered = True
        except Exception:
            pass

    @classmethod
    def get_domain_tools(cls, domain: str) -> List[str]:
        cls.auto_discover()
        return [name for name, meta in cls._registry.items() if meta.domain == domain]

    @classmethod
    def get_tool_metadata(cls, name: str) -> ToolMetadata:
        cls.auto_discover()
        return cls._registry.get(name, ToolMetadata(name=name, domain="CORE_PANTRY_GROCERY_MULTIMODAL", subdomain="general", risk_level="low"))

    @classmethod
    def execute_tool(cls, tool_name: str, kwargs: Dict[str, Any]) -> str:
        """Dynamically invokes any registered culinary tool by name to optimize model schema payload."""
        import app.tools as tools_mod
        func = getattr(tools_mod, tool_name, None)
        if not func or not callable(func):
            return f"Error: Tool '{tool_name}' is not registered or callable."
        try:
            return str(func(**kwargs))
        except Exception as e:
            return f"Error executing tool '{tool_name}': {e}"
