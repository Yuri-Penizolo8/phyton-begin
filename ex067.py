while True :
    n=int(input('Deseja ver a tabuada de qual valor?'))
    if n<0 :
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Você digitou um valor negativo.Volte sempre!')
    