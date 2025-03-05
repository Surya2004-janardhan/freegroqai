# # # # # import streamlit as st
# # # # # import requests
# # # # # import os
# # # # # from groq import Groq

# # # # # # Correctly access the API key from Streamlit secrets
# # # # # GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# # # # # # Initialize Groq client with the correct key
# # # # # client = Groq(api_key=GROQ_API_KEY)

# # # # # # Streamlit UI
# # # # # st.title("Ask anything")
# # # # # # st.title("Your App Title")  
# # # # # st.markdown("<small>Press send to generate response</small>", unsafe_allow_html=True)

# # # # # # st.subheader("Press send to generate a response")

# # # # # user_input = st.text_input("Ask me anything:")

# # # # # if st.button("Send"):
# # # # #     if user_input:
# # # # #         response = client.chat.completions.create(
# # # # #             model="llama-3.3-70b-versatile",
# # # # #             messages=[{"role": "user", "content": user_input}]
# # # # #         )
# # # # #         st.write(response.choices[0].message.content)
# # # # import streamlit as st
# # # # from groq import Groq

# # # # # Set API Key
# # # # GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# # # # client = Groq(api_key=GROQ_API_KEY)

# # # # st.title("Ask anything")
# # # # st.markdown("<small>Press send to generate a response</small>", unsafe_allow_html=True)

# # # # # Store messages in session state
# # # # if "messages" not in st.session_state:
# # # #     st.session_state.messages = []

# # # # # Display previous messages in reverse order (newest on top)
# # # # for msg in reversed(st.session_state.messages):
# # # #     with st.chat_message(msg["role"]):
# # # #         st.markdown(msg["content"])

# # # # # Sticky input box at the bottom
# # # # user_input = st.text_input("Type your message:", key="user_input", label_visibility="hidden")

# # # # if st.button("Send") and user_input:
# # # #     # Append user input to message history
# # # #     st.session_state.messages.append({"role": "user", "content": user_input})

# # # #     # Get response from the model
# # # #     response = client.chat.completions.create(
# # # #         model="llama-3.3-70b-versatile", 
# # # #         messages=[{"role": "user", "content": user_input}]
# # # #     )

# # # #     # Append response to message history
# # # #     bot_response = response.choices[0].message.content
    
# # # #     st.session_state.messages.append({"role": "assistant", "content": bot_response})

# # # #     # Clear input box
# # # #     st.rerun()
# # # import streamlit as st
# # # from groq import Groq

# # # # Set API Key
# # # GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# # # client = Groq(api_key=GROQ_API_KEY)

# # # # Custom CSS to keep the input box at the bottom
# # # st.markdown(
# # #     """
# # #     <style>
# # #     .stChatInputContainer {
# # #         position: fixed;
# # #         bottom: 10px;
# # #         width: 100%;
# # #         background: white;
# # #         padding: 10px;
# # #         z-index: 100;
# # #     }
# # #     .stApp {
# # #         padding-bottom: 70px; /* Adjust based on input box height */
# # #     }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True
# # # )

# # # st.title("Your Chat App")
# # # st.markdown("<small>Press send to generate a response</small>", unsafe_allow_html=True)

# # # # Initialize message history
# # # if "messages" not in st.session_state:
# # #     st.session_state.messages = []

# # # # Show messages (newest at the top)
# # # for msg in reversed(st.session_state.messages):
# # #     with st.chat_message(msg["role"]):
# # #         st.markdown(msg["content"])

# # # # Sticky input at the bottom using the custom class
# # # user_input = st.text_input("Type your message:", key="user_input", label_visibility="hidden")

# # # if st.button("Send", key="send_button"):
# # #     if user_input:
# # #         st.session_state.messages.append({"role": "user", "content": user_input})

# # #         # Send to Groq API
# # #         response = client.chat.completions.create(
# # #             model="mixtral-8x7b-32768",  # Use a valid model name
# # #             messages=[{"role": "user", "content": user_input}]
# # #         )

# # #         # Fix response parsing
# # #         bot_response = response.choices[0].message.content
# # #         st.session_state.messages.append({"role": "assistant", "content": bot_response})

# # #         # Rerun to update chat
# # #         st.rerun()

# # import streamlit as st
# # from groq import Groq

# # # Set API Key
# # GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# # client = Groq(api_key=GROQ_API_KEY)

# # st.title("Ask anything")

# # # Initialize message history
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # # Show messages in order (newest at the bottom)
# # for msg in st.session_state.messages:
# #     with st.chat_message(msg["role"]):
# #         st.markdown(msg["content"])

# # # Sticky input box at the bottom
# # user_input = st.chat_input("Type your message...")

# # if user_input:
# #     st.session_state.messages.append({"role": "user", "content": user_input})

# #     # Send to Groq API
# #     response = client.chat.completions.create(
# #         model="mixtral-8x7b-32768",  # Use a valid model name
# #         messages=[{"role": "user", "content": user_input}]
# #     )

# #     # Fix response parsing
# #     bot_response = response.choices[0].message.content
# #     st.session_state.messages.append({"role": "assistant", "content": bot_response})

# #     # Rerun app to update chat
# #     st.rerun()

# import streamlit as st
# from groq import Groq

# # Apply custom CSS
# st.markdown("""
#     <style>
#         /* Full dark mode chat UI */
#         body {
#             background-color: #121212;
#             color: #EAEAEA;
#         }
#         .stChatMessage {
#             background: #181818;
#             padding: 10px;
#             border-radius: 8px;
#             margin-bottom: 5px;
#         }
#         .stChatMessageUser {
#             background: #1DB954;
#             color: white;
#             padding: 10px;
#             border-radius: 8px;
#             margin-bottom: 5px;
#         }
#         .stChatMessageAssistant {
#             background: #333;
#             padding: 10px;
#             border-radius: 8px;
#             margin-bottom: 5px;
#         }
#         /* Sticky input box */
#         div[data-testid="stChatInput"] {
#             position: fixed;
#             bottom: 0;
#             width: 100%;
#             background: #121212;
#             padding: 10px;
#             box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.2);
#             z-index: 1000;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Set API Key
# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
# client = Groq(api_key=GROQ_API_KEY)

# st.title("💬 Ask anythin")

# # Initialize message history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # Fixed input box at bottom
# user_input = st.chat_input("Type your message...")

# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})

#     # Send to Groq API
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{"role": "user", "content": user_input}]
#     )

#     # Process response
#     bot_response = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": bot_response})

#     st.rerun()

import streamlit as st
from groq import Groq

# Apply custom CSS
st.markdown("""
    <style>
        /* Full dark mode chat UI */
        body {
            background-color: #121212;
            color: #EAEAEA;
        }
        .stChatMessage {
            background: #181818;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .stChatMessageUser {
            background: #1DB954;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        .stChatMessageAssistant {
            background: #333;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
        /* Sticky input box (Centered with margin-bottom) */
        div[data-testid="stChatInput"] {
            position: fixed;
            bottom: 20px; /* 20px margin from bottom */
            left: 50%;
            transform: translateX(-50%);
            width: 80%; /* Adjust width as needed */
            max-width: 600px; /* Prevent it from stretching too wide */
            background: #222;
            padding: 12px;
            border-radius: 8px;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.2);
            z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# Set API Key
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

st.title("💬 Ask anything:)")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Fixed input box at bottom (centered)
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking... 💭"):
      
    # Send to Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_input}]
        )

    # Process response
    bot_response = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    st.rerun()
