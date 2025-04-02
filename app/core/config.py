import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/app.db")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
