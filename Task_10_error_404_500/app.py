# 10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for books
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
]

# Routes for CRUD operations

# ... (Same as the previous example)

# Error handling

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
