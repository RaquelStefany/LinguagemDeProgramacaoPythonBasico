def lernotas():
    n = float(input("Digite a Nota do Aluno(a): "))
    return n


def resultado(n1, n2):
    media = (n1 + n2) / 2

    print("\nNota 1: ", n1)
    print("Nota 2: ", n2)
    print("Media: ", media, "\n")

    if media >= 7:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")


a = lernotas()
b = lernotas()
resultado(a, b)