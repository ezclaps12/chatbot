import google.generativeai as genai


# --- IMPORTANT: PASTE YOUR API KEY HERE ---
# (Or set it as an environment variable for better security)
YOUR_API_KEY = "AIzaSyCEHP0K36JiNHqH1e8e6VWLeqm0Wlj46oI"

try:
    genai.configure(api_key=YOUR_API_KEY)
except Exception as e:
    print(f"Error: Could not configure the API. Check your API key. {e}")
    exit()

# Configuration for the model
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    generation_config=generation_config
)


def llm_chatbot():
    """
    A chatbot that uses the Gemini LLM via an API call.
    """

    # Start a chat session (this allows it to remember history)
    chat = model.start_chat(history=[])

    print("Bot: Hello! I'm an LLM chatbot. Ask me anything, or type 'bye' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye" or user_input == "quit":
            print("Bot: Goodbye! Have a great day.")
            break

        try:
            # --- This is the API Call ---
            # Send the user's message to the model
            response = chat.send_message(user_input)

            # Print the text part of the response
            print(f"Bot: {response.text}")

        except Exception as e:
            print(f"Error: Failed to get a response from the API. {e}")


# --- Run the chatbot ---
if __name__ == "__main__":
    llm_chatbot()
