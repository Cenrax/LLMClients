import os
from dotenv import load_dotenv

# Function to load configurations for local LLM
def load_local_llm_config():
    try:
        # Load environment variables from .env file
        load_dotenv()
        
        # Attempt to read the configurations
        api_key = os.getenv("LOCAL_LLM_KEY")
        base_url = os.getenv("LOCAL_BASE_URL")
        api_base = os.getenv("LOCAL_API_BASE")

        # Validate the configurations
        if api_key is None:
            raise ValueError("LOCAL_LLM_KEY is not set in the .env file.")
        if base_url is None:
            raise ValueError("LOCAL_BASE_URL is not set in the .env file.")
        if api_base is None:
            raise ValueError("LOCAL_API_BASE is not set in the .env file.")
        
        print(f"API Key: {api_key}")
        print(f"Base URL: {base_url}")
        print(f"API Base: {api_base}")
        
        return api_key, base_url, api_base
    except Exception as e:
        # Handle errors (e.g., file not found, variable not set)
        print(f"Error loading the local LLM configurations: {e}")

# Example usage
if __name__ == "__main__":
    load_local_llm_config()
