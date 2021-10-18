import random
n1=int(input('Escolha um número de 0 à 5. '))
n2=[0,1,2,3,4,5]
n3=random.choice(n2)
if n1==n3:
    print('Meus parabéns você acertou, o número escolhido foi {}.'.format(n3))
else:
    print('Sinto muito, você escolheu o número {}, o escolhido aleatoriamento foi {}.'.format(n1,n3))
input('Para jogar de novo abra novamente o programa, para fechar o abreto aperte ENTER.')
