# Students will build and run a Python program that 
# sends an image to Hugging Face’s facebook/detr-resnet-50 
# model and gets back object detections. They’ll visualize 
# the results with bounding boxes and fun emojis using Pillow. 
# The activity demonstrates how cloud AI + Python work 
# together to create real-world computer vision applications.
from importlib.resources import path
import os, io, time, random, requests, mimetypes, random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from conflg import hf_api_key
from colorama import Style, Fore


# Api key
model = "facebook/detr-resnet-101"
api = f"https://router.huggingface.co/hf-inference/models/{model}"

# Supported image formats
format, MAX_MB = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
emoji = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",
         "bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",
         "apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

# Function to generate a unique filename
def ask_image():
    print(f"{Fore.CYAN}\n🎯 Pick an image (JPG/PNG/WebP/BMP/TIFF ≤ 8MB) from this folder.{Style.RESET_ALL}")
    while True:
        path = input(f"{Fore.YELLOW}Enter image path: {Style.RESET_ALL}").strip('"').strip("'")
        # Check if file exists
        if not os.path.isfile(path):
            print(f"{Fore.RED} File not found. Try again.{Style.RESET_ALL}")
        # Check file type
        if not path.endswith((".jpg", ".png", ".jpeg")):
            print(f"{Fore.RED}Only JPG or PNG allowed.{Style.RESET_ALL}")
            continue
        # Check size (max 8MB)
        size = os.path.getsize(path) / (1024 * 1024)
        if size > 8:
            print(f"{Fore.RED}File too big (max 8MB).{Style.RESET_ALL}")
            continue
        try:
            img = Image.open(path)
            img.verify()
        except:
            print(f"{Fore.RED}Invalid image file.{Style.RESET_ALL}")
            continue
        print(f"{Fore.GREEN}Image accepted!{Style.RESET_ALL}")
        return path
def infer(path, img_bytes, tries=8):
    response = requests.post(api, data=img_bytes, headers={
        "Authorization": f"Bearer {hf_api_key}", 
        "Content-Type": mimetypes.guess_type(path)[0]}, 
        timeout=60)
    if response.status_code == 200:
        return response.json()   # success
    elif response.status_code == 503:
        print(f"{Fore.YELLOW}Busy... trying again{Style.RESET_ALL}")
        time.sleep(2)

    print(f"{Fore.RED}Failed to get result{Style.RESET_ALL}")
    return None

# Draw boxes
def draw_boxes(path, result):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    # Load a font (change path if needed)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    for obj in result:
        box = obj["box"]
        label = emoji.get(obj["label"], obj["label"])
        x1 = box["xmin"]
        y1 = box["ymin"]
        x2 = box["xmax"]
        y2 = box["ymax"]
        draw.rectangle([x1, y1, x2, y2], outline=random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown","cyan","magenta"]), width=3)
        draw.text((x1, y1), label, fill="red")
    img.show()

    
if __name__ == "__main__":
    path = ask_image()
    with open(path,"rb") as f:
        img_bytes = f.read()
    result = infer(path, img_bytes)
    print("Result:", result)
    if result is not None:
       print("Objects found:", result)
       draw_boxes(path, result)
    else:
        print(f"{Fore.RED}Inference failed after multiple attempts.{Style.RESET_ALL}")