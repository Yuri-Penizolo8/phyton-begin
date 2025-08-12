r1=float(input('Digite o comprimento da primeira reta'))
r2=float(input('Digite o comprimento da segunda reta'))
r3=float(input('digite o comprimento da terceira reta'))
if r1-r2<r3<r1+r2 :
    print('É possível formar um triangulo com essas três retas')
else :
    print('Não é possível formar um triângulo com essas três retas')