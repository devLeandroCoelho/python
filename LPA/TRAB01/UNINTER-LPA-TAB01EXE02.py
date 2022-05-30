<<<<<<< HEAD
##########################################################################################################
#                               Leandro Coelho - RU 3867885 (devLeandroCoelho)                           #
##########################################################################################################

#IMPORTANDO OS MODULOS e CONFIGURANDO
import locale 
locale.setlocale(locale.LC_ALL,'') 

# ARQUIVOS AUXILIARES DO CODIGO DO PRODUTO
cod1 = ('100')
cod2 = ('101')
cod3 = ('102')
cod4 = ('103')
cod5 = ('104')
cod6 = ('105')
cod7 = ('200')
cod8 = ('201')

# ARQUIVOS AUXILIARES DO NOME DO PRODUTO
prod1 = ('Cachorro Quente')
prod2 = ('Cachorro Quente Duplo')
prod3 = ('X-Egg')
prod4 = ('X-Salada')
prod5 = ('X-Bacon')
prod6 = ('X-Tudo')
prod7 = ('Refrigerante Lata')
prod8 = ('Chá Gelado')

# ARQUIVOS AUXILIARES DO VALOR DO PRODUTO
vlr1 = (9.00)
vlr2 = (11.00)
vlr3 = (12.00)
vlr4 = (12.00)
vlr5 = (14.00)
vlr6 = (17.00)
vlr7 = (5.00)
vlr8 = (4.00)

def menu():  # FUNÇÃO PARA IMPRIMIR O MENU DA LANCHONETE
    print('Bem vindo(a) a Lanchonete do Leandro Coelho - RU 3867885')
    print('*********************Cardápio********************')
    print('| Código |        Descrição        |    Valor   |')
    print('|  100   |     Cachorro Quente     |    9,00    |')
    print('|  101   |  Cachorro Quente Duplo  |   11,00    |')
    print('|  102   |          X-Egg          |   12,00    |')
    print('|  103   |         X-Salada        |   12,00    |')
    print('|  104   |         X-Bacon         |   14,00    |')
    print('|  105   |         X-Tudo          |   17,00    |')
    print('|  200   |     Refrigente Lata     |    5,00    |')
    print('|  201   |        Chá Gelado       |    4,00    |')
    print('*************************************************')

# INICIANDO / ZERANDO VARIAVEIS
totalPagar = 0.0
pedido = 1

# ESTRUTURA DE REPETIÇÃO
while pedido != 0:
    menu()  # EXIBINDO O MENU DA LANCHONETE
    prod = str(input('Entre com o código desejado:\n>> '))
    if prod == cod1:  # SE O CODIGO FOR 100
        totalPagar = totalPagar + vlr1  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod1} no valor de {locale.currency(vlr1)}')
    elif prod == cod2:  # SE O CODIGO FOR 101
        totalPagar = totalPagar + vlr2  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod2} no valor de {locale.currency(vlr2)}')
    elif prod == cod3:  # SE O CODIGO FOR 102
        totalPagar = totalPagar + vlr3  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod3} no valor de {locale.currency(vlr3)}')
    elif prod == cod4:  # SE O CODIGO FOR 103
        totalPagar = totalPagar + vlr4  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod4} no valor de {locale.currency(vlr4)}')
    elif prod == cod5:  # SE O CODIGO FOR 104
        totalPagar = totalPagar + vlr5  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod5} no valor de {locale.currency(vlr5)}')
    elif prod == cod6:  # SE O CODIGO FOR 105
        totalPagar = totalPagar + vlr6  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod6} no valor de {locale.currency(vlr6)}')
    elif prod == cod7:  # SE O CODIGO FOR 200
        totalPagar = totalPagar + vlr7  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod7} no valor de {locale.currency(vlr7)}')
    elif prod == cod8:  # SE O CODIGO FOR 201
        totalPagar = totalPagar + vlr8  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod8} no valor de {locale.currency(vlr8)}')
    else:
        print('******************\n'
              '* Opção invalida *\n'
              '******************')  # SE DIGITOU UMA OPÇÃO INVALIDA
        continue
    pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n>> '))
    if pedido == 1:  # SE DESEJA UM NOVO PRODUTO ELE VOLTA AO INICIO DO LAÇO DE REPETIÇÃO
        continue
    elif pedido == 0:  # SE NÃO DESEJA UM NOVO PRODUTO ELE FINALIZA INFORMANDO O TOTAL A PAGAR
        print(f'O total a ser pago é de {locale.currency(totalPagar)}')
