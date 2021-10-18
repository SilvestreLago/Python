n1=int(input('Digite um numero. '))
n2=int(input('Digite outro numero. '))
n3= n1+n2
print('A soma entre {} e {} é igua à {}.'.format(n1,n2,n3))
n4=input('Deseja repetir? ')
while n4=='sim':
    n1 = int(input('Digite um numero. '))
    n2 = int(input('Digite outro numero. '))
    n3 = n1 + n2
    print('A soma entre {} e {} é igua à {}.'.format(n1, n2, n3))
    n4 = input('Deseja repetir? ')
print('')