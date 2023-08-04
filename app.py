from flask import Flask
from flask import jsonify
app = Flask(__name__)

def hello_json():
    return ([
                {'name':'Scott', 'country':'USA'},
                {'name':'Maria', 'country':'Spain'},
                {'name':'Akiko', 'country':'Japan'},
                {'name':'Lukas', 'country':'Germany'},
                {'name':'Sophie', 'country':'France'},
                {'name':'Giovanni', 'country':'Italy'},
                {'name':'Sara', 'country':'Sweden'},
                {'name':'Oliver', 'country':'United Kingdom'},
                {'name':'Mikhail', 'country':'Russia'},
                {'name':'Mei', 'country':'China'}
            ])

@app.route('/home/')
def home():
    return "Home page"

@app.route('/contact')
def contact():
    return "Contact page"

@app.route('/hello/')
def welcome():
    return "Hello World!"

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(100)))

@app.route('/persons/')
def hello_person():
    list = hello_json()

@app.route('/person/<string:name>/')


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)