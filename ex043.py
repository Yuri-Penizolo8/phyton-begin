h=float(input('Digite sua altura em metros :'))
w=float(input('Digite seu peso em kg :'))
imc=w/(h**2)
print('Seu IMC é : {}'.format(imc))
if imc<18.5 :
    print('Abaixo do peso')
elif 18.5==imc :
    print('Peso ideal')