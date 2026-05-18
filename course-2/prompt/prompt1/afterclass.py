"""
    To reinforce the skill of prompt 
    engineering by crafting, refining, 
    and evaluating prompts for clarity,
    specificity, and context.
                                        """
fro

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