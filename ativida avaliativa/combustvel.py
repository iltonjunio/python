
preco_gasolina = 5.95
preco_alcool = 3.10

litros_abastecidos = float(input("Digite o total de litros abastecidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool ou G para gasolina): ")

if tipo_combustivel.upper() == "A":
    if litros_abastecidos <= 20:
        valor_a_pagar = litros_abastecidos * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_a_pagar = litros_abastecidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel.upper() == "G":
    if litros_abastecidos <= 20:
        valor_a_pagar = litros_abastecidos * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_a_pagar = litros_abastecidos * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print("Tipo de combustível inválido.")
    exit()

print(f"O valor a ser pago pelo cliente é: R${valor_a_pagar:.2f}")
