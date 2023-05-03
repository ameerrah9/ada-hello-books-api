from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import Migrate from flask_migrate
from flask_migrate import Migrate
# import libraries
from dotenv import load_dotenv
# used to read environment variables
import os

# give us access to database operations
# instantiate the db
db = SQLAlchemy()
# instantiate the migrate
migrate = Migrate()
# loads the values from our .env file so that 
# the os module is able to see them.
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    # set up the database
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "DATABASE_URL")
    else:
        # If there is a test_config passed in, 
        # this means we're trying to test the app, 
        # configure test settings
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # connect the db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # register the books blueprint
    from .book_routes import books_bp
    app.register_blueprint(books_bp)

    from .author_routes import authors_bp
    app.register_blueprint(authors_bp)
    
    from app.models.book import Book
    from app.models.author import Author

    return app