was=int(input('Qual sua data de nascimento :'))
age=2025-was
if 0<=age<=9 :
    print('MIRIM')
elif 10<=age<=14 :
    print('INFANTIL')
elif 15<=age<=19 :
    print('JUNIOR')
elif age==20 :
    print('SÊNIOR')
elif age>20 :
    print('MASTER')