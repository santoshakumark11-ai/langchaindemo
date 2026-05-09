import os
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

st.title("Speech Title and Content Generator")
#llm=ChatOllama(model="gemma:2B")
llm=ChatOpenAI(model="gpt-5-mini", openai_api_key=OPENAI_API_KEY)
llm_speech=ChatOllama(model="mistral")
title_prompt = PromptTemplate(input_variables=["topic"], 
                                 template=""" You are an experienced speech writer.
                                    You need to craft an impactful title for a speech
                                    on the following topic: {topic}
                                    Answer exactly with one title.""")

speech_prompt = PromptTemplate(input_variables=["title"], 
                                 template=""" You need to write a powerful speech of 350 words
                                    for the following title: {title}""")

first_chain = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(f"Title: {title}"), title)[1])
second_chain = speech_prompt | llm_speech
final_chain = first_chain | second_chain

topic = st.text_input("Enter The Topic:")

if button := st.button("Generate Speech"):
    response = final_chain.invoke({"topic": topic})
    st.write(response.content)

    