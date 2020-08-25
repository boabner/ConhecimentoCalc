from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoa(id):
    return jsonify(
        {'id': id,
         'nome': 'Abner',
         'profissao': 'Analista'}
    )


@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/soma2', methods=['POST'])
def soma2():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})


desenvolvedores = [
    {'nome': 'Abner',
     'habilidades': ['Python', 'Flask']
     },
    {'nome': 'Fulano',
     'habilidades': ['Java', 'PHP']
     }
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desevolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {
                'status': 'erro',
                'mensagem:': 'Desenvolvedor de id {} não existe'.format(id)
            }
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


@app.route("/dev/", methods=['POST', 'GET'])
def listaDesenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({
            'status': 'sucesso', 'mensagem': 'registros inseridos'}
        )
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
