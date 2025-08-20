from random import randint 
v=0
print('Vamos jogar par ou ímpar:')
while True:
    player=int(input('Digite um valor:'))
    comp=randint(0,10)
    tot=player+comp
    tip=' '
    while tip not in 'PpIi'.strip().upper()[0]:
        tip=str(input('Par ou Ímpar [P/I] :'))
    print(f'Você jogou {player} e o computador escolheu {comp}.Total de {tot}')
    if tot%2==0 :
        if tip=='P': 
            print('Você venceu')
            v+=1
        elif tip=='I':
            break
            print('Você perdeu!')
    if tot%2==1:
        if tip=='I':
            print('Você venceu')
            v+=1
        elif tip=='P':
            break
            print('Você perdeu!')
