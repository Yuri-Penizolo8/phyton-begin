prosseguir='S'.upper().strip()[0]
cont=soma=n=maior=menor=0
while prosseguir in "Ss":
    cont+=1
    n=int(input('digite um número:'))
    soma+=n
    prosseguir=str(input('Quer continuar?'))
    if cont==1:
        maior=menor=n
    else :
        if n>maior :
            maior=n
        if n<menor:
            menor=n
    if prosseguir in "Nn":
        print('Você digitou {} e a média entre eles é {}'.format(cont,(soma/cont)))
        print('O maior entre eles é {} e o menor entre eles é {}'.format(maior,menor))
