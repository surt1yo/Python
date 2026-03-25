# Students will expand their 
# knowledge of APIs by experimenting 
# with various endpoints in the 
# Random Useless Facts API. 
# They'll fetch and display facts 
# from different categories, 
# building on their previous work.
import requests
import html

# Define the API endpoints for different categories
api_endpoints = {
    "random": "https://uselessfacts.jsph.pl/random.json?language=en",
    "today": "https://uselessfacts.jsph.pl/today.json?language=en"
}

print("Welcome to the random facts generator!")
print("Available categories: random, today")

while True:
    category = input("Enter a category (random/today) or type 'exit' to quit: \n").lower()
    
    if category == "exit":
        print("Thanks for using the random facts generator! Goodbye!")
        break
    elif category in api_endpoints:
        response = requests.get(api_endpoints[category])
        if response.status_code == 200:
            data = response.json()
            fact = html.unescape(data["text"] + "\n")
            print(f"[{category.upper()}] {fact}")
        else:
            print("Error fetching fact. Please try again.")
    else:
        print("Invalid category. Please choose from: random, today")