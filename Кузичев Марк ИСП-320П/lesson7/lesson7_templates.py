from flask import Flask, request, render_template

# app = Flask(__name__, template_folder="jinja_templates")
app = Flask(__name__)

@app.route('/')
def index():
    name, fruit = "jerry", "apple"
    x, y = 5, 6 
    template_context = dict(name=name, fruit = fruit, x =x, y= y)
    return render_template('lesson7_create_templates.html', **template_context)

@app.route('/html')
def index_html():
    return render_template('lesson7_create_templates.html')

if __name__ == "__main__":
    app.run(debug=True)

