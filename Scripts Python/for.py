n1=int(input('Quantas vezes deseja repetir? '))
for c in range (n1):
    if n1==1:
        print('Você quer que repita {} vez.'.format(n1))
    else:
        print('Você quer que repita {} vezes.'.format(n1))
print('FIM')
s=0
for c1 in range (n1):
    n2=int(input('Digite um número: '))
    s+=n2
print('O somatório de todos os númeres é igual à: {}'.format(s))