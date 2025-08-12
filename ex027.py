n=str(input('Digite seu nome')).strip()
name=n.split()
print('Seu primeiro nome é : {}'.format(name[0]))
print('Seu último nome é : {}'.format(name[len(name)-1]))