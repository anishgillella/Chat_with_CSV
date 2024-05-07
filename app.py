import streamlit as st
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI and PandasAI
llm = OpenAI(api_token=openai_api_key)
pandas_ai = PandasAI(llm)

# Create a Streamlit app
st.set_page_config(layout='wide')
st.title("Query CSV with Natural Language")

# Upload CSV file
input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

# Query input field
query_input = st.text_area("Enter your query")

# Button to trigger query
if st.button("Query CSV"):
	# Read uploaded CSV file
	if input_csv is not None:
		data = pd.read_csv(input_csv)
		
		# Query CSV with natural language
		result = pandas_ai.run(data, prompt=query_input)
		
		# Display result
		st.success(result)
	else:
		st.error("Please upload a CSV file")
