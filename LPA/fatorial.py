import math

# Fatorial

fat = 1
i = 1
num =  int(input('Digite o valor para fatorial: '))

while i <= num:
    fat *= i #fat = fat * i
    i += 1
print('Resposta: ', fat)

resposta = math.factorial(num)
print(resposta)