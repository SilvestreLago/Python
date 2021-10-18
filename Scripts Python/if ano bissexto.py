from datetime import date
ano=int(input('QUAL ANO QUER ANALIZAR? COLOQUE 0 PARA ANALIZAR O ANO ATUAL. '))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ANO DE {} É BISSEXTO.'.format(ano))
else:
    print('O ANO DE {} NÃO É BISSEXTO.'.format(ano))
input('APERTE ENTER PARA FINALIZAR.')
