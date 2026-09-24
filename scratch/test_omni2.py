import base64
import sys
from google import genai

PROJECT_ID = "qwiklabs-gcp-02-8b55424b019a"

client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")

prompt = "A 3-second quick food clip of sizzling steak on a hot pan"

print("Calling client.interactions.create with gemini-omni-flash-preview...", flush=True)
try:
    interaction = client.interactions.create(
        model="gemini-omni-flash-preview",
        input=prompt,
    )
    print("Interaction type:", type(interaction), flush=True)
    print("Interaction dir/attributes:", [a for a in dir(interaction) if not a.startswith("_")], flush=True)
    
    video_bytes = None
    if hasattr(interaction, "output_video") and interaction.output_video:
        print("Found output_video:", type(interaction.output_video), flush=True)
        if hasattr(interaction.output_video, "data"):
            data = interaction.output_video.data
            if isinstance(data, str):
                video_bytes = base64.b64decode(data)
            else:
                video_bytes = data
    elif hasattr(interaction, "outputs"):
        print("Found outputs:", interaction.outputs, flush=True)
    
    if video_bytes:
        print("Successfully extracted video_bytes! Length:", len(video_bytes), flush=True)
    else:
        print("Raw interaction object:", interaction, flush=True)

except Exception as e:
    print("Error:", e, flush=True)
