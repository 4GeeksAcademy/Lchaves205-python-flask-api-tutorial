from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial todos list
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    print("Returning todos: ", todos)
    return jsonify(todos)  # Return all todos as JSON

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    
    todos.append(request_body)
    
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)
    return jsonify(todos)
