import json

from flask import request
from flask_restful import Resource


class CalcValorMerc(Resource):

  def post(self):
    dados = json.loads(request.data)
    print(dados)
    #
    numPedido = dados['numPedido']
    pesoSaida = float(dados['pesoSaida'])
    precoKgMercadoria = float(dados['precoKgMercadoria'])
    #
    if numPedido is not None:
      resultado = pesoSaida * precoKgMercadoria
    else:
      resultado = 0
    #
    print(resultado)
    return {
      'status': 'sucesso', 'resultado': str(resultado)
    }
