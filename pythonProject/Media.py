notaA = float(input("Informe a 1ª nota: "))
notaB = float(input("Informe a 2ª nota: "))

media = (notaA + notaB) / 2

if(media >= 7.0):
    print("\nAprovado - Media: %.1f" %media)
else:
    print("\nReprovado - Media: %1.f" %media)