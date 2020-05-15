from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'test@flask.app' or request.form['password'] != 'password123':
            error = 'Login failed! Invalid username or password'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home')
def home():
  return render_template('success.html')