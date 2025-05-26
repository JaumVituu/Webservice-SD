import uuid
from flask import Flask, jsonify, request
import requests

while True:
    porta = int(input("Selecione o número da porta: 5000 ou 5001: "))

    if porta == 5000 or porta == 5001:
        break

    print("Porta não encontrada. Tente novamente.")

app = Flask(__name__)

tasks = {}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values()))

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = str(uuid.uuid4())
    task = {'id': task_id, 'title': data.get('title', ''), 'done': False}
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    data = request.json
    tasks[task_id].update(data)
    return jsonify(tasks[task_id])

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    del tasks[task_id]
    return jsonify({'message': 'Tarefa excluida com sucesso'})

if __name__ == '__main__':
    app.run(port=porta)