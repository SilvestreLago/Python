n1=int(input('A que velocidade você passou? '))
if n1>80:
    a2=(n1-80)*7
    print('VOCÊ FOI MULTADO EM R${} POR TER ULTRAPASSADO À {}KM/H, O LIMITE É DE 80KM/H. VOCÊ GANHOU MAIS 7 REAIS A CADA KM ACIMA DO LIMITE.'.format(a2,n1))
else:
    print('MEUS PARABÉNS VOCÊ NÃO FOI MULTADO')
print('--FIM--')
input('Para finalizar aperte ENTER.')
