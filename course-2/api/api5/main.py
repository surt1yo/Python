# In this lesson, students will build a Sentiment 
# Analysis Tool using Hugging Face API. They will 
# learn how to classify text into categories based
# on its sentiment (e.g., positive, negative, neutral) 
# using a pre-trained transformer model hosted by 
# Hugging Face. The lesson covers sentiment analysis, 
# understanding transformer models, and interacting with 
# Hugging Face's API using Python. By the end of the lesson, 
# students will have a fully functional sentiment analysis
# tool that they can apply to real-world use cases like 
# customer reviews, product feedback, or social media posts.
import requests
from conflg import hf_api_key

# Define the API endpoint and headers for Hugging Face
base_url = "https://router.huggingface.co/hf-inference/models"
model = "sentence-transformers/all-MiniLM-L6-v2"
api_url = base_url + "/" + model


# Functions
def check_similarity(sentence1, sentence2):
    headers = {
        "Authorization": f"Bearer {hf_api_key}"
                                                }
    payload = {
        "inputs" : {
            "source_sentence": sentence1,
            "sentences": [sentence2]
        }
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    data = response.json()[0]
    return data

# Welcome the user
print("Welcome to Sentiment Analysis!\n------------------------------------------------")
print("Sentences to compare to:\n")
q1 = input("Enter Your Sentence: ")
q2 = input("Enter Sentence to Compare To: ")


if not q1 or not q2:
    print("Please fill in the sentences.")
    print(q1,q2)
else:
    score = check_similarity(q1, q2)
    if score is None:
        print("Failed to get similarity score.")
    else:
        print(f"Similarity Score: {round(score * 100, 2)}%")
    