<<<<<<< HEAD
#IMPORTANDO OS MODULOS e CONFIGURANDO
import locale 
locale.setlocale(locale.LC_ALL,'') 

# INICIANDO AS VARIAVEIS
rotaObj = 0 # Variável para a rota do envio
pesObj = 0 # Variável para o peso do objeto
dimObj = 0 # Variável para dimensão do objeto

def bemVindo():# Função de identificação da empresa
    print('#' * 74) # escrito 74 vezes
    print('#                                                                        #')
    print('#          Bem vindo a LLC Ltda - Logística Leandro Coelho Ltda.         #')
    print('#                                                                        #')
    print('#                          Código RU 3867885                             #')
    print('#                                                                        #')
    print('#' * 74) # escrito 74 vezes
    print('Preencha os dados abaixo para obter o valor de envio da encomenda\n')
    

def dimensoesObjeto(): # Função que coleta as dimensões
    while True: # Loop para ficar repetindo até que seja acionado o break
        try:
            print('#' * 74) # escrito 74 vezes
            altura = float(input('Insira a altura do Objeto (em cm):\n>> '))
            break
        except ValueError:
            print('ERRO! Insira um valor numérico.')
            # Except para verificar se foi digitado um dado inválido
    while True:
        try:
            print('#' * 74) # escrito 74 vezes
            comprimento = float(input('Insira o comprimento do Objeto (em cm):\n>> '))
            break
        except ValueError:
            print('ERRO! Insira um valor numérico.')
            # try/except para verificar se foi digitado um dado inválido
    while True:
        try:
            print('#' * 74) # escrito 74 vezes
            largura = float(input('Insira a largura do Objeto (em cm):\n>> '))
            #Cálculo do volume do objeto
            volume = altura * comprimento * largura
            #variavel criada para apresentar o volume com ajuste de , e nao mais de .
            vol = locale.format_string('%.2f', volume)
            print('#' * 74) # escrito 74 vezes
            print(f'\nO volume do objeto é {vol} cm³\n')
            print('#' * 74) # escrito 74 vezes
            global dimObj # Variável global
            # verificação da opção desejada com IF e ELIF retornando os dados para a dimensão
            if volume <= 1000:
                vlr1 = 10 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr1 # Variável para fazer a atribuição dos dados
                break
            elif volume >= 1001 and volume <= 10000:
                vlr2 = 20 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr2
                break
            elif volume >= 10001 and volume <= 30000:
                vlr3 = 30 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr3
                break
            elif volume >= 30001 and volume <= 100000:
                vlr4 = 50 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr4
                break
            elif volume > 100000: # elif para informar que essa dimensão não é aceita e tentar novamente
                print('Não aceitamos objetos com as dimensões tão grandes.')
                print('Insira as informações novamente.')
                dimensoesObjeto()
                break
        except ValueError:
            # try/except para verificar se foi digitado um valor não valido
            print('ERRO! Insira um valor numérico.')

def pesoObjeto(): # Função para ler o peso
    while True:
        try:
            peso = float(input('Insira o peso do objeto (em kg):\n>> ')) #Leitura do Peso em KG
            print('#' * 74) # escrito 74 vezes
            global pesObj
            # verificação da opção desejada com IF e ELIF retornando os dados para o peso
            if peso <= 0.1:
                mult1 = 1 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult1
                break
            elif peso >= 0.11 and peso <= 1:
                mult2 = 1.5 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult2
                break
            elif peso >= 1.10 and peso <= 10:
                mult3 = 2 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult3
                break
            elif peso >= 10.1 and peso <= 30:
                mult4 = 3 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult4
                break
            else:
                print('Não aceitamos objetos tão pesados!')
                print('Insira o peso novamente.')
        except ValueError:
            print('ERRO! Insira um valor numérico.')
def rotaObjeto(): # Função das rotas do objeto
    while True:
        print('Selecione a rota:\n'
        'RS - De Rio de Janeiro até São Paulo\n'
        'SR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\n'
        'SB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\n'
        'RB - Rio de Janeiro até Brasília')
        rota = input('>> ').lower() # Caso seja digitada em maiúsculo, o lower transforma as letras em minúscula
        print('#' * 74) # escrito 74 vezes
        global rotaObj
        # Sequência de if e elif para verificar as rotas
        if rota == 'rs':
            rs = 1 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + rs # Variável para adicionar os dados a parâmetro global
            break
        elif rota == 'sr':
            sr = 1 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + sr
            break
        elif rota == 'bs':
            bs = 1.2 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + bs
            break
        elif rota == 'sb':
            sb = 1.2 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + sb
            break
        elif rota == 'br':
            br = 1.5 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + br
            break
        elif rota == 'rb':
            rb = 1.5 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + rb
            break
        else: # else para um possível código errado
            print('Essa rota não existe.\nInsira a rota novamente!')
bemVindo()
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
vlrFinal = dimObj * pesObj * rotaObj # Variável para fazer o cálculo do valor a ser pago
vlrFinal = locale.currency(vlrFinal) # Ajusta a apresentação do valor na moeda local
print(f'O valor a ser pago é: {vlrFinal} - Dimensões: {dimObj} * Peso: {pesObj} * Rota: {rotaObj})')
=======
#IMPORTANDO OS MODULOS e CONFIGURANDO
import locale 
locale.setlocale(locale.LC_ALL,'') 

