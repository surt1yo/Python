# In this activity, a local image file is 
# processed through the robust 
# "nlpconnect/vit-gpt2-image-captioning" model 
# from Hugging Face. The model generates a 
# descriptive caption by analyzing visual content in the image.
import base64, requests, mimetypes, os, time, random
from colorama import Fore, Style
from PIL import Image, ImageDraw, ImageFont
from conflg import hf_api_key

# API details
url = "https://router.huggingface.co/v1/chat/completions"
headers = {"Authorization": f"Bearer {hf_api_key}", 
           "Content-Type": "application/json"}

# Functions
def caption_single_image():
    img_src = input(f"{Fore.CYAN}🖼️ Enter image filename (default: test.jpg): {Style.RESET_ALL}").strip() or "test.jpg"
    try:
        with open(img_src, "rb") as f:
            #This line converts the image file into a text format (base64) so it can be safely sent over the internet to the A
            img_bytes = base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        print(f"{Fore.RED}Error reading file: {e}{Style.RESET_ALL}")
        return
    
    # This payload is the data sent to the AI, telling it which model to use 
    # and asking it to look at the image and generate a short caption for it.
    payload = {"model":  "Qwen/Qwen3-VL-8B-Instruct", 
               "messages": [{"role": "user", 
                             "content": [{"type": "text", "text": "Give a short caption for this image."}, 
                                     {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_bytes}"}}]
                            }], 
           "max_tokens": 50} 
    api_url = "https://router.huggingface.co/v1/chat/completions"  
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        caption = data["choices"][0]["message"]["content"]
        print(caption)
        print(f"{Fore.GREEN}Caption: {caption}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
        
if __name__ == "__main__":
    caption_single_image()
        