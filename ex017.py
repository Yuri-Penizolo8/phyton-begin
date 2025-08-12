import math
co=int(input('Digite o valor do cateto oposto:'))
ca=int(input('Digite o valor do cateto adjacente:'))
h=math.sqrt((co**2)+(ca**2))
print('Dessa maneira, a hipotenusa vale {}'.format(h))