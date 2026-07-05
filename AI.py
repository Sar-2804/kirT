from openai import OpenAI

# ==========================
# Configuration
# ==========================
API_KEY = "YOUR_OPENAI_API_KEY"

client = OpenAI(api_key=API_KEY)

print("=" * 50)
print("🤖 AI Chatbot")
print("Type 'exit' to quit.")
print("=" * 50)

conversation = []

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=conversation
        )

        bot_reply = response.output_text

        print("\nBot:", bot_reply)

        conversation.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

    except Exception as e:
        print("Error:", e)
