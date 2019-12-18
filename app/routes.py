from flask import Flask,request, jsonify
from app import releasedMovies_beyazperde
from app import app

@app.route('/')
@app.route('/index')
def index():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return jsonify(movies)