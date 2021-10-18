n1=int(input('EM QUE ANO VOCÊ NASCEU? '))
idade=2020-n1
if idade<18:
    a1=(n1+18)
    print('VOCÊ TEM {} ANOS SEU ALISTAMENTO DEVERÁ SER REALIZADO EM {}.'.format(idade,a1))
elif idade==18:
    print('VOCÊ DEVE SE ALISTAR IMEDIATAMENTE.')
elif idade>18:
    a1=(n1+18)
    print('VOCÊ TEM {} ANOS SEU ALISTAMENTO DEVERIA TER SIDO FEITO EM {}.'.format(idade,a1))
input('APERTE ENTER PARA FINALIZAR.')
