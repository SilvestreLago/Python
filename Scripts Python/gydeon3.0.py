print('POR FAVOR DIGITE TUDO EM LETRAS MAIUSCULAS, E SEM ACENTOS, OBRIGADO.')
print('OLA, MUITO PRAZER EM TE CONHECER, MEU NOME E GIDEON, QUAL O SEU NOME? ')
n1=input('QUAL O SEU NOME?')
print('OLA {} COMO JA MENCIONEI ANTERIORMENTE MEU NOME E GIDEON, SOU UM PROJETO'.format(n1))
print('AINDA EM DESENVOLVIMENTO, TENHO ALGUMAS FUNCOES QUE VOCE PODERA VER LOGO.')
n2=input('COMO VOCE ESTA SE SENTINDO HOJE {}? BEM, MAL, OU MAIS OU MENOS? '.format(n1))
if n2 == 'BEM':
    import random
    print('QUE BOM QUE VOCE ESTA SE SENTINDO BEM,')
    print('TENTE ESPALHAR ESSA FELICIDADE PARA OUTRAS PESSOAS TAMBEM.')
    input('APERTE ENTER PARA SABER UMA FRASE SOBRE A FELICIDADE!')
    # charle chaplin#
    n1 = str(
        'CERTA VEZ CHARLES CHAPLIN DISSE:\n ESTOU SEMPRE ALEGRE. ESSA E A MELHOR MANEIRA DE RESOLVER OS PROBLEMAS DA VIDA.')
    # carlos drumond de andrade#
    n2 = str(
        'CERTA VEZ CARLOS DRUMMOND DE ANDRADE DISSE:\n SER FELIZ SEM MOTIVO E A MAIS AUTENTICA FORMA DE FELICIDADE. ')
    # mahatma ganhdi#
    n3 = str('CERTA VEZ MAHATMA GANDHI DISSE:\n NAO EXTISTE UM CAMINHO PARA A FELICIDADE. A FELICIDADE E O CAMINHO. ')
    # dalai lama#
    n4 = str(
        'CERTA VEZDALAI LAMA DISSE:\n A FELICIDADE E UM ESTADO DE ESPIRITO. SE A SUA MENTE ESTIVER NUM ESTADO CONFUSO DE AGITACAO,\nOS BENS MATERIAS NAO VAO LHE PROPORCIONAR FELICIDADE.\n FELICIDADE SIGNIFICA PAZ DE ESPIRITO.')
    # jonh lennon#
    n5 = str(
        'CERTA VEZ JOHN LENNON DISSE:\n QUANDO EU FUI PARA A ESCOLA ME PERGUNTARAM OQUE EU QUERIA SER QUANDO CRESCESSE.\nEU ESCREVI FELIZ. ELES ME DISSERAM QUE EU NAO ENTENDI A TAREFA,\nE EU DISSE A ELES QUE ELES NAO ENTENDIAM A VIDA.')
    lista = [n1, n2, n3, n4, n5]
    escolha = random.choice(lista)
    print('{}'.format(escolha))
    input('APERTE ENTER PARA CONTINUAR!')
elif n2 == 'MAIS OU MENOS':
    import random

    print('ENTENDO AS VEZES NAO ESTAMOS NEM FELIZES NEM TRISTES.')
    print('MAS TENTE BUSCAR A FELICIDADE DE ALGUMA FORMA.')
    input('APERTE ENTER PARA SABER UMA FRASE SOBRE A FELICIDADE!')
    # charle chaplin#
    n1 = str(
        'CERTA VEZ CHAPLIN DISSE:\n ESTOU SEMPRE ALEGRE. ESSA E A MELHOR MANEIRA DE RESOLVER OS PROBLEMAS DA VIDA.')
    # carlos drumond de andrade#
    n2 = str(
        'CERTA VEZ CARLOS DRUMMOND DE ANDRADE DISSE:\n SER FELIZ SEM MOTIVO E A MAIS AUTENTICA FORMA DE FELICIDADE. ')
    # mahatma ganhdi#
    n3 = str(
        'CERTA VEZ MAHATMA GANDHI DISSE:\n NAO EXTISTE UM CAMINHO PARA A FELICIDADE. A FELICIDADE E O CAMINHO. ')
    # dalai lama#
    n4 = str(
        'CERTA VEZ DALAI LAMA DISSE:\n A FELICIDADE E UM ESTADO DE ESPIRITO. SE A SUA MENTE ESTIVER NUM ESTADO CONFUSO DE AGITACAO,\nOS BENS MATERIAS NAO VAO LHE PROPORCIONAR FELICIDADE.\n FELICIDADE SIGNIFICA PAZ DE ESPIRITO.')
    # jonh lennon#
    n5 = str(
        'CERTA VEZ JOHN LENNON DISSE:\n QUANDO EU FUI PARA A ESCOLA ME PERGUNTARAM OQUE EU QUERIA SER QUANDO CRESCESSE.\nEU ESCREVI FELIZ. ELES ME DISSERAM QUE EU NAO ENTENDI A TAREFA,\nE EU DISSE A ELES QUE ELES NAO ENTENDIAM A VIDA.')
    lista = [n1, n2, n3, n4, n5]
    escolha = random.choice(lista)
    print('{}'.format(escolha))
    input('APERTE ENTER PARA CONTINUAR!')
