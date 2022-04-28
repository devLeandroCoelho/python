while numeroatual != 0:
    numeroatual = float(input("digite um número diferente de 0 para prosseguir, ou 0 para encerrar a operação"))
    if numeroatual > maiornumero:
        maiornumero = numeroatual
    else:
        continue

print (f"o maior valor entre todos os digitados é {maiornumero}")