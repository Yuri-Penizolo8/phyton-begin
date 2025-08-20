num=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True :
    n=int(input('Digite um número'))
    if 0<=n<=20 : 
        print(f'Você digitou o número {num[n]}')
    else :
        print('TENTE NOVAMENTE...')
        n=int(input('Digite um número'))
    