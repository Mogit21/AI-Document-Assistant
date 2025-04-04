from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_processing import extract_text_from_pdf
from app.services.csv_processing import process_csv
from app.services.chatbot import generate_response

router = APIRouter()

@router.post("/upload/pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    return {"extracted_text": text}

@router.post("/upload/csv/")
async def upload_csv(file: UploadFile = File(...)):
    data = process_csv(file)
    return {"processed_data": data}

@router.get("/chat/")
async def chat(query: str):
    response = generate_response(query)
    return {"response": response}


#todo
