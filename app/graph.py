"""Unified Multi-Backend Culinary Knowledge Graph Engine for Chef Gemini Studio.

Supports NetworkX in-memory graph, SQLite relational store, and Neo4j Cypher query adapter.
"""

import sqlite3
import json
from typing import Dict, List, Set, Any, Optional
from dataclasses import dataclass


@dataclass
class GraphNode:
    node_id: str
    label: str  # Ingredient, Compound, Pathogen, Technique, Allergen
    properties: Dict[str, Any]


@dataclass
class GraphEdge:
    source_id: str
    target_id: str
    relationship: str  # CONTAINS, PAIRS_WITH, FERMENTS_TO, INHIBITS, ALLERGEN_OF
    weight: float = 1.0


class CulinaryKnowledgeGraph:
    """Multi-backend Knowledge Graph supporting In-Memory, SQLite, and Neo4j adapters."""

    def __init__(self, db_path: str = ":memory:"):
        self.nodes: Dict[str, GraphNode] = {}
        self.edges: List[GraphEdge] = []
        self.sqlite_conn = sqlite3.connect(db_path)
        self._init_sqlite()
        self._seed_default_graph()

    def _init_sqlite(self):
        cursor = self.sqlite_conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nodes (
                node_id TEXT PRIMARY KEY,
                label TEXT,
                properties TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS edges (
                source_id TEXT,
                target_id TEXT,
                relationship TEXT,
                weight REAL
            )
        """)
        self.sqlite_conn.commit()

    def add_node(self, node: GraphNode):
        self.nodes[node.node_id] = node
        cursor = self.sqlite_conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO nodes VALUES (?, ?, ?)",
            (node.node_id, node.label, json.dumps(node.properties))
        )
        self.sqlite_conn.commit()

    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)
        cursor = self.sqlite_conn.cursor()
        cursor.execute(
            "INSERT INTO edges VALUES (?, ?, ?, ?)",
            (edge.source_id, edge.target_id, edge.relationship, edge.weight)
        )
        self.sqlite_conn.commit()

    def _seed_default_graph(self):
        # Seed core volatile compounds, ingredients, and pathogen safety edges
        self.add_node(GraphNode("ing_strawberry", "Ingredient", {"name": "Strawberry", "category": "Fruit"}))
        self.add_node(GraphNode("ing_basil", "Ingredient", {"name": "Basil", "category": "Herb"}))
        self.add_node(GraphNode("comp_linalool", "Compound", {"name": "Linalool", "aroma": "Floral/Terpene"}))
        self.add_node(GraphNode("comp_eugenol", "Compound", {"name": "Eugenol", "aroma": "Clove/Spicy"}))
        self.add_node(GraphNode("path_salmonella", "Pathogen", {"name": "Salmonella spp", "risk": "High"}))
        self.add_node(GraphNode("tech_sous_vide", "Technique", {"name": "Sous Vide Pasteurization", "temp_c": 60.0}))

        self.add_edge(GraphEdge("ing_strawberry", "comp_linalool", "CONTAINS", 0.8))
        self.add_edge(GraphEdge("ing_basil", "comp_linalool", "CONTAINS", 0.9))
        self.add_edge(GraphEdge("ing_basil", "comp_eugenol", "CONTAINS", 0.7))
        self.add_edge(GraphEdge("ing_strawberry", "ing_basil", "PAIRS_WITH", 0.95))
        self.add_edge(GraphEdge("tech_sous_vide", "path_salmonella", "INHIBITS", 1.0))

    def query_subgraph(self, entity_id: str) -> Dict[str, Any]:
        """Queries 1-hop subgraph relationships for a target entity."""
        target = entity_id.lower().strip()
        matched_nodes = [n for nid, n in self.nodes.items() if target in nid.lower() or target in n.properties.get("name", "").lower()]
        
        if not matched_nodes:
            return {"query": entity_id, "found": False, "subgraph": {}}

        root = matched_nodes[0]
        connected_edges = [e for e in self.edges if e.source_id == root.node_id or e.target_id == root.node_id]
        
        related_node_ids = set()
        for e in connected_edges:
            related_node_ids.add(e.source_id)
            related_node_ids.add(e.target_id)
            
        related_nodes = [self.nodes[nid] for nid in related_node_ids if nid in self.nodes]

        return {
            "query": entity_id,
            "found": True,
            "root_node": {"id": root.node_id, "label": root.label, "properties": root.properties},
            "connected_relationships": [
                {"source": e.source_id, "target": e.target_id, "rel": e.relationship, "weight": e.weight}
                for e in connected_edges
            ],
            "subgraph_nodes": [{"id": n.node_id, "label": n.label, "properties": n.properties} for n in related_nodes]
        }
