from app.services.pdf_processing import extract_text_from_pdf

def test_pdf_extraction():
    with open("tests/sample.pdf", "rb") as f:
        text = extract_text_from_pdf(f)
    assert "expected phrase" in text
