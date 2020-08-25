from flask import Flask, request
from flask_restful import Resource, Api
from CalcValorFreteFiscal import CalcValorFreteFiscal
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome': 'Abner',
     'habilidades': ['Python', 'Flask']
     },
    {'nome': 'Fulano',
     'habilidades': ['Java', 'PHP']
     }
]

class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {
                'status': 'erro',
                'mensagem:': 'Desenvolvedor de id {} não existe'.format(id)
            }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def post(self):
        pass

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}


class ListaDesenvolvedores(Resource):

    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {
            'status': 'sucesso', 'mensagem': 'registros inseridos'
        }


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(CalcValorFreteFiscal, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)