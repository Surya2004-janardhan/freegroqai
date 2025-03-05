import streamlit as st
import os
from groq import Groq

# os.environ['GROQ_API_KEY'] = ''
GROQ_API_KEY = st.secrets["API_KEY"]


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Ask anything")

user_input = st.text_input("Enter your message:")

if st.button("Submit"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    st.write("Response:")
    st.write(chat_completion.choices[0].message.content)
