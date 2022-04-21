import locale
locale.setlocale(locale.LC_ALL,'')
vlrProd = 0
vlrPagar = 0.0
qtdeProd = 0
vlrComDesc = 0.0
print('Bem Vindo a Loja do Leandro Prazeres Coelho - 3867885')
vlrProd = float(input('Qual o valor do produto?'))
qtdeProd = int(input('Qual a quantidade deste produto?'))
if qtdeProd < 10:
    vlrPagar = vlrProd * qtdeProd
elif 10 <= qtdeProd < 100:
    vlrPagar = vlrProd * qtdeProd
    vlrComDesc = vlrPagar - (vlrPagar*0.05)
elif 100 <= qtdeProd < 1000:
    vlrPagar = vlrProd * qtdeProd
    vlrComDesc = vlrPagar - (vlrPagar*0.10)
else:
    vlrPagar = vlrProd * qtdeProd
    vlrComDesc = vlrPagar - (vlrPagar*0.15)


vlrPagar = locale.currency(vlrPagar)
vlrComDesc = locale.currency(vlrComDesc)

print(f'Valor total a pagar sem desconto = {vlrPagar}')
print(f'Valor total a pagar com desconto = {vlrComDesc}')