import streamlit as st
from openai import OpenAI

# Replace with your real OpenAI API key
API_KEY = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=API_KEY)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
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
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

    except Exception as e:
        st.error(e)
