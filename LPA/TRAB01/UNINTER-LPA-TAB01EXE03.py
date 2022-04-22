from pickle import FALSE, TRUE
altura = 0.00
a = TRUE
multi = 0.0
volume = 0.0
def dimensoesObejto():
    try:
        altura = float(input('Digite a altura do produto (em cm)'))
        comprimento = float(input('Digite o comprimeto do produto (em cm)'))
        largura = float(input('Digite a largura do produto (em cm)'))
        volume = altura * comprimento * largura
        return volume
    except ValueError: 
        print('ERRO!!! Digite um valor númérico!')
        dimensoesObejto()
def pesoObejto():
    try:
        peso = float(input('Digite o peso do produto (em kg)'))
        return peso
        if peso < 0.1: 
            multi = 1            
        elif 0.1 < peso <= 1: 
            multi = 1.5
        elif 1 < peso <= 10: 
            multi = 2
        elif 10 < peso <= 30: 
            multi = 1.5
        elif peso > 30: 
            print('Permitido apenas peso até 30 kg, preencha novamente')
            pesoObejto()
    except ValueError: 
        print('ERRO!!! Digite um valor númérico!')
        pesoObejto()
print(volume)
dimensoesObejto()
pesoObejto()