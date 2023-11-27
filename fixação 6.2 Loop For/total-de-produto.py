produto = int(input("Informe o total de produtos? " ))
n = 0
for i in range(produto):
    preco = float(input("Digite o preço? "))
    n += preco
    print(n)

