a=int(input('DIGITE O PRIMEIRO VALOR. '))
b=int(input('DIGITE O SEGUNDO VALOR. '))
c=int(input('DIGITE O TERCEIRO VALOR. '))
#VERIFICANDO O MENOR VALOR
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
#VERIFICANDO O MAIOR VALOR
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O MAIOR VALOR É {}.'.format(maior))
print('O MENOR VALOR É {}.'.format(menor))
input('APERTE ENTER PARA FINALIZAR.')
