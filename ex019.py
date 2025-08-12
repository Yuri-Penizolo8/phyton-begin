from random import choice
n1=str(input('Digite um aluno:'))
n2=str(input('Digite outro aluno:'))
n3=str(input('Digitre mais um aluno:'))
n4=str(input('Por fim digite o último aluno:'))
list=[n1,n2,n3,n4]
chose=choice(list)
print('O aluno escolhido foi {}'.format(chose))