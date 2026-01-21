import streamlit as st
from langchain_ollama import OllamaLLM

@st.cache_resource
def loadllm():
    return OllamaLLM(model="phi3")

llm = loadllm()

st.header("OMNITRON AI")
st.write("OMNITRON V1.0")

user_input = st.text_input("ASK ME SOMETHING !")

response = ""
if user_input :
     with st.spinner("OMNITRON IS THINKING !"):
        response = llm.invoke(user_input)

st.write("Here's your answer")
st.write(response)

