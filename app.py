from movies import get_five_similar_movies
from flask import Flask, request, render_template
from books import get_five_similar_books
import os

app = Flask(__name__)

@app.route('/movies', methods=['GET'])
def index():
    title = request.args.get('name')
    # print('title',title)
    movies = get_five_similar_movies(title)
    return render_template('index.html', movies = movies)

@app.route('/', methods=['GET'])
def search_form():
    return render_template('index.html')

@app.route('/books')
def books():
    title = request.args.get('name')
    books = get_five_similar_books(title)
    return render_template('index.html', books = books)

@app.errorhandler(404) 
def invalid_route(e): 
    return "404 Page not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))




