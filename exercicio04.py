nota = input("Escolha uma letra entre A, B, C, D, e F: ").upper()
match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case _:
        print("Não se Aplica. Escolha entre A, B, C, D e F")
    
