from flask import Flask, request, jsonify

app = Flask(__name__)
ID = 3

db = [
    {"id": 1, "Name": "John Doe", "Department": "Software", "Role": "Intern"},
    {"id": 2, "Name": "Alina", "Department": "Software", "Role": "Senior Developer"}
]

@app.route('/get/<int:id>', methods=['GET'])
def get_record(id):
    value = None
    for val in db:
        if val['id'] == id:
            value = val

    if value:
        return jsonify(value), 200
    else:
        return jsonify({"error": f"No record with id {id}"}), 404

@app.route('/add', methods=['GET'])
def add():
    global ID
    name = request.args.get("name")
    dep = request.args.get("dep")
    role = request.args.get("role")

    missing = [k for k, v in {"name": name, "dep": dep, "role": role}.items() if not v]
    if missing:
        return jsonify({"error": f"Missing required params, {','.join(missing)}"}), 400
    
    record = {"id": ID, "Name": name, "Department": dep, "Role": role}
    db.append(record)
    ID += 1

    return jsonify({"message": "Record added", "record": record}), 201

@app.route('/employee', methods=['POST'])
def create_employee():
    global ID
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    dep = data.get("dep")
    role = data.get("role")

    missing = [k for k, v in {"name": name, "dep": dep, "role": role}.items() if not v]
    if missing:
        return jsonify({"error": f"Missing required params, {','.join(missing)}"}), 400
    
    record = {"id": ID, "Name": name, "Department": dep, "Role": role}
    db.append(record)
    ID +=1
    return jsonify({"message": "record added", "record": record}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5001)