"""Aroma Compound Volatile Flavor Pairing Engine for Chef Gemini Studio."""

from typing import Dict, List, Set, Any
from dataclasses import dataclass, field


@dataclass
class VolatileCompound:
    name: str
    chemical_class: str
    aroma_descriptor: str
    threshold_ppm: float


@dataclass
class FlavorProfile:
    ingredient: str
    primary_compounds: Set[str]
    category: str


class AromaPairingEngine:
    """Calculates chemical flavor synergy based on shared volatile aroma compounds."""

    # Built-in volatile database for key ingredients
    COMPOUND_DATABASE: Dict[str, Set[str]] = {
        "chocolate": {"vanillin", "pyrazines", "phenylethanol", "linalool", "isovaleraldehyde"},
        "strawberry": {"furaneol", "linalool", "ethyl_butyrate", "cis_3_hexenol"},
        "coffee": {"2_furfurylthiol", "pyrazines", "guaiacol", "methional", "diacetyl"},
        "vanilla": {"vanillin", "4_hydroxybenzaldehyde", "guaiacol", "eugenol"},
        "basil": {"linalool", "eugenol", "estragole", "1_8_cineole"},
        "tomato": {"cis_3_hexenol", "beta_damascenone", "methional", "2_isobutylthiazole"},
        "salmon": {"1_octen_3_ol", "hexanal", "trimethylamine", "beta_ionone"},
        "blue_cheese": {"2_heptanone", "2_nonanone", "butyric_acid", "methyl_ketones"},
        "pork": {"hexanal", "methional", "pyrazines", "2_methyl_3_furanthiol"},
        "apple": {"ethyl_2_methylbutyrate", "hexanal", "trans_2_hexenal", "damascenone"},
    }

    @classmethod
    def calculate_compatibility(cls, ingredient_a: str, ingredient_b: str) -> Dict[str, Any]:
        ing_a = ingredient_a.lower().strip()
        ing_b = ingredient_b.lower().strip()

        compounds_a = cls.COMPOUND_DATABASE.get(ing_a, {"linalool", "pyrazines"})
        compounds_b = cls.COMPOUND_DATABASE.get(ing_b, {"eugenol", "pyrazines"})

        shared = compounds_a.intersection(compounds_b)
        union = compounds_a.union(compounds_b)

        jaccard_index = len(shared) / len(union) if union else 0.0
        synergy_score = round(jaccard_index * 100, 1)

        pairing_strength = (
            "EXCEPTIONAL_SYNERGY" if synergy_score >= 25.0
            else "HIGH_COMPATIBILITY" if synergy_score >= 15.0
            else "MODERATE_COMPATIBILITY" if synergy_score >= 5.0
            else "NOVEL_CONTRAST"
        )

        return {
            "ingredient_a": ingredient_a,
            "ingredient_b": ingredient_b,
            "synergy_score": synergy_score,
            "pairing_strength": pairing_strength,
            "shared_aroma_compounds": list(shared),
            "total_aroma_compounds_analyzed": len(union),
            "recommendation": (
                f"Combining {ingredient_a} and {ingredient_b} leverages shared aroma volatiles "
                f"({', '.join(shared) if shared else 'contrast notes'}), producing harmonized sensory perception."
            )
        }
