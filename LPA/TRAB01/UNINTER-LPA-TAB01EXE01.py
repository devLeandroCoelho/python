#IMPORTANDO OS MODULOS e CONFIGURANDO
import locale 
locale.setlocale(locale.LC_ALL,'') 

#INICIALIZANDO AS VARIAVEIS
vlrProd = 0
vlrPagar = 0.0
qtdeProd = 0
vlrComDesc = 0.0

def menu (): # Função que contem o menu do app 
    print('Bem Vindo a Loja do Leandro Coelho - RU 3867885')
    print('###############################################')
    print('#            TABELA DE DESCONTO               #')
    print('#     QUANTIDADE    |         DESCONTO        #')
    print('#        até 9 un   |               0%        #')
    print('#      10 à 99 un   |               5%        #')
    print('#    100 à 999 un   |              10%        #')
    print('# mais de 1000 un   |              15%        #')
    print('###############################################')

menu() # Executa a função que exibe o menu

vlrProd = float(input('Qual o valor do produto?\n>> ')) # Questiona ao usuário o valor do Produto
qtdeProd = int(input('Qual a quantidade deste produto?\n>> ')) # Questiona ao usuário a quantidade de Produto
if qtdeProd < 10: # Verifica se a quantidade é entre 1 e 9
    vlrPagar = vlrProd * qtdeProd # Calcula valor a pagar sem desconto
    desconto = 'sem desconto aplicado'
elif 10 <= qtdeProd < 100: # Verifica se a quantidade é entre 10 e 99
    vlrPagar = vlrProd * qtdeProd # Calcula valor a pagar sem desconto
    vlrComDesc = vlrPagar - (vlrPagar*0.05) # Aplicadesconto de 05%
    desconto = 'desconto de 5%'
elif 100 <= qtdeProd < 1000: # Verifica se a quantidade é entre 100 e 999
    vlrPagar = vlrProd * qtdeProd # Calcula valor a pagar sem desconto
    vlrComDesc = vlrPagar - (vlrPagar*0.10) # Aplica desconto de 10%
    desconto = 'desconto de 10%'
else:  # Se nao atender nenhuma das anteriores 
    vlrPagar = vlrProd * qtdeProd # Calcula valor a pagar sem desconto
    vlrComDesc = vlrPagar - (vlrPagar*0.15) # Aplica desconto de 15%
    desconto = 'desconto de 15%'


vlrPagar = locale.currency(vlrPagar) # Ajusta a apresentação do valor na moeda local
vlrComDesc = locale.currency(vlrComDesc) # Ajusta a apresentação do valor na moeda local

print(f'Valor total a pagar sem desconto = {vlrPagar}') # Exibe na tela o valor sem desconto
print(f'Valor total a pagar com desconto = {vlrComDesc} ({desconto})') # Exibe na tela o valor com desconto