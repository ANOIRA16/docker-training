from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded list of users
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]

# Endpoint to return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
