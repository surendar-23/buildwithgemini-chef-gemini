from unittest.mock import MagicMock
from app.tools import generate_dish_video

# Create a mock ToolContext
mock_tool_context = MagicMock()

print("Testing generate_dish_video tool function...")
result = generate_dish_video("Sizzling Tuscan Pasta", mock_tool_context)
print("Tool Output:", result)

print("Checking if tool_context.save_artifact was called...")
print("save_artifact call count:", mock_tool_context.save_artifact.call_count)
if mock_tool_context.save_artifact.call_count > 0:
    args, kwargs = mock_tool_context.save_artifact.call_args
    print("Saved filename:", kwargs.get("filename"))
    artifact = kwargs.get("artifact")
    print("Artifact mime_type:", getattr(artifact, "mime_type", "video/mp4"))
