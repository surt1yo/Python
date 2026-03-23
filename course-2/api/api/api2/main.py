# Students will use a Trivia API to 
# fetch trivia questions and create 
# an interactive quiz where they can 
# answer the questions and receive feedback.
import requests
import html 

# Define the API endpoint
api_url = "https://opentdb.com/api.php?amount=5&type=multiple"
score = 0
# Trivia API
print("Welcome to the trivia quiz!")
print("Press Enter to start the quiz or type 'exit' to quit: ")
choice = input()
if choice.lower() == 'exit':
    print("Thanks for playing! Goodbye!")
else:
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for i, data in enumerate(data["results"]):
            q = question = data["question"]
            q = html.unescape(q)
            print(f"Question {i+1}: {q}")
            options = data['incorrect_answers'] + [data['correct_answer']]
            options = sorted(options)
            for j, option in enumerate(options):
                print(f"{j+1}. {option}")
            answer = input("Your answer (1-4): ")
            if options[int(answer)-1] == data["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect!\n")
                score -= 1
        print(f"Your final score is: {score}/5")
            
    else:
        print("Sorry, couldn't fetch trivia questions at the moment. Please try again later.\n")
    
