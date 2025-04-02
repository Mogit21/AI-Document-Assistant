from fastapi.testclient import TestClient
from app.routers.uploads import router  # Import the router

client = TestClient(router)

def test_upload_pdf():
    file_content = b"Dummy PDF content"
    response = client.post(
        "/upload/pdf/",
        files={"file": ("test.pdf", file_content, "application/pdf")}
    )
    assert response.status_code == 200
    assert "extracted_text" in response.json()

def test_upload_csv():
    file_content = b"name,age\nJohn,30\nAlice,25"
    response = client.post(
        "/upload/csv/",
        files={"file": ("test.csv", file_content, "text/csv")}
    )
    assert response.status_code == 200
    assert "processed_data" in response.json()

def test_chat():
    response = client.get("/chat/?query=Hello")
    assert response.status_code == 200
    assert "response" in response.json()
