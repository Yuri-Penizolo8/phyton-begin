n=0
s=0
tot=0
while n!= 999:
    s+=n
    tot+=1
    n=int(input('Digite um número [999 para parar]:'))
    if n==999:
        print('A soma entre os {} números é {}'.format(tot,s))