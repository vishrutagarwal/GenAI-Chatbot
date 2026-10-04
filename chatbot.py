from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
                   page_title="Chatbot",
                   page_icon="",
                   layout="centered"
                   )

st.title("Generative AI Chatbot")

# initiate char history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# store chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# LLM initiation

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1
    )

user_prompt = st.chat_input("Ask Chatbot ...")

if user_prompt:
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({'role':'user','content':user_prompt})

    response = llm.invoke(
        input=[{'role':'system','content':'yoou are a helpful assistent'},*st.session_state.chat_history]
    )

    assistent_response = response.content
    st.session_state.chat_history.append({'role':'assistant','content':assistent_response})

    with st.chat_message('assistant'):
        st.markdown(assistent_response)