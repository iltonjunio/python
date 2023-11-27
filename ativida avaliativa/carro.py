custo_de_fabrica = float(input("Digite o custo de fábrica do carro: "))
categoria = input("Digite a categoria do veículo (utilitário, SUV ou caminhonete): ")

percentual_impostos = 0.45 * custo_de_fabrica

if categoria.lower() == "utilitário":
    margem_lucro = 0.20
elif categoria.lower() == "suv":
    margem_lucro = 0.25
elif categoria.lower() == "caminhonete":
    margem_lucro = 0.30
else:
    print("Categoria de veículo inválida.")
    exit()

custo_final = custo_de_fabrica + percentual_impostos + (custo_de_fabrica * margem_lucro)

print(f"O custo final ao consumidor é: R${custo_final:.2f}")
