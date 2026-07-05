import streamlit as st
from groq import Groq

# -------------------------
# Page setup
# -------------------------
st.set_page_config(
    page_title="ChatGPT Clone (Free)",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ChatGPT Clone (Free with Groq)")

# -------------------------
# Load API key from secrets
# -------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -------------------------
# Session memory
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Show chat history
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# User input
# -------------------------
prompt = st.chat_input("Type your message...")

if prompt:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # -------------------------
        # Groq API call (UPDATED MODEL)
        # -------------------------
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=st.session_state.messages
        )

        reply = response.choices[0].message.content

        # Save assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Error: {e}")
