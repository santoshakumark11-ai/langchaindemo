import os
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

st.title("Travel Guide Information")
#llm=ChatOllama(model="gemma:2B")
llm=ChatOpenAI(model="gpt-5-mini", openai_api_key=OPENAI_API_KEY)
prompt_template = PromptTemplate(input_variables=["city", "month", "language", "budget"], 
                                 template=""" Yor are a Travel Guide Expert. Answer the question in following format: 
                                            Welcome to the {city} travel guide!
                                            If you're visiting in {month}, here's what you can do:
                                            1. Must-visit attractions.
                                            2. Local cuisine you must try.
                                            3. Useful phrases in {language}.
                                            4. Tips for traveling on a {budget} budget.
                                            Enjoy your trip!""")

city = st.text_input("Enter The City:")
month = st.text_input("Enter The Month:")
language = st.text_input("Enter the language:")
budget = st.text_input("Enter your budget (e.g., low, medium, high):")

if button := st.button("Get Travel Information"):
    response = llm.invoke(prompt_template.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)
    