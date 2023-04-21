# provides a pattern for grouping related routes
# from flask import Blueprint
# group of imports
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

# instantiate a new Book class
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

# # create a group of related books routes
# # all books routes will be prefixed with /books
# # first argument is the name of the blueprint
# books_bp = Blueprint("books", __name__, url_prefix="/books")

# # define a route for the books resource
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)

# # validate a book helper function
# def validate_book(book_id):
#     # validate book_id is an integer
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     # if book_id is not found, return 404
#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# # define a route for a single book resource
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }

# define a route for creating a book resource
@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)