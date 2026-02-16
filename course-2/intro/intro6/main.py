# Create an AI Movie Recommendation System using 
# TensorFlow and Keras to get MovieLens dataset using Python.
import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)

try: 
    df = pd.read_csv("course-2/intro/intro6/imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); 
    raise SystemExit
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs}) 
def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genres, 1):
        print(Fore.YELLOW + f"{i}. {g}", end="  ")
    choice = int(input("\n\nEnter the number of your favorite genre: ").strip())
    return genres[choice - 1] if 1 <= choice <= len(genres) else get_genre()
def get_rating():
    choice = float(input("Enter minimum IMDB rating (7.6 - 9.3): ").strip())
    if not (7.6 <= choice <= 9.3):
        print(Fore.RED + "Please enter a valid rating between 7.6 and 9.3.")
        return get_rating()
    return choice
def recommend(genre=None, mood_desc=None, rating=None, n=5):
    filtered = df.copy()
    if genre:
        filtered = filtered[filtered["Genre"].str.contains(genre)]
    if mood_desc:
        if mood_desc == "positive":
            filtered = filtered[filtered["IMDB_Rating"] >= 8.0]
        elif mood_desc == "negative":
            filtered = filtered[filtered["IMDB_Rating"] < 8.0]
    if rating:
        filtered = filtered[filtered["IMDB_Rating"] >= rating]
    return filtered.sort_values(by="IMDB_Rating", ascending=False).head(n)
   
    


print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
name = input("What's your name? ").strip() or "Movie Lover"
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")
genre = get_genre()

mood = input("\nHow are you feeling today? (e.g., happy, sad, adventurous): ").strip().lower() or "neutral"
sentiment = TextBlob(mood).sentiment.polarity
if sentiment > 0.1:
    mood_desc = "positive"
elif sentiment < -0.1:
    mood_desc = "negative"
else:    
    mood_desc = "neutral"
print(f"\n{Fore.GREEN}Got it! You're in a {mood_desc} mood.\n")
rating = get_rating()
recommend = recommend(genre, mood_desc, rating, n=5)
if recommend.empty:
    print(Fore.RED + "Sorry, no movies found matching your criteria. Try adjusting your preferences.")
else:
    print(Fore.BLUE + f"\n🎬 Here are some {genre} movies you might enjoy:\n")
    for idx, row in recommend.iterrows():
        print(Fore.YELLOW + f"{row['Series_Title']} ({row['Released_Year']}) - Rating: {row['IMDB_Rating']}")