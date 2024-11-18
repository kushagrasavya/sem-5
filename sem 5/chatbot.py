def chatbot_response(user_input):
    # Predefined rules for responses
    rules = {
        "hello": "Hi! How can I help you today?",
        "how are you": "I'm just a chatbot, but I'm doing well. How about you?",
        "bye": "Goodbye! Have a great day!",
        "your name": "I am a chatbot created by OpenAI.",
        "default": "I'm sorry, I don't understand that. Can you ask something else?"
    }
    
    # Normalize input to lowercase
    user_input = user_input.lower()

    # Match input to a rule
    for key in rules:
        if key in user_input:
            return rules[key]
    
    # Default response for unmatched input
    return rules["default"]

# Example interaction
print("Chatbot: Hello! I am your friendly chatbot. Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", chatbot_response(user_input))
        break
    print("Chatbot:", chatbot_response(user_input))
