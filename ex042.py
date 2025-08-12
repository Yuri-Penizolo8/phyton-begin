r1=int(input('Digite o valor da primeira reta :'))
r2=int(input('Digite o valor da segunda reta :'))
r3=int(input('Digite o valor da terceira reta :'))
if r1-r2<r3<r1+r2 :
    print('É possível formar um triângulo !!')
else :
    print('Não é possível formar um triângulo')
if r1==r2==r3 :
    print('Esse é um triângulo equilátero')
elif r1==r2 :
    print('Esse é um triângulo isósceles')
elif r1==r3 :
    print('Esse é um triângulo isósceles')
elif r2==r3 :
    print('Esse é um triângulo isósceles')
else :
    print('Esse é um triângulo escaleno')