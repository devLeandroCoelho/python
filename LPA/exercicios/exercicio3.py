# Leônidas é constantemente questionado sobre quantos soldados seus trezentos espartanos irão enfrentar.
# Ajude Leônidas fazendo um pequeno jogo de adivinhação em que o jogador deve dar um palpite, 
# caso seja abaixo ou acima do valor correto imprima mensagens adequadas informando o fato. (Valor correto deve ser: 10000)


valorCorreto = 10000

palpite = 0

while True:
    palpite = int(input(' Qual o valor, soldado?'))
    if (palpite == valorCorreto):
        print('Acerto Miseravii!!!')
        break
    elif(palpite < valorCorreto):
        print('É maior')
    elif(palpite > valorCorreto):
        print('É Menor')
    