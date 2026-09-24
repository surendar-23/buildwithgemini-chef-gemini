"""Independent Audit & Verification Script for Chef Gemini Studio."""

import ast
import time
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def audit_inventory_and_counts():
    tools_py = Path(__file__).parent.parent / "app" / "tools.py"
    with open(tools_py, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename="app/tools.py")
    
    func_defs = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    public_funcs = [f for f in func_defs if not f.startswith("_")]
    duplicates = [f for f in public_funcs if public_funcs.count(f) > 1]
    unique_funcs = set(public_funcs)
    
    from app.agent import root_agent
    registered_tools_count = len(root_agent.tools)
    
    return {
        "total_ast_functions": len(func_defs),
        "public_functions": len(public_funcs),
        "unique_public_functions": len(unique_funcs),
        "duplicate_names": list(set(duplicates)),
        "registered_root_agent_tools": registered_tools_count
    }

def audit_performance_benchmarks():
    t0 = time.perf_counter()
    import app.agent
    startup_time_ms = (time.perf_counter() - t0) * 1000
    
    from app.agent import root_agent
    total_docstring_bytes = sum(len(str(getattr(t, "__doc__", "") or "")) for t in root_agent.tools if hasattr(t, "__doc__"))
    estimated_tokens = total_docstring_bytes // 4
    
    return {
        "startup_time_ms": round(startup_time_ms, 2),
        "total_docstring_bytes": total_docstring_bytes,
        "estimated_tool_tokens": estimated_tokens
    }

def run_auditor_suite():
    inv = audit_inventory_and_counts()
    perf = audit_performance_benchmarks()
    
    report = {
        "inventory": inv,
        "performance": perf,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    
    out_path = Path(__file__).parent / "audit_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        
    return report

if __name__ == "__main__":
    rep = run_auditor_suite()
    print(json.dumps(rep, indent=2))
