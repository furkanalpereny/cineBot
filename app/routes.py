from flask import Flask,request, jsonify
from app import releasedMovies_beyazperde
from app import app
from flask import render_template
import json

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/index')
def index():
    with open('src/json/2019-12-21_releasedMovies.json') as json_file:
        movies = json.load(json_file)
    return render_template("index.html",movies = movies)

@app.route('/getMoviesThisWeek')
def getMoviesThisWeek():
    movies = releasedMovies_beyazperde.getMoviesThisWeek()
    return jsonify(movies)