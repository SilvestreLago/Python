n1=float(input('DIGITE O PRIMEIRO SEGMENTO: '))
n2=float(input('DIGITE O SEGUNDO SEGMENTO: '))
n3=float(input('DIGITE O TERCEIRO SEGMENTO: '))
if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    print('É POSSÍVEL FORMAR UM TRIANGULO')
    if n1==n2==n3:
        print('EQUILÁTERO.')
    if n1!=n2!=n3!=n1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
input('APERTE ENTER PARA FINALIZAR.')
