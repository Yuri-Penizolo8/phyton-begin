v=float(input('Digite a velocidade de seu carro:'))
if v>80.0 :
    print('Você foi multado !')
    print('Dessa maneira deverá pagar uma multa de {} reais !'.format((v-80)*7))
else :
    print('Siga viagem !')