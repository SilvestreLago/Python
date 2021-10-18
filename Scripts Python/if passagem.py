n1=int(input('QUAL A DISTANCIA DA VIAGEM? '))
if n1>=200:
    n2=n1*0.45
    print('O VALOR DA PASSAGEM É DE R${}.'.format(n2))
if n1<200:
    n3=n1*0.5
    print('O VALOR DA PASSAGEM É DE R${}.'.format(n3))
input('APERTE ENTER PARA FINALIZAR.')
