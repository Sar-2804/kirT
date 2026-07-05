import streamlit as st
from openai import OpenAI

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

# -----------------------------
# Load API Key
# -----------------------------
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    st.error("OPENAI_API_KEY not found in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=st.session_state.messages
        )

        answer = response.output_text

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(f"Error: {e}")
