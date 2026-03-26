# In this After Class Project, you build an
# AI-powered message classifier that detects spam messages. 
# Using a Hugging Face model, your program analyzes text and 
# classifies messages as “Spam” or “Safe,” helping 
# you understand how AI protects users from harmful or misleading messages.
from conflg import hf_api_key
import requests

# Define the API endpoint and headers for Hugging Face
base_url = "https://router.huggingface.co/hf-inference/models"
model = "facebook/bart-large-mnli"
api_url = base_url + "/" + model

headers = {
    "Authorization": f"Bearer {hf_api_key}",
    "Content-Type": "application/json"
}

def classify_message(message):
    payload = {
        "inputs": message,
        "parameters": {
            "candidate_labels": ["scam", "fraud", "spam", "legitimate", "safe"]
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)
    
    try:
        result = response.json()
    except:
        return "error", "Invalid response from API"

    if isinstance(result, dict) and "labels" in result and "scores" in result:
        return result["labels"][0], result["scores"][0]
    elif isinstance(result, list) and len(result) > 0:
        sorted_result = sorted(result, key=lambda x: x["score"], reverse=True)
        return sorted_result[0]["label"], sorted_result[0]["score"]
    else:
        return "error", result
    


# Main program
print("AI Message Classifier")
print("This tool analyzes messages and classifies them as Spam or Safe.")

while True:
    user_input = input("\nEnter a message to analyze (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    label, score = classify_message(user_input)

    if label == "error":
        print("Error:", score)
    else:
        if label == "spam":
            print(f"Result: Spam (Confidence: {score:.2f})")
        else:
            print(f"Result: Safe (Confidence: {score:.2f})")

