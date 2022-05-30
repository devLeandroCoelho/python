pessoa1 = input("nome da pessoa 1:")
pessoa2 = input("nome da pessoa 2:")

if len(pessoa1) > len(pessoa2):
    print(f"{pessoa1} tem mais letras que {pessoa2}")
elif len(pessoa1) < len(pessoa2):
    print(f"{pessoa2} tem mais letras que {pessoa1}")
else:
    print(f"{pessoa1} e {pessoa2} tem a mesma quantidade de letras.")