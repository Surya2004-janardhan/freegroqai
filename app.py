# import streamlit as st
# import requests
# import os
# from groq import Groq

# # Correctly access the API key from Streamlit secrets
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# # Initialize Groq client with the correct key
# client = Groq(api_key=GROQ_API_KEY)

# # Streamlit UI
# st.title("Ask anything")
# # st.title("Your App Title")  
# st.markdown("<small>Press send to generate response</small>", unsafe_allow_html=True)

# # st.subheader("Press send to generate a response")

# user_input = st.text_input("Ask me anything:")

# if st.button("Send"):
#     if user_input:
#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[{"role": "user", "content": user_input}]
#         )
#         st.write(response.choices[0].message.content)
import streamlit as st
from groq import Groq

# Set API Key
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.title("Ask anything")
st.markdown("<small>Press send to generate a response</small>", unsafe_allow_html=True)

# Store messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages in reverse order (newest on top)
for msg in reversed(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Sticky input box at the bottom
user_input = st.text_input("Type your message:", key="user_input", label_visibility="hidden")

if st.button("Send") and user_input:
    # Append user input to message history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from the model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[{"role": "user", "content": user_input}]
    )

    # Append response to message history
    bot_response = response.choices[0].message.content
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Clear input box
    st.return()
