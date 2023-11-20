# 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask URL Parameters Example!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello, {username}!'

@app.route('/book/<int:book_id>')
def show_book(book_id):
    return f'Book ID: {book_id}'

@app.route('/greet')
def greet_user():
    # Get the 'name' parameter from the URL, default to 'Guest' if not provided
    username = request.args.get('name', 'Guest')
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(port=0,debug=True)
