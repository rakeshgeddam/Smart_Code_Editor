from qdrant_client import QdrantClient
import subprocess
from sentence_transformers import SentenceTransformer
import sys
# Run an external Python script and capture its stderr output
# result = subprocess.run(
#     ['python', 'script_with_error.py'],  
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True  # Ensures output is returned as a string
# )

# Capture only the error output (stderr)
# error_output = result.stderr
# print("Captured Error from Subprocess:")
# print(error_output)

# Convert the captured error string into a vector embedding
# model = SentenceTransformer("all-MiniLM-L6-v2")
# embedding = model.encode("The Very own biscuit that I left in the car")
#print("Vector Embedding:")
# print(embedding)

def getClosestErrors(embedding):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = model.encode(embedding)

    client = QdrantClient(
        url="https://bf2cca4e-db89-405b-8488-25e46e99f5cf.us-east4-0.gcp.cloud.qdrant.io:6333", 
        api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ1OTc5MDc4fQ.hLR33jYHhK7Jv1F0moloBaVNFo-ofhnR-XWD3IQAEOI",
    )


    # Query Qdrant
    #query_vector = [1, 2, 3, 4]  # Replace with your query vector
    search_result = client.query_points(
        collection_name="errors_collection",
        query=embedding,
        limit=2
    )

    # /print(search_result)
    for i in search_result:
        try:
            value = i[1]
            for point in value:
                # print(val)
                if point.score > 1.0:
                    print("This is closest error we found which might not possibly be thee right one")
                print(f"ID: {point.id}, Score: {point.score}")
                print(f"Error: {point.payload.get('error', 'N/A')}")
                print(f"Solution: {point.payload.get('solution', 'N/A')}")
                print(f"Description: {point.payload.get('error_description', 'N/A')}")
                print(f"Error ID: {point.payload.get('error_id', 'N/A')}")
                print("-" * 40)
        except Exception as e:
            print("The Response failed with the following error", e)


    return value
# getClosestErrors(embedding)    