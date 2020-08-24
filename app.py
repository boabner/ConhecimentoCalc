from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class CalcValorMerc(Resource):

    def post(self):
        dados = json.loads(request.data)
        print(dados)
        #
        numPedido = dados['numPedido']
        pesoSaida = dados['pesoSaida']
        precoKgMercadoria = dados['precoKgMercadoria']
        #
        if numPedido is not None:
            resultado = (float(pesoSaida) * float(precoKgMercadoria))
        else:
            resultado = 0
        #
        print(resultado)
        return {
            'status': 'sucesso', 'resultado': str(resultado)
        }


api.add_resource(CalcValorMerc, '/calcValorMerc/')

if __name__ == '__main__':
    app.run(debug=True)