import streamlit as st
from groq import Groq

# -----------------------
# Setup
# -----------------------
st.set_page_config(page_title="Free ChatGPT Clone", page_icon="🤖", layout="centered")

st.title("🤖 Free ChatGPT Clone (Groq)")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -----------------------
# Memory
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Show chat
# -----------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------
# Input
# -----------------------
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
       response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=st.session_state.messages
)
        reply = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Error: {e}")
