n1=int(input('DIGITE O PRIMEIRO VALOR: '))
n2=int(input('DIGITE O SEGUNDO VALOR: '))
print('OQUE VOCE DESEJA FAZER?')
print('[1] SOMAR OS NUMEROS: ')
print('[2] MULTIPLICAR OS NUMEROS: ')
print('[3] DIVIDIR OS NUMEROS: ')
print('[4] SUBTRAIR OS NUMEROS: ')
print('[5] DIGITAR OUTROS NUMEROS: ')
print('[6] FINALIZAR O PROGRAMA: ')
n3=input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
if n3=='1':
    print('VOCE CLICOU NO NUMERO 1: ')
    a1= n1+n2
    print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1,n2,a1))
elif n3=='2':
    print('VOCE CLICOU NO NUMERO 2: ')
    b1= n1*n2
    print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1,n2,b1))
elif n3=='3':
    print('VOCE CLICOU NO NUMERO 3:')
    c1=n1/n2
    print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1,n2,c1))
elif n3=='4':
    print('VOCE CLICOU NO NUMERO 4:')
    d1=n1-n2
    print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1,n2,d1))
while n3=='5':
    print('VOCE CLICOU NO NUMERO 5:')
    n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    n2 = int(input('DIGITE O SEGUNDO VALOR: '))
    print('OQUE VOCE DESEJA FAZER?')
    print('[1] SOMAR OS NUMEROS: ')
    print('[2] MULTIPLICAR OS NUMEROS: ')
    print('[3] DIVIDIR OS NUMEROS: ')
    print('[4] SUBTRAIR OS NUMEROS: ')
    print('[5] DIGITAR OUTROS NUMEROS: ')
    print('[6] FINALIZAR O PROGRAMA: ')
    n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
    if n3 == '1':
        print('VOCE CLICOU NO NUMERO 1: ')
        a1 = n1 + n2
        print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
    elif n3 == '2':
        print('VOCE CLICOU NO NUMERO 2: ')
        b1 = n1 * n2
        print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
    elif n3 == '3':
        print('VOCE CLICOU NO NUMERO 3:')
        c1 = n1 / n2
        print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
    elif n3 == '4':
        print('VOCE CLICOU NO NUMERO 4:')
        d1 = n1 - n2
        print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
    elif n3 == '6':
        print('VOCE CLICOU NO NUMERO 6:')
        input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
        quit()
if n3=='6':
    print('VOCE APERTOU O NUMERO 6')
    input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
    quit()
while n3!='1' and n3!='2' and n3!='4' and n3!='5' and n3!='6':
    print('ERRO, TENTE NOVAMENTE! ')
    n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    n2 = int(input('DIGITE O SEGUNDO VALOR: '))
    print('OQUE VOCE DESEJA FAZER?')
    print('[1] SOMAR OS NUMEROS: ')
    print('[2] MULTIPLICAR OS NUMEROS: ')
    print('[3] DIVIDIR OS NUMEROS: ')
    print('[4] SUBTRAIR OS NUMEROS: ')
    print('[5] DIGITAR OUTROS NUMEROS: ')
    print('[6] FINALIZAR O PROGRAMA: ')
    n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
    if n3 == '1':
        print('VOCE CLICOU NO NUMERO 1: ')
        a1 = n1 + n2
        print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
    elif n3 == '2':
        print('VOCE CLICOU NO NUMERO 2: ')
        b1 = n1 * n2
        print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
    elif n3 == '3':
        print('VOCE CLICOU NO NUMERO 3:')
        c1 = n1 / n2
        print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
    elif n3 == '4':
        print('VOCE CLICOU NO NUMERO 4:')
        d1 = n1 - n2
        print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
    while n3 == '5':
        print('VOCE CLICOU NO NUMERO 5:')
        n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        n2 = int(input('DIGITE O SEGUNDO VALOR: '))
        print('OQUE VOCE DESEJA FAZER?')
        print('[1] SOMAR OS NUMEROS: ')
        print('[2] MULTIPLICAR OS NUMEROS: ')
        print('[3] DIVIDIR OS NUMEROS: ')
        print('[4] SUBTRAIR OS NUMEROS: ')
        print('[5] DIGITAR OUTROS NUMEROS: ')
        print('[6] FINALIZAR O PROGRAMA: ')
        n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
        if n3 == '1':
            print('VOCE CLICOU NO NUMERO 1: ')
            a1 = n1 + n2
            print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
        elif n3 == '2':
            print('VOCE CLICOU NO NUMERO 2: ')
            b1 = n1 * n2
            print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
        elif n3 == '3':
            print('VOCE CLICOU NO NUMERO 3:')
            c1 = n1 / n2
            print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
        elif n3 == '4':
            print('VOCE CLICOU NO NUMERO 4:')
            d1 = n1 - n2
            print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
        elif n3 == '6':
            print('VOCE CLICOU NO NUMERO 6:')
            input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
            quit()
    if n3 == '6':
        print('VOCE APERTOU O NUMERO 6')
        input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
        quit()
