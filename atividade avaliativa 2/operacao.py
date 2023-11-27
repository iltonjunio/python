while True:
    print("Selecione a opção desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair do programa")
    
    opcao = input("Digite a opção: ")
    
    if opcao == '0':
        break 
    
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue 
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == '1':
        resultado = num1 + num2
    elif opcao == '2':
        resultado = num1 - num2
    elif opcao == '3':
        resultado = num1 * num2
    elif opcao == '4':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero.")
            continue 
        resultado = num1 / num2
    
    print("Resultado:", resultado)
