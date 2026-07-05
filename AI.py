import streamlit as st
from openai import OpenAI

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

# -------------------------
# Load API key from secrets
# -------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
        # Call OpenAI
        response = client.responses.create(
            model="gpt-4o-mini",
            input=st.session_state.messages
        )

        reply = response.output_text

        # Save assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Error: {e}")
