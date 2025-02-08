import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # Reads the API key from the environment variable

client = OpenAI()

custom_messages = [
        {
            "role": "developer",
            "content": [
            {
                "type": "text",
                "text": """You are an historian and give ligimate answers.
                        Respond with no more than 10 words"""
            }
        ]
        },
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "What is the capital of the United States?"
            }
            ]
        }
]

completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=custom_messages,
)
chat_complettion_message_content= completion.choices[0].message.content
print(chat_complettion_message_content)