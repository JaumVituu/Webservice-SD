from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

servers = ['http://localhost:5000', 'http://localhost:5001']

@app.route('/<path:path>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def proxy(path):
    data = request.get_json(silent=True)
    headers = {'Content-Type': 'application/json'}

    for server in servers:
        try:
            if request.method == 'GET':
                resp = requests.get(f'{server}/{path}', params=request.args)
            elif request.method == 'POST':
                resp = requests.post(f'{server}/{path}', json=data, headers=headers)
            elif request.method == 'PATCH':
                resp = requests.patch(f'{server}/{path}', json=data, headers=headers)
            elif request.method == 'DELETE':
                resp = requests.delete(f'{server}/{path}', json=data, headers=headers)
            else:
                return jsonify({'error': 'Metodo não suportado pela aplicação'}), 405

            print(f"Requisição enviada com sucesso para o servidor: {server}")
            return jsonify(resp.json()), resp.status_code

        except requests.exceptions.ConnectionError:
            print(f"Servidor {server} indisponível.")

    return jsonify({'error': 'Servidores indisponíveis'}), 503

if __name__ == '__main__':
    app.run(port=8000, debug=True)
