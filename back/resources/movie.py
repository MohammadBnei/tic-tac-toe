from flask import Blueprint, Response, jsonify, request

movies = Blueprint('movies', __name__)

movies_list = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]

@movies.route('/movies')
def show_movies():
    return jsonify(movies_list), 200

@movies.route('/movies/<int:id>')
def show_movie(id):
    return jsonify(movies_list[id]), 200

@movies.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies_list.append(movie)
    return {'id': len(movies_list)}, 200

@movies.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies_list[index] = (movie)
    return {'id': len(movies_list)}, 200

@movies.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies_list.pop(index)
    return 'None', 200