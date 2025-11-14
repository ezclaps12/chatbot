import google.generativeai as genai



YOUR_API_KEY = "AIzaSyCEHP0K36JiNHqH1e8e6VWLeqm0Wlj46oI"

try:
    genai.configure(api_key=YOUR_API_KEY)
except Exception as e:
    print(f"Error: Could not configure the API. Check your API key. {e}")
    exit()


generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}


model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    generation_config=generation_config
)


def llm_chatbot():
    """
    A chatbot that uses the Gemini LLM via an API call.
    """


    chat = model.start_chat(history=[])

    print("Bot: Hello! I'm an LLM chatbot. Ask me anything, or type 'bye' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye" or user_input == "quit":
            print("Bot: Goodbye! Have a great day.")
            break

        try:
         
            response = chat.send_message(user_input)

            print(f"Bot: {response.text}")

        except Exception as e:
            print(f"Error: Failed to get a response from the API. {e}")


# --- Run the chatbot ---
if __name__ == "__main__":
    llm_chatbot()

