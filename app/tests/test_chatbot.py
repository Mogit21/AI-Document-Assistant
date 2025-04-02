from app.services.chatbot import generate_response

def test_chatbot():
    response = generate_response("What is AI?")
    assert isinstance(response, str)
    assert len(response) > 0
