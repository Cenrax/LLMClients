import os
from dotenv import load_dotenv

# Function to load the OpenAI API key
def load_openai_api_key():
    try:
        # Load environment variables from .env file
        load_dotenv()
        
        # Attempt to read the API key
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("OPENAI_API_KEY is not set in the .env file.")
        print(api_key)
        return api_key
    except Exception as e:
        # Handle errors (e.g., file not found, variable not set)
        print(f"Error loading the OpenAI API key: {e}")
        
