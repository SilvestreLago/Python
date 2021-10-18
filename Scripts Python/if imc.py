n1=float(input('QUAL O SEU PESO? (KG) '))
n2=float(input('QUAL A SUA ALTURA? (M) '))
#CALCULANDO O IMC
n3=n1/(n2*n2)
print('O IMC DA PESSOA É DE {:.2f}.'.format(n3))
if n3<18.5:
    print('ABAIXO DO PESO.')
elif n3>18.5 and n3<24.9:
    print('PESO NORMAL.')
elif n3>25 and n3<29.9:
    print('SOBREPESO.')
elif n3>30 and n3<34.9:
    print('OBESIDADE GRAU 1.')
elif n3>35 and n3<39.9:
    print('OBESIDADE GRAU 2.')
elif n3>=40:
    print('OBESIDADE GRAU 3 OU MÓRBIDA.')
input('APERTE ENTER PARA FINALIZAR.')
