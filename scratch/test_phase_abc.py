"""Test suite for Phase ABC: Knowledge Graph, USDA/Places, and A2A Protocol Routing."""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.graph import CulinaryKnowledgeGraph
from app.external import USDAFoodDataClient, GooglePlacesClient
from app.a2a import A2ADomainRouter
from app.tools import (
    query_culinary_knowledge_graph,
    query_usda_micronutrients,
    search_nearby_culinary_groceries,
    route_a2a_domain_request,
)


def test_culinary_knowledge_graph_query():
    kg = CulinaryKnowledgeGraph()
    res = kg.query_subgraph("strawberry")
    assert res["found"] is True
    assert res["root_node"]["id"] == "ing_strawberry"
    assert len(res["connected_relationships"]) > 0


def test_usda_client():
    res = USDAFoodDataClient.search_food_nutrients("salmon")
    assert res["status"] == "success"
    assert "Protein" in res["nutrients"]


def test_google_places_client():
    res = GooglePlacesClient.search_nearby_markets("matcha", "San Francisco, CA")
    assert res["status"] == "success"
    assert len(res["markets_found"]) > 0


def test_a2a_domain_router():
    res = A2ADomainRouter.route_request("PASTRY", "calc_rheology", {"hydration": 0.65})
    assert res["status"] == "success"
    assert res["frame"]["recipient"] == "PastryAndRheologySpecialist"
    assert res["dispatch_status"] == "DELIVERED_TO_SPECIALIST"


def test_phase_abc_tools():
    out_kg = query_culinary_knowledge_graph("basil")
    assert "Query Culinary Knowledge Graph Analysis" in out_kg or "result" in out_kg.lower()

    out_usda = query_usda_micronutrients("chicken breast")
    assert "Query Usda Micronutrients Analysis" in out_usda or "nutrients" in out_usda.lower()

    out_places = search_nearby_culinary_groceries("nori")
    assert "Search Nearby Culinary Groceries Analysis" in out_places or "markets" in out_places.lower()

    out_a2a = route_a2a_domain_request("FERMENTATION", "check_koji", '{"temp": 30.0}')
    assert "Route A2A Domain Request Analysis" in out_a2a or "delivered" in out_a2a.lower()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
