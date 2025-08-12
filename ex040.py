n1=float(input('Digite sua primeira nota :'))
n2=float(input('Digite sua segunda nota'))
m=(n1+n2)/2
print('Sua média foi {}'.format(m))
if m<5 :
    print('REPROVADO')
elif 5==m:
    print('RECUPERAÇÃO')
elif m<6.9 :
    print('RECUPERAÇÃO')
elif m>7 :
    print('APROVADO')