pha=str(input('Digite uma frase :')).strip().lower()
sp=pha.split()
tog="".join(sp)
inv=tog[::-1]
print(tog)

'''for c in range(len(tog)-1,-1,-1):
    inv+=tog[c]'''

print('O inverso de {} é {} e, portanto :'.format(tog,inv))
if inv==tog :
    print('Esse é um palíndromo')
else :
    print('Esse não é um palíndromo !')
