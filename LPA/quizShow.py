import os # IMPORTAR A FUNÇÃO 'OS'
os.system('clear') or None # COMANDO PARA LIMPAR TELA

# O NOME CORRETO
esc = 'cpm22'
esc2 = 'cpm 22'

# MEU AMIGO GOSTA DE AMADO BATISTA FAZER O QUE? TIVE QUE USA-LO NÃO SÓ COMO HOMENAGEM MAS PARA O LOOPING INFINITO SE FORMAR
art = 'Amado Batista'

# CONTADOR PARA LANÇAR A DICA AUTOMATICAMENTE
cont = 9

#LOOP INFINITO PQ ELA NÃO IRÁ DESISTIR
while (True):
    # A PERGUNTA DA VEZ
    art = str(input('Qual o show você gostaria de assistir ou ter assistido?'))
    
    # TESTE PARA VER SE ACERTOU
    if (art == esc) or (art ==esc2):
        os.system('clear') or None
        print('Parabéns, você acertou! Esse é o show que iremos assistir!')
        break 
    
    # VAI UMA DICA ??
    elif (art == 'dica') or (cont == 0):
        os.system('clear') or None
        print('#### DICA ####\n')
        print('"Dias atrás"..."')
        print('...ou foi "Ontem" ???\n')
        print('será que só tinhamos apenas "1 minuto para o fim do mundo" ... ')
        print('... para assistir um show em uma "Tarde de Outubro" !\n')
        print('Ou seriam todas essas nomes de musicas???\n')
        cont = 1
        continue

    # DEIXANDO CLARO QUE TEM DICAS
    elif (art == 'desisto') or (cont <= 5):
        os.system('clear') or None
        print('Não desista, você pode pedir uma dica!\n')
        cont = cont -1
        continue
    # QUANDO ELA ERRA !
    else:
        os.system('clear') or None
        print('Não é esse o show que iremos ver... Tente novamente!!!\n')
        cont = cont -1
        continue