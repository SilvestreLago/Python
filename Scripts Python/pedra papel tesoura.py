from random import randint
itens=('PEDRA', 'PAPEL', 'TESOURA')
computador=randint(0,2)
print('SUAS OPÇÕES:\n[0] PEDRA.\n[1] PAPEL.\n[2] TESOURA.')
n1=int(input('QUAL A SUA ESCOLHA? '))
print('COMPUTADOR JOGOU {}.'.format(itens[computador]))
print('JOGADOR JOGOU {}.'.format(itens[n1]))
if computador==0:
    if n1==0:
        print('EMPATE.')
    elif n1==1:
        print('VITÓRIA.')
    elif n1==2:
        print('DERROTA.')
    else:
        print('JOGADA INVÁLIDA.')
elif computador==1:
    if n1==0:
        print('DERROTA.')
    elif n1==1:
        print('EMPATE.')
    elif n1==2:
        print('VITÓRIA.')
    else:
        print('JOGADA INVÁLIDA.')
elif computador==2:
    if n1==0:
        print('DERROTA.')
    elif n1==1:
        print('VITÓRIA')
    elif n1==2:
        print('EMPATE.')
    else:
        print('JOGADA INVÁLIDA.')
input('APERTE ENTER PARA FINALIZAR.')
