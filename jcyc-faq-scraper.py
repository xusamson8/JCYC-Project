import requests
from bs4 import BeautifulSoup
import json

url = 'https://jcyc.org/about-us/faqs-frequently-asked-questions/'

# GET request to the URL and get the response
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the page content") #debug
else:
    print(f"Failed to fetch the page content. Status code: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

JCYC_FAQS = []

# find all question elements using h5 tag, (their class names are weird)
question_elements = soup.find_all('h5')

# Loop through each question element
for question_element in question_elements:
    # Extract the text of the question
    question = question_element.get_text(strip=True)
    
    # # Debug: print the question text for 
    # print(f"Question: {question}")

    # Find the next sibling element that contains the answer
    answer_element = question_element.find_next_sibling('p')
    
    if answer_element:
        # extract answer test
        answer = answer_element.get_text(strip=True)
        
        # # Debug: print the answer text
        # print(f"Answer: {answer}")

        # add to list
        JCYC_FAQS.append({'question': question, 'answer': answer})

    # else:
    #     # Debug: print if answer element is not found
    #     print(f"No answer found for question: {question}")

# # Debug: print FAQs to verify
# print(f"FAQs extracted: {JCYC_FAQS}")

# Save the list of FAQs to a JSON file if there are any FAQs
if JCYC_FAQS:
    with open('jcyc-faq-data.json', 'w') as f:
        json.dump(JCYC_FAQS, f, indent=4)
    print(f"FAQs successfully saved to faqs.json")
else:
    print("No FAQs found to save.")
