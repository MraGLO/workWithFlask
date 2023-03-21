from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    with app.test_request_context('/'):
        a = request.url
        b = request.method
        c = current_app.name

    print(a)
    print(b)
    print(c)
    return 'Hello visitor'
    
    

@app.route('/news')
def News():
    with app.test_request_context('/news'):
        a = request.path
        b = request.method
        c = current_app.name

    print(a)
    print(b)
    print(c)
    return 'РЕГИОНАЛЬНЫЙ ЭТАП ЧЕМПИОНАТА &#8220;ПРОФЕССИОНАЛЫ&#8221; ВОЛОГОДСКОЙ ОБЛАСТИ'
    

@app.route('/entrance')
def Entrance():
    with app.test_request_context('/entrance'):
        a = request.path
        b = request.method
        c = current_app.name

    print(a)
    print(b)
    print(c)
    return 'Введите логин и пароль'

@app.route('/user/<id>/')
def User_Profile(id):
    with app.test_request_context('/user/<id>/'):
        a = request.path
        b = request.method
        c = current_app.name

    print(a)
    print(b)
    print(c)
    return "Profile page of user #{}".format(id)

    
    
if __name__ == "__main__":
    app.run(debug=True)