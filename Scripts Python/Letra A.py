n1=str(input('Digite uma frase. '))
c1=n1.upper()
n2=c1.strip()
n3=c1.count('A')
n4=c1.find('A')
n5=n4+1
n6=c1.rfind('A')
n7=n6+1
print('A letra A aparece {} vezes na frase.'.format(n3))
print('A primeira letra A apareceu na posição {}.'.format(n5))
print('A última letra A apareceu na posição {}.'.format(n7))
