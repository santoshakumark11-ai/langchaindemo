import os
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llm=ChatOllama(model="mistral")

query=input("What is your question? ")
response= llm.invoke(query)

print(response)
