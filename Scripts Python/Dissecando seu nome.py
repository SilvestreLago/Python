n1=str(input('Digite seu nome. '))
a1=n1.upper()
a2=n1.lower()
b1=n1.split()
b2=b1[0]
c1=len(b1)
c2=n1.count(' ')
c3=len(n1)
c4=(c3-c2)
print('O seu nome em maiúsculas{}'.format(a1))
print('O seu nome em minúsculas{}'.format(a2))
print('O seu nome tem {} letras'.format(c4))
print('O seu primeiro nome é {} e ele tem {} letras'.format(b2,c1))

