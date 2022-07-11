from flask import Flask, jsonify, request

import utils

app = Flask(__name__)


@app.get('/books')
def read_books():
    books = utils.load_books_from_json()
    return jsonify(books)


@app.get('/books/<int:book_id>')
def read_book(book_id):
    book = utils.get_book_by_id(book_id)
    return jsonify(book)


@app.post('/books')
def create_book():
    book = {}
    post_data = request.json
    book["title"] = post_data.get("title")
    book["year"] = post_data.get("year")
    book["author"] = post_data.get("author")
    new_book = utils.add_book(book)
    return jsonify(new_book)


@app.put('/books/<int:book_id>')
def update_book(book_id):
    book = utils.get_book_by_id(book_id)
    post_data = request.json
    book["title"] = post_data.get("title")
    book["year"] = post_data.get("year")
    book["author"] = post_data.get("author")
    utils.update_book(book_id, book)
    return jsonify(book)


@app.delete('/books/<int:book_id>')
def delete_book(book_id):
    utils.delete_book(book_id)
    return ""


app.run()
