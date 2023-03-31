from flask import Flask, render_template, request


app = Flask(__name__)


app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'


@app.route('/')
def index():
    return render_template('index.html', name='Jerry')

@app.route('/user/<user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)


if __name__ == "__main__":
    app.run()