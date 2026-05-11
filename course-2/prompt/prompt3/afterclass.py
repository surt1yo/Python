"""
    To help students practically understand 
    how the level of context and examples 
    (zero, one, few) influences AI's accuracy and 
    creativity in performing classification and text generation tasks.
                                                                        """
from hf import generate_response

print("Zero Shot, One Shot, and Few Shot Learning with Hugging Face API")

category = input("Enter a category (e.g. fruit, animal, vehicle): ")
item = input("Enter an item to classify (e.g. apple, dog, car): ")

# Zero Shot Learning
print("\nZero Shot Learning")

zero_shot_prompt = (
    f"Classify the item '{item}' under the category '{category}'."
)

print("Prompt:")
print(zero_shot_prompt)

zero_shot_response = generate_response(zero_shot_prompt)

print("Response:")
print(zero_shot_response)


# One Shot Learning
print("\nOne Shot Learning")

one_shot_prompt = f"""
Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Now classify the following:
Category: {category}
Item: {item}
"""

print("Prompt:")
print(one_shot_prompt)

one_shot_response = generate_response(one_shot_prompt)

print("Response:")
print(one_shot_response)


# Few Shot Learning
print("\nFew Shot Learning")

few_shot_prompt = f"""
Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.

Example 2:
Category: animal
Item: dog
Answer: Yes, dog is an animal.

Now classify the following:
Category: {category}
Item: {item}
"""

print("Prompt:")
print(few_shot_prompt)

few_shot_response = generate_response(few_shot_prompt)

print("Response:")
print(few_shot_response)