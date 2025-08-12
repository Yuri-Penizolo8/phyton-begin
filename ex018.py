import math
an=float(input('Digite um ângulo:'))
an2=math.radians(an)
c=math.cos(an2)
s=math.sin(an2)
t=math.tan(an2)
print('Dessa maneira, o seno, cosseno e tangente de {}, vale, respectivamente {:.2f},{:.2f},{:.2f}.'.format(an,s,c,t))