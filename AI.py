import streamlit as st
from groq import Groq

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Stable AI Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Stable ChatGPT Clone (No Model Errors)")

# -------------------------
# API Key
# -------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -------------------------
# Stable model list (fallback system)
# -------------------------
MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

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
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = None
    last_error = None

    # -------------------------
    # Try multiple models (AUTO FIX)
    # -------------------------
    for model in MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages
            )

            reply = response.choices[0].message.content
            break

        except Exception as e:
            last_error = str(e)
            continue

    # -------------------------
    # Show result or error
    # -------------------------
    if reply:
        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)
    else:
        st.error(f"All models failed. Last error: {last_error}")
