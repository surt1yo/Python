# Students will use the requests library to fetch 
# data from public APIs (e.g., joke API, trivia API) 
# and display the results in a user-friendly way.
import requests

# Define the API endpoint
api_url = "https://official-joke-api.appspot.com/random_joke"

# Joke API
print("Welcome to the random joke generator!")

while True:
    user_input = input("Press Enter to fetch another joke or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break
    else:
        response = requests.get(api_url)
        if response.status_code == 200:
            joke = response.json()
            print(f"{joke['setup']}, {joke['punchline']}\n")
        else:
            print("Sorry, couldn't fetch a joke at the moment. Please try again later.\n")
