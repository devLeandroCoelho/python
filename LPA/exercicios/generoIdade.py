# Exercício Boa noite

# Faça um programa que repetidamente pergunte a idade e o gênero para o usuário. E para cada resposta o programa deve responder imprimir a mensagem:


# “Boa noite rapaz.” caso gênero masculino e idade < 18
# “Boa noite senhor.” caso gênero masculino e idade >= 18
# “Boa noite moça.” caso gênero feminino e idade < 18
# “Boa noite senhora.” caso gênero feminino e idade >=18

# Quando o usuário digitar 0 no campo idade o programa deve encerrar.

idade = 1000
genero = 'D'
while idade != 0:
    idade = int(input('Qual a sua idade?'))
    genero = str(input(' Digite o seu genero: M = Masculino e F = Feminino')).upper
    if genero != 'M' and genero != 'F':
        print(f'Você digitou: {genero} ... carecter diferente do solicitado (M ou F)')
    elif genero == 'M' and idade < 18:
        print('Boa noite rapaz.')
    elif genero == 'M' and idade >= 18:
        print('Boa noite senhor.')
    elif genero == 'F' and idade < 18:
        print('Boa noite moça.')
    elif genero == 'F' and idade >= 18:
        print('Boa noite senhora.')
    

