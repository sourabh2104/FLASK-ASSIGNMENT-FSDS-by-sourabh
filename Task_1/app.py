
# 1. Flask App displaying "Hello, World!" on the Homepage:

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(debug=True)

