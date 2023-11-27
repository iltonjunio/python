votos_agnaldo = int(input("Digite o número de votos para Agnaldo: "))
votos_belmiro = int(input("Digite o número de votos para Belmiro: "))
votos_carlito = int(input("Digite o número de votos para Carlito: "))
votos_validos = int(input("Digite o número de votos válidos: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))

nome_agnaldo = "Agnaldo"
nome_belmiro = "Belmiro"
nome_carlito = "Carlito"

total_votos = votos_validos + votos_brancos + votos_nulos
percentual_brancos_nulos = (votos_brancos + votos_nulos) / total_votos * 100

if percentual_brancos_nulos > 25:
    votos_candidatos = {
        nome_agnaldo: votos_agnaldo,
        nome_belmiro: votos_belmiro,
        nome_carlito: votos_carlito,
    }
    
    primeiro_turno_vencedor = max(votos_candidatos, key=votos_candidatos.get)
    
    del votos_candidatos[primeiro_turno_vencedor]
    
    segundo_turno_candidato = max(votos_candidatos, key=votos_candidatos.get)

    print(f"Haverá segundo turno entre {primeiro_turno_vencedor} e {segundo_turno_candidato}.")
else:
    percentual_agnaldo = (votos_agnaldo / votos_validos) * 100
    percentual_belmiro = (votos_belmiro / votos_validos) * 100
    percentual_carlito = (votos_carlito / votos_validos) * 100

    if (
        percentual_agnaldo > percentual_belmiro
        and percentual_agnaldo > percentual_carlito
    ):
        print(nome_agnaldo, "é o vencedor da eleição.")
    elif (
        percentual_belmiro > percentual_agnaldo
        and percentual_belmiro > percentual_carlito
    ):
        print(nome_belmiro, "é o vencedor da eleição.")
    elif (
        percentual_carlito > percentual_agnaldo
        and percentual_carlito > percentual_belmiro
    ):
        print(nome_carlito, "é o vencedor da eleição.")



