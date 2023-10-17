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


# Authenticate these requests and allow user.folder
#   to be retrieved from the authenticated user
@app_views.route('/books', methods=['POST'], strict_slashes=False)
def post_book():
    """ Uploads a book and stores it """
    if 'book_file' not in request.files:
        abort(400, 'Missing file')
    book_data = request.form.to_dict(flat=True)
    if not book_data:
        abort(400, 'Not a JSON')
    file = request.files['book_file']
    size = file.content_length
    if size > (10 * 1024 * 1024):
        abort(400, 'File too large')
    extension = file.filename.split('.')[-1]
    allowed_ext = [
        "pdf",
        "epub",
        "mobi",
        "txt",
        "doc",
        "docx",
        "rtf"
    ]
    if extension not in allowed_ext:
        abort(400, 'Invalid file type')
    required = [
        'name',
        'author',
        'public',
    ]
    for field in required:
        # Refactor
        if field == 'public':
            if book_data[field].lower() == 'true':
                book_data[field] = True
            elif book_data[field].lower() == 'false':
                book_data[field] = False
        if field not in book_data:
            abort(400, 'Missing {}'.format(field))
    book_data['size'] = size
    book = Book(**book_data)
    user_folder = book_data['user_folder']
    more_data = manager.create_book(user_folder, file)
    for key, value in more_data.items():
        setattr(book, key, value)
    storage.add(book)
    return jsonify(book.to_dict()), 201


@app_views.route('/books/<book_id>', methods=['GET'], strict_slashes=False)
def get_book(book_id):
    book = storage.get('Book', book_id)
    if book:
        return jsonify(book.to_dict())
    abort(404)


@app_views.route('/books/<book_id>', methods=['DELETE'], strict_slashes=False)
def delete_book(book_id):
    book = storage.get('Book', book_id)
    if book:
        manager.delete_book(book.driveId)
        storage.delete(book)
        return jsonify({}), 200
    abort(404)

@app_views.route('/books/<book_id>', methods=['PUT'], strict_slashes=False)
def put_book(book_id):
    book = storage.get('Book', book_id)
    if not book:
        abort(404)
    data = request.form.to_dict()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        setattr(book, key, value)
    storage.add(book)
    return jsonify(book.to_dict()), 200
