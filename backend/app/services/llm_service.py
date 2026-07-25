import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def ask_gemini(question: str, context: str) -> str:
    """
    Generate an answer using the retrieved document context.
    """

    prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

If the answer is not present in the context, reply:
"I couldn't find the answer in the uploaded document."

--------------------
Context:
{context}
--------------------

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text