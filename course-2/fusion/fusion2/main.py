# In this activity, you'll generate an image 
# using a text-to-image model (Stable Diffusion) 
# and then enhance it with post-processing techniques. 
# The session focuses on applying practical image 
# adjustments such as increasing brightness,
# boosting contrast, and adding a soft-focus effect 
# with Gaussian blur. Using Python libraries like Pillow, 
# you'll learn how to transform raw AI-generated images 
# into polished artworks, highlighting the impact of subtle 
# adjustments on the overall visual quality. 
# Enjoy exploring how post-processing can refine and elevate your creative output!
import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from conflg import hf_api_key
from colorama import Style, Fore


# A list of fallback models
MODELS = [
    "black-forest-labs/FLUX.1-dev",
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
]

#"Authorization" → proves you’re allowed to use API
#"Accept": "image/png"}"Accept": "image/png" → tells API you want an image
HEADERS = {
    "Authorization": f"Bearer {hf_api_key}",
    "Accept": "image/png"
}

def generate_image(prompt):
    payload, last_err = {"inputs": prompt}, None
    for model in MODELS:
        url = f"https://router.huggingface.co/hf-inference/models/{model}"
        #Try each model 3 times - Helps handle temporary failure
        for i in range(3):
            try:
                response = requests.post(url, headers=HEADERS, json=payload,timeout=120)
                # checking if response has a image or an error
                ct = (response.headers.get("content-type") or "").lower()
                if response.status_code == 503:
                    print(f"{Fore.YELLOW}Model {model} is loading, retrying...{Style.RESET_ALL}")
                    wait_s = int(response.json().get("estimated_time", 5))
                    time.sleep(wait_s)
                elif response.status_code == 200:
                    #return Image.open(BytesIO(r.content)).convert("RGB"
                    return Image.open(BytesIO(response.content)).convert("RGB")
                else:
                    last_err = f"Error {response.status_code}: {response.text}"
                    break
            except Exception as e:
                last_err = str(e)
                break
    raise Exception(f"All models failed. Last error: {last_err}")
    

if __name__ == "__main__":
    print(f"{Fore.GREEN}Welcome to the Text-to-Image Generator with Post-Processing!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}This program generates an image from text and applies post-processing effects.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'exit' to quit.{Style.RESET_ALL}\n")
    while True:
        user_input = input(f"{Fore.BLUE}Enter a description for the image you want to generate: {Style.RESET_ALL}").strip()
        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.MAGENTA}Generating image...{Style.RESET_ALL}")
            img = generate_image(user_input)
            print(f"{Fore.MAGENTA}Applying post-processing...{Style.RESET_ALL}")
            if img:
                print(f"{Fore.GREEN}✓ Image generated successfully!{Style.RESET_ALL}")
                img.show(title="ORIGINAL IMAGE GENERATED")
                enh_img = input(f"{Fore.BLUE}Do you want to enhance the image? (y/n): {Style.RESET_ALL}").strip().lower()
                if enh_img == "y":
                    img_enh = ImageEnhance.Brightness(img).enhance(1.2)
                    img_enh = ImageEnhance.Contrast(img_enh).enhance(1.3)
                    img_enh.show(title="ENHANCED IMAGE")
                    save_img = input(f"{Fore.BLUE}Do you want to save the enhanced image? (y/n): {Style.RESET_ALL}").strip().lower()
                    if save_img == "y":
                        filename = f"enhanced_{int(time.time())}.png"
                        img_enh.save(filename)
                        print(f"{Fore.GREEN}✓ Enhanced image saved as {filename}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}Skipping save.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}Skipping enhancement.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ Failed to generate image.{Style.RESET_ALL}")
