n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
op=0
while op!=5 :
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    op=int(input('Qual é sua opção'))
    if op==1 :
        print('A soma entre {} e {} é {}'.format(n1,n2,n1+n2))
    if op==2 :
        print('A multiplicação entre {} e {} é {}'.format(n1,n2,n1*n2))
    if op==3 :
        if n1>n2 :
            print('Entre {} e {} o maior é {}'.format(n1,n2,n1))
        if n1<n2 :
            print('Entre {} e {} o maior é {}'.format(n1,n2,n2))
    
