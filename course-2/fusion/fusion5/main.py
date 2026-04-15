# Use the Hugging Face Inference API to:
# Generate a basic caption from an input image. 
# Offer user options to truncate (for a short caption), 
# expand (for a 30-word description), 
# or summarize (for a 50-word summary) the caption using GPT-2.
import mimetypes
from conflg import hf_api_key
import requests, base64, os, re, time
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)

url = "https://router.huggingface.co/v1/chat/completions"
headers = {"Authorization": f"Bearer {hf_api_key}", 
           "Content-Type": "application/json"}

models = [
    "Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen3-VL-32B-Instruct:together",
    "Qwen/Qwen2.5-VL-7B-Instruct:together",
    "Qwen/Qwen2.5-VL-32B-Instruct:together",
    "Qwen/Qwen2-VL-2B-Instruct:together",
    "Qwen/Qwen2-VL-7B-Instruct:together",
]
txt_models = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "Qwen/Qwen2.5-14B-Instruct:together",
    "Qwen/Qwen2.5-32B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
    "mistralai/Mixtral-8x7B-Instruct-v0.1:together",
]

# Functions 
def _data_url(img_path):
    with open(img_path, "rb") as f:
        img_bytes = base64.b64encode(f.read()).decode("utf-8")
    mime_type, _ = mimetypes.guess_type(img_path)
    return f"data:{mime_type};base64,{img_bytes}"
    
    
def get_basic_caption(img_path: str) -> str:
    print(f"{Fore.CYAN}Generating basic caption...{Style.RESET_ALL}")
    msgs = [{
        "role": "user",
        "content": [
            {"type": "text", "text": "Write one complete sentence describing this image."},
            {"type": "image_url", "image_url": {"url": _data_url(img_path)}},
        ],
    }]
    cap, err = _run_models(models, msgs, max_tokens=90, temperature=0.2)
    if err:
        print(f"{Fore.RED}Error generating caption: {err}{Style.RESET_ALL}")
        return ""
    return cap.strip('"').strip("'").replace("\n", " ")


def query_hf_api(payload):
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"{Fore.GREEN}Model '{payload['model']}' succeeded.{Style.RESET_ALL}")
        return response.json(), None
    else:
        print(f"{Fore.YELLOW}Model '{payload['model']}' failed with status {response.status_code}.{Style.RESET_ALL}")
        return None, f"{Fore.RED}HTTP {response.status_code}: {response.text}{Style.RESET_ALL}"
def _ensure_sentence_end(text: str) -> str:
    t = (text or "").strip()
    if t and t[-1] not in ".!?":
        t += "."
    return t

def _extract_text(data) -> str:
    msg = (data or {}).get("choices", [{}])[0].get("message", {}) or {}
    return (msg.get("content") or "").strip()


def _run_models(models, messages, max_tokens=160, temperature=0.3):
    last_err = None
    for model in models:
        data, err = query_hf_api({"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": temperature})
        if err:
            last_err = err
            continue
        out = _extract_text(data)
        if out:
            return out, None
        last_err = "Empty response from model."
    return None, last_err or f"{Fore.RED}All models failed.{Style.RESET_ALL}"
def _words(text: str):
    return re.findall(r"\S+", (text or "").strip())

def generate_text(prompt: str, max_new_tokens: int = 220) -> str:
    msgs = [{"role": "user", "content": prompt}]
    text, err = _run_models(txt_models, msgs, max_tokens=max_new_tokens, temperature=0.3)
    print(text)
    if err:
        raise Exception(err)
    return text

def generate_exact_sentence(prompt: str, n_words: int, max_new_tokens: int, tries: int = 6) -> str:
    for i in range(tries):
        text = generate_text(prompt, max_new_tokens)
        words = _words(text)

        if len(words) >= n_words:
            text = " ".join(words[:n_words])   # keep only first 30 words
            return _ensure_sentence_end(text)
    
    raise Exception(f"{Fore.RED}Could not generate exact words.{Style.RESET_ALL}")

def main():
    img_path = input(f"{Fore.CYAN}🖼️ Enter image filename (default: test.jpg): {Style.RESET_ALL}").strip() or "test.jpg"
    if not os.path.isfile(img_path):
        print(f"{Fore.RED}Error: File '{img_path}' not found.{Style.RESET_ALL}")
        return
    try:
        Image.open(img_path)
    except Exception as e:
        print(f"{Fore.RED}Error opening image: {e}{Style.RESET_ALL}")
        return
    basic_cap = get_basic_caption(img_path)
    print(f"{Fore.GREEN}Basic Caption: {basic_cap}{Style.RESET_ALL}")

# User options for caption manipulation
    print(f"""{Style.BRIGHT}{Fore.GREEN}
================ Image-to-Text Conversion =================
Select output type:
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
=============================================================
""")
    choice = input(f"{Fore.CYAN}Enter your choice (1-4): {Style.RESET_ALL}").strip()
    if choice == "4":
        print(f"{Fore.CYAN}Exiting...{Style.RESET_ALL}")
        exit(0)
    elif choice in ["1", "2", "3"]:
        if choice == "1":
            return basic_cap
        elif choice == "2":
            prompt = ("Rewrite as EXACTLY 30 words. Single paragraph. One complete sentence. "
                      "End with a period. No title/bullets.\n\nText: " + basic_cap)
            out = generate_exact_sentence(prompt, 30, max_new_tokens=220, tries=6)
            print(f"{Fore.GREEN}✅ Description (30 words): {Fore.YELLOW}{Style.BRIGHT}{out}\n")
            
            
if __name__ == "__main__":
    main()