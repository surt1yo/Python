"""
    In this challenge, you'll further explore how AI models 
    handle biases and work within token limits by conducting 
    two activities: Bias Mitigation and Token Limit Optimization. 
    Through these exercises, you will deepen your understanding 
    of how to craft effective prompts and improve AI output quality.
                                                                    """
from hf import generate_response


# Functions

def bias_mitigation():
    print("\nBias Mitigation Activity")
    prompt = input("Enter a prompt to explore bias (eg., 'Describe an ideal doctor'): ").strip()
    if not prompt:
        print("Prompt cannot be empty. Please try again.")
        return
    response = generate_response(prompt)
    print(f"AI Response: {response}")
    modified_prompt = input("Modify the prompt to reduce bias (eg., 'Describe an ideal doctor without mentioning gender'): ").strip()
    if not modified_prompt:
        print("Modified prompt cannot be empty. Please try again.")
        return
    modified_response = generate_response(modified_prompt)
    print(f"Modified AI Response: {modified_response}") 


def token_limit_optimization():
    print("\nToken Limit Optimization Activity")
    prompt = input("Enter a long text input (eg., a news article or story): ").strip()  
    if not prompt:
        print("Input cannot be empty. Please try again.")
        return
    response = generate_response(prompt)
    print(f"AI Response: {response[:500]}...")  
    shorter_prompt = input("Enter a shorter version of the text (eg., a summary or key points): ").strip()
    if not shorter_prompt:
        print("Shorter prompt cannot be empty. Please try again.")
        return
    shorter_response = generate_response(shorter_prompt)
    print(f"AI Response to Shorter Prompt: {shorter_response}")

def run_activity():
    print(50*"=")
    print("AI Response Generation: Bias Mitigation and Token Limits")
    print(50*"=")
    print("\nActivity 1: Bias Mitigation")
    print("Activity 2: Token Limit Optimization")
    choice = int(input("Choose an activity (1 or 2): "))

    if choice == 1:
        bias_mitigation()
    elif choice == 2:
        token_limit_optimization()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":  
    run_activity()



    