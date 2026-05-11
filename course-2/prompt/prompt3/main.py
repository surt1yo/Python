"""
    This activity explores Zero-shot, One-shot, 
    and Few-shot learning using the Groq and Hugging Face API. 
    Participants will input a category and an item, 
    and observe how different learning approaches 
    impact AI-generated responses. 
    They will experiment with different learning 
    paradigms and reflect on how providing examples 
    in the prompt influences the AI's performance 
    in tasks such as classification and creative generation.
                                                            """
from hf import generate_response

print("Zero Shot, One Shot, FewShot Learning with Hugging Face API")
category = input("Enter a category (e.g., 'fruit', 'animal', 'vehicle'): ")
item = input("Enter an item to classify (e.g., 'apple', 'dog', 'car'): ")

print("Trying Zero Shot Learning")
zero_shot_prompt = f"Classify the following item: {item} into the category: {category}."
print("Prompt:", zero_shot_prompt)
zero_shot_response = generate_response(zero_shot_prompt)
print("Zero Shot Response:", zero_shot_response)

print("\nTrying One Shot Learning")
one_shot_prompt = f"""Example: Category: fruit\nItem: apple\nAnswer: Yes, apple is a fruit.
                    Now classify the following item: {item} into the category: {category}."""
print("Prompt:", one_shot_prompt)
one_shot_response = generate_response(one_shot_prompt)
print("One Shot Response:", one_shot_response)

print("\nTrying Few Shot Learning")
few_shot_prompt = f"""Example 1: Category: fruit\nItem: apple\nAnswer: Yes, apple is a fruit.
                      Example 2: Category: animal\nItem: dog\nAnswer: Yes, dog is an animal.
                      Now classify the following item: {item} into the category: {category}."""
print("Prompt:", few_shot_prompt)
few_shot_response = generate_response(few_shot_prompt)
print("Few Shot Response:", few_shot_response)
