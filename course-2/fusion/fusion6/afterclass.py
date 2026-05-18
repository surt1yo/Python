# Students will apply AI-powered tools to
# generate captions, descriptions, and summaries 
# from images. By expanding on a simple image caption, 
# they will utilize a text generation model 
# (GPT-2) and a text-to-image model (Stable Diffusion) 
# to create a complete, interactive workflow 
# for text-to-image conversion. They will practice 
# generating descriptive text, summarizing the 
# content, and exploring creative applications.
import requests
import json
from conflg import hf_api_key
import time
from colorama import Fore, Style

caption_model = "Salesforce/blip-image-captioning-base"
text_model = "gpt2"
image_model = "stabilityai/stable-diffusion-2"

headers = {
    "Authorization": f"Bearer {hf_api_key}",
    "Content-Type": "application/json"
}


def query_hf_api(model, data, is_binary=False):
    url = f"https://router.huggingface.co/hf-inference/models/{model}"

    if is_binary:
        local_headers = {
            "Authorization": f"Bearer {hf_api_key}"
        }
        response = requests.post(url, headers=local_headers, data=data)
    else:
        local_headers = {
            "Authorization": f"Bearer {hf_api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=local_headers, json=data)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    return response.content if is_binary else response.json()


def generate_caption(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    result = query_hf_api(caption_model, image_bytes, is_binary=True)
    result_json = json.loads(result.decode("utf-8"))

    return result_json[0]["generated_text"]


def generate_text(prompt, max_length=50):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "temperature": 0.7
        }
    }

    result = query_hf_api(text_model, payload)
    return result[0]["generated_text"]


def generate_image(prompt, output_file="generated.png"):
    payload = {
        "inputs": prompt
    }

    image_bytes = query_hf_api(image_model, payload, is_binary=True)

    with open(output_file, "wb") as f:
        f.write(image_bytes)

    return output_file


def main():
    image_path = input(f"{Fore.YELLOW}Enter image file path: {Style.RESET_ALL}").strip()

    try:
        caption = generate_caption(image_path)
        print(f"{Fore.GREEN}\nCaption:{Style.RESET_ALL}")
        print(caption)

        print(f"{Fore.BLUE}\nOptions:{Style.RESET_ALL}")
        print(f"{Fore.BLUE}1. Expand description{Style.RESET_ALL}")
        print(f"{Fore.BLUE}2. Summarize{Style.RESET_ALL}")
        choice = input(f"{Fore.BLUE}Select option (1/2): {Style.RESET_ALL}").strip()

        if choice == "1":
            prompt = f"Expand this image caption into a detailed description: {caption}"
            text_output = generate_text(prompt, max_length=100)
        elif choice == "2":
            prompt = f"Summarize this image caption: {caption}"
            text_output = generate_text(prompt, max_length=60)
        else:
            print("Invalid choice")
            return

        print("\nGenerated Text:")
        print(text_output)

        generate_choice = input(f"{Fore.GREEN}Generate image from this text? (y/n): {Style.RESET_ALL}").strip().lower()

        if generate_choice == "y":
            output_file = generate_image(text_output)
            print(f"{Fore.GREEN}Image generated and saved as: {output_file}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()