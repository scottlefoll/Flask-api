import json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/home/')
def home():
    return "Home page"

@app.route('/contact')
def contact():
    return "Contact page"

@app.route('/hello/')
def welcome():
    return "Hello World!"

@app.route('/numbers/<int:number>/')
def print_list(number):
    return jsonify(list(range(number)))

@app.route('/persons/')
def hello_persons():
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

@app.route('/person/<string:name>/')
def hello_person(name):
    people = [
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
    ]

    # Filtering the list to find the record that matches the name (case-insensitive)
    matching_person = next((person for person in people if person['name'].lower() == name.lower()), None)

    if matching_person is not None:
        return jsonify(matching_person)
    else:
        return jsonify({"error": "Person not found"}), 404

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)