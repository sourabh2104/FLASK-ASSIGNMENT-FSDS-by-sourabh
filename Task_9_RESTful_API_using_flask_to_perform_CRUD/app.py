# 8. Implement user authentication and registration in a Flask app using Flask-Login.

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy data for books
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
]

# Routes for CRUD operations

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify({'book': book})
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify({'book': new_book}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        data = request.get_json()
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify({'book': book})
    else:
        return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted successfully'}), 200

# HTML rendering

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
