import openai

# Set your OpenAI API key
openai.api_key = "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"

def chat_with_chatgpt():
    print("ChatGPT: Hi! I'm your chatbot. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatGPT: Bye! Have a great day!")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can use "gpt-3.5-turbo" if preferred
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7
            )
            chatbot_reply = response['choices'][0]['message']['content']
            print(f"ChatGPT: {chatbot_reply}")
        except Exception as e:
            print(f"ChatGPT: Sorry, there was an error: {e}")

if __name__ == "__main__":
    chat_with_chatgpt()
