barras = int(input("Digite a quantidade de barras de chocolate: "))
valor_total = 0

if barras >= 3:
    promo_3_barras = barras // 3
    valor_total += promo_3_barras * 10
    quantidade_barras_restantes = barras % 3
    valor_total += quantidade_barras_restantes * 4
else:
    valor_total = barras * 4
print(f"O valor a ser pago é: R${valor_total:.2f}")

# --------------------------------------------------
# n = int(input("informe a quantidade a ser comprado de barras de chocolate:" ))
# if n % 3 == 0:
#     valor = n * 10/3
#     print("o valor a ser pago é ", format(valor, "2f"),"reais")
# else:
#     valor = (n - n%3) * 10/3 + 4 (n%3)
#     print("O valor a ser pago é", format(valor, ".2f"), "reais")
# ------------------------------------------------------------------
# barras = int(input("Digite a quantidade de barras de chocolate: "))
# valor = 0

# valor += barras // 3 * 10
# valor += barras % 3 * 4
# print(valor)