import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    # Use Llama 3 70B for best reasoning/speed balance
    MODEL_NAME = "llama-3.3-70b-versatile" 

    if not GROQ_API_KEY:
        raise ValueError("❌ API Key missing! Please set GROQ_API_KEY in .env file.")