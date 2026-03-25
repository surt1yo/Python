# Build a complete, interactive news
# topic classifier that takes any headline 
# from the user, sends it to the Hugging 
# Face API, and displays which topic it 
# belongs to with a visual confidence bar. 
# This is the same technology used by major news organizations!
from cProfile import label
from conflg import hf_api_key
import requests

# Define the API endpoint and headers for Hugging Face
base_url = "https://router.huggingface.co/hf-inference/models"
model = "facebook/bart-large-mnli"
api_url = base_url + "/" + model
TOPICS = ["Sports", "Technology", "Business", "Politics", "Health"]
headers = {"Authorization": f"Bearer {hf_api_key}"}

def BART_model(headline: str):
    payload = {
        "inputs": headline,
        "parameters": {
            "candidate_labels": TOPICS
        }
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        print(f"Result: {result[0]}")
    else:
        print("Error occurred while fetching the API response.")

headline = input("Headline: ")
if not headline.strip():
    print("Please enter a valid headline.")
else:
    BART_model(headline)

