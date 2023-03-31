from flask import Flask

app = Flask(__name__)


def index():
    return 'Home Page'
app.add_url_rule('/', 'index', index)

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

@app.route('/user/<id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)


if __name__ == "__main__":
    app.run(debug=True)