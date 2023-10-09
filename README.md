# LangChainSamples
Learning LangeChain using simple code samples

## Installation
Install the following
- Install latest Python
- Install latest Anaconda

Add Python and Anaconda to the Path (Environment Variables)
## Verify the installation
Make sure you have Python version > 3.8

## Clone this repo
Get the latest code from this repo

## Test the solution
- Using Visual Studio Code open the folder LangChainSamples
- In the Terminal open a new Terminal using Command Prompt
- Create a new virtual environment
  ```python
 	conda create -p myenv python=3.10 -y

- Activate the virtual environment
	```python
    conda activate myenv
    or
    conda activate C:\Users\umarm\Source\Repos\langchain\myenv
- Install the requirements
  ```python
  pip install -r requirements.txt
- Open the constants.py file
  - Update *openai_key* with your own value
  - If you don't have an OpenAI key, you can get one from https://platform.openai.com/
  - Once you login, click on *Personal* (top right coner) and then click on *View API keys*, click on *+Create new secret key* 
  - If you dont have enough balance or not able to create a key, go to *Billing*, then *Overview* then click on *Add to credit balance* and add $5 (example) or so to your account
  
- Run the code from the Terminal (Command Prompt)
  ```python
  streamlit run 1-OpenAISearch.py
- You can enter any topic or question and the OpenAI will try to answer it for you
- Once you successfully run the first file you can run the other files as well. For example:
  ```python
  streamlit run 2-Singleprompt.py
