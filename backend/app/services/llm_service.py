import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read the API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create the Gemini client
client = genai.Client(api_key=API_KEY)


def generate_response(user_message: str) -> str:
    """
    Sends the user's message to Gemini and returns the generated text.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message,
    )

    return response.text