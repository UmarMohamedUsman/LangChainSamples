# Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework
st.title("Destination search with OpenAI API (using Simple Sequential Chain)")
input_text = st.text_input("Using Two Prompts: I would like to explore the following destination. Tell me about {destination}.\r\nWhen is the good time to visit {output1}.")

# PromptTemplate

if input_text:
    llm=OpenAI(temperature=0.8)

    first_input_prompt = PromptTemplate(
                              input_variables=['destination'],
                              template="I would like to explore the following destination. Tell me about {destination}."
                              )
    chain1=LLMChain(llm=llm,prompt=first_input_prompt, verbose=True, output_key='output1')
    
    second_input_prompt = PromptTemplate(
                              input_variables=['output1'],
                              template="When is the good time to visit {output1}."
                              )
    chain2=LLMChain(llm=llm,prompt=second_input_prompt, verbose=True, output_key='output2')
    
    parent_chain = SimpleSequentialChain(chains=[chain1,chain2],verbose=True)
    st.write(parent_chain.run(input_text))
    
