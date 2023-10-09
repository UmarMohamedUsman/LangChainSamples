# Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework
st.title("LangChain demo with OpenAI API")
input_text = st.text_input("Search using OpenAI for anything you would like to explore")

if input_text:
    llm=OpenAI(temperature=0.8)
    st.write(llm(input_text))
