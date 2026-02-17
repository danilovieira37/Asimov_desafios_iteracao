# Dado uma sequencia de numeros, calcule a soma e media dos numeros.
# ATENCAO: Nao vale usar a funcao sum() !

seq = []
resultado = ''
while not resultado == 'S' and not resultado == 'M':
    num = int(input('Digite um numero: '))
    seq.append(num)
    resultado = input('Digite A para adicionar mais um numero, S para somar ou M para media: ').upper()
if resultado == 'S':
    soma = 0
    for numero in seq:
        soma += numero
    print(f'A soma dos numeros é: {soma}')
else:
    soma = 0
    for numero in seq:
        soma += numero
    media = soma / len(seq)
    print(f'A media dos numeros é: {media}')
