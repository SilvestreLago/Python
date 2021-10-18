n1=float(input('QUAL A PRIMEIRA NOTA? '))
n2=float(input('QUAL A SEGUNDA NOTA? '))
n3=(n1+n2)/2
if n3<3.0 or n3<3:
    print('A MÉDIA DESSE ALENO É {} ELE PERDEU DE ANO.'.format(n3))
elif n3<6.0 or n3<6:
    print('A MÉDIA DESSE ALUNO É {} ELE ESTÁ DE RECUPERAÇÃO.'.format(n3))
elif n3>6.0 or n3>6:
    print('A MÉDIA DESSE ALUNO É {} ELE ESTÁ APROVADO.'.format(n3))
input('APERTE ENTER PARA FINALIZAR.')
