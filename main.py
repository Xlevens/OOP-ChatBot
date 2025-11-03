# main.py

from Modules.interface import Interface
from Modules.Khaadi import KhaadiChat

def main():
    print("👋 Welcome to Khaadi Chat Support!\n")

    # Step 1: Get user info
    name = input("Please enter your name: ").strip()
    contact = input("Please enter your contact number: ").strip()
    order = input("Please enter your order ID: ").strip()

    # Step 2: Create Interface object (user info)
    user = Interface(name, contact, order)
    print("\n✅ User info registered:")
    user.ordercheck()
    print(user)
    print(user.orderstatus())

    print("\n--- Starting chat ---\n")

    # Step 3: Create chatbot object
    bot = KhaadiChat(user.name)

    # Show welcome message from bot
    print(bot.response())

    # Step 4: Chat loop
    while True:
        query = input("You: ").strip()

        # Exit condition
        if query.lower() in ["exit", "quit", "bye"]:
            print("IBOT: Chat ended. Goodbye! 👋")
            break

        # Set user query in chatbot
        bot.chatbot_response(query)

        # Print bot response
        print(bot)

        # Optional: end chat if the user says goodbye
        if any(word in query.lower() for word in ["goodbye", "bye", "thanks"]):
            print("IBOT: Chat ended. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
