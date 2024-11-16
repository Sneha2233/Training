import openai

# Set your OpenAI API key
openai.api_key = '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'

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
