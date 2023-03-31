from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/products')
def prod():
    with app.test_request_context('/products'):
        a = request.path + " " + request.method + " " + current_app.name

        print(a)
    return a

@app.route('/user/<user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

if __name__ == "__main__":
    app.run(debug=True)