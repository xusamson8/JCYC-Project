import os
import openai
import json


openai.api_key = 'insert OPENAI API key'


def load_faqs(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_response(question, faqs):
    for faq in faqs:
        if question.lower() in faq['question'].lower():
            return faq['answer']
    return "Sorry, I don't have an answer for that question."

def ask_openai(question, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about the Japanese Community Youth Council San Francisco California. Please Limit Tokens to 50"},
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ],
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()

def chatbot():
    faqs = load_faqs('jcyc-faq-data.json')  
    context = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faqs])

    print("Welcome to the San Francisco JCYC FAQ chatbot! Ask me questions about JCYC!")
    while True:
        user_question = input("You: ")
        if user_question.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        response = generate_response(user_question, faqs)
        if "Sorry" in response:
            response = ask_openai(user_question, context)
        print(f"AI: {response}")

if __name__ == "__main__":
    chatbot()