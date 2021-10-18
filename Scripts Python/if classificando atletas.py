n1=int(input('ANO DE NASCIMENTO. '))
n2=2020-n1
if n2>=20:
    print(' O ATLETA TEM {} ANOS.\n CLASSIFICAÇÃO: SÊNIOR.'.format(n2))
elif n2>=10:
    print(' O ATLETA TEM {} ANOS.\n CLASSIFICAÇÃO: JUNIOR.'.format(n2))
elif n2<=5:
    print(' O ATLETA TEM {} ANOS.\n CLASSIFICAÇÃO: MIRIM.'.format(n2))
input('APERTE ENTER PARA FINALIZAR.')