z1=input('DESEJA REPETIR O PROGRAMA? S/N? ')
while z1=='S':
    n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
    n2 = int(input('DIGITE O SEGUNDO VALOR: '))
    print('OQUE VOCE DESEJA FAZER?')
    print('[1] SOMAR OS NUMEROS: ')
    print('[2] MULTIPLICAR OS NUMEROS: ')
    print('[3] DIVIDIR OS NUMEROS: ')
    print('[4] SUBTRAIR OS NUMEROS: ')
    print('[5] DIGITAR OUTROS NUMEROS: ')
    print('[6] FINALIZAR O PROGRAMA: ')
    n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
    if n3 == '1':
        print('VOCE CLICOU NO NUMERO 1: ')
        a1 = n1 + n2
        print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
    elif n3 == '2':
        print('VOCE CLICOU NO NUMERO 2: ')
        b1 = n1 * n2
        print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
    elif n3 == '3':
        print('VOCE CLICOU NO NUMERO 3:')
        c1 = n1 / n2
        print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
    elif n3 == '4':
        print('VOCE CLICOU NO NUMERO 4:')
        d1 = n1 - n2
        print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
    while n3 == '5':
        print('VOCE CLICOU NO NUMERO 5:')
        n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        n2 = int(input('DIGITE O SEGUNDO VALOR: '))
        print('OQUE VOCE DESEJA FAZER?')
        print('[1] SOMAR OS NUMEROS: ')
        print('[2] MULTIPLICAR OS NUMEROS: ')
        print('[3] DIVIDIR OS NUMEROS: ')
        print('[4] SUBTRAIR OS NUMEROS: ')
        print('[5] DIGITAR OUTROS NUMEROS: ')
        print('[6] FINALIZAR O PROGRAMA: ')
        n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
        if n3 == '1':
            print('VOCE CLICOU NO NUMERO 1: ')
            a1 = n1 + n2
            print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
        elif n3 == '2':
            print('VOCE CLICOU NO NUMERO 2: ')
            b1 = n1 * n2
            print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
        elif n3 == '3':
            print('VOCE CLICOU NO NUMERO 3:')
            c1 = n1 / n2
            print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
        elif n3 == '4':
            print('VOCE CLICOU NO NUMERO 4:')
            d1 = n1 - n2
            print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
        elif n3 == '6':
            print('VOCE CLICOU NO NUMERO 6:')
            input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
            quit()
    if n3 == '6':
        print('VOCE APERTOU O NUMERO 6')
        input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
        quit()
    while n3 != '1' and n3 != '2' and n3 != '4' and n3 != '5' and n3 != '6':
        print('ERRO, TENTE NOVAMENTE! ')
        n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        n2 = int(input('DIGITE O SEGUNDO VALOR: '))
        print('OQUE VOCE DESEJA FAZER?')
        print('[1] SOMAR OS NUMEROS: ')
        print('[2] MULTIPLICAR OS NUMEROS: ')
        print('[3] DIVIDIR OS NUMEROS: ')
        print('[4] SUBTRAIR OS NUMEROS: ')
        print('[5] DIGITAR OUTROS NUMEROS: ')
        print('[6] FINALIZAR O PROGRAMA: ')
        n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
        if n3 == '1':
            print('VOCE CLICOU NO NUMERO 1: ')
            a1 = n1 + n2
            print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
        elif n3 == '2':
            print('VOCE CLICOU NO NUMERO 2: ')
            b1 = n1 * n2
            print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
        elif n3 == '3':
            print('VOCE CLICOU NO NUMERO 3:')
            c1 = n1 / n2
            print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
        elif n3 == '4':
            print('VOCE CLICOU NO NUMERO 4:')
            d1 = n1 - n2
            print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
        while n3 == '5':
            print('VOCE CLICOU NO NUMERO 5:')
            n1 = int(input('DIGITE O PRIMEIRO VALOR: '))
            n2 = int(input('DIGITE O SEGUNDO VALOR: '))
            print('OQUE VOCE DESEJA FAZER?')
            print('[1] SOMAR OS NUMEROS: ')
            print('[2] MULTIPLICAR OS NUMEROS: ')
            print('[3] DIVIDIR OS NUMEROS: ')
            print('[4] SUBTRAIR OS NUMEROS: ')
            print('[5] DIGITAR OUTROS NUMEROS: ')
            print('[6] FINALIZAR O PROGRAMA: ')
            n3 = input('DIGITE O NUMERO DA FUNCAO QUE DESEJA REALIZAR: ')
            if n3 == '1':
                print('VOCE CLICOU NO NUMERO 1: ')
                a1 = n1 + n2
                print('A SOMA ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, a1))
            elif n3 == '2':
                print('VOCE CLICOU NO NUMERO 2: ')
                b1 = n1 * n2
                print('A MULTIPLICACAO DE {} E {} E IGUAL A {}.'.format(n1, n2, b1))
            elif n3 == '3':
                print('VOCE CLICOU NO NUMERO 3:')
                c1 = n1 / n2
                print('A DIVISAO ENTRE {} E {} E IGUAL A {:.2f}.'.format(n1, n2, c1))
            elif n3 == '4':
                print('VOCE CLICOU NO NUMERO 4:')
                d1 = n1 - n2
                print('A SUBTRACAO ENTRE {} E {} E IGUAL A {}.'.format(n1, n2, d1))
            elif n3 == '6':
                print('VOCE CLICOU NO NUMERO 6:')
                input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
                quit()
        if n3 == '6':
            print('VOCE APERTOU O NUMERO 6')
            input('APERTE ENTER PARA FINALIZAR O PROGRAMA: ')
            quit()
    z1 = input('DESEJA REPETIR O PROGRAMA? S/N? ')
