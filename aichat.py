print("🤖 AI Chatbot")
print("Type 'bye' to exit.")

while True:
    you = input("You: ").lower()

    if you == "hello" or you == "hi":
        print("Bot: Hello! How can I help you?")

    elif you =="python":
        print("Bot: Python is a popular programming language.")

    elif you == "java":
        print("Bot: Java is an object-oriented programming language.")

    elif you == "ai" or you == "artificial intelligence":
        print("Bot: AI means Artificial Intelligence.")

    elif you == "how are you":
        print("Bot: I am doing great! 😊")

    elif you == "your name":
        print("Bot: I am your AI Chatbot.")

    elif you == "bye":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")