from flask import Flask, render_template, Command, Shell, request
from flask_script import Manager

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

manager = Manager(app)


class Faker(Command):
    def run(self):
        print("Fake data entered")

manager.add_command("faker", Faker())

@manager.command
def foo():
    "Это созданная команда"
    print("foo command executed")

def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))

@app.route('/')
def index():
    return render_template('index.html', name='Jerry')

@app.route('/user//')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books//')
def books(genre):
    return "All Books in {} category".format(genre)

@app.route('/login/', methods=['post', 'get'])
def login():
    message =''
    if request.method=='POST':
        username = request.form.get('username') 
        password = request.form.get('password')
    if username == 'root' and password =='pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)

if __name__ == "__main__":
    manager.run()