import math
co=float(input('Comprimento do cateto opsoto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hi=math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
input('Apeerte ENTER para finalizar')
