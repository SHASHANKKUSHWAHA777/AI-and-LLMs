import streamlit as st
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")  
response = llm.invoke("guide me on how to make an ai assistant")
print(response)
st.title("Hello Streamlit")
st.write("my 1st ai assistant")
user_input = st.text_input("Ask me anything!")
 
if user_input :
    with st.spinner("Thinking"):
        response = llm.invoke(user_input)
        
st.write("Answer:")
st.write(response)


