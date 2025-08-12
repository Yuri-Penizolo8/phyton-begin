from time import sleep
g=str(input('pedra, papel ou tesoura ?')).strip().lower()
if g=='pedra' :
    print('PROCESSANDO...')
    sleep(2)
    print('Eu escolho papel')
elif g=='papel' :
    print('PROCESSANDO...')
    sleep(2)
    print('Eu escolho tesoura')
elif g=='tesoura' :
    print('PROCESSANDO...')
    sleep(2)
    print('Eu escolho pedra')

