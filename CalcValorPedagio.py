import json

from flask import request
from flask_restful import Resource


class CalcValorPedagio(Resource):

  def post(self):
    dados = json.loads(request.data)
    print(dados)
    #
    pedagioCalcEixo = dados['pedagioCalcEixo']
    precoTonPedagio = float(dados['precoTonPedagio'])
    quantidadeEixos = float(dados['quantidadeEixos'])
    #
    if pedagioCalcEixo == 'S':
      resultado = precoTonPedagio * quantidadeEixos
    else:
      pesoSaida = dados['pesoSaida']
      resultado = precoTonPedagio * (pesoSaida / 100)
    #
    return {
      'status': 'sucesso', 'resultado': str(resultado)
    }
