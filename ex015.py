
d=int(input('Quantos dias você ficou com o carro:'))
km=int(input('Quantos km você rodou com o carro:'))
df=60*d
kmf=0.15*km
vf=df+kmf
print('O valor final a pagar é {}'.format(vf))