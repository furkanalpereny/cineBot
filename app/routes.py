from flask import Flask,request, jsonify
from app import releasedMovies_beyazperde
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("main.html")
@app.route('/getMoviesThisWeek')
def getMoviesThisWeek():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return jsonify(movies)