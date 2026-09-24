"""Comprehensive audit script for Chef Gemini Studio codebase."""

import ast
import inspect
import importlib.util
from pathlib import Path
import json

TOOLS_PY = Path("/config/Desktop/Session1/chef-gemini/app/tools.py")
AGENT_PY = Path("/config/Desktop/Session1/chef-gemini/app/agent.py")

def audit_tools_py():
    with open(TOOLS_PY, "r") as f:
        source = f.read()

    tree = ast.parse(source, filename=str(TOOLS_PY))
    
    functions = []
    func_names_seen = set()
    duplicates = []
    
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            fn_name = node.name
            if fn_name in func_names_seen:
                duplicates.append(fn_name)
            func_names_seen.add(fn_name)
            
            # Check args
            args = [arg.arg for arg in node.args.args]
            type_hints = [arg.annotation is not None for arg in node.args.args]
            has_return_hint = node.returns is not None
            has_docstring = ast.get_docstring(node) is not None
            
            functions.append({
                "name": fn_name,
                "line": node.lineno,
                "args": args,
                "all_args_typed": all(type_hints) if type_hints else True,
                "has_return_hint": has_return_hint,
                "has_docstring": has_docstring,
            })
            
    return functions, duplicates, source

def audit_agent_py(tools_in_py):
    with open(AGENT_PY, "r") as f:
        source = f.read()
        
    tree = ast.parse(source, filename=str(AGENT_PY))
    
    imports_from_tools = []
    registered_tools = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module in ("app.tools", "tools"):
            for alias in node.names:
                imports_from_tools.append(alias.name)
                
    # Search for tools=[...] inside Agent(...)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if (isinstance(func, ast.Name) and func.id == "Agent") or (isinstance(func, ast.Attribute) and func.attr == "Agent"):
                for kw in node.keywords:
                    if kw.arg == "tools" and isinstance(kw.value, ast.List):
                        for el in kw.value.elts:
                            if isinstance(el, ast.Name):
                                registered_tools.append(el.id)
                            elif isinstance(el, ast.Call) and isinstance(el.func, ast.Name):
                                registered_tools.append(el.func.id)

    tools_py_names = set(f["name"] for f in tools_in_py)
    imported_set = set(imports_from_tools)
    registered_set = set(registered_tools)
    
    unimported = tools_py_names - imported_set
    unregistered = imported_set - registered_set
    missing_in_py = registered_set - tools_py_names - {"PreloadMemoryTool"}
    
    return {
        "imported_count": len(imports_from_tools),
        "registered_count": len(registered_tools),
        "unimported": list(unimported),
        "unregistered": list(unregistered),
        "missing_in_py": list(missing_in_py),
    }

if __name__ == "__main__":
    functions, duplicates, source = audit_tools_py()
    agent_audit = audit_agent_py(functions)
    
    print("=== AUDIT SUMMARY ===")
    print(f"Total function definitions in app/tools.py: {len(functions)}")
    print(f"Duplicate/overwritten function names in app/tools.py: {duplicates}")
    print(f"Total tools imported in app/agent.py: {agent_audit['imported_count']}")
    print(f"Total tools registered in root_agent: {agent_audit['registered_count']}")
    print(f"Unimported tools: {agent_audit['unimported']}")
    print(f"Unregistered tools: {agent_audit['unregistered']}")
    print(f"Missing functions in app/tools.py: {agent_audit['missing_in_py']}")
    
    untyped = [f["name"] for f in functions if not f["all_args_typed"]]
    no_doc = [f["name"] for f in functions if not f["has_docstring"]]
    no_ret = [f["name"] for f in functions if not f["has_return_hint"]]
    
    print(f"\nUntyped arg functions ({len(untyped)}): {untyped[:5]}...")
    print(f"Missing docstring functions ({len(no_doc)}): {no_doc[:5]}...")
    print(f"Missing return type hint functions ({len(no_ret)}): {no_ret[:5]}...")
