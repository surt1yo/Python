"""
    In this interactive Activity, you will 
    explore two AI learning techniques: 
    Reinforcement Learning and Role-Based Prompts. 
    They will experiment with giving feedback to 
    improve AI responses and observe how 
    role-specific instructions can tailor AI outputs.
                                                        """
from hf import generate_response


print(50*"=")
print("AI LEARNING ACTIVITY")
print(50*"=")
print("Choose an activity:")
print("1. Reinforcement Learning\n2. Role-Based Prompts")

# Functions
def reinforcement_learning():
    prompt = input("Enter a prompt for the AI: for example, 'What is the capital of France?'")
    if prompt == None or prompt.strip() == "":
        print("Prompt cannot be empty.")
        return
    response = generate_response(prompt, temperature=0.3, max_tokens=512)
    print(f"AI Response: {response}")
    rating = int(input("Enter a rating of the response from 1(Bad) to 10(Amazing)"))
    if rating not in range(1, 11):
        rating = 4
        return
    feedback = input("Please give the feedback for improvement: ")
    if feedback == None or feedback.strip() == "":
        print("Feedback cannot be empty.")
        return
    improve_resp = generate_response(f"Improve the following response: '{response}' based on this feedback: '{feedback}'", temperature=0.3, max_tokens=512)
    print(f"Improved AI Response: {improve_resp}")

def role_based_prompts():
    role = input("Enter a role for the AI (e.g., 'teacher', 'doctor', 'chef'): ")
    if role == None or role.strip() == "":
        print("Role cannot be empty.")
        return
    prompt = input(f"Enter a prompt for the AI in the role of {role}: ")
    if prompt == None or prompt.strip() == "":
        print("Prompt cannot be empty.")
        return
    response = generate_response(f"As a {role}, {prompt}", temperature=0.3, max_tokens=512)
    print(f"AI Response: {response}")    

choice = int(input("Enter the number of your choice: "))


if choice == 1:
    reinforcement_learning()

elif choice == 2:
    role_based_prompts()
else:
    print("Invalid choice. Please enter 1 or 2.")
    