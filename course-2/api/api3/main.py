# In this project we will be learning 
# how to use APIS and fetching random 
# technology facts and useless facts from a public API. 
# The goal is to learn how to fetch data 
# from APIs, handle JSON responses, and 
# display the results in a interactive manner.
import requests
import html

# Define the API endpoint
api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
print("Welcome to the random facts generator!")
while True:
    choice = input("Press Enter to get a random fact or type 'exit' to quit: \n")
    if choice.lower() == "exit":
        print("Thanks for using the random facts generator! Goodbye!")
        break
    else:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            fact = html.unescape(data["text"]+"\n")
            print(fact)
        else:
            print("Error fetching fact. Please try again.")