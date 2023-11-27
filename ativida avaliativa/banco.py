numero_conta = input("Digite o número da conta do cliente: ")
saldo_conta = float(input("Digite o saldo atual da conta: "))

valor_transferencia = float(input("Digite o valor da transferência: "))
conta_destino = input("Digite o número da conta de destino: ")

if saldo_conta >= valor_transferencia:
    saldo_conta -= valor_transferencia
    print(f"Transferência de R${valor_transferencia:.2f} para a conta {conta_destino} realizada com sucesso.")
    print(f"Saldo atual da conta {numero_conta}: R${saldo_conta:.2f}")
else:
    print("Saldo insuficiente para realizar a transferência.")
