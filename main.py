import sys
import os

# Add the local 'lib' folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

import google.genai as genai
from google.genai import errors

# Your Google AI API key
api_key = input("Please enter a valid Google AI API key: ")

try:
    # Create client
    client = genai.Client(api_key=api_key)

    # Make a lightweight test call (generate very short content)
    test_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hi"
    )

    print("\nAPI key is valid! Starting chat...")

except errors.APIError as e:
    print("\n", e.message)

# Create the client
client = genai.Client(api_key=api_key)

# Start a chat session that remembers previous messages
chat = client.chats.create(model="gemini-2.5-flash")

print("\nType 'exit' to quit the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send message to chat session
    response = chat.send_message(user_input)

    # AI reply
    print("AI:", response.text)