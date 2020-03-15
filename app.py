from recommend import get_five_similar_movies
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    title = request.args.get('name')
    print('title',title)
    movies = get_five_similar_movies(title)
    return render_template('index.html', movies = movies)


@app.route('/search', methods=['GET'])
def search_form():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)