from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

db = [
    {"id": 1, "name": "John Doe", "Department": "Software", "Role": "Intern"},
    {"id": 2, "name": "Alina", "Department": "Software", "Role": "Senior Developer"}
]

@app.route('/get/<id>')
def get(id):
    value = None
    for val in db:
        if val['id'] == int(id):
            value = val

    if value:
        return value
    else:
        return f"No record with id {id}"

if __name__ == '__main__':
    app.run(debug=True)