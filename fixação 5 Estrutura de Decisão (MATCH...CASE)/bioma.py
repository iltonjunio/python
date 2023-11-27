bioma= str(input("Digite o bioma que voce mora? "))
match bioma:
    case "amazônia":
        print("Acre, Amapá, Amazonas, Maranhão, Mato Grosso, Pará, Rondônia, Roraima, Tocantins")
    case "mata atlântica":
        print("Alagoas, Bahia, Espírito Santo, Goiás, Mato Grosso do Sul, Minas Gerais, Paraíba, Pernambuco, Rio de Janeiro ,Rio Grande do Norte, Rio Grande do Sul, Santa Catarina, São Paulo, Sergipe, Litígio Piauí-Ceará ")
    case "caatinga":
        print("Alagoas, Bahia, Ceará, Maranhão, Minas Gerais, Paraíba , Pernambuco, Piauí, Rio Grande do Norte, Sergipe, Litígio Piauí-Ceará ")
    case "cerrado":
        print("Bahia, Distrito Federal, Goiás, Maranhão,  Mato Grosso, Mato Grosso do Sul, Minas Gerais, Paraná, Piauí, Rondônia, São Paulo, Tocantins")
    case "pantanal":
        print("Mato Grosso, Mato Grosso do Sul")
    case "pampa":
        print("Rio Grande do Sul")
    case __:
        print("Estado incorreto")
