import openai
from typing import Optional
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


async def fetch_gpt_response(
    prompt: str, gpt_version: Optional[str] = "gpt-3.5"
) -> str:
    engine = "text-davinci-002" if gpt_version == "gpt-3.5" else "gpt-4"

    data = {
        "prompt": prompt,
        "max_token": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    response = openai.Complete.create(engine=engine, **data)

    if response["object"] == "text_completion":
        return response["choice"][0]["text"].strip()
    else:
        raise Exception("Error on request API OpenAI")
