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



AI-Document-Assistant/
│── app/                          # Main application module  
│   ├── api/                      # API-related code  
│   │   ├── __init__.py  
│   │   ├── routes.py             # Defines FastAPI routes  
│   ├── core/                     # Core app configurations  
│   │   ├── __init__.py  
│   │   ├── config.py             # Settings & environment variables  
│   │   ├── database.py           # Database setup (SQLite/PostgreSQL)  
│   ├── services/                 # Business logic and processing  
│   │   ├── __init__.py  
│   │   ├── pdf_processing.py     # PDF extraction logic  
│   │   ├── csv_processing.py     # CSV parsing logic  
│   │   ├── vector_store.py       # Qdrant vector storage operations  
│   │   ├── chatbot.py            # AI chatbot logic  
│   ├── tests/                    # Unit & integration tests  
│   │   ├── __init__.py  
│   │   ├── test_pdf_processing.py  
│   │   ├── test_csv_processing.py  
│   │   ├── test_chatbot.py  
│   ├── main.py                   # FastAPI entry point  
│── data/                         # Folder for uploaded files  
│── docker/                       # Docker-related files  
│   ├── Dockerfile  
│   ├── docker-compose.yml  
│── requirements.txt              # Dependencies  
│── README.md                     # Documentation  




Running with Docker:
'''
docker build -t ai-doc-assistant .
docker run -p 8000:8000 ai-doc-assistant '''


http://localhost:8000/

http://localhost:8000/docs for Swagger UI

http://localhost:8000/redoc for ReDoc

FastAPI automatically generates documentation for all your endpoints



## Run Qdrant using Docker:

docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
This starts the Qdrant server on:

REST API: http://localhost:6333

gRPC: http://localhost:6334

Then try running your FastAPI app again


### **Next Steps:**
- Add a **Streamlit Dashboard**  
- Deploy to **VPS using Docker Compose**  
- Improve **chatbot accuracy** using **LLM fine-tuning**  

