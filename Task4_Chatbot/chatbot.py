# CodeAlpha Internship - Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Nice to meet you!"

    elif "how are you" in user_input:
        return "I am doing great! How can I help you?"

    elif "your name" in user_input:
        return "I am CodeAlpha Chatbot."

    elif "help" in user_input:
        return "I can respond to greetings and simple questions."

    elif "thank" in user_input:
        return "You're welcome!"

    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


print("================================")
print("        BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if "bye" in user_input.lower():
        break

print("\nChatbot ended.")
