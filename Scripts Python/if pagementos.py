n1=float(input('PREÇO DAS COMPRAS. R$'))
print('FORMAS DE PAGAMENTO:\n[1] À VISTA DINHEIRO/CHEQUE.\n[2]À VISTA CARTÃO.\n[3]2X NO CARTÃO.\n[4] 3x OU MAIS NO CARTÃO.')
n2=int(input('QUAL A OPÇÃO DE PAGAMENTO? '))
if n2==1 or n2==2:
    a1=n1*0.10
    a2=n1-a1
    print('O VALOR A SER PAGO É DE R${} POIS PAGAMENTOS A VISTA TEM 10% DE DESCONTO.'.format(a2))
elif n2==3:
    a1=n1*0.10
    a2=n1+a1
    print('O VALOR A SER PAGO É DE R$ {} POIS PAGAMENTOS EM 2x NO CARTÃO TEM JUROS DE +10%.'.format(a2))
elif n2==4:
    a1=int(input('QUANTAS PARCELAS? '))
    a2=n1*0.20
    a3=n1+a2
    a4=a3/a1
    print('O VALOR A SER PAGO É DE R${} POR PARCELA, POIS OS PAGAMENTOS FEITOS EM {}x NO CARTÃO TEM JUROS DE +20%.'.format(a4,a1))
input('APERTE ENTER PARA FINALIZAR.')
