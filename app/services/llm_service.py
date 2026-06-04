import requests

def generate_reply(message: str):

    prompt = f"""
    You are a professional customer support assistant.

    Reply politely and professionally.

    Customer message:
    {message}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]