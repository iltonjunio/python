nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3.0

conceito = ""
if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.5:
    conceito = "C"
else:
    conceito = "D"

print(f"A média do aluno é {media:.2f}, e seu conceito é {conceito}.")
