import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Reads the API key from the environment variable

client = openai.OpenAI()

# In a real-world scenario, you would get the schema from the database.
# sql_schema = get_schema_from_database()

# Function to read the content of the shopping-cart-schema-file.txt file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Read the database schema from the file. 
sql_schema = read_file('shopping-cart-schema-file.txt')

messages = [
    {
        "role": "user",
        "content": [{ "type": "text", "text": "How many order are there in total?" }]
    },
    {
        "role": "assistant",
        "content": [{ "type": "text", "text": "Select count(*) as order_count from Orders" }]
    },
    {
        "role": "user",
        "content": [{ "type": "text", "text": "Get me details of all the customers who placed an order for product_id=2234." }]
    },
    {
        "role": "system",
        "content": [{ "type": "text", "text": "You are a database expert. You will provide SQL queries to user prompts using only this schema="+sql_schema }]

    }
]

completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=messages,
    temperature=0.8,
    max_tokens=100,
    top_p=1
)
chat_complettion_message_content= completion.choices[0].message.content
print(chat_complettion_message_content)