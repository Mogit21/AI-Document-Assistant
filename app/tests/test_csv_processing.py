from io import BytesIO
from app.services.csv_processing import process_csv

def test_csv_processing():
    csv_data = b"Name, Age\nJohn, 30\nDoe, 25"
    file = BytesIO(csv_data)
    result = process_csv(file)
    assert result[0]["Name"] == "John"
