
print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
	user = input("You: ").lower()

	if user == "hello" or user == "hi":
		print("Bot: Hello! How can I help you?")

	elif user == "how are you":
		print("Bot: I am fine. Thank you!")

	elif user == "your name":
		print("Bot: My name is AI Chatbot.")

	elif user == "bye":
		print("Bot: Goodbye!")
		break

	else:
		print("Bot: Sorry, I don't understand that.")
