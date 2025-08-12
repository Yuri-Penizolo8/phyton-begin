casa=float(input('Qual valor da casa ?'))
sa=float(input('Qual seu salário ?'))
an=int(input('Quantos anos você vai pagar ?'))

if casa/(an*12)>=0.3*sa :
    print('Sua compra foi aprovada')
    print('Dessa maneira você deverá pagar, mensalmente, : {}'.format(casa/(an*12)))
elif casa/(an*12)<0.3*sa :
    print('Sua compra não foi aprovada, visto que a parcela excede muito salário')