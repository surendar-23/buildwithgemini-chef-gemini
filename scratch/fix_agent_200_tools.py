"""Script to parse all tool functions from app/tools.py and update app/agent.py."""

import inspect
import importlib.util
from pathlib import Path

TOOLS_PY = Path("/config/Desktop/Session1/chef-gemini/app/tools.py")
AGENT_PY = Path("/config/Desktop/Session1/chef-gemini/app/agent.py")

# Import app.tools dynamically
spec = importlib.util.spec_from_file_location("app.tools", str(TOOLS_PY))
tools_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools_mod)

tool_names = [
    name for name, obj in inspect.getmembers(tools_mod, inspect.isfunction)
    if obj.__module__ == "app.tools" and not name.startswith("_")
]

tool_names.sort()

print(f"Discovered {len(tool_names)} tool functions in app/tools.py")

with open(AGENT_PY, "r") as f:
    text = f.read()

# Replace import block
import_block = "from app.tools import (\n" + ",\n".join([f"    {t}" for t in tool_names]) + ",\n)\n"

start_imp = text.find("from app.tools import (")
end_imp = text.find(")", start_imp) + 1
text = text[:start_imp] + import_block + text[end_imp:]

# Replace tools list in Agent
start_tools = text.find("tools=[\n        PreloadMemoryTool(),")
end_tools = text.find("],", start_tools) + 2

tools_param = "tools=[\n        PreloadMemoryTool(),\n" + ",\n".join([f"        {t}" for t in tool_names]) + ",\n    ],"
text = text[:start_tools] + tools_param + text[end_tools:]

with open(AGENT_PY, "w") as f:
    f.write(text)

print(f"Successfully registered all {len(tool_names)} tools in app/agent.py!")
