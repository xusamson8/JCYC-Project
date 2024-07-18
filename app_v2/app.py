import os
import random
from webscraper import scrape, extract_info, extract_from_links
from google.cloud import dialogflow
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Set the path to your service account key file
key_file_path = '/Users/samsonxu/Downloads/ofa-chatbot-45dbb77a9825.json' 

# Hadrian File Path: r'C:\Users\lkuc3\Downloads\ofa-chatbot-36bcf1d0cb1d.json'

# Set Google Cloud Project ID and Session ID
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
project_id = 'ofa-chatbot'
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
        return response.query_result
    except Exception as e:
        return f"Error: {e}"

# Main interaction loop
def main():
    print("Welcome to the OFA Terminal Chatbot! Ask about FAQs, programs, and more!")
    print("Type 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Send user input to Dialogflow and get response
        query_result = detect_intent_texts(user_input)

        # Check if an error occurred
        if isinstance(query_result, str) and query_result.startswith("Error:"):
            print(f"Bot: {query_result}")
            continue

        # Get the intent name
        intent_name = query_result.intent.display_name
        fulfillment_text = query_result.fulfillment_text

        # Handle custom intents
        if intent_name == 'scrape_website':
            url = 'https://opps4allsfsummer.org/csi-tech-home'
            try:
                soup = scrape(url)
                title, links, text = extract_info(soup)
                linked_websites_info = extract_from_links(url, links)
                response_text = f"Title: {title}\nText: {text}\nLinks: {links[:5]}"
                print(f"Bot: {response_text}")
            except Exception as e:
                print(f"Error: {e}")

        elif intent_name == 'about':
            responses = [
                "This is an SF-based program that matches youth to internships to gain work experience.",
                "Our program in San Francisco helps youth find internships for valuable work experience.",
                "We offer a program in SF that connects young people with internship opportunities to build their careers."
            ]
            response_text = random.choice(responses)
            print(f"Bot: {response_text}")

        elif intent_name == 'Programs':
            # Access pre-defined fulfillment text from Dialogflow response
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'health':
            # Access pre-defined fulfillment text from Dialogflow response
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'art':
            # Access pre-defined fulfillment text from Dialogflow response
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'civic':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'culinary':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'environment':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'education':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'legal':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'engineering':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'market':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'travel':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'entrepreneurship':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'business':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        elif intent_name == 'communications':
            response_text = query_result.fulfillment_text
            print(f"Bot: {response_text}")
        else:
            print(f"Bot: {fulfillment_text}")

if __name__ == '__main__':
    app.run(Debug=True)

# flask
# setuptools
# google-cloud-dialogflow