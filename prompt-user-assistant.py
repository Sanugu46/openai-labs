import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # Reads the API key from the environment variable

client = OpenAI()

custom_messages = [
    {
      "role": "user",
      "content": [{ "type": "text", "text": "Knock, knock" }]
    },
    {
      "role": "assistant",
      "content": [{ "type": "text", "text": "Who's is there?" }]
    },
    {
      "role": "user",
      "content": [{ "type": "text", "text": "Elephant" }]
    }
  
]

completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=custom_messages,
    temperature=0.8,
    max_tokens=10,
    top_p=1
)
chat_complettion_message_content= completion.choices[0].message.content
print(chat_complettion_message_content)