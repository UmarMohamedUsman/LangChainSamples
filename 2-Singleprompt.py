# Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework
st.title("Destination search with OpenAI API (using Single Prompt)")
input_text = st.text_input("Single Prompt: I would like to explore the following destination. Tell me about {destination}.")


if input_text:
    llm=OpenAI(temperature=0.8)

    # PromptTemplate
    first_input_prompt = PromptTemplate(
                              input_variables=['destination'],
                              template="I would like to explore the following destination. Tell me about {destination}."
                              )
    chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)
        
    st.write(chain.run(input_text))
