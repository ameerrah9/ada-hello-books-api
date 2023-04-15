from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    # register the books blueprint
    from .routes import books_bp
    app.register_blueprint(books_bp)
    
    return app