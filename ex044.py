p=(float(input('Qual o valor a ser pago pelo produto :')))
c=str(input('Qual a condiçao de pagamento :'))
if c=='a vista, no dinheiro' :
    print('Você deverá pagar {}'.format(0.90*p))
elif c=='a vista, no cartão' :
    print('Você deverá pagar {}'.format(0.95*p))
elif c=='2 vezes no cartão' :
    print('Você deverá pagar {}'.format(p))
elif c=='mais de 3 vezes' :
    print('Você deverá pagar {}'.format(1.2*p))
