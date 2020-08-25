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


class CalcAdiantamentoEmpresa(Resource):

  def post(self):
    dados = json.loads(request.data)
    print(dados)
    #
    freteEmpresa = float(dados['freteEmpresa'])
    adiantamentoEmpresa = float(dados['adiantamentoEmpresa'])
    #
    if adiantamentoEmpresa is not None and adiantamentoEmpresa > 0:
      resultado = freteEmpresa * (adiantamentoEmpresa / 100)
    else:
      resultado = 0
    #
    print(resultado)
    return {
      'status': 'sucesso', 'resultado': str(resultado)
    }


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


api.add_resource(CalcValorMerc, '/calcValorMerc/')
api.add_resource(CalcAdiantamentoEmpresa, '/calcAdiantamentoEmpresa/')
api.add_resource(CalcValorPedagio, '/calcValorPedagio/')

if __name__ == '__main__':
  app.run(debug=True)
