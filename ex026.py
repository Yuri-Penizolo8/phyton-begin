pha=str(input('digite algo :')).lower().strip()
print('Nessa frase a letra a aparece {} vezes'.format(pha.count('a')))
print('Nessa frase a letra a aparece pela primeira vez na posição : {}'.format(pha.find('a')+1))
print('Nessa frase a letra a aparece pela última vez na posição : {}'.format(pha.rfind('a')+1))