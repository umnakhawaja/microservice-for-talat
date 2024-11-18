import requests
import time

# Function to add movies using the movie ranker service
def add_movie_via_service(title, rank):
    url = 'http://127.0.0.1:5000/add_movie'
    response = requests.post(url, json={"title": title, "rank": rank})
    return response.json()

# Function to read and sort movies from the file based on rank
def rank_movies():
    # Read the movies from the input file
    with open('movies_input.txt', 'r') as file:
        lines = file.readlines()

    # Extract movie titles and ranks (skip lines that don't start with "Added movie:")
    movies = []
    for line in lines:
        if line.startswith("Added movie:"):
            parts = line.strip().replace("Added movie: ", "").split(", Rank: ")
            title = parts[0]
            rank = int(parts[1])
            movies.append({"title": title, "rank": rank})
    
    # Sort movies by rank
    movies.sort(key=lambda movie: movie['rank'])
    
    # Write the sorted list back to the file
    with open('movies_input.txt', 'a') as file:
        file.write("\nMovies ranked successfully!\n")
        for movie in movies:
            file.write(f"Title: {movie['title']}, Rank: {movie['rank']}\n")
            time.sleep(1)  # Slow down to show the process

    return movies

# Main function to run the test
def main():
    print("Adding movies to the service...")

    # Add movies via the service
    add_movie_via_service("The Dark Knight", 2)
    add_movie_via_service("Inception", 1)
    add_movie_via_service("Interstellar", 3)

    # Wait a moment to simulate real-time interaction
    time.sleep(2)

    print("\nRanking movies...")
    ranked_movies = rank_movies()

    print("\nRanked Movies:")
    for movie in ranked_movies:
        print(f"Title: {movie['title']}, Rank: {movie['rank']}")

if __name__ == "__main__":
    main()
