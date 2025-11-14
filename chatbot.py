import random


def simple_chatbot():
    """
    A simple, rule-based chatbot with a 'help' command.
    """
    # Updated greeting to mention 'help'
    print("Bot: Hello! I'm a simple chatbot. Ask me something, type 'help' for options, or 'bye' to quit.")

    while True:
        user_input = input("You: ").lower()

        # --- Define the rules ---

        # 1. Exit condition
        if user_input == "bye" or user_input == "quit":
            print("Bot: Goodbye! Have a great day.")
            break

        # 2. Greetings
        elif "hello" in user_input or "hi" in user_input:
            # Using random.choice to make it more interesting
            responses = ["Hello there! How can I help you?", "Hi! What's up?", "Hey!"]
            print(f"Bot: {random.choice(responses)}")

        # 3. How are you?
        elif "how are you" in user_input:
            print("Bot: I'm just a bunch of code, but I'm running perfectly!")

        # 4. What is your name?
        elif "your name" in user_input:
            print("Bot: You can call me 'Assignment Bot 1.0'.")

        # 5. Ask about the weather
        elif "weather" in user_input:
            print("Bot: I'm sorry, I can't check the real weather. It's always sunny in my code!")

        # 6. --- NEW HELP COMMAND ---
        elif "help" in user_input:
            print("Bot: Sure! You can ask me things like:")
            print("* 'hello' or 'hi'")
            print("* 'how are you'")
            print("* 'what is your name'")
            print("* 'weather'")
            print("* 'bye' (to quit)")

        # 7. Default fallback response
        else:
            # Updated fallback to suggest 'help'
            print("Bot: I'm sorry, I don't understand that. Try typing 'help' to see what I can do.")


# --- Run the chatbot ---
if __name__ == "__main__":
    simple_chatbot()