# INICIANDO AS VARIAVEIS
rotaObj = 0 # Variável para a rota do envio
pesObj = 0 # Variável para o peso do objeto
dimObj = 0 # Variável para dimensão do objeto

def bemVindo():# Função de identificação da empresa
    print('#' * 74) # escrito 74 vezes
    print('#                                                                        #')
    print('#          Bem vindo a LLC Ltda - Logística Leandro Coelho Ltda.         #')
    print('#                                                                        #')
    print('#                          Código RU 3867885                             #')
    print('#                                                                        #')
    print('#' * 74) # escrito 74 vezes
    print('Preencha os dados abaixo para obter o valor de envio da encomenda\n')
    

def dimensoesObjeto(): # Função que coleta as dimensões
    while True: # Loop para ficar repetindo até que seja acionado o break
        try:
            print('#' * 74) # escrito 74 vezes
            altura = float(input('Insira a altura do Objeto (em cm):\n>> '))
            break
        except ValueError:
            print('ERRO! Insira um valor numérico.')
            # Except para verificar se foi digitado um dado inválido
    while True:
        try:
            print('#' * 74) # escrito 74 vezes
            comprimento = float(input('Insira o comprimento do Objeto (em cm):\n>> '))
            break
        except ValueError:
            print('ERRO! Insira um valor numérico.')
            # try/except para verificar se foi digitado um dado inválido
    while True:
        try:
            print('#' * 74) # escrito 74 vezes
            largura = float(input('Insira a largura do Objeto (em cm):\n>> '))
            #Cálculo do volume do objeto
            volume = altura * comprimento * largura
            #variavel criada para apresentar o volume com ajuste de , e nao mais de .
            vol = locale.format_string('%.2f', volume)
            print('#' * 74) # escrito 74 vezes
            print(f'\nO volume do objeto é {vol} cm³\n')
            print('#' * 74) # escrito 74 vezes
            global dimObj # Variável global
            # verificação da opção desejada com IF e ELIF retornando os dados para a dimensão
            if volume <= 1000:
                vlr1 = 10 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr1 # Variável para fazer a atribuição dos dados
                break
            elif volume >= 1001 and volume <= 10000:
                vlr2 = 20 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr2
                break
            elif volume >= 10001 and volume <= 30000:
                vlr3 = 30 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr3
                break
            elif volume >= 30001 and volume <= 100000:
                vlr4 = 50 # Variável com o valor do range de dimensão
                dimObj = dimObj + vlr4
                break
            elif volume > 100000: # elif para informar que essa dimensão não é aceita e tentar novamente
                print('Não aceitamos objetos com as dimensões tão grandes.')
                print('Insira as informações novamente.')
                dimensoesObjeto()
                break
        except ValueError:
            # try/except para verificar se foi digitado um valor não valido
            print('ERRO! Insira um valor numérico.')

def pesoObjeto(): # Função para ler o peso
    while True:
        try:
            peso = float(input('Insira o peso do objeto (em kg):\n>> ')) #Leitura do Peso em KG
            print('#' * 74) # escrito 74 vezes
            global pesObj
            # verificação da opção desejada com IF e ELIF retornando os dados para o peso
            if peso <= 0.1:
                mult1 = 1 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult1
                break
            elif peso >= 0.11 and peso <= 1:
                mult2 = 1.5 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult2
                break
            elif peso >= 1.10 and peso <= 10:
                mult3 = 2 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult3
                break
            elif peso >= 10.1 and peso <= 30:
                mult4 = 3 #Variavel com o Multiplicador do range de peso
                pesObj = pesObj + mult4
                break
            else:
                print('Não aceitamos objetos tão pesados!')
                print('Insira o peso novamente.')
        except ValueError:
            print('ERRO! Insira um valor numérico.')
def rotaObjeto(): # Função das rotas do objeto
    while True:
        print('Selecione a rota:\n'
        'RS - De Rio de Janeiro até São Paulo\n'
        'SR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\n'
        'SB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\n'
        'RB - Rio de Janeiro até Brasília')
        rota = input('>> ').lower() # Caso seja digitada em maiúsculo, o lower transforma as letras em minúscula
        print('#' * 74) # escrito 74 vezes
        global rotaObj
        # Sequência de if e elif para verificar as rotas
        if rota == 'rs':
            rs = 1 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + rs # Variável para adicionar os dados a parâmetro global
            break
        elif rota == 'sr':
            sr = 1 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + sr
            break
        elif rota == 'bs':
            bs = 1.2 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + bs
            break
        elif rota == 'sb':
            sb = 1.2 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + sb
            break
        elif rota == 'br':
            br = 1.5 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + br
            break
        elif rota == 'rb':
            rb = 1.5 #Variavel com o Multiplicador do range de rota
            rotaObj = rotaObj + rb
            break
        else: # else para um possível código errado
            print('Essa rota não existe.\nInsira a rota novamente!')
bemVindo()
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
vlrFinal = dimObj * pesObj * rotaObj # Variável para fazer o cálculo do valor a ser pago
vlrFinal = locale.currency(vlrFinal) # Ajusta a apresentação do valor na moeda local
print(f'O valor a ser pago é: {vlrFinal} - Dimensões: {dimObj} * Peso: {pesObj} * Rota: {rotaObj})')
>>>>>>> c776919b9bd023c0845ce08fa915e0430b5da8e5
print('#' * 74) # escrito 74 vezes