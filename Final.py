import pandas as pd

# Read scraped data into a Pandas DataFrame
try:
    df = pd.read_csv('movies_list.csv')  # Adjust the filename and format as needed
except FileNotFoundError:
    print("Error: Scraped data file not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("Error: Scraped data file is empty.")
    exit(1)
except pd.errors.ParserError:
    print("Error: Unable to parse scraped data.")
    exit(1)
    
# Prompt user for genre input
user_genre = input("Enter a movie genre: ")

# Filter movies by user's input genre
filtered_movies = df[df['genre_list'].str.contains(user_genre, case=False)]

# Display the movie suggestions
if not filtered_movies.empty:
    print("Here are some movie suggestions based on your genre:")
    print(filtered_movies[['genre_list','Title','Year of release', 'Watch time']])
else:
    print(f"No movies found for the genre '{user_genre}'.")
