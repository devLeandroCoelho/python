# exercício, solicitar ao usuário dois números inteiros. imprimir a soma desses dois números na tela.
x=int(input('digite um número '))
y=int(input('digite um segundo valor '))

# maneira clássica
res = int('o resultado da soma de ? com ? é igual a ?.' %(x, y, x + y))
print(res)
#maneira moderna
resp = int('a soma de {} com {} é igual a {}' .format(x, y, x + y))
print(resp)