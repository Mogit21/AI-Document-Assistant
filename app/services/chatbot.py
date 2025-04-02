from app.services.vector_store import retrieve_vectors
from transformers import pipeline

chat_model = pipeline("text-generation", model="gpt2")

def generate_response(query):
    context = retrieve_vectors(query)
    prompt = " ".join(context) + " Answer: "
    response = chat_model(prompt, max_length=100)[0]["generated_text"]
    return response
