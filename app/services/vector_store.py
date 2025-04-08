from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import uuid



# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Qdrant
client = QdrantClient("http://localhost:6333")

COLLECTION_NAME = "document_vectors"

# Create collection if not exists
def create_collection():
    if COLLECTION_NAME not in [col.name for col in client.get_collections().collections]:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance=Distance.COSINE)
        )

create_collection()

# Store vectors into Qdrant
def store_vectors(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    vectors = model.encode(lines).tolist()
    points = [
        PointStruct(id=str(uuid.uuid4()), vector=vector, payload={"text": line})
        for vector, line in zip(vectors, lines)
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)

# Retrieve vectors from Qdrant
def retrieve_vectors(query, top_k=5):
    query_vector = model.encode(query).tolist()
    results = client.search(collection_name=COLLECTION_NAME, query_vector=query_vector, limit=top_k)
    return [hit.payload["text"] for hit in results]
