km=float(input('Digite a distância em Km de sua viagem :'))
if km<=200 :
    print('O valor a ser pago é de {}'.format(km*(1/2)))
else :
    print('O valor a ser pago é de {}'.format(km*(45/100)))