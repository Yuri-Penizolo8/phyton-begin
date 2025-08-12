was=int(input('Digite sua data de nascimento :'))
age=2025-was
if age==18 :
    print('Está na hora de se alistar')
elif age>18 :
    print('Considero que você já se alistou')
elif age<18 :
    print('Você ainda não se alistou !')
    print('Ainda falta {} anos'.format(18-age))