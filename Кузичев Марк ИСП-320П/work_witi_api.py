from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello visitor'

@app.route('/news')
def News():
    return 'РЕГИОНАЛЬНЫЙ ЭТАП ЧЕМПИОНАТА &#8220;ПРОФЕССИОНАЛЫ&#8221; ВОЛОГОДСКОЙ ОБЛАСТИ'

@app.route('/entrance')
def Entrance():
    return 'Введите логин и пароль'

@app.route('/user/<id>/')
def User_Profile(id):
    return "Profile page of user #{}".format(id)
    


if __name__ == "__main__":
    app.run(debug=True)