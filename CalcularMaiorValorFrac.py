CALCM3 = '2'
CALCVLMERC = '3'
CALCPPTVLMERC = '13'
CALCPPTDEF = '30'


def CalcularMaiorValorFrac(tipoFreteEmpresa, precoTonFiscal, pesoCubado, pesoSaida, taxaMercFrete, pesoMinimo,
                           valorMercadoria, tipoCalculo, freteMinimo):
  valorFrete = 0.0
  valorMaior = 0.0
  valorPeso = 0.0
  #
  if tipoCalculo == 1:
    if precoTonFiscal > 0:
      if pesoCubado > 0:
        valorFrete = precoTonFiscal(pesoCubado / 1000)
      valorMaior = valorFrete
      tipoFreteEmpresa = CALCM3
      if pesoSaida >= pesoMinimo:
        valorFrete = precoTonFiscal * (pesoSaida / 1000)
      else:
        valorFrete = precoTonFiscal * (pesoMinimo / 1000)
      valorPeso = valorFrete
      if valorFrete >= valorMaior:
        valorMaior = valorFrete
        tipoFreteEmpresa = CALCPPTDEF
    #
    if taxaMercFrete > 0:
      valorFrete = valorMercadoria * (taxaMercFrete / 100)
      if valorFrete >= valorMaior:
        valorMaior = valorFrete
        tipoFreteEmpresa = CALCVLMERC
      valorFrete = valorPeso + valorMercadoria * (taxaMercFrete / 100)
      if valorFrete >= valorMaior:
        valorMaior = valorFrete
        tipoFreteEmpresa = CALCPPTVLMERC
  #
  elif tipoCalculo == 2:
    if precoTonFiscal > 0:
      if pesoCubado > 0:
        if tipoFreteEmpresa == CALCM3:
          valorFrete = pesoCubado * precoTonFiscal
        else:
          valorFrete = precoTonFiscal * (pesoCubado / 1000)
      else:
        if pesoSaida >= pesoMinimo:
          valorFrete = precoTonFiscal * (pesoSaida / 1000)
        else:
          valorFrete = precoTonFiscal * (pesoMinimo / 1000)
      #
      if taxaMercFrete > 0:
        if tipoFreteEmpresa == CALCPPTVLMERC:
          valorFrete = valorFrete + valorMercadoria * (taxaMercFrete / 100)
        else:
          valorFrete = valorMercadoria * (taxaMercFrete / 100)
      #
      valorMaior = valorFrete
  #
  if valorMaior >= freteMinimo:
    valorMaior = freteMinimo
  #
  return valorMaior, tipoFreteEmpresa
