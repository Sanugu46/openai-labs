import os
from dotenv import load_dotenv
import openai

#This code is a simple example of how to use the OpenAI API with the Azure OpenAI service
# Requires OpenAI API key, Azure endpoint, and Azure API key

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") # Reads the API key from the environment variable
openai.api_type = "azure" # Sets the API type to Azure
openai.api_version = os.getenv("OPENAI_AZURE_API_VERSION") # Sets the API versionopenai.azure_endpoint=os.getenv("OPENAI_AZURE_ENDPOINT") # Sets the Azure endpoint
deployment_model = os.getenv("OPENAI_AZURE_DEPLOYMENT_MODEL") # The model to use for the deployment

response = openai.chat.completions.create(
    model=deployment_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. You respond with no more than 10 words"},
        { "role": "user", "content": "How big is the world?"}
    ]
)

#main function
if __name__ == '__main__':
    print(response.choices[0].message.content)
