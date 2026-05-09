import os
import streamlit as st
from langchain_community.chat_models import ChatOllama
#from langchain.globals import set_debug
from dotenv import load_dotenv

load_dotenv()
#set_debug(True)

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

st.title("Chat with Gemma:2B")
query = st.text_input("What is your question?")
if query:
    llm = ChatOllama(model="gemma:2B")
    response = llm.invoke(query, streaming=True)
    st.write(response.content)
