
sex=str(input('Digite seu sexo :')).upper().strip()[0]
while sex not in 'MmFf' :
    sex=str(input('Sexo inválido.Digite novamente :'))
print('O sexo {} foi cadastrado'.format(sex))
