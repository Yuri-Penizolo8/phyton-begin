maior = 0
menor = 0
for c in range(1,6):
    w=float(input('Digite o peso da {}° pessoa :'.format(c)))
    if c==1 :
        maior = w
        menor = w
    else :
        if w>maior :
            maior=w
        if w<menor :
            menor=w 
print('O menor peso lido foi {}'.format(menor))
print('O maior peso lido foi {}'.format(maior))

