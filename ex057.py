maior = 0
soma = 0
media = 0
maiorh=0
namemoreold=""
totmulher=0
for c in range(1,5):
    print('{}° PESSOA'.format(c))
    name=str(input('Qual seu nome ?')).strip()
    age=int(input('Qual sua idade?'))
    sex=str(input('Qual seu sexo[M/F]?')).strip().upper()
    soma += age
    media += age/4
    if c==1 and sex in 'Mm' :
        maiorh=age
        namemoreold=name
    if sex in 'Mm' and age>maiorh :
        maiorh=age 
        namemoreold=name
    if sex in "Ff" and age<20 :
        totmulher+=1

print('A média entre as idades é {}:'.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(namemoreold,maiorh))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher)) 