from sentence_transformers import SentenceTransformer
import qdrant_client

model = SentenceTransformer("all-MiniLM-L6-v2")
client = qdrant_client.QdrantClient("http://localhost:6333")

def store_vectors(text):
    vectors = model.encode(text.split("\n")).tolist()
    client.upload_collection(
        collection_name="document_vectors",
        vectors=vectors,
        payloads=[{"text": s} for s in text.split("\n")]
    )

def retrieve_vectors(query):
    query_vector = model.encode(query).tolist()
    results = client.search("document_vectors", query_vector, limit=5)
    return [hit.payload["text"] for hit in results]
