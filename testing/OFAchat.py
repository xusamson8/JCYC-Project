import os
import requests
from flask import Flask, request, jsonify
from webscraper import scrape, extract_info, extract_from_links
import random

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')

    intent_name = query_result.get('intent').get('displayName')

    # Handle different intents based on their unique characteristics
    if intent_name == 'scrape_website':
        url = 'https://opps4allsfsummer.org/csi-tech-home'
        soup = scrape(url)
        title, links, text = extract_info(url, soup)
        linked_websites_info = extract_from_links(url, links)
        
        response_text = f"Title: {title}\nText: {text}\nLinks: {links[:5]}"
    
    elif intent_name == 'about':
        # Provide information about the program with response variations
        responses = [
            "This is an SF-based program that matches youth to internships to gain work experience.",
            "Our program in San Francisco helps youth find internships for valuable work experience.",
            "We offer a program in SF that connects young people with internship opportunities to build their careers."
        ]
        response_text = random.choice(responses)

    elif intent_name == 'info':
        # Provide general information scraped from the website
        url = 'https://opps4allsfsummer.org/csi-tech-home'
        soup = scrape(url)
        title, links, text = extract_info(url, soup)
        
        responses = [
            f"Here's some information from our website:\n\nTitle: {title}\nText: {text}",
            f"According to our website:\n\nTitle: {title}\nText: {text}",
            f"From our site, we have:\n\nTitle: {title}\nText: {text}"
        ]
        response_text = random.choice(responses)

    elif intent_name == 'programs':
        # List the programs available by scraping the website
        url = 'https://opps4allsfsummer.org/csi-tech-home'
        soup = scrape(url)
        title, links, text = extract_info(url, soup)
        
        responses = [
            f"Here are some of the programs we offer according to our website:\n\n{text}",
            f"On our website, we list the following programs:\n\n{text}",
            f"The programs we offer include:\n\n{text}"
        ]
        response_text = random.choice(responses)

    else:
        # Default fallback response
        response_text = "I'm sorry, I didn't understand that."

    response = {
        "fulfillmentText": response_text,
        "source": "webhook"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
