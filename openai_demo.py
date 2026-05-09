import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(model="gpt-5-mini", openai_api_key=OPENAI_API_KEY)

query=input("What is your question? ")
response= llm.invoke(query)

print(response)
