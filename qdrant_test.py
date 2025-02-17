from qdrant_client import QdrantClient
import json
import uuid
from qdrant_client.models import Distance, VectorParams, PointStruct


def create_collection(client, collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config={
            "size": 384,
            "distance": "Euclid"
        }
    )


def upload_data_to_qdrant(client, collection_name, data):
    points = [
    PointStruct(
        id=i + 1,  # Unique ID for each point
        vector=item["vector"],  # Embedding vector (replace with real embeddings)
        payload={
            "error": item["error"],
            "solution": item["solution"],
            "error_description": item["error_description"],
            "error_id" : i
        }
    )
    for i, item in enumerate(data)
    ]
    client.upsert(collection_name, points)


qdrant_client = QdrantClient(
    url="https://bf2cca4e-db89-405b-8488-25e46e99f5cf.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ1OTc5MDc4fQ.hLR33jYHhK7Jv1F0moloBaVNFo-ofhnR-XWD3IQAEOI",
)

with open("data.json") as f:
    input_data = json.load(f)

# print(len(input_data[0]['vector']))
create_collection(qdrant_client, "errors_collection")

upload_data_to_qdrant(qdrant_client, "errors_collection", input_data)