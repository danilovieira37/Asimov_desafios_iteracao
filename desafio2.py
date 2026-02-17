# Dado uma sequencia de numeros, calcule a o maior valor da sequencia.
# ATENCAO: Nao vale usar a funcao max() !

lista: list = [10, 5, 3, 48, 2, 34]
maior = lista[0]
for num in lista:
    if num >= maior:
        maior = num
print(f'O maior numero da sequencia é {maior}.')