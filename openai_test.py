import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


def get_query(Prompt):
    from openai import AzureOpenAI

  
    client = AzureOpenAI(
                azure_endpoint = os.getenv("azure_endpoint"),
                api_key = os.getenv("api_key"),
                api_version = os.getenv("api_version")
            )
    conversation1 = [{"role": "system", "content": f"""You are a assistant, just reply with details answer.
    """},
                    {"role": "user", "content": prompt}]
    response1 = client.chat.completions.create(
            messages=conversation1,
            model="gpt-4",
            temperature=0
        )
    output=response1.choices[0].message.content
    return output


st.title("DEMO")

prompt = st.text_area("Enter your prompt")
if st.button("Get Query"):
    with st.spinner('Processing...'):
        output = get_query(prompt)
        st.write(output)
