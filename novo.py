#############################################################################################
# CODIGO ELABORADO COM VSCODE POR LEANDRO COELHO (devLeandroCoelho) e LUCIANO SILVA         #
# TODOS OS DIREITOS DE USO DESTE CODIGO DEVEM SER COMUNICADOS AOS RESPECTIVOS CODIFICADORES #
#############################################################################################

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
    print('Bem vindo(a) a Lanchonete do Luciano da Silva')
    print('*******************Cardápio******************')
    print('| Código |        Descrição        |    Valor   |')
    print('|  100   |     Cachorro Quente     |    9,00    |')
    print('|  101   |  Cachorro Quente Duplo  |   11,00    |')
    print('|  102   |          X-Egg          |   12,00    |')
    print('|  103   |         X-Salada        |   12,00    |')
    print('|  104   |         X-Bacon         |   14,00    |')
    print('|  105   |         X-Tudo          |   17,00    |')
    print('|  200   |     Refrigente Lata     |    5,00    |')
    print('|  201   |        Chá Gelado       |    4,00    |')


# INICIANDO / ZERANDO VARIAVEIS
totalPagar = 0.0
pedido = 1

# ESTRUTURA DE REPETIÇÃO
while pedido != 0:
    menu()  # EXIBINDO O MENU DA LANCHONETE
    prod = str(input('Entre com o código desejado: '))
    if prod == cod1:  # SE O CODIGO FOR 100
        totalPagar = totalPagar + vlr1  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod1} no valor de {vlr1}')
    elif prod == cod2:  # SE O CODIGO FOR 101
        totalPagar = totalPagar + vlr2  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod2} no valor de {vlr2}')
    elif prod == cod3:  # SE O CODIGO FOR 102
        totalPagar = totalPagar + vlr3  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod3} no valor de {vlr3}')
    elif prod == cod4:  # SE O CODIGO FOR 103
        totalPagar = totalPagar + vlr4  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod4} no valor de {vlr4}')
    elif prod == cod5:  # SE O CODIGO FOR 104
        totalPagar = totalPagar + vlr5  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod5} no valor de {vlr5}')
    elif prod == cod6:  # SE O CODIGO FOR 105
        totalPagar = totalPagar + vlr6  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod6} no valor de {vlr6}')
    elif prod == cod7:  # SE O CODIGO FOR 200
        totalPagar = totalPagar + vlr7  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod7} no valor de {vlr7}')
    elif prod == cod8:  # SE O CODIGO FOR 201
        totalPagar = totalPagar + vlr8  # SOMA AO TOTAL A PAGAR O VALOR DO NOVO PRODUTO
        print(f'Você escolheu um {prod8} no valor de {vlr8}')
    else:
        print('Opção invalida')  # SE DIGITOU UMA OPÇÃO INVALIDA
    print('Deseja pedir mais alguma coisa? ')
    print('1 - Sim')
    print('0 - Não')
    pedido = int(input())
    if pedido == 1:  # SE DESEJA UM NOVO PRODUTO ELE VOLTA AO INICIO DO LAÇO DE REPETIÇÃO
        continue
    elif pedido == 0:  # SE NÃO DESEJA UM NOVO PRODUTO ELE FINALIZA INFORMANDO O TOTAL A PAGAR
        print(f'O total a ser pago é de R$ {totalPagar}')
        break
