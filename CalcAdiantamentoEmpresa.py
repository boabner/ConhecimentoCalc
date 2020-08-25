import json

from flask import request
from flask_restful import Resource


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
