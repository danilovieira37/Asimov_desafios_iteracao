# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras: list = ['Mama', 'Largatixa', 'Doce', 'Cara', 'Fil']
for palavra in palavras:
    if len(palavra) <= 5:
        print(palavra)