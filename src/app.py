from flask import Flask
from flask import request, jsonify
from src import releasedMovies_beyazperde

app = Flask(__name__)

@app.route("/")
def index():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return jsonify(movies)

if __name__ == "__main__":
    app.run(debug=True)