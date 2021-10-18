n1=int(input('DIGITE UM NÚMERO '))
print('ESCOLHA A BASE DE CONVERSÃO.')
n2=input(' APERTE [1] PARA CONVERTE PARA BINÁRIO.\n APERTE [2] PARA CONVERTE PARA OCTAL.\n APERTE [3] PARA CONVERTER PARA HEXADECIMAL.\n SUA OPÇÃO: ')
if n2=='1':
    print('{} CONVERTIDO PARA BINÁRIO É {}.'.format(n1,bin(n1)))
elif n2=='2':
    print('{} CONVERTIDO PARA OCATL É {}.'.format(n1,oct(n1)))
elif n2=='3':
    print('{} CONVERTIDO PARA HEXADECIMAL É {}.'.format(n1,hex(n1)))
else:
    print('SINTO MUITO VOCÊ DIGITOU UM NÚMERO INVÁLIDO.')
input('APERTE ENTER PARA FINALIZAR.')
