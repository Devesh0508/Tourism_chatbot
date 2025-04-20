# chatbot.py
pip install nltk

import nltk
from nltk.tokenize import word_tokenize

class ChatBot:
    def __init__(self):
        # Predefined responses for specific user inputs
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "help": "Sure! I can help you with tourist information, flight details, or hotel bookings. What would you like to know?",
            "paris": "Paris is known for its Eiffel Tower, Louvre Museum, and amazing food. Do you want to know more?",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()  # Convert to lowercase to standardize
        for keyword, response in self.responses.items():
            if keyword in user_input:
                return response
        return "Sorry, I didn't understand that. Could you please clarify?"

# Example usage
if __name__ == "__main__":
    bot = ChatBot()
    print("ChatBot: Hello! I'm your tourism assistant.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"ChatBot: {response}")


# Download NLTK tokenizer
nltk.download('punkt')


# Example usage
if __name__ == "__main__":
    bot = ChatBot()
    print("ChatBot: Hello! I'm your tourism assistant.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"ChatBot: {response}")

class ChatBot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "help": "Sure! I can help you with tourist information, flight details, or hotel bookings.",
            "paris": "Paris is known for the Eiffel Tower, Louvre Museum, and amazing food. Do you want to know more?",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, user_input):
        # Tokenize and normalize input
        tokens = word_tokenize(user_input.lower())
        for keyword, response in self.responses.items():
            if keyword in tokens:
                return response
        return "Sorry, I didn't understand that. Could you clarify?"

