'''n=int(input('Digite um valor:'))
r=int(input('Digite a razão'))
for c in range(n,n*9,r):
    print(c)'''
print('GERADOR DE PA')
first=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razão:'))
cont = 1
term = first 
while cont<=10 :
    term += razao
    cont += 1
print('{}'.format(term), end=" ")
    