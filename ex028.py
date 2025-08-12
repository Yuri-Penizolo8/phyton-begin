from random import randint
from time import sleep
cm=randint(0,5)
player=int(input('Em que número eu pensei :'))
print('Processando...')
sleep(3)
if player==cm :
    print('Você acertou !!!')
else :
    print('Você errou !!!')
    print('Eu pensei no número {}'.format(cm))