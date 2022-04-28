#LEIA O NOME E A QUANTIDADE DE VEZES QUE REPETE O NOME ESCRITO

nome =input('Seu nome?')
num = int(input('Quantas vezes?'))

for i in range(num):
    print(nome)
    
# i=0
# while i<num:
#     print(nome)
#     i +=1

#OU

# print((nome + '\n')* num)