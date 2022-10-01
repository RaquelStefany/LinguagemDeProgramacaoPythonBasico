qtd = 0
soma = 0
media = 0
valor = float(input("Digote um valor: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1

    valor = float(input("Digite um valor: "))

# Se um numero negativo for digitado o programa será encerrado
media = soma / qtd

print("\nTotal da Soma: ", soma)
print("Quantidade de Valores Digitados: ", qtd)
print("Media dos Valores: ", media)