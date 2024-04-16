import streamlit as st
from openai import OpenAI

f = open("C:\\Users\\91949\\Data Science Internship\\genai\\.openai_api_key.txt")
OPENAI_API_KEY = f.read()

st.title("Code GPT")
st.subheader("Finds mistake and corrects the code ")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_input("Enter a Code")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-16k-0613",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)