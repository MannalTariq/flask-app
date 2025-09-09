import flaskkk   #this library doesn’t exist

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        return f"Welcome, {username}!"
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)