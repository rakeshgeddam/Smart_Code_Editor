from sentence_transformers import SentenceTransformer
import json
# Load your JSON data
with open('python_errors.json') as f:
    data = json.load(f)

# Create a Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
vector_size = 0

# Embed your text data
for item in data:
    text = item['error']
    vector = model.encode(text)
    item['vector'] = vector.tolist()
    if vector_size == 0:
        vector_size = len(item['vector'])
    

# Now your data is embedded in vectors
#print(data)
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)  # indent=4 makes it human-readable