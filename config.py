import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT = os.environ['TELEGRAM_BOT_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
ALLOWED_USERS = [int(user_id) for user_id in os.environ['ALLOWED_USERS'].split(",")]
POSTGRES_URI = os.getenv("POSTGRES_URI")