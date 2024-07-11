import os
import random
from webscraper import scrape, extract_info, extract_from_links
from google.cloud import dialogflow

# Set the path to your service account key file
key_file_path = r'C:\Users\Spongebob\Downloads\ofa-chatbot-9ecc385d862d.json'

# Set Google Cloud Project ID and Session ID
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
project_id = 'your-project-id'
session_id = 'unique-session-id'

# Create a session client
session_client = dialogflow.SessionsClient()

# Function to detect intent and get response from Dialogflow
def detect_intent_texts(text):
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code="en-US")
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except Exception as e:
        return f"Error: {e}"

# Main interaction loop
def main():
    print("Welcome to the Dialogflow Terminal Chatbot!")
    print("Type 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Send user input to Dialogflow and get response
        response = detect_intent_texts(user_input)

        # Handle custom intents
        if response.startswith('SCRAPE_'):
            intent, url = response.split('_', 1)
            try:
                soup = scrape(url)
                title, text = extract_info(url, soup)
                linked_websites_info = extract_from_links(url, [a['href'] for a in soup.find_all('a', href=True)])
                print(f"Bot: Title: {title}\nText: {text}")
                for info in linked_websites_info:
                    print(f"Linked Website: {info['url']}\nTitle: {info['title']}\nText: {info['text']}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"Bot: {response}")

if __name__ == '__main__':
    main()
