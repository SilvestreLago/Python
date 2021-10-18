n1=float(input('DIGITE O PRIMEIRO VALOR. '))
n2=float(input('DIGITE O SEGUNDO VALOR. '))
n3=float(input('DIGITE O TERCEIRO VALOR. '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('É POSSIVEL FORMAR UM TRIANGULO.')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIANGULO.')
input('APERTE ENTER PARA FINALIZAR.')
