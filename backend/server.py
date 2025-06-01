import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

while True:
    porta = int(input("Selecione o número da porta: 5000 ou 5001: "))

    if porta == 5000 or porta == 5001:
        break

    print("Porta não encontrada. Tente novamente.")

app = Flask(__name__)

CORS(app)

tasks = {}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(tasks.values()))

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id]), 200
    return jsonify({'error' : 'Tarefa não encontrada'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = str(data.get("id"))
    if task_id in tasks:
        return jsonify({'error': 'Id já existe'}), 409
    done = data.get("done")
    title = data.get("title")
    task = {'id': task_id, 'title': title, 'done': done}
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