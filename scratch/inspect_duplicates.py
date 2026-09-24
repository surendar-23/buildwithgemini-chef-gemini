"""Inspect duplicates and line numbers in app/tools.py"""
import ast
from pathlib import Path

TOOLS_PY = Path("/config/Desktop/Session1/chef-gemini/app/tools.py")

with open(TOOLS_PY, "r") as f:
    source = f.read()

tree = ast.parse(source)

seen = {}
for node in tree.body:
    if isinstance(node, ast.FunctionDef):
        name = node.name
        if name in seen:
            print(f"Duplicate function '{name}': line {seen[name]} and line {node.lineno}")
        else:
            seen[name] = node.lineno
