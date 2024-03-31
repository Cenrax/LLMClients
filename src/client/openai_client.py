from config import openai_config, local_llm_config
from llama_index.llms.openai import OpenAI
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.prompts.system import SHAKESPEARE_WRITING_ASSISTANT

def perform_chat(message : str):
    try:
        
        key = openai_config.load_openai_api_key()
        llm = OpenAI(model="gpt-3.5-turbo-0613", api_key=key, max_retries=2)
        chat_engine = SimpleChatEngine.from_defaults(
    system_prompt=SHAKESPEARE_WRITING_ASSISTANT, llm=llm
)
        response = chat_engine.chat(message)
        print(response)
        return response
    
    except Exception as e:
        print("Primary attempt failed")
        print("*******************Defaulting to LocalLLM*******************")
        try:
            # Retry with the fallback configuration
            local_key,base_url,api_base= local_llm_config.load_local_llm_config()
            llm_local = OpenAI(model="gpt-3.5-turbo-0613", api_key=local_key, base_url=base_url, api_base=api_base)
            chat_engine = SimpleChatEngine.from_defaults(
    system_prompt=SHAKESPEARE_WRITING_ASSISTANT, llm=llm_local
)
            response = chat_engine.chat(message)
            print(response)
            return response
        
        except Exception as e:
            # If the retry also fails, then show error
            print("Retry attempt failed:", str(e))
            return "Error"

