# INICIALIZANDO VARIAVEIS
listaPecas = []

# FUNÇÃO CADASTRO DE PEÇAS
def cadastrarPeca(cp):
    print('Você escolheu a opção "CADASTRAR PEÇAS"')
    print(f'O código da peça a ser cadastrada é: {cp}')
    # Coletando informações
    nome = str(input('Digite o nome da peça:\n>> '))
    fabricante = str(input('Digite o fabricante da peça:\n>> '))
    valor = float(input('Digite o valor da peça:\n>> '))
    # Criando dicionário
    dicionarioPeca = {'cp': cp,
                      'nome': nome,
                      'fabricante': fabricante,
                      'valor': valor}
    # Adicionando a lista no dicionário
    listaPecas.append(dicionarioPeca.copy())

# FUNÇÃO CONSULTA DE PEÇAS
def consultarPeca():
    while True:
        try:
            print('Você escolheu a opção "CONSULTAR PEÇAS"')
            opConsult = int(input('Entre com a opção desejada: \n'
                                  '1 - Consultar Todas as Peças \n'
                                  '2 - Consultar Peças por Códigos \n'
                                  '3 - Consultar Peças por Fabricante \n'
                                  '4 - Retornar.'
                                  '\n>> '))
            # Primeira condição = Consultar Peças
            if opConsult == 1:
                print('Você escolheu a opção "CONSULTAR TODAS AS PEÇAS"')
                # Selecionar cada dicionário da minha lista (lista de peças)
                for pecas in listaPecas:
                    for key, value in pecas.items():  # Seleciona cada chave e valor do dicionário
                        # imprime cada chave/valor
                        print('{} : {}'.format(key, value))
                    print('-' * 20)
            # Segunda condição = Consultar Peças por código
            elif opConsult == 2:
                print('Você escolheu a opção "CONSULTAR PEÇAS POR CÓDIGO"')
                entrada = int(input('Digite o Código da Peça:\n>> '))
                for pecas in listaPecas:
                    if(pecas['cp'] == entrada):  # Verifica se a peça é a mesma do codigo solicitado
                        for key, value in pecas.items():
                            # imprime a peça com codigo solicitado
                            print('{} : {}'.format(key, value))
                    print('-' * 20)
            # Terceira condição = Consultar Peças por fabricante
            elif opConsult == 3:
                print('Você escolheu a opção "CONSULTAR PEÇAS POR FABRICANTE"')
                entrada = (input('Digite o Fabricante da Peça:\n>> '))
                for pecas in listaPecas:
                    if(pecas['fabricante'] == entrada):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
                    print('-' * 20)
            # Quarta Opção = Encerra o laço while
            elif opConsult == 4:
                break
            else:
                print('Por favor, digite apenas as opções existentes no MENU.')
        # Tratamento possíveis de erros
        except ValueError:
            print('Você digitou uma opção inexistente!')

# FUNÇÃO REMOVER PEÇAS
def removerPeca():
    print('Você Selecionou a Opção REMOVER PEÇA: ')
    entrada = int(input('Digite o Código da Peça a ser removida:\n>> '))
    for pecas in listaPecas:  # Localizando as peças na lista criada
        if(pecas['cp'] == entrada):
            listaPecas.remove(pecas)  # Comando para remover a peça
            print(f'Peça de código {entrada} removida')
            break
        else:
            print(f'Peça de código {entrada} não encontrada')

# PROGRAMA PRINCIPAL
print('Leandro Coelho Bicicletaria LTDA. Código RU 3867885')
codigoProduto = 0
while True:  # Laço de repetição
    try:  # Comando para seleção de execussão das condições
        opcao = int(input('Digite a opção desejada:\n'
                          '1 - Cadastrar Peça\n'
                          '2 - Consultar Peça\n'
                          '3 - Remover Peça\n'
                          '4 - Sair\n'
                          '>> '))
        if opcao == 1:  # Condição para cadastro do produto
            codigoProduto = codigoProduto + 1  # Usado para acrescentar mais um
            cadastrarPeca(codigoProduto)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            break
        else:
            print('Opção inexistente, digite uma opção valida.')
            continue
    except ValueError:
        print('ERRO! Opção invalida.')