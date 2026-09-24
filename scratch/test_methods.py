import base64
from google import genai
from google.genai import types

PROJECT_ID = "qwiklabs-gcp-02-8b55424b019a"
client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")

prompt = "A 3-second appetizing clip of a sizzling gourmet burger"

print("1. Testing client.models.generate_videos...")
try:
    operation = client.models.generate_videos(
        model="gemini-omni-flash-preview",
        prompt=prompt,
    )
    print("generate_videos return type:", type(operation))
    print("generate_videos attrs:", [a for a in dir(operation) if not a.startswith("_")])
    if hasattr(operation, "generated_videos"):
        for gv in operation.generated_videos:
            print("gv video bytes:", len(gv.video.video_bytes) if hasattr(gv, "video") and hasattr(gv.video, "video_bytes") else gv)
    elif hasattr(operation, "result"):
        print("operation.result():", operation.result())
except Exception as e:
    print("generate_videos error:", e)

print("\n2. Testing client.interactions.create...")
try:
    interaction = client.interactions.create(
        model="gemini-omni-flash-preview",
        input=prompt,
    )
    print("interaction type:", type(interaction))
    print("interaction attrs:", [a for a in dir(interaction) if not a.startswith("_")])
    print("interaction dict/repr:", str(interaction)[:300])
except Exception as e:
    print("interactions.create error:", e)
