def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        return "Bot: Hi! Nice to meet you."

    elif user_input == "how are you":
        return "Bot: I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "Bot: I'm a simple Python chatbot."

    elif user_input == "help":
        return "Bot: You can say hello, ask how I am, ask my name, or say bye."

    elif user_input == "what can you do":
        return "Bot: I can chat with you and answer simple questions."

    elif user_input == "what is python":
        return "Bot: Python is a high-level, interpreted programming language known for its simplicity and readability."

    elif user_input == "bye":
        return "Bot: Goodbye! Have a great day!"

    else:
        return "Bot: Sorry, I don't understand that."


def chatbot():
    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)
    print("Type 'bye' anytime to exit.")
    print()

    conversation_history = []

    while True:
        user_input = input("You: ").lower().strip()

        conversation_history.append(user_input)

        response = get_response(user_input)
        print(response)

        conversation_history.append(response)


        if user_input == "bye":
            break

    print()
    print("=" * 40)
    print("       CONVERSATION HISTORY")
    print("=" * 40)

    for message in conversation_history:
        print(message)

chatbot()