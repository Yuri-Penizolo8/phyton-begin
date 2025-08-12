from datetime import date 
atual=date.today().year
totmaior=0
totmenor=0
for pers in range(1,8) :
    nasc=int(input('Qual a data de nascimento da {}° pessoa ?'.format(pers)))
    idade=atual-nasc
    if idade>=18 :
        totmaior+=1
    else :
        totmenor+=1
print('Ao todo tivemos {} pessoas maiores'.format(totmaior))
print('Ao todo tivemos {} pessoas menores'.format(totmenor))