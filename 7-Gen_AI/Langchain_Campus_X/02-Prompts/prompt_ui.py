from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


load_dotenv()
api_key = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta", 
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Elaborate'):
    result = model.invoke(user_input)
    st.write(result.content)