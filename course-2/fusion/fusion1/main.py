# In this activity, students will build 
# an interactive Text-to-Image Generator 
# that takes textual descriptions (prompts) 
# as input and generates corresponding images 
# using the Hugging Face API with the Stable 
# Diffusion model. The tool will allow users 
# to generate creative artwork from simple 
# descriptions, explore the potential of AI 
# in creative fields, and understand how machine 
# learning models process and generate images based on text.
from tkinter import Image
import requests
from conflg import hf_api_key
from PIL import Image
import io
# Api key
base_url = "https://router.huggingface.co/hf-inference/models"
model = "black-forest-labs/FLUX.1-schnell"
api_url = base_url + "/" + model

# Functions
if __name__ == "__main__":
    prompt = input("Enter a description for the image you want to generate: ")
    headers = {
        "Authorization": f"Bearer {hf_api_key}"
    }
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
        else:
            # Converting the response to a image
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image.show()
            image.save('mypic.png')
    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
