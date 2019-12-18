from flask import Flask
from flask import request, jsonify

import releasedMovies_beyazperde

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        movies = releasedMovies_beyazperde.getMoviesThisWeek()
        return jsonify(movies)

if __name__ == "__main__":
    app.run()