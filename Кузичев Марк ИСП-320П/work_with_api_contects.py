from work_witi_api import app
from flask import request, current_app



with app.test_request_context('/'):
    a = request.url
    b = request.method
    c = current_app.name

print(a)
print(b)
print(c)


with app.test_request_context('/news'):
        a = request.path
        b = request.method
        c = current_app.name

print(a)
print(b)
print(c)
    
with app.test_request_context('/entrance'):
    a = request.path
    b = request.method
    c = current_app.name

print(a)
print(b)
print(c)

with app.test_request_context('/user/<id>/'):
    a = request.path
    b = request.method
    c = current_app.name

print(a)
print(b)
print(c)

if __name__ == "__main__":
    app.run(debug=True)