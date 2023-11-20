
# 4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
