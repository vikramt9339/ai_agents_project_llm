import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Validate that API key is available
if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY not found in environment variables.")
    print("Please check your .env file and ensure the API key is on a single line.")
    print("Example .env file content:")
    print("OPENAI_API_KEY=sk-your-actual-api-key-here")
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

def get_openai_client():
    """
    Returns a configured OpenAI client instance
    """
    from openai import OpenAI
    
    return OpenAI(api_key=OPENAI_API_KEY)

def create_chat_completion(messages, model="gpt-4o-mini"):
    """
    Helper function to create chat completions
    """
    client = get_openai_client()
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response 