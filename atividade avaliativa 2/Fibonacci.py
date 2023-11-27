ultimo = 1
penultimo = 1

print("Números de Fibonacci entre 1 e 500:")
print(ultimo, end=' ')

while ultimo + penultimo <= 500:
    atual = ultimo + penultimo
    if atual <= 500:
        print(atual, end=' ')
    penultimo, ultimo = ultimo, atual

print()
