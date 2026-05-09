from itertools import chain
import os
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

st.title("Agile Coaching Information")
llm=ChatOllama(model="gemma:2B")
#llm=ChatOpenAI(model="gpt-5-mini", openai_api_key=OPENAI_API_KEY)
prompt_template = ChatPromptTemplate.from_messages(
    [
            ("system", "Yor are a Agile Coach Expert. "
            "If the question is not related to Agile Coaching then simply reply as 'I dont Know'."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{query}")
            ] 
           )



chain = prompt_template | llm

history = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain, 
    lambda session_id: history,
    input_messages_key="query",
    history_messages_key="chat_history"
)

# Display chat history
for msg in history.messages:
    with st.chat_message(msg.type):
        st.write(msg.content)

# Handle user input
if query := st.chat_input("Enter your query:"):
    # Display user message
    with st.chat_message("human"):
        st.write(query)
    
    # Display AI message with streaming
    with st.chat_message("ai"):
        response_placeholder = st.empty()
        full_response = ""
        for chunk in chain_with_history.stream(
            input={"query": query},
            config={"configurable": {"session_id": "user_session"}}
        ):
            full_response += chunk.content
            response_placeholder.write(full_response)
        