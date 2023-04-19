from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import Migrate from flask_migrate
from flask_migrate import Migrate

# give us access to database operations
# instantiate the db
db = SQLAlchemy()
# instantiate the migrate
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    # set up the database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # connect the db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # register the books blueprint
    from .routes import books_bp
    app.register_blueprint(books_bp)

    from app.models.book import Book

    return app