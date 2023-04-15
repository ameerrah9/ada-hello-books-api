# provides a pattern for grouping related routes
# from flask import Blueprint
# group of imports
from flask import Blueprint, jsonify

# instantiate a new Book class
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]

# create a group of related books routes
# all books routes will be prefixed with /books
# first argument is the name of the blueprint
books_bp = Blueprint("books", __name__, url_prefix="/books")

# define a route for the books resource
@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)