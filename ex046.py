from time import sleep
n=str(input('Digite start para iniciar a contagem regressiva :')).strip().lower()
if n=='start':
    for c in range(10,-1,-1) :
        print(c)
        sleep(1)
print('BBUUUUMM!!!!')