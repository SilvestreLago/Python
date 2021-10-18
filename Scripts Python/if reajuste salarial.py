n1=float(input('QUAL O SALÁRIO DO FUNCIONÁRIO? R$'))
if n1>=2000.00:
    n2=n1*0.10
    n3=n1+n2
    print('O NOVO SALÁRIO DO FUNCIONÁRIO É R${}.'.format(n3))
if n1<2000.00:
    n2=n1*0.15
    n3=n1+n2
    print('O NOVO SALÁRIO DO FUNCIONÁRIO É R${}.'.format(n3))
input('APERTE ENTER PARA FINALIZAR.')
