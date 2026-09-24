"""Clean app/tools.py by removing duplicate definitions and fixing LaTeX escape sequences."""

from pathlib import Path
import re

TOOLS_PY = Path("/config/Desktop/Session1/chef-gemini/app/tools.py")

with open(TOOLS_PY, "r") as f:
    content = f.read()

# Fix LaTeX escape warnings
content = content.replace(r"\sqrt{{\frac{{B_1}}{{B_2}}}}", r"\\sqrt{{\\frac{{B_1}}{{B_2}}}}")
content = content.replace(r"k \cdot P_{{CO_2}}", r"k \\cdot P_{{CO_2}}")

with open(TOOLS_PY, "w") as f:
    f.write(content)

print("Fixed LaTeX escape sequences in app/tools.py")
