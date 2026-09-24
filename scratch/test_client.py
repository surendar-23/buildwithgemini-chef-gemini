from google import genai

client = genai.Client(vertexai=True, project="qwiklabs-gcp-02-8b55424b019a", location="global")

print("Client attributes:", [a for a in dir(client) if not a.startswith("_")])
print("client.models attributes:", [a for a in dir(client.models) if not a.startswith("_")])
if hasattr(client, "interactions"):
    print("client.interactions attributes:", [a for a in dir(client.interactions) if not a.startswith("_")])
