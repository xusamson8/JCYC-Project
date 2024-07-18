import os
import random
from flask import Flask, request, render_template, jsonify
from google.cloud import dialogflow
# from webscraper import scrape, extract_info, extract_from_links

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    query_result = detect_intent_texts(user_input)

    if isinstance(query_result, str) and query_result.startswith("Error:"):
        return jsonify({"response": query_result})

    intent_name = query_result.intent.display_name
    fulfillment_text = query_result.fulfillment_text

    if intent_name == 'about':
        responses = [
            "This is an SF-based program that matches youth to internships to gain work experience.",
            "Our program in San Francisco helps youth find internships for valuable work experience.",
            "We offer a program in SF that connects young people with internship opportunities to build their careers."
        ]
        response_text = random.choice(responses)

    elif intent_name == 'Programs':
        response_text = fulfillment_text

    elif intent_name == 'health':
        response_text = fulfillment_text

    elif intent_name == 'art':
        response_text = fulfillment_text

    elif intent_name == 'civic':
        response_text = fulfillment_text

    elif intent_name == 'culinary':
        response_text = fulfillment_text

    elif intent_name == 'environment':
        response_text = fulfillment_text

    elif intent_name == 'education':
        response_text = fulfillment_text

    elif intent_name == 'legal':
        response_text = fulfillment_text

    elif intent_name == 'engineering':
        response_text = fulfillment_text

    elif intent_name == 'market':
        response_text = fulfillment_text

    elif intent_name == 'travel':
        response_text = fulfillment_text

    elif intent_name == 'entrepreneurship':
        response_text = fulfillment_text

    elif intent_name == 'business':
        response_text = fulfillment_text

    elif intent_name == 'communications':
        response_text = fulfillment_text

    else:
        response_text = fulfillment_text

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True, port = 8000)