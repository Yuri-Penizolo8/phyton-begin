print('GERADOR DE PA')
first=int(input('Digite o primeiro termo:'))
razao=int(input('Digite a razão:'))
cont = 1
term = first
mais = 10
total = 0
while mais!= 0:
    total += mais 
    while cont<=total :
        print('{}'.format(term), end=" ")
        term += razao
        cont += 1
    print('Pausa')
    mais=int(input('Quantos termos a mais você deseja mostrar ?')) 
print('PA finalizada com {} termos mostrados'.format(total))