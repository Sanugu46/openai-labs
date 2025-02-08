import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # Reads the API key from the environment variable

client = OpenAI()

completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant. You respond with no more than 10 words"},
        {
            "role": "user", 
            "content": "What is the purpose of life?"
        }
    ]
)
chat_complettion_message_content= completion.choices[0].message.content
print(chat_complettion_message_content)