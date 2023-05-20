from flask import Flask, request, render_template, make_response, url_for


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'


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
    message = ''
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
    return res

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res

@app.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')

if __name__ == "__main__":
    app.run()