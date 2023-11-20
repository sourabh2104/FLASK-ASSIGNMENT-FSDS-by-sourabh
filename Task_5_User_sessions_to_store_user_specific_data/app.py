
# 5. Flask App with User Sessions to Store and Display User-Specific Data:

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Sample user-specific data
user_data = {
    'user1': {'name': 'John', 'email': 'john@example.com'},
    'user2': {'name': 'Jane', 'email': 'jane@example.com'}
}

@app.route('/')
def index():
    if 'username' in session:
        # If the user is logged in, display their data
        user = user_data.get(session['username'])
        return render_template('index.html', user=user)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in user_data:
            # Store the username in the session
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
