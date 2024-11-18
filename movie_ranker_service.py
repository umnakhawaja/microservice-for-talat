from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Function to write movie data to the file
def write_to_file(data):
    with open('movies_input.txt', 'a') as file:
        file.write(data + "\n")
        file.flush()  # Ensure data is written immediately
        time.sleep(1)  # Slow down to show the process in the file

# Route to add a movie with its rank
@app.route('/add_movie', methods=['POST'])
def add_movie():
    # Get movie details from the POST request
    movie_data = request.get_json()
    title = movie_data['title']
    rank = movie_data['rank']

    # Write to file
    write_to_file(f"Added movie: {title}, Rank: {rank}")

    return jsonify({"message": f"Movie '{title}' added successfully."}), 200

if __name__ == "__main__":
    app.run(port=5000)  # Run the Flask app on port 5000
