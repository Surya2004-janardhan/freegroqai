import streamlit as st
import requests
import os
from groq import Groq

# Correctly access the API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client with the correct key
client = Groq(api_key=GROQ_API_KEY)

# Streamlit UI
st.title("Ask anything")
st.subheader("Press send to generate a response")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)
