import uuid
import json
from flask import Flask, jsonify, request

def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

while True:
    porta = int(input("Selecione o número da porta: 5000 ou 5001: "))

    if porta == 5000 or porta == 5001:
        break

    print("Porta não encontrada. Tente novamente.")

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    current_tasks = load_tasks()
    return jsonify(list(current_tasks.values()))

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = str(uuid.uuid4())
    tasks = load_tasks()
    task = {'id': task_id, 'title': data.get('title', ''), 'done': False}
    tasks[task_id] = task
    save_tasks(tasks)
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    tasks = load_tasks()
    if task_id not in tasks:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    data = request.json
    tasks[task_id].update(data)
    save_tasks(tasks)
    return jsonify(tasks[task_id])

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    if task_id not in tasks:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    del tasks[task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Tarefa excluída com sucesso'})

if __name__ == '__main__':
    app.run(port=porta)
