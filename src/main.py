


import os

from dotenv import load_dotenv
from client import openai_client

if __name__ == "__main__":
    response = openai_client.perform_chat("Who was Portia")