=======
##########################################################################################################
#                               Leandro Coelho - RU 3867885 (devLeandroCoelho)                           #
##########################################################################################################

#IMPORTANDO OS MODULOS e CONFIGURANDO
import locale 
locale.setlocale(locale.LC_ALL,'') 

# ARQUIVOS AUXILIARES DO CODIGO DO PRODUTO
cod1 = ('100')
cod2 = ('101')
cod3 = ('102')
cod4 = ('103')
cod5 = ('104')
cod6 = ('105')
cod7 = ('200')
cod8 = ('201')

# ARQUIVOS AUXILIARES DO NOME DO PRODUTO
prod1 = ('Cachorro Quente')
prod2 = ('Cachorro Quente Duplo')
prod3 = ('X-Egg')
prod4 = ('X-Salada')
prod5 = ('X-Bacon')
prod6 = ('X-Tudo')
prod7 = ('Refrigerante Lata')
prod8 = ('Chá Gelado')

# ARQUIVOS AUXILIARES DO VALOR DO PRODUTO
vlr1 = (9.00)
vlr2 = (11.00)
vlr3 = (12.00)
vlr4 = (12.00)
vlr5 = (14.00)
vlr6 = (17.00)
vlr7 = (5.00)
vlr8 = (4.00)

def menu():  # FUNÇÃO PARA IMPRIMIR O MENU DA LANCHONETE
    print('Bem vindo(a) a Lanchonete do Leandro Coelho - RU 3867885')
    print('*********************Cardápio********************')
    print('| Código |        Descrição        |    Valor   |')
    print('|  100   |     Cachorro Quente     |    9,00    |')
    print('|  101   |  Cachorro Quente Duplo  |   11,00    |')
    print('|  102   |          X-Egg          |   12,00    |')
    print('|  103   |         X-Salada        |   12,00    |')
    print('|  104   |         X-Bacon         |   14,00    |')
    print('|  105   |         X-Tudo          |   17,00    |')
    print('|  200   |     Refrigente Lata     |    5,00    |')
    print('|  201   |        Chá Gelado       |    4,00    |')
    print('*************************************************')

# INICIANDO / ZERANDO VARIAVEIS
totalPagar = 0.0
pedido = 1

# ESTRUTURA DE REPETIÇÃO
while pedido != 0:
    menu()  # EXIBINDO O MENU DA LANCHONETE
    prod = str(input('Entre com o código desejado:\n>> '))
    if prod == cod1:  # SE O CODIGO FOR 100
        totalPagar = totalPagar + vlr1  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod1} no valor de {locale.currency(vlr1)}')
    elif prod == cod2:  # SE O CODIGO FOR 101
        totalPagar = totalPagar + vlr2  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod2} no valor de {locale.currency(vlr2)}')
    elif prod == cod3:  # SE O CODIGO FOR 102
        totalPagar = totalPagar + vlr3  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod3} no valor de {locale.currency(vlr3)}')
    elif prod == cod4:  # SE O CODIGO FOR 103
        totalPagar = totalPagar + vlr4  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod4} no valor de {locale.currency(vlr4)}')
    elif prod == cod5:  # SE O CODIGO FOR 104
        totalPagar = totalPagar + vlr5  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod5} no valor de {locale.currency(vlr5)}')
    elif prod == cod6:  # SE O CODIGO FOR 105
        totalPagar = totalPagar + vlr6  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod6} no valor de {locale.currency(vlr6)}')
    elif prod == cod7:  # SE O CODIGO FOR 200
        totalPagar = totalPagar + vlr7  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod7} no valor de {locale.currency(vlr7)}')
    elif prod == cod8:  # SE O CODIGO FOR 201
        totalPagar = totalPagar + vlr8  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod8} no valor de {locale.currency(vlr8)}')
    else:
        print('******************\n'
              '* Opção invalida *\n'
              '******************')  # SE DIGITOU UMA OPÇÃO INVALIDA
        continue
    pedido = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n>> '))
    if pedido == 1:  # SE DESEJA UM NOVO PRODUTO ELE VOLTA AO INICIO DO LAÇO DE REPETIÇÃO
        continue
    elif pedido == 0:  # SE NÃO DESEJA UM NOVO PRODUTO ELE FINALIZA INFORMANDO O TOTAL A PAGAR
        print(f'O total a ser pago é de {locale.currency(totalPagar)}')
>>>>>>> c776919b9bd023c0845ce08fa915e0430b5da8e5
        break