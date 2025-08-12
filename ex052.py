tot=0
n=int(input('digite um número :'))
for c in range(1,n+1) :
    if n%c==0:
        print('\033[34m')
        tot+=1
    else :
        print('\033[m')
    print('{}'.format(c), end=' ')
    if tot==2 :
        print('O número {} é primo'.format(n))
    else :
        print('Ele não é primo!')
