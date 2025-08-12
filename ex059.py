from random import randint
from time import sleep 
cm=randint(0,10)
palpites=0
acertou=False
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
player=int(input('Qual é seu palpite'))
while cm!=player :
    palpites+=1
    if cm>player :
        print('Mais...tente mais uma vez')
        player=int(input('Qual é seu palpite ?'))
    if cm<player :
        print('Menos...tente mais uma vez')
        player=int(input('Qual é seu palpite?'))
print('Eu pensei no número {} e você o acertou com {} palpites'.format(cm,palpites))
    
