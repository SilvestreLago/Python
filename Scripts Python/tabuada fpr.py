n1=int(input('QUAL O NÚMERO VOCÊ QUER SABER A TABUADA? '))
for n1 in range(1):
    print(n1*2)
input('APERTE ENTER PARA CONTINUAR')
print('1-CALCULAR O ALUGUEL DE UM CARRO.')
print('2-APROVAR UM EMPRESTIMO.')
print('3-CALCULADORA.')
print('4-CATETO DA HIPOTENUSA.')
print('5-CONVERSOR DE TEMPERATURAS.')
print('6-ALISTAMENTO MILITAR. (2020)')
print('7-DESCOBRIR O ANO BISSEXTO.')
print('8-CALCULAR O IMC.')
print('9-CALCULAR A MEDIA.')
print('10-PAGAMENTOS.')
print('11-PASSAGEM.')
print('12-RADAR.')
print('13-REAJUSTE SALARIAL.')
print('14-TRIANGULO.')
print('15-JOKENPO.')
print('16-PORCENTAGEM DE UM PRODUTO.')
print('17-RAIZ QUADRADA.')
print('18-SENO COSSENO E TANGENTE.')
print('19-SORTEIO.')
print('20-TABUADA. (INDISPONIVEL)')
a1=input('GOSTARIA DE EXECUTAR ALGUMA TAREFA, SIM OU NAO? ')
if a1=="SIM":
    b1=input('INSIRA O NÚMERO DO PROGRAMA QUE DESEJA EXECUTAR: ')
    if b1=='1':
        n1 = int(input('Quantos dias o carro foi alugado? '))
        n2 = int(input('Quantos KM foram rodados? '))
        n3 = ((n1 * 60) + (n2 * 0.15))
        print('O valor usado foram de R$60,00 por dia e, R$0,15 por KM rodados!')
        print('O carro foi alugado por {} dias, rodou {} KM, no total ficou por R${}'.format(n1, n2, n3))
        input('Aperte ENTER para finalizar')
    if b1=='2':
        emprestimo = float(input('QUANTO DE EMPRÉSTIMO VOCÊ QUER PEGAR? R$'))
        salario = float(input('QUAL O SEU SALÁRIO? R$'))
        anos = int(input('EM QUANTOS ANOS VOCÊ PRETENDE PAGAR? '))
        prestação = emprestimo / (anos * 12)
        minimo = salario * 30 / 100
        print('PARA PEGAR UM EMPRESTIMO DE R${} EM {} ANOS, CADA PRESTAÇÃO SAIRÁ POR R${:.2f}'.format(emprestimo, anos,
                                                                                                      prestação))
        if prestação <= minimo:
            print('EMPRÉSTIMO APROVADO!')
        else:
            print('EMPRÉSTIMO NEGADO!')
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='3':
        s1 = int(input('Digite um número: '))
        s2 = int(input('Digite outro número: '))
        # Soma
        a = (s1 + s2)
        # Diminuição
        b = (s1 - s2)
        # Multiplicação
        c = (s1 * s2)
        # Divisão
        d = (s1 / s2)
        # Potência 1
        e = (s1 ** 2)
        # Potência 2
        f = (s2 ** 2)
        # Raiz quadrada 1
        g = (s1 ** 0.5)
        # Raiz quadrada 2
        h = (s2 ** 0.5)
        print('A soma entre {} e {} é igual à {}'.format(s1, s2, a))
        print('A subtração entre {} e {} é igual à {}'.format(s1, s2, b))
        print('A multiplicação entre {} e {} é igual à {}'.format(s1, s2, c))
        print('A divisão entre {} e {} é igual à {}'.format(s1, s2, d))
        print('O número {} elevado à 2 é igual à {}'.format(s1, e))
        print('O número {} elevado à 2 é igual à {}'.format(s2, f))
        print('A raiz quadrada de {} é igual à {}'.format(s1, g))
        print('A raiz quadrada de {} é igual à {}'.format(s2, h))
        input('Aperte ENTER para finalizar o programa')
    if b1=='4':
        n1 = float(input('Qual o comprimento do cateto oposto? '))
        n2 = float(input('Qual o comprimento do cateto adjacente? '))
        n3 = (n1 ** 2 + n2 ** 2) ** 0.5
        print('A hipotenusa é igual à {:.2f}.'.format(n3))
        input('Aperte ENTER para finalizar')
    if b1=='5':
        n1 = float(input('Quantos graus celsius estão? '))
        n2 = ((n1 * 9 / 5) + 32)
        print('A temperatura de {} graus celsius em fahrenheit são equivalentes à {}.'.format(n1, n2))
        input('Aperte ENTER para finalizar')
    if b1=='6':
        n1 = int(input('EM QUE ANO VOCÊ NASCEU? '))
        idade = 2020 - n1
        if idade < 18:
            a1 = (n1 + 18)
            print('VOCÊ TEM {} ANOS SEU ALISTAMENTO DEVERÁ SER REALIZADO EM {}.'.format(idade, a1))
        elif idade == 18:
            print('VOCÊ DEVE SE ALISTAR IMEDIATAMENTE.')
        elif idade > 18:
            a1 = (n1 + 18)
            print('VOCÊ TEM {} ANOS SEU ALISTAMENTO DEVERIA TER SIDO FEITO EM {}.'.format(idade, a1))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='7':
        from datetime import date
        ano = int(input('QUAL ANO QUER ANALIZAR? COLOQUE 0 PARA ANALIZAR O ANO ATUAL. '))
        if ano == 0:
            ano = date.today().year
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print('O ANO DE {} É BISSEXTO.'.format(ano))
        else:
            print('O ANO DE {} NÃO É BISSEXTO.'.format(ano))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='8':
        n1 = float(input('QUAL O SEU PESO? (KG) '))
        n2 = float(input('QUAL A SUA ALTURA? (M) '))
        # CALCULANDO O IMC
        n3 = n1 / (n2 * n2)
        print('O IMC DA PESSOA É DE {:.2f}.'.format(n3))
        if n3 < 18.5:
            print('ABAIXO DO PESO.')
        elif n3 > 18.5 and n3 < 24.9:
            print('PESO NORMAL.')
        elif n3 > 25 and n3 < 29.9:
            print('SOBREPESO.')
        elif n3 > 30 and n3 < 34.9:
            print('OBESIDADE GRAU 1.')
        elif n3 > 35 and n3 < 39.9:
            print('OBESIDADE GRAU 2.')
        elif n3 >= 40:
            print('OBESIDADE GRAU 3 OU MÓRBIDA.')
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='9':
        n1 = float(input('QUAL A PRIMEIRA NOTA? '))
        n2 = float(input('QUAL A SEGUNDA NOTA? '))
        n3 = (n1 + n2) / 2
        if n3 < 3.0 or n3 < 3:
            print('A MÉDIA DESSE ALENO É {} ELE PERDEU DE ANO.'.format(n3))
        elif n3 < 6.0 or n3 < 6:
            print('A MÉDIA DESSE ALUNO É {} ELE ESTÁ DE RECUPERAÇÃO.'.format(n3))
        elif n3 > 6.0 or n3 > 6:
            print('A MÉDIA DESSE ALUNO É {} ELE ESTÁ APROVADO.'.format(n3))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='10':
        n1 = float(input('PREÇO DAS COMPRAS. R$'))
        print(
            'FORMAS DE PAGAMENTO:\n[1] À VISTA DINHEIRO/CHEQUE.\n[2]À VISTA CARTÃO.\n[3]2X NO CARTÃO.\n[4] 3x OU MAIS NO CARTÃO.')
        n2 = int(input('QUAL A OPÇÃO DE PAGAMENTO? '))
        if n2 == 1 or n2 == 2:
            a1 = n1 * 0.10
            a2 = n1 - a1
            print('O VALOR A SER PAGO É DE R${} POIS PAGAMENTOS A VISTA TEM 10% DE DESCONTO.'.format(a2))
        elif n2 == 3:
            a1 = n1 * 0.10
            a2 = n1 + a1
            print('O VALOR A SER PAGO É DE R$ {} POIS PAGAMENTOS EM 2x NO CARTÃO TEM JUROS DE +10%.'.format(a2))
        elif n2 == 4:
            a1 = int(input('QUANTAS PARCELAS? '))
            a2 = n1 * 0.20
            a3 = n1 + a2
            a4 = a3 / a1
            print(
                'O VALOR A SER PAGO É DE R${} POR PARCELA, POIS OS PAGAMENTOS FEITOS EM {}x NO CARTÃO TEM JUROS DE +20%.'.format(
                    a4, a1))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='11':
        n1 = int(input('QUAL A DISTANCIA DA VIAGEM? '))
        if n1 >= 200:
            n2 = n1 * 0.45
            print('O VALOR DA PASSAGEM É DE R${}.'.format(n2))
        if n1 < 200:
            n3 = n1 * 0.5
            print('O VALOR DA PASSAGEM É DE R${}.'.format(n3))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='12':
        n1 = int(input('A que velocidade você passou? '))
        if n1 > 80:
            a2 = (n1 - 80) * 7
            print(
                'VOCÊ FOI MULTADO EM R${} POR TER ULTRAPASSADO À {}KM/H, O LIMITE É DE 80KM/H.\n VOCÊ GANHOU MAIS 7 REAIS A CADA KM ACIMA DO LIMITE.'.format(
                    a2, n1))
        else:
            print('MEUS PARABÉNS VOCÊ NÃO FOI MULTADO')
        print('--FIM--')
        input('Para finalizar aperte ENTER.')
    if b1=='13':
        n1 = float(input('QUAL O SALÁRIO DO FUNCIONÁRIO? R$'))
        if n1 >= 2000.00:
            n2 = n1 * 0.10
            n3 = n1 + n2
            print('O NOVO SALÁRIO DO FUNCIONÁRIO É R${}.'.format(n3))
        if n1 < 2000.00:
            n2 = n1 * 0.15
            n3 = n1 + n2
            print('O NOVO SALÁRIO DO FUNCIONÁRIO É R${}.'.format(n3))
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='14':
        n1 = float(input('DIGITE O PRIMEIRO SEGMENTO: '))
        n2 = float(input('DIGITE O SEGUNDO SEGMENTO: '))
        n3 = float(input('DIGITE O TERCEIRO SEGMENTO: '))
        if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
            print('É POSSÍVEL FORMAR UM TRIANGULO')
            if n1 == n2 == n3:
                print('EQUILÁTERO.')
            if n1 != n2 != n3 != n1:
                print('ESCALENO.')
            else:
                print('ISÓSCELES.')
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='15':
        from random import randint

        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        computador = randint(0, 2)
        print('SUAS OPÇÕES:\n[0] PEDRA.\n[1] PAPEL.\n[2] TESOURA.')
        n1 = int(input('QUAL A SUA ESCOLHA? '))
        print('COMPUTADOR JOGOU {}.'.format(itens[computador]))
        print('JOGADOR JOGOU {}.'.format(itens[n1]))
        if computador == 0:
            if n1 == 0:
                print('EMPATE.')
            elif n1 == 1:
                print('VITÓRIA.')
            elif n1 == 2:
                print('DERROTA.')
            else:
                print('JOGADA INVÁLIDA.')
        elif computador == 1:
            if n1 == 0:
                print('DERROTA.')
            elif n1 == 1:
                print('EMPATE.')
            elif n1 == 2:
                print('VITÓRIA.')
            else:
                print('JOGADA INVÁLIDA.')
        elif computador == 2:
            if n1 == 0:
                print('DERROTA.')
            elif n1 == 1:
                print('VITÓRIA')
            elif n1 == 2:
                print('EMPATE.')
            else:
                print('JOGADA INVÁLIDA.')
        input('APERTE ENTER PARA FINALIZAR.')
    if b1=='16':
        n1 = float(input('Qual o valor do item? R$'))
        n2 = float(input('(Em números decimais: EX: 20% 0.20) Quanto de desconto? '))
        n3 = (n1 * n2)
        n4 = (n1 - n3)
        print('Um item que custava R${} com {}% de desconto passou a custar R${}.'.format(n1, n3, n4))
        input('Aperte ENTER para finalizar')
    if b1=='17':
        import math

        num = int(input('Digite um número. '))
        raiz = math.sqrt(num)
        print('A raiz de {} é {:.2f}.'.format(num, raiz))
    if b1=='18':
        import math
        an = float(input('Digite o ângulo que você deseja. '))
        seno = math.sin(math.radians(an))
        print('O ângulo de {} tem o seno de {:.2f}.'.format(an, seno))
        cosseno = math.cos(math.radians(an))
        print('O ângulo de {} tem o cosseno de {:.2f}.'.format(an, cosseno))
        tangente = math.tan(math.radians(an))
        print('O ângulo de {} tem a tangente de {:.2f}.'.format(an, tangente))
        input('Aperte ENTER par finalizar')
    if b1=='19':
        import random

        n1 = str(input('Qual o primeiro nome? '))
        n2 = str(input('Qual o segundo nome? '))
        n3 = str(input('Qual o terceiro nome? '))
        n4 = str(input('Qual o quarto nome? '))
        lista = [n1, n2, n3, n4]
        escolhido = random.choice(lista)
        print('O escolhido foi {}.'.format(escolhido))
        input('Aperte ENTER para finaliar.')