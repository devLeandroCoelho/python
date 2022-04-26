esc = 'cpm22'
esc2 = 'cpm 22'
art = 'oi'
cont = 3
while (art != 'desisto'):
    art = str(input('Qual o show você gostaria de assistir ou ter assistido?'))
    if (art == esc) or (art ==esc2):
        print('Parabéns, você acertou! Esse é o show que iremos assistir!')
        break
    elif (art == 'dica') or (cont == 0):
        print('DICA BONUS!!!')
        print('"Dias atrás" ou foi "Ontem"')
        print('... tinhamos apenas "1 minuto para o fim do mundo"')
        print('para assistir um show em uma "Tarde de Outubro" !')
        cont = 1
        continue
    else:
        print('Não é esse o show que iremos ver... Tente novamente!!!')
        cont = cont -1
        continue


