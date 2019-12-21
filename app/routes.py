from flask import Flask,request, jsonify
from app import releasedMovies_beyazperde
from app import app
from flask import render_template
import json

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/released_movies')
def released_movies():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return render_template("released_movies.html",movies = movies)

@app.route('/getMoviesThisWeek')
def getMoviesThisWeek():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return jsonify(movies)