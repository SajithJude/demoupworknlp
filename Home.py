import streamlit as st
import os 
import openai

openai.api_key = os.getenv("APIKEY")

inp = st.text_input("Enter you query")
if st.button("Search"):
    input = str(source) + "  :"+ str(input)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.56,
        max_tokens=2066,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0
    )
    out=  response.choices[0].text
    st.write(out)