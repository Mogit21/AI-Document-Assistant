# AI-Document-Assistant

## Features:
- Extracts text from PDFs & CSVs
- Stores document embeddings in Qdrant
- AI-powered chatbot for querying documents
- API built with FastAPI
- Dockerized for easy deployment

## Installation:
```sh
git clone https://github.com/your-username/AI-Document-Assistant.git
cd AI-Document-Assistant
pip install -r requirements.txt
uvicorn app.main:app --reload
