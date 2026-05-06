""""
    AI Prompt Engineering Tutorial" is an interactive 
    learning activity that guides users in creating and 
    refining prompts for AI models like Groq, Hugging Face 
    or OpenAI's GPT. The tutorial focuses on teaching 
    Clarity and Specificity and Contextual Information 
    in crafting effective prompts for AI. Users will 
    start by providing a vague prompt, then refine it 
    to be more specific, and finally, add contextual 
    information to see how the AI's responses 
    evolve with each iteration.
                                                                """
from hf import generate_response

print("Welcome to ai engineering tutorial!")
vague = input("Enter a vague prompt: ")
print("\nGenerating response for vague prompt...")
print(generate_response(vague))


specific = input("\nNow, enter a more specific prompt: ")
print("\nGenerating response for specific prompt...")
print(generate_response(specific))


context = input("\nFinally, add some context to your prompt: ")
print("\nGenerating response for prompt with context...")
print(generate_response(context))


