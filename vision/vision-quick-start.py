import base64
import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # Reads the API key from the environment variable

client = OpenAI()

image_path = "wiki-elephant-family.jpg"

def encode_image(image_url):
    with open(image_url, "rb") as image_file:
        image_data = image_file.read()
        return base64.b64encode(image_data).decode("utf-8")

base64_image = encode_image(image_path)

completion = client.chat.completions.create(
    model ="gpt-40-mini",
    messages=[
        {"role": "user", 
         "content": [
             {"type": "text", "text": "What is in the image?"},
             {
                 "type": "image_url", 
                 "image_url": {
                        "url": f'data:image/jpeg;base64,{base64_image}'
                 },
            },
         ],
        },
    ],
    max_tokens=300
)
chat_complettion_message_content= completion.choices[0]
print(chat_complettion_message_content)