""" This module contains the book view """
from api.views import app_views
from flask import (
    jsonify,
    request,
    abort,
)
from models import storage
from models import manager
from models.user import User
from models.book import Book


@app_views.route('/books', methods=['GET'], strict_slashes=False)
def get_books():
    """ Returns all books """
    books = storage.all('Book')
    return jsonify([book.to_dict() for book in books.values()])


@app_views.route('/post_books', methods=['GET'], strict_slashes=False)
def get_book():
    """ allows user to upload a book using a form """

    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Upload Book</title>
        </head>
        <body>
            <h1>Upload a Book</h1>
            <form
                action="/api/post_books"
                method="post"
                enctype="multipart/form-data"
            >
                <label for="bookName">Book Name:</label>
                <input type="text" name="name" id="name" required><br><br>

                <label for="author">Author:</label>
                <input type="text" name="author" id="author" required><br><br>

                <label for="user_folder">User Folder:</label>
                <input
                    type="text"
                    name="user_folder"
                    id="user_folder"
                    required
                >
                <br><br>

                <label for="privacy">Privacy:</label>
                <input
                    type="checkbox"
                    name="private"
                    id="private"
                    value="true"
                >
                <br><br>

                <label for="bookFile">Select Book File:</label>
                <input type="file" name="bookFile" id="bookFile" required>
                <br><br>

                <input type="submit" value="Upload">
            </form>
        </body>
        </html>
    """


# Update to /books, need to allow form for testing
# Authenticate these requests and allow user.folder
#   to be retrieved from the authenticated user
@app_views.route('/post_books', methods=['POST'], strict_slashes=False)
def post_book():
    """ Uploads a book and stores it """
    name = request.form.get('name')
    author = request.form.get('author')
    user_folder = request.form.get('user_folder')
    public = bool(request.form.get('private'))
    file = request.files['bookFile']
    size = file.content_length
    required = [
        'name',
        'author',
    ]
    print(public)
    if 'bookFile' not in request.files:
        abort(400, 'Missing file')
    for field in required:
        if field not in request.form:
            abort(400, 'Missing {}'.format(field))
    data = {
        'name': name,
        'author': author,
        'public': public,
        'size': size,
    }
    book = Book(**data)
    more_data = manager.create_book(user_folder, file)
    for key, value in more_data.items():
        setattr(book, key, value)

    storage.add(book)

    return jsonify(book.to_dict()), 201
