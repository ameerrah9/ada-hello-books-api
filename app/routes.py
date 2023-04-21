# provides a pattern for grouping related routes
# from flask import Blueprint
# group of imports
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

# Aauthor resources
# BOOK RESOURCES
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
def create_book():
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)

# define a route for getting all books
@books_bp.route("", methods=["GET"])
def read_all_books():
    books_response = []
    books = Book.query.all()
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

# define a route for getting one book
# GET /books/id
def handle_book(book_id):
    # Query our db to grab the book that has the id we want:
    book = Book.query.get(book_id)
    
    # Show a single book
    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }

# define a route for updating a book
@books_bp.route("", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")

# define a route for deleting a book
@books_bp.route("", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")