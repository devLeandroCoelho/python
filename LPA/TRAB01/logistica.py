from pickle import TRUE


def showMenu(nomeMenu):
    if nomeMenu == "dim":
        altura = "1,00"
        while (altura.isdigit()):
            altura = input('Digite a altura do produto (em cm)')
        comprimento = float(input('Digite o comprimento do produto (em cm)'))
        largura = float(input('Digite a largura do produto (em cm)'))
showMenu('dim')