import base64
from google import genai

client = genai.Client(vertexai=True, project="qwiklabs-gcp-02-8b55424b019a", location="global")

prompt = "A 3-second appetizing clip of sizzling prawns with garlic and butter"

print("Generating video with gemini-omni-flash-preview...")
interaction = client.interactions.create(
    model="gemini-omni-flash-preview",
    input=prompt,
)

def extract_bytes(interaction):
    video_bytes = None
    if hasattr(interaction, "output_video") and interaction.output_video:
        ov = interaction.output_video
        if isinstance(ov, list) and len(ov) > 0:
            data = getattr(ov[0], "data", None)
        else:
            data = getattr(ov, "data", None)
        if data:
            return base64.b64decode(data) if isinstance(data, str) else data
    return None

bytes_out = extract_bytes(interaction)
if bytes_out:
    print("SUCCESS! Video bytes length:", len(bytes_out))
else:
    print("Failed to extract bytes. Interaction:", interaction)
