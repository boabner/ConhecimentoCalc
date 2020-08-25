from flask import Flask
from flask_restful import Api

from CalcAdiantamentoEmpresa import CalcAdiantamentoEmpresa
from CalcValorFreteFiscal import CalcValorFreteFiscal
from CalcValorMerc import CalcValorMerc
from CalcValorPedagio import CalcValorPedagio

app = Flask(__name__)
api = Api(app)


api.add_resource(CalcValorFreteFiscal, '/calcValorFreteFiscal/')
api.add_resource(CalcValorMerc, '/calcValorMerc/')
api.add_resource(CalcAdiantamentoEmpresa, '/calcAdiantamentoEmpresa/')
api.add_resource(CalcValorPedagio, '/calcValorPedagio/')


if __name__ == '__main__':
  app.run(debug=True)
