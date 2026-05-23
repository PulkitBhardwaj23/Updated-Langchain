from langchain_openai import ChatOpenAI  # communicate with open ai models
from langchain_core.prompts import ChatPromptTemplate   # structured reusable template with placeholders
from langchain_core.output_parsers import StrOutputParser    # strips metadata from LLMs

import streamlit as st    # to create web app
import os   # operating system
from dotenv import load_dotenv   # to load variables from .env file

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")   # grabbing api key which is an environment variable
## LangSmith tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"   # to start langSmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")   # loading langchain api key

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),   # instructions for system
        ("user","Question:{question}")     # actual input
    ]
)

## streamlit framework -> creating web app

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")   # renders text box

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser    # LCEL(LangChain Expression Language): prompt -> llm -> parser : using pipe

if input_text:     # runs only if user entered something 
    st.write(chain.invoke({'question':input_text}))    # runs the pipeline
