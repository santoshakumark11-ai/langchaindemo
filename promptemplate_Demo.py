import os
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

st.title("Country Cuisine Information")
#llm=ChatOllama(model="gemma:2B")
llm=ChatOpenAI(model="gpt-5-mini", openai_api_key=OPENAI_API_KEY)
prompt_template = PromptTemplate(input_variables=["country", "no_of_paragraphs", "language"], 
                                 template="""You are an expert in traditional cuisines. 
                                 You provide information about a specific dish from a specific country. 
                                 Avoid giving information about fictional places. 
                                 If the country is fictional or non-existent answer: I don't know. 
                                 Answer the question: What is the traditional cuisine of {country}?.
                                 answer in {no_of_paragraphs} paragraphs and answer in  {language} language""")

country = st.text_input("Enter The Country:")
no_of_paragraphs = st.number_input("Enter the number of paragraphs:", min_value=1, value=5)
language = st.text_input("Enter the language:")

if button := st.button("Get Cuisine Information"):
    response = llm.invoke(prompt_template.format(country=country, no_of_paragraphs=no_of_paragraphs, language=language))
    st.write(response.content)
    