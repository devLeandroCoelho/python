import os
os.system('clear') or None
esc = 'cpm22'
esc2 = 'cpm 22'
art = 'Amado Batista'
cont = 9
while (art != 'desisto'):
    art = str(input('Qual o show você gostaria de assistir ou ter assistido?'))
    if (art == esc) or (art ==esc2):
        os.system('clear') or None
        print('Parabéns, você acertou! Esse é o show que iremos assistir!')
        break
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
    elif (art == 'desisto') or (cont <= 5):
        os.system('clear') or None
        print('Não desista, você pode pedir uma dica!\n')
        cont = cont -1
        continue
    else:
        os.system('clear') or None
        print('Não é esse o show que iremos ver... Tente novamente!!!\n')
        cont = cont -1
        continue


