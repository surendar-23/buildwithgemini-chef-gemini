import base64
import os
from google import genai
from google.genai import types

PROJECT_ID = "qwiklabs-gcp-02-8b55424b019a"

client = genai.Client(vertexai=True, project=PROJECT_ID, location="global")

prompt = "A 5-second appetizing video clip of sizzling garlic shrimp in an olive oil pan, gourmet plating"

print("Testing generate_content with gemini-omni-flash-preview...")
try:
    response = client.models.generate_content(
        model="gemini-omni-flash-preview",
        contents=prompt,
    )
    print("Response candidates:", len(response.candidates))
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            print("Found inline_data with mime_type:", part.inline_data.mime_type)
            print("Bytes length:", len(part.inline_data.data))
        elif part.text:
            print("Text part:", part.text[:100])
except Exception as e:
    print("generate_content error:", e)

print("\nTesting interactions.create with gemini-omni-flash-preview...")
try:
    interaction = client.interactions.create(
        model="gemini-omni-flash-preview",
        input=prompt,
    )
    print("Interaction output:", interaction)
except Exception as e:
    print("interactions.create error:", e)