elif n2 == 'MAL':
    import random

    print(
        'ENTENDO, MUITAS VEZES NAO NOS SENTIMOS BEM, MAS NOS PRECISAMOS LEVANTAR A CABECA E PROCURAR UMA FORMA DE SAIR DA BAD.')
    print('A MELHOR COISA QUE TEMOS A FAZER E FALAR COM ALGUEM, TALVES UM AMIGO PARA DESABAFAR.')
    k1 = input('SE VOCE QUISER CONVERSAR DIGITE SIM! CASO CONTRARIO DIGITE NAO! ')
    if k1 == 'SIM':
        print(
            'COMO AINDA SOU UM PROTOTIPO EU AINDA NAO TENHO CAPACIDADE DE DESENVOLVER UMA CONVERSA, MAS VOCE PODE LIGAR PARA O CVV (CENTRO DE VALORIZACAO DE VIDA) ')
        print(
            'E UM NUMERO DE TELEFONE (188) COM PROPOSITO ANTI-SUICIDIO, PODE SER UM POUCO EXTREMO, MAS TENHO CERTEZA QUE ALGUEM CONVERSARA COM VOCE E QUEM SABE SE SENTIRA MELHOR!')
    if k1 == 'NAO':
        print(
            'ENTENDO QUE CONVERSAR COM UMA MAQUINA SERIA ESTRANHO, MAS SE VOCE ESTIVER SE SENTINDO MAL CONVERSE COM UM AMIGO, OU FAMILIAR, E CASO QUEIRA,')
        print(
            'VOCE PODE LIGAR PARA O CVV (CENTRO DE VVALORIZACAO DE VIDA) (188) PODE SER UM POUCO ESTRANHO EU SEI, MAS TAMBEM PODE AJUDAR!')
    input('APERTE ENTER PARA SABER UMA FRASE SOBRE A FELICIDADE!')
    # charle chaplin#
    n1 = str(
        'CERTA VEZ CHAPLIN DISSE:\n ESTOU SEMPRE ALEGRE. ESSA E A MELHOR MANEIRA DE RESOLVER OS PROBLEMAS DA VIDA.')
    # carlos drumond de andrade#
    n2 = str(
        'CERTA VEZ CARLOS DRUMMOND DE ANDRADE DISSE:\n SER FELIZ SEM MOTIVO E A MAIS AUTENTICA FORMA DE FELICIDADE. ')
    # mahatma ganhdi#
    n3 = str(
        'CERTA VEZ MAHATMA GANDHI DISSE:\n NAO EXTISTE UM CAMINHO PARA A FELICIDADE. A FELICIDADE E O CAMINHO. ')
    # dalai lama#
    n4 = str(
        'CERTA VEZ DALAI LAMA DISSE:\n A FELICIDADE E UM ESTADO DE ESPIRITO. SE A SUA MENTE ESTIVER NUM ESTADO CONFUSO DE AGITACAO,\nOS BENS MATERIAS NAO VAO LHE PROPORCIONAR FELICIDADE.\n FELICIDADE SIGNIFICA PAZ DE ESPIRITO.')
    # jonh lennon#
    n5 = str(
        'CERTA VEZ JOHN LENNON DISSE:\n QUANDO EU FUI PARA A ESCOLA ME PERGUNTARAM OQUE EU QUERIA SER QUANDO CRESCESSE.\nEU ESCREVI FELIZ. ELES ME DISSERAM QUE EU NAO ENTENDI A TAREFA,\nE EU DISSE A ELES QUE ELES NAO ENTENDIAM A VIDA.')
    lista = [n1, n2, n3, n4, n5]
    escolha = random.choice(lista)
    print('{}'.format(escolha))
    input('APERTE ENTER PARA CONTINURAR!')
n3=input('ENTAO {} AGORA EU GOSTARIA DE CONHECER VOCE UM POUCO MAIS, POSSO? SIM, OU NAO?')
if n3=='SIM':
    print('QUE BOM, VAMOS LA!')
    a111