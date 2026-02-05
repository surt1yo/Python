# Create a basic Python program that simulates an AI chatbot, 
# interacting with users through text and responding 
# intelligently based on their input.
print("Hello! I am your AI chatbot. What is your name?")
name = input()
print(f"Nice to meet you, {name}, how are you feeling today?")
answer = input()
if answer.lower() in ["good", "great", "fine", "well"]:
    print("Nice to hear that!")
else:
    print("I'm sorry to hear that.")