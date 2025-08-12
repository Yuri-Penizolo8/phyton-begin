soma = 0
cont = 0
for n in range(1,7) :
    n1=int(input('Digite um número :'))
    if n1%2==0 :
        soma= soma + n1 
        cont = cont + 1
    print('A soma netre os números pares é {}'.format(soma))