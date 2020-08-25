from flask import request
from flask_restful import Resource
from CalcularMaiorValorFrac import CalcularMaiorValorFrac

import json

CALCM3 = '2'
CALCVLMERC = '3'
CALCCARGAFECHADA = '4'
CALCCARGAFECHADARAT = '5'
CALCREENT50CFECH = '9'
CALCPPTVLMERC = '13'
CALCMAIORVALOR = '14'
CALCPPTDEF = '30'
CALCPPTKM = '32'


class CalcValorFreteFiscal(Resource):

  def post(self):
    dados = json.loads(request.data)
    print(dados)
    #
    tipoFreteEmpresa = dados['tipoFreteEmpresa']
    #
    divCalcPesoCubado = float(dados['divCalcPesoCubado'])
    precoTonFiscal = float(dados['precoTonFiscal'])
    pesoCubado = float(dados['precoTonFiscal'])
    pesoMinimo = float(dados['pesoMinimo'])
    pesoSaida = float(dados['precoTonFiscal'])
    taxaMercFrete = float(dados['precoTonFiscal'])
    valorMercadoria = float(dados['precoTonFiscal'])
    kmRodado = float(dados['precoTonFiscal'])
    #
    freteMinimo = 0.0
    resultado = 0.0
    if tipoFreteEmpresa != CALCPPTDEF and tipoFreteEmpresa != CALCCARGAFECHADA:
      #
      if tipoFreteEmpresa == CALCMAIORVALOR:
        resultado, tipoFreteEmpresa = CalcularMaiorValorFrac(tipoFreteEmpresa, precoTonFiscal, pesoCubado, pesoSaida,
                                                             taxaMercFrete, pesoMinimo, valorMercadoria, 1, freteMinimo)
      #
      elif tipoFreteEmpresa != CALCCARGAFECHADA and tipoFreteEmpresa != CALCREENT50CFECH and \
          tipoFreteEmpresa != CALCCARGAFECHADARAT:
        resultado, tipoFreteEmpresa = CalcularMaiorValorFrac(tipoFreteEmpresa, precoTonFiscal, pesoCubado, pesoSaida,
                                                             taxaMercFrete, pesoMinimo, valorMercadoria, 1, freteMinimo)
      #
      elif tipoFreteEmpresa == CALCPPTKM:
        resultado = kmRodado * precoTonFiscal
      #
      elif tipoFreteEmpresa == CALCM3 and pesoCubado > 0:
        resultado = precoTonFiscal * (pesoCubado / divCalcPesoCubado)
      #
    elif tipoFreteEmpresa != CALCCARGAFECHADA:
      if precoTonFiscal > 0 and pesoSaida > 0:
        resultado = precoTonFiscal * (pesoSaida / 1000)
      #
      if tipoFreteEmpresa == CALCPPTKM or pesoCubado > 0:
        resultado = precoTonFiscal * (pesoCubado / divCalcPesoCubado)
    #
    print(resultado)
    return {
      'status': 'sucesso', 'resultado': str(resultado), 'tipoFreteEmpresa': str(tipoFreteEmpresa)
    }